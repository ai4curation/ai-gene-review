# SNAP23 (donkey, Equus asinus; UniProt A0A8C4M285) - review notes

## Sources used

- Donkey UniProt record (unreviewed, Ensembl ENSEASP00005019168.1): `SNAP23-uniprot.txt`. Length 97 aa.
- Donkey GOA (8 IEA rows: 6 TreeGrafter GO_REF:0000118 from PANTHER:PTN000447812, plasma membrane via GO_REF:0000120, presynapse via GO_REF:0000108 inferred from synaptic vesicle priming): `SNAP23-goa.tsv`.
- Human SNAP23 (O00161) UniProt record, fetched 2026-10-14: `SNAP23-bioinformatics/human-SNAP23-O00161-uniprot.txt`.
- Donkey-human alignment: `SNAP23-bioinformatics/RESULTS.md`.
- Human/mouse QuickGO annotations (queried 2026-10-14) as comparator: human SNAP23 has IDA for helical-bundle zippering fusogenic activity, SNARE complex, vesicle fusion and plasma membrane; the synaptic vesicle priming and synaptic vesicle fusion to presynaptic active zone membrane rows on human/mouse SNAP23 are IBA only.
- No publication-based GOA rows for the donkey protein; no publications fetched.

## Sequence

- The entry is a truncated SNAP23 product [file:EQUAS/SNAP23/SNAP23-bioinformatics/RESULTS.md "The donkey entry A0A8C4M285 is a 97-residue product."].
- It keeps the first SNARE motif and the palmitoylated cysteine linker [RESULTS.md "all five linker cysteines (human C79, C80, C83, C85, C87) are conserved"].
- It lacks the second SNARE motif [RESULTS.md "The product lacks the human region 90..211, which includes the C-terminal t-SNARE coiled-coil motif (Qc, human 146..208)."].
- Other donkey SNAP23 entries exist in UniProt (A0A8C4M333, 211 aa; A0A8C4M5X5, 222 aa; A0A9L0K6I4, 209 aa; A0A9L0J3X0, 158 aa), queried 2026-10-14.

## Function (human ortholog)

- [human UniProt "SNAP23 is a t-SNARE (target-SNARE) that resides on"] target membranes and functions in fusion of transport vesicles with the plasma membrane; it supplies two of the four helices of the SNARE bundle.
- Localization: [human UniProt "Lipid-anchor {ECO:0000269|PubMed:21044946}"]; donkey record [donkey UniProt "SUBCELLULAR LOCATION: Cell membrane"].

## Review decisions (summary)

- plasma membrane: ACCEPT (palmitoylation cysteines conserved).
- helical-bundle zippering fusogenic activity, SNARE complex, exocytosis, vesicle fusion: UNDECIDED for this 97-aa product (correct for full-length SNAP23 but this product lacks the Qc SNARE motif; no data on whether such a product assembles into fusogenic complexes).
- synaptic vesicle priming, synaptic vesicle fusion to presynaptic active zone membrane, presynapse: MARK_AS_OVER_ANNOTATED (neuronal SNAP25 functions propagated across the SNAP-25 family; SNAP23 is the ubiquitous non-neuronal paralog).
