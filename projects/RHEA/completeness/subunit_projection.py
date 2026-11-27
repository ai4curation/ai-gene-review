"""Where do Rhea-to-GO projections meet complex-subunit annotation practice?

UniProt's Rhea2GO projection (GO_REF:0000116) emits an `enables` row for every Swiss-Prot
entry whose catalytic-activity annotation carries a Rhea reaction with a GO xref
(exactMatch/narrowMatch). Swiss-Prot often records a complex's reaction on each subunit,
while GO curators give non-catalytic subunits `contributes_to`. This script measures the
overlap between the two practices.

Inputs (DATA_DIR, default .cache/rhea-completeness):
  rhea2uniprot_sprot.tsv        Rhea FTP
  GO_EDIT_OBO (2nd argument)    go-ontology src/ontology/go-edit.obo (RHEA xrefs carry the skos predicate;
                                the released go-basic.obo drops it)
  goa_contributes_to_mf.tsv     QuickGO downloadSearch: qualifier=contributes_to, aspect=MF, protein
  sp_rhea_complex.tsv           UniProt stream: reviewed, cc_catalytic_activity:RHEA;
                                fields accession,organism_id,xref_complexportal,go_c,cc_subunit

Outputs: a summary on stdout and DATA_DIR/subunit_projection.tsv, one row per
(entry, mapped GO term) where the entry carries a native contributes_to MF row on the
projected term or a descendant of it, i.e. where the projection asserts `enables` for an
activity curators record the entry as only contributing to.
"""
import sys, csv, re, collections
sys.path.insert(0, sys.argv[0].rsplit("/", 1)[0])
from rheago_lib import parse_obo, ancestors

D = sys.argv[1] if len(sys.argv) > 1 else ".cache/rhea-completeness"
csv.field_size_limit(10**8)
G = parse_obo(sys.argv[2]); anc = ancestors(G)

# Rhea id -> mapped GO terms (the projection uses exact and narrow xrefs)
rhea2go = collections.defaultdict(set)
for t in G.values():
    if t["obs"]:
        continue
    for db, x, p in t["xrefs"]:
        if db == "RHEA" and p in ("skos:exactMatch", "skos:narrowMatch"):
            rhea2go[x].add(t["id"])

# entry -> projected GO terms
proj = collections.defaultdict(set)
for r in csv.DictReader(open(f"{D}/rhea2uniprot_sprot.tsv"), delimiter="\t"):
    for g in rhea2go.get(r["RHEA_ID"], ()):
        proj[r["ID"]].add(g)

# entry -> native contributes_to MF terms (any source)
DOWNLOAD_LIMIT = 200000  # must match downloadLimit in fetch_data.sh
ct = collections.defaultdict(set); ct_src = {}; n_ct = 0
rd = csv.DictReader(open(f"{D}/goa_contributes_to_mf.tsv"), delimiter="\t")
need = {"GENE PRODUCT ID", "GO TERM", "ECO ID", "REFERENCE", "ASSIGNED BY"}
assert need <= set(rd.fieldnames or []), f"QuickGO columns changed: {rd.fieldnames}"
for r in rd:
    n_ct += 1
    ac = r["GENE PRODUCT ID"].split("-")[0]
    ct[ac].add(r["GO TERM"])
    ct_src.setdefault((ac, r["GO TERM"]), set()).add(f'{r["ASSIGNED BY"]}:{r["REFERENCE"]}:{r["ECO ID"]}')
assert n_ct < DOWNLOAD_LIMIT, f"{n_ct} contributes_to rows reached the QuickGO downloadLimit; raise it"

HETERO = re.compile(r"heterodimer|heterotrimer|heterotetramer|hetero-?oligomer|heteromer|composed of|subunits? of|complex", re.I)
info = {}
rd = csv.DictReader(open(f"{D}/sp_rhea_complex.tsv"), delimiter="\t")
need = {"Entry", "Organism (ID)", "ComplexPortal", "Gene Ontology (cellular component)", "Subunit structure"}
assert need <= set(rd.fieldnames or []), f"UniProt columns changed: {rd.fieldnames}"
for r in rd:
    cc_terms = [t for t in (r["Gene Ontology (cellular component)"] or "").split("; ") if t]
    info[r["Entry"]] = {
        "cpx": bool((r["ComplexPortal"] or "").strip()),
        # any CC label containing "complex", e.g. "mitochondrial respiratory chain complex IV"
        "cc_complex": any("complex" in t.rsplit(" [GO:", 1)[0].lower() for t in cc_terms),
        "subunit_hetero": bool(HETERO.search(r["Subunit structure"] or "")),
        "taxon": r["Organism (ID)"],
    }

entries = set(info) | set(proj)
projected = {a for a in entries if proj.get(a)}
complexish = {a for a in projected if a in info and (info[a]["cpx"] or info[a]["cc_complex"] or info[a]["subunit_hetero"])}
with_ct = {a for a in complexish if ct.get(a)}
not_in_stream = projected - set(info)

rows = []
for a in sorted(projected):
    for g in sorted(proj[a]):
        hits = sorted(t for t in ct.get(a, ()) if g in anc(t))  # t == g or a descendant of g
        if hits:
            i = info.get(a, {})
            rows.append([a, i.get("taxon", ""), g, G[g].get("name", ""), ";".join(hits),
                         ";".join(sorted(set().union(*(ct_src[(a, t)] for t in hits)))),
                         int(i.get("cpx", False)), int(i.get("cc_complex", False)), int(i.get("subunit_hetero", False))])

with open(f"{D}/subunit_projection.tsv", "w") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["accession", "taxon", "projected_go", "projected_label", "native_contributes_to", "ct_sources (assigned_by:reference:eco)",
                "complexportal", "cc_complex", "subunit_heteromeric"])
    w.writerows(rows)

conf_entries = {r[0] for r in rows}
by_term = collections.Counter((r[2], r[3]) for r in rows)
src = collections.Counter(s.split(":")[0] for r in rows for s in r[5].split(";"))
print(f"Swiss-Prot entries with a Rhea reaction (UniProt stream): {len(info)}")
print(f"Swiss-Prot entries with at least one projected GO MF (Rhea FTP join, xref exact/narrow): {len(projected)}"
      f"  [{len(not_in_stream)} of them absent from the UniProt stream]")
print(f"native contributes_to MF rows read: {n_ct}")
print(f"  ... with a complex signal (ComplexPortal xref, GO 'complex' CC term, or heteromeric SUBUNIT note): {len(complexish)}"
      f"  [ComplexPortal {sum(info[a]['cpx'] for a in complexish)}; CC complex {sum(info[a]['cc_complex'] for a in complexish)};"
      f" SUBUNIT {sum(info[a]['subunit_hetero'] for a in complexish)}]")
print(f"  ... of those, with any native contributes_to MF row: {len(with_ct)}")
print(f"Projection says enables, native says contributes_to the same term or a descendant: {len(rows)} entry-term pairs on {len(conf_entries)} entries")
print("  native contributes_to source mentions (assigned_by; a pair can have several):", ", ".join(f"{k} {v}" for k, v in src.most_common()))
eco = collections.Counter("ECO:" + s.rsplit(":", 1)[1] for r in rows for s in r[5].split(";"))
print("  native contributes_to evidence (ECO; ECO:0000318 = IBA, ECO:0000250 = ISS):",
      ", ".join(f"{k} {v}" for k, v in eco.most_common(6)))
print("  top projected terms:")
for (g, n), c in by_term.most_common(15):
    print(f"    {c:6d}  {g} {n}")
