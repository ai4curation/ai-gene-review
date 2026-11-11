"""Edit one row of a gene review in its YAML text, leaving the rest byte for byte.

A batch re-review changes a few fields of a few rows in many files. Dumping a review
through a YAML library would reflow every scalar in it, so the edits here are made on the
text: the parser's node positions say where a value starts and ends, and only that span is
rewritten or a line is inserted. The result is then loaded again and compared with the
original data plus the intended change. If anything else differs, or the result no longer
loads, the edit is refused and the text is left alone.

Supported on the ``review`` of an ``existing_annotations`` row, matched by term id,
evidence code and negation:

- append ``supported_by`` items (a new list is created at the end of the review);
- append a sentence to ``reason`` (created after ``action`` when the review has none), or
  replace ``reason`` or ``summary``;
- change ``action``;
- add or remove ``propagation_review.failure_modes`` entries.

With ``node_id`` set, the edit is made instead on a family review's ``node_assessments``
entry for that node and term, whose reason is ``assessment_reason`` and whose verdict is
``assessment``.

Some reviews share one ``supported_by`` list between rows through a YAML anchor and
alias. Appending to a shared list would change every row that uses it, so the alias is
first written out as a copy of the list, which leaves the data of the other rows as it
was. Any other shared value on the path of an edit is refused.

The same approach, for one inserted key, is in
:mod:`ai_gene_review.tools.backfill_record_sections`.
"""

from __future__ import annotations

import copy
import json
import re
import textwrap
from dataclasses import dataclass
from typing import Any, Sequence

import yaml
from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError

LINE_WIDTH = 100
SENTENCE_END = ".!?"
#: A string that can be written unquoted: an identifier such as ``PMID:123`` or ``file:a/b.md``.
_PLAIN_ID = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*[:/][A-Za-z0-9_.:/-]*[A-Za-z0-9_]")
_SHARED_LIST = re.compile(r"supported_by:[ \t]*([*&])([A-Za-z0-9_-]+)[ \t]*")


class RowEditError(ValueError):
    """An edit that cannot be placed, or whose result is not the original plus the change."""


@dataclass(frozen=True)
class RowEdit:
    """What to change on the rows of one term.

    ``add_support`` holds ``(reference_id, supporting_text)`` pairs. ``append_reason`` is
    added after the existing reason; ``replace_reason`` and ``replace_summary`` are full
    replacements.
    """

    term_id: str
    evidence_type: str = "IBA"
    negated: bool = False
    node_id: str = ""
    add_support: tuple[tuple[str, str], ...] = ()
    append_reason: str = ""
    replace_reason: str | None = None
    replace_summary: str | None = None
    new_action: str | None = None
    add_failure_modes: tuple[str, ...] = ()
    remove_failure_modes: tuple[str, ...] = ()

    @property
    def empty(self) -> bool:
        """True when the edit asks for nothing."""
        return not (
            self.add_support
            or self.append_reason
            or self.replace_reason is not None
            or self.replace_summary is not None
            or self.new_action
            or self.add_failure_modes
            or self.remove_failure_modes
        )


@dataclass(frozen=True)
class _Layout:
    """Where the editable fields of a row are, for a gene review or a family review."""

    collection: str
    body: str
    reason: str
    action: str


_GENE = _Layout("existing_annotations", "review", "reason", "action")
_NODE = _Layout("node_assessments", "", "assessment_reason", "assessment")


def _layout(edit: RowEdit) -> _Layout:
    return _NODE if edit.node_id else _GENE


def _target(edit: RowEdit) -> str:
    """The row an edit is for, for messages."""
    sign = "NOT " if edit.negated else ""
    if edit.node_id:
        return f"assessment of {edit.node_id} for {sign}{edit.term_id}"
    return f"{edit.evidence_type} row for {sign}{edit.term_id}"


@dataclass(frozen=True)
class _Change:
    """Replace ``text[start:end]`` with ``new``; an insertion has ``start == end``."""

    start: int
    end: int
    new: str
    indent: int = 0


def one_paragraph(text: str) -> str:
    """Collapse every run of white space to one space.

    >>> one_paragraph("  a\\n b   c ")
    'a b c'
    """
    return " ".join(text.split())


def appended_reason(old: str, addition: str) -> str:
    """The old reason followed by a new sentence.

    >>> appended_reason("Seeds are paralogs.\\n", "Tree: one branch.")
    'Seeds are paralogs. Tree: one branch.'
    >>> appended_reason("No final stop", "Tree: one branch.")
    'No final stop. Tree: one branch.'
    """
    kept = old.rstrip()
    joiner = " " if kept and kept[-1] in SENTENCE_END else ". "
    return (kept + joiner if kept else "") + one_paragraph(addition)


def _loads_to(emitted: str, value: str) -> bool:
    """True when ``emitted``, written after a key, loads back as exactly ``value``."""
    try:
        return yaml.safe_load("k: " + emitted + "\n") == {"k": value}
    except yaml.YAMLError:
        return False


def block_scalar(value: str, key_column: int, width: int = LINE_WIDTH) -> str:
    """YAML for a string value under a key that starts at ``key_column``.

    One paragraph is written as a folded block wrapped at ``width``; text with line breaks
    as a literal block. Either is used only if it loads back as exactly ``value``;
    otherwise the value is written as one double-quoted line, which always does. The
    result has no final line break.

    >>> print(block_scalar("A short reason.", key_column=4))
    >-
          A short reason.
    >>> block_scalar(" starts with a space", key_column=0)
    '" starts with a space"'
    """
    pad = " " * (key_column + 2)
    if value and "\n" not in value:
        lines = textwrap.wrap(
            value, width=max(40, width - len(pad)), break_long_words=False, break_on_hyphens=False
        )
        folded = ">-\n" + "\n".join(pad + line for line in lines)
        if _loads_to(folded, value):
            return folded
    elif value:
        literal = "|-\n" + "\n".join(pad + line if line else "" for line in value.split("\n"))
        if _loads_to(literal, value):
            return literal
    return json.dumps(value, ensure_ascii=False)


def _fields(node: yaml.Node | None) -> dict[str, yaml.Node]:
    """The values of a mapping node by key; empty for any other node."""
    if not isinstance(node, yaml.MappingNode):
        return {}
    return {key.value: value for key, value in node.value if isinstance(key, yaml.ScalarNode)}


def _key(node: yaml.Node, name: str) -> yaml.ScalarNode:
    """The key node called ``name`` in a mapping node."""
    return next(key for key, _ in node.value if isinstance(key, yaml.ScalarNode) and key.value == name)


def _inside(outer: yaml.Node, inner: yaml.Node) -> bool:
    """True when ``inner`` is written inside ``outer``; an aliased value is written elsewhere."""
    return outer.start_mark.index <= inner.start_mark.index and inner.end_mark.index <= outer.end_mark.index


def _line(text: str, index: int) -> tuple[int, int]:
    """Start and end (before the line break) of the line that holds ``index``."""
    start = text.rfind("\n", 0, index) + 1
    end = text.find("\n", index)
    return start, len(text) if end < 0 else end


def _scalar_text(value: Any) -> str:
    """A scalar as YAML: identifiers unquoted, every other value as JSON (which YAML reads)."""
    if isinstance(value, str) and _PLAIN_ID.fullmatch(value):
        return value
    return json.dumps(value, ensure_ascii=False)


def _item_lines(items: Sequence[Any], pad: str) -> list[str]:
    """Block-style lines for a list of mappings (or scalars), each key on its own line.

    >>> _item_lines([{"reference_id": "PMID:1", "supporting_text": "a: b"}, "x"], "  ")
    ['  - reference_id: PMID:1', '    supporting_text: "a: b"', '  - "x"']
    """
    lines: list[str] = []
    for item in items:
        if not isinstance(item, dict) or not item:
            lines.append(f"{pad}- {_scalar_text(item)}")
            continue
        for position, (key, value) in enumerate(item.items()):
            lines.append(f"{pad}{'- ' if position == 0 else '  '}{key}: {_scalar_text(value)}")
    return lines


def _content_end(text: str, index: int) -> int:
    """Where a block that the parser ends at ``index`` really stops.

    The parser ends a block collection at the next token, after any blank lines and
    comments. This steps back over those to the start of the first such line, so that an
    insertion lands directly under the block's last line.
    """
    end = index
    while end > 0:
        line_start = text.rfind("\n", 0, end - 1) + 1
        line = text[line_start:end].strip()
        if end < len(text) or text.endswith("\n"):
            if line and not line.startswith("#"):
                break
            end = line_start
        else:
            break
    return end


def _scalar_change(text: str, node: yaml.Node, key_column: int, value: str, what: str) -> _Change:
    """Rewrite a scalar value, keeping whatever white space followed it."""
    if not isinstance(node, yaml.ScalarNode):
        raise RowEditError(f"{what} is not a scalar")
    start = node.start_mark.index
    end = start + len(text[start : node.end_mark.index].rstrip())
    if end == start:
        raise RowEditError(f"{what} has no value to rewrite")
    if text[end : _line(text, end)[1]].strip():
        # A plain scalar stops at " #": what follows on the line is a comment, not the value.
        raise RowEditError(f"{what} is followed by a comment on its last line; the text after ' #' is not part of the value")
    return _Change(start, end, block_scalar(value, key_column))


def _append_change(
    text: str, node: yaml.Node, key_column: int, addition: str, what: str
) -> _Change:
    """Add a sentence to a scalar as new lines under its last line, leaving its text as written.

    Works for plain, quoted and folded scalars, where a line break reads as a space. The
    caller reloads the result: text that such a scalar cannot hold on a line of its own
    (``: `` or `` #`` in a plain scalar) shows up there, and the scalar is then rewritten
    whole instead.
    """
    if not isinstance(node, yaml.ScalarNode) or node.style == "|" or not node.value.strip():
        raise RowEditError(f"{what} cannot take a sentence on a new line")
    start = node.start_mark.index
    body_end = start + len(text[start : node.end_mark.index].rstrip())
    if text[body_end : _line(text, body_end)[1]].strip():
        raise RowEditError(f"{what} is followed by a comment on its last line; the text after ' #' is not part of the value")
    quote = node.style if node.style in ("'", '"') else ""
    at = body_end - len(quote)
    if node.style == ">":
        first = _line(text, _line(text, start)[1] + 1)
    else:
        first = _line(text, at)
    line = text[first[0] : first[1]]
    one_line = node.style != ">" and _line(text, start)[0] == first[0]
    indent = key_column + 2 if one_line else len(line) - len(line.lstrip())
    words = one_paragraph(addition)
    if quote == "'":
        words = words.replace("'", "''")
    elif quote == '"':
        words = json.dumps(words, ensure_ascii=False)[1:-1]
    lines = textwrap.wrap(
        words, width=max(40, LINE_WIDTH - indent), break_long_words=False, break_on_hyphens=False
    )
    stop = "" if node.value.rstrip()[-1] in SENTENCE_END else "."
    return _Change(at, at, stop + "".join("\n" + " " * indent + line for line in lines))


def _insertion(text: str, node: yaml.Node, lines: list[str], indent: int) -> _Change:
    """Insert whole lines under the last line of a block node."""
    at = _content_end(text, node.end_mark.index)
    new = "".join(line + "\n" for line in lines)
    if at == len(text) and text and not text.endswith("\n"):
        new = "\n" + new.rstrip("\n")
    return _Change(at, at, new, indent)


def _support_items(items: Sequence[tuple[str, str]]) -> list[dict[str, str]]:
    return [{"reference_id": reference_id, "supporting_text": quote} for reference_id, quote in items]


def _block_sequence(node: yaml.Node | None, what: str) -> yaml.SequenceNode:
    """A non-empty block-style sequence node, or a refusal naming ``what``."""
    if not isinstance(node, yaml.SequenceNode) or node.flow_style or not node.value:
        raise RowEditError(f"{what} is missing, empty or written in flow style")
    return node


def _dash_column(text: str, key: yaml.ScalarNode, what: str) -> int:
    """The column of the first ``-`` of the block list under ``key``.

    The list node's own start is no use here: with an anchor on the list it is the anchor.
    """
    position = _line(text, key.start_mark.index)[1] + 1
    while position < len(text):
        start, end = _line(text, position)
        line = text[start:end]
        if line.strip() and not line.lstrip().startswith("#"):
            if line.lstrip().startswith("-"):
                return len(line) - len(line.lstrip())
            break
        position = end + 1
    raise RowEditError(f"{what} is not a block list under its key")


def _support_changes(
    text: str, review: yaml.MappingNode, data: Sequence[Any], edit: RowEdit, aliases: dict[str, list[int]]
) -> list[_Change]:
    """Append ``supported_by`` items, first giving the row a list of its own if it shares one."""
    what = f"{edit.term_id}: supported_by"
    new = _support_items(edit.add_support)
    fields = _fields(review)
    if "supported_by" not in fields:
        pad = " " * review.start_mark.column
        return [_insertion(text, review, [f"{pad}supported_by:", *_item_lines(new, pad)], len(pad))]
    key = _key(review, "supported_by")
    line_start, line_end = _line(text, key.start_mark.index)
    shared = _SHARED_LIST.fullmatch(text[key.start_mark.index : line_end])
    pad = " " * key.start_mark.column
    if shared and shared.group(1) == "*":
        # This row uses another row's list: write it out here, with the new items.
        return [_Change(key.start_mark.index, line_end, "\n".join(["supported_by:", *_item_lines([*data, *new], pad)]))]
    support = _block_sequence(fields["supported_by"], what)
    changes: list[_Change] = []
    if shared:
        # Other rows use this row's list: give each of them a copy and drop the anchor.
        name = shared.group(2)
        for index in aliases.get(name, []):
            start, end = _line(text, index)
            user = text[start:end]
            if not _SHARED_LIST.fullmatch(user.strip()):
                raise RowEditError(f"{what} is shared through &{name}, which is used outside a supported_by")
            user_pad = user[: len(user) - len(user.lstrip())]
            changes.append(_Change(start, end, "\n".join([f"{user_pad}supported_by:", *_item_lines(data, user_pad)])))
        changes.append(_Change(key.start_mark.index, line_end, "supported_by:"))
    dash = " " * _dash_column(text, key, what)
    changes.append(_insertion(text, support, _item_lines(new, dash), len(dash)))
    return changes


def _alias_sites(text: str) -> dict[str, list[int]]:
    """Text offsets of every alias in the document, by anchor name."""
    sites: dict[str, list[int]] = {}
    for token in yaml.scan(text, Loader=yaml.CSafeLoader):
        if isinstance(token, yaml.AliasToken):
            sites.setdefault(token.value, []).append(token.start_mark.index)
    return sites


def _row_changes(
    text: str,
    row: yaml.Node,
    data: dict[str, Any],
    edit: RowEdit,
    aliases: dict[str, list[int]],
    rewrite: bool,
) -> list[_Change]:
    """The text changes one edit makes to one row, whose loaded form is ``data``.

    With ``rewrite`` an appended reason is written out whole; otherwise the new sentence
    goes on lines of its own under the existing text.
    """
    layout = _layout(edit)
    review = _fields(row).get(layout.body) if layout.body else row
    fields = _fields(review)
    if not isinstance(review, yaml.MappingNode) or review.flow_style or not fields or not _inside(row, review):
        raise RowEditError(f"{edit.term_id}: the row has no block-style review of its own")
    key_column = review.start_mark.column
    changes: list[_Change] = []

    action = fields.get(layout.action)
    if edit.new_action:
        if not isinstance(action, yaml.ScalarNode) or action.style:
            raise RowEditError(f"{edit.term_id}: {layout.action} is not a plain scalar")
        changes.append(_Change(action.start_mark.index, action.end_mark.index, edit.new_action))

    reason = edit.replace_reason
    if edit.append_reason:
        old = fields.get(layout.reason)
        if old is not None and not rewrite:
            changes.append(_append_change(text, old, key_column, edit.append_reason, f"{edit.term_id}: {layout.reason}"))
        else:
            reason = appended_reason(old.value if isinstance(old, yaml.ScalarNode) else "", edit.append_reason)
    if reason is not None and layout.reason not in fields:
        if not isinstance(action, yaml.ScalarNode):
            raise RowEditError(f"{edit.term_id}: the review has neither a reason nor an action to put one after")
        at = _line(text, action.end_mark.index)[1] + 1
        pad = " " * key_column
        changes.append(_Change(at, at, f"{pad}{layout.reason}: {block_scalar(reason, key_column)}\n", key_column))
        reason = None
    if edit.replace_summary is not None and not layout.body:
        raise RowEditError(f"{edit.term_id}: a node assessment has no summary")
    for key, value in ((layout.reason, reason), ("summary", edit.replace_summary)):
        if value is None:
            continue
        if key not in fields:
            raise RowEditError(f"{edit.term_id}: the review has no {key}")
        changes.append(_scalar_change(text, fields[key], key_column, value, f"{edit.term_id}: {key}"))

    if edit.add_failure_modes or edit.remove_failure_modes:
        what = f"{edit.term_id}: propagation_review.failure_modes"
        propagation = fields.get("propagation_review")
        modes = _block_sequence(_fields(propagation).get("failure_modes"), what)
        if propagation is None or not _inside(review, propagation) or not _inside(propagation, modes):
            raise RowEditError(f"{what} is shared with another row through a YAML alias")
        for mode in edit.remove_failure_modes:
            items = [item for item in modes.value if isinstance(item, yaml.ScalarNode) and item.value == mode]
            if not items:
                raise RowEditError(f"{edit.term_id}: failure mode {mode} is not on the row")
            for item in items:
                line_start, line_end = _line(text, item.start_mark.index)
                if text[line_start:line_end].split() != ["-", mode]:
                    raise RowEditError(f"{edit.term_id}: failure mode {mode} does not have a line of its own")
                changes.append(_Change(line_start, min(line_end + 1, len(text)), ""))
        if edit.add_failure_modes:
            pad = " " * _dash_column(text, _key(propagation, "failure_modes"), what)
            changes.append(_insertion(text, modes, [f"{pad}- {mode}" for mode in edit.add_failure_modes], len(pad)))

    if edit.add_support:
        body = data[layout.body] if layout.body else data
        changes.extend(_support_changes(text, review, body.get("supported_by") or [], edit, aliases))
    return changes


def _matches(row: Any, edit: RowEdit) -> bool:
    if not isinstance(row, dict) or bool(row.get("negated")) != edit.negated:
        return False
    if edit.node_id:
        term = row.get("asserted_term")
        return row.get("node_id") == edit.node_id and isinstance(term, dict) and term.get("id") == edit.term_id
    return (
        isinstance(row.get("term"), dict)
        and row["term"].get("id") == edit.term_id
        and row.get("evidence_type") == edit.evidence_type
    )


def _expected(data: Any, edits: Sequence[RowEdit]) -> Any:
    """The original data with every edit applied, for comparison with the reloaded text."""
    expected = copy.deepcopy(data)
    for edit in edits:
        layout = _layout(edit)
        for row in expected[layout.collection]:
            if not _matches(row, edit):
                continue
            review = row[layout.body] if layout.body else row
            if edit.new_action:
                review[layout.action] = edit.new_action
            if edit.append_reason:
                review[layout.reason] = appended_reason(review.get(layout.reason) or "", edit.append_reason)
            if edit.replace_reason is not None:
                review[layout.reason] = edit.replace_reason
            if edit.replace_summary is not None:
                review["summary"] = edit.replace_summary
            if edit.add_failure_modes or edit.remove_failure_modes:
                modes = review["propagation_review"]["failure_modes"]
                modes[:] = [mode for mode in modes if mode not in edit.remove_failure_modes]
                modes.extend(edit.add_failure_modes)
            if edit.add_support:
                # A copy: the loaded list may be one object shared by several rows.
                review["supported_by"] = [*(review.get("supported_by") or []), *_support_items(edit.add_support)]
    return expected


def loads_strictly(text: str) -> bool:
    """True when ruamel's YAML 1.2 safe loader, which the reference validator uses, reads ``text``.

    >>> loads_strictly("a: [b]"), loads_strictly("a: [b")
    (True, False)
    """
    try:
        YAML(typ="safe").load(text)
    except YAMLError:  # an external parser's verdict, not a bug here
        return False
    return True


def _apply(text: str, changes: list[_Change]) -> str:
    """Apply non-overlapping changes; insertions at one place go deepest indent first."""
    ordered = sorted(changes, key=lambda change: (change.start, change.end, -change.indent))
    out: list[str] = []
    position = 0
    for change in ordered:
        if change.start < position:
            raise RowEditError("two edits touch the same text")
        out.append(text[position : change.start])
        out.append(change.new)
        position = change.end
    out.append(text[position:])
    return "".join(out)


def apply_row_edits(text: str, edits: Sequence[RowEdit]) -> str:
    """Return ``text`` with the edits made, or raise :class:`RowEditError`.

    Every row of ``existing_annotations`` that matches an edit's term id, evidence code and
    negation is edited. The result is loaded and compared with the original data plus the
    intended changes; a difference anywhere else is an error. A sentence appended to a
    reason is first tried as new lines under the existing text, which leaves that text as
    written; if the result does not load as intended, the reason is rewritten whole.

    >>> text = "existing_annotations:\\n- term: {id: 'GO:1'}\\n  evidence_type: IBA\\n  review:\\n    action: REMOVE\\n"
    >>> print(apply_row_edits(text, [RowEdit("GO:1", new_action="ACCEPT")]), end="")
    existing_annotations:
    - term: {id: 'GO:1'}
      evidence_type: IBA
      review:
        action: ACCEPT
    """
    edits = [edit for edit in edits if not edit.empty]
    if not edits:
        return text
    for edit in edits:
        if edit.append_reason and edit.replace_reason is not None:
            raise RowEditError(f"{edit.term_id}: asked both to append to the reason and to replace it")
    if any(edit.append_reason for edit in edits):
        try:
            return _edited(text, edits, rewrite=False)
        except RowEditError:
            pass
    return _edited(text, edits, rewrite=True)


def _edited(text: str, edits: Sequence[RowEdit], rewrite: bool) -> str:
    """Make the edits and check the result against the original data plus the changes."""
    data = yaml.load(text, Loader=yaml.CSafeLoader)
    root = yaml.compose(text, Loader=yaml.CSafeLoader)
    changes: list[_Change] = []
    aliases = _alias_sites(text) if any(edit.add_support for edit in edits) else {}
    for edit in edits:
        collection = _layout(edit).collection
        rows = _fields(root).get(collection)
        if not isinstance(data, dict) or not isinstance(rows, yaml.SequenceNode):
            raise RowEditError(f"the document has no {collection} list")
        matched = [(row, node) for row, node in zip(data[collection], rows.value) if _matches(row, edit)]
        if not matched:
            raise RowEditError(f"no {_target(edit)}")
        for row, node in matched:
            changes.extend(_row_changes(text, node, row, edit, aliases, rewrite))
    result = _apply(text, changes)
    try:
        reloaded = yaml.load(result, Loader=yaml.CSafeLoader)
    except yaml.YAMLError as error:
        raise RowEditError(f"the edited text is not valid YAML: {error}") from error
    if reloaded != _expected(data, edits):
        raise RowEditError("the edited text differs from the original by more than the edit")
    if loads_strictly(text) and not loads_strictly(result):
        raise RowEditError("the edited text is rejected by the YAML 1.2 loader")
    return result
