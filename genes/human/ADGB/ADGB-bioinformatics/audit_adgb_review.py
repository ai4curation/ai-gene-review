"""Invariant checks on ADGB-ai-review.yaml that no repo validator performs.

Three classes of defect this campaign has repeatedly shipped, none of which
`just validate` or `checkquotes.py` can see, because all three walk the *parsed*
document or check only schema shape:

  A. A duplicate YAML mapping key silently DELETES data.  PyYAML keeps the last
     occurrence and discards the earlier one with no warning, so a quote that
     parsing removed cannot fail a quote checker.  Detected by loading with a
     strict loader that raises on repeats, AND by reconciling a raw grep count
     against the parsed count.

  B. `supporting_entities` / `propagation_review.source_entities` drift from the
     GOA WITH/FROM column.  Hand-maintained lists have drifted on every gene that
     tried it.  Here they are DERIVED from the TSV and compared, so a mismatch is
     an error rather than something to notice by eye.

  C. Row-count reconciliation.  The `fetch-gene` stub keys on
     (GO ID, evidence, reference, negated, qualifier) and omits WITH/FROM, so
     per-partner rows can collapse.  Counted against *distinct* GOA rows, not raw
     line count, because byte-identical duplicate lines are a legitimate reason
     for the numbers to differ.

Run:
    uv run python audit_adgb_review.py             # audit
    uv run python audit_adgb_review.py --self-test # break the guards, both ways
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ADGB-ai-review.yaml"
GOA = GENE_DIR / "ADGB-goa.tsv"

# GOA TSV is 16 columns; term is $5, evidence $9, reference $10, with/from $11,
# qualifier $4.  Indices are 0-based here and asserted against the header so an
# upstream column change fails loudly instead of silently matching nothing.
EXPECTED_HEADER_FIELDS = {
    "QUALIFIER": 3, "GO TERM": 4, "GO EVIDENCE CODE": 8,
    "REFERENCE": 9, "WITH/FROM": 10,
}


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys instead of dropping data."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"DUPLICATE KEY {key!r} - PyYAML would silently discard the "
                f"earlier value, deleting data no quote checker can see",
                key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


def read_goa(path: Path) -> list[dict]:
    with path.open() as fh:
        rows = list(csv.reader(fh, delimiter="\t"))
    header = rows[0]
    for name, idx in EXPECTED_HEADER_FIELDS.items():
        if header[idx] != name:
            raise SystemExit(
                f"FATAL: GOA column layout changed - expected {name!r} at index "
                f"{idx}, found {header[idx]!r}. Fix EXPECTED_HEADER_FIELDS "
                f"rather than letting the audit silently match nothing.")
    out = []
    for r in rows[1:]:
        if not r:
            continue
        out.append({
            "qualifier": r[3], "term": r[4], "evidence": r[8],
            "reference": r[9],
            "withfrom": [t for t in r[10].split("|") if t],
        })
    return out


def goa_key(row: dict) -> tuple:
    return (row["term"], row["evidence"], row["reference"], row["qualifier"])


def ann_key(a: dict) -> tuple:
    return (a["term"]["id"], a.get("evidence_type", ""),
            a.get("original_reference_id", ""), a.get("qualifier", ""))


def audit(review_path: Path = REVIEW, goa_path: Path = GOA) -> list[str]:
    problems: list[str] = []
    raw = review_path.read_text()

    # ---- A. duplicate keys -------------------------------------------------
    try:
        doc = yaml.load(raw, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as exc:
        problems.append(f"[dupkey] {exc}")
        doc = yaml.safe_load(raw)

    # raw-vs-parsed reconciliation on the field most often duplicated.
    # Anchored: 'reference_id:' also matches 'original_reference_id:' (ACTG2).
    raw_refs = len(re.findall(r"^\s*- reference_id:", raw, re.M))
    parsed_refs = 0

    def count(node):
        nonlocal parsed_refs
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "supported_by" and isinstance(v, list):
                    parsed_refs += sum(
                        1 for e in v if isinstance(e, dict) and "reference_id" in e)
                count(v)
        elif isinstance(node, list):
            for e in node:
                count(e)

    count(doc)
    if raw_refs != parsed_refs:
        problems.append(
            f"[dupkey] raw '- reference_id:' occurrences ({raw_refs}) != parsed "
            f"supported_by entries ({parsed_refs}). Do NOT find a story that "
            f"makes the gap acceptable - derive the expected number independently.")

    # ---- C. row-count reconciliation --------------------------------------
    goa = read_goa(goa_path)
    distinct_goa = {tuple(sorted(r.items(), key=lambda kv: kv[0]))
                    if False else (r["term"], r["evidence"], r["reference"],
                                   r["qualifier"], tuple(r["withfrom"]))
                    for r in goa}
    anns = doc["existing_annotations"]
    new_anns = [a for a in anns
                if (a.get("review") or {}).get("action") == "NEW"]
    goa_anns = [a for a in anns
                if (a.get("review") or {}).get("action") != "NEW"]
    if len(goa_anns) != len(distinct_goa):
        problems.append(
            f"[rows] {len(goa_anns)} non-NEW annotations vs {len(distinct_goa)} "
            f"distinct GOA rows ({len(goa)} raw). Reconcile explicitly.")

    # every GOA row must be covered, and nothing invented
    goa_keys = Counter(goa_key(r) for r in goa)
    ann_keys = Counter(ann_key(a) for a in goa_anns)
    for k, n in goa_keys.items():
        if ann_keys.get(k, 0) != n:
            problems.append(f"[rows] GOA row {k} appears {n}x in TSV but "
                            f"{ann_keys.get(k, 0)}x in the review")
    for k, n in ann_keys.items():
        if goa_keys.get(k, 0) != n:
            problems.append(f"[rows] review row {k} appears {n}x but "
                            f"{goa_keys.get(k, 0)}x in GOA")

    # ---- B. supporting_entities derived from GOA, not by hand -------------
    by_key: dict[tuple, list] = {}
    for r in goa:
        by_key.setdefault(goa_key(r), []).extend(r["withfrom"])
    for a in goa_anns:
        k = ann_key(a)
        expected = sorted(set(by_key.get(k, [])))
        got = sorted(set(a.get("supporting_entities") or []))
        if expected != got:
            problems.append(
                f"[withfrom] {k[0]} {k[1]}: supporting_entities {got} != GOA "
                f"WITH/FROM {expected}")
        # source_entities, where present, must be a subset of the WITH/FROM set
        pr = ((a.get("review") or {}).get("propagation_review") or {})
        se = [e["source_id"] for e in (pr.get("source_entities") or [])]
        if se:
            # ASSERT PRESENCE, don't just validate on match: a guard that skips
            # unmatched entries passes when the entity is deleted (ACTA1 #1).
            missing = [x for x in expected if x not in se]
            extra = [x for x in se if x not in expected]
            if missing or extra:
                problems.append(
                    f"[withfrom] {k[0]} {k[1]}: source_entities {sorted(se)} does "
                    f"not match WITH/FROM {expected} (missing={missing}, extra={extra})")

    # ---- D. propagation_review present where the schema needs it ----------
    for a in anns:
        rv = a.get("review") or {}
        act = rv.get("action")
        ev = a.get("evidence_type")
        if act in ("REMOVE", "MARK_AS_OVER_ANNOTATED") and ev in ("IBA", "ISS", "IEA"):
            if not rv.get("propagation_review"):
                problems.append(
                    f"[prop] {a['term']['id']} {ev} {act} has no propagation_review")

    # ---- E. NEW annotations must not reuse a GOA reference id blindly -----
    for a in new_anns:
        if str(a.get("original_reference_id", "")).startswith("GO_REF:"):
            problems.append(
                f"[new] NEW annotation {a['term']['id']} cites a GO_REF; a "
                f"proposed annotation needs a real evidence source")
    return problems


# --------------------------------------------------------------------------- #
def self_test() -> None:
    """Break every guard in the direction it exists to catch AND in the happy one.

    A self-test proves the guards you thought of fire; it cannot tell you which
    guard you failed to write.  It is necessary and nowhere near sufficient.
    """
    import tempfile

    failures: list[str] = []
    base_raw = REVIEW.read_text()
    base_goa = GOA.read_text()

    def run(raw=None, goa=None) -> list[str]:
        with tempfile.TemporaryDirectory() as td:
            rp = Path(td) / "r.yaml"
            gp = Path(td) / "g.tsv"
            rp.write_text(raw if raw is not None else base_raw)
            gp.write_text(goa if goa is not None else base_goa)
            return audit(rp, gp)

    # HAPPY DIRECTION FIRST.  A check can be wrong about success as easily as
    # about failure - ACTA1's agreement check failed on *perfect* agreement.
    clean = run()
    if clean:
        failures.append(f"[happy] unmodified files must audit clean, got: {clean}")

    def mutate(anchor: str, replacement: str, raw: str = base_raw) -> str:
        # Assert the anchor is present BEFORE mutating: a self-test whose target
        # string has drifted "proves" the guard fires when nothing was broken.
        if anchor not in raw:
            raise SystemExit(f"SELF-TEST BROKEN: anchor absent: {anchor!r}")
        return raw.replace(anchor, replacement, 1)

    # A. duplicate key must be caught
    dup = mutate("  evidence_type: IBA\n  original_reference_id: GO_REF:0000033",
                 "  evidence_type: IBA\n  evidence_type: IBA\n"
                 "  original_reference_id: GO_REF:0000033")
    if not any(p.startswith("[dupkey]") for p in run(raw=dup)):
        failures.append("[catch] duplicate mapping key not detected")

    # B1. a deleted supporting_entities token must be caught
    drop = mutate("  - MGI:MGI:3605549\n  - PANTHER:PTN002922608\n",
                  "  - PANTHER:PTN002922608\n")
    if not any(p.startswith("[withfrom]") for p in run(raw=drop)):
        failures.append("[catch] dropped supporting_entities token not detected")

    # B2. a deleted source_entities block must be caught, not skipped.  This is
    #     the ACTA1 defect: a loop that `continue`s on non-match passes silently
    #     when the entity is deleted.
    killed = mutate(
        "      - source_id: PANTHER:PTN002922608\n"
        "        source_label: PANTHER internal tree node in PTHR46298 (Androglobin-like)\n",
        "      - source_id: PANTHER:WRONGNODE\n"
        "        source_label: PANTHER internal tree node in PTHR46298 (Androglobin-like)\n")
    if not any(p.startswith("[withfrom]") for p in run(raw=killed)):
        failures.append("[catch] relabelled source_id not detected")

    # C. a removed annotation must be caught
    cut = base_raw.replace(
        "- term:\n    id: GO:0031514\n    label: motile cilium\n", "- term:\n"
        "    id: GO:0031514\n    label: motile cilium\n  RETIRED_MARKER: true\n", 1)
    missing_row = re.sub(
        r"- term:\n    id: GO:0031514.*?(?=\n- term:)", "", base_raw, flags=re.S)
    if missing_row == base_raw:
        raise SystemExit("SELF-TEST BROKEN: row-deletion mutation was a no-op")
    if not any(p.startswith("[rows]") for p in run(raw=missing_row)):
        failures.append("[catch] deleted annotation row not detected")
    del cut

    # C2. GOA column shift must fail loudly rather than matching nothing
    shifted = "\n".join(
        ["\t".join(["X"] + line.split("\t")) for line in base_goa.splitlines()])
    try:
        run(goa=shifted)
        failures.append("[catch] GOA column shift did not raise")
    except SystemExit:
        pass

    # D. removing a propagation_review from a REMOVE row must be caught
    noprop = re.sub(r"    propagation_review:\n      root_cause: PROPAGATION_BAD.*?"
                    r"(?=\n- term:)", "", base_raw, count=1, flags=re.S)
    if noprop == base_raw:
        raise SystemExit("SELF-TEST BROKEN: propagation_review mutation was a no-op")
    if not any(p.startswith("[prop]") for p in run(raw=noprop)):
        failures.append("[catch] missing propagation_review on a REMOVE not detected")

    # E. anchored-substring test: 'reference_id:' must not match
    #    'original_reference_id:'  (the ACTG2 substring trap)
    probe = "  original_reference_id: PMID:1\n  - reference_id: PMID:2\n"
    n = len(re.findall(r"^\s*- reference_id:", probe, re.M))
    if n != 1:
        failures.append(f"[anchor] reference_id regex matched {n} times, expected 1")

    if failures:
        print("SELF-TEST FAILED:")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("SELF-TEST PASSED: happy direction clean; 6 mutations each caught by "
          "their intended guard; anchored substring verified.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    problems = audit()
    goa = read_goa(GOA)
    doc = yaml.safe_load(REVIEW.read_text())
    anns = doc["existing_annotations"]
    new = [a for a in anns if (a.get("review") or {}).get("action") == "NEW"]
    print(f"GOA rows (raw)            : {len(goa)}")
    print(f"GOA rows (distinct)       : "
          f"{len({(r['term'], r['evidence'], r['reference'], r['qualifier'], tuple(r['withfrom'])) for r in goa})}")
    print(f"existing_annotations      : {len(anns)}  "
          f"({len(anns) - len(new)} reviewing GOA + {len(new)} proposed NEW)")
    print(f"actions                   : "
          f"{dict(Counter((a.get('review') or {}).get('action') for a in anns))}")
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("\nAll invariants hold.")


if __name__ == "__main__":
    main()
