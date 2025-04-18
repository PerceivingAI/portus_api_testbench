from config_manager import N_CTX
from tiktoken import get_encoding  # or your tokenizer of choice

# --- Threshold ratio (shared across trimmer/summarizer) ---
CONTEXT_THRESHOLD = 0.85

# --- Tokenizer setup ---
ENCODING = get_encoding("cl100k_base")  # OpenAI-compatible; replace if needed

def count_tokens(text):
    if not text:
        return 0
    return len(ENCODING.encode(text))

def count_history_tokens(history):
    """
    Count total tokens in the full context history.
    """
    total = 0
    for entry in history:
        role = entry.get("role", "")
        text = entry.get("text", "")
        total += count_tokens(role) + count_tokens(text)
    return total

def is_above_threshold(history):
    """
    Returns True if token usage exceeds CONTEXT_THRESHOLD of N_CTX.
    Prints debug info either way.
    """
    token_count = count_history_tokens(history)
    limit = int(N_CTX * CONTEXT_THRESHOLD)

    print(f"[context_counter] 🧮 History: {token_count} tokens used / {N_CTX} max | Threshold = {limit} tokens ({int(CONTEXT_THRESHOLD*100)}%)")

    return token_count >= limit
