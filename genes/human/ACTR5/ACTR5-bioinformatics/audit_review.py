#!/usr/bin/env python3
"""Lint for ACTR5-ai-review.yaml: mechanical checks that reading cannot do.

Run from the repo root or from this directory:

    uv run python audit_review.py

Checks
------
1.  **GOA coverage, both ways.** Every (term, evidence, reference, qualifier)
    tuple in ACTR5-goa.tsv is reviewed, and no non-NEW review row is absent
    from GOA.
2.  **`propagation_review.source_entities` are the GOA WITH/FROM tokens.**
    Compared token-by-token, because hand-maintained source lists drifted on
    every gene in this campaign that tried it.
3.  **IPI partners.** The union of `supporting_entities` on the `GO:0005515`
    rows equals the multiset of WITH/FROM partners in GOA, so no interaction
    partner is silently dropped when the seeded file's dedup is expanded.
4.  **Propagation review present** wherever the schema/validator expects it
    (IBA/IEA rows actioned REMOVE or MARK_AS_OVER_ANNOTATED).
5.  **Retracted / retracted-phrasing guard.** Claims this review deliberately
    does *not* make must not appear anywhere in the YAML, and claims it does
    make must appear the expected number of times. Both directions, because a
    claim asserted at five sites with no generation relationship between them
    was the failure mode that cost ACBD3 seven review rounds.

Every failure is a non-zero exit with the offending value printed. Verified to
fail by deliberate mutation, not by reading.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA = GENE_DIR / "ACTR5-goa.tsv"
REVIEW = GENE_DIR / "ACTR5-ai-review.yaml"

# Phrasings that would be wrong if they ever appeared. Each was considered and
# rejected during the review; see ACTR5-notes.md for why.
FORBIDDEN = {
    "actin filament": "ACTR5 retains only ~21% of the F-actin protomer interface; no filament claim is licensed",
    "polymeris": "ACTR5 cannot be expected to polymerise (see RESULTS.md); no polymerisation claim is licensed",
    "polymeriz": "same as above, US spelling",
    "ATP hydrolysis activity of ACTR5": "ACTR5 keeps only 2/5 actin catalytic positions; it is not an ATPase",
    "ATPase activity of ACTR5": "same as above",
    "INO80-independent function of ACTR5": "the INO80-independence claim is recorded as a knowledge gap, never asserted",
    "ATP binding": "the observed ligand in the ARP5 chain is ADP, never ATP; ACTR1A's rule is to annotate what is observed",
}
# Exceptions: substrings that legitimately contain a forbidden phrase.
ALLOWED_CONTEXTS = [
    "the ATP analog ADP",              # quoted methods phrasing
    "does not test an ADP-versus-ATP", # explicit statement of the caveat
    "ADP-versus-ATP preference",
    "neither hydrolyses the bound nucleotide nor polymerises",  # the negation, not the claim
]

# Claims that must be present, with their expected number of occurrences as a
# lower bound (0 means "at least once").
REQUIRED = {
    "nucleosomal DNA": 3,
    "ADP": 3,
    "contributes_to": 2,
    "GO:0031492": 2,
    "GO:0043531": 2,
    "acidic patch binding foot": 2,
    "in vivo relevant concentrations": 2,
}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    globals()["FAILURES"] += 1


FAILURES = 0


def main() -> int:
    global FAILURES
    if not GOA.exists() or not REVIEW.exists():
        raise SystemExit(f"ERROR: missing input; expected {GOA} and {REVIEW}")

    doc = yaml.safe_load(REVIEW.read_text())
    raw = REVIEW.read_text()
    rows = doc["existing_annotations"]

    goa = list(csv.DictReader(GOA.open(), delimiter="\t"))
    if not goa:
        raise SystemExit(f"ERROR: {GOA} parsed to zero rows — wrong delimiter or empty file")
    goa_tuples = [
        (g["GO TERM"], g["GO EVIDENCE CODE"], g["REFERENCE"], g["QUALIFIER"], g["WITH/FROM"])
        for g in goa
    ]

    # --- 1. coverage both ways
    goa_keys = {(t, e, r, q) for t, e, r, q, _ in goa_tuples}
    review_keys = {
        (a["term"]["id"], a["evidence_type"], a["original_reference_id"], a.get("qualifier", ""))
        for a in rows
        if a["review"]["action"] != "NEW"
    }
    for k in sorted(goa_keys - review_keys):
        fail(f"GOA annotation not reviewed: {k}")
    for k in sorted(review_keys - goa_keys):
        fail(f"non-NEW review row absent from GOA: {k}")

    # --- 2. source_entities == GOA WITH/FROM
    wf = {(t, e, r, q): [x for x in w.split("|") if x] for t, e, r, q, w in goa_tuples}
    n_prop = 0
    for a in rows:
        pr = a["review"].get("propagation_review")
        if not pr:
            continue
        n_prop += 1
        key = (a["term"]["id"], a["evidence_type"], a["original_reference_id"], a.get("qualifier", ""))
        expect = sorted(wf.get(key, []))
        got = sorted(s["source_id"] for s in pr.get("source_entities", []))
        if got != expect:
            fail(f"source_entities != GOA WITH/FROM for {key}: {got} vs {expect}")
    if n_prop == 0:
        fail("no propagation_review found at all — the check would pass vacuously")

    # --- 3. IPI partners
    goa_ipi = Counter(w for t, e, r, q, w in goa_tuples if e == "IPI")
    rev_ipi: Counter[str] = Counter()
    for a in rows:
        if a["evidence_type"] == "IPI" and a["review"]["action"] != "NEW":
            ents = a.get("supporting_entities") or []
            if not ents:
                fail(f"IPI row with no supporting_entities: {a['original_reference_id']}")
            rev_ipi.update(ents)
    if goa_ipi != rev_ipi:
        fail(f"IPI partner multiset mismatch: review={dict(rev_ipi)} goa={dict(goa_ipi)}")

    # --- 4. propagation_review required where validation expects it
    for a in rows:
        if a["evidence_type"] in ("IBA", "IEA", "ISS", "ISO", "IBD") and \
                a["review"]["action"] in ("REMOVE", "MARK_AS_OVER_ANNOTATED") and \
                not a["review"].get("propagation_review"):
            fail(f"{a['evidence_type']} row actioned {a['review']['action']} without "
                 f"propagation_review: {a['term']['id']}")

    # --- 5. forbidden / required phrasings.
    # Whitespace is normalised first: yaml.dump hard-wraps long scalars, so a
    # phrase can be split across lines and a raw-text scan would miss it. This
    # bit was found by the check reporting zero for a phrase that is present.
    flat = re.sub(r"\s+", " ", raw)
    scan = flat
    for ctx in ALLOWED_CONTEXTS:
        scan = scan.replace(ctx, " ")
    for phrase, why in FORBIDDEN.items():
        if phrase.lower() in scan.lower():
            fail(f"forbidden phrasing {phrase!r} present — {why}")
    for phrase, minimum in REQUIRED.items():
        n = len(re.findall(re.escape(phrase), flat))
        if n < max(minimum, 1):
            fail(f"required claim {phrase!r} appears {n} times, expected >= {max(minimum,1)}")

    actions = Counter(a["review"]["action"] for a in rows)
    print(f"reviewed rows: {len(rows)} (GOA data lines: {len(goa_tuples)}, "
          f"distinct GOA annotations: {len(goa_keys)})")
    print("actions:", dict(actions))
    print(f"propagation_review blocks checked against GOA WITH/FROM: {n_prop}")
    print(f"IPI partner rows: {sum(rev_ipi.values())}")
    if FAILURES:
        print(f"\n{FAILURES} failure(s)")
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
