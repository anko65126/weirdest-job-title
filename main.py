"""Entry program for the 'Weirdest Job Title: Blind Judge Showdown' make.fun bounty.

The entry is a single job title, at most 60 characters, as weird and funny
as it can be. The program writes exactly that title to /output/entry.txt
(an optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = "Vice President of Apologizing to Printers"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 60, f"entry must be 1-60 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    assert LINE == LINE.strip(), "entry must not have leading or trailing space"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
