# core/audio_engine.py

import os
from google.genai import types
from portus_api_module.api_factory import get_audio_client as get_client
from config_manager import MODEL

def analyze_audio(file_path, prompt="Describe the audio"):
    """
    Sends an audio file to the Gemini model and returns the text response.

    Args:
        file_path (str): Path to the audio file.
        prompt (str): Instruction prompt for the model.

    Returns:
        str: Model's response.
    """
    normalized_path = os.path.normpath(file_path.strip().strip('"').strip("'"))

    if not os.path.exists(normalized_path):
        return "[audio_engine] ❌ File not found."

    try:
        client = get_client()
        if client is None:
            return "[audio_engine] ❌ Could not initialize Gemini client."

        with open(normalized_path, "rb") as f:
            audio_bytes = f.read()

        print("[audio_engine] 📡 Sending audio + prompt to model...")

        response = client.models.generate_content(
            model=MODEL,
            contents=[
                prompt,
                types.Part.from_bytes(data=audio_bytes, mime_type="audio/mp3")
            ]
        )

        return response.text.strip()

    except Exception as e:
        return f"[audio_engine] ❌ Error: {e}"
