# api_module/api_gemini.py

from openai import OpenAI

class GeminiClient:
    def __init__(self, api_key, model, base_url):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def chat(self, messages, stream=False, tools=None, tool_choice="auto", **kwargs):
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=stream,
            tools=tools,
            tool_choice=tool_choice,
            **kwargs
        )
