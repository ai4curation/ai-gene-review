# DDHD1 notes

## 2026-10-17 — initial Mendelian-project review

The review covers all 12 normally fetched annotation identities and preserves their terms, qualifiers, original references, supporting entities and explicit isoform identifiers. Four UniProt products are retained at lengths 900, 872, 454 and 879 aa. The two HuRI interactions explicitly identify Q8NEL9-2; this does not establish equivalent functions for the other products.

The core is glycerophospholipid phospholipase A1 activity in the cytosolic pool, including direct participation in phosphatidylinositol metabolism. DDHD1 performs PI deacylation itself. The existing process term already covers this chemistry; a complete deacylation/re-acylation cycle is not established. No new annotation is proposed. The domain-to-metal-binding inference remains undecided because conserved residues and mutational sensitivity do not demonstrate metal occupancy [PMID:20359546; PMID:22922100].

The original COPII pull-down methods and Figure 7 identify p125/SEC23IP as the tested target, supporting correction of the two source-specific DDHD1 interaction rows [PMID:17428803]. The actual Results state: “p125 was also found to interact with GST-Sec24C as well as GST-Sec23A” ([original, Figure 7B Results](https://www.researchgate.net/publication/6399283_Mammalian_Sec16p250_Plays_a_Role_in_Membrane_Traffic_from_the_Endoplasmic_Reticulum)). HuRI's ZBTB24 partner has experimentally demonstrated sequence-specific DNA binding and transcriptional regulation, supporting a partner-class refinement; the CR1L interaction remains non-core [PMID:32296183; PMID:30085123].

Human FLAG-PA-PLA1 is cytosolic in the comparator experiment of the p125 localization paper [PMID:15623529]. Human DDHD1 also affects mitochondrial fragmentation in HeLa cells, with wild-type versus S537A rescue and two siRNAs; this context-dependent output is retained as non-core [PMID:24599962]. The SPG49/CYP2U1 fibroblast images in PMID:23176821 are not used as DDHD1 morphology experiments.

The [source guide](DDHD1-source-guide.md) records access, construct and inference limits. The normal Falcon deep-research command failed authentication; its fallback failed with HTTP401 insufficient quota. No provider report was produced. These notes and the source guide are manually authored from the documented sources and independent consultation.

Positive generic interactions follow the user's [project curation instructions](https://github.com/ai4curation/ai-gene-review/blob/1f2d0f4c42bde7e51deeed7d0486ef015657404b/projects/CLINGEN_MENDELIAN.md#curation-instructions). A supported partner-class refinement is preferred where available, and experimental source mismatches require actual assay evidence.

## 2026-10-17 — merged source reconciliation

Main `e32937e9a43d197137f795d76417027d318843f0` added the full-text PMID:23176821 cache with the CYP2U1 review. The new cache preserves the same article identity and the DDHD1/CYP2U1 distinctions documented above. It is protected in the publication plan; the initial abstract cache remains archived. Only access and provenance wording changed, with all annotation decisions and source fields preserved.
