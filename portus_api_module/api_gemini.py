from openai import OpenAI

class GeminiClient:
    def __init__(self, api_key, model, base_url, stream=False):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        self.stream = stream
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)


    def chat(self, messages, tools=None, tool_choice="auto", **kwargs):
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=self.stream,
            tools=tools,
            tool_choice=tool_choice,
            **kwargs
        )
