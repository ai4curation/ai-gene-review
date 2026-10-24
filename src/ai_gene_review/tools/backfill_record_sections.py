"""Fill ``record_section`` on quotes from cached UniProt flat files.

A review quotes a ``file:...-uniprot.txt`` record verbatim, so which section
of the record a quote comes from (``CC:CAUTION``, ``CC:FUNCTION``,
``FT:BINDING`` ...) can be read off the cited file. This tool adds that value
next to each such ``supporting_text``.

The edit is made on the YAML text, one inserted line per quote, so the rest
of the file (quoting, folding, comments, key order) is left byte for byte as
it was. The result is reloaded and compared with the original, and the file is
not written unless the only difference is the added ``record_section`` keys.

Existing values are kept; ``fix=True`` rewrites the ones that disagree with
the cited file, when the value is a one-line flow sequence that can be
replaced by rewriting its line. A quote whose text occurs in more than one
section of the record gets no value: the section is not established.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple

import yaml

from ai_gene_review.validation.local_source_text import (
    PROJECT_ROOT,
    iter_local_quote_items,
    resolve_local_source,
)
from ai_gene_review.validation.uniprot_quote_source import (
    AMBIGUOUS,
    UNLOCATED,
    is_uniprot_source,
    locate_sections,
)

KEY = "record_section"
_PLAIN = re.compile(r"[A-Za-z0-9][A-Za-z0-9 :/_.()-]*")


class MarkedDict(dict):
    """A mapping that remembers where each key and value starts (0-based line, column)."""

    key_marks: Dict[Any, Tuple[int, int]]
    value_marks: Dict[Any, Tuple[int, int]]


class _MarkedLoader(yaml.CSafeLoader):
    """The libyaml safe loader, building ``MarkedDict`` mappings."""


def _construct_marked(
    loader: _MarkedLoader, node: yaml.MappingNode
) -> Iterator[MarkedDict]:
    data = MarkedDict()
    yield data
    data.update(loader.construct_mapping(node))
    data.key_marks, data.value_marks = {}, {}
    for k, v in node.value:
        if isinstance(k, yaml.ScalarNode):
            data.key_marks[k.value] = (k.start_mark.line, k.start_mark.column)
            data.value_marks[k.value] = (v.start_mark.line, v.start_mark.column)


_MarkedLoader.add_constructor("tag:yaml.org,2002:map", _construct_marked)


def load_marked(text: str) -> Any:
    r"""Load YAML with key positions on every mapping.

    >>> d = load_marked("a: 1\nb:\n  c: x\n")
    >>> d["b"].key_marks["c"], d.value_marks["a"]
    ((2, 2), (0, 3))
    """
    return yaml.load(text, Loader=_MarkedLoader)


@dataclass
class BackfillResult:
    """Outcome of backfilling one document.

    ``text`` is the updated document. ``added`` and ``fixed`` count values
    written; ``mismatched`` counts existing values that disagree with the
    cited file and were left alone; ``unlocated`` counts quotes that could not
    be found in the cited file; ``ambiguous`` counts quotes found in more than
    one section, which are left without a value; ``unplaceable`` counts quotes
    whose layout (e.g. a flow mapping) leaves no line to insert the key on.
    """

    text: str
    added: int = 0
    fixed: int = 0
    mismatched: int = 0
    unlocated: int = 0
    ambiguous: int = 0
    unplaceable: int = 0
    paths: List[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return bool(self.added or self.fixed)


def flow_value(sections: Iterable[str]) -> str:
    """Render sections as a one-line YAML flow sequence.

    >>> flow_value(["CC:CAUTION", "CC:SUBCELLULAR LOCATION"])
    '[CC:CAUTION, CC:SUBCELLULAR LOCATION]'
    >>> flow_value(["FT:a,b"])
    '["FT:a,b"]'
    """
    return (
        "["
        + ", ".join(s if _PLAIN.fullmatch(s) else json.dumps(s) for s in sections)
        + "]"
    )


def _record_items(
    data: Any, project_root: Path
) -> Iterator[Tuple[str, MarkedDict, Path]]:
    """``(path, item, source)`` for each quote whose cited source is a cached UniProt record."""
    for path, reference_id, item in iter_local_quote_items(data):
        source = resolve_local_source(reference_id, project_root)
        if source is not None and is_uniprot_source(source):
            if not isinstance(item, MarkedDict):
                raise TypeError(
                    "load the document with load_marked to get key positions"
                )
            yield path, item, source


def _stated(value: Any) -> Optional[List[str]]:
    if value is None:
        return None
    return [value] if isinstance(value, str) else [str(v) for v in value]


def backfill_text(
    text: str, project_root: Path = PROJECT_ROOT, fix: bool = False
) -> BackfillResult:
    """Add ``record_section`` to every UniProt quote in a YAML document's text."""
    data = load_marked(text)
    result = BackfillResult(text)
    if data is None:
        return result
    lines = text.splitlines(keepends=True)
    # line index -> (replacement for that line or None, lines to insert before it)
    edits: Dict[int, Tuple[Optional[str], List[str]]] = {}
    for path, item, source in _record_items(data, project_root):
        status, sections = locate_sections(item["supporting_text"], source)
        if status == UNLOCATED:
            result.unlocated += 1
            continue
        if status == AMBIGUOUS:
            result.ambiguous += 1
            continue
        stated = _stated(item.get(KEY))
        if stated is not None:
            if stated == sections:
                continue
            line, col = item.value_marks[KEY]
            if not fix or not _rewritable(item, lines):
                result.mismatched += 1
                continue
            edits[line] = (
                lines[line][:col] + flow_value(sections) + _eol(lines[line]),
                [],
            )
            result.fixed += 1
            result.paths.append(path)
            continue
        line, col = item.key_marks["supporting_text"]
        prefix = lines[line][:col]
        if prefix.strip() == "":
            replacement = None
        elif prefix.strip() == "-":  # supporting_text opens the list item
            replacement = prefix.replace("-", " ") + lines[line][col:]
        else:
            result.unplaceable += 1
            continue
        edits[line] = (
            replacement,
            [f"{prefix}{KEY}: {flow_value(sections)}{_eol(lines[line])}"],
        )
        result.added += 1
        result.paths.append(path)
    if not edits:
        return result
    out: List[str] = []
    for i, original in enumerate(lines):
        replacement, inserted = edits.get(i, (None, []))
        out.extend(inserted)
        out.append(original if replacement is None else replacement)
    result.text = "".join(out)
    _check_only_sections_changed(text, result)
    return result


def _rewritable(item: MarkedDict, lines: List[str]) -> bool:
    """True when the stated value is a one-line flow sequence on its key's line, with no comment.

    Only such a value can be replaced by rewriting one line; a block sequence
    or a flow sequence wrapped over several lines is left alone.
    """
    line, col = item.value_marks[KEY]
    if line != item.key_marks[KEY][0]:
        return False
    rest = lines[line][col:].strip()
    return rest.startswith("[") and rest.endswith("]") and " #" not in rest


def _eol(line: str) -> str:
    return line[len(line.rstrip("\r\n")) :] or "\n"


def _check_only_sections_changed(original: str, result: BackfillResult) -> None:
    """Fail unless the new text differs from the original only in ``record_section`` values."""
    try:
        before, after = yaml.safe_load(original), yaml.safe_load(result.text)
    except yaml.YAMLError as e:  # the edit broke the document
        raise ValueError(
            f"record_section backfill produced invalid YAML; refusing to write: {e}"
        ) from e
    changed = set(result.paths)
    for doc in (before, after):
        for path, _, item in iter_local_quote_items(doc):
            if path in changed:
                item.pop(KEY, None)
    if before != after:
        raise ValueError(
            "record_section backfill changed more than record_section; refusing to write"
        )


def backfill_file(
    path: Path,
    project_root: Path = PROJECT_ROOT,
    fix: bool = False,
    dry_run: bool = False,
) -> BackfillResult:
    """Backfill one review file in place (unless *dry_run*)."""
    text = path.read_text(encoding="utf-8")
    result = backfill_text(text, project_root, fix=fix)
    if result.changed and not dry_run:
        path.write_text(result.text, encoding="utf-8")
    return result


def review_files(paths: Iterable[Path]) -> List[Path]:
    """Expand files and directories to ``*-ai-review.yaml`` files, sorted."""
    found: List[Path] = []
    for p in paths:
        if p.is_dir():
            found.extend(p.rglob("*-ai-review.yaml"))
        else:
            found.append(p)
    return sorted(set(found))
