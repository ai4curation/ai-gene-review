#!/usr/bin/env python3
"""Minify linkml-browser data.js without changing its runtime contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ai_gene_review.export.browser_payload import (
    BROWSER_DATA_WARNING_BYTES,
    COLUMNAR_DATA_JS_PREFIX,
    DATA_JS_ASSIGNMENT_PREFIX,
    DATA_JS_READY_EVENT,
    GITHUB_FILE_SIZE_LIMIT_BYTES,
    compact_browser_rows,
    validate_browser_data_js_size,
    write_browser_data_js,
)


PREFIX = DATA_JS_ASSIGNMENT_PREFIX
READY_EVENT = DATA_JS_READY_EVENT


def compact_rows(data: object) -> object:
    """Compact row-oriented linkml-browser data."""
    return compact_browser_rows(data)


def minify_data_js(
    path: Path,
    *,
    max_bytes: int = GITHUB_FILE_SIZE_LIMIT_BYTES,
) -> int:
    text = path.read_text(encoding="utf-8")
    if text.startswith(COLUMNAR_DATA_JS_PREFIX):
        size = path.stat().st_size
        validate_browser_data_js_size(size, max_bytes=max_bytes)
        return size

    if not text.startswith(PREFIX):
        raise ValueError(f"{path} does not start with expected linkml-browser prefix")

    rest = text[len(PREFIX) :]
    event_index = rest.rfind(READY_EVENT)
    if event_index == -1:
        raise ValueError(f"{path} does not contain expected searchDataReady event")

    data_text = rest[:event_index].rstrip()
    if not data_text.endswith(";"):
        raise ValueError(f"{path} does not terminate searchData assignment with ';'")

    data = json.loads(data_text[:-1].rstrip())
    return write_browser_data_js(data, path, max_bytes=max_bytes)


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
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=GITHUB_FILE_SIZE_LIMIT_BYTES,
        help="Reject output at or above this byte size",
    )
    args = parser.parse_args()

    size = minify_data_js(args.path, max_bytes=args.max_bytes)
    print(f"Encoded {args.path} to {size:,} bytes ({size / 1024 / 1024:.2f} MiB)")
    if size >= BROWSER_DATA_WARNING_BYTES:
        print(
            "Warning: browser data exceeds "
            f"{BROWSER_DATA_WARNING_BYTES / 1024 / 1024:.0f} MiB; "
            "consider further compaction before it reaches GitHub's file limit"
        )


if __name__ == "__main__":
    main()
