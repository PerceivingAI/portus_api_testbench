import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import argparse
from core.chat_engine import chat_with_model
from api_module.api_factory import get_client
from config_manager import config
from dotenv import load_dotenv
import os

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, help="User message to send")
args = parser.parse_args()

provider = "gemini"
api_key = os.getenv("GEMINI_API_KEY")
client = get_client(provider, api_key)

messages = [
    {"role": "user", "content": args.prompt or "Say something nice."}
]

response = chat_with_model(client, messages)

if config.get("stream", False):
    for chunk in response:
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content:
            print(delta.content, end="", flush=True)
else:
    print(response.choices[0].message.content)
