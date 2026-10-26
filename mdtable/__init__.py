"""Turn CSV into a Markdown table."""
import csv
import io

__all__ = ["to_markdown"]
__version__ = "0.1.0"


def _cell(value):
    return value.strip().replace("|", "\\|").replace("\n", " ")


def to_markdown(text, delimiter=",", align=None):
    """Return a Markdown table for CSV `text`. The first row is the header.

    `align` is an optional string with one letter per column:
    l (left), c (centre), r (right).
    """
    rows = [r for r in csv.reader(io.StringIO(text), delimiter=delimiter) if r]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [[_cell(c) for c in r] + [""] * (width - len(r)) for r in rows]
    marks = {"l": ":---", "c": ":---:", "r": "---:"}
    align = (align or "").lower().ljust(width, "-")
    rule = [marks.get(a, "---") for a in align[:width]]
    lines = [rows[0], rule] + rows[1:]
    return "\n".join("| " + " | ".join(r) + " |" for r in lines) + "\n"
