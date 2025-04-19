import os
import sys
from dotenv import load_dotenv

from core.chat_engine import chat_with_model
from config_manager import STREAM, PROVIDER_NAME
from portus_api_module.api_factory import get_client
from interface.cli.utils import handle_special_commands  # ✅ Imported here

load_dotenv()

def run_chat_mode():
    client = get_client()

    print("💬 Chat mode activated. Type /exit to quit or /menu to return.\n")

    while True:
        prompt = input("🧑 You: ").strip()

        if not prompt:
            print("⚠️ Empty input, try again.")
            continue

        if not handle_special_commands(prompt):
            break  # /menu returns False, exits loop

        messages = [{"role": "user", "content": prompt}]
        response = chat_with_model(client, messages)

        if STREAM:
            print("🤖 Assistant: ", end="", flush=True)
            for token in response:  # response is a generator of tokens
                print(token, end="", flush=True)
            print()
        else:
            print(f"🤖 Assistant: {response}")
