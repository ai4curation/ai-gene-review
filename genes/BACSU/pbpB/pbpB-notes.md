# pbpB literature and annotation review

## 2026-11-06

Q07868, pbpB/BSU15160, current 713 residues, strain 168. PMID28792086 amplified pbpB from 168 and tested native 168/168CA derivatives plus E. coli membrane expression. The paper discusses a historical translation start offset; current sequence version 3 already has the assayed serine at 309, so no additional +3 offset is applied. PMID38480901 is PY79-derived HaloTag-PBP2B imaging and is explicitly comparative.

Catalyzes serine-dependent D,D peptide crosslinking in septal peptidoglycan and supplies a separable essential physical role in the divisome. Native Bacillus uses mDAP-containing peptidoglycan; the strain 168 S309A/PBP3 experiments establish catalytic compensation, not a product-resolved assay of every linkage or a dispensable PBP2B protein.

PBP3 catalytic rescue applies to the tested strain 168 backgrounds and conditions. It does not establish replacement of the physical PBP2B component. The structural association with FtsW must not be represented as PBP2B independently catalyzing glycan polymerization.

Primary sources: [PMID:28792086](https://pubmed.ncbi.nlm.nih.gov/28792086/), [PMID:38480901](https://pubmed.ncbi.nlm.nih.gov/38480901/), [PMID:30692671](https://pubmed.ncbi.nlm.nih.gov/30692671/).

The normal Falcon attempt failed with HTTP403 (authentication/access); no provider report was authored or substituted. The normal PAINT-loss command found no IRD or IKR loss on this target lineage. All original machine annotation payloads and raw sources are preserved against the parent-frozen additional-seed-state.json. No NEW annotation row is added. Specific proposed transpeptidase functions are separate from the immutable machine rows. No new process annotation is manufactured from necessity alone.

The ontology gap for serine D,D transpeptidation is recorded as a proposed molecular-function term, not as an unknown biological activity. The reviewed catalytic role is kept distinct from physical association with the polymerase.

PMID10383963 supplies native strain168 muropeptide chemistry; it is not a direct assay of this individual PBP. Generic protein-binding removals preserve the reported interactions as context.


## PR6123 round-1 follow-up (2026-11-06)

- activation boundary documented without unsupported MF.
- claim-specific membrane topology evidence.
- explicit divisome complex membership with target/ortholog scope.
- retain true cell wall organization.
- standardized DD proposal definition and verified parent.

Historical annotation payloads, inherited NEW rows and raw/provider bytes were preserved against the published head 1678b44ceb3b7781cc4abcafbe54090c89f742bc. Claim-specific membrane support uses the frozen transmembrane prediction with its actual evidence code; a computational topology feature is not called an experimental localization. Full construct/strain mappings remain in the earlier notes and source analysis instead of being repeated on unrelated rows.

The direct enzyme-activator evidence in PMID:30692671 applies to the assayed StPBP2x and SaPBP1 constructs, including catalytic-serine mutants. GO:0008047 is current and requires direct interaction without covalent modification. No corresponding role is inferred for Bacillus PBP3 from catalytic compensation, and an essential physical PBP2B requirement alone does not identify direct activation chemistry. A divisome complex annotation describes septal pair membership, not a purified complete native assembly; PBP3 conditional backup is left outside that assertion.

All five D,D proposals now share one reaction definition and the QuickGO-verified GO:0016755 parent. The definition retains organism-dependent acceptors and does not turn an inferred PBP3 linkage into a product-resolved assay. QuickGO searches and responses are preserved in the ignored round-1 audit cache.
