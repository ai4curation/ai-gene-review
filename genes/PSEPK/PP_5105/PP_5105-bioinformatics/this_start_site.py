"""Check the PP_5105 (Q88CS5) ThiS gene model against Pseudomonas ThiS orthologs.

Fetches every UniProtKB entry in genus Pseudomonas (taxon 286) carrying InterPro
IPR010035 (ThiS), reports the length distribution, aligns each ortholog to Q88CS5
and records where on Q88CS5 the ortholog's first residue aligns. Also aligns Q88CS5
to E. coli ThiS (O32583) and checks the C-terminal Gly-Gly motif.

Usage: python this_start_site.py PP_5105-uniprot.txt > this_start_site.out
Results are printed; nothing is hard-coded.
"""
import collections
import io
import sys
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

URL = ("https://rest.uniprot.org/uniprotkb/stream?query=xref:interpro-IPR010035"
       "+AND+taxonomy_id:286&format=fasta")
ECOLI = "https://rest.uniprot.org/uniprotkb/O32583.fasta"


def read_flatfile_seq(path):
    rec = SeqIO.read(path, "swiss")
    return str(rec.seq)


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return list(SeqIO.parse(io.StringIO(r.read().decode()), "fasta"))


def aligner():
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "local"
    return a


def main():
    q = read_flatfile_seq(sys.argv[1])
    print(f"Q88CS5 length {len(q)}; C-terminal dipeptide {q[-2:]}")
    al = aligner()
    for rec in fetch(ECOLI):
        aln = al.align(q, str(rec.seq))[0]
        qs, ts = aln.aligned[0][0][0], aln.aligned[1][0][0]
        print(f"E. coli ThiS {rec.id} len {len(rec.seq)}: local alignment begins at "
              f"Q88CS5 residue {qs + 1} / O32583 residue {ts + 1}; score {aln.score:.1f}")
        print(aln)
    recs = fetch(URL)
    lengths = collections.Counter(len(r.seq) for r in recs)
    print(f"Pseudomonas IPR010035 entries: {len(recs)}")
    print("length distribution:", dict(sorted(lengths.items())))
    gg = sum(1 for r in recs if str(r.seq).endswith("GG"))
    print(f"entries ending in GG: {gg}")
    starts = collections.Counter()
    m_at = collections.Counter()
    for r in recs:
        s = str(r.seq)
        if r.id.split("|")[1] == "Q88CS5":
            continue
        aln = al.align(q, s)[0]
        qs, ts = aln.aligned[0][0][0], aln.aligned[1][0][0]
        if ts == 0:
            starts[qs + 1] += 1
            m_at[(len(s), qs + 1)] += 1
    print("Q88CS5 residue to which ortholog residue 1 aligns (orthologs whose N-terminus is in the local alignment):")
    print(dict(sorted(starts.items())))
    print("(ortholog length, Q88CS5 residue aligned to ortholog Met1):", dict(sorted(m_at.items())))
    print(f"Q88CS5 residue 22 = {q[21]}; segment 22-30 = {q[21:30]}")


if __name__ == "__main__":
    main()
