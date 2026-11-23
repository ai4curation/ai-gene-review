"""Check the KBase query against A2RMK5 and score A2RMK5 with the SufB family HMM.

1. Global alignment of the KBase Dark Protein Atlas protein NZ_LKLC01000161.1_58
   (kbase_NZ_LKLC01000161.1_58.fasta, saved from the dashboard's sequence panel)
   against UniProtKB A2RMK5.
2. hmmsearch of A2RMK5 with the NCBIfam SufB model TIGR01980, downloaded from the
   InterPro API, reporting envelope coordinates, query coverage and E-value.

Run from this directory:
  uv run --no-project --with pyhmmer --with biopython python identity_and_family.py
"""

import gzip
import urllib.request
from pathlib import Path

import pyhmmer
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
HMM_URL = "https://www.ebi.ac.uk/interpro/api/entry/ncbifam/TIGR01980?annotation=hmm"
HMM_FILE = HERE / "TIGR01980.hmm"


def identity(a: str, b: str) -> None:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aln = aligner.align(a, b)[0]
    aligned = ident = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1
            ident += a[i] == b[j]
    print(f"KBase length {len(a)}; A2RMK5 length {len(b)}")
    print(f"aligned columns: {aligned}; identical: {ident}; identity: {ident / aligned:.1%}")
    print(f"sequences exactly equal: {a == b}")


def family(seq_id: str, seq: str) -> None:
    if not HMM_FILE.exists():
        with urllib.request.urlopen(HMM_URL) as r:
            HMM_FILE.write_bytes(gzip.decompress(r.read()))
    with pyhmmer.plan7.HMMFile(HMM_FILE) as f:
        hmm = f.read()
    alphabet = pyhmmer.easel.Alphabet.amino()
    target = pyhmmer.easel.TextSequence(name=seq_id.encode(), sequence=seq).digitize(alphabet)
    pipeline = pyhmmer.plan7.Pipeline(alphabet)
    hits = pipeline.search_hmm(hmm, pyhmmer.easel.DigitalSequenceBlock(alphabet, [target]))
    name = hmm.name.decode() if isinstance(hmm.name, bytes) else hmm.name
    acc = hmm.accession.decode() if isinstance(hmm.accession, bytes) else hmm.accession
    print(f"HMM {acc} ({name}), model length {hmm.M}")
    if len(hits) == 0:
        print("no hit")
        return
    for hit in hits:
        print(f"full-sequence E-value {hit.evalue:.2g}, score {hit.score:.1f}")
        for d in hit.domains:
            ali = d.alignment
            env_len = d.env_to - d.env_from + 1
            print(
                f"domain envelope {d.env_from}-{d.env_to} "
                f"(query coverage {env_len / len(seq):.1%}), "
                f"HMM {ali.hmm_from}-{ali.hmm_to} of {hmm.M} "
                f"(HMM coverage {(ali.hmm_to - ali.hmm_from + 1) / hmm.M:.1%}), "
                f"i-Evalue {d.i_evalue:.2g}"
            )


def main() -> None:
    kbase = next(SeqIO.parse(HERE / "kbase_NZ_LKLC01000161.1_58.fasta", "fasta"))
    a2 = next(SeqIO.parse(HERE / "A2RMK5.fasta", "fasta"))
    print("== KBase NZ_LKLC01000161.1_58 vs UniProtKB A2RMK5")
    identity(str(kbase.seq), str(a2.seq))
    print("== TIGR01980 hmmsearch on A2RMK5")
    family(a2.id, str(a2.seq))


if __name__ == "__main__":
    main()
