import json
from pathlib import Path

def load_config():
    config_path = Path(__file__).resolve().parent / "config" / "portus_api_config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

config = load_config()

# --- Provider routing ---
def get_provider_mode():
    return config.get("mode", {}).get("default_mode")

def get_provider_name():
    source = get_provider_mode()
    return config.get("mode", {}).get(source, {}).get("default_provider")

# --- Model and URL ---
def get_model():
    source = get_provider_mode()
    provider = get_provider_name()
    return config["mode"][source][provider]["model"]

def get_model_url(feature="base_url"):
    source = get_provider_mode()
    provider = get_provider_name()
    return config["mode"][source][provider].get(feature)

# --- Parameters ---
def get_system_prompt():
    return config.get("parameters", {}).get("system_prompt")

def get_parameters():
    provider = get_provider_name()
    global_params = config.get("parameters", {}).get("global", {})
    provider_params = config.get("parameters", {}).get(provider, {})
    return {**global_params, **provider_params}

def get_context_limit():
    return get_parameters().get("n_ctx")

# --- Shared constants from config ---
PROVIDER_MODE     = get_provider_mode()
PROVIDER_NAME     = get_provider_name()
MODEL             = get_model()
BASE_URL          = get_model_url("base_url")
EMBEDDING_URL     = get_model_url("embedding_url")
AUDIO_URL         = get_model_url("audio_url")

SYSTEM_PROMPT     = get_system_prompt()
PARAMETERS        = get_parameters()

TEMPERATURE       = PARAMETERS.get("temperature")
TOP_P             = PARAMETERS.get("top_p")
TOP_K             = PARAMETERS.get("top_k")
N_CTX             = PARAMETERS.get("n_ctx")
MAX_TOKENS        = PARAMETERS.get("max_tokens")
STREAM            = PARAMETERS.get("stream")
TOOLS             = PARAMETERS.get("tools")
TOOL_CHOICE       = PARAMETERS.get("tool_choice")
RESPONSE_FORMAT   = PARAMETERS.get("response_format")
STOP              = PARAMETERS.get("stop")