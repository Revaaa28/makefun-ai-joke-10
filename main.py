#!/usr/bin/env python3
"""make.fun bounty ai-joke-03 entry.

Writes one one-liner about AI coding agents to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no clock —
two runs produce byte-identical output.
"""

import os

JOKE = (
    '"It works on my machine," said the AI — whose machine is a data center in Virginia running a Python version that doesn\'t exist yet.'
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly the joke text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Read back and verify: a partial or mangled write must fail loudly
    # rather than leave a wrong entry on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == JOKE, "written entry does not match the joke"


if __name__ == "__main__":
    main()
