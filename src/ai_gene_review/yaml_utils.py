"""Safe YAML construction using libyaml when available, without global patches."""

from typing import Any, BinaryIO, TextIO

import yaml

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:  # pragma: no cover - supported on installations without libyaml
    from yaml import SafeLoader  # type: ignore[assignment]


def safe_load(stream: str | bytes | TextIO | BinaryIO) -> Any:
    """Use the same safe constructors/resolvers as PyYAML's Python SafeLoader."""
    return yaml.load(stream, Loader=SafeLoader)
