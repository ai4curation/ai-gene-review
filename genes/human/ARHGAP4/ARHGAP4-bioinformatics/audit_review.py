#!/usr/bin/env python3
"""Invariants over ARHGAP4-ai-review.yaml that the repository validator does not cover.

Needs no network. Six checks, each covering a failure this repository has actually
shipped at least once:

1. **Row reconciliation** against the committed GOA TSV, by
   ``(term, evidence, reference, with/from)`` multiset. The ``fetch-gene`` stub is known
   to collapse distinct ``GO:0005515`` partner rows into one entry, so the correspondence
   is asserted rather than eyeballed.
2. **Duplicate YAML keys.** PyYAML keeps the last occurrence and discards the earlier one
   *silently*, and every other gate in this repo walks the parsed document -- so data
   destroyed by parsing cannot fail them.
3. **Quote verbatimness** for both ``PMID:`` and ``file:`` references. CI checks only the
   former, and an agent in this campaign fabricated two ``file:`` quotes that every gate
   passed.
4. **No line of a wrapped scalar ends in a hyphen.** YAML folds a newline into a space, so
   wrapping ``A-kinase-anchoring`` across lines silently publishes ``A-kinase- anchoring``.
   Both forms are legal YAML, so only rendering shows the damage.
5. **No row left PENDING**, no surviving ``TODO``, ``status: COMPLETE``.
6. **Reference completeness** -- every ``PMID:`` cited anywhere in the document resolves
   to a ``references`` entry. The repo validator only checks ``original_reference_id``, so
   a PMID named in a ``reason``, a ``review_notes`` or a ``knowledge_gap`` can dangle.
   The scan deliberately strips only the reference ``id`` fields: scanning the whole
   ``references`` block would let a deleted entry satisfy the check with its own id, and
   excluding the block entirely loses PMIDs cited only inside another entry's notes.

``--self-test`` mutates an in-memory copy for each check and requires the check to fire
with its own message; every mutation asserts its anchor matches **exactly once** first, so
a drifted anchor is an error rather than a silent pass. Negative controls are included and
must stay silent.

Run:  uv run python audit_review.py
      uv run python audit_review.py --self-test
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

GENE = "ARHGAP4"
ORGANISM = "human"


def repo_root() -> Path:
    """The repository root.

    Two markers, not one: ``genes/human/publications/`` exists in this repo as a
    stray artefact of an old cache-warming run, so a ``publications``-only probe
    resolves to ``genes/human`` and every path below it is then silently wrong.
    Requiring ``pyproject.toml`` alongside it pins the real root."""
    here = Path(__file__).resolve()
    return next(
        p
        for p in here.parents
        if (p / "publications").is_dir() and (p / "pyproject.toml").is_file()
    )


def gene_dir() -> Path:
    return repo_root() / "genes" / ORGANISM / GENE


def review_path() -> Path:
    return gene_dir() / f"{GENE}-ai-review.yaml"


class NoDuplicateLoader(yaml.SafeLoader):
    """SafeLoader that raises on a repeated mapping key instead of silently
    keeping the last one."""


def _no_dup_mapping(loader, node, deep=False):  # type: ignore[no-untyped-def]
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


NoDuplicateLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dup_mapping
)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# --------------------------------------------------------------------------- checks


def check_duplicate_keys(text: str) -> list[str]:
    try:
        yaml.load(text, Loader=NoDuplicateLoader)
    except yaml.constructor.ConstructorError as exc:
        return [f"duplicate YAML key: {exc}"]
    return []


def check_row_reconciliation(doc: dict, text: str) -> list[str]:
    tsv = gene_dir() / f"{GENE}-goa.tsv"
    with tsv.open() as fh:
        goa = [
            (
                r["GO TERM"],
                r["GO EVIDENCE CODE"],
                r["REFERENCE"],
                tuple(sorted(t for t in (r["WITH/FROM"] or "").split("|") if t)),
            )
            for r in csv.DictReader(fh, delimiter="\t")
        ]
    rows = [
        (
            a["term"]["id"],
            a["evidence_type"],
            a["original_reference_id"],
            tuple(sorted(a.get("supporting_entities") or [])),
        )
        for a in doc["existing_annotations"]
        if (a.get("review") or {}).get("action") != "NEW"
    ]
    problems = []
    if sorted(goa) != sorted(rows):
        missing = [g for g in goa if g not in rows]
        extra = [r for r in rows if r not in goa]
        problems.append(
            f"GOA/review row mismatch: {len(goa)} GOA rows vs {len(rows)} non-NEW "
            f"entries; missing={missing[:3]} extra={extra[:3]}"
        )
    return problems


def _iter_quotes(node, path="") -> list[tuple[str, str, str]]:
    """Yield (path, reference_id, supporting_text) for every quote in the document."""
    out: list[tuple[str, str, str]] = []
    if isinstance(node, dict):
        if "reference_id" in node and "supporting_text" in node:
            out.append((path, node["reference_id"], node["supporting_text"]))
        for k, v in node.items():
            out.extend(_iter_quotes(v, f"{path}/{k}"))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out.extend(_iter_quotes(v, f"{path}[{i}]"))
    return out


def check_quotes(doc: dict) -> list[str]:
    problems = []
    for path, ref, quote in _iter_quotes(doc):
        if ref.startswith("PMID:"):
            src = repo_root() / "publications" / f"PMID_{ref.split(':', 1)[1]}.md"
        elif ref.startswith("file:"):
            src = repo_root() / "genes" / ref.split(":", 1)[1]
        else:
            continue
        if not src.exists():
            problems.append(f"{path}: source for {ref} not found at {src}")
            continue
        if norm(quote) not in norm(src.read_text()):
            problems.append(f"{path}: quote not verbatim in {ref}: {quote[:70]!r}")
    return problems


def check_no_hyphen_line_endings(text: str) -> list[str]:
    """A wrapped plain/folded scalar whose line ends in '-' silently gains a space
    when YAML folds it. Structural lines (keys, list items) are exempt because they
    are not folded."""
    problems = []
    for n, line in enumerate(text.splitlines(), start=1):
        stripped = line.rstrip()
        if not stripped.endswith("-"):
            continue
        if re.match(r"^\s*-\s*$", stripped):  # a bare list indicator
            continue
        if re.match(r"^\s*[-\w\"']*[\w\"']\s*:\s*[|>]-?\s*$", stripped):  # block header
            continue
        problems.append(f"line {n} ends in a hyphen and will fold to '- ': {stripped[-50:]!r}")
    return problems


def check_no_pending(doc: dict, text: str) -> list[str]:
    problems = []
    pending = [
        a["term"]["id"]
        for a in doc["existing_annotations"]
        if (a.get("review") or {}).get("action") == "PENDING"
    ]
    if pending:
        problems.append(f"annotations still PENDING: {pending}")
    if doc.get("status") != "COMPLETE":
        problems.append(f"status is {doc.get('status')!r}, expected COMPLETE")
    if "TODO" in text:
        problems.append("document still contains TODO")
    return problems


REF_ID_LINE = re.compile(r"^- id: (PMID:\d+)\s*$", re.M)
PMID_TOKEN = re.compile(r"PMID:\d+")


def check_reference_completeness(text: str) -> list[str]:
    declared = set(REF_ID_LINE.findall(text))
    # Strip ONLY the reference id lines, so a deleted entry cannot satisfy the check
    # with its own id, while PMIDs cited inside another entry's notes still count.
    body = REF_ID_LINE.sub("", text)
    cited = set(PMID_TOKEN.findall(body))
    dangling = sorted(cited - declared)
    if dangling:
        return [f"PMIDs cited but not in references: {dangling}"]
    return []


def run_all(text: str) -> dict[str, list[str]]:
    doc = yaml.safe_load(text)
    return {
        "duplicate YAML keys": check_duplicate_keys(text),
        "GOA row reconciliation": check_row_reconciliation(doc, text),
        "quote verbatimness (PMID and file)": check_quotes(doc),
        "no hyphen at a folded line ending": check_no_hyphen_line_endings(text),
        "no PENDING / TODO, status COMPLETE": check_no_pending(doc, text),
        "reference completeness": check_reference_completeness(text),
    }


# ------------------------------------------------------------------------ self-test


def _mutate(text: str, anchor: str, replacement: str) -> str:
    n = text.count(anchor)
    if n != 1:
        raise AssertionError(
            f"self-test anchor matched {n} times, expected exactly 1: {anchor[:60]!r}"
        )
    return text.replace(anchor, replacement)


def self_test() -> int:
    text = review_path().read_text()
    checks: list[tuple[str, str]] = []

    # 0. NEGATIVE CONTROL: the real document must be clean.
    baseline = run_all(text)
    dirty = {k: v for k, v in baseline.items() if v}
    checks.append(
        (
            "negative control: unmutated document passes every check",
            "PASS" if not dirty else f"FAIL {dirty}",
        )
    )

    # 1. Duplicate key.
    m = _mutate(text, "\ngene_symbol: ARHGAP4\n", "\ngene_symbol: ARHGAP4\ngene_symbol: X\n")
    checks.append(
        (
            "duplicate key check fires",
            "PASS" if check_duplicate_keys(m) else "FAIL (silent)",
        )
    )

    # 2. A dropped GOA row.
    m = _mutate(
        text,
        "- term:\n    id: GO:0051056\n    label: regulation of small GTPase mediated signal transduction\n",
        "- term:\n    id: GO:9999999\n    label: bogus\n",
    )
    checks.append(
        (
            "GOA reconciliation fires on a changed term",
            "PASS" if check_row_reconciliation(yaml.safe_load(m), m) else "FAIL (silent)",
        )
    )

    # 3a. A fabricated PMID quote. The anchor carries its own indentation because the
    #     same sentence appears twice -- once under an annotation's supported_by (six
    #     spaces) and once under the reference's findings (four). Without it the
    #     exactly-once assertion fires, which is the guard doing its job.
    m = _mutate(
        text,
        "\n      supporting_text: A subset of these leading edge complexes are biochemically separable",
        "\n      supporting_text: ARHGAP4 was shown to be a dedicated RAC1-specific GAP in neutrophils",
    )
    fired = check_quotes(yaml.safe_load(m))
    checks.append(
        (
            "quote check fires on a fabricated PMID quote",
            "PASS" if any("not verbatim" in p for p in fired) else f"FAIL {fired}",
        )
    )

    # 3b. A fabricated file: quote -- the class CI does not cover.
    m = _mutate(
        text,
        "supporting_text: Residue identity and curated activity are decoupled in both directions.",
        "supporting_text: The arginine finger is absent from ARHGAP4.",
    )
    fired = check_quotes(yaml.safe_load(m))
    checks.append(
        (
            "quote check fires on a fabricated file: quote",
            "PASS" if any("not verbatim" in p for p in fired) else f"FAIL {fired}",
        )
    )

    # 4. A hyphen at a folded line ending.
    m = _mutate(
        text,
        "  combines an N-terminal F-BAR membrane-deforming module",
        "  combines an N-\n  terminal F-BAR membrane-deforming module",
    )
    checks.append(
        (
            "hyphen-fold check fires",
            "PASS" if check_no_hyphen_line_endings(m) else "FAIL (silent)",
        )
    )

    # 5a. A PENDING action.
    m = _mutate(text, "    action: MODIFY\n", "    action: PENDING\n")
    checks.append(
        (
            "PENDING check fires",
            "PASS" if check_no_pending(yaml.safe_load(m), m) else "FAIL (silent)",
        )
    )
    # 5b. A non-COMPLETE status.
    m = _mutate(text, "\nstatus: COMPLETE\n", "\nstatus: INITIALIZED\n")
    checks.append(
        (
            "status check fires",
            "PASS" if check_no_pending(yaml.safe_load(m), m) else "FAIL (silent)",
        )
    )

    # 6a. A dangling PMID.
    m = _mutate(text, "- id: PMID:16781893\n", "- id: PMID:16781890\n")
    fired = check_reference_completeness(m)
    checks.append(
        (
            "reference completeness fires on a dangling PMID",
            "PASS" if any("16781893" in p for p in fired) else f"FAIL {fired}",
        )
    )
    # 6b. NEGATIVE CONTROL for the scoping subtlety: deleting a reference entry whose
    #     PMID is cited nowhere else must still fire, i.e. the entry's own id line must
    #     not be able to satisfy the check for it.
    checks.append(
        (
            "negative control: an entry cannot satisfy the check with its own id",
            "PASS"
            if check_reference_completeness(
                "- id: PMID:11111111\n  title: x\nreason: nothing cites it\n"
            )
            == []
            and any(
                "22222222" in p
                for p in check_reference_completeness(
                    "- id: PMID:11111111\n  title: x\nreason: see PMID:22222222\n"
                )
            )
            else "FAIL",
        )
    )

    for name, verdict in checks:
        print(
            f"  [{verdict.split()[0]}] {name}"
            + ("" if verdict.startswith("PASS") else f" -- {verdict}")
        )
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    text = review_path().read_text()
    results = run_all(text)
    doc = yaml.safe_load(text)
    n_quotes = len(
        [q for q in _iter_quotes(doc) if q[1].startswith(("PMID:", "file:"))]
    )
    print(f"{len(doc['existing_annotations'])} annotation entries, {n_quotes} quotes checked\n")
    failed = 0
    for name, problems in results.items():
        print(f"  [{'FAIL' if problems else 'OK  '}] {name}")
        for p in problems:
            print(f"        {p}")
        failed += bool(problems)
    print(f"\n{len(results) - failed}/{len(results)} invariants hold")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
