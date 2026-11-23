"""Survey of the 53 Arabidopsis NRT1/PTR FAMILY (NPF) members in PANTHER PTHR11654.

Reproducible, network-backed analysis; nothing is hard-coded except the query
parameters. Run from the repository root:

    uv run --with biopython python \
        interpro/panther/PTHR11654/PTHR11654-bioinformatics/npf_arabidopsis_survey.py

Outputs (written next to this script):
  arath_npf_members.tsv   UniProt accession, NPF name, PANTHER subfamily id + name
  arath_npf_goa.tsv       GOA MF/BP/CC rows (term, evidence, source) for all members
  arath_npf_goa_summary.tsv per (aspect, term, evidence, source): member count and members
  arath_npf_exxer.tsv     residues aligned to NPF6.3 E41/E44/R45 (TM1 ExxER/K motif)
  global_electronic_counts.tsv  all-taxa QuickGO annotation counts for the InterPro2GO
                          and ARBA mappings discussed in the review (one query per row)

Steps:
1. UniProtKB (reviewed, taxon 3702, xref PANTHER PTHR11654) -> member list.
2. PANTHER geneinfo API -> subfamily (SF) per member; SF names from the local
   interpro/panther/panther.obo.
3. QuickGO annotation download -> all GO annotations (MF, BP and CC) for the members.
3b. QuickGO annotation search (exact GO id, withFrom = mapping source, optional taxon)
   -> global annotation counts for each electronic mapping in GLOBAL_QUERIES.
4. Global pairwise alignment (BLOSUM62, gap open -10, extend -0.5) of every member
   to NPF6.3/CHL1 (Q05085) and read the residues aligned to E41, E44, R45. A
   pairwise alignment is a coarse proxy for a family MSA; treat gaps or ambiguous
   calls as inconclusive.
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
OBO = REPO / "interpro" / "panther" / "panther.obo"
ANCHOR = "Q05085"  # NPF6.3 / CHL1 / NRT1.1
ANCHOR_SITES = {41: "E", 44: "E", 45: "R"}
# (label, GO id, withFrom source, NCBI taxon or None for all taxa)
GLOBAL_QUERIES = [
    ("IPR044739", "GO:0071916", "InterPro:IPR044739", None),
    ("IPR044739", "GO:0042937", "InterPro:IPR044739", None),
    ("IPR044739", "GO:0042938", "InterPro:IPR044739", None),
    ("IPR018456", "GO:0006857", "InterPro:IPR018456", None),
    ("IPR018456", "GO:0006857", "InterPro:IPR018456", 33090),
    ("ARBA00084141", "GO:0080054", "ARBA:ARBA00084141", None),
]


def get(url: str, accept: str | None = None) -> str:
    headers = {"User-Agent": "ai-gene-review/npf-survey (python-urllib)"}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=180) as fh:
        return fh.read().decode()


def members() -> list[dict]:
    q = "xref:panther-PTHR11654 AND organism_id:3702 AND reviewed:true"
    url = (
        "https://rest.uniprot.org/uniprotkb/stream?format=tsv&fields=accession,gene_names&query="
        + urllib.parse.quote(q)
    )
    rows = list(csv.DictReader(io.StringIO(get(url)), delimiter="\t"))
    return [{"acc": r["Entry"], "name": r["Gene Names"].split()[0]} for r in rows]


def panther_sf(accs: list[str]) -> dict[str, str]:
    url = (
        "https://www.pantherdb.org/services/oai/pantherdb/geneinfo?organism=3702&geneInputList="
        + ",".join(accs)
    )
    genes = json.loads(get(url))["search"]["mapped_genes"]["gene"]
    if isinstance(genes, dict):
        genes = [genes]
    return {g["accession"].split("UniProtKB=")[-1]: g["sf_id"] for g in genes}


def sf_names() -> dict[str, str]:
    text = OBO.read_text()
    return {
        m.group(1): m.group(2)
        for m in re.finditer(r"id: PANTHER:(PTHR\d+:SF\d+)\nname: (.*)", text)
    }


def goa(accs: list[str]) -> list[dict]:
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?includeFields=goName&"
        "selectedFields=geneProductId,symbol,qualifier,goId,goName,goEvidence,goAspect,reference,withFrom,assignedBy"
        "&geneProductId=" + ",".join(accs)
    )
    rows = list(csv.DictReader(io.StringIO(get(url, "text/tsv")), delimiter="\t"))
    return [r for r in rows if r["GO ASPECT"] in ("F", "P", "C")]


def global_count(go_id: str, with_from: str, taxon: int | None) -> int:
    params = {"goId": go_id, "goUsage": "exact", "withFrom": with_from, "limit": 1}
    if taxon is not None:
        params.update({"taxonId": taxon, "taxonUsage": "descendants"})
    url = "https://www.ebi.ac.uk/QuickGO/services/annotation/search?" + urllib.parse.urlencode(params)
    return int(json.loads(get(url, "application/json"))["numberOfHits"])


def seq(acc: str) -> str:
    fasta = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(fasta.splitlines()[1:])


def aligned_residues(anchor: str, target: str) -> dict[int, tuple[int | None, str]]:
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(anchor, target)[0]
    mapping: dict[int, tuple[int | None, str]] = {}
    for (a0, a1), (t0, t1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            mapping[a0 + k + 1] = (t0 + k + 1, target[t0 + k])
    return {p: mapping.get(p, (None, "-")) for p in ANCHOR_SITES}


def main() -> int:
    mem = members()
    accs = [m["acc"] for m in mem]
    sf = panther_sf(accs)
    names = sf_names()
    with open(HERE / "arath_npf_members.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["accession", "npf_name", "panther_sf", "panther_sf_name"])
        for m in sorted(mem, key=lambda x: [int(t) for t in re.findall(r"\d+", x["name"])]):
            s = sf.get(m["acc"], "")
            w.writerow([m["acc"], m["name"], s, names.get(s, "")])

    rows = goa(accs)
    name_of = {m["acc"]: m["name"] for m in mem}
    summary: dict[tuple, set] = defaultdict(set)
    with open(HERE / "arath_npf_goa.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["accession", "npf_name", "qualifier", "go_id", "go_name", "aspect", "evidence", "reference", "with_from", "assigned_by"])
        for r in rows:
            acc = r["GENE PRODUCT ID"]
            src = r["WITH/FROM"] if r["GO EVIDENCE CODE"] in ("IEA",) else ""
            if r["GO EVIDENCE CODE"] == "IBA":
                src = ",".join(t for t in r["WITH/FROM"].split("|") if t.startswith("PANTHER:PTN"))
            w.writerow([acc, name_of.get(acc, ""), r["QUALIFIER"], r["GO TERM"], r["GO NAME"], r["GO ASPECT"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["WITH/FROM"], r["ASSIGNED BY"]])
            summary[(r["GO ASPECT"], r["GO TERM"], r["GO NAME"], r["QUALIFIER"], r["GO EVIDENCE CODE"], src)].add(name_of.get(acc, acc))
    with open(HERE / "arath_npf_goa_summary.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["aspect", "go_id", "go_name", "qualifier", "evidence", "electronic_source", "n_members", "members"])
        for k in sorted(summary, key=lambda k: (k[0], k[2], k[4])):
            w.writerow([*k, len(summary[k]), " ".join(sorted(summary[k]))])

    with open(HERE / "global_electronic_counts.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["source", "go_id", "with_from", "taxon", "n_annotations"])
        for label, go_id, wf, taxon in GLOBAL_QUERIES:
            w.writerow([label, go_id, wf, f"NCBITaxon:{taxon}" if taxon else "all", global_count(go_id, wf, taxon)])

    anchor_seq = seq(ANCHOR)
    for p, aa in ANCHOR_SITES.items():
        assert anchor_seq[p - 1] == aa, f"anchor {ANCHOR} {p} is {anchor_seq[p-1]}, expected {aa}"
    with open(HERE / "arath_npf_exxer.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["accession", "npf_name", "pos_E41", "aa_E41", "pos_E44", "aa_E44", "pos_R45", "aa_R45", "ExxE[RK]_intact"])
        for m in sorted(mem, key=lambda x: [int(t) for t in re.findall(r"\d+", x["name"])]):
            res = aligned_residues(anchor_seq, seq(m["acc"]))
            intact = res[41][1] == "E" and res[44][1] == "E" and res[45][1] in ("R", "K")
            w.writerow([m["acc"], m["name"], res[41][0], res[41][1], res[44][0], res[44][1], res[45][0], res[45][1], intact])
    print(f"{len(mem)} members; {len(rows)} GO annotation rows (MF/BP/CC) written to {HERE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
