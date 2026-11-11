"""Compare horse DYNLT2B model A0A9L0S9P8 with human Q8WW35 and sibling horse models.

Run with the repository environment:
  uv run python genes/HORSE/DYNLT2B__A0A9L0S9P8/DYNLT2B__A0A9L0S9P8-bioinformatics/compare_s9p8.py

Inputs: the cached horse (A0A9L0S9P8) and human (Q8WW35) UniProt flat files, plus
live UniProt FASTA for the sibling horse models of the same Ensembl gene
(A0A9L0TLH8, A0A9L0S150). For each human secondary-structure element (from the
human record's STRAND/HELIX features, PDB 8RGI) it reports how many human residues
are paired with an *identical* horse residue, not merely aligned. It also reports
the longest shared C-terminal stretch between S9P8 and each sibling model, which
locates where the S9P8 N-terminus diverges from the other gene models.
Writes results.json and RESULTS.md next to this script.
"""

import json
from pathlib import Path

import requests
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

here = Path(__file__).resolve().parent
root = next(p for p in here.parents if (p / "pyproject.toml").exists())
HORSE_FILE = root / "genes/HORSE/DYNLT2B__A0A9L0S9P8/DYNLT2B__A0A9L0S9P8-uniprot.txt"
HUMAN_FILE = root / "genes/human/DYNLT2B/DYNLT2B-uniprot.txt"
SIBLINGS = ["A0A9L0TLH8", "A0A9L0S150"]

horse = str(SeqIO.read(HORSE_FILE, "swiss").seq)
human_rec = SeqIO.read(HUMAN_FILE, "swiss")
human = str(human_rec.seq)
elements = [
    (f.type, int(f.location.start) + 1, int(f.location.end))
    for f in human_rec.features
    if f.type in ("STRAND", "HELIX")
]

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"


def pair_map(a: str, b: str) -> dict[int, int]:
    """Map 1-based positions of b to 1-based positions of a (aligned pairs only)."""
    aln = aligner.align(a, b)[0]
    m: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(int(a1 - a0)):
            m[int(b0) + i + 1] = int(a0) + i + 1
    return m


# human position -> horse position
h2x = pair_map(horse, human)
identical = {h for h, x in h2x.items() if human[h - 1] == horse[x - 1]}
overall = {
    "horse_length": len(horse),
    "human_length": len(human),
    "horse_starts_with_met": horse.startswith("M"),
    "aligned_pairs": len(h2x),
    "identical_pairs": len(identical),
    "identity_pct_of_aligned": round(100 * len(identical) / len(h2x), 2),
}

per_element = []
for kind, start, end in elements:
    span = range(start, end + 1)
    per_element.append(
        {
            "element": kind,
            "human_start": start,
            "human_end": end,
            "human_seq": human[start - 1 : end],
            "aligned": sum(1 for p in span if p in h2x),
            "identical": sum(1 for p in span if p in identical),
            "length": len(span),
        }
    )

siblings = {}
for acc in SIBLINGS:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    seq = "".join(r.text.split("\n")[1:])
    k = 0
    while k < min(len(seq), len(horse)) and seq[-1 - k] == horse[-1 - k]:
        k += 1
    siblings[acc] = {
        "length": len(seq),
        "shared_c_terminal_suffix": k,
        "s9p8_divergent_prefix": horse[: len(horse) - k],
        "sibling_prefix_replaced": seq[: len(seq) - k],
    }

# first human residue whose identical pairing begins a run of >=10 identities
first_conserved = next(
    h for h in sorted(identical) if all(h + i in identical for i in range(10))
)
overall["first_human_residue_of_conserved_core"] = first_conserved

out = {"overall": overall, "per_element": per_element, "siblings": siblings}
(here / "results.json").write_text(json.dumps(out, indent=2) + "\n")

lines = [
    "# A0A9L0S9P8 (horse DYNLT2B, UniProt gene-centric entry) vs human Q8WW35",
    "",
    f"Horse length {overall['horse_length']}; starts with Met: {overall['horse_starts_with_met']}. "
    f"Global alignment to human ({overall['human_length']} aa): {overall['aligned_pairs']} aligned pairs, "
    f"{overall['identical_pairs']} identical ({overall['identity_pct_of_aligned']}% of aligned).",
    f"First human residue starting a run of at least 10 consecutive identities: "
    f"{overall['first_human_residue_of_conserved_core']}.",
    "",
    "## Human structural elements (PDB 8RGI) - identical horse residues",
    "",
    "| element | human range | human sequence | aligned | identical | length |",
    "|---|---|---|---|---|---|",
]
for e in per_element:
    lines.append(
        f"| {e['element']} | {e['human_start']}-{e['human_end']} | {e['human_seq']} | "
        f"{e['aligned']} | {e['identical']} | {e['length']} |"
    )
lines += [
    "",
    "## Sibling horse models of the same gene (ENSECAG00000015913)",
    "",
    "| model | length | shared C-terminal suffix with S9P8 | S9P8 divergent prefix | sibling sequence it replaces |",
    "|---|---|---|---|---|",
]
for acc, s in siblings.items():
    lines.append(
        f"| {acc} | {s['length']} | {s['shared_c_terminal_suffix']} | "
        f"{s['s9p8_divergent_prefix']} | {s['sibling_prefix_replaced']} |"
    )
lines += [
    "",
    "Global alignment: Biopython PairwiseAligner, BLOSUM62, gap open -10, extension -0.5. "
    "Identity is counted per human residue paired with an identical horse residue. "
    "This is a sequence comparison only; it does not assess transcript support, folding or binding.",
    "",
]
(here / "RESULTS.md").write_text("\n".join(lines))
print("\n".join(lines))
