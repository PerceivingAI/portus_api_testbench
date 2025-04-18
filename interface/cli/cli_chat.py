import os
from dotenv import load_dotenv

from core.chat_engine import chat_with_model
from config_manager import STREAM, PROVIDER_NAME
from api_module.api_factory import get_client

load_dotenv()

def run_chat_mode():
    api_key = os.getenv(f"{PROVIDER_NAME.upper()}_API_KEY")
    client = get_client(api_key)

    prompt = input("💬 Enter your prompt: ").strip()
    if not prompt:
        print("⚠️ No prompt provided.")
        return

    messages = [{"role": "user", "content": prompt}]
    response = chat_with_model(client, messages)

    if STREAM:
        for chunk in response:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                print(delta.content, end="", flush=True)
    else:
        print(response.choices[0].message.content)
