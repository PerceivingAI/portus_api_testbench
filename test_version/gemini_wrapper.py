# gemini_wrapper.py
from openai import OpenAI
import os

class GeminiClient:
    def __init__(self, api_key=None, model="gemini-2.0-flash", base_url="https://generativelanguage.googleapis.com/v1beta/openai/"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key not provided and GEMINI_API_KEY not set in environment.")
        self.model = model
        self.client = OpenAI(api_key=self.api_key, base_url=base_url)

    def chat(self, messages, stream=False, tools=None, tool_choice="auto", **kwargs):
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=stream,
            tools=tools,
            tool_choice=tool_choice,
            **kwargs
        )

    def list_models(self):
        return self.client.models.list()

    def retrieve_model(self, model_id):
        return self.client.models.retrieve(model_id)

    def embeddings(self, input_text, model="text-embedding-004"):
        return self.client.embeddings.create(
            input=input_text,
            model=model
        )
