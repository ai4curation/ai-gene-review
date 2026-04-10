"""Analyze Ramazzottius varieornatus Cu/Zn SOD paralogs for catalytic residue conservation.

Canonical CuZnSOD active site (based on human SOD1, P00441):
- Cu ligands: His47, His49, His64, His121 (all 4 histidines)
- Zn ligands: His64 (bridging), His72, His81, Asp84
- Disulfide: Cys58-Cys147

We align all RAMVA SOD paralogs to human SOD1 and check which preserve
these critical residues.
"""

import re
from pathlib import Path
from Bio import SeqIO, Align
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Human SOD1 (P00441) mature sequence - the canonical reference
# Numbering starts from Ala1 (after signal peptide removal) in the mature protein
# This matches the residue numbering used in PDB structures
HUMAN_SOD1 = (
    "ATKAVCVLKGDGPVQGIINFEQKESNGPVKVWGSIKGLTEGLHGFHVHEFGDNTAGCTSAGPHFNPLSRKHGGPKDEERHVGDLGNVTADKDGVADVSIEDSVISLSGDHCIIGRTLVVHEKADDLGKGGNEESTKTGNAGSRLACGVIGIAQ"
)
# Length 153 - mature form (P00441 minus initial Met)
assert len(HUMAN_SOD1) == 153, f"Expected 153 aa, got {len(HUMAN_SOD1)}"
assert HUMAN_SOD1[46 - 1] == "H", f"Pos 46 should be H, got {HUMAN_SOD1[46-1]}"
assert HUMAN_SOD1[48 - 1] == "H", f"Pos 48 should be H, got {HUMAN_SOD1[48-1]}"
assert HUMAN_SOD1[63 - 1] == "H", f"Pos 63 should be H, got {HUMAN_SOD1[63-1]}"
assert HUMAN_SOD1[71 - 1] == "H", f"Pos 71 should be H, got {HUMAN_SOD1[71-1]}"
assert HUMAN_SOD1[80 - 1] == "H", f"Pos 80 should be H, got {HUMAN_SOD1[80-1]}"
assert HUMAN_SOD1[83 - 1] == "D", f"Pos 83 should be D, got {HUMAN_SOD1[83-1]}"
assert HUMAN_SOD1[120 - 1] == "H", f"Pos 120 should be H, got {HUMAN_SOD1[120-1]}"
assert HUMAN_SOD1[57 - 1] == "C", f"Pos 57 should be C, got {HUMAN_SOD1[57-1]}"
assert HUMAN_SOD1[146 - 1] == "C", f"Pos 146 should be C, got {HUMAN_SOD1[146-1]}"
# Key residues (human SOD1 numbering, 1-based from Ala1):
# Cu ligands: H46, H48, H63, H120
# Zn ligands: H63, H71, H80, D83
# Disulfide: C57-C146
# Note: Position 87 in the paper's numbering for RvSOD15 (Val87) corresponds to
# one of the copper-binding histidines via pairwise alignment

HUMAN_SOD1_CU_LIGANDS = [46, 48, 63, 120]  # His (63 is bridging)
HUMAN_SOD1_ZN_LIGANDS = [63, 71, 80, 83]    # His, His, His, Asp
HUMAN_SOD1_DISULFIDE = [57, 146]            # Cys


def parse_uniprot_sequence(uniprot_file: Path) -> tuple[str, str]:
    """Extract accession and sequence from a UniProt .txt file."""
    acc = None
    sequence_lines = []
    in_sequence = False
    with open(uniprot_file) as f:
        for line in f:
            if line.startswith("AC"):
                if acc is None:
                    acc = line.split()[1].rstrip(";")
            if line.startswith("SQ"):
                in_sequence = True
                continue
            if in_sequence:
                if line.startswith("//"):
                    break
                sequence_lines.append(line.strip().replace(" ", ""))
    return acc, "".join(sequence_lines)


def get_signal_peptide_end(uniprot_file: Path) -> int | None:
    """Find the end of the signal peptide if annotated."""
    with open(uniprot_file) as f:
        text = f.read()
    # Look for FT SIGNAL line
    match = re.search(r"FT\s+SIGNAL\s+\d+\.\.(\d+)", text)
    if match:
        return int(match.group(1))
    return None


def pairwise_align(seq1: str, seq2: str) -> tuple[str, str, float]:
    """Return aligned seq1, aligned seq2, and percent identity."""
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.substitution_matrix = Align.substitution_matrices.load("BLOSUM62")
    alignments = aligner.align(seq1, seq2)
    best = alignments[0]
    a1 = str(best[0])
    a2 = str(best[1])
    matches = sum(1 for x, y in zip(a1, a2) if x == y and x != "-")
    aligned_len = sum(1 for x, y in zip(a1, a2) if x != "-" and y != "-")
    identity = 100 * matches / aligned_len if aligned_len else 0
    return a1, a2, identity


def map_residues(ref_aligned: str, query_aligned: str, ref_positions: list[int]) -> dict[int, tuple[int | None, str]]:
    """Map reference residue positions to the query sequence.

    Returns dict of ref_pos -> (query_pos, query_residue). query_pos is None if gapped.
    """
    # Walk through alignment; track positions in reference and query
    ref_pos = 0
    query_pos = 0
    ref_to_query = {}
    for r, q in zip(ref_aligned, query_aligned):
        if r != "-":
            ref_pos += 1
        if q != "-":
            query_pos += 1
        if r != "-" and ref_pos in ref_positions:
            if q == "-":
                ref_to_query[ref_pos] = (None, "-")
            else:
                ref_to_query[ref_pos] = (query_pos, q)
    return ref_to_query


def analyze_sod(name: str, uniprot_file: Path) -> dict:
    """Analyze a single SOD paralog for catalytic residue preservation."""
    acc, full_seq = parse_uniprot_sequence(uniprot_file)
    sig_end = get_signal_peptide_end(uniprot_file)

    # Use mature sequence if signal peptide annotated
    if sig_end:
        mature = full_seq[sig_end:]
    else:
        mature = full_seq

    # Align to human SOD1
    ref_aln, qry_aln, identity = pairwise_align(HUMAN_SOD1, mature)

    # Map catalytic residues
    cu_map = map_residues(ref_aln, qry_aln, HUMAN_SOD1_CU_LIGANDS)
    zn_map = map_residues(ref_aln, qry_aln, HUMAN_SOD1_ZN_LIGANDS)
    ds_map = map_residues(ref_aln, qry_aln, HUMAN_SOD1_DISULFIDE)

    # Count preserved residues
    cu_preserved = sum(1 for pos in HUMAN_SOD1_CU_LIGANDS if cu_map.get(pos, (None, "-"))[1] == "H")
    zn_ok = sum(
        1
        for pos, expected in zip(HUMAN_SOD1_ZN_LIGANDS, ["H", "H", "H", "D"])
        if zn_map.get(pos, (None, "-"))[1] == expected
    )
    ds_preserved = sum(1 for pos in HUMAN_SOD1_DISULFIDE if ds_map.get(pos, (None, "-"))[1] == "C")

    # Verdict
    cu_intact = cu_preserved == 4
    zn_intact = zn_ok == 4
    ds_intact = ds_preserved == 2
    likely_functional = cu_intact and zn_intact and ds_intact

    return {
        "name": name,
        "accession": acc,
        "length_full": len(full_seq),
        "length_mature": len(mature),
        "signal_peptide_end": sig_end,
        "identity_to_human_sod1": identity,
        "cu_ligands": {pos: cu_map.get(pos, (None, "-")) for pos in HUMAN_SOD1_CU_LIGANDS},
        "zn_ligands": {pos: zn_map.get(pos, (None, "-")) for pos in HUMAN_SOD1_ZN_LIGANDS},
        "disulfide": {pos: ds_map.get(pos, (None, "-")) for pos in HUMAN_SOD1_DISULFIDE},
        "cu_preserved": f"{cu_preserved}/4",
        "zn_preserved": f"{zn_ok}/4",
        "disulfide_preserved": f"{ds_preserved}/2",
        "likely_functional": likely_functional,
    }


def main():
    # Find all SOD gene directories
    genes_dir = Path("/Users/cjm/repos/ai-gene-review/genes/RAMVA")
    sod_genes = [
        "RvY_13070",   # RvSOD15 - reviewed, pseudoenzyme per Sim & Inoue
        "RvY_00650",
        "RvY_00651",
        "RvY_01767",
        "RvY_03754",
        "RvY_03757",
        "RvY_09480",
        "RvY_10893",
        "RvY_17310",
        "RvY_15948",  # Copper chaperone
    ]

    results = []
    for gene in sod_genes:
        up_file = genes_dir / gene / f"{gene}-uniprot.txt"
        if not up_file.exists():
            print(f"WARNING: {up_file} does not exist")
            continue
        result = analyze_sod(gene, up_file)
        results.append(result)

    # Print summary table
    print("\n" + "=" * 100)
    print(f"{'Gene':<12} {'Length':<10} {'Cu lig':<8} {'Zn lig':<8} {'SS':<6} {'%id SOD1':<10} {'Verdict':<20}")
    print("=" * 100)
    for r in results:
        verdict = "LIKELY FUNCTIONAL" if r["likely_functional"] else "LIKELY NON-FUNCTIONAL"
        length = f"{r['length_mature']}(mat)" if r["signal_peptide_end"] else f"{r['length_full']}"
        print(
            f"{r['name']:<12} {length:<10} {r['cu_preserved']:<8} {r['zn_preserved']:<8} "
            f"{r['disulfide_preserved']:<6} {r['identity_to_human_sod1']:<10.1f} {verdict:<20}"
        )

    # Detailed per-gene breakdown
    print("\n" + "=" * 100)
    print("DETAILED CATALYTIC RESIDUE ANALYSIS")
    print("=" * 100)
    for r in results:
        print(f"\n{r['name']} ({r['accession']}) - length {r['length_full']} aa")
        if r["signal_peptide_end"]:
            print(f"  Signal peptide: 1-{r['signal_peptide_end']}")
        print(f"  Identity to human SOD1: {r['identity_to_human_sod1']:.1f}%")
        print(f"  Cu ligands (expect all H): ", end="")
        for pos in HUMAN_SOD1_CU_LIGANDS:
            q_pos, q_res = r["cu_ligands"][pos]
            marker = "OK" if q_res == "H" else "**X**"
            print(f"H{pos}->{q_res}(pos{q_pos}){marker}", end="  ")
        print()
        print(f"  Zn ligands (H H H D): ", end="")
        for pos, expected in zip(HUMAN_SOD1_ZN_LIGANDS, ["H", "H", "H", "D"]):
            q_pos, q_res = r["zn_ligands"][pos]
            marker = "OK" if q_res == expected else "**X**"
            print(f"{expected}{pos}->{q_res}(pos{q_pos}){marker}", end="  ")
        print()
        print(f"  Disulfide Cys (expect C C): ", end="")
        for pos in HUMAN_SOD1_DISULFIDE:
            q_pos, q_res = r["disulfide"][pos]
            marker = "OK" if q_res == "C" else "**X**"
            print(f"C{pos}->{q_res}(pos{q_pos}){marker}", end="  ")
        print()

    return results


if __name__ == "__main__":
    main()
