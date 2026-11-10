# WHY2 review notes

- UniProt Q8VYF7 confirmed (WHY2_ARATH, At1g71260, GeneID 843467). GOA keyed to Q8VYF7, 26 rows (25 seeded).
- Literature synthesis in WHY2-deep-research-manual.md (no API deep research available).

## Decisions
- ssDNA binding: core MF. Direct AtWHY2 evidence [PMID:30698803 "AtOSB2 and AtWhirly2 bind to a pssDNA-10 substrate with dissociation constants (Kd) of 8 and 22 nM respectively"]. Generic DNA binding rows -> MODIFY to ssDNA binding.
- DNA repair rows -> MODIFY to GO:0097551 mitochondrial double-strand break repair (checked in OLS: is_a GO:0006302 is_a GO:0006281). Basis: ciprofloxacin DSB assay [PMID:20551348] plus in vitro MMEJ suppression [PMID:30698803]. WHY2 performs a step (binds the resected ssDNA), so this is participation, not just necessity.
- Mitochondrion rows kept (root organelle policy). NEW mitochondrial nucleoid (IC) from two lines: mtDNA ChIP [PMID:18423020] and punctate intramitochondrial GFP with nucleoid disorganisation in the mutant [PMID:32490348], plus the ssDNA-binding function itself.
- Chloroplast ISM -> REMOVE (prediction contradicted by GFP/import data); source_defects recorded.
- Defense response, regulation of transcription -> MARK_AS_OVER_ANNOTATED: family-level (WHY1) functions, no WHY2 evidence.
- mRNA binding (IBA/HDA/IDA) -> KEEP_AS_NON_CORE: interactome capture only.
- DNA repair complex (ComplexPortal WHY2 homotetramer) -> KEEP_AS_NON_CORE.
- Protein binding (GWD1, Y2H) -> REMOVE per protein-binding policy.
- No NEW process terms for mitochondrial morphology/germination phenotypes (PMID:32490348): phenotype only.
- PMID:21911368 read in full: potato StWHY2 24-mer assembly via K67 and AtWHY1 K91 complementation; no AtWHY2 experiment, used as background only.
