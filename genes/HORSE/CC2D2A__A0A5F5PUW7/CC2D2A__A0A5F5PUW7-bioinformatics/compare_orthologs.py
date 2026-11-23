# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython", "requests"]
# ///
"""Compare horse CC2D2A (A0A5F5PUW7) with human/mouse CC2D2A and the CC2D2B paralog.

- Global BLOSUM62 alignments of the horse gene-centric canonical model against
  human CC2D2A (Q9P2K1, PTHR20837:SF7), mouse Cc2d2a (Q8CFW7, SF7), human CC2D2B
  (Q6DHV5, SF2) and the second horse model of the same gene (A0A5F5PJ44).
- Maps the human C2 domain and coiled-coil features and every disease-associated
  human missense VARIANT onto horse residues and reports conservation.

Human and horse sequences are read from the local UniProt flat files; mouse
Cc2d2a and human CC2D2B are fetched from the UniProt REST API.
Run: uv run compare_orthologs.py
"""

import re
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
GENES = HERE.parents[2]


def seq_from_flatfile(text: str) -> str:
    sq = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", sq)


def fetch_fasta(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


horse = seq_from_flatfile((HERE.parent / "CC2D2A__A0A5F5PUW7-uniprot.txt").read_text())
human_text = (GENES / "human" / "CC2D2A" / "CC2D2A-uniprot.txt").read_text()
human = seq_from_flatfile(human_text)
others = {
    "mouse Cc2d2a Q8CFW7 (SF7)": fetch_fasta("Q8CFW7"),
    "human CC2D2B Q6DHV5 (SF2)": fetch_fasta("Q6DHV5"),
    "horse CC2D2A A0A5F5PJ44 (other model)": seq_from_flatfile(
        (GENES / "HORSE" / "CC2D2A" / "CC2D2A-uniprot.txt").read_text()
    ),
}

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"


def summarise(name: str, a: str, b: str):
    aln = aligner.align(a, b)[0]
    pairs = 0
    ident = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            pairs += 1
            ident += a[i] == b[j]
    print(
        f"{name}: len={len(b)}; aligned pairs={pairs}; identical={ident} "
        f"({100 * ident / pairs:.1f}% of aligned; {100 * ident / len(a):.1f}% of horse length)"
    )
    return aln


print(f"horse A0A5F5PUW7 length: {len(horse)}")
print(f"human Q9P2K1 length: {len(human)}")
aln_h = summarise("human CC2D2A Q9P2K1 (SF7)", horse, human)
for name, s in others.items():
    summarise(name, horse, s)

# human -> horse position map
hmap = {}
for (s1, e1), (s2, e2) in zip(*aln_h.aligned):
    for i, j in zip(range(s1, e1), range(s2, e2)):
        hmap[j + 1] = i + 1  # human pos -> horse pos (1-based)


def region_cov(start: int, end: int):
    mapped = [p for p in range(start, end + 1) if p in hmap]
    same = [p for p in mapped if human[p - 1] == horse[hmap[p] - 1]]
    return len(mapped), len(same), end - start + 1


print("\nHuman UniProt features mapped to horse:")
for kind, s, e in re.findall(r"^FT   (DOMAIN|COILED)\s+(\d+)\.\.(\d+)", human_text, re.M):
    m, same, n = region_cov(int(s), int(e))
    hs = [hmap.get(p) for p in range(int(s), int(e) + 1) if p in hmap]
    print(
        f"  {kind} human {s}-{e}: horse {min(hs)}-{max(hs)}; mapped {m}/{n}, identical {same} ({100 * same / n:.1f}%)"
    )

print("\nHuman disease-associated missense variants (UniProt VARIANT) at horse positions:")
var_re = re.compile(r'^FT   VARIANT\s+(\d+)\n((?:FT {19}.*\n)+)', re.M)
n_tot = n_cons = 0
for pos, body in var_re.findall(human_text):
    body = " ".join(line[21:].strip() for line in body.splitlines())
    m = re.search(r'/note="([A-Z]) -> ([A-Z]) \(in ([^)]*)', body)
    if not m:
        continue
    ref, alt, note = m.groups()
    if not re.search(r"MKS6|JBTS9|COACH2|RP93", note):
        continue
    p = int(pos)
    hp = hmap.get(p)
    hres = horse[hp - 1] if hp else "-"
    n_tot += 1
    n_cons += hres == ref
    print(f"  human {ref}{p}{alt} ({note.split(';')[0]}): horse {hres}{hp if hp else ''} {'conserved' if hres == ref else 'DIFFERENT'}")
print(f"  conserved: {n_cons}/{n_tot}")
