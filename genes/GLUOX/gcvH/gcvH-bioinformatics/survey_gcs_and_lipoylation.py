#!/usr/bin/env python3
"""Survey the glycine cleavage system and the lipoylation machinery encoded by
Gluconobacter oxydans 621H (NCBITaxon:290633), using the UniProtKB REST API.

Purpose: two questions bear directly on the gcvH (Q5FRY1) review.

1. Does G. oxydans 621H encode a complete glycine cleavage system (P, T, H, L)?
   If it does not, the GO:0005960 / GO:0019464 annotations propagated onto
   Q5FRY1 would rest on family membership alone.
2. Which lipoyl-attachment route does the organism use? Organisms of the
   Bacillus subtilis type (LipM octanoyltransferase + LipL
   octanoyl-GcvH:E2 amidotransferase) route de novo lipoylation of all
   acceptors through GcvH, which makes GcvH a participant in protein
   lipoylation. Organisms of the Escherichia coli type (LipB) octanoylate
   each acceptor directly, so GcvH is only a lipoyl acceptor.

Run:  python3 survey_gcs_and_lipoylation.py
No API key or local database is needed. Results are printed and are not
cached; RESULTS.md records the output of the run it documents.
"""

import json
import urllib.parse
import urllib.request

TAXON = "290633"
BASE = "https://rest.uniprot.org/uniprotkb/search"
FIELDS = "accession,id,gene_names,protein_name,ec,reviewed"

# Each probe is (label, UniProt query fragment restricted to the taxon below).
PROBES = [
    ("GCS P protein (glycine dehydrogenase, decarboxylating)",
     'gene:gcvP OR protein_name:"glycine dehydrogenase"'),
    ("GCS T protein (aminomethyltransferase)",
     'gene:gcvT OR protein_name:aminomethyltransferase'),
    ("GCS H protein (lipoyl carrier)",
     'gene:gcvH OR protein_name:"glycine cleavage system H"'),
    ("GCS L protein (dihydrolipoyl dehydrogenase)",
     'protein_name:"dihydrolipoyl dehydrogenase" OR gene:lpdA'),
    ("LipB-type octanoyltransferase (E. coli route)",
     'gene:lipB OR protein_name:octanoyltransferase'),
    ("LipM-type octanoyltransferase (B. subtilis route)",
     'gene:lipM'),
    ("LipL octanoyl-GcvH:E2 amidotransferase (B. subtilis route)",
     'gene:lipL OR protein_name:"octanoyl-[GcvH]:protein N-octanoyltransferase"'),
    ("LipA lipoyl synthase", 'gene:lipA OR protein_name:"lipoyl synthase"'),
    ("LplA/LplJ lipoate-protein ligase (salvage)",
     'gene:lplA OR gene:lplJ OR protein_name:"lipoate--protein ligase"'),
]


def search(fragment):
    query = f"(organism_id:{TAXON}) AND ({fragment})"
    url = f"{BASE}?" + urllib.parse.urlencode(
        {"query": query, "fields": FIELDS, "format": "json", "size": "25"}
    )
    with urllib.request.urlopen(url, timeout=60) as handle:
        return json.load(handle).get("results", [])


def describe(entry):
    genes = []
    for gene in entry.get("genes", []):
        name = gene.get("geneName", {}).get("value")
        if name:
            genes.append(name)
        genes.extend(
            locus.get("value") for locus in gene.get("orderedLocusNames", [])
        )
    desc = entry.get("proteinDescription", {})
    recommended = desc.get("recommendedName") or {}
    name = recommended.get("fullName", {}).get("value")
    if not name and desc.get("submissionNames"):
        name = desc["submissionNames"][0].get("fullName", {}).get("value")
    return entry["primaryAccession"], "/".join(g for g in genes if g), name


def main():
    print(f"UniProtKB survey, organism_id:{TAXON} (G. oxydans 621H)\n")
    for label, fragment in PROBES:
        hits = search(fragment)
        print(f"## {label}")
        if not hits:
            print("  no entry matched this probe")
        for entry in hits:
            accession, genes, name = describe(entry)
            print(f"  {accession}\t{genes}\t{name}")
        print()


if __name__ == "__main__":
    main()
