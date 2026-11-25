"""Make the AI Judge Laugh — one-line office joke entry.

Writes a single office-life joke (1-200 UTF-8 characters, one line)
to /output/entry.txt.
"""

JOKE = (
    "The shared drive has a file called FINAL_v9_REAL_FINAL_USE_THIS_ONE, "
    "and nobody alive knows which version the client actually saw."
)


def validate(text: str) -> None:
    """Check the entry is a single line of 1-200 UTF-8 characters.

    Also rejects leading/trailing whitespace, so the judge receives
    exactly one tight line with no stray padding.
    """
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    byte_len = len(text.encode("utf-8"))
    if not 1 <= byte_len <= 200:
        raise ValueError(f"entry must be 1-200 UTF-8 characters, got {byte_len}")


def main() -> None:
    validate(JOKE)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
