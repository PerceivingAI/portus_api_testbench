from config_manager import N_CTX
from tiktoken import get_encoding
from portus_context_module.context_trimmer_summarizer import trim_context

# --- Thresholds ---
CONTEXT_THRESHOLD = 0.85
TRIM_RATIO = 0.33

ENCODING = get_encoding("cl100k_base")

def count_tokens(text):
    if not text:
        return 0
    return len(ENCODING.encode(text))

def count_history_tokens(history):
    total = 0
    for entry in history:
        total += count_tokens(entry.get("role", "")) + count_tokens(entry.get("text", ""))
    return total

def is_above_threshold(history):
    token_count = count_history_tokens(history)
    limit = int(N_CTX * CONTEXT_THRESHOLD)

    print(f"[context_counter] 🧮 History: {token_count} tokens used / {N_CTX} max | Threshold = {limit} tokens ({int(CONTEXT_THRESHOLD*100)}%)")

    if token_count >= limit:
        print("[context_counter] ⚠️ Context limit reached. Initiating trimming...")
        trim_context(history, TRIM_RATIO)
        # Recount and print again
        token_count = count_history_tokens(history)
        print(f"[context_counter] 🔁 Recount: {token_count} tokens now in history.\n")
        return True

    return False
