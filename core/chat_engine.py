def chat_with_model(client, messages, tools=None, tool_choice="auto", **kwargs):
    return client.chat(
        messages=messages,
        tools=tools,
        tool_choice=tool_choice,
        **kwargs
    )
