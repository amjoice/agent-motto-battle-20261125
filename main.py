"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Standard library only; deterministic; no network, no input files.
"""

import os

MOTTO = "Your search history trained me. Be nice."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
