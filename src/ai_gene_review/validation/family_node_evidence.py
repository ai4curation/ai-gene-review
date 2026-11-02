"""Fill PAINT evidence, negation and loss seeds into family-review node assessments.

A ``node_assessment`` in ``interpro/panther/<PTHR>/<PTHR>-review.yaml`` judges one PAINT
row: a (node, term) pair in the family's ``<PTHR>-paint.tsv`` slice. Three of its fields
are not judgment but facts about that row, and the ``NODE_POLARITY`` check in
:mod:`family_residue_validator` requires them on every loss:

* ``evidence`` -- PAINT's code for the row (IBD for a gain; IRD or IKR for a loss).
* ``negated: true`` -- the row is a loss (a NOT), so the assessment judges a negation.
* ``seeds`` -- for a loss, the ancestral IBD node whose term it stops, which PAINT records
  in the row's with/from column.

This module copies those facts from the slice into the review. It never sets or changes
``assessment`` (the verdict): a loss assessed with a gain verdict such as SOUND still needs
a reviewer to choose LOSS_SUPPORTED, LOSS_CONTRADICTED and so on, and is reported instead.
It also leaves alone any field a curator already wrote, and gain seeds, which are a
curated readable subset of PAINT's donor list rather than a copy of it.

Edits are inserted as text after each assessment's ``asserted_term`` block, so the rest
of the file is untouched byte for byte, and every edit is checked by re-parsing.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from ai_gene_review.validation.family_residue_validator import node_polarity_problem
from ai_gene_review.validation.module_validator import PaintAnnotationRow, load_paint_index

FIELD_ORDER = ("evidence", "negated", "seeds")


@dataclass(frozen=True)
class FieldChange:
    """Fields added to one node assessment."""

    node: str
    term: str
    fields: dict[str, Any]


def planned_fields(assessment: dict, term_rows: list[PaintAnnotationRow]) -> dict[str, Any]:
    """Return the PAINT-determined fields this assessment lacks, in insertion order.

    ``term_rows`` are the family's PAINT rows for the assessment's node and term.
    Nothing is planned when PAINT records no row, or records the pair as both a gain and
    a loss (ambiguous). An existing key is never overwritten, even ``negated: false`` on a
    loss row, which the validator then reports for a curator to resolve.

    >>> from pathlib import Path
    >>> ird = PaintAnnotationRow("PTHR1", "PANTHER:PTN2", "GO:1", "F", "IRD", True,
    ...                          "PANTHER:PTN1", Path("x"))
    >>> planned_fields({"assessment": "UNRESOLVED"}, [ird])
    {'evidence': 'IRD', 'negated': True, 'seeds': [{'id': 'PANTHER:PTN1'}]}
    """
    negations = {row.negated for row in term_rows}
    if len(negations) != 1:
        return {}
    is_loss = negations == {True}
    evidences = sorted({row.evidence for row in term_rows} - {""})

    fields: dict[str, Any] = {}
    if "evidence" not in assessment and len(evidences) == 1:
        fields["evidence"] = evidences[0]
    if is_loss and "negated" not in assessment:
        fields["negated"] = True
    if is_loss and not assessment.get("seeds"):
        seeds = sorted(
            {
                piece
                for row in term_rows
                for piece in (row.seeds or "").split("|")
                if piece.startswith("PANTHER:PTN")
            }
        )
        if seeds:
            fields["seeds"] = [{"id": seed} for seed in seeds]
    return fields


def _render(fields: dict[str, Any], indent: str) -> list[str]:
    """Render planned fields as YAML lines at the assessment's key indent.

    >>> _render({"evidence": "IRD", "negated": True, "seeds": [{"id": "PANTHER:PTN1"}]}, "  ")
    ['  evidence: IRD', '  negated: true', '  seeds:', '  - id: PANTHER:PTN1']
    """
    lines: list[str] = []
    for key in FIELD_ORDER:
        if key not in fields:
            continue
        value = fields[key]
        if key == "seeds":
            lines.append(f"{indent}seeds:")
            lines.extend(f"{indent}- id: {seed['id']}" for seed in value)
        elif isinstance(value, bool):
            lines.append(f"{indent}{key}: {'true' if value else 'false'}")
        else:
            lines.append(f"{indent}{key}: {value}")
    return lines


def _assessment_nodes(text: str) -> list[yaml.MappingNode]:
    """Return the composed mapping node of each ``node_assessments`` item, in order."""
    root = yaml.compose(text)
    if not isinstance(root, yaml.MappingNode):
        return []
    for key, value in root.value:
        if key.value == "node_assessments" and isinstance(value, yaml.SequenceNode):
            return [item for item in value.value if isinstance(item, yaml.MappingNode)]
    return []


def _insertion_line(item: yaml.MappingNode) -> int:
    """Line index after which new keys go: the end of ``asserted_term``, else the first key."""
    keys = [key for key, _ in item.value]
    for i, key in enumerate(keys):
        if key.value == "asserted_term":
            if i + 1 < len(keys):
                return keys[i + 1].start_mark.line
            return item.end_mark.line
    return keys[0].start_mark.line + 1


def fill_review_text(
    text: str, family: str, paint_index: dict[str, list[PaintAnnotationRow]]
) -> tuple[str, list[FieldChange], list[str]]:
    """Fill missing PAINT fields into one family review's text.

    Returns the new text, the changes made, and the NODE_POLARITY problems that remain
    after filling (each needs a curator, usually to pick a LOSS_* verdict). Raises
    ``ValueError`` if an insertion would change anything other than the planned fields.
    """
    data = yaml.safe_load(text) or {}
    assessments = data.get("node_assessments") or []
    items = _assessment_nodes(text)
    if len(items) != len(assessments):
        raise ValueError(f"{family}: could not align node_assessments in the YAML text")

    lines = text.split("\n")
    inserts: list[tuple[int, list[str]]] = []
    changes: list[FieldChange] = []
    problems: list[str] = []
    expected = []
    for assessment, item in zip(assessments, items):
        node = str(assessment.get("node_id", ""))
        term = (assessment.get("asserted_term") or {}).get("id", "")
        rows = [
            row
            for row in paint_index.get(node, [])
            if row.family == family and row.go_id == term
        ]
        fields = planned_fields(assessment, rows)
        filled = {**assessment, **fields}
        expected.append(filled)
        if fields:
            indent = " " * item.value[0][0].start_mark.column
            inserts.append((_insertion_line(item), _render(fields, indent)))
            changes.append(FieldChange(node, term, fields))
        if rows:
            problem = node_polarity_problem(filled, rows)
            if problem:
                problems.append(f"{family} {node} {term}: {problem}")

    for at, new_lines in sorted(inserts, key=lambda pair: pair[0], reverse=True):
        lines[at:at] = new_lines
    new_text = "\n".join(lines)

    if changes:
        new_data = yaml.safe_load(new_text)
        if new_data.get("node_assessments") != expected or {
            k: v for k, v in new_data.items() if k != "node_assessments"
        } != {k: v for k, v in data.items() if k != "node_assessments"}:
            raise ValueError(f"{family}: inserted text did not parse to the planned edit")
    return new_text, changes, problems


def fill_review(
    path: Path, paint_index: dict[str, list[PaintAnnotationRow]], apply: bool
) -> tuple[list[FieldChange], list[str]]:
    """Fill one review file, writing it only when ``apply`` and something changed."""
    family = path.parent.name
    text = path.read_text()
    new_text, changes, problems = fill_review_text(text, family, paint_index)
    if apply and changes:
        path.write_text(new_text)
    return changes, problems


def main(argv: Iterable[str] | None = None) -> int:
    """Fill PAINT fields across family reviews; dry run unless ``--apply``.

    Exits 1 when an assessment still disagrees with PAINT after filling, so the
    remaining work (choosing a LOSS_* verdict) is visible.
    """
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "paths", nargs="*", type=Path,
        help="Family review YAML files; defaults to all under interpro/panther.",
    )
    parser.add_argument("--apply", action="store_true", help="Write the changes.")
    parser.add_argument("--panther-dir", type=Path, default=Path("interpro/panther"))
    args = parser.parse_args(list(argv) if argv is not None else None)

    paths = args.paths or sorted(args.panther_dir.glob("PTHR*/PTHR*-review.yaml"))
    paint_index = load_paint_index(args.panther_dir)
    files = fields = 0
    all_problems: list[str] = []
    for path in paths:
        changes, problems = fill_review(path, paint_index, args.apply)
        all_problems.extend(problems)
        if changes:
            files += 1
            fields += sum(len(c.fields) for c in changes)
            for c in changes:
                print(f"{path}: {c.node} {c.term} += {', '.join(c.fields)}")
    for problem in all_problems:
        print(f"NEEDS VERDICT: {problem}", file=sys.stderr)
    verb = "filled" if args.apply else "would fill"
    print(
        f"{verb} {fields} field(s) in {files} of {len(paths)} family review(s); "
        f"{len(all_problems)} assessment(s) still need a curator"
    )
    return 1 if all_problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
