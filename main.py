"""Deadpan forecast for a city that does not exist.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt:
a flat, broadcast-style weather forecast for the invented city
of Vortessel, with one absurd, specific detail delivered deadpan.
"""

import os
import stat
import sys

ENTRY = (
    "In Vortessel, expect a high of 61 and light rain, with a brief "
    "shower of office chairs over the downtown core around 3 p.m."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)

    # Clear only the directory's contents, never the directory itself:
    # the grader mounts it and removing it kills the run with EPERM.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    os.rmdir(os.path.join(root, d))
            os.rmdir(path)
        else:
            os.unlink(path)

    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(entry_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

    raw = open(entry_path, "rb").read()
    text = raw.decode("utf-8")
    assert raw == ENTRY.encode("utf-8"), "written bytes differ from ENTRY"
    assert not text.endswith(("\n", " ", "\t")), "no trailing newline or whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    print(f"wrote {len(text)} chars to {entry_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
