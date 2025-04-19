from openai import OpenAI
import httpx

class GeminiClient:
    def __init__(self, api_key, model, base_url, stream=False):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        self.stream = stream
        http_client = httpx.Client()
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url, http_client=http_client)

    def chat(self, messages, tools=None, tool_choice="auto", **kwargs):
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=self.stream,
            tools=tools,
            tool_choice=tool_choice,
            **kwargs
        )