# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Map rat Pnkd B4F7D2 onto the reviewed human and mouse PNKD isoforms.

Fetches sequences live from UniProt REST and Pfam locations from the InterPro
API, aligns B4F7D2 globally to every isoform of Q8N490 (human) and Q69ZP3
(mouse), and to the other rat Pnkd TrEMBL products, checks the Zn(2+) ligand
positions annotated on human Q8N490, and writes RESULTS-rereview.md.

Run from this directory:  uv run --script compare_isoforms_rereview.py
"""

import io
from pathlib import Path

import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb"
INTERPRO = "https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot"
TARGET = "B4F7D2"
REVIEWED = ["Q8N490", "Q69ZP3"]
RAT_OTHERS = ["D3ZXB0", "A0A0G2JTS8", "A0A0G2K0M0", "F1M1E4"]
# Zn(2+) BINDING positions on human Q8N490 (UniProt FT lines)
ZN_LIGANDS = [172, 174, 176, 177, 229, 253, 291]


def fasta(query: str) -> list:
    r = requests.get(f"{UNIPROT}/search", params={"query": query, "format": "fasta", "includeIsoform": "true"}, timeout=60)
    r.raise_for_status()
    return list(SeqIO.parse(io.StringIO(r.text), "fasta"))


def single(acc: str) -> str:
    r = requests.get(f"{UNIPROT}/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return str(next(SeqIO.parse(io.StringIO(r.text), "fasta")).seq)


def pfam(acc: str) -> list:
    r = requests.get(f"{INTERPRO}/{acc}", timeout=60)
    r.raise_for_status()
    out = []
    for res in r.json()["results"]:
        for p in res["proteins"]:
            for loc in p["entry_protein_locations"]:
                for f in loc["fragments"]:
                    out.append((res["metadata"]["accession"], f["start"], f["end"]))
    return out


def aligner() -> PairwiseAligner:
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al


def compare(al, a: str, b: str):
    aln = al.align(a, b)[0]
    blocks, ident = [], 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        same = sum(1 for i in range(e1 - s1) if a[s1 + i] == b[s2 + i])
        ident += same
        blocks.append((int(s1) + 1, int(e1), int(s2) + 1, int(e2), same))
    return ident, blocks


def main() -> None:
    al = aligner()
    target = single(TARGET)
    lines = [
        "# Pnkd B4F7D2 re-review: mapping onto reviewed human and mouse PNKD isoforms",
        "",
        f"B4F7D2 length: {len(target)} residues. Sequences fetched live from UniProt REST; "
        "Biopython PairwiseAligner global, BLOSUM62, gap open -10, extension -0.5.",
        "",
        "## Alignment to reviewed isoforms and other rat products",
        "",
        "| Entry | Length | Identical residues | Aligned blocks (B4F7D2 start-end : entry start-end, identical) |",
        "|---|---|---|---|",
    ]
    records = []
    for acc in REVIEWED:
        records += [(r.id.split("|")[1], str(r.seq)) for r in fasta(f"accession:{acc}")]
    records += [(acc, single(acc)) for acc in RAT_OTHERS]
    for name, seq in records:
        ident, blocks = compare(al, target, seq)
        btxt = "; ".join(f"{a}-{b} : {c}-{d} ({s})" for a, b, c, d, s in blocks)
        lines.append(f"| {name} | {len(seq)} | {ident} | {btxt} |")
    human = dict(records)["Q8N490"]
    lines += ["", "## Zn(2+) ligand positions annotated on human Q8N490", "",
              "| Position | Q8N490 | B4F7D2 |", "|---|---|---|"]
    for p in ZN_LIGANDS:
        lines.append(f"| {p} | {human[p-1]} | {target[p-1]} |")
    lines += ["", "## Pfam domain locations (InterPro API)", "", "| Entry | Pfam | Start | End |", "|---|---|---|---|"]
    for acc in [TARGET, "Q69ZP3", "Q8N490"]:
        for pf, s, e in pfam(acc):
            lines.append(f"| {acc} | {pf} | {s} | {e} |")
    lines += ["", "## C-terminal sequences from residue 321", "",
              f"- B4F7D2: `{target[320:]}`",
              f"- Q69ZP3 (mouse isoform 1): `{dict(records)['Q69ZP3'][320:]}`",
              f"- Q8N490 (human isoform 1): `{human[320:]}`",
              "",
              "Interpretation is left to the review; sequence identity does not establish that a product "
              "is expressed, folds, localizes or catalyses any reaction."]
    Path("RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
