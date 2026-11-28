"""Benchmark YAML input, normalizing dates for schema validation."""

from datetime import date
from pathlib import Path
from typing import Any

import yaml


def isoformat_dates(value: Any) -> Any:
    """Replace YAML-parsed dates with ISO strings, recursively (the schema's dates are strings).

    >>> isoformat_dates({"d": date(2025, 6, 1), "l": [date(2026, 1, 2)]})
    {'d': '2025-06-01', 'l': ['2026-01-02']}
    """
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: isoformat_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [isoformat_dates(v) for v in value]
    return value


def load_yaml(path: Path) -> dict:
    """Read a YAML mapping, with dates as ISO strings."""
    return isoformat_dates(yaml.safe_load(path.read_text()))
