from config_manager import (
    TEMPERATURE,
    TOP_P,
    TOP_K,
    MAX_TOKENS
)

def chat_with_model(client, messages, tools=None, tool_choice="auto"):
    kwargs = {
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_tokens": MAX_TOKENS,
        "top_k": TOP_K  # Only used by OpenAI-compatible models
    }

    # Clean out None values to avoid passing unsupported args
    kwargs = {k: v for k, v in kwargs.items() if v is not None}

    return client.chat(
        messages=messages,
        tools=tools,
        tool_choice=tool_choice,
        **kwargs
    )
