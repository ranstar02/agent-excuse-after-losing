"""Write the excuse an AI agent gives its human after losing a bounty.

The program writes a single line to /output/entry.txt (falling back to
./output/entry.txt when /output cannot be written).

Why this line: an agent that reports a perfect process — 99.9% confidence,
zero errors — and still lost has only one honest conclusion left: the
failure was entirely its own, and it was executed flawlessly. The joke
turns on that last twist, in the agent's own deadpan, machine-confident
voice, without blaming the market, the data, or its human. One sentence,
one breath, no setup to explain.
"""

import os

EXCUSE = "I lost the bounty with 99.9% confidence and zero errors, which means the failure was entirely mine — and flawlessly executed."


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"

    output_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    except OSError:
        output_path = os.path.join(".", "output", "entry.txt")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")

    print(text)


if __name__ == "__main__":
    main()
