
def str_to_bytes(text: bytes | str) -> bytes:
    """Converts text to bytes.

    Args:
        text (bytes | str): Input text.

    Returns:
        bytes: Output bytes.
    """
    if type(text) == str:
        return text.encode(encoding='utf-8')
    if type(text) == bytes:
        return text
    return str(text).encode(encoding='utf-8')