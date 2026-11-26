"""Score the same GO rules on OUR review calls (accepted/kept/modified/new rows + core_functions)."""
import collections
import yaml
from common import RESULTS, benchmark, reviewed_human, term_sets

truth, ours, T = benchmark(), reviewed_human(), term_sets()


def review_terms(d):
    y = yaml.safe_load(open(f"genes/human/{d}/{d}-ai-review.yaml"))
    out, core = set(), set()
    for a in y.get("existing_annotations") or []:
        if a.get("negated"):
            continue
        rv = a.get("review") or {}
        act = rv.get("action")
        if act in ("ACCEPT", "KEEP_AS_NON_CORE", "NEW"):
            out.add(a["term"]["id"])
        if act == "MODIFY":
            out |= {p.get("id") for p in rv.get("proposed_replacement_terms") or []}
    for c in y.get("core_functions") or []:
        core |= {l.get("id") for l in c.get("locations") or []}
        if c.get("molecular_function"):
            out.add(c["molecular_function"].get("id"))
    return out | core, core


rows, res = [], collections.Counter()
for a, r in truth.items():
    d = ours.get(a) or r["gene_symbol"]
    t, core = review_terms(d)
    r1 = bool(t & T["OUT_CC"])
    r2 = r1 or (bool(t & T["PM"]) and bool(t & T["TM_MF"]))
    outcall = "core" if core & T["OUT_CC"] else ("non-core" if r1 else "none")
    for name, v in (("R1", r1), ("R2", r2), ("R0", bool(t & T["PM"]))):
        res[(name, r["truth_verdict"], v)] += 1
    rows.append((r["truth_verdict"], r["gene_symbol"], d, int(r1), int(r2), outcall))
print("rule\tyes\tcontextual\tno_called_surface\tacc_yes+ctx_n147\tacc_yes_vs_no_n116")
for name in ("R1", "R2", "R0"):
    y, cx, n = res[(name, "yes", True)], res[(name, "contextual", True)], res[(name, "no", True)]
    print(f"{name}\t{y}/68\t{cx}/31\t{n}/48\t{(y + cx + 48 - n) / 147:.1%}\t{(y + 48 - n) / 116:.1%}")
with open(RESULTS / "review_per_gene.tsv", "w") as f:
    f.write("truth\tgene\treview_folder\tR1\tR2\toutward_CC_call\n")
    for row in sorted(rows):
        f.write("\t".join(map(str, row)) + "\n")
