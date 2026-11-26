"""Compare Msed_1700 (A4YHF3) with its MCR paralog and reference ASDs.

Reproducible: fetches sequences and annotations live from UniProt REST.
Run:  uv run python compare_asd_mcr.py > results.txt

Outputs
 1. Pairwise global identity between A4YHF3 and comparators.
 2. Residues of each protein aligned to the catalytic Cys and His of the
    S. tokodaii MCR structure (Cys153, His248 in Q96YK1 numbering, PMID:23325803)
    and of the M. jannaschii ASD (Q57658).
 3. CDD subfamily signatures of all archaeal proteins named EC 1.2.1.75 in
    UniProt (the set reached by ARBA00067001), split into the MCR-type CDD
    models (cd23940/cd24150) and the ASD-type models (cd18130/cd02315).
"""
import io
import urllib.parse
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

PROTEINS = {
    "A4YHF3": "Msed_1700 (query)",
    "A4YEN2": "Msed_0709 M. sedula MCR",
    "Q96YK1": "STK_21710 S. tokodaii MCR (PDB 4DPK)",
    "Q971Y6": "STK_12420/ST1242 S. tokodaii asd",
    "Q57658": "MJ0205 M. jannaschii ASD (PDB 1YS4)",
}
REST = "https://rest.uniprot.org/uniprotkb"


def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()


def seq(acc):
    return str(next(SeqIO.parse(io.StringIO(fetch(f"{REST}/{acc}.fasta")), "fasta")).seq)


def aligner():
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score, a.extend_gap_score = -10, -0.5
    a.mode = "global"
    return a


def mapping(aln):
    """Map 1-based positions of target (seqA) to query (seqB)."""
    m = {}
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i in range(e1 - s1):
            m[s1 + i + 1] = s2 + i + 1
    return m


def identity(aln, a, b):
    same = sum(
        a[s1 + i] == b[s2 + i]
        for (s1, e1), (s2, e2) in zip(*aln.aligned)
        for i in range(e1 - s1)
    )
    return 100.0 * same / min(len(a), len(b))


def main():
    seqs = {acc: seq(acc) for acc in PROTEINS}
    al = aligner()
    q = seqs["A4YHF3"]
    print("## 1. Global pairwise identity to A4YHF3 (identical positions / shorter length)")
    for acc, name in PROTEINS.items():
        if acc == "A4YHF3":
            continue
        aln = al.align(q, seqs[acc])[0]
        print(f"{acc}\t{name}\t{identity(aln, q, seqs[acc]):.1f}%")

    print("\n## 2. Residues aligned to S. tokodaii MCR (Q96YK1) Cys153 / His248")
    ref = seqs["Q96YK1"]
    print(f"Q96YK1 C153={ref[152]} H248={ref[247]}")
    for acc in PROTEINS:
        if acc == "Q96YK1":
            continue
        aln = al.align(ref, seqs[acc])[0]
        m = mapping(aln)
        out = []
        for pos in (153, 248):
            j = m.get(pos)
            out.append(f"{pos}->{seqs[acc][j-1]}{j}" if j else f"{pos}->gap")
        print(f"{acc}\t{PROTEINS[acc]}\t" + "\t".join(out))

    print("\n## 3. CDD models on archaeal UniProt entries named EC 1.2.1.75")
    params = urllib.parse.urlencode({
        "query": "ec:1.2.1.75 AND taxonomy_id:2157",
        "fields": "accession,gene_oln,organism_name,xref_cdd,reviewed",
        "format": "tsv", "size": "500"})
    rows = [r.split("\t") for r in fetch(f"{REST}/search?{params}").strip().split("\n")[1:]]
    mcr = {"cd23940", "cd24150"}
    asd = {"cd18130", "cd02315"}
    counts = {"MCR-type CDD": 0, "ASD-type CDD": 0, "both/none": 0}
    for acc, oln, org, cdd, rev in rows:
        c = {x for x in cdd.split(";") if x}
        k = ("MCR-type CDD" if c & mcr and not c & asd else
             "ASD-type CDD" if c & asd and not c & mcr else "both/none")
        counts[k] += 1
        print(f"{acc}\t{oln}\t{rev}\t{cdd}\t{k}\t{org[:45]}")
    print("Totals:", counts, "of", len(rows))


if __name__ == "__main__":
    main()
