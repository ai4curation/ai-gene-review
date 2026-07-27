#!/usr/bin/env python3
"""Invariant checks over the committed ADGRA1 review artifacts.

This exists because a check written in a scratch file gets described as
permanent by the same commit that throws it away. Everything asserted in the PR
body or in `ADGRA1-notes.md` that is *countable* is enforced here, against the
files as committed.

Checks:
  A. One `existing_annotations` entry per GOA data line, plus the NEW rows,
     counted separately -- no silent collapse of the 22 GO:0005515 rows.
  B. `supporting_entities` equals the GOA WITH/FROM field, row for row.
  C. The raw YAML parses under a duplicate-key-rejecting loader, and the raw
     count of `reference_id:` keys reconciles with the parsed count. (A duplicate
     key silently discards data *before* any quote gate can see it.)
  D. No YAML anchors/aliases -- an alias silently multiplies one object across
     rows, and every validator here walks the parsed tree.
  E. The verdict counts stated in ADGRA1-notes.md match the YAML.
  F. Every ACCEPT/NEW row's term appears in core_functions, AND every
     core_functions term is backed by an ACCEPT or NEW row. Both directions:
     unwritten is not the same as passing. (CC/BP terms are matched against
     locations/directly_involved_in, MF against molecular_function.)
  G. Withdrawn framings do not reappear. LIMITATION: this matches fixed phrases
     and CANNOT catch a paraphrase. Prose surfaces still need re-reading by hand
     when a claim is withdrawn.
  H. Every `file:` supporting_text that points at the UniProt record lies on ONE
     physical line of that file -- the repo validator does not check `file:`
     quotes, so a quote broken across a `CC       ` continuation passes silently.

Usage:
    uv run python audit_adgra1_claims.py
    uv run python audit_adgra1_claims.py --self-test
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE = HERE.parent
REPO = GENE.parents[2]
REVIEW = GENE / "ADGRA1-ai-review.yaml"
NOTES = GENE / "ADGRA1-notes.md"
GOA = GENE / "ADGRA1-goa.tsv"
UNIPROT = GENE / "ADGRA1-uniprot.txt"

N_NEW_EXPECTED = 2

# Framings considered and withdrawn while writing this review. Keeping them out
# matters because each is a *stronger* claim than the evidence carried.
WITHDRAWN_PHRASES = [
    # The GO:0004930 rows were nearly called over-annotations before PMID:41961591
    # was read; the term is in fact supported.
    "GO:0004930 is an over-annotation",
    "no evidence that ADGRA1 couples",
    "ADGRA1 does not couple to G proteins",
    # The 13 unquantified partners were nearly refuted from a placeholder value.
    "13 partners do not bind",
    "failed to bind",
    # The paralog-transfer hypothesis did NOT confirm; do not state it as found.
    "ADGRA2 biology propagated to ADGRA1",
    "Wnt terms leaked",
    # Round 2: the affinity ranking was stated inverted. Lower Kd is TIGHTER, so
    # MAST2 (4.9) and MAGI3 (5.1) are weaker than the retained DLG1 (4.6), and
    # DLG1 is itself the second-tightest binder in the dataset.
    "three tightest binders in the dataset",
    "three tightest binders in the whole dataset",
    "three tightest in the dataset",
    "all at or below the best retained partner",
    # The PDZ motif does NOT target the receptor to synapses.
    "PDZ-binding motif targets the receptor to synapses",
    "PDZ motif is required for synaptic localization",
    "PDZ motif is required for synaptic localisation",
]
WITHDRAWN_SCAN = ["ADGRA1-notes.md", "ADGRA1-ai-review.yaml", "ADGRA1-bioinformatics/RESULTS.md"]


class StrictLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys instead of silently keeping the last."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def goa_rows(path: Path = GOA) -> list[dict]:
    lines = path.read_text().rstrip("\n").split("\n")
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, ln.split("\t"))) for ln in lines[1:]]


def walk_reference_ids(node) -> list[str]:
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "reference_id" and isinstance(v, str):
                out.append(v)
            else:
                out.extend(walk_reference_ids(v))
    elif isinstance(node, list):
        for e in node:
            out.extend(walk_reference_ids(e))
    return out


def walk_supported(node):
    """Yield (reference_id, supporting_text) for every quote-bearing entry."""
    if isinstance(node, dict):
        if "supporting_text" in node and "reference_id" in node:
            yield node["reference_id"], node["supporting_text"]
        for v in node.values():
            yield from walk_supported(v)
    elif isinstance(node, list):
        for e in node:
            yield from walk_supported(e)


def audit(review_path: Path = REVIEW, notes_path: Path = NOTES,
          goa_path: Path = GOA) -> list[str]:
    problems: list[str] = []
    raw = review_path.read_text()

    # --- C (part 1): strict parse -------------------------------------------
    try:
        doc = yaml.load(raw, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as exc:
        return [f"C: duplicate YAML key -- data was silently discarded: {exc}"]
    except yaml.YAMLError as exc:
        # A malformed file must be reported, not raised through the caller: a
        # check that kills the harness is worse than no check, because the
        # harness still prints as though it ran.
        return [f"C: file does not parse as YAML: {exc}"]

    anns = doc.get("existing_annotations") or []
    rows = goa_rows(goa_path)
    new_rows = [a for a in anns if (a.get("review") or {}).get("action") == "NEW"]
    goa_anns = [a for a in anns if (a.get("review") or {}).get("action") != "NEW"]

    # --- A: coverage ---------------------------------------------------------
    if len(goa_anns) != len(rows):
        problems.append(
            f"A: {len(goa_anns)} non-NEW entries for {len(rows)} GOA rows "
            "-- a row is uncovered or was collapsed"
        )
    if len(new_rows) != N_NEW_EXPECTED:
        problems.append(f"A: expected {N_NEW_EXPECTED} NEW rows, found {len(new_rows)}")
    n_5515 = sum(1 for r in rows if r["GO TERM"] == "GO:0005515")
    n_5515_ann = sum(1 for a in goa_anns if a["term"]["id"] == "GO:0005515")
    if n_5515 != n_5515_ann:
        problems.append(
            f"A: {n_5515_ann} GO:0005515 entries for {n_5515} GOA rows -- partner rows collapsed"
        )

    # --- B: supporting_entities mirrors WITH/FROM ---------------------------
    if len(goa_anns) == len(rows):
        for a, r in zip(goa_anns, rows):
            want = [t for t in r["WITH/FROM"].split("|") if t]
            got = list(a.get("supporting_entities") or [])
            if got != want:
                problems.append(
                    f"B: {a['term']['id']}/{a['evidence_type']}: supporting_entities "
                    f"{got} != GOA WITH/FROM {want}"
                )

    # --- C (part 2): raw vs parsed reference_id count -----------------------
    # Anchor the regex: `reference_id:` is a substring of `original_reference_id:`.
    raw_ids = len(re.findall(r"^\s*(?:-\s*)?reference_id:", raw, re.M))
    parsed_ids = len(walk_reference_ids(doc))
    if raw_ids != parsed_ids:
        problems.append(
            f"C: raw reference_id keys {raw_ids} != parsed {parsed_ids} "
            "-- derive the expected number, do not rationalise the gap"
        )

    # --- D: no anchors -------------------------------------------------------
    if re.search(r"(?<![\w])&id\d+", raw) or re.search(r"(?<![\w*])\*id\d+", raw):
        problems.append("D: YAML anchor/alias present -- rows may be sharing one object")

    # --- E: notes counts match the YAML -------------------------------------
    acts = Counter((a.get("review") or {}).get("action") for a in goa_anns)
    notes = notes_path.read_text()
    m = re.search(r"\*\*ACCEPT (\d+), MODIFY (\d+)\*\*", notes)
    if not m:
        problems.append("E: notes verdict-count sentence not found (did the wording drift?)")
    else:
        want = {"ACCEPT": int(m.group(1)), "MODIFY": int(m.group(2))}
        got = {k: v for k, v in acts.items() if k in want}
        if got != want:
            problems.append(f"E: notes claim {want} but YAML has {dict(acts)}")
    m2 = re.search(r"Plus \*\*(\d+) NEW\*\*", notes)
    if not m2 or int(m2.group(1)) != len(new_rows):
        problems.append(f"E: notes NEW count does not match YAML ({len(new_rows)})")

    # --- F: ACCEPT/NEW terms <-> core_functions, both directions ------------
    cf = doc.get("core_functions") or []
    cf_mf = {t["id"] for c in cf for t in [c.get("molecular_function")] if t}
    cf_other = set()
    for c in cf:
        for slot in ("locations", "directly_involved_in", "contributes_to_molecular_function"):
            for t in c.get(slot) or []:
                cf_other.add(t["id"])
    cf_all = cf_mf | cf_other

    # A core function may be backed either by a row we kept (ACCEPT/NEW) or by a
    # term we are proposing to MODIFY *to* -- on this gene GO:0030165 is reached
    # only that way, from 22 GO:0005515 rows. Omitting the second source made the
    # check fire on a correct review, which is the failure mode where a guard is
    # wrong about success.
    kept = set()
    for a in anns:
        rev = a.get("review") or {}
        act = rev.get("action")
        if act in ("ACCEPT", "NEW"):
            kept.add(a["term"]["id"])
        elif act == "MODIFY":
            for t in rev.get("proposed_replacement_terms") or []:
                kept.add(t["id"])
    # Terms deliberately kept but intentionally NOT core: record them explicitly
    # so the exemption is visible rather than implied by the check's silence.
    NON_CORE_KEPT = {
        "GO:0007166",  # generic parent of the GPCR pathway term, kept as consistent
    }
    missing = kept - cf_all - NON_CORE_KEPT
    if missing:
        problems.append(
            f"F: ACCEPT/NEW terms absent from core_functions and not exempted: {sorted(missing)}"
        )
    unbacked = cf_all - kept
    if unbacked:
        problems.append(
            f"F: core_functions terms with no ACCEPT/NEW row behind them: {sorted(unbacked)}"
        )

    # --- G: withdrawn framings -----------------------------------------------
    # Scan the paths actually under audit, not the fixed committed ones: if the
    # detector's scope and the mutator's scope diverge, the self-test is
    # structurally blind and will report success for a mutation it cannot see.
    scan: list[tuple[str, Path]] = [
        (review_path.name, review_path),
        (notes_path.name, notes_path),
    ]
    for rel in WITHDRAWN_SCAN:
        p = GENE / rel
        if p.name in (review_path.name, notes_path.name, REVIEW.name, NOTES.name):
            continue
        scan.append((rel, p))
    for label, p in scan:
        if not p.exists():
            problems.append(f"G: scan target missing: {label}")
            continue
        text = p.read_text().lower()
        for phrase in WITHDRAWN_PHRASES:
            if phrase.lower() in text:
                problems.append(f"G: withdrawn framing {phrase!r} reappeared in {label}")

    # --- H: file: quotes into the UniProt record stay on one physical line ---
    up_lines = UNIPROT.read_text().split("\n")
    for ref, quote in walk_supported(doc):
        if not (isinstance(ref, str) and ref.endswith("ADGRA1-uniprot.txt")):
            continue
        if not any(quote in ln for ln in up_lines):
            problems.append(
                f"H: UniProt file: quote is not on any single physical line: {quote[:70]!r}"
            )
    return problems


# ------------------------------------------------------------------ self-test


def self_test() -> int:
    """Break-test every check in the direction it exists to catch, AND confirm
    the happy path is clean. A self-test proves the guards you thought of fire;
    it cannot tell you which guard you failed to write.
    """
    import copy
    import tempfile

    base = audit()
    if base:
        print("SELF-TEST: baseline is not clean, cannot mutate meaningfully:")
        for p in base:
            print("   ", p)
        return 1

    raw = REVIEW.read_text()
    doc = yaml.safe_load(raw)
    failures: list[str] = []

    def run_on(mutated_doc=None, mutated_raw=None, mutated_notes=None, label=""):
        with tempfile.TemporaryDirectory() as td:
            rp = Path(td) / "r.yaml"
            np_ = Path(td) / "n.md"
            if mutated_raw is not None:
                rp.write_text(mutated_raw)
            else:
                # Default to the UNMUTATED document, never to None -- writing
                # `null` would make every downstream check crash and the harness
                # would report a failure that has nothing to do with the mutation.
                rp.write_text(
                    yaml.dump(
                        doc if mutated_doc is None else mutated_doc,
                        sort_keys=False,
                        allow_unicode=True,
                    )
                )
            np_.write_text(mutated_notes if mutated_notes is not None else NOTES.read_text())
            return audit(rp, np_)

    # A: drop a GO:0005515 row.
    d = copy.deepcopy(doc)
    idx = next(i for i, a in enumerate(d["existing_annotations"]) if a["term"]["id"] == "GO:0005515")
    del d["existing_annotations"][idx]
    if not any(p.startswith("A:") for p in run_on(d)):
        failures.append("A did not fire on a deleted GO:0005515 row")

    # A, against THE DEFECT THAT ACTUALLY SHIPPED. `just fetch-gene` seeded 19
    # entries for 39 GOA rows because GOAValidator.seed_missing_annotations keys
    # on (term, evidence, reference, negated, qualifier) and omits WITH/FROM.
    # Replaying that exact key here must (a) reproduce 19 -- a number measured
    # from the real stub, not chosen -- and (b) make check A fire. A self-test
    # only proves the guards you thought of fire; reproducing the shipped defect
    # is the stronger claim.
    STUB_ENTRY_COUNT = 19
    d = copy.deepcopy(doc)
    seen, collapsed = set(), []
    for a in d["existing_annotations"]:
        if (a.get("review") or {}).get("action") == "NEW":
            continue
        key = (
            a["term"]["id"],
            a.get("evidence_type"),
            a.get("original_reference_id"),
            a.get("negated"),
            a.get("qualifier"),
        )
        if key in seen:
            continue
        seen.add(key)
        collapsed.append(a)
    if len(collapsed) != STUB_ENTRY_COUNT:
        failures.append(
            f"A: replaying the seeder key gives {len(collapsed)} entries, but the real "
            f"fetch-gene stub had {STUB_ENTRY_COUNT} -- the collapse model is wrong"
        )
    d["existing_annotations"] = collapsed
    probs = run_on(d)
    if not any(p.startswith("A:") and "collapsed" in p for p in probs):
        failures.append(
            f"A did not fire on the real seeder collapse (19 for 39) -- got {probs[:1]}"
        )

    # B: mutate a supporting_entities list.
    d = copy.deepcopy(doc)
    tgt = next(a for a in d["existing_annotations"] if a.get("supporting_entities"))
    tgt["supporting_entities"] = ["UniProtKB:P00000"]
    if not any(p.startswith("B:") for p in run_on(d)):
        failures.append("B did not fire on a rewritten supporting_entities list")

    # B (deletion form): a guard defeatable by deleting the thing it guards.
    d = copy.deepcopy(doc)
    tgt = next(a for a in d["existing_annotations"] if a.get("supporting_entities"))
    del tgt["supporting_entities"]
    if not any(p.startswith("B:") for p in run_on(d)):
        failures.append("B did not fire when supporting_entities was DELETED")

    # C: duplicate key. Injected into the raw text, since the parser is the point.
    # The anchor must carry its FULL indentation, or the replacement produces a
    # syntax error rather than a duplicate key and the mutation tests the wrong
    # thing while still appearing to pass.
    m_ind = re.search(r"^(\s+)action: ACCEPT$", raw, re.M)
    if not m_ind:
        failures.append("C mutation target string drifted -- mutation would be a no-op")
    else:
        anchor = m_ind.group(0) + "\n"
        mutated = raw.replace(anchor, anchor + m_ind.group(1) + "action: REMOVE\n", 1)
        if mutated == raw:
            failures.append("C mutation was a no-op")
        else:
            probs = run_on(mutated_raw=mutated)
            if not any(p.startswith("C: duplicate YAML key") for p in probs):
                failures.append(f"C did not fire on a duplicate YAML key (got {probs[:1]})")

    # D: anchors.
    if "existing_annotations:" not in raw:
        failures.append("D mutation target string drifted")
    else:
        mutated = raw.replace("existing_annotations:", "existing_annotations: &id001", 1)
        if not any(p.startswith("D:") for p in run_on(mutated_raw=mutated)):
            failures.append("D did not fire on an injected anchor")

    # E: notes/YAML count divergence.
    notes = NOTES.read_text()
    m = re.search(r"\*\*ACCEPT (\d+), MODIFY (\d+)\*\*", notes)
    if not m:
        failures.append("E mutation target string drifted")
    else:
        bad = notes.replace(m.group(0), "**ACCEPT 99, MODIFY 1**", 1)
        if not any(p.startswith("E:") for p in run_on(mutated_notes=bad)):
            failures.append("E did not fire on a wrong count in the notes")

    # F, direction 1: an ACCEPT term missing from core_functions.
    d = copy.deepcopy(doc)
    d["core_functions"][0]["molecular_function"] = {"id": "GO:0005515", "label": "protein binding"}
    if not any(p.startswith("F:") for p in run_on(d)):
        failures.append("F did not fire when a core_functions MF lost its ACCEPT backing")

    # F, direction 2: a core_functions term with no ACCEPT/NEW row.
    d = copy.deepcopy(doc)
    d["core_functions"][0]["locations"].append({"id": "GO:0005634", "label": "nucleus"})
    if not any("no ACCEPT/NEW row" in p for p in run_on(d)):
        failures.append("F did not fire on an unbacked core_functions location")

    # G: withdrawn phrase. Must be exercised on a file the scan actually reads.
    d = copy.deepcopy(doc)
    d["description"] = d["description"] + " GO:0004930 is an over-annotation."
    if not any(p.startswith("G:") for p in run_on(d)):
        failures.append("G did not fire on a withdrawn phrase in the review YAML")

    # H: a UniProt quote spanning a CC continuation.
    d = copy.deepcopy(doc)
    d["core_functions"][0]["supported_by"].append(
        {
            "reference_id": "file:human/ADGRA1/ADGRA1-uniprot.txt",
            "supporting_text": "SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane protein",
        }
    )
    if not any(p.startswith("H:") for p in run_on(d)):
        failures.append("H did not fire on a quote crossing a CC continuation line")

    for f in failures:
        print("SELF-TEST FAIL:", f)
    print(f"self-test: {len(failures)} problem(s)")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    problems = audit()
    for p in problems:
        print("FAIL:", p)
    print(f"audit: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
