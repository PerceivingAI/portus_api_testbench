# api_module/api_factory.py

from config_manager import get_provider_name, get_model, get_model_url, get_parameters

def get_client(api_key: str):
    provider = get_provider_name()
    model = get_model()
    base_url = get_model_url("base_url")
    params = get_parameters()
    stream = params.get("stream", False)

    if provider == "gemini":
        from .api_gemini import GeminiClient
        return GeminiClient(
            api_key=api_key,
            model=model,
            base_url=base_url,
            stream=stream
        )

    elif provider == "openai":
        from .api_openai import OpenAIClient
        return OpenAIClient(
            api_key=api_key,
            model=model,
            base_url=base_url,
            stream=stream
        )

    else:
        raise ValueError(f"Unsupported provider: {provider}")
