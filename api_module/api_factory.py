# api_module/api_factory.py

from config_manager import config

def get_client(provider: str, api_key: str):
    model = config.get("model")
    base_url = config.get("base_url")
    stream = config.get("stream", False)

    if provider == "gemini":
        from .api_gemini import GeminiClient
        return GeminiClient(api_key=api_key, model=model, base_url=base_url, stream=stream)
    elif provider == "openai":
        from .api_openai import OpenAIClient
        return OpenAIClient(api_key=api_key, model=model, base_url=base_url, stream=stream)
    else:
        raise ValueError(f"Unsupported provider: {provider}")
