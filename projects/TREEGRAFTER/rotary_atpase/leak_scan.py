"""Scan for ATP-synthase GO terms leaking onto FliI/SctN export ATPases.

Two live queries, no hard-coded results:
1. UniProtKB counts: of entries indexed with InterPro IPR005714 (T3SS ATPase FliI/YscN),
   how many carry each rotary-ATP-synthase GO term (any evidence).
2. QuickGO: every IBA (ECO:0000318) GO:0046933 annotation whose WITH/FROM cites the
   F1-beta PAINT node PANTHER:PTN008558586, classified by the target's InterPro family.

Run: uv run --with requests projects/TREEGRAFTER/rotary_atpase/leak_scan.py
"""
import collections, csv, io, pathlib, requests

OUT = pathlib.Path(__file__).parent
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"
FLII = "IPR005714"
TERMS = {
    "GO:0046933": "proton-transporting ATP synthase activity, rotational mechanism",
    "GO:0045259": "proton-transporting ATP synthase complex",
    "GO:0015986": "proton motive force-driven ATP synthesis",
    "GO:0046961": "proton-transporting ATPase activity, rotational mechanism",
    "GO:1902600": "proton transmembrane transport",
    "GO:0008564": "protein-exporting ATPase activity",
    "GO:0016887": "ATP hydrolysis activity",
}


def count(query):
    r = requests.get(UNIPROT, params={"query": query, "size": 1}, timeout=120)
    r.raise_for_status()
    return int(r.headers["x-total-results"])


def uniprot_counts():
    total = count(f"xref:interpro-{FLII}")
    rows = [("scope", "go_id", "go_label", "n_with_term", "n_family", "fraction")]
    for scope, extra in [("all", ""), ("reviewed", " AND reviewed:true")]:
        n = count(f"xref:interpro-{FLII}{extra}") if extra else total
        for go, label in TERMS.items():
            k = count(f"go:{go[3:]} AND xref:interpro-{FLII}{extra}")
            rows.append((scope, go, label, k, n, f"{k / n:.4f}"))
    return rows


def family(interpro):
    s = set(filter(None, interpro.split(";")))
    if "IPR005722" in s:
        return "F1_beta"
    if FLII in s:
        return "FliI_SctN"
    if s & {"IPR022878", "IPR022879"}:
        return "V_A_type"
    return "other"


def iba_targets(node="PTN008558586"):
    r = requests.get(QUICKGO, headers={"Accept": "text/tsv"}, timeout=300, params={
        "goId": "GO:0046933", "goUsage": "exact", "evidenceCode": "ECO:0000318",
        "evidenceCodeUsage": "exact", "downloadLimit": 50000,
        "selectedFields": "geneProductId,symbol,qualifier,goId,evidenceCode,reference,withFrom,taxonId"})
    r.raise_for_status()
    accs = sorted({row["GENE PRODUCT ID"] for row in csv.DictReader(io.StringIO(r.text), delimiter="\t")
                   if node in row["WITH/FROM"]})
    out = []
    for i in range(0, len(accs), 100):
        q = " OR ".join(f"accession:{a}" for a in accs[i:i + 100])
        t = requests.get(UNIPROT, timeout=120, params={"query": q, "format": "tsv", "size": 500,
                         "fields": "accession,gene_primary,protein_name,organism_name,reviewed,xref_interpro"}).text
        for row in csv.DictReader(io.StringIO(t), delimiter="\t"):
            out.append((row["Entry"], row["Gene Names (primary)"], row["Protein names"], row["Organism"],
                        row["Reviewed"], family(row["InterPro"])))
    return node, sorted(out, key=lambda r: (r[5], r[3]))


def write(name, rows):
    with open(OUT / name, "w", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)


if __name__ == "__main__":
    write("fliI_sctN_go_counts.tsv", uniprot_counts())
    node, targets = iba_targets()
    write("ptn008558586_iba_targets.tsv",
          [("accession", "gene", "protein_name", "organism", "reviewed", "family")] + targets)
    print(f"{node}: {len(targets)} IBA GO:0046933 targets;",
          dict(collections.Counter(t[5] for t in targets)))
