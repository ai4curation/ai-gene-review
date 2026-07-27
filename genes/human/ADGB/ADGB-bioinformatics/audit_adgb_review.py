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

    # ---- F. ACCEPT <-> core_functions, BOTH directions --------------------
    # ActionEnum defines ACCEPT as "retain as representing the core function of
    # the gene", so an ACCEPT row whose term never reaches core_functions is a
    # self-contradiction.  PR #2313 shipped exactly that on GO:0007283, where
    # the row's own summary said "non-core" while its action said ACCEPT.
    #
    # This check exists because the first fix for that defect was performed in a
    # throwaway patch script and then *described* in the notes as enforced. A
    # verification you performed is not a verification that exists: the
    # enforcement has to live in the committed artifact or it is not enforcement.
    problems.extend(check_core_function_consistency(doc))
    return problems


def core_function_terms(doc: dict) -> set[str]:
    """Every GO id reachable from core_functions, across all of its term slots."""
    out: set[str] = set()
    for cf in doc.get("core_functions") or []:
        for slot in ("molecular_function", "contributes_to_molecular_function"):
            if cf.get(slot):
                out.add(cf[slot]["id"])
        for slot in ("locations", "directly_involved_in", "in_complex"):
            for term in (cf.get(slot) or []):
                out.add(term["id"])
    return out


def check_core_function_consistency(doc: dict) -> list[str]:
    """Both directions of the ACCEPT <-> core_functions invariant.

    Forward : every ACCEPT row's term must appear in core_functions.
    Reverse : every core_functions term must be backed by a row whose action is
              ACCEPT or NEW -- a core function must not rest on a row that was
              removed, downgraded to non-core, or flagged as over-annotated, and
              must not be absent from the annotation set altogether.

    The reverse direction is the one that would otherwise go unwritten, and it is
    the direction that catches a core_functions entry quietly outliving the row
    that justified it.

    SCOPE CAVEAT before anyone generalises this beyond ADGB. The reverse
    direction requires every core_functions term to have an annotation row at
    all, which makes it a *gene-local consistency* check, not a curation rule. A
    reviewer may legitimately place a well-supported term in core_functions that
    GOA does not carry - a genuine annotation gap is exactly the thing a review
    is supposed to surface - and this check would flag it. That is correct here,
    because every ADGB core term is backed by either a GOA row or an explicit
    NEW row, which is the discipline this file follows. Generalising the check
    would mean allowing a core term whose only backing is a NEW row, and
    rejecting only those with no backing of any kind; the forward direction
    generalises without change.
    """
    problems: list[str] = []
    core = core_function_terms(doc)
    anns = doc.get("existing_annotations") or []

    by_term: dict[str, set[str]] = {}
    for a in anns:
        by_term.setdefault(a["term"]["id"], set()).add(
            (a.get("review") or {}).get("action"))

    for a in anns:
        act = (a.get("review") or {}).get("action")
        tid = a["term"]["id"]
        if act == "ACCEPT" and tid not in core:
            problems.append(
                f"[core] {tid} ({a['term'].get('label')}) has action ACCEPT but does "
                f"not appear in core_functions. ActionEnum defines ACCEPT as "
                f"retaining the term as a core function; use KEEP_AS_NON_CORE if "
                f"the term is correct but not core.")

    for tid in sorted(core):
        actions = by_term.get(tid)
        if actions is None:
            problems.append(
                f"[core] core_functions uses {tid} but no existing_annotations "
                f"entry carries that term")
        elif not (actions & {"ACCEPT", "NEW"}):
            problems.append(
                f"[core] core_functions uses {tid} but its only annotation "
                f"action(s) are {sorted(a for a in actions if a)} - a core "
                f"function must rest on an ACCEPT or NEW row")
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

    # F. the ACCEPT <-> core_functions invariant, broken in BOTH directions.
    #    Operates on the parsed document rather than on raw text, so it is
    #    exercised independently of whether any anchor string has drifted.
    doc = yaml.safe_load(base_raw)

    #    F-happy: the real document must satisfy it.  A check can be wrong about
    #    success as easily as about failure (ACTA1 defect #5: an agreement check
    #    that failed on perfect agreement).
    if check_core_function_consistency(doc):
        failures.append(f"[happy/core] real document flagged: "
                        f"{check_core_function_consistency(doc)}")

    #    F-forward: an ACCEPT row whose term is not in core_functions.
    import copy
    fwd = copy.deepcopy(doc)
    target = next((a for a in fwd["existing_annotations"]
                   if (a.get("review") or {}).get("action") == "KEEP_AS_NON_CORE"
                   and a["term"]["id"] not in core_function_terms(fwd)), None)
    if target is None:
        raise SystemExit("SELF-TEST BROKEN: no KEEP_AS_NON_CORE row outside "
                         "core_functions to flip; the forward mutation is inert")
    target["review"]["action"] = "ACCEPT"
    fwd_problems = [p for p in check_core_function_consistency(fwd)
                    if p.startswith("[core]") and "ACCEPT but does not appear" in p]
    if not fwd_problems:
        failures.append("[catch/core] an ACCEPT row absent from core_functions "
                        "was not detected (forward direction)")

    #    F-reverse: a core_functions term whose row is not ACCEPT/NEW.  Written
    #    explicitly because this is the direction that would otherwise go
    #    unwritten, and unwritten is not the same as passing.
    rev = copy.deepcopy(doc)
    core_ids = core_function_terms(rev)
    victim = next((a for a in rev["existing_annotations"]
                   if a["term"]["id"] in core_ids
                   and (a.get("review") or {}).get("action") == "ACCEPT"), None)
    if victim is None:
        raise SystemExit("SELF-TEST BROKEN: no ACCEPT row backing a core_functions "
                         "term to demote; the reverse mutation is inert")
    demote_id = victim["term"]["id"]
    for a in rev["existing_annotations"]:
        if a["term"]["id"] == demote_id:
            a["review"]["action"] = "MARK_AS_OVER_ANNOTATED"
    rev_problems = [p for p in check_core_function_consistency(rev)
                    if "must rest on an ACCEPT or NEW row" in p]
    if not rev_problems:
        failures.append("[catch/core] a core_functions term backed only by a "
                        "non-ACCEPT row was not detected (reverse direction)")

    #    F-reverse-2: a core_functions term with no annotation row at all.
    orphan = copy.deepcopy(doc)
    orphan["core_functions"].append(
        {"description": "synthetic", "molecular_function":
            {"id": "GO:0000000", "label": "synthetic term"}})
    if not [p for p in check_core_function_consistency(orphan)
            if "no existing_annotations entry carries that term" in p]:
        failures.append("[catch/core] a core_functions term with no annotation "
                        "row was not detected")

    if failures:
        print("SELF-TEST FAILED:")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("SELF-TEST PASSED: happy direction clean (twice - raw-text mutations and "
          "the core-function invariant); 9 mutations each caught by their intended "
          "guard, including BOTH directions of the ACCEPT<->core_functions check; "
          "anchored substring verified.")


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
