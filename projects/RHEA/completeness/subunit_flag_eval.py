"""Can a complex-membership condition flag projected Rhea2GO rows as contributes_to candidates?

Universe: every (Swiss-Prot entry, GO term g) pair that UniProt's Rhea2GO projection (GO_REF:0000116)
turns into an `enables` row: the entry carries a RHEA id that GO maps to g by exactMatch/narrowMatch.

Gold labels, where a curator has annotated g (or a descendant of g) to the entry:
  CT  the entry has a contributes_to MF row on g or a descendant (QuickGO, all contributes_to MF rows)
  EN  the entry has a curated (non-IEA) MF row on g or a descendant, and no contributes_to row on that term
      (UniProt's GO cross-references drop the qualifier; QuickGO's contributes_to download supplies it)
A pair can be both (e.g. IBA contributes_to and an IDA row); it then counts as CT.
Each label is also computed without IBA rows (ECO:0000318 for CT, IBA:* for EN), because most CT rows
are PAINT IBA and the PANTHER signal below is derived from PAINT.

Candidate signals (entry level):
  complexportal   ComplexPortal xref
  cc_complex      specific GO CC term with "complex" in its label (<= 10 is_a children)
  subunit_note    SUBUNIT note naming a heteromer, a complex or subunits
  any_complex     any of the three
  panther_ct      another Swiss-Prot Rhea entry in the same PANTHER subfamily has an IBA contributes_to
                  row on g or a descendant (PAINT has placed contributes_to for g in this clade)
  no_act_site     no ACT_SITE feature on the entry
  name_subunit    recommended name says subunit/component/chain, without "catalytic"
Combinations are reported too. A convention check counts PANTHER subfamilies whose labelled members
(IBA excluded) disagree, CT for some and EN for others, on the same projected term. For each signal: pairs flagged, CT and EN gold among them, precision
(CT / (CT + EN)) and recall over gold CT.

Usage: subunit_flag_eval.py DATA_DIR GO_EDIT_OBO
Inputs (DATA_DIR, from fetch_data.sh): rhea2uniprot_sprot.tsv, sp_mf.*.jsonl, go-basic.obo,
goa_contributes_to_mf.tsv, sp_rhea_complex.tsv, sp_rhea_roles.tsv.
Outputs: summary on stdout; DATA_DIR/subunit_flag_spotcheck.tsv (all projected pairs for the spot-check
families in seven model organisms, with signals and gold).
"""
import sys, glob, json, csv, re, collections
sys.path.insert(0, sys.argv[0].rsplit("/", 1)[0])
from rheago_lib import parse_obo, ancestors

D, OBO = sys.argv[1], sys.argv[2]
csv.field_size_limit(10**8)
T = parse_obo(OBO); anc = ancestors(T)
G = parse_obo(f"{D}/go-basic.obo"); ganc = ancestors(G)
def A(x): return ganc(x) if x in G else anc(x)
def name(g): return G.get(g, T.get(g, {})).get("name", "?")
CIRC = {"IEA:RHEA", "IEA:UniProtKB-EC"}

rhea2go = collections.defaultdict(set)
for t in T.values():
    if t["obs"]:
        continue
    for db, x, p in t["xrefs"]:
        if db == "RHEA" and p in ("skos:exactMatch", "skos:narrowMatch"):
            rhea2go[x].add(t["id"])
proj = collections.defaultdict(set)
for r in csv.DictReader(open(f"{D}/rhea2uniprot_sprot.tsv"), delimiter="\t"):
    for g in rhea2go.get(r["RHEA_ID"], ()):
        proj[r["ID"]].add(g)

native = {}
for f in glob.glob(f"{D}/sp_mf.*.jsonl"):
    for l in open(f):
        e = json.loads(l); native[e["ac"]] = [(t, ev) for t, ev in e["mf"] if ev not in CIRC]

ct = collections.defaultdict(dict)  # ac -> term -> set of ECO ids
for r in csv.DictReader(open(f"{D}/goa_contributes_to_mf.tsv"), delimiter="\t"):
    ct[r["GENE PRODUCT ID"].split("-")[0]].setdefault(r["GO TERM"], set()).add(r["ECO ID"])
IBA = "ECO:0000318"

kids = collections.Counter(p for t in G.values() for p in t["isa"])
HETERO = re.compile(r"heterodimer|heterotrimer|heterotetramer|hetero-?oligomer|heteromer|composed of|subunits? of|complex", re.I)
CCX = re.compile(r"([^;]*?complex[^;]*?) \[(GO:\d{7})\]")
sig = {}
for r in csv.DictReader(open(f"{D}/sp_rhea_complex.tsv"), delimiter="\t"):
    sig[r["Entry"]] = {
        "complexportal": bool((r.get("ComplexPortal") or "").strip()),
        "cc_complex": any(kids[m.group(2)] <= 10 for m in CCX.finditer(r.get("Gene Ontology (cellular component)") or "")),
        "subunit_note": bool(HETERO.search(r.get("Subunit structure") or "")),
        "taxon": r.get("Organism (ID)", ""),
    }
SUBNAME = re.compile(r"\b(subunit|component|chain)\b", re.I)
sf = {}; pname = {}
for r in csv.DictReader(open(f"{D}/sp_rhea_roles.tsv"), delimiter="\t"):
    a = r["Entry"]; s = sig.setdefault(a, {"complexportal": False, "cc_complex": False, "subunit_note": False, "taxon": ""})
    rec = (r.get("Protein names") or "").split(" (")[0]
    pname[a] = rec
    s["no_act_site"] = not (r.get("Active site") or "").strip()
    s["name_subunit"] = bool(SUBNAME.search(rec)) and "catalytic" not in rec.lower()
    sf[a] = {x for x in (r.get("PANTHER") or "").split(";") if ":SF" in x}
for s in sig.values():
    s["any_complex"] = s["complexportal"] or s["cc_complex"] or s["subunit_note"]

# PAINT clades with an IBA contributes_to for g: subfamily -> set of (g-lineage term) on members
sf_ct = collections.defaultdict(lambda: collections.defaultdict(set))  # sf -> term -> members
for a, terms in ct.items():
    for t, ecos in terms.items():
        if IBA in ecos:
            for x in sf.get(a, ()):
                sf_ct[x][t].add(a)
def panther_ct(a, g):
    for x in sf.get(a, ()):
        for t, mem in sf_ct.get(x, {}).items():
            if mem - {a} and g in A(t):
                return True
    return False

def gold(a, g, no_iba):
    c = [t for t, e in ct.get(a, {}).items() if g in A(t) and (not no_iba or e - {IBA})]
    if c:
        return "CT"
    cts = set(ct.get(a, {}))
    e = [t for t, ev in native.get(a, []) if not ev.startswith("IEA") and g in A(t) and t not in cts
         and not (no_iba and ev.startswith("IBA"))]
    return "EN" if e else None

SIGNALS = ["complexportal", "cc_complex", "subunit_note", "any_complex", "panther_ct", "no_act_site", "name_subunit"]
COMBOS = {
    "any_complex & panther_ct": lambda s: s["any_complex"] and s["panther_ct"],
    "any_complex & no_act_site": lambda s: s["any_complex"] and s["no_act_site"],
    "any_complex & name_subunit": lambda s: s["any_complex"] and s["name_subunit"],
    "any_complex & no_act_site & name_subunit": lambda s: s["any_complex"] and s["no_act_site"] and s["name_subunit"],
}
stats = {k: {v: collections.Counter() for v in ("all", "noIBA")} for k in SIGNALS + list(COMBOS) + ["(none: every projected pair)"]}
golds = {"all": collections.Counter(), "noIBA": collections.Counter()}
spot = []
SPOT = {"GO:0004129", "GO:0034062", "GO:0003899", "GO:0004088", "GO:0050567", "GO:0004049", "GO:0000107",
        "GO:0036381", "GO:0004642", "GO:0004359"}
SPOT_TAXA = {"9606", "10090", "559292", "284812", "83333", "224308", "3702"}  # human, mouse, yeasts, E. coli, B. subtilis, Arabidopsis
npairs = 0
clade = collections.defaultdict(collections.Counter)  # (subfamily, g) -> gold label counts (IBA excluded)
for a, gs in proj.items():
    s = dict(sig.get(a, {}))
    if not s:
        continue
    for g in gs:
        npairs += 1
        s["panther_ct"] = panther_ct(a, g)
        flags = {k for k in SIGNALS if s.get(k)} | {k for k, f in COMBOS.items() if f(s)} | {"(none: every projected pair)"}
        for v, no_iba in (("all", False), ("noIBA", True)):
            lab = gold(a, g, no_iba)
            golds[v][lab] += 1
            for k in flags:
                stats[k][v]["flagged"] += 1
                if lab:
                    stats[k][v][lab] += 1
        lab = gold(a, g, True)
        if lab:
            for x in sf.get(a, ()):
                clade[(x, g)][lab] += 1
        if g in SPOT and s.get("taxon") in SPOT_TAXA:
            spot.append([a, s.get("taxon", ""), pname.get(a, ""), g, name(g), gold(a, g, False) or "", gold(a, g, True) or "",
                         *(int(bool(s.get(k))) for k in SIGNALS)])

print(f"Projected (entry, GO term) pairs: {npairs}")
for v in ("all", "noIBA"):
    print(f"Gold ({'all curated rows' if v == 'all' else 'IBA rows excluded'}): CT {golds[v]['CT']}, EN {golds[v]['EN']}, unlabelled {golds[v][None]}")
for v in ("all", "noIBA"):
    print(f"\n[{v}] {'signal':45s} {'flagged':>8s} {'CT':>6s} {'EN':>7s} {'precision':>9s} {'recall':>7s}")
    for k in stats:
        c = stats[k][v]; lab = c["CT"] + c["EN"]
        prec = f"{100*c['CT']/lab:.1f}%" if lab else "-"
        rec = f"{100*c['CT']/golds[v]['CT']:.1f}%" if golds[v]["CT"] else "-"
        print(f"[{v}] {k:45s} {c['flagged']:8d} {c['CT']:6d} {c['EN']:7d} {prec:>9s} {rec:>7s}")

lab2 = [c for c in clade.values() if c["CT"] + c["EN"] >= 2]
mixed = [k for k, c in clade.items() if c["CT"] + c["EN"] >= 2 and c["CT"] and c["EN"]]
print(f"\nConvention check (IBA excluded): PANTHER subfamilies x projected term with >= 2 labelled Swiss-Prot members: {len(lab2)};"
      f" all CT {sum(1 for c in lab2 if not c['EN'])}, all EN {sum(1 for c in lab2 if not c['CT'])}, mixed {len(mixed)}")
for k in sorted(mixed, key=lambda k: -sum(clade[k].values()))[:12]:
    print(f"  mixed: {k[0]} {k[1]} {name(k[1])}: CT {clade[k]['CT']}, EN {clade[k]['EN']}")

with open(f"{D}/subunit_flag_spotcheck.tsv", "w") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["accession", "taxon", "recommended_name", "projected_go", "projected_label", "gold", "gold_noIBA", *SIGNALS])
    w.writerows(sorted(spot, key=lambda r: (r[3], r[1], r[2])))
