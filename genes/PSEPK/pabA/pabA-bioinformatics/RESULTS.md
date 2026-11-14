# PP_0420 (pabA/trpG): KT2440 amidotransferase inventory

## Question

Is PP_0420 (Q88QR8) the only TrpG/PabA-type glutamine amidotransferase in
*Pseudomonas putida* KT2440 that could partner both anthranilate synthase
component I (TrpE) and aminodeoxychorismate synthase component I (PabB)?

## Method

`amidotransferase_inventory.py` queries the live UniProt REST API for KT2440
(taxon 160488) proteins carrying Pfam PF00425 (chorismate-binding synthase
domain), Pfam PF00117 (class-I glutamine amidotransferase) or NCBIfam TIGR00566
(TrpG/PabA amidotransferase). Raw output: `inventory.tsv` (retrieved
2026-11-11).

## Results

- Chorismate-binding synthase components (PF00425): TrpE PP_0417 (TIGR00564)
  and PabB PP_2329 (TIGR00553, 446 aa). Neither carries a fused class-I GATase
  (PF00117) domain.
- Class-I GATase proteins (PF00117): PP_0420 is the only one matching the
  TrpG/PabA model TIGR00566. The others belong to dedicated enzymes (PyrG, CarA,
  HisH, GuaA) or to the ChyE-like PP_1842 (NF004212, PTHR42695).

## Interpretation

KT2440 has a standalone PabB but only one TrpG/PabA-family amidotransferase.
PP_0420 is therefore the best sequence-based candidate for the glutaminase
subunit of aminodeoxychorismate synthase as well as of anthranilate synthase,
an "amphibolic" arrangement. This is an inference from gene inventory only. No
experiment in KT2440 shows that PP_0420 partners PabB.
