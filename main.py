"""One Letter for Your Day: Q for queasy.

The letter stands for the day in one word: queasy, a stomach turning
over after bad street food, one hand gripping a boat rail while the
world tilts. One concrete physical scene, opened mid-moment: the
churn, the grip, the tilt. A sharp picture rather than a vague mood,
funny the moment you hear it, and true to any ordinary day that went
wrong at the stomach.
Writes exactly one character, Q, to /output/entry.txt, and nothing else.
No trailing newline: the file must be exactly one byte.
"""

import os


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Binary mode: exactly one byte, no newline translation, no extra output.
    with open("/output/entry.txt", "wb") as f:
        f.write(b"Q")


if __name__ == "__main__":
    main()
