# Mrm2 (Q9VDT6) catalytic-site conservation check

Script: `compare_catalytic_sites.py` (run with `uv run python compare_catalytic_sites.py > RESULTS-catalytic.txt`).
Raw output: `RESULTS-catalytic.txt`.

## Method

UniProt entries for fly Mrm2 (Q9VDT6), E. coli RlmE (P0C0R7) and human MRM2 (Q9UI43) were
fetched from the UniProt REST API at run time. Each reference was globally aligned to Q9VDT6
(Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5), and every UniProt
"Active site" and "Binding site" feature of the reference was mapped to the aligned Q9VDT6
position.

## Results

- Q9VDT6 vs E. coli RlmE P0C0R7: 202 aligned pairs, 41.1% identity over aligned positions.
- Q9VDT6 vs human MRM2 Q9UI43: 237 aligned pairs, 42.6% identity over aligned positions.
- The experimentally supported RlmE active-site lysine (P0C0R7 K164, ECO:0000269 PubMed:12181314)
  maps to Q9VDT6 K201 (conserved). Human MRM2 K194 also maps to Q9VDT6 K201.
- All five experimentally supported RlmE SAM-binding residues (G63, W65, D83, D99, D124;
  PubMed:10983982) are conserved in Q9VDT6 (G91, W93, D119, D136, D161).
- Human MRM2 SAM-binding residues D112 and D154 are conserved (Q9VDT6 D119, D161); the motif
  PGAW (83-86) is PGSW in fly (90-93) and DV (129-130) is DF (136-137): conservative changes
  in non-ligand-contacting positions of these motifs, with the invariant G and W retained.

## Interpretation

Q9VDT6 retains the annotated catalytic lysine and the SAM-binding residues of the RlmE/MRM2
enzymes, so there is no sequence evidence that it is a pseudoenzyme. This supports, but does not
prove, transfer of rRNA uridine 2'-O-methyltransferase activity; no fly enzyme assay or rRNA
methylation mapping exists. Only UniProt-annotated sites were mapped; other tetrad residues of
the K-D-K-E motif were not separately tested here.
