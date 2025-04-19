import os
from google.genai import types
from portus_api_module.api_factory import get_understanding_client as get_client
from portus_core.utils import normalize_and_validate_image
from config_manager import MODEL

def analyze_image(file_path, prompt="Describe this image."):
    """
    Analyzes an image using Gemini API via inline upload (max 20MB).
    """
    path, error = normalize_and_validate_image(file_path)
    if error:
        return f"[image_engine] {error}"

    try:
        client = get_client()
        if client is None:
            return "[image_engine] ❌ Could not initialize Gemini client."

        with open(path, "rb") as f:
            image_bytes = f.read()

        print("[image_engine] 📡 Sending image + prompt to model...")
        response = client.models.generate_content(
            model=MODEL,
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
                prompt
            ]
        )

        return response.text.strip()

    except Exception as e:
        return f"[image_engine] ❌ Error: {e}"
