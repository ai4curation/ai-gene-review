#!/usr/bin/env python3
"""Place rat Pnkd B4F7D2 against PNKD orthologs and the rat gene model.

Run from this directory with the repository environment:

    UV_NO_SYNC=1 uv run python compare_sequences.py

Inputs:
  * ../Pnkd-uniprot.txt (UniProt flat file for B4F7D2; target sequence)
  * ../Pnkd-same-gene-reference.json (UniProt JSON record for rat D3ZXB0)
  * UniProt REST: reviewed mouse Q69ZP3 and human Q8N490 with isoforms
    (both PANTHER PTHR11935:SF116, the subfamily of B4F7D2)
  * NCBI E-utilities: rat RefSeq protein NP_001128222.1 (isoform 1), the MGC
    cDNA BC168228 that B4F7D2 translates, the RefSeq mRNA NM_001134750 and the
    genomic sequence downstream of the exon whose end is the divergence point

Alignments describe sequence correspondence, not protein expression or activity.
"""

import json
import re
import urllib.request
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
INPUTS = HERE / "inputs"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Zn(2+) ligands of mouse Q69ZP3 (UniProt FT BINDING, by similarity to HAGH Q16775).
MOUSE_ZN_LIGANDS = [172, 174, 176, 177, 229, 253, 291]
# Genomic window just downstream of the RefSeq exon spanning NM_001134750 880-995
# (JAXUCZ010000009.1 83384077-83384192, from the RefSeq PRIMARY block).
GENOMIC_ACC = "JAXUCZ010000009.1"
GENOMIC_START, GENOMIC_END = 83384150, 83384400


def fetch(url: str, dest: Path) -> str:
    """Download url to dest once, then reuse the cached copy."""
    if not dest.exists():
        INPUTS.mkdir(exist_ok=True)
        with urllib.request.urlopen(url) as r:
            dest.write_bytes(r.read())
    return dest.read_text()


def fasta_records(text: str) -> dict[str, str]:
    out = {}
    for block in text.strip().split(">")[1:]:
        header, *seq = block.splitlines()
        acc = header.split("|")[1] if "|" in header else header.split()[0]
        out[acc] = "".join(seq).strip()
    return out


def uniprot_flatfile_sequence(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ.*?\n(.*?)^//", txt, re.S | re.M)
    assert m, "no SQ block"
    return "".join(m.group(1).split())


def protein_aligner() -> PairwiseAligner:
    al = PairwiseAligner(mode="global")
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    return al


def blocks(aln) -> list[tuple[int, int, int, int]]:
    return [
        (int(x) + 1, int(y), int(u) + 1, int(w))
        for (x, y), (u, w) in zip(*aln.aligned)
    ]


def main() -> None:
    target = uniprot_flatfile_sequence(GENE_DIR / "Pnkd-uniprot.txt")
    d3 = json.loads((GENE_DIR / "Pnkd-same-gene-reference.json").read_text())
    refs = {"D3ZXB0 (rat, 424 aa model)": d3["record"]["sequence"]["value"]}

    iso = fasta_records(
        fetch(
            "https://rest.uniprot.org/uniprotkb/search?query=(accession:Q8N490"
            "+OR+accession:Q69ZP3)&format=fasta&includeIsoform=true",
            INPUTS / "PNKD_human_mouse_isoforms.fasta",
        )
    )
    for acc, seq in sorted(iso.items()):
        refs[acc] = seq
    np1 = fasta_records(
        fetch(
            f"{EUTILS}?db=protein&id=NP_001128222.1&rettype=fasta",
            INPUTS / "NP_001128222.1.fasta",
        )
    )
    refs["NP_001128222.1 (rat RefSeq isoform 1)"] = next(iter(np1.values()))

    al = protein_aligner()
    rows = []
    for name, seq in refs.items():
        a = al.align(seq, target)[0]
        ident = sum(
            seq[x - 1 + k] == target[u - 1 + k]
            for x, y, u, w in blocks(a)
            for k in range(y - x + 1)
        )
        rows.append(
            {"reference": name, "length": len(seq), "identical": ident,
             "blocks_ref_vs_target": blocks(a)}
        )

    mouse = refs["Q69ZP3"]
    zn = [
        {"mouse_pos": p, "mouse": mouse[p - 1], "target": target[p - 1]}
        for p in MOUSE_ZN_LIGANDS
    ]
    rat1 = refs["NP_001128222.1 (rat RefSeq isoform 1)"]
    shared_prefix = next(
        (i for i, (a, b) in enumerate(zip(rat1, target)) if a != b),
        min(len(rat1), len(target)),
    )

    # Nucleotide check: where does the BC168228 CDS leave the RefSeq CDS, and
    # does the divergent sequence continue into the downstream intron?
    bc_seq = "".join(
        line.strip() for line in fetch(
            "https://www.ebi.ac.uk/ena/browser/api/fasta/BC168228",
            INPUTS / "BC168228.fasta").splitlines() if not line.startswith(">")
    ).upper()
    nm_seq = "".join(
        line.strip() for line in fetch(
            f"{EUTILS}?db=nuccore&id=NM_001134750&rettype=fasta",
            INPUTS / "NM_001134750.fasta").splitlines() if not line.startswith(">")
    ).upper()
    gen_seq = "".join(
        line.strip() for line in fetch(
            f"{EUTILS}?db=nuccore&id={GENOMIC_ACC}&seq_start={GENOMIC_START}"
            f"&seq_stop={GENOMIC_END}&rettype=fasta",
            INPUTS / "genomic_window.fasta").splitlines() if not line.startswith(">")
    ).upper()
    start = "ATGGCGGCGGTG"
    cb = bc_seq[bc_seq.find(start):]
    cn = nm_seq[nm_seq.find(start):]
    cds_div = next(i for i, (a, b) in enumerate(zip(cb, cn)) if a != b)
    probe = cb[cds_div:cds_div + 36]
    probe_hit = gen_seq.find(probe)
    exon_end_in_window = gen_seq[probe_hit - 9:probe_hit] if probe_hit >= 9 else ""

    out = {
        "target_accession": "B4F7D2",
        "target_length": len(target),
        "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5",
        "alignments": rows,
        "identical_prefix_with_rat_isoform1": shared_prefix,
        "rat_isoform1_length": len(rat1),
        "target_c_terminal_tail": target[shared_prefix:],
        "rat_isoform1_c_terminal_tail": rat1[shared_prefix:],
        "zn_ligands": zn,
        "cdna_vs_refseq_cds_divergence_nt": cds_div + 1,
        "cdna_divergent_probe": probe,
        "probe_offset_in_genomic_window": probe_hit,
        "genomic_bases_preceding_probe": exon_end_in_window,
        "genomic_window": f"{GENOMIC_ACC}:{GENOMIC_START}-{GENOMIC_END}",
    }
    (HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")

    lines = [
        "# Pnkd B4F7D2: placement against PNKD orthologs and the rat gene model",
        "",
        f"Target B4F7D2 has {len(target)} residues. {out['method']}.",
        "",
        "## Protein alignments (reference blocks vs target blocks, 1-based)",
        "",
        "| Reference | Length | Identical to B4F7D2 | Aligned blocks (ref start-end : target start-end) |",
        "|---|---|---|---|",
    ]
    for r in rows:
        b = "; ".join(f"{x}-{y}:{u}-{w}" for x, y, u, w in r["blocks_ref_vs_target"])
        lines.append(f"| {r['reference']} | {r['length']} | {r['identical']} | {b} |")
    lines += [
        "",
        "## Rat isoform 1 versus B4F7D2",
        "",
        f"B4F7D2 is identical to rat RefSeq NP_001128222.1 (isoform 1, {len(rat1)} aa) over "
        f"residues 1-{shared_prefix}; after that the two C-termini are unrelated.",
        "",
        f"- B4F7D2 tail ({len(target) - shared_prefix} aa): `{target[shared_prefix:]}`",
        f"- Isoform 1 tail ({len(rat1) - shared_prefix} aa): `{rat1[shared_prefix:]}`",
        "",
        "## Zn(2+) ligands (mouse Q69ZP3 positions, by similarity to HAGH)",
        "",
        "| Mouse position | Mouse | B4F7D2 |",
        "|---|---|---|",
    ]
    for z in zn:
        lines.append(f"| {z['mouse_pos']} | {z['mouse']} | {z['target']} |")
    lines += [
        "",
        "## Origin of the divergent tail (nucleotide level)",
        "",
        f"The BC168228 CDS (source of B4F7D2) matches the NM_001134750 CDS up to CDS "
        f"nucleotide {cds_div}, then diverges. The first 36 divergent cDNA bases "
        f"(`{probe}`) are found at offset {probe_hit} of genomic window "
        f"{out['genomic_window']}, preceded by `{exon_end_in_window}`.",
        "",
        "A probe offset >= 0 that begins with GT immediately after the exon end means the "
        "cDNA reads straight from the exon into the downstream intron (intron retention), "
        "so the B4F7D2 tail is intron-encoded rather than an alternative coding exon.",
        "",
        "Shared sequence does not establish that the B4F7D2 product is expressed, folds, "
        "localizes, or catalyses the reaction of the full-length protein.",
        "",
    ]
    (HERE / "RESULTS.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
