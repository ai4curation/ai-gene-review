# CG33090 PC isoform boundary mapping (re-review, 2026-10-20)

This supplements, and does not replace, `RESULTS.md`. It reuses the existing MAFFT G-INS-i
(`outputs/global.fasta`) and L-INS-i (`outputs/local.fasta`) alignments of X2JE45 (PC, 799 aa),
Q7KT91 (PB, 948 aa) and human GBA2 Q9HCG7, and maps chosen PC positions onto the other two
sequences with `map_isoform_boundary_rereview.py`. Raw output: `outputs/rereview-boundary-global.json`
and `outputs/rereview-boundary-local.json`.

Reproduce:

    uv run python map_isoform_boundary_rereview.py outputs/global.fasta --query X2JE45 --positions 1 28 29 51 296 356 362 575 787 --output outputs/rereview-boundary-global.json
    uv run python map_isoform_boundary_rereview.py outputs/local.fasta --query X2JE45 --positions 1 28 29 51 296 356 362 575 787 --output outputs/rereview-boundary-local.json

## Findings

In both alignments PC position 29, the first residue of the sequence shared with PB, aligns with PB position 178 and human GBA2 position 194.
The 28-residue PC-specific N terminus does not align consistently between strategies, so no residue-level homology is claimed for it.
PC therefore has no counterpart for approximately human GBA2 residues 1-193 (PB 1-177).

PC's own Pfam GH116 N-terminal domain match (51-296) maps to PB 200-445 and ends at human 455 in both alignments.
PC's Pfam GH116 catalytic region (356-787) maps to PB 505-936 and human 521-886 in both alignments.
The catalytic nucleophile PC Glu362 aligns with human Glu527, and the acid/base PC Asp575 aligns with human Asp677, in both alignments.

## Interpretation

The PC truncation removes sequence upstream of, and at the start of, the region Pfam recognizes as the GH116 N-terminal domain.
Pfam still detects that domain and the complete catalytic region in PC.
The alteration is distinct from the internal insertions and deletions tested in human GBA2 isoforms (PMID:33261081), so those human results show that GBA2 isoforms can differ in activity but do not predict PC's activity.
Whether PC folds, associates with membranes and hydrolyzes glucosides has not been measured.
