# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Compare all UniProt products of the donkey SEC23A gene with human SEC23A.

Usage:
  uv run --script compare_gene_models_rereview.py <out_dir>

Steps (all data fetched live; nothing is hardcoded):
1. UniProt gene-centric lookup for A0A9L0IQB9 -> canonical + related donkey entries.
2. Each donkey entry is globally aligned (BLOSUM62, open -10, extend -0.5) to human
   SEC23A Q15436; identity, coverage and gap blocks are printed.
3. Ensembl REST: the transcripts of the donkey gene carrying A0A9L0IQB9 are listed
   with exon counts, and the exons of the benchmark transcript are compared with
   those of the transcript encoding the UniProt canonical, reporting exons present
   in one transcript but not the other (by genomic coordinates).
"""
import json
import sys
import pathlib
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

BENCH = "A0A9L0IQB9"
HUMAN = "Q15436"


def get(url, accept="application/json"):
    req = urllib.request.Request(url, headers={"Accept": accept})
    return urllib.request.urlopen(req).read().decode()


def fasta_seq(acc):
    txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", "text/plain")
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))


def ensembl_xref(acc):
    d = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))
    for x in d.get("uniProtKBCrossReferences", []):
        if x["database"] == "Ensembl":
            props = {p["key"]: p["value"] for p in x.get("properties", [])}
            return x["id"].split(".")[0], props.get("GeneId", "").split(".")[0]
    return None, None


out = pathlib.Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)

gc = json.loads(get(f"https://rest.uniprot.org/genecentric/search?query=accession:{BENCH}"))
res = gc["results"][0]
canonical = res["canonicalProtein"]["id"]
members = [canonical] + [p["id"] for p in res.get("relatedProteins", [])]
print(f"UniProt gene-centric canonical: {canonical}")
print(f"gene-centric members: {', '.join(members)}")

al = Align.PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
al.mode = "global"
hseq = fasta_seq(HUMAN)
print(f"\nhuman {HUMAN} length {len(hseq)}")
tx_of = {}
for acc in members:
    s = fasta_seq(acc)
    (out / f"{acc}.fasta").write_text(f">{acc}\n{s}\n")
    tx, gene = ensembl_xref(acc)
    tx_of[acc] = tx
    aln = al.align(s, hseq)[0]
    pairs = ident = 0
    for (ds, de), (hs, he) in zip(*aln.aligned):
        for i, j in zip(range(ds, de), range(hs, he)):
            pairs += 1
            ident += s[i] == hseq[j]
    blocks = "; ".join(f"{ds+1}-{de}:{hs+1}-{he}" for (ds, de), (hs, he) in zip(*aln.aligned))
    print(f"## {acc} len {len(s)} transcript {tx} gene {gene}: identity {100*ident/pairs:.2f}% "
          f"over {pairs} pairs; human coverage {100*pairs/len(hseq):.1f}%; blocks {blocks}")

_, gene = ensembl_xref(BENCH)
g = json.loads(get(f"https://rest.ensembl.org/lookup/id/{gene}?expand=1"))
print(f"\nEnsembl gene {gene} transcripts:")
exons = {}
for t in g["Transcript"]:
    exons[t["id"]] = {(e["start"], e["end"]) for e in t["Exon"]}
    print(f"  {t['id']} exons {len(t['Exon'])} protein_len {t.get('Translation', {}).get('length')} "
          f"ensembl_canonical {t.get('is_canonical')}")
b, c = tx_of[BENCH], tx_of[canonical]
print(f"\nexons in {c} (UniProt canonical {canonical}) not in {b} ({BENCH}):")
for s_, e_ in sorted(exons[c] - exons[b]):
    print(f"  {s_}-{e_} length {e_-s_+1} nt")
print(f"exons in {b} not in {c}:")
for s_, e_ in sorted(exons[b] - exons[c]):
    print(f"  {s_}-{e_} length {e_-s_+1} nt")

# 4. Human functional residues (UniProt Q15436 features: Zn ligands C61/C66/C85/C88,
#    MIA3-binding gelsolin-repeat residues F628/Y672/Y678/F681, CLSD residue F382)
#    mapped through the benchmark-to-human alignment.
bseq = fasta_seq(BENCH)
aln = al.align(bseq, hseq)[0]
h2b = {}
for (ds, de), (hs, he) in zip(*aln.aligned):
    for i, j in zip(range(ds, de), range(hs, he)):
        h2b[j + 1] = i + 1
print(f"\nhuman residue -> {BENCH} residue:")
for p in [61, 66, 85, 88, 382, 628, 672, 678, 681]:
    q = h2b.get(p)
    print(f"  human {hseq[p-1]}{p} -> " + (f"{bseq[q-1]}{q}" if q else "gap"))
print(f"human segment absent from {BENCH}: "
      + "".join(hseq[j - 1] for j in range(1, len(hseq) + 1) if j not in h2b))
