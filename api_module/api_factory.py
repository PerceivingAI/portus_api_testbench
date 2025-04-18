# api_module/api_factory.py

from config_manager import PROVIDER_NAME, MODEL, BASE_URL, STREAM

def get_client(api_key: str):
    if PROVIDER_NAME == "gemini":
        from .api_gemini import GeminiClient
        return GeminiClient(
            api_key=api_key,
            model=MODEL,
            base_url=BASE_URL,
            stream=STREAM
        )

    elif PROVIDER_NAME == "openai":
        from .api_openai import OpenAIClient
        return OpenAIClient(
            api_key=api_key,
            model=MODEL,
            base_url=BASE_URL,
            stream=STREAM
        )

    else:
        raise ValueError(f"Unsupported provider: {PROVIDER_NAME}")
