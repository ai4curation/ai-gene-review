#!/usr/bin/env python3
"""Minify linkml-browser data.js without changing its runtime contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PREFIX = "window.searchData = "
READY_EVENT = "window.dispatchEvent(new Event('searchDataReady'));"


def compact_rows(data: object) -> object:
    """Drop inert top-level values from row-oriented linkml-browser data."""
    if not isinstance(data, list):
        return data

    return [
        {key: value for key, value in row.items() if value is not None and value != []}
        if isinstance(row, dict)
        else row
        for row in data
    ]


def minify_data_js(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    if not text.startswith(PREFIX):
        raise ValueError(f"{path} does not start with expected linkml-browser prefix")

    rest = text[len(PREFIX) :]
    event_index = rest.rfind(READY_EVENT)
    if event_index == -1:
        raise ValueError(f"{path} does not contain expected searchDataReady event")

    data_text = rest[:event_index].rstrip()
    if not data_text.endswith(";"):
        raise ValueError(f"{path} does not terminate searchData assignment with ';'")

    data = compact_rows(json.loads(data_text[:-1].rstrip()))
    compact_json = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    path.write_text(f"{PREFIX}{compact_json};\n{READY_EVENT}\n", encoding="utf-8")
    return path.stat().st_size


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Minify a linkml-browser data.js file in place."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="app/data.js",
        type=Path,
        help="Path to data.js, default: app/data.js",
    )
    args = parser.parse_args()

    size = minify_data_js(args.path)
    print(f"Minified {args.path} to {size:,} bytes ({size / 1024 / 1024:.2f} MiB)")


if __name__ == "__main__":
    main()
