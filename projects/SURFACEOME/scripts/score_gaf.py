"""Score GO-only surface rules on PUBLIC GO annotations (goa_human.gaf) against SurfaceBench truth.

Also reverse-engineers which GO term set reproduces the benchmark's own `db_go` column.
"""
import csv
import collections
import gzip
import itertools
from common import DATA, RESULTS, benchmark, term_sets, label

truth = benchmark()
T = term_sets()
terms = {"no_iea": collections.defaultdict(set), "all": collections.defaultdict(set)}
gaf_date = ""
with gzip.open(DATA / "goa_human.gaf.gz", "rt") as f:
    for line in f:
        if line.startswith("!date-generated") and not gaf_date:
            gaf_date = line.split(":", 1)[1].strip()
        if line.startswith("!"):
            continue
        c = line.rstrip("\n").split("\t")
        if c[1] not in truth or "NOT" in c[3]:
            continue
        terms["all"][c[1]].add(c[4])
        if c[6] != "IEA":
            terms["no_iea"][c[1]].add(c[4])
print(f"GAF date-generated: {gaf_date}")
n_obs = sum("GO:0005887" in s for s in terms["all"].values())
print(f"benchmark proteins annotated to obsolete GO:0005887 (paper root): {n_obs}")


def r2(t):
    return bool(t & T["OUT_CC"]) or (bool(t & T["PM"]) and bool(t & T["TM_MF"]))


RULES = {
    "R1 outward CC (cell surface | external side PM) = paper rule on current GO": lambda t: bool(t & T["OUT_CC"]),
    "R2 R1 OR (PM AND TM-MF)": r2,
    "R3 R2 AND NOT inner-side-only": lambda t: r2(t) and not (t & T["INNER"] and not t & T["OUT_CC"] and not t & T["TM_MF"]),
    "R0 plain PM": lambda t: bool(t & T["PM"]),
}
out = open(RESULTS / "gaf_rule_scores.tsv", "w")
hdr = "evidence\trule\tyes\tcontextual\tno_called_surface\tacc_yes+ctx_as_surface_n147\tacc_yes_vs_no_n116"
print(hdr); out.write(hdr + "\n")
for ev, tt in terms.items():
    for name, rule in RULES.items():
        c = collections.Counter((r["truth_verdict"], rule(tt[a])) for a, r in truth.items())
        y, cx, n = c[("yes", True)], c[("contextual", True)], c[("no", True)]
        line = f"{ev}\t{name}\t{y}/68\t{cx}/31\t{n}/48\t{(y + cx + c[('no', False)]) / 147:.1%}\t{(y + c[('no', False)]) / 116:.1%}"
        print(line); out.write(line + "\n")
out.close()

with open(RESULTS / "gaf_per_gene.tsv", "w") as f:
    f.write("gene\tuniprot\ttruth\ttruth_reason\tpaper_db_go\tR1_no_iea\tR2_no_iea\tR2_all\tR0_no_iea\n")
    for a, r in sorted(truth.items(), key=lambda x: (x[1]["truth_verdict"], x[1]["gene_symbol"])):
        n, al = terms["no_iea"][a], terms["all"][a]
        f.write("\t".join([r["gene_symbol"], a, r["truth_verdict"], r["truth_reason"], r["db_go"],
                           str(int(RULES[list(RULES)[0]](n))), str(int(r2(n))), str(int(r2(al))), str(int(bool(n & T["PM"])))]) + "\n")
print("\nR2 (no IEA) errors:")
for tv in ("yes", "contextual", "no"):
    wrong = sorted(r["gene_symbol"] for a, r in truth.items() if r["truth_verdict"] == tv and r2(terms["no_iea"][a]) == (tv == "no"))
    print(f"  [{tv}] {len(wrong)}: {' '.join(wrong)}")

print("\nWhich term set reproduces the benchmark's own db_go column? (agreement /147)")
cands = {k: T[k] for k in ("OUT_CC", "SIDE", "PM_COMPLEX", "PM", "TM_MF")}
best = []
for n in range(1, 4):
    for combo in itertools.combinations(cands, n):
        s = set().union(*(cands[k] for k in combo))
        for ev in terms:
            ag = sum((r["db_go"] == "1") == bool(terms[ev][a] & s) for a, r in truth.items())
            best.append((ag, ev, "+".join(combo)))
for b in sorted(best, reverse=True)[:6]:
    print(f"  {b[0]}/147  {b[1]}  {b[2]}")
for acc in ("P01116", "P23458", "P47871"):  # KRAS, JAK1, GCGR examples
    cc = sorted(label(x) for x in terms["no_iea"][acc] & (T["PM"] | T["SIDE"] | T["OUT_CC"]))
    print(f"  {truth[acc]['gene_symbol']}: paper db_go={truth[acc]['db_go']}  PM-type terms={cc}")
