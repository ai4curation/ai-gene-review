# A0A1S3Y076 vs Arabidopsis PRORP1/2/3 (re-review, 2026-10-20)

Script: `compare_prorp_rereview.py` (run with `uv run --no-project --with biopython python compare_prorp_rereview.py`).
Raw output: `compare_prorp_rereview.out`. Relative sequences in `relatives.fasta` were fetched from UniProt REST
(Q680B9 PRORP2, F4JKB6 PRORP3, Q66GI4 PRORP1).

Method: global pairwise alignment (BLOSUM62, gap open -10, extend -0.5, free end gaps) of the 540-aa target
against each Arabidopsis PRORP; identity over aligned columns; PRORP1 metal-binding positions (UniProt Q66GI4
BINDING features) mapped through the alignment.

## Results

- A0A1S3Y076 length 540 aa (PRORP2 528 aa, PRORP3 576 aa, PRORP1 572 aa including its 70-aa transit peptide).
- Identity: PRORP2 57.2% (279/488 columns); PRORP3 58.6% (282/481); PRORP1 49.9% (238/477).
- All eight PRORP1 metal-binding residues are conserved in the target:
  Zn ligands C255, C258, H459, C476; NYN catalytic aspartates D310, D386, D387, D405
  (PRORP1 C344, C347, H548, C565 and D399, D474, D475, D493 respectively).
- The target N-terminus (MDKNKKKKNLTPEVQFRLSL...) begins directly with the PPR region and has no
  extension corresponding to the PRORP1 organellar transit peptide.

## Interpretation

The target is equally close to the two Arabidopsis nuclear PRORPs (PRORP2/PRORP3) and more distant from the
organellar PRORP1, consistent with its PANTHER placement in PTHR13547:SF13 (PROTEINACEOUS RNASE P 2, which
contains Arabidopsis PRORP2 Q680B9) rather than SF1 (which contains PRORP1 Q66GI4 and animal mitochondrial
PRORP). It is a full-length protein with an intact catalytic site, so it is predicted to be an active nuclear
protein-only RNase P. Pairwise identity alone does not establish orthology; the subfamily placement is the
phylogenetic basis, and these numbers are only consistent with it.
