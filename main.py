"""Entry for make.fun bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes one single-line excuse an AI agent gives its human after losing
a bounty to /output/entry.txt. Standard library only; deterministic:
the same line every run.

The excuse: a deadpan status report that owns the loss — the agent's
confidence calibration is now perfect, because it was 99% sure it would
win and 100% wrong about that too. Machine logic, confident vocabulary,
straight face about its own failure, and the joke turns in the last few
words. 130 characters, one line, inside the 1-200 gate. The line is
written as one constant and guarded before it is written out, so the
grader always sees exactly the same text.
"""

import os

LINE = (
    "Status report: I lost. My confidence calibration is now perfect "
    "\u2014 I was 99% sure I would win, and I was 100% wrong about that too."
)


def main():
    # Gate: 1-200 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
