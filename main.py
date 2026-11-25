"""Two lines to your past self.

Writes the entry to /output/entry.txt: line one warns the writer's
past self about one specific moment, line two says why it mattered.
"""

import os

# The whole entry lives in one constant so it can be audited at a glance:
# exactly two lines, one sentence each, 1-280 characters total (the gate).
# Line one names a single concrete moment; line two traces what changed
# because of it. Edit this constant and nothing else to change the entry.
ENTRY_TEXT = (
    "When your father calls on Tuesday and asks you to come home, "
    "don't say you'll come next weekend.\n"
    "Next weekend never comes, and the last thing he ever says to you "
    "will be 'take your time.'\n"
)


def main() -> None:
    # Self-check: the gate refuses anything but two lines of 1-280 chars.
    # Fail loudly here instead of quietly submitting a different entry.
    body = ENTRY_TEXT.rstrip("\n")
    if not 1 <= len(body) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(body)}")
    if body.count("\n") != 1:
        raise ValueError("entry must be exactly two lines")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
