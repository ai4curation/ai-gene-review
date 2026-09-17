#!/usr/bin/env python3
"""Invariant checks over ARHGAP21-ai-review.yaml.

Each check exists because the corresponding failure is invisible to the repo
validator:

1. **Row reconciliation.**  The `fetch-gene` stub is known to collapse GOA rows
   (distinct `GO:0005515` partners, or same-term rows from different
   assigners, merging into one).  CLAUDE.md requires one entry per GOA line, so
   the counts are reconciled *by construction* against the TSV rather than by
   eye, and every GOA key must be matched.

2. **Duplicate YAML keys.**  PyYAML keeps the LAST occurrence of a duplicated
   mapping key and silently discards the earlier one.  Every other gate in this
   repo walks the *parsed* document, so data destroyed by parsing cannot fail
   them.  Detection requires a strict loader over the RAW text.

3. **Quote verbatimness.**  CI checks `supporting_text` only for `PMID:`
   references; `file:` quotes are unchecked.  Both are checked here.

4. **No row left PENDING**, and no `TODO` placeholder survives.

Self-test: `--self-test` mutates an in-memory copy for each check and asserts
the check fires.  A passing self-test proves the guards that exist work; it
cannot tell you which guard was never written.

Run:  uv run python audit_review.py [--self-test]
"""

from __future__ import annotations

import argparse
import copy
import sys
import unicodedata
from pathlib import Path

import yaml


def repo_root() -> Path:
    """Derive the root; never assert it.  A shared script with a hardcoded
    worktree path resolves quotes against the wrong publications/ cache and
    reports confident mass failures on clean work."""
    for parent in Path(__file__).resolve().parents:
        if (parent / "src").is_dir() and (parent / "publications").is_dir():
            return parent
    raise RuntimeError("cannot locate repo root (need src/ and publications/)")


ROOT = repo_root()
GENE_DIR = ROOT / "genes" / "human" / "ARHGAP21"
REVIEW = GENE_DIR / "ARHGAP21-ai-review.yaml"
GOA = GENE_DIR / "ARHGAP21-goa.tsv"


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicated mapping key instead of silently
    keeping the last one."""


def _no_dup(loader: yaml.Loader, node: yaml.MappingNode, deep: bool = False) -> dict:
    mapping: dict = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.YAMLError(f"duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dup
)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'),
                 ("”", '"'), ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    return " ".join(s.split())


def goa_keys() -> list[tuple[str, str, str, str]]:
    """(go_id, evidence, reference, with/from) for every GOA data row."""
    lines = GOA.read_text().rstrip("\n").split("\n")
    header = lines[0].split("\t")
    rows = [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]
    if not rows:
        raise RuntimeError(f"{GOA} has no data rows; run `just fetch-gene human ARHGAP21`")
    return [
        (
            r["GO TERM"],
            r["GO EVIDENCE CODE"],
            r["REFERENCE"],
            r.get("WITH/FROM", "").strip(),
        )
        for r in rows
    ]


def yaml_keys(doc: dict) -> list[tuple[str, str, str, str]]:
    out = []
    for a in doc["existing_annotations"]:
        if (a.get("review") or {}).get("action") == "NEW":
            continue
        se = a.get("supporting_entities") or []
        out.append(
            (
                a["term"]["id"],
                a["evidence_type"],
                a["original_reference_id"],
                "|".join(se),
            )
        )
    return out


def check_rows(doc: dict, problems: list[str]) -> None:
    g = sorted(goa_keys())
    y = sorted(yaml_keys(doc))
    if len(g) != len(y):
        problems.append(
            f"row count mismatch: GOA has {len(g)} data rows, review has {len(y)} "
            "non-NEW entries"
        )
    from collections import Counter

    gc, yc = Counter(g), Counter(y)
    for key in sorted(set(gc) | set(yc)):
        if gc[key] != yc[key]:
            problems.append(
                f"GOA/review multiplicity differs for {key}: GOA={gc[key]} review={yc[key]}"
            )


def check_pending(doc: dict, problems: list[str]) -> None:
    for i, a in enumerate(doc["existing_annotations"]):
        rev = a.get("review") or {}
        action = rev.get("action")
        if action in (None, "PENDING"):
            problems.append(f"annotation[{i}] ({a['term']['id']}) action={action!r}")
        for field in ("summary", "reason"):
            val = rev.get(field) or ""
            if "TODO" in val:
                problems.append(f"annotation[{i}] {field} still contains TODO")
    if "TODO" in (doc.get("description") or ""):
        problems.append("description still contains TODO")
    if doc.get("status") != "COMPLETE":
        problems.append(f"status is {doc.get('status')!r}, expected COMPLETE")


def _iter_quotes(node: object, out: list[tuple[str, str]]) -> None:
    if isinstance(node, dict):
        ref, txt = node.get("reference_id"), node.get("supporting_text")
        if isinstance(ref, str) and isinstance(txt, str) and txt.strip():
            out.append((ref, txt))
        for v in node.values():
            _iter_quotes(v, out)
    elif isinstance(node, list):
        for v in node:
            _iter_quotes(v, out)


def source_text(ref: str) -> tuple[str, str] | None:
    if ref.startswith("PMID:"):
        p = ROOT / "publications" / f"PMID_{ref.split(':', 1)[1]}.md"
        return (str(p), p.read_text()) if p.is_file() else None
    if ref.startswith("file:"):
        p = ROOT / "genes" / ref.split(":", 1)[1]
        return (str(p), p.read_text()) if p.is_file() else None
    return None  # GO_REF:/Reactome: carry no cached text; not checkable here


def check_quotes(doc: dict, problems: list[str]) -> int:
    quotes: list[tuple[str, str]] = []
    _iter_quotes(doc, quotes)
    checked = 0
    for ref, txt in quotes:
        src = source_text(ref)
        if src is None:
            if ref.startswith(("PMID:", "file:")):
                problems.append(f"{ref}: source not found for quote {txt[:60]!r}")
            continue
        checked += 1
        _, body = src
        if norm(txt) not in norm(body):
            problems.append(f"{ref}: supporting_text NOT verbatim: {txt[:90]!r}")
    return checked


def check_duplicate_keys(problems: list[str]) -> None:
    try:
        yaml.load(REVIEW.read_text(), Loader=StrictLoader)
    except yaml.YAMLError as exc:
        problems.append(f"strict YAML load failed: {exc}")


def run(doc: dict) -> tuple[list[str], int]:
    problems: list[str] = []
    check_rows(doc, problems)
    check_pending(doc, problems)
    n = check_quotes(doc, problems)
    return problems, n


def self_test(doc: dict) -> int:
    """Break each invariant and require the matching check to fire.

    Every mutation asserts its target is present first: a mutation whose anchor
    has drifted 'proves' the guard fires when nothing was broken.
    """
    failures = 0

    # 1. drop a GOA row
    d = copy.deepcopy(doc)
    before = len(d["existing_annotations"])
    d["existing_annotations"] = [
        a for a in d["existing_annotations"] if (a.get("review") or {}).get("action") != "NEW"
    ][:-1]
    assert len(d["existing_annotations"]) < before, "mutation 1 removed nothing"
    p: list[str] = []
    check_rows(d, p)
    if not p:
        print("SELF-TEST FAIL: dropping a GOA row was not detected")
        failures += 1

    # 2. leave a row PENDING
    d = copy.deepcopy(doc)
    assert d["existing_annotations"][0].get("review"), "mutation 2 anchor missing"
    d["existing_annotations"][0]["review"]["action"] = "PENDING"
    p = []
    check_pending(d, p)
    if not p:
        print("SELF-TEST FAIL: a PENDING row was not detected")
        failures += 1

    # 3. corrupt a quote
    d = copy.deepcopy(doc)
    quotes: list[tuple[str, str]] = []
    _iter_quotes(d, quotes)
    assert quotes, "mutation 3: no quotes found to corrupt"

    def corrupt(node: object) -> bool:
        if isinstance(node, dict):
            if isinstance(node.get("supporting_text"), str) and str(
                node.get("reference_id", "")
            ).startswith("PMID:"):
                node["supporting_text"] = node["supporting_text"] + " ZZQQ_NOT_REAL"
                return True
            for v in node.values():
                if corrupt(v):
                    return True
        elif isinstance(node, list):
            for v in node:
                if corrupt(v):
                    return True
        return False

    assert corrupt(d), "mutation 3 changed nothing"
    p = []
    check_quotes(d, p)
    if not p:
        print("SELF-TEST FAIL: a non-verbatim quote was not detected")
        failures += 1

    # 4. wrong status
    d = copy.deepcopy(doc)
    assert d.get("status") == "COMPLETE", "mutation 4 anchor missing"
    d["status"] = "INITIALIZED"
    p = []
    check_pending(d, p)
    if not any("status" in x for x in p):
        print("SELF-TEST FAIL: non-COMPLETE status was not detected")
        failures += 1

    # 5. duplicate YAML key (raw-text level)
    raw = REVIEW.read_text()
    anchor = "existing_annotations:"
    assert anchor in raw, "mutation 5 anchor missing"
    dup = raw.replace(anchor, anchor + "\n- {}\nexisting_annotations:", 1)
    assert dup != raw, "mutation 5 changed nothing"
    try:
        yaml.load(dup, Loader=StrictLoader)
        print("SELF-TEST FAIL: duplicate YAML key was not detected")
        failures += 1
    except yaml.YAMLError:
        pass

    print(f"self-test: {'PASS' if failures == 0 else f'{failures} FAILURES'}")
    return failures


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    problems: list[str] = []
    check_duplicate_keys(problems)
    doc = yaml.safe_load(REVIEW.read_text())

    p2, n_quotes = run(doc)
    problems.extend(p2)

    n_goa = len(goa_keys())
    n_entries = len(doc["existing_annotations"])
    n_new = sum(
        1
        for a in doc["existing_annotations"]
        if (a.get("review") or {}).get("action") == "NEW"
    )
    print(f"GOA data rows          : {n_goa}")
    print(f"existing_annotations   : {n_entries}  (= {n_entries - n_new} GOA + {n_new} NEW)")
    print(f"supporting_text quotes : {n_quotes} checked verbatim")

    rc = 0
    if args.self_test:
        rc |= 1 if self_test(doc) else 0

    if problems:
        print(f"\n{len(problems)} PROBLEM(S):")
        for x in problems:
            print("  -", x)
        return 1
    print("\nno problems")
    return rc


if __name__ == "__main__":
    sys.exit(main())
