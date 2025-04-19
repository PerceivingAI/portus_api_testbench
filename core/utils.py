import os

def normalize_and_validate_file(file_path, allowed_exts, max_mb):
    """
    Generic path normalization and validation.

    Args:
        file_path (str): User-provided file path (quoted or unquoted).
        allowed_exts (tuple): Allowed file extensions (e.g., ('.pdf',)).
        max_mb (int): Maximum allowed size in megabytes.

    Returns:
        tuple: (normalized_path or None, error_message or None)
    """
    path = os.path.normpath(file_path.strip().strip('"').strip("'"))

    if not os.path.exists(path):
        return None, "[utils] ❌ File not found."

    if not path.lower().endswith(allowed_exts):
        return None, f"[utils] ❌ Only {', '.join(allowed_exts)} files are supported."

    size = os.path.getsize(path)
    max_bytes = max_mb * 1024 * 1024
    if size > max_bytes:
        return None, f"[utils] ❌ File exceeds {max_mb}MB limit."

    return path, None


def normalize_and_validate_pdf(file_path, max_mb=20):
    return normalize_and_validate_file(file_path, allowed_exts=(".pdf",), max_mb=max_mb)


def normalize_and_validate_audio(file_path, allowed_exts=(".mp3",), max_mb=20):
    return normalize_and_validate_file(file_path, allowed_exts=allowed_exts, max_mb=max_mb)
