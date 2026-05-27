#!/usr/bin/env python3
"""Analyze conservation across CDC48/p97 orthologs.

Performs multiple sequence alignment using Biopython's built-in pairwise alignment
(as a proxy when external MSA tools like MUSCLE/MAFFT are unavailable), then computes
per-position conservation scores relative to the reference sequence.

Input: Multi-FASTA of orthologs, motif TSV from analyze_domains.py
Output: Conservation scores per position, conservation at functional sites
"""

import sys
import csv
from pathlib import Path
from collections import Counter

from Bio import SeqIO, Align


def compute_pairwise_identity(ref_seq: str, query_seq: str) -> tuple[float, list[bool]]:
    """Compute pairwise identity between reference and query, return identity and per-position match."""
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -3
    aligner.extend_gap_score = -0.5

    alignments = aligner.align(ref_seq, query_seq)
    best = alignments[0]

    # Count matches
    aligned = best.format("fasta")
    # Use the alignment coordinates instead
    matches = 0
    total = 0
    ref_aligned = []
    query_aligned = []

    # Extract aligned sequences from format
    lines = aligned.strip().split("\n")
    seqs = []
    current = ""
    for line in lines:
        if line.startswith(">"):
            if current:
                seqs.append(current)
            current = ""
        else:
            current += line
    if current:
        seqs.append(current)

    if len(seqs) >= 2:
        for r, q in zip(seqs[0], seqs[1]):
            if r != "-" and q != "-":
                total += 1
                if r == q:
                    matches += 1

    identity = matches / total if total > 0 else 0
    return identity, []


def compute_column_conservation(sequences: dict[str, str], ref_id: str) -> list[dict]:
    """Compute conservation score at each position of the reference sequence.

    Uses simple pairwise comparisons against reference (not full MSA column analysis).
    Conservation = fraction of orthologs with identical residue at each ref position.
    """
    ref_seq = sequences[ref_id]
    n_seqs = len(sequences) - 1  # Exclude reference

    if n_seqs == 0:
        return [{"position": i + 1, "residue": aa, "conservation": 1.0, "n_identical": 0, "n_aligned": 0}
                for i, aa in enumerate(ref_seq)]

    # For each reference position, count how many orthologs have the same AA
    # Use simple global alignment and map back to reference coordinates
    position_matches = [0] * len(ref_seq)
    position_aligned = [0] * len(ref_seq)

    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -3
    aligner.extend_gap_score = -0.5

    for seq_id, seq in sequences.items():
        if seq_id == ref_id:
            continue

        alignments = aligner.align(ref_seq, seq)
        best = alignments[0]

        # Parse the alignment to map ref positions
        aligned_lines = best.format("fasta").strip().split("\n")
        aligned_seqs = []
        current = ""
        for line in aligned_lines:
            if line.startswith(">"):
                if current:
                    aligned_seqs.append(current)
                current = ""
            else:
                current += line
        if current:
            aligned_seqs.append(current)

        if len(aligned_seqs) >= 2:
            ref_pos = 0
            for ref_char, query_char in zip(aligned_seqs[0], aligned_seqs[1]):
                if ref_char != "-":
                    if query_char != "-":
                        position_aligned[ref_pos] += 1
                        if ref_char == query_char:
                            position_matches[ref_pos] += 1
                    ref_pos += 1

    results = []
    for i, aa in enumerate(ref_seq):
        n_aligned = position_aligned[i]
        n_identical = position_matches[i]
        conservation = n_identical / n_aligned if n_aligned > 0 else 0.0
        results.append({
            "position": i + 1,
            "residue": aa,
            "conservation": round(conservation, 3),
            "n_identical": n_identical,
            "n_aligned": n_aligned,
        })

    return results


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <orthologs_fasta> <motifs_tsv> <output_prefix>", file=sys.stderr)
        sys.exit(1)

    orthologs_fasta = Path(sys.argv[1])
    motifs_tsv = Path(sys.argv[2])
    output_prefix = sys.argv[3]

    # Load sequences
    sequences = {}
    ref_id = None
    for record in SeqIO.parse(orthologs_fasta, "fasta"):
        sequences[record.id] = str(record.seq)
        if ref_id is None:
            ref_id = record.id  # First sequence is reference

    print(f"Loaded {len(sequences)} sequences, reference: {ref_id}")

    # Compute overall pairwise identities
    ref_seq = sequences[ref_id]
    identities = {}
    for seq_id, seq in sequences.items():
        if seq_id == ref_id:
            continue
        identity, _ = compute_pairwise_identity(ref_seq, seq)
        identities[seq_id] = identity
        print(f"  {seq_id}: {identity:.1%} identity to reference")

    # Write pairwise identity summary
    id_file = f"{output_prefix}_pairwise_identity.tsv"
    with open(id_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ortholog", "identity"], delimiter="\t")
        writer.writeheader()
        for seq_id, identity in sorted(identities.items(), key=lambda x: -x[1]):
            writer.writerow({"ortholog": seq_id, "identity": f"{identity:.4f}"})
    print(f"Wrote pairwise identities to {id_file}")

    # Compute per-position conservation
    print("Computing per-position conservation...")
    conservation = compute_column_conservation(sequences, ref_id)

    # Write full conservation profile
    cons_file = f"{output_prefix}_conservation.tsv"
    with open(cons_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["position", "residue", "conservation", "n_identical", "n_aligned"], delimiter="\t")
        writer.writeheader()
        for c in conservation:
            writer.writerow(c)
    print(f"Wrote conservation profile to {cons_file}")

    # Load motifs and check conservation at functional sites
    motifs = []
    with open(motifs_tsv) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            row["start"] = int(row["start"])
            row["end"] = int(row["end"])
            motifs.append(row)

    motif_cons_file = f"{output_prefix}_motif_conservation.tsv"
    with open(motif_cons_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["motif", "domain", "start", "end", "sequence", "mean_conservation", "min_conservation", "fully_conserved"],
            delimiter="\t",
        )
        writer.writeheader()
        for m in motifs:
            positions = range(m["start"] - 1, m["end"])  # Convert to 0-based for list indexing
            cons_values = [conservation[p]["conservation"] for p in positions if p < len(conservation)]
            if cons_values:
                mean_cons = sum(cons_values) / len(cons_values)
                min_cons = min(cons_values)
                fully_conserved = all(c >= 0.9 for c in cons_values)
            else:
                mean_cons = min_cons = 0
                fully_conserved = False

            writer.writerow({
                "motif": m["motif"],
                "domain": m.get("domain_assignment", ""),
                "start": m["start"],
                "end": m["end"],
                "sequence": m["sequence"],
                "mean_conservation": f"{mean_cons:.3f}",
                "min_conservation": f"{min_cons:.3f}",
                "fully_conserved": fully_conserved,
            })
            print(f"  {m['motif']} ({m['sequence']}): mean conservation = {mean_cons:.3f}")

    print(f"Wrote motif conservation to {motif_cons_file}")

    # Summary statistics
    all_cons = [c["conservation"] for c in conservation]
    print(f"\nOverall conservation statistics:")
    print(f"  Mean: {sum(all_cons)/len(all_cons):.3f}")
    print(f"  Positions with >90% conservation: {sum(1 for c in all_cons if c > 0.9)}/{len(all_cons)}")
    print(f"  Positions with 100% conservation: {sum(1 for c in all_cons if c >= 1.0)}/{len(all_cons)}")


if __name__ == "__main__":
    main()
