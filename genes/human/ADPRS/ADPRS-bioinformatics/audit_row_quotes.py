#!/usr/bin/env python3
"""Check that each annotation's `supporting_text` is about the row it sits under.

The repo's reference validator checks that every `supporting_text` is a verbatim
substring of its cited publication. It does **not** check *relevance* — so a quote
about mitochondria attached to a `nucleus` row passes every automated gate while
supporting nothing. That failure has now occurred on four genes in this campaign, and
this file is the standing rule made executable for ADPRS.

The check
---------
For every entry in `existing_annotations`, at least one of:

1. some `supported_by` entry whose `supporting_text` matches one of the *topic patterns*
   declared for that GO term below; or
2. some `supported_by` entry carrying `full_text_unavailable: true` **and** a `reason`
   that explicitly states the limitation — the ADPRS pattern for "the cited paper cannot
   be quoted for this claim, here is what can".

Deliberate limitations, stated rather than implied
--------------------------------------------------
* Topic patterns are **hand-declared per GO term**, so this catches a quote that is
  about the wrong subject, not one that is about the right subject and still wrong.
  Judging whether a relevant sentence actually *entails* the claim is a reading task and
  is not mechanised here.
* Because the patterns are declared, **a new GO term with no entry fails loudly** rather
  than passing vacuously. Vacuous passing is the single most common way a guard in this
  campaign has reported coverage it did not have.

Usage
-----
    uv run python audit_row_quotes.py            # audit the committed review
    uv run python audit_row_quotes.py --self-test
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent / "ADPRS-ai-review.yaml"

# Topic patterns per GO term. A quote must mention the row's subject matter.
# Keep these keyed on the GO ID — the stable entity — never on the summary wording,
# which is what gets reworded.
TOPICS: dict[str, list[str]] = {
    "GO:0000287": [r"\bMg", r"magnesium"],
    "GO:0004553": [r"hydroly", r"glycosid", r"O-linkage"],
    "GO:0004649": [r"poly\(ADP-ribose\)", r"poly-\(ADP-ribose\)", r"\bPAR\b", r"PARylat", r"PARG activity"],
    "GO:0005515": [r"interact", r"two-hybrid", r"Y2H", r"binary PPI", r"HuRI"],
    "GO:0005634": [r"nucle"],
    "GO:0005654": [r"nucle"],
    "GO:0005694": [r"chromatin", r"chromosom", r"DNA lesion", r"histone"],
    "GO:0005737": [r"cytoso", r"cytoplasm"],
    "GO:0005739": [r"mitochondri"],
    "GO:0005759": [r"mitochondri"],
    "GO:0006281": [r"DNA damage", r"DNA repair", r"repair"],
    "GO:0006287": [r"mitochondri", r"poly\(ADP-ribose\)", r"repair"],
    "GO:0060546": [r"cell death", r"AIF", r"apoptosis inducing factor", r"apoptosis-inducing factor", r"parthanatos", r"necro"],
    "GO:0061463": [r"O-acetyl-ADP-ribose", r"OAADPr", r"acetyl"],
    "GO:0062099": [r"cell death", r"AIF", r"apoptosis inducing factor", r"apoptosis-inducing factor", r"parthanatos", r"necro"],
    "GO:0070301": [r"peroxide", r"H2O2", r"superoxide", r"oxidative"],
    "GO:0071451": [r"peroxide", r"H2O2", r"superoxide", r"oxidative"],
    "GO:0090734": [r"DNA lesion", r"DNA damage", r"recruit"],
    "GO:0140290": [r"serine", r"Ser-ADPr", r"Ser-linked", r"MARylat", r"de-?ADP-ribosyl", r"demodif"],
    "GO:0140292": [r"serine", r"Ser-ADPr", r"Ser-linked", r"MARylat", r"hydroly"],
}

LIMITATION_MARKERS = [
    "abstract-only",
    "full-text-unavailable",
    "cannot be quoted",
    "does not occur anywhere in the cached full text",
    "no gene-level quote from this paper is",
    "has no PMID",
]


def audit(doc: dict) -> list[str]:
    problems: list[str] = []
    anns = doc.get("existing_annotations")
    if not anns:
        # A guard that passes on an empty list is not a guard.
        return ["existing_annotations is missing or empty - nothing was audited"]
    for i, a in enumerate(anns):
        term = a["term"]["id"]
        row = f"[{i}] {term} {a.get('evidence_type')} {a.get('original_reference_id')}"
        if term not in TOPICS:
            problems.append(f"{row}: no topic pattern declared for {term} - add one, do not skip")
            continue
        review = a.get("review") or {}
        topic_terms = [term]
        for r in (review.get("proposed_replacement_terms") or []):
            rid = r.get("id") if isinstance(r, dict) else None
            if rid is None:
                problems.append(f"{row}: proposed_replacement_terms entry is not a Term object")
                continue
            if rid not in TOPICS:
                problems.append(f"{row}: no topic pattern declared for replacement {rid}")
                continue
            topic_terms.append(rid)
        pats = [re.compile(p, re.I) for tt in topic_terms for p in TOPICS[tt]]
        sbs = review.get("supported_by") or []
        if not sbs:
            problems.append(f"{row}: no supported_by at all")
            continue
        on_topic = [s for s in sbs if s.get("supporting_text")
                    and any(p.search(s["supporting_text"]) for p in pats)]
        if on_topic:
            continue
        declared = any(s.get("full_text_unavailable") for s in sbs)
        reason = review.get("reason") or ""
        stated = any(m in reason for m in LIMITATION_MARKERS)
        if declared and stated:
            continue
        quotes = " | ".join((s.get("supporting_text") or "<no text>")[:60] for s in sbs)
        problems.append(
            f"{row}: no quote matches the topics of {topic_terms}"
            + ("" if declared else " and no full_text_unavailable marker")
            + ("" if stated else " and the reason does not state a limitation")
            + f" -- quotes: {quotes}"
        )
    return problems


def self_test() -> int:
    """Break-tests. Each mutation is as fine-grained as the claim it certifies: a
    mutation that blanks a whole surface would be caught by a much weaker check."""
    problems: list[str] = []
    base = yaml.safe_load(REVIEW.read_text())

    if audit(base):
        problems.append("A: the committed review does not pass its own audit")

    # B. swap one row's quote for an on-topic-for-another-row quote. This is the exact
    #    defect the guard exists to catch, and it is finer than blanking: the quote is
    #    still verbatim, still present, still attached — only its subject is wrong.
    import copy
    mut = copy.deepcopy(base)
    victim = next(a for a in mut["existing_annotations"] if a["term"]["id"] == "GO:0005634")
    victim["review"]["supported_by"] = [
        {"reference_id": "PMID:22433848",
         "supporting_text": "embryonic fibroblasts from ARH3(-/-) mice lack most of the mitochondrial PAR degrading activity detected in wild-type cells"}
    ]
    victim["review"]["reason"] = "no limitation stated here"
    if not any("GO:0005634" in p for p in audit(mut)):
        problems.append("B: guard did not fire on a wrong-subject quote")

    # C. the limitation escape hatch must need BOTH halves. A full_text_unavailable
    #    marker without a stated limitation must still fail, or the hatch becomes a
    #    bypass for exactly the defect being guarded.
    mut2 = copy.deepcopy(base)
    v2 = next(a for a in mut2["existing_annotations"] if a["term"]["id"] == "GO:0005737")
    v2["review"]["supported_by"] = [{"reference_id": "PMID:16278211", "full_text_unavailable": True}]
    v2["review"]["reason"] = "nothing said about why"
    if not any("GO:0005737" in p for p in audit(mut2)):
        problems.append("C: marker without a stated limitation was accepted")

    # D. an undeclared GO term must fail loudly rather than pass vacuously.
    mut3 = copy.deepcopy(base)
    mut3["existing_annotations"][0]["term"]["id"] = "GO:9999999"
    if not any("GO:9999999" in p for p in audit(mut3)):
        problems.append("D: an undeclared term passed vacuously")

    # E. an empty annotation list must fail, not report success.
    if not audit({"existing_annotations": []}):
        problems.append("E: an empty review passed")

    # F. run the guard against the defect that actually shipped: commit aa019d486's
    #    GO:0005634 EXP row carried a mitochondrial-matrix quote. Reconstruct it.
    mut4 = copy.deepcopy(base)
    v4 = next(a for a in mut4["existing_annotations"]
              if a["term"]["id"] == "GO:0005634" and a.get("original_reference_id") == "PMID:17991898")
    v4["review"]["supported_by"] = [
        {"reference_id": "PMID:17991898",
         "supporting_text": "Both full-length ARH3 and a PARG isoform, which arises from alternative splicing, localized to the mitochondrial matrix."}
    ]
    v4["review"]["reason"] = ("Niere et al. mapped both PAR-degrading enzymes; ARH3 is a genuinely "
                              "multi-compartment protein and the nuclear pool is where it erases "
                              "chromatin Ser-ADPr.")
    if not any("GO:0005634" in p for p in audit(mut4)):
        problems.append("F: guard does not fire on the defect that actually shipped in aa019d486")

    for p in problems:
        print("SELF-TEST FAIL:", p)
    print(f"self-test: {len(problems)} problem(s)")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not REVIEW.exists():
        raise SystemExit(f"missing {REVIEW}. Fix with:  just fetch-gene human ADPRS")
    problems = audit(yaml.safe_load(REVIEW.read_text()))
    for p in problems:
        print("PROBLEM:", p)
    print(f"{len(yaml.safe_load(REVIEW.read_text())['existing_annotations'])} rows audited, "
          f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
