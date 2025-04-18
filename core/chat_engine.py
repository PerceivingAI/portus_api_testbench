from config_manager import (
    TEMPERATURE,
    TOP_P,
    TOP_K,
    MAX_TOKENS,
    PROVIDER_NAME,
    BASE_URL,
    STREAM
)

from portus_context_module.context_manager import ContextManager
from portus_context_module.context_adapters import to_openai_format, to_gemini_native_format

# Global context instance (per run/session)
context = ContextManager()

# Determine format style based on endpoint
USING_OPENAI_STYLE = "openai" in BASE_URL.lower()

def chat_with_model(client, messages, tools=None, tool_choice="auto"):
    # Step 1: Add user message(s) to context
    for msg in messages:
        print(f"[chat_engine] ➕ Sending to context: {msg}")
        context.add_turn(msg["role"], msg["content"])

    # Step 2: Convert full context history to appropriate format
    formatted_history = (
        to_openai_format(context.get_history())
        if USING_OPENAI_STYLE
        else to_gemini_native_format(context.get_history())
    )

    # Step 3: Prepare generation parameters
    kwargs = {
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_tokens": MAX_TOKENS,
        "top_k": TOP_K,
        "tools": tools,
        "tool_choice": tool_choice,
    }
    kwargs = {k: v for k, v in kwargs.items() if v is not None}

    # Step 4: Stream or return full response
    if STREAM:
        assistant_reply = ""

        def token_generator():
            nonlocal assistant_reply
            response = client.chat(messages=formatted_history, **kwargs)
            for chunk in response:
                delta = chunk.choices[0].delta
                if hasattr(delta, "content") and delta.content:
                    token = delta.content
                    assistant_reply += token
                    yield token
            context.add_turn("assistant", assistant_reply)

        return token_generator()

    else:
        response = client.chat(messages=formatted_history, **kwargs)
        assistant_reply = response.choices[0].message.content
        context.add_turn("assistant", assistant_reply)
        return assistant_reply
