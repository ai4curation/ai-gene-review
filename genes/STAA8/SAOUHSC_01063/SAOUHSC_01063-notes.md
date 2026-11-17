# SAOUHSC_01063 literature and annotation review

## 2026-11-06

Q2G2C2, official locus SAOUHSC_01063 without a UniProt primary gene symbol, 408 residues, NCTC8325. PMID30692671 explicitly amplified K2–N408 from NCTC8325 genomic DNA; N-terminal His or His-SUMO-FLAG constructs were expressed in E. coli C43(DE3), including D287A. Native overexpression experiments were RN4220; PMID38480900 imaging used other S. aureus backgrounds, not this strain.

Polymerizes lipid-II-derived glycan strands as the catalytic FtsW unit of a complex with PBP1. NCTC8325-derived residues 2–408 were assayed with purified PBP1 and S. aureus lipid II; PBP1 active-site inactivation does not remove its activation of FtsW. The deleted initiator methionine and fusion tags are construct boundaries, not a demonstrated native gene-model error.

The purified construct establishes polymerase activity. Native RN4220 overexpression and JE2/COL imaging are separate strain evidence. No target-specific physiological lipid-II transport contribution is established.

Primary sources: [PMID:30692671](https://pubmed.ncbi.nlm.nih.gov/30692671/), [PMID:38480900](https://pubmed.ncbi.nlm.nih.gov/38480900/).

The normal Falcon attempt failed with HTTP403 (authentication/access); no provider report was authored or substituted. The normal PAINT-loss command found no IRD or IKR loss on this target lineage. All original machine annotation payloads and raw sources are preserved against the parent-frozen additional-seed-state.json. One NEW IDA GO:0009252 row is added for the direct purified-construct polymerization result. Specific proposed transpeptidase functions are separate from the immutable machine rows. No new process annotation is manufactured from necessity alone.

The flippase claims remain unresolved and are excluded from the core polymerase function.

The process proposal was checked against same-role FtsW comparators P0ABG4 and O07639 using QuickGO (2026-11-06): both carry GO:0009252. This is a convention check, not evidence for the target. The term parents describe chemical biosynthesis and are not redundant with target cell-shape/division terms. No target entry was found in gocams/index.tsv.


## PR6123 round-1 follow-up (2026-11-06)

- claim-specific membrane topology evidence.
- explicit divisome complex membership with target/ortholog scope.
- replace accession-as-symbol with verified locus tag.

Historical annotation payloads, inherited NEW rows and raw/provider bytes were preserved against the published head 1678b44ceb3b7781cc4abcafbe54090c89f742bc. Claim-specific membrane support uses the frozen transmembrane prediction with its actual evidence code; a computational topology feature is not called an experimental localization. Full construct/strain mappings remain in the earlier notes and source analysis instead of being repeated on unrelated rows.

The direct enzyme-activator evidence in PMID:30692671 applies to the assayed StPBP2x and SaPBP1 constructs, including catalytic-serine mutants. GO:0008047 is current and requires direct interaction without covalent modification. No corresponding role is inferred for Bacillus PBP3 from catalytic compensation, and an essential physical PBP2B requirement alone does not identify direct activation chemistry. A divisome complex annotation describes septal pair membership, not a purified complete native assembly; PBP3 conditional backup is left outside that assertion.

All five D,D proposals now share one reaction definition and the QuickGO-verified GO:0016755 parent. The definition retains organism-dependent acceptors and does not turn an inferred PBP3 linkage into a product-resolved assay. QuickGO searches and responses are preserved in the ignored round-1 audit cache.
