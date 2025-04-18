import json
from pathlib import Path

def load_config():
    config_path = Path(__file__).resolve().parent / "config" / "portus-api-config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

config = load_config()

# --- Provider routing ---
def get_provider_source():
    return config.get("mode", {}).get("default_mode")

def get_provider_name():
    source = get_provider_source()
    return config.get("mode", {}).get(source, {}).get("default_provider")

# --- Model and URL ---
def get_model():
    source = get_provider_source()
    provider = get_provider_name()
    return config["mode"][source][provider]["model"]

def get_model_url(feature="base_url"):
    source = get_provider_source()
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
