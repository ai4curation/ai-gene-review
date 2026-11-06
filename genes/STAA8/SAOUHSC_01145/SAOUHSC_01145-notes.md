# SAOUHSC_01145 literature and annotation review

## 2026-11-06

Q2FZ94, official locus SAOUHSC_01145 without a UniProt primary gene symbol, 744 residues, NCTC8325. PMID30692671 amplified A2–D744 from NCTC8325 genomic DNA, expressed C-terminal His6 protein in E. coli C43(DE3), and tested S314A as the inactive PBP1 partner. PMID35703435 principally tests SH1000 and derived MRSA backgrounds; those phenotypes are homolog/strain-transfer evidence, not NCTC8325 measurements. PMID38527711 structures39–608 map to Q2FZ94 in frozen UniProt but the cached text is abstract-only.

Catalyzes class-B-PBP D,D peptide crosslinking in S. aureus peptidoglycan, whose acceptor includes the lysine-associated pentaglycine bridge, and physically activates FtsW. NCTC8325 constructs directly establish activation even with PBP1 S314A; the physiological contribution of the catalytic site is independently supported by SH1000/MRSA comparisons and transferred explicitly to this reference protein, not inferred solely from activation or antibiotic binding.

The 2019 polymerase experiment used catalytically disabled PBP1 and is not a direct PBP1 crosslink-product assay. 2022 catalytic essentiality depends on MSSA/MRSA background. Soluble-domain antibiotic acylation and crystal structures alone do not prove net physiological crosslinking.

Primary sources: [PMID:30692671](https://pubmed.ncbi.nlm.nih.gov/30692671/), [PMID:35703435](https://pubmed.ncbi.nlm.nih.gov/35703435/), [PMID:38527711](https://pubmed.ncbi.nlm.nih.gov/38527711/).

The normal Falcon attempt failed with HTTP403 (authentication/access); no provider report was authored or substituted. The normal PAINT-loss command found no IRD or IKR loss on this target lineage. All original machine annotation payloads and raw sources are preserved against the parent-frozen additional-seed-state.json. No NEW annotation row is added. Specific proposed transpeptidase functions are separate from the immutable machine rows. No new process annotation is manufactured from necessity alone.

The ontology gap for serine D,D transpeptidation is recorded as a proposed molecular-function term, not as an unknown biological activity. The reviewed catalytic role is kept distinct from physical association with the polymerase.


## PR6123 round-1 follow-up (2026-11-06)

- NEW direct FtsW activation and separate core activity.
- claim-specific membrane topology evidence.
- explicit divisome complex membership with target/ortholog scope.
- replace accession-as-symbol with verified locus tag.
- retain true cell wall organization.
- standardized DD proposal definition and verified parent.

Historical annotation payloads, inherited NEW rows and raw/provider bytes were preserved against the published head 1678b44ceb3b7781cc4abcafbe54090c89f742bc. Claim-specific membrane support uses the frozen transmembrane prediction with its actual evidence code; a computational topology feature is not called an experimental localization. Full construct/strain mappings remain in the earlier notes and source analysis instead of being repeated on unrelated rows.

The direct enzyme-activator evidence in PMID:30692671 applies to the assayed StPBP2x and SaPBP1 constructs, including catalytic-serine mutants. GO:0008047 is current and requires direct interaction without covalent modification. No corresponding role is inferred for Bacillus PBP3 from catalytic compensation, and an essential physical PBP2B requirement alone does not identify direct activation chemistry. A divisome complex annotation describes septal pair membership, not a purified complete native assembly; PBP3 conditional backup is left outside that assertion.

All five D,D proposals now share one reaction definition and the QuickGO-verified GO:0016755 parent. The definition retains organism-dependent acceptors and does not turn an inferred PBP3 linkage into a product-resolved assay. QuickGO searches and responses are preserved in the ignored round-1 audit cache.
