"""AKAP12 review audit.

Invariants asserted (each corresponds to a failure this campaign has actually hit):

1. RAW vs PARSED: a duplicate YAML mapping key silently drops data, and every other gate
   walks the parsed document, so it cannot see the loss. Load with a strict loader that
   raises on duplicates, and reconcile raw occurrence counts against parsed counts.
2. ROW COVERAGE: every GOA TSV row has exactly one existing_annotations entry keyed on
   (term, evidence, reference, with/from); extras must be exactly the NEW rows.
3. SOURCE ENTITIES: propagation_review.source_entities is derived FROM the GOA WITH/FROM
   field, never by hand. Counts and ids must match by construction.
4. NO PENDING actions remain.
5. Reference ids used in supported_by/findings all exist in references[].
6. Species discipline: no experimental code (IDA/IPI/IMP/IGI/IEP/HDA) on a NEW row whose
   reason names a non-human-only system.
"""
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = None
for cand in [Path.cwd(), *Path.cwd().parents]:
    if (cand / "src").is_dir() and (cand / "publications").is_dir():
        ROOT = cand
        break
if ROOT is None:
    raise SystemExit("could not derive repo root")
print(f"root = {ROOT}")

YAML_PATH = ROOT / "genes/human/AKAP12/AKAP12-ai-review.yaml"
GOA_PATH = ROOT / "genes/human/AKAP12/AKAP12-goa.tsv"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


class StrictLoader(yaml.SafeLoader):
    pass


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(
                f"duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}"
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)

problems = []


def check(cond, msg):
    if not cond:
        problems.append(msg)


raw = YAML_PATH.read_text()
doc = yaml.load(raw, Loader=StrictLoader)  # raises on duplicate keys

# --- 1. raw vs parsed -------------------------------------------------------
# Anchored so `original_reference_id:` does not match `reference_id:`.
raw_ref_ids = len(re.findall(r"^\s*- reference_id:", raw, re.M))
parsed_ref_ids = 0


def walk(obj):
    global parsed_ref_ids
    if isinstance(obj, dict):
        if "reference_id" in obj:
            parsed_ref_ids += 1
        for v in obj.values():
            walk(v)
    elif isinstance(obj, list):
        for v in obj:
            walk(v)


walk(doc)
print(f"reference_id occurrences: raw={raw_ref_ids} parsed={parsed_ref_ids}")
check(
    raw_ref_ids == parsed_ref_ids,
    f"raw/parsed reference_id mismatch: {raw_ref_ids} vs {parsed_ref_ids}",
)

# --- 2. row coverage -------------------------------------------------------
goa_rows = []
with open(GOA_PATH) as fh:
    header = fh.readline().rstrip("\n").split("\t")
    idx = {name: i for i, name in enumerate(header)}
    for line in fh:
        f = line.rstrip("\n").split("\t")
        wf = tuple(sorted(t for t in f[idx["WITH/FROM"]].split("|") if t))
        goa_rows.append(
            (f[idx["GO TERM"]], f[idx["GO EVIDENCE CODE"]], f[idx["REFERENCE"]], wf)
        )

anns = doc["existing_annotations"]
new_rows = [a for a in anns if a["review"]["action"] == "NEW"]
goa_anns = [a for a in anns if a["review"]["action"] != "NEW"]

keys = [
    (
        a["term"]["id"],
        a["evidence_type"],
        a["original_reference_id"],
        tuple(sorted(a.get("supporting_entities") or [])),
    )
    for a in goa_anns
]
cg, ck = Counter(goa_rows), Counter(keys)
print(
    f"GOA rows={len(goa_rows)}  non-NEW entries={len(goa_anns)}  "
    f"NEW entries={len(new_rows)}  total entries={len(anns)}"
)
check(cg == ck, f"row coverage mismatch:\n  missing={cg - ck}\n  extra={ck - cg}")
check(
    len(anns) == len(goa_rows) + len(new_rows),
    "entry count does not equal GOA rows + NEW rows",
)

# --- 3. source_entities built from GOA WITH/FROM ---------------------------
wf_by_key = {k: set(k[3]) for k in goa_rows}
n_prop = 0
for a in goa_anns:
    pr = a["review"].get("propagation_review")
    if not pr:
        continue
    n_prop += 1
    k = (
        a["term"]["id"],
        a["evidence_type"],
        a["original_reference_id"],
        tuple(sorted(a.get("supporting_entities") or [])),
    )
    expected = wf_by_key[k]
    got = {e["source_id"] for e in pr.get("source_entities") or []}
    check(
        expected == got,
        f"{a['term']['id']} ({a['evidence_type']}) source_entities != GOA WITH/FROM:\n"
        f"      expected {sorted(expected)}\n      got      {sorted(got)}",
    )
    # a guard that cannot be defeated by deleting the thing it guards
    check(
        len(pr.get("source_entities") or []) == len(expected),
        f"{a['term']['id']}: source_entities count {len(pr.get('source_entities') or [])}"
        f" != WITH/FROM count {len(expected)}",
    )
    # root_cause must agree with the action, not merely be present
    action = a["review"]["action"]
    rc = pr["root_cause"]
    if action in {"MARK_AS_OVER_ANNOTATED", "REMOVE"}:
        check(
            rc not in {"NO_FAILURE_CORE", "NO_FAILURE_NON_CORE"},
            f"{a['term']['id']}: action {action} but root_cause {rc} asserts no failure",
        )
    if rc in {"NO_FAILURE_CORE", "NO_FAILURE_NON_CORE"}:
        check(
            not pr.get("failure_modes"),
            f"{a['term']['id']}: root_cause {rc} but failure_modes is non-empty",
        )
    else:
        check(
            bool(pr.get("failure_modes")),
            f"{a['term']['id']}: root_cause {rc} but no failure_modes recorded",
        )
print(f"propagation_review blocks checked: {n_prop}")
check(n_prop > 0, "no propagation_review blocks found - the check never ran")

# --- 4. no PENDING ---------------------------------------------------------
pending = [a["term"]["id"] for a in anns if a["review"]["action"] == "PENDING"]
check(not pending, f"PENDING actions remain: {pending}")
print("actions:", dict(Counter(a["review"]["action"] for a in anns)))

# --- 5. every cited reference_id is declared -------------------------------
declared = {r["id"] for r in doc["references"]}
cited = set()


def collect(obj):
    if isinstance(obj, dict):
        if "reference_id" in obj:
            cited.add(obj["reference_id"])
        for v in obj.values():
            collect(v)
    elif isinstance(obj, list):
        for v in obj:
            collect(v)


collect(doc)
undeclared = {c for c in cited if c.startswith(("PMID:", "GO_REF:"))} - declared
check(not undeclared, f"cited but not declared in references[]: {sorted(undeclared)}")

# --- 6. NEW rows: the species of the experiment must be stated --------------
# A keyword BLACKLIST ("does the reason mention rodent?") is the wrong shape: a reason may
# legitimately cite rodent work as corroboration while its primary evidence is human, and
# the blacklist cannot tell the two apart - it fired a false positive on GO:0005080, whose
# primary reference (PMID:9000000) assays human gravin fragments and only cites the rodent
# motif mapping as support. The invariant that actually matters is POSITIVE: an
# experimental code asserts the experiment was done in the annotated organism, so the
# reason must say so.
for a in new_rows:
    ev = a["evidence_type"]
    reason = a["review"]["reason"].lower()
    if ev in EXPERIMENTAL:
        check(
            "human" in reason,
            f"NEW {a['term']['id']} carries experimental code {ev} but its reason never "
            f"names the species the experiment was performed in",
        )
    if ev in {"ISS", "ISO"}:
        check(
            bool(a.get("supporting_entities")),
            f"NEW {a['term']['id']} is {ev} but has no supporting_entities",
        )
        check(
            any(s in reason for s in ("mouse", "rat", "rodent", "zebrafish")),
            f"NEW {a['term']['id']} is {ev} but its reason never names the source species",
        )
print("NEW rows:", [(a["term"]["id"], a["evidence_type"]) for a in new_rows])

# --- 7. retracted phrasings, checked over the CLASS not a site list ---------
# A hand-enumerated list of sites never terminates the "fixed in N places, landed in N-1"
# regress: fixing the `description` left an identical claim standing in a core_functions
# entry, found only by grepping the raw file. So this check is a pattern over the whole raw
# document, with no site list to go stale.
RETRACTED_PATTERNS = [
    (
        r"amphipathic",
        "gene-level secondary-structure claim: 'amphipathic' is textbook for the AKAP "
        "class but is not stated for AKAP12 in any cached source",
    ),
    (
        r"in fibroblasts SSeCKS suppresses",
        "PMID:20018890 used rat MAT-LyLu prostate carcinoma cells, not fibroblasts",
    ),
    (
        r"tumou?r suppressor activity of AKAP12|AKAP12 (?:is|acts as) a tumou?r suppressor",
        "tumour suppression is not an MF or a BP and must not be asserted as a function",
    ),
]
for pat, why in RETRACTED_PATTERNS:
    hits = [
        (i + 1, ln.strip())
        for i, ln in enumerate(raw.splitlines())
        if re.search(pat, ln, re.I)
    ]
    check(not hits, f"retracted phrasing /{pat}/ at lines {[h[0] for h in hits]} - {why}")

# Required claims. A raw occurrence COUNT with a hand-assigned floor is the wrong tool for
# the curation decisions: GO:0034237 appears 7 times, mostly in explanatory prose, so any
# floor low enough to be true is too low to notice one of the two MODIFY targets being
# swapped out - the self-test demonstrated exactly that. Derive the assertion from the
# PARSED structure instead of from a number I chose.
modify_targets = Counter()
for a in anns:
    for t in a["review"].get("proposed_replacement_terms") or []:
        modify_targets[t["id"]] += 1
check(
    modify_targets.get("GO:0034237") == 2,
    f"expected exactly 2 MODIFY rows targeting GO:0034237 (the PRKAR2A pair), "
    f"got {modify_targets.get('GO:0034237')}",
)
# GO:0008013 was PROPOSED for the CTNNB1 pair and then WITHDRAWN after measuring
# beta-catenin's IntAct promiscuity (1138 records vs AKAP12's 128). Assert the withdrawal
# held, and that both CTNNB1 rows still agree with each other - a partner split across two
# verdicts is the AADACL2/3/4 defect.
check(
    "GO:0008013" not in modify_targets,
    "GO:0008013 is a proposed_replacement_term again; it was withdrawn on promiscuity "
    "grounds and the CTNNB1 rows should be MARK_AS_OVER_ANNOTATED",
)
ctnnb1_actions = {
    a["review"]["action"]
    for a in anns
    if "UniProtKB:P35222" in (a.get("supporting_entities") or [])
}
check(
    ctnnb1_actions == {"MARK_AS_OVER_ANNOTATED"},
    f"the two CTNNB1 rows must share one verdict; got {ctnnb1_actions}",
)
egfr_actions = {
    a["review"]["action"]
    for a in anns
    if "UniProtKB:P00533" in (a.get("supporting_entities") or [])
}
check(
    egfr_actions == {"MARK_AS_OVER_ANNOTATED"},
    f"the two EGFR rows must share one verdict; got {egfr_actions}",
)
fhl1_actions = {
    a["review"]["action"]
    for a in anns
    if "UniProtKB:Q13642" in (a.get("supporting_entities") or [])
}
check(
    fhl1_actions == {"KEEP_AS_NON_CORE"},
    f"the three FHL1 rows must share one verdict; got {fhl1_actions}",
)
prkar2a_actions = {
    a["review"]["action"]
    for a in anns
    if "UniProtKB:P13861" in (a.get("supporting_entities") or [])
}
check(
    prkar2a_actions == {"MODIFY"},
    f"the two PRKAR2A rows must share one verdict; got {prkar2a_actions}",
)
check(
    modify_targets.get("GO:0007188") == 1,
    f"expected exactly 1 MODIFY row targeting GO:0007188, "
    f"got {modify_targets.get('GO:0007188')}",
)
check(
    "GO:0005515" not in modify_targets,
    "a MODIFY row proposes bare GO:0005515 protein binding as a replacement",
)

# The retracted paper must stay flagged, and nothing may cite it as support.
retracted = {
    r["id"] for r in doc["references"] if r.get("is_invalid") and r["id"] != "PMID:33091128"
}
check(
    "PMID:27683220" in retracted,
    "PMID:27683220 is retracted for data fabrication but is not flagged is_invalid",
)
check(
    not (retracted & cited),
    f"a retracted reference is used as supporting evidence: {sorted(retracted & cited)}",
)

check(
    "REGULATORY_SIGN_INVERSION" in raw,
    "the GO:0043116 sign-inversion finding is no longer recorded",
)

# --- report ---------------------------------------------------------------
print()
if problems:
    for p in problems:
        print(f"FAIL: {p}")
    print(f"\n{len(problems)} problem(s)")
    sys.exit(1)
print("all audit checks passed")
