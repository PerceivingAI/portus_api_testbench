# portus_context_module/context_trimmer_summarizer.py

def trim_context(history, trim_ratio):
    """
    Trim the oldest messages from the history by the given ratio.
    This modifies the history in place and prints full debug output.

    Args:
        history (list): The complete message history.
        trim_ratio (float): Ratio of messages to trim from the start.
    """
    if not history:
        print("[trimmer] 🟡 Empty history — skipping trim.")
        return

    print("\n[trimmer] ✂️ Trimming history...")

    print("[trimmer] 📜 Full history before:")
    for i, entry in enumerate(history):
        print(f"  {i+1:02d}. {entry['role']}: {entry['text'][:80]}")

    total_messages = len(history)
    trim_count = max(1, int(total_messages * trim_ratio))

    history[:] = history[trim_count:]  # Trim in place

    print(f"[trimmer] 🗑️ Trimmed {trim_count} messages.")

    print("[trimmer] ✅ Remaining history:")
    for i, entry in enumerate(history):
        print(f"  {i+1:02d}. {entry['role']}: {entry['text'][:80]}")
    print()
