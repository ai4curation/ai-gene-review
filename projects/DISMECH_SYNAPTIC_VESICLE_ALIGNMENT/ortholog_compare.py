"""Compare each human gene review with the ortholog and paralog reviews in the repository.

Usage, from the ai-gene-review root:

    uv run python projects/DISMECH_SYNAPTIC_VESICLE_ALIGNMENT/ortholog_compare.py \
        projects/DISMECH_SYNAPTIC_VESICLE_ALIGNMENT/ortholog-comparison.yaml

For every pair listed in PAIRS it reports, by GO id:

* ``opposed``: terms both reviews carry where one keeps the claim (ACCEPT,
  KEEP_AS_NON_CORE, TOO_GENERAL, NEW) and the other rejects it (REMOVE,
  MARK_AS_OVER_ANNOTATED), with no row on the rejecting side keeping it.
* ``core_only_in_human`` / ``core_only_in_other``: core-function terms
  (molecular function, directly_involved_in, locations) one review names as
  core and the other does not.
* ``core_rejected_by_other``: a core term of one review that the other review
  rejects on an annotation row. This is the strongest disagreement.

An opposed pair is a difference to read, not an error: the two reviews judge
different species' evidence, and an electronic transfer onto the human gene can
be over-annotation where the ortholog's own experimental row is sound.
GO:0005515 protein binding is left out; its removal is policy, not a verdict.
"""
import sys

import yaml

PAIRS = [
    ("human/STXBP1", ["rat/Stxbp1", "worm/unc-18"]),
    ("human/UNC13A", ["worm/unc-13"]),
    ("human/SYT1", ["rat/Syt1", "worm/snt-1"]),
    ("human/SNAP25", ["worm/ric-4"]),
    ("human/VAMP2", ["worm/snb-1"]),
    ("human/STX1B", ["worm/unc-64"]),
    ("human/CPLX1", ["worm/cpx-1", "DORPE/cpx"]),
    ("human/SYN1", ["worm/snn-1", "human/SYN2"]),
    ("human/DNM1", ["worm/dyn-1", "human/DNM2"]),
    ("human/ATP6V0C", ["worm/vha-1", "human/ATP6V0B"]),
    ("human/TSPOAP1", ["worm/rimb-1", "human/RIMBP2"]),
    ("human/CACNA2D4", ["human/CACNA2D1"]),
]
KEEP = {"ACCEPT", "KEEP_AS_NON_CORE", "TOO_GENERAL", "NEW"}
REJECT = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
SKIP = {"GO:0005515"}


def load(og):
    org, gene = og.split("/")
    path = f"genes/{org}/{gene}/{gene}-ai-review.yaml"
    d = yaml.safe_load(open(path))
    rows, labels = {}, {}
    for a in d.get("existing_annotations") or []:
        t = a.get("term") or {}
        if not t.get("id") or t["id"] in SKIP or a.get("negated"):
            continue
        labels[t["id"]] = t.get("label")
        rows.setdefault(t["id"], set()).add((a.get("review") or {}).get("action"))
    core = set()
    for cf in d.get("core_functions") or []:
        for key in ("molecular_function", "contributes_to_molecular_function"):
            t = cf.get(key)
            if isinstance(t, dict) and t.get("id"):
                core.add(t["id"]); labels[t["id"]] = t.get("label")
        for key in ("directly_involved_in", "locations"):
            for t in cf.get(key) or []:
                if isinstance(t, dict) and t.get("id"):
                    core.add(t["id"]); labels[t["id"]] = t.get("label")
    return dict(status=d.get("status"), rows=rows, core=core, labels=labels)


def kept(actions):
    return bool(actions & KEEP)


def rejected(actions):
    return bool(actions & REJECT) and not kept(actions) and "MODIFY" not in actions


out = []
for human, others in PAIRS:
    h = load(human)
    for other in others:
        o = load(other)
        lab = {**o["labels"], **h["labels"]}
        opposed = []
        for t in sorted(set(h["rows"]) & set(o["rows"])):
            ha, oa = h["rows"][t], o["rows"][t]
            if (kept(ha) and rejected(oa)) or (rejected(ha) and kept(oa)):
                opposed.append(dict(term=t, label=lab.get(t), human=sorted(ha), other=sorted(oa)))
        core_rej = []
        for t in sorted(h["core"]):
            if t in o["rows"] and rejected(o["rows"][t]):
                core_rej.append(dict(term=t, label=lab.get(t), core_in=human, rejected_in=other, actions=sorted(o["rows"][t])))
        for t in sorted(o["core"]):
            if t in h["rows"] and rejected(h["rows"][t]):
                core_rej.append(dict(term=t, label=lab.get(t), core_in=other, rejected_in=human, actions=sorted(h["rows"][t])))
        out.append(
            dict(
                human=human,
                other=other,
                human_status=h["status"],
                other_status=o["status"],
                shared_terms=len(set(h["rows"]) & set(o["rows"])),
                opposed=opposed,
                core_shared=[dict(term=t, label=lab.get(t)) for t in sorted(h["core"] & o["core"])],
                core_only_in_human=[dict(term=t, label=lab.get(t)) for t in sorted(h["core"] - o["core"])],
                core_only_in_other=[dict(term=t, label=lab.get(t)) for t in sorted(o["core"] - h["core"])],
                core_rejected_by_other=core_rej,
            )
        )

with open(sys.argv[1], "w") as fh:
    yaml.safe_dump(out, fh, sort_keys=False, width=110)

for r in out:
    print(
        f"{r['human']} vs {r['other']}: shared {r['shared_terms']}; opposed {len(r['opposed'])}; "
        f"core shared {len(r['core_shared'])}, human-only {len(r['core_only_in_human'])}, "
        f"other-only {len(r['core_only_in_other'])}; core rejected by other side {len(r['core_rejected_by_other'])}"
    )
