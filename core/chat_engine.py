from config_manager import get_parameters

def chat_with_model(client, messages, tools=None, tool_choice="auto"):
    params = get_parameters()

    # Build kwargs only if values are not None
    kwargs = {
        "temperature": params.get("temperature"),
        "top_p": params.get("top_p"),
        "max_tokens": params.get("max_tokens"),
        "top_k": params.get("top_k")  # Only present for OpenAI
    }

    # Remove keys with None values to avoid passing unsupported params
    kwargs = {k: v for k, v in kwargs.items() if v is not None}

    return client.chat(
        messages=messages,
        tools=tools,
        tool_choice=tool_choice,
        **kwargs
    )
