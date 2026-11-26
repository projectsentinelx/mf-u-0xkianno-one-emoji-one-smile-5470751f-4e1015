"""One Emoji, One Smile.

The entry is exactly one emoji and nothing else: no words, no caption, no
trailing newline. The program writes those UTF-8 bytes to /output/entry.txt,
which is the file the sealed gate scores and the judge reads.
"""

import os

EMOJI = "\U0001F604"  # 😄


def write_entry() -> str:
    """Write the emoji, verify the bytes on disk, and return the path."""
    data = EMOJI.encode("utf-8")
    for directory in ("/output", "./output"):
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "wb") as handle:
                handle.write(data)
            with open(path, "rb") as handle:
                if handle.read() != data:
                    continue
            return path
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    write_entry()
