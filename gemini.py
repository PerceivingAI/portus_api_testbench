# gemini.py

from api_module.api_factory import get_client
from dotenv import load_dotenv
import os

load_dotenv()

provider = "gemini"
api_key = os.getenv("GEMINI_API_KEY")

client = get_client(provider, api_key)

response = client.chat([
    {"role": "user", "content": "What are the main causes of thunderstorms?"}
])

print(response.choices[0].message.content)
