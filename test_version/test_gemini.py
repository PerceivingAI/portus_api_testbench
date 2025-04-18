# test_gemini.py
from gemini_wrapper import GeminiClient

gemini = GeminiClient()

response = gemini.chat([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain how rainbows form"}
])

print(response.choices[0].message.content)
