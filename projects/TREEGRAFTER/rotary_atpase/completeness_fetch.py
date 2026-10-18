"""Fetch bacterial reference proteomes and F-type/V-type rotary ATPase family members from UniProt REST.

Writes large TSVs to ./cache (git-ignored). Run:
  uv run --with requests projects/TREEGRAFTER/rotary_atpase/completeness_fetch.py
"""
import csv, gzip, io, sys, requests
import os, pathlib

CACHE = pathlib.Path(__file__).resolve().parent / "cache"
CACHE.mkdir(exist_ok=True)
os.chdir(CACHE)

BASE = "https://rest.uniprot.org"
def stream(endpoint, query, fields, out):
    r = requests.get(f"{BASE}/{endpoint}/stream", params=dict(query=query, fields=fields, format="tsv", compressed="true"), timeout=600)
    r.raise_for_status()
    open(out, "wb").write(gzip.decompress(r.content))
    print(out, sum(1 for _ in open(out)) - 1, file=sys.stderr)

stream("proteomes", "reference:true AND taxonomy_id:2", "upid,organism,organism_id,protein_count,busco,lineage", "proteomes.tsv")

FAMS = {  # F-type subunits (InterPro families, checked against E. coli atp operon entries)
    "alpha": "IPR005294", "beta": "IPR005722", "gamma": "IPR000131", "delta": "IPR000711",
    "epsilon": "IPR001469", "a": "IPR000568", "b": "IPR002146", "c": "IPR000454",
    "V_alpha": "IPR022878", "V_beta": "IPR022879",  # V/A-type catalytic subunits
}
for name, ipr in FAMS.items():
    stream("uniprotkb", f"xref:interpro-{ipr} AND keyword:KW-1185 AND taxonomy_id:2",
           "accession,xref_proteomes,protein_name,gene_primary", f"fam_{name}.tsv")

# anything carrying the F-type synthase MF (incl. descendants), for false-positive check
stream("uniprotkb", "go:0046933 AND keyword:KW-1185 AND taxonomy_id:2",
       "accession,xref_proteomes,protein_name,gene_primary,xref_interpro,go_id", "go_0046933.tsv")
