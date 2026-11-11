# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Identity and relative analysis for A0A6I8W8A2 (LOC117183218, D. pseudoobscura).

1. Fetches every UniProt product of LOC117183218 and tests containment of
   the benchmark isoform X3 in the longest product (X1).
2. Fetches all D. pseudoobscura (46245) and D. melanogaster (7227) proteins with
   an RCC1 repeat (InterPro IPR000408), local-aligns X1 against each
   (BLOSUM62, gap -11/-1) and reports the top hits with their PANTHER
   family/subfamily and HECT domain status from UniProt.

Run: uv run compare_sequences.py
"""
import io
import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

API = "https://rest.uniprot.org/uniprotkb"


def fasta(query: str) -> dict[str, str]:
    r = requests.get(f"{API}/stream", params={"query": query, "format": "fasta"}, timeout=120)
    r.raise_for_status()
    return {rec.id.split("|")[1]: str(rec.seq) for rec in SeqIO.parse(io.StringIO(r.text), "fasta")}


def meta(accs: list[str]) -> dict[str, dict]:
    r = requests.get(
        f"{API}/accessions",
        params={"accessions": ",".join(accs), "fields": "accession,gene_names,length,xref_panther,ft_domain,xref_pfam", "format": "tsv"},
        timeout=120,
    )
    r.raise_for_status()
    lines = r.text.strip().split("\n")
    head = lines[0].split("\t")
    return {row.split("\t")[0]: dict(zip(head, row.split("\t"))) for row in lines[1:]}


same_gene = fasta("gene:LOC117183218 AND organism_id:46245")
md = meta(sorted(same_gene))
print("## Products of LOC117183218")
for a, s in sorted(same_gene.items(), key=lambda x: -len(x[1])):
    print(a, len(s), md[a]["PANTHER"], md[a]["Pfam"])
x1_acc = max(same_gene, key=lambda a: len(same_gene[a]))
x1 = same_gene[x1_acc]
x3 = same_gene["A0A6I8W8A2"]
for k in range(len(x3)):
    if x1.endswith(x3[k:]):
        print(f"A0A6I8W8A2 residues {k+1}-{len(x3)} identical to {x1_acc} residues {len(x1)-len(x3)+k+1}-{len(x1)}; "
              f"A0A6I8W8A2 unique N-terminus: {x3[:k]} (vs {x1_acc}: {x1[len(x1)-len(x3):len(x1)-len(x3)+k]})")
        break

al = PairwiseAligner(mode="local", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                     open_gap_score=-11, extend_gap_score=-1)
db = {}
for tax in ("46245", "7227"):
    db.update(fasta(f"organism_id:{tax} AND xref:interpro-IPR000408"))
hits = []
for a, s in db.items():
    if a in same_gene:
        continue
    aln = al.align(x1, s)[0]
    pairs = [(i, j) for i, j in zip(aln[0], aln[1]) if i != "-" and j != "-"]
    ident = sum(i == j for i, j in pairs)
    hits.append((aln.score, a, len(s), ident, len(pairs)))
hits.sort(reverse=True)
top = hits[:12]
m2 = meta([h[1] for h in top])
print(f"\n## Top local alignments of {x1_acc} (X1) vs fly RCC1-repeat proteins")
print("score\tacc\tgene\tlen\tidentity\tPANTHER\tHECT")
for sc, a, L, idn, n in top:
    d = m2[a]
    hect = "yes" if "HECT" in d["Domain [FT]"] else "no"
    print(f"{sc:.0f}\t{a}\t{d['Gene Names'].split(' ')[0]}\t{L}\t{idn}/{n} ({100*idn/n:.0f}%)\t{d['PANTHER']}\t{hect}")
