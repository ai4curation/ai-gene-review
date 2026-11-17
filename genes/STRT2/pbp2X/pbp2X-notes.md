# pbp2X literature and annotation review

## 2026-11-06

Q5M2U8, official pbp2X/stu1701, 755 residues, LMG18311. PMID30692671 cloned M1–D755 with a C-terminal His6 tag and S343A catalytic mutant; the soluble G53–D755 construct lacked the transmembrane segment. Full-length constructs were expressed in E. coli C43(DE3), soluble protein in BL21. Direct LC-MS crosslinking used E. faecalis lipid II-derived polymer, not isolated native S. thermophilus lipid II.

Catalyzes serine-dependent D,D transpeptidation of peptidoglycan peptide stems. LC-MS detected a crosslinked dimer that disappeared with PBP2x catalytic inactivation. Activity also occurs with polymer produced by SgtB or transpeptidase-dead PBP1a and survives deletion of the PBP2x transmembrane segment; therefore crosslink catalysis is not an activity supplied only by an inseparable FtsW–PBP2x complex. The assay used E. faecalis substrate and does not fix the exact native S. thermophilus bridge chemistry.

Physical activation of FtsW requires the PBP2x transmembrane interface; peptide crosslinking does not require that interface once a suitable polymer is available. Native bridge specificity and physiological kinetic preference are not established by the heterologous-lipid II assay.

Primary sources: [PMID:30692671](https://pubmed.ncbi.nlm.nih.gov/30692671/).

The normal Falcon attempt failed with HTTP403 (authentication/access); no provider report was authored or substituted. The normal PAINT-loss command found no IRD or IKR loss on this target lineage. All original machine annotation payloads and raw sources are preserved against the parent-frozen additional-seed-state.json. No NEW annotation row is added. Specific proposed transpeptidase functions are separate from the immutable machine rows. No new process annotation is manufactured from necessity alone.

The ontology gap for serine D,D transpeptidation is recorded as a proposed molecular-function term, not as an unknown biological activity. The reviewed catalytic role is kept distinct from physical association with the polymerase.


## PR6123 round-1 follow-up (2026-11-06)

- NEW direct FtsW activation and separate core activity.
- claim-specific membrane topology evidence.
- explicit divisome complex membership with target/ortholog scope.
- retain true cell wall organization.
- standardized DD proposal definition and verified parent.

Historical annotation payloads, inherited NEW rows and raw/provider bytes were preserved against the published head 1678b44ceb3b7781cc4abcafbe54090c89f742bc. Claim-specific membrane support uses the frozen transmembrane prediction with its actual evidence code; a computational topology feature is not called an experimental localization. Full construct/strain mappings remain in the earlier notes and source analysis instead of being repeated on unrelated rows.

The direct enzyme-activator evidence in PMID:30692671 applies to the assayed StPBP2x and SaPBP1 constructs, including catalytic-serine mutants. GO:0008047 is current and requires direct interaction without covalent modification. No corresponding role is inferred for Bacillus PBP3 from catalytic compensation, and an essential physical PBP2B requirement alone does not identify direct activation chemistry. A divisome complex annotation describes septal pair membership, not a purified complete native assembly; PBP3 conditional backup is left outside that assertion.

All five D,D proposals now share one reaction definition and the QuickGO-verified GO:0016755 parent. The definition retains organism-dependent acceptors and does not turn an inferred PBP3 linkage into a product-resolved assay. QuickGO searches and responses are preserved in the ignored round-1 audit cache.
