import os
from dotenv import load_dotenv

from core.chat_engine import chat_with_model
from config_manager import STREAM, PROVIDER_NAME
from portus_api_module.api_factory import get_client

load_dotenv()

def run_chat_mode():
    api_key = os.getenv(f"{PROVIDER_NAME.upper()}_API_KEY")
    client = get_client(api_key)

    print("💬 Chat mode activated. Type /exit to return to menu.\n")

    while True:
        prompt = input("🧑 You: ").strip()

        if not prompt:
            print("⚠️ Empty input, try again.")
            continue

        if prompt.lower() == "/exit":
            print("👋 Exiting chat mode.\n")
            break

        messages = [{"role": "user", "content": prompt}]
        response = chat_with_model(client, messages)

        if STREAM:
            print("🤖 Assistant: ", end="", flush=True)
            for token in response:  # response is a generator of tokens
                print(token, end="", flush=True)
            print()
        else:
            print(f"🤖 Assistant: {response}")
