import sys
from pathlib import Path

# Ensure root directory is on sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import argparse
import os
from dotenv import load_dotenv

from core.chat_engine import chat_with_model
from api_module.api_factory import get_client
from config_manager import config, get_provider_name

# Load .env for API keys
load_dotenv()

# CLI parser
parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, help="User message to send")
args = parser.parse_args()

# Get provider name (e.g., "gemini", "openai")
provider = get_provider_name()

# Dynamically load the right API key
api_key = os.getenv(f"{provider.upper()}_API_KEY")

# Initialize LLM client
client = get_client(api_key)

# Prepare messages
messages = [{"role": "user", "content": args.prompt or "Say something nice."}]

# Send message(s)
response = chat_with_model(client, messages)

# Handle output (streaming vs full)
if config["parameters"]["global"].get("stream", False):
    for chunk in response:
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content:
            print(delta.content, end="", flush=True)
else:
    print(response.choices[0].message.content)
