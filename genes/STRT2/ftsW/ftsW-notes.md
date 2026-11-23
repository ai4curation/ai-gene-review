# ftsW literature and annotation review

## 2026-11-06

Q5M5I9, ftsW/stu0486, current 431 residues, LMG18311. PMID30692671 calls the construct M1–R426. Supplementary Table 5 primers oAT01/oAT02 align to CP000023.1 CDS 465656..466951 at relative nucleotides 15..1296, encoding current residues 6–431. Paper D292A/L345G map to current D297A/L350G. Current UniProt sequence version 1 dates from 2005; this is a five-residue construct omission, not evidence of a later database extension or proven native start-site error.

Polymerizes lipid-II-derived glycan chains after activation by a compatible PBP2x transmembrane interface. Direct assay used LMG18311 FtsW current residues 6–431 with affinity tags in E. coli expression; the FtsW active-site mutation abolished polymerization while PBP2x catalytic inactivation did not. The St reaction used E. faecalis lipid II, so it does not alone identify the exact native S. thermophilus acceptor bridge.

Direct biochemical evidence is on the shortened 426-residue construct. Native full-length kinetics and physiological flipping are not established by that assay. The positive polymerase result does not exclude every possible secondary flippase activity.

Primary sources: [PMID:30692671](https://pubmed.ncbi.nlm.nih.gov/30692671/).

The normal Falcon attempt failed with HTTP403 (authentication/access); no provider report was authored or substituted. The normal PAINT-loss command found no IRD or IKR loss on this target lineage. All original machine annotation payloads and raw sources are preserved against the parent-frozen additional-seed-state.json. One NEW IDA GO:0009252 row is added for the direct purified-construct polymerization result. Specific proposed transpeptidase functions are separate from the immutable machine rows. No new process annotation is manufactured from necessity alone.

The flippase claims remain unresolved and are excluded from the core polymerase function.

The process proposal was checked against same-role FtsW comparators P0ABG4 and O07639 using QuickGO (2026-11-06): both carry GO:0009252. This is a convention check, not evidence for the target. The term parents describe chemical biosynthesis and are not redundant with target cell-shape/division terms. No target entry was found in gocams/index.tsv.


## PR6123 round-1 follow-up (2026-11-06)

- claim-specific membrane topology evidence.
- explicit divisome complex membership with target/ortholog scope.

Historical annotation payloads, inherited NEW rows and raw/provider bytes were preserved against the published head 1678b44ceb3b7781cc4abcafbe54090c89f742bc. Claim-specific membrane support uses the frozen transmembrane prediction with its actual evidence code; a computational topology feature is not called an experimental localization. Full construct/strain mappings remain in the earlier notes and source analysis instead of being repeated on unrelated rows.

The direct enzyme-activator evidence in PMID:30692671 applies to the assayed StPBP2x and SaPBP1 constructs, including catalytic-serine mutants. GO:0008047 is current and requires direct interaction without covalent modification. No corresponding role is inferred for Bacillus PBP3 from catalytic compensation, and an essential physical PBP2B requirement alone does not identify direct activation chemistry. A divisome complex annotation describes septal pair membership, not a purified complete native assembly; PBP3 conditional backup is left outside that assertion.

All five D,D proposals now share one reaction definition and the QuickGO-verified GO:0016755 parent. The definition retains organism-dependent acceptors and does not turn an inferred PBP3 linkage into a product-resolved assay. QuickGO searches and responses are preserved in the ignored round-1 audit cache.
