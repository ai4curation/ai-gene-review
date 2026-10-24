# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""List all horse (taxon 9796) UniProt APP entries with their Ensembl transcript,
length, C-terminal 50 residues and presence of conserved APP motifs, and report
which transcript Ensembl flags as canonical for the horse APP gene.

Usage: uv run --script compare_horse_models.py <ensembl_gene_id>
"""
import sys, json, csv, io, urllib.request

gene = sys.argv[1]
url = ("https://rest.uniprot.org/uniprotkb/search?query=gene_exact:APP+AND+organism_id:9796"
       "&fields=accession,reviewed,length,xref_ensembl,sequence&format=tsv")
rows = list(csv.DictReader(io.StringIO(urllib.request.urlopen(url).read().decode()), delimiter="\t"))
motifs = {"Abeta1-16 DAEFRHDSGYEVHHQK": "DAEFRHDSGYEVHHQK",
          "KPI start EVCSEQAETGPCRA": "EVCSEQAETGPCRA",
          "OX-2 exon (MSQSLLKT)": "MSQSLLKT",
          "AICD Thr site VTPEER": "VTPEER",
          "YENPTY": "YENPTY"}
for r in rows:
    s = r["Sequence"]
    present = [k for k, m in motifs.items() if m in s]
    absent = [k for k, m in motifs.items() if m not in s]
    print(f"{r['Entry']} {r['Reviewed']} length {r['Length']} ensembl {r['Ensembl'].strip(';')}")
    print(f"  C-terminal 50: {s[-50:]}")
    print(f"  motifs present: {'; '.join(present) or 'none'}")
    print(f"  motifs absent: {'; '.join(absent) or 'none'}")
e = json.load(urllib.request.urlopen(
    f"https://rest.ensembl.org/lookup/id/{gene}?expand=1;content-type=application/json"))
print(f"Ensembl gene {gene} canonical transcript: {e.get('canonical_transcript')}")
for t in e["Transcript"]:
    tl = t.get("Translation") or {}
    print(f"  {t['id']} canonical={t.get('is_canonical')} protein={tl.get('id')} length={tl.get('length')}")
