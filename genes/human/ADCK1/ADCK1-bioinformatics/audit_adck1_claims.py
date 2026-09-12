#!/usr/bin/env python3
"""Content audit for the ADCK1 review.

Asserts, per SITE rather than per occurrence-count, that (a) no retracted phrasing
survives anywhere, and (b) every place that discusses UbiB protein-kinase activity
carries the PMID:38425362 qualification. Occurrence-count thresholds were tried first
and were a guess; a site list is derivable from the documents themselves.
"""
import csv, pathlib, sys, yaml

ROOT = pathlib.Path("genes/human/ADCK1")
prob = []

RETRACTED = [
    "no UbiB-family protein has\n    been shown to phosphorylate a protein substrate in trans",
    "No UbiB protein has been shown to phosphorylate a protein substrate in trans",
    "No other ADCK-family gene has a merged review in\n  this repo",
    "serine/threonine-kinase keyword on ADCK1 has no family-level support",
]
SELF = pathlib.Path(__file__).resolve()


def is_claim_surface(f: pathlib.Path) -> bool:
    """Files that carry claims: not the gitignored venv, not the fetch cache."""
    if not f.is_file() or f.suffix not in (".yaml", ".md", ".py"):
        return False
    parts = set(f.parts)
    return ".venv" not in parts and "cache" not in parts


scanned = []
for f in sorted(filter(is_claim_surface, ROOT.rglob("*"))):
    if True:
        # This file quotes the retracted phrasings as literals in order to detect
        # them; scanning it would always self-trip. Excluded by identity, not by
        # name, and the exclusion is asserted to remove exactly one file.
        if f.resolve() == SELF:
            continue
        scanned.append(f)
        txt = f.read_text()
        for r in RETRACTED:
            if r in txt:
                prob.append(f"retracted phrasing in {f}: {r[:55]!r}")

rev = yaml.safe_load((ROOT / "ADCK1-ai-review.yaml").read_text())
notes = (ROOT / "ADCK1-notes.md").read_text()
results_md = (ROOT / "ADCK1-bioinformatics" / "RESULTS.md").read_text()

# Every SITE that discusses UbiB protein-kinase activity must qualify it.
def qualified(text: str) -> bool:
    return "38425362" in text

sites = {
    "core_functions[1].description": rev["core_functions"][1]["description"],
    "suggested_questions[0] (UniProt keywords)": rev["suggested_questions"][0]["question"],
    "references PMID:27499294 finding": next(
        r for r in rev["references"] if r["id"] == "PMID:27499294")["findings"][0]["statement"],
    "notes section 2": notes.split("## 3.")[0].split("## 2.")[1],
    "RESULTS.md 'What this supports'": results_md.split("## What this supports")[1],
}
for name, text in sites.items():
    ok = qualified(text)
    print(f"  {'OK  ' if ok else 'FAIL'} {name} qualifies with PMID:38425362")
    if not ok:
        prob.append(f"site {name} discusses UbiB kinase activity without the PMID:38425362 qualification")

# Every NUMBER the prose states about the motif scan must equal the computed value.
# The reviewer caught "absent in 0 of 8" where RESULTS.md computes "0/8 ... have an
# arginine" — the sentence had inverted its own table. Prose cannot be generated from
# results.json here, so instead each numeric claim is parsed back out and compared to
# the source of truth; divergence becomes a hard failure rather than a silent one.
import json
import re as _re

res = json.loads((ROOT / "ADCK1-bioinformatics" / "results.json").read_text())
n_ubib = res["n_total"] - 1
n_all4 = sum(
    1 for acc, row in res["proteins"].items()
    if acc != res["reference"]
    and all(row["motifs"][k]["matches_canonical"]
            for k in ("beta3_lys", "catalytic_asp", "catalytic_asn", "dfg_asp"))
)
desc = rev["core_functions"][1]["description"]
numeric_claims = [
    (r"conserved in (\d+) of (\d+) UbiB proteins examined", (n_all4, n_ubib),
     "all-four-motifs-conserved count"),
    (r"retaining (\d+) of the (\d+) canonical glycines", 
     (res["adck1_ploop_glycines_retained"], 3), "ADCK1 P-loop glycine count"),
    (r"an arginine present in (\d+) of (\d+) UbiB proteins examined",
     (res["n_ubib_with_arg_before_catalytic_asp"], n_ubib), "HRD-arginine count"),
]
for pattern, expected, label in numeric_claims:
    m = _re.search(pattern, desc)
    if not m:
        prob.append(f"core_functions[1].description no longer states the {label} "
                    f"in the expected form (/{pattern}/) — cannot verify it against results.json")
        continue
    got = (int(m.group(1)), int(m.group(2)))
    ok = got == expected
    print(f"  {'OK  ' if ok else 'FAIL'} {label}: prose says {got[0]}/{got[1]}, "
          f"results.json says {expected[0]}/{expected[1]}")
    if not ok:
        prob.append(f"{label}: prose {got[0]}/{got[1]} != computed {expected[0]}/{expected[1]}")

# ADCK1 must not assert a catalytic relationship to OPA1 in a structured slot while
# the prose denies one. `substrates` is an assertion in the reviewer's own voice.
for i, cf in enumerate(rev["core_functions"]):
    if cf.get("substrates"):
        prob.append(f"core_functions[{i}] declares substrates {cf['substrates']} while the review "
                    "states ADCK1 is not the protease; use the has_input extension instead")
    for slot in ("molecular_function", "contributes_to_molecular_function"):
        if cf.get(slot):
            prob.append(f"core_functions[{i}].{slot} asserts a molecular function, but this review "
                        "concludes ADCK1's molecular function is unknown")
print("  OK   no core_functions slot asserts a catalytic claim the prose refuses")

# The corrected sibling-review statement must name the real state of the repo.
for tok in ["COQ8A", "COQ8B", "#2108"]:
    if tok not in notes:
        prob.append(f"notes sibling-consistency section does not mention {tok}")
sib = notes.split("Sibling/paralog consistency")[1][:1400]
for tok in ["do** have merged reviews", "ADCK2", "ADCK5"]:
    if tok not in sib:
        prob.append(f"sibling-consistency section missing {tok!r}")

# PMID:38425362 must be a reviewed reference.
refs = {r["id"]: r for r in rev["references"]}
if "PMID:38425362" not in refs:
    prob.append("PMID:38425362 missing from references")
elif not refs["PMID:38425362"].get("reference_review", {}).get("correctness"):
    prob.append("PMID:38425362 has no reference_review.correctness")

# Coverage invariant, unchanged by the correction round.
tsv = list(csv.DictReader(open(ROOT / "ADCK1-goa.tsv"), delimiter="\t"))
acts = [a["review"]["action"] for a in rev["existing_annotations"]]
n_rev = sum(1 for a in acts if a != "NEW")
print(f"  GOA rows {len(tsv)} == reviewed {n_rev}: {len(tsv) == n_rev}")
if len(tsv) != n_rev:
    prob.append("coverage regressed")
if "PENDING" in acts:
    prob.append("PENDING actions remain")

all_candidates = list(filter(is_claim_surface, ROOT.rglob("*")))
if len(all_candidates) - len(scanned) != 1:
    prob.append(f"self-exclusion removed {len(all_candidates) - len(scanned)} files, expected exactly 1")
print(f"  scanned {len(scanned)} of {len(all_candidates)} candidate files (this script excluded)")

print()
for p in prob:
    print("PROBLEM:", p)
print("AUDIT CLEAN" if not prob else "AUDIT FAILED")
sys.exit(1 if prob else 0)
