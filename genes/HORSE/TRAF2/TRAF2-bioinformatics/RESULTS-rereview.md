# TRAF2 horse re-review: feature mapping (2026-10-20)

Script: [compare_features_rereview.py](compare_features_rereview.py); raw output: [compare_features_rereview.out](compare_features_rereview.out).
Input: the canonical sequences in `genes/human/TRAF2/TRAF2-uniprot.txt` (Q12933, 501 aa) and `genes/HORSE/TRAF2/TRAF2-uniprot.txt` (F7BIV4, 516 aa). Global alignment, BLOSUM62, gap open -10, extension -0.5. Human feature positions come from the Q12933 UniProt record.

## Results

- Every human residue has an aligned horse partner (0 unaligned human residues), so F7BIV4 is not a fragment.
- RING window (human 34-73): 37/40 identical; all 8 Cys/His positions are identical.
- cIAP-binding residues: human I285, V288 and E292 align to identical horse I300, V303 and E307.
- Coiled coil (human 299-348): 46/50 identical. MATH domain (human 351-496): 142/146 identical, with all 5 Cys/His positions identical.
- The phosphosite S11 is conserved.
- The extra 15 horse residues are two insertions in the linker between the second TRAF-type zinc finger and the cIAP-binding segment: horse 261-266 'SSSFLG' after human position 260, and horse 272-280 'NPGAEVSKA' after human position 265. None of the human splice-variant segments (VSP_007401 at 122, VSP_039687 at 53-63, VSP_039688 at 176-200) falls here.

## Interpretation and limits

F7BIV4 is a full-length TRAF2 gene model. Its 15-residue linker insertion does not remove or interrupt any annotated domain or functional residue. This analysis cannot tell whether the insertion is a horse-specific exon extension, an Ensembl gene-model artefact or an unannotated splice form. Phylogenetic placement comes from PANTHER (PTHR10131:SF21, TRAF2 subfamily, the same subfamily as human Q12933), not from this pairwise alignment.
