"""Map E. coli DusA (P32695) functional residues onto S. meliloti DusA (Q92P85).

Residues tested (E. coli DusA numbering; HAMAP MF_02041 features on P32695):
  C114 - catalytic proton donor (C114A inactive, Yu et al. 2011, PMID:22123979)
  FMN-binding residues 32-34, 84, 153, 186, 226-228, 248-249
  tRNA-interacting sites 111, 198, 201, 314, 317 (198, 314, 317 are the
  DusA subfamily-specific tRNA-binding signature, Byrne et al. 2015,
  PMID:25902496)

Also reports identity, and whether the KBase Dark Protein Atlas sequence
(NZ_RPHN01000062.1_55) contains Q92P85 exactly.

Run from this directory:
  uv run python map_ecoli_residues.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
ECOLI_SITES = {
    "catalytic proton donor": [114],
    "FMN binding": [32, 33, 34, 84, 153, 186, 226, 227, 228, 248, 249],
    "tRNA interaction": [111, 201],
    "tRNA interaction, DusA subfamily signature": [198, 314, 317],
}


def map_sites(ecoli, name: str, q: str) -> None:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aln = aligner.align(str(ecoli.seq), q)[0]
    e2q = {}
    for (es, ee), (qs, qe) in zip(*aln.aligned):
        for i, j in zip(range(es, ee), range(qs, qe)):
            e2q[i + 1] = j + 1
    print(f"\n== {name}: E. coli N-terminal FMN-binding residues 32-34 ==")
    for pos in (32, 33, 34):
        qp = e2q.get(pos)
        aa = ecoli.seq[pos - 1]
        print(f"  E. coli {aa}{pos} -> " + (f"{q[qp - 1]}{qp}" if qp else "gap"))


def main() -> None:
    ecoli = next(SeqIO.parse(HERE / "ecoli_dusA_P32695.fasta", "fasta"))
    query = next(SeqIO.parse(HERE / "Q92P85.fasta", "fasta"))
    kbase = next(SeqIO.parse(HERE / "kbase_NZ_RPHN01000062.1_55.fasta", "fasta"))

    refseq = next(SeqIO.parse(HERE / "refseq_WP_015241224.1.fasta", "fasta"))
    q, k = str(query.seq), str(kbase.seq)
    r = str(refseq.seq)
    print(f"RefSeq {refseq.id} length {len(r)}; Q92P85 is its residues "
          f"{r.find(q) + 1}-{len(r)}" if r.endswith(q) else "RefSeq does not end with Q92P85")
    offset = k.find(q)
    print(f"KBase {kbase.id} length {len(k)}; Q92P85 length {len(q)}")
    if offset >= 0 and k[offset:] == q:
        print(f"Q92P85 = KBase residues {offset + 1}-{len(k)} exactly "
              f"(KBase has a {offset}-residue N-terminal extension: {k[:offset]})")
    else:
        print("Q92P85 is not an exact suffix of the KBase sequence")

    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aln = aligner.align(str(ecoli.seq), q)[0]

    ident = aligned = 0
    e2q = {}
    for (es, ee), (qs, qe) in zip(*aln.aligned):
        for i, j in zip(range(es, ee), range(qs, qe)):
            aligned += 1
            ident += ecoli.seq[i] == q[j]
            e2q[i + 1] = j + 1
    print(f"E. coli DusA {ecoli.id} length {len(ecoli.seq)}")
    print(f"aligned columns: {aligned}; identity: {ident / aligned:.1%}")
    print()
    print(aln)
    for role, positions in ECOLI_SITES.items():
        print(f"\n{role}")
        for pos in positions:
            aa = ecoli.seq[pos - 1]
            qp = e2q.get(pos)
            if qp is None:
                print(f"  E. coli {aa}{pos}: gap in Q92P85")
                continue
            qa = q[qp - 1]
            mark = "conserved" if qa == aa else "DIFFERENT"
            print(f"  E. coli {aa}{pos} -> Q92P85 {qa}{qp} (KBase {qp + offset})  {mark}"
                  f"   E.coli {ecoli.seq[max(pos - 6, 0):pos + 5]}  Q92P85 {q[max(qp - 6, 0):qp + 5]}")


    map_sites(ecoli, "RefSeq WP_015241224.1 (upstream ATG start)", r)
    map_sites(ecoli, "KBase NZ_RPHN01000062.1_55", k)


if __name__ == "__main__":
    main()
