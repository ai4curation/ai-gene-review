# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Compare every donkey NDEL1 gene model in UniProt with human NDEL1 (Q9GZM8).

Fetches the donkey NDEL1 entries (taxon 9793) from the UniProt REST API, writes
them to donkey_ndel1_models_rereview.fasta, and for each model reports:
  * length,
  * the last human residue of the gapless block shared with human isoform 1
    before the model's C-terminal exon diverges,
  * whether human-mapped functional residues (LIS1-binding region 114-133,
    DISC1-binding residues L266/E267, palmitoyl C273, CDK phosphosites
    S198/T219/S231/S242/T245, S344) are conserved.

Run: uv run --script compare_gene_models_rereview.py
"""

import hashlib
import json
import re
import sys
from pathlib import Path

import requests
from Bio import Align

HERE = Path(__file__).parent
HUMAN_UNIPROT = HERE.parents[2] / "human" / "NDEL1" / "NDEL1-uniprot.txt"
BENCHMARK = "A0A9L0IJ72"
QUERY = "https://rest.uniprot.org/uniprotkb/stream?query=gene_exact:NDEL1+AND+organism_id:9793&format=fasta"
SITES = {
    "S198": 198, "T219": 219, "S231": 231, "S242": 242, "T245": 245,
    "L266": 266, "E267": 267, "C273": 273, "S344": 344,
}


def human_seq() -> str:
    text = HUMAN_UNIPROT.read_text()
    block = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//", 1)[0]
    return re.sub(r"[^A-Z]", "", block)


def parse_fasta(text: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    acc = None
    for line in text.splitlines():
        if line.startswith(">"):
            acc = line.split("|")[1]
            seqs[acc] = ""
        elif acc:
            seqs[acc] += line.strip()
    return seqs


def collinear_end(seq: str, human: str) -> int:
    """Last human residue of the gapless N-terminal block shared with the model.

    Walks from residue 1 and stops at the first window of 5 consecutive
    mismatches, i.e. where the model's C-terminal exon diverges.
    """
    last = 0
    for i, (x, y) in enumerate(zip(seq, human)):
        if x == y:
            last = i + 1
        elif i + 5 <= min(len(seq), len(human)) and all(seq[j] != human[j] for j in range(i, i + 5)):
            break
    return last


def main() -> None:
    resp = requests.get(QUERY, timeout=60)
    resp.raise_for_status()
    (HERE / "donkey_ndel1_models_rereview.fasta").write_text(resp.text)
    donkey = parse_fasta(resp.text)
    human = human_seq()

    aligner = Align.PairwiseAligner()  # noqa: global alignment for site mapping
    aligner.mode = "global"
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.end_gap_score = 0

    rows = []
    for acc, seq in sorted(donkey.items(), key=lambda kv: -len(kv[1])):
        aln = aligner.align(seq, human)[0]
        # map human position -> donkey residue
        hmap: dict[int, str] = {}
        ident = paired = 0
        for (ds, de), (hs, he) in zip(*aln.aligned):
            for k in range(de - ds):
                hmap[hs + k + 1] = seq[ds + k]
                paired += 1
                ident += seq[ds + k] == human[hs + k]
        prefix = collinear_end(seq, human)
        sites = {name: (hmap.get(pos, "-") == human[pos - 1]) for name, pos in SITES.items()}
        lis1 = all(hmap.get(p) == human[p - 1] for p in range(114, 134))
        rows.append({
            "accession": acc,
            "benchmark": acc == BENCHMARK,
            "length": len(seq),
            "sha256": hashlib.sha256(seq.encode()).hexdigest()[:16],
            "collinear_with_human_isoform1_to": prefix,
            "tail_after_prefix": seq[prefix:prefix + 25],
            "aligned_pairs": paired,
            "identities": ident,
            "lis1_region_114_133_identical": lis1,
            "sites_identical": sites,
        })

    out = {"human_length": len(human), "human_tail_316_345": human[315:], "models": rows}
    (HERE / "gene_models_rereview.json").write_text(json.dumps(out, indent=2))
    print(f"human Q9GZM8 length {len(human)}; residues 316-345: {human[315:]}")
    for r in rows:
        tag = " (benchmark)" if r["benchmark"] else ""
        bad = [k for k, v in r["sites_identical"].items() if not v]
        print(f"{r['accession']}{tag}: {r['length']} aa; collinear with human 1-{r['collinear_with_human_isoform1_to']}"
              f" then '{r['tail_after_prefix']}...'; {r['identities']}/{r['aligned_pairs']} identical pairs;"
              f" LIS1 region conserved={r['lis1_region_114_133_identical']}; sites not conserved: {bad or 'none'}")
    sys.exit(0)


if __name__ == "__main__":
    main()
