from google.genai import types
from portus_api_module.api_factory import get_understanding_client as get_client
from portus_engine_module.utils import normalize_and_validate_pdf
from config_manager import MODEL

def analyze_pdf(file_path, prompt="Summarize this document"):
    """
    Analyzes a PDF using Gemini API via inline upload. Only works for files < 20MB.
    """
    try:
        normalized_path, error = normalize_and_validate_pdf(file_path)
        if error:
            return error

        with open(normalized_path, "rb") as f:
            pdf_bytes = f.read()

        client = get_client()
        print("[docs_engine] 📡 Sending PDF + prompt to model...")

        response = client.models.generate_content(
            model=MODEL,
            contents=[
                types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
                prompt
            ]
        )

        return response.text.strip()

    except Exception as e:
        return f"[docs_engine] ❌ Error: {e}"
