#!/usr/bin/env python3
"""Bulk-download whole-proteome annotations (one request per source, not per gene).

  data/<ORG>/uniprot.tsv   UniProt REST *stream* endpoint: accession, symbol, ordered
                           locus, Rhea IDs (from CC CATALYTIC ACTIVITY), EC, GO MF/BP.
                           One HTTP request returns the whole proteome.
  data/<ORG>/goa.gaf.gz    GOA GAF for the organism/proteome (carries evidence codes,
                           which the UniProt GO columns do not).
  data/go-edit.obo         GO editors' file: the only GO release form whose RHEA xrefs keep
                           their skos:exactMatch/narrowMatch/broadMatch predicate.
  data/chebiId_name.tsv    Rhea's ChEBI names (for participants that only occur in transport
                           reactions, so the currency filter can recognise them).
  data/rhea-directions.tsv maps directional Rhea ids (UniProt often cites LR/RL ids)
                           to the master reaction.

Usage: uv run python fetch_bulk.py PSEPK [human ...]
"""
from __future__ import annotations

import shutil
import sys
import urllib.request
from pathlib import Path

DATA = Path(__file__).parent / "data"

UNIPROT_FIELDS = "accession,gene_primary,gene_oln,reviewed,rhea,ec,go_f,go_p"
ORGANISMS = {
    # query is a UniProtKB query; gaf is a GOA download for the same proteome
    "PSEPK": {
        "query": "organism_id:160488",
        "gaf": "https://ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/109.P_putida_KT2440.goa",
    },
    "human": {
        "query": "organism_id:9606 AND reviewed:true",
        "gaf": "https://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/goa_human.gaf.gz",
    },
}


def download(url: str, dest: Path):
    print(f"GET {url}\n -> {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=600) as r, dest.open("wb") as fh:
        shutil.copyfileobj(r, fh)


def main():
    if not (DATA / "rhea-directions.tsv").exists():
        download("https://ftp.expasy.org/databases/rhea/tsv/rhea-directions.tsv", DATA / "rhea-directions.tsv")
    if not (DATA / "chebiId_name.tsv").exists():
        download("https://ftp.expasy.org/databases/rhea/tsv/chebiId_name.tsv", DATA / "chebiId_name.tsv")
    if not (DATA / "go-edit.obo").exists():  # carries skos predicates on RHEA xrefs
        download("https://raw.githubusercontent.com/geneontology/go-ontology/master/src/ontology/go-edit.obo",
                 DATA / "go-edit.obo")
    for org in sys.argv[1:]:
        cfg = ORGANISMS[org]
        q = urllib.parse.quote(cfg["query"])
        download(f"https://rest.uniprot.org/uniprotkb/stream?query={q}&fields={UNIPROT_FIELDS}&format=tsv",
                 DATA / org / "uniprot.tsv")
        gaf = DATA / org / "goa.gaf.gz"
        if cfg["gaf"].endswith(".gz"):
            download(cfg["gaf"], gaf)
        else:  # plain-text proteome file: gzip it for uniform reading
            import gzip
            tmp = DATA / org / "goa.gaf"
            download(cfg["gaf"], tmp)
            with tmp.open("rb") as i, gzip.open(gaf, "wb") as o:
                shutil.copyfileobj(i, o)
            tmp.unlink()


if __name__ == "__main__":
    import urllib.parse  # noqa: F401
    main()
