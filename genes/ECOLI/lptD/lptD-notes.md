# lptD (P31554) notes

Review session 2026-10-24. No provider deep research was run (no `*-deep-research-*.md`); the review relies on the cached publications and the UniProt entry.

## Sources used
- UniProt P31554 (`lptD-uniprot.txt`): function, subunit, outer-membrane location, disulfides Cys31-Cys724 and Cys173-Cys725, LptE/LptA interactions.
- Name history: imp, "increased membrane permeability" [PMID:2547691 "We have designated this locus imp for increased membrane permeability."]; ostA, organic solvent (n-hexane) tolerance [PMID:7811102; PMID:12724388]. Solvent tolerance is treated as an indirect outer-membrane barrier phenotype, not a separate function.
- Essential outer-membrane complex [PMID:12207697 "Imp is essential and forms a high-molecular-weight disulphide-bonded complex in the outer membrane."]
- LptDE complex and LPS surface assembly [PMID:16861298 "These data clearly show that in the absence of Imp or RlpB de novo synthesized LPS does not reach the outer leaflet of the OM."]
- Plug-and-barrel [PMID:21257904]; LptE needed for BAM assembly of LptD [PMID:21257909]; LptA docking at the N-terminal jellyroll [PMID:22668317].
- Structures: Dong et al. 2014 [PMID:24990744] and Qiao et al. 2014 (Shigella flexneri) [PMID:24990751], both fetched for this review. 26-stranded barrel; lateral beta1-beta26 gate.
- Reconstitution of the seven-protein bridge [PMID:29449493]; review [PMID:26370939]; assembly factors BepA [PMID:34463613] and LptM [PMID:37821449].

## Decisions
- All 8 bare protein-binding IPI rows: REMOVE (policy; the interactions are real).
- outer membrane: MODIFY to cell outer membrane. membrane organization: MODIFY to GO:0043165. The PSEPK orthologue used MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE; changed to follow the CLAUDE.md "general term -> MODIFY" rule.
- GO:1990351: the IBA row (LptDE translocon) is ACCEPTed; the IDA row from PMID:29449493 is MODIFIED to GO:0062051, matching lptB. The validator warns that the same term has different actions; this is a deliberate per-row decision.
- MF: NEW contributes_to GO:0015221. GO:0140332 was rejected because its definition describes aqueous-phase carriage, i.e. the LptA/LptC bridge.
