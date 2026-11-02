# A0BFB4 kinase-domain placement and catalytic motifs (2026-10-21 re-review)

Scripts: `kinase_domain_placement.py`, `catalytic_motifs.py` (run with `uv run python <script>`).
Computed outputs: `placement_results.json`, `nj_tree.nwk`, `kinase_domains.aln.fasta`,
`catalytic_motifs.json`. Nothing in this file is hard-coded in the scripts; values below are
copied from those outputs.

## 1. Catalytic motifs

All canonical kinase catalytic motifs are present in A0BFB4 (381 aa): glycine-rich loop GEGTFG at 103,
beta3 lysine motif ACK at 123 (K125, the UniProt ATP-binding residue), catalytic loop HRD at 213
(HRDIKPDN), DFG at 236 and APE at 260 (TPGFMAPE). The protein is predicted to be a catalytically
competent serine/threonine kinase, not a pseudokinase.

## 2. Kinase-domain placement against a characterised panel

The UniProt-annotated kinase domain of A0BFB4 (residues 96-348) was aligned (MAFFT L-INS-i) with the
kinase domains of 17 characterised kinases: ATG1/ULK (human ULK1, ULK2, yeast ATG1, worm unc-51),
ULK3, CAMK group (CAMK1, CAMK2A, CAMK4, DCLK1, PHKG1), CHEK1, CHEK2, PRKAA1, MARK2, STE20 group
(STK10/LOK, SLK) and CDC7 (outgroup).

Pairwise identity of A0BFB4 to the panel is uniformly low, 24.8-32.0%. The top values are
unc-51 32.0%, ULK2 30.7%, CAMK2A 30.1% and SLK 29.8%; yeast ATG1 is 24.8%. Identity alone
does not distinguish an ATG1/ULK relationship from a CAMK or STE20 relationship.

In the BLOSUM62 neighbour-joining tree, A0BFB4 falls on a long branch next to a clade made of the
ATG1/ULK kinases plus the two STE20 kinases. It sits away from the CAMK/CHK/AMPK/MARK clade. In 200 bootstrap
replicates A0BFB4 formed an exclusive clade with the four ATG1/ULK kinases in only 1 replicate. It
grouped as sister to the two STE20 kinases in 72 replicates and with the joint ULK + STE20 set in
64. Its nearest neighbour changed between replicates.

## Interpretation

- A0BFB4 is an active-site-intact Ser/Thr kinase domain (supports the kinase MF terms).
- Its placement is weakly toward the ULK/STE20 side of the kinome rather than the CAMK side. That is
  consistent with PANTHER's PTHR24348 tree graft, but it does **not** support specific orthology to
  ATG1/ULK: bootstrap support for A0BFB4 + ATG1/ULK is 1/200. This matches the conflict between the
  PANTHER tree leaf (PTHR24348:SF22) and the current HMM classification (PTHR44167:SF18).
- This is a small-panel distance analysis, not a full kinome phylogeny. It cannot settle the
  placement. It does show that the ATG1-specific inheritance used by the IBA autophagy terms is not
  robustly supported at the sequence level.
