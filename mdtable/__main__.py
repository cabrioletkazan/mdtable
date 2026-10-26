import argparse
import sys

from . import __version__, to_markdown


def main(argv=None):
    p = argparse.ArgumentParser(prog="mdtable", description="Turn CSV into a Markdown table.")
    p.add_argument("file", nargs="?", help="CSV file (default: read from stdin)")
    p.add_argument("-d", "--delimiter", default=",", help="field separator (default: ,)")
    p.add_argument("-a", "--align", help="one letter per column: l, c or r")
    p.add_argument("--version", action="version", version=__version__)
    args = p.parse_args(argv)
    if args.file:
        with open(args.file, newline="", encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    delim = "\t" if args.delimiter == "\\t" else args.delimiter
    sys.stdout.write(to_markdown(text, delim, args.align))


if __name__ == "__main__":
    main()
