"""Survey: are well-known protein ligands annotated involved_in the pathway they activate?

For each ligand (and a few receptors as comparators) in human, Drosophila and S. pombe,
fetch all biological-process annotations from QuickGO and classify each against the
ligand's own pathway term ("cognate" pathway):
  pathway     the term is the cognate pathway or an is_a/part_of descendant
  regulation  the term reaches the cognate pathway only through regulates relations
  other       any other signal transduction term
Accessions are resolved from UniProt (reviewed entries; a few fly genes need the
unreviewed FlyBase-mapped accession, given in OVERRIDES).

The ligand and pathway lists are a hand-picked sample of textbook pathways.

Usage:
  uv run python projects/LIGANDS_IN_SIGNALING/scripts/survey/ligand_pathway_survey.py \
      --out projects/LIGANDS_IN_SIGNALING/results/ligand_survey.json
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

import requests

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
HEADERS = {"Accept": "application/json"}
# gene -> cognate pathway term
COGNATE = {
    "9606": {
        "WNT3A": "GO:0016055", "WNT5A": "GO:0016055", "WNT1": "GO:0016055",
        "SHH": "GO:0007224", "IHH": "GO:0007224", "DLL1": "GO:0007219", "JAG1": "GO:0007219",
        "TGFB1": "GO:0007179", "BMP4": "GO:0030509", "NODAL": "GO:0038092",
        "EGF": "GO:0007173", "TGFA": "GO:0007173", "INS": "GO:0008286",
        "FGF2": "GO:0008543", "FGF8": "GO:0008543", "IFNG": "GO:0060333", "TNF": "GO:0033209",
        "IL6": "GO:0070102", "KITLG": "GO:0038109", "EPO": "GO:0038162", "CXCL12": "GO:0038146",
        "VEGFA": "GO:0048010", "NGF": "GO:0038180", "LEP": "GO:0033210",
        # receptor comparators
        "FZD1": "GO:0016055", "PTCH1": "GO:0007224", "NOTCH1": "GO:0007219",
        "EGFR": "GO:0007173", "INSR": "GO:0008286",
    },
    "7227": {
        "wg": "GO:0016055", "hh": "GO:0007224", "Dl": "GO:0007219", "Ser": "GO:0007219",
        "dpp": "GO:0030509", "gbb": "GO:0030509", "spi": "GO:0007173", "grk": "GO:0007173",
        "upd1": "GO:0007259", "Ilp2": "GO:0008286", "boss": "GO:0045500", "Pvf1": "GO:0048010",
        "bnl": "GO:0008543", "spz": "GO:0008063",
        "fz": "GO:0016055", "ptc": "GO:0007224", "N": "GO:0007219", "Egfr": "GO:0007173",
        "InR": "GO:0008286", "Tl": "GO:0008063",
    },
    # The pombe pheromone pathway term (GO:0000750) is obsolete; no cognate term is checked.
    "284812": {"map2": None, "mfm1": None, "mfm2": None, "mfm3": None, "mam2": None, "map3": None},
}
RECEPTORS = {"FZD1", "PTCH1", "NOTCH1", "EGFR", "INSR", "fz", "ptc", "N", "Egfr", "InR", "Tl", "mam2", "map3"}
# Name search returns the wrong gene (Dl matches dorsal) or no reviewed entry.
OVERRIDES = {("7227", "Dl"): "P10041", ("7227", "upd1"): "Q9VWW4",
             ("7227", "Pvf1"): "Q9VWP6", ("7227", "bnl"): "Q9VDT9"}
SIGNAL_TRANSDUCTION = "GO:0007165"


def resolve(taxon: str, gene: str) -> str | None:
    if (taxon, gene) in OVERRIDES:
        return OVERRIDES[(taxon, gene)]
    r = requests.get("https://rest.uniprot.org/uniprotkb/search", params={
        "query": f"gene_exact:{gene} AND organism_id:{taxon} AND reviewed:true",
        "fields": "accession,gene_names", "format": "json"}).json()
    hits = [(x["primaryAccession"], (x.get("genes") or [{}])[0].get("geneName", {}).get("value"))
            for x in r.get("results", [])]
    exact = [a for a, n in hits if n == gene]
    return (exact or [a for a, _ in hits] or [None])[0]


def bp_annotations(acc: str) -> list[dict]:
    rows, page = [], 1
    while True:
        r = requests.get(f"{QUICKGO}/annotation/search", headers=HEADERS, params={
            "geneProductId": acc, "aspect": "biological_process", "limit": 200, "page": page}).json()
        rows += r["results"]
        if page >= r["pageInfo"]["total"]:
            return rows
        page += 1


def ancestors(terms: list[str], relations: str) -> dict[str, set[str]]:
    out = {}
    for i in range(0, len(terms), 50):
        chunk = ",".join(terms[i:i + 50])
        r = requests.get(f"{QUICKGO}/ontology/go/terms/{chunk}/ancestors", headers=HEADERS,
                         params={"relations": relations}).json()
        for x in r["results"]:
            out[x["id"]] = set(x.get("ancestors", [])) | {x["id"]}
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    annots = {}
    for taxon, genes in COGNATE.items():
        for gene in genes:
            acc = resolve(taxon, gene)
            annots[(taxon, gene)] = (acc, bp_annotations(acc) if acc else [])
    terms = sorted({a["goId"] for _, rows in annots.values() for a in rows})
    structural = ancestors(terms, "is_a,part_of")
    with_reg = ancestors(terms, "is_a,part_of,regulates")
    exp = {"IDA", "IMP", "IPI", "IGI", "IEP", "EXP"}
    results = []
    for (taxon, gene), (acc, rows) in annots.items():
        cognate = COGNATE[taxon][gene]
        counts = collections.Counter()
        evidence = collections.Counter()
        for a in rows:
            t = a["goId"]
            if cognate and cognate in structural.get(t, ()):
                counts["pathway_" + a["qualifier"]] += 1
                if a["qualifier"] == "involved_in":
                    evidence["experimental" if a["goEvidence"] in exp else "other"] += 1
            elif cognate and cognate in with_reg.get(t, ()):
                counts["regulation"] += 1
            elif SIGNAL_TRANSDUCTION in structural.get(t, ()):
                counts["other_signal_transduction"] += 1
        results.append(dict(taxon=taxon, gene=gene, accession=acc, role="receptor" if gene in RECEPTORS else "ligand",
                            cognate_pathway=cognate, n_bp_annotations=len(rows), counts=dict(counts),
                            pathway_involved_in_evidence=dict(evidence)))
        print(f"{taxon:7} {gene:7} {acc} pathway(involved_in)={counts['pathway_involved_in']:3} "
              f"regulation={counts['regulation']:2} other_signaling={counts['other_signal_transduction']:2}")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(results, indent=1))


if __name__ == "__main__":
    main()
