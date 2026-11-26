"""Split the consistency metric: how much curated-only disagreement is complex-subunit practice?

consistency.py classifies each (mapped RHEA id -> GO term g, Swiss-Prot entry carrying that RHEA id)
pair by the entry's curated (non-IEA) MF annotations as consistent / ancestor_only / disjoint / none.
About 17% of the pairs with any catalytic or transporter MF are ancestor_only or disjoint. Some of
those are entries that are one subunit of a complex: Swiss-Prot puts the complex reaction on every
subunit, while GO curators annotate the complex activity to the subunit that carries it (or give the
others `contributes_to`), so the other subunits look like disagreement.

This script re-runs the curated-only classification and gives every ancestor_only or disjoint pair one
of these sub-classes (first match wins):

  subunit_ct        the entry has a native contributes_to MF row (QuickGO, any source) on g or a
                    descendant of g. UniProt's GO cross-references drop the qualifier, so this can only
                    happen when the contributes_to row is IEA, i.e. absent from the curated set.
  subunit_partner   another Swiss-Prot entry of the same organism carries the same RHEA id, is
                    curated-consistent for g, is in a different PANTHER family (a different kind of
                    subunit, not an isozyme or paralog), and shares a complex with this entry: the same
                    ComplexPortal id or the same specific GO cellular-component term whose label
                    contains "complex" (generic grouping terms with more than 10 is_a children, such as
                    protein-containing complex, are ignored). The complex activity is annotated, on a
                    partner subunit.
  complex_only      as subunit_partner, but no shared complex is recorded: the entry only has a complex
                    signal of its own (ComplexPortal xref, specific GO 'complex' CC term, or a
                    heteromeric SUBUNIT note). Weaker.
  disagreement      none of the above: treated as real disagreement about the activity.

The same split is reported for the all-sources classification for comparison.

Usage: subunit_consistency.py DATA_DIR GO_EDIT_OBO
Inputs (DATA_DIR, from fetch_data.sh): rhea2uniprot_sprot.tsv, sp_mf.*.jsonl, go-basic.obo,
goa_contributes_to_mf.tsv, sp_rhea_complex.tsv, sp_rhea_roles.tsv.
Outputs: summary on stdout; DATA_DIR/subunit_consistency.tsv (one row per mapping with at least one
non-consistent curated pair, with the per-sub-class counts and example accessions).
"""
import sys, glob, json, csv, re, collections
sys.path.insert(0, sys.argv[0].rsplit("/", 1)[0])
from rheago_lib import parse_obo, ancestors

D, OBO = sys.argv[1], sys.argv[2]
csv.field_size_limit(10**8)
T = parse_obo(OBO); anc = ancestors(T)
G = parse_obo(f"{D}/go-basic.obo"); ganc = ancestors(G)
def A(x): return ganc(x) if x in G else anc(x)
ROOTS = {"GO:0003824", "GO:0005215"}
CIRC = {"IEA:RHEA", "IEA:UniProtKB-EC"}

native = {}
for f in glob.glob(f"{D}/sp_mf.*.jsonl"):
    for l in open(f):
        e = json.loads(l); native[e["ac"]] = [(t, ev) for t, ev in e["mf"] if ev not in CIRC]

byid = collections.defaultdict(list)
for t in T.values():
    if t["obs"]:
        continue
    for db, x, p in t["xrefs"]:
        if db == "RHEA" and p in ("skos:exactMatch", "skos:narrowMatch"):
            byid[x].append(t["id"])
pairs = collections.defaultdict(set)
for r in csv.DictReader(open(f"{D}/rhea2uniprot_sprot.tsv"), delimiter="\t"):
    for g in byid.get(r["RHEA_ID"], []):
        pairs[(r["MASTER_ID"], g)].add(r["ID"])

ct = collections.defaultdict(set)
for r in csv.DictReader(open(f"{D}/goa_contributes_to_mf.tsv"), delimiter="\t"):
    ct[r["GENE PRODUCT ID"].split("-")[0]].add(r["GO TERM"])
# GO terms on which the entry also has a row other than contributes_to is unknowable from the UniProt
# cross-references (they carry no qualifier), so "contributes_to only" below means: every curated term in
# g's lineage that makes the entry consistent is a term the entry has a contributes_to row for.

HETERO = re.compile(r"heterodimer|heterotrimer|heterotetramer|hetero-?oligomer|heteromer|composed of|subunits? of|complex", re.I)
CCX = re.compile(r"([^;]*?complex[^;]*?) \[(GO:\d{7})\]")
# A CC term counts as a shared complex only if it names a specific complex: generic grouping terms
# (protein-containing complex, catalytic complex, membrane protein complex, ...) have many is_a children.
kids = collections.Counter(p for t in G.values() for p in t["isa"])
def specific_cc(t): return kids[t] <= GENERIC_CC_CHILDREN
GENERIC_CC_CHILDREN = 10
fam = {}
for r in csv.DictReader(open(f"{D}/sp_rhea_roles.tsv"), delimiter="\t"):
    fam[r["Entry"]] = {x for x in (r.get("PANTHER") or "").split(";") if x and ":" not in x}
def other_kind(a, b):
    """Different PANTHER families: a distinct subunit, not an isozyme or paralog of the partner."""
    return bool(fam.get(a)) and bool(fam.get(b)) and not (fam[a] & fam[b])
info = {}
for r in csv.DictReader(open(f"{D}/sp_rhea_complex.tsv"), delimiter="\t"):
    cpx = {x for x in (r.get("ComplexPortal") or "").split(";") if x.strip()}
    ccs = {m.group(2) for m in CCX.finditer(r.get("Gene Ontology (cellular component)") or "") if specific_cc(m.group(2))}
    info[r["Entry"]] = {"cpx": cpx, "cc": ccs, "het": bool(HETERO.search(r.get("Subunit structure") or "")),
                        "taxon": r.get("Organism (ID)", "")}

def classify(terms, g, ga):
    enz = {t for t in terms if A(t) & ROOTS}
    if any(g in A(t) for t in terms): return "consistent"
    if any(t in ga and t not in ROOTS for t in enz): return "ancestor_only"
    if enz: return "disjoint"
    return "none"

SUB = ("subunit_ct", "subunit_partner", "complex_only", "disagreement")
tot = {s: collections.Counter() for s in ("cur", "all")}
rows = []
for (m, g), prots in pairs.items():
    ga = A(g)
    cls = {"cur": {}, "all": {}}
    for ac in prots:
        if ac not in native:
            continue
        cls["cur"][ac] = classify({t for t, ev in native[ac] if not ev.startswith("IEA")}, g, ga)
        cls["all"][ac] = classify({t for t, _ in native[ac]}, g, ga)
    row = collections.Counter(); ex = collections.defaultdict(list)
    for s in ("cur", "all"):
        ok = [b for b, k in cls[s].items() if k == "consistent"]
        for ac, k in cls[s].items():
            if k == "consistent" and s == "cur":
                hits = {t for t, ev in native[ac] if not ev.startswith("IEA") and g in A(t)}
                if hits and hits <= ct.get(ac, set()):
                    tot[s]["consistent_ct_only"] += 1; row["cur_consistent_ct_only"] += 1
            if k not in ("ancestor_only", "disjoint"):
                tot[s][k] += 1; continue
            i = info.get(ac, {"cpx": set(), "cc": set(), "het": False, "taxon": None})
            sig = bool(i["cpx"] or i["cc"] or i["het"])
            mates = [b for b in ok if b != ac and info.get(b, {}).get("taxon") == i["taxon"] and i["taxon"] and other_kind(ac, b)]
            if any(g in A(t) for t in ct.get(ac, ())):
                sub = "subunit_ct"
            elif any(i["cpx"] & info[b]["cpx"] or i["cc"] & info[b]["cc"] for b in mates):
                sub = "subunit_partner"
            elif sig and mates:
                sub = "complex_only"
            else:
                sub = "disagreement"
            tot[s][(k, sub)] += 1
            row[f"{s}_{sub}"] += 1
            if s == "cur" and len(ex[sub]) < 5:
                ex[sub].append(ac)
    if any(row[f"cur_{x}"] for x in SUB) or row["cur_consistent_ct_only"]:
        rows.append({"rhea": m, "go": g, "label": T[g].get("name", ""),
                     "cur_consistent_ct_only": row["cur_consistent_ct_only"],
                     **{f"cur_{x}": row[f"cur_{x}"] for x in SUB},
                     **{f"all_{x}": row[f"all_{x}"] for x in SUB},
                     "examples_subunit": ",".join(ex["subunit_ct"] + ex["subunit_partner"]),
                     "examples_disagreement": ",".join(ex["disagreement"])})

rows.sort(key=lambda r: -(r["cur_subunit_ct"] + r["cur_subunit_partner"]))
with open(f"{D}/subunit_consistency.tsv", "w") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t"); w.writeheader(); w.writerows(rows)

for s, name in (("cur", "Curated sources only"), ("all", "All non-circular sources")):
    t = tot[s]
    cons = t["consistent"]
    nonc = sum(v for k, v in t.items() if isinstance(k, tuple))
    base = cons + nonc
    print(f"{name}: consistent {cons}; ancestor_only+disjoint {nonc} ({100*nonc/base:.1f}% of {base} pairs with a catalytic/transporter MF); none {t['none']}")
    if s == "cur":
        print(f"  (of the consistent pairs, {t['consistent_ct_only']} are consistent only through a contributes_to row:"
              " UniProt's GO cross-references drop the qualifier)")
    for sub in SUB:
        n = sum(v for k, v in t.items() if isinstance(k, tuple) and k[1] == sub)
        print(f"  {sub:16s} {n:7d}  ({100*n/nonc:.1f}% of non-consistent; ancestor_only {t[('ancestor_only', sub)]}, disjoint {t[('disjoint', sub)]})")
    sub_n = sum(v for k, v in t.items() if isinstance(k, tuple) and k[1] in ("subunit_ct", "subunit_partner"))
    print(f"  => subunit practice (subunit_ct + subunit_partner) explains {sub_n} pairs; disagreement rate falls from "
          f"{100*nonc/base:.1f}% to {100*(nonc-sub_n)/(base-sub_n):.1f}% if they are set aside")
print("top mappings by subunit-practice pairs (curated):")
for r in rows[:15]:
    print(f"  {r['cur_subunit_ct']+r['cur_subunit_partner']:5d}  RHEA:{r['rhea']} {r['go']} {r['label']}")
