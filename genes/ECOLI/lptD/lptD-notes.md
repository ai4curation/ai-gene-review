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
- outer membrane: MODIFY to cell outer membrane. membrane organization: MODIFY to GO:0043165. Both follow the CLAUDE.md "general term -> MODIFY" rule; the P. putida LptD review makes the same two refinements.
- GO:1990351: both the IBA row (PTN001249597) and the IDA row from PMID:29449493 are MODIFIED to GO:0062051, matching lptB and lptE; core in_complex is GO:0062051. (An earlier draft ACCEPTed the IBA row; that split, and its validator warning, are gone.)
- MF: NEW contributes_to GO:0015221. GO:0140332 was rejected because its definition describes aqueous-phase carriage, i.e. the LptA/LptC bridge.


## 2026-11-07 — cross-taxon Lpt audit, E. coli member consultation

All original annotation rows, reference findings and core roles were reassessed. Source payloads/order, qualifiers and historical NEW lifecycle remain unchanged. Targeted full-primary reading supports the existing division between LptB ATPase, membrane extractor subunit contributions, bridge transfer and terminal LptDE translocation. Abstract-only source details are not treated as disproven or silently relabeled as newly inspected full-text evidence. Generic location/assembly quotations were strengthened where appropriate; no new annotation was added. PMID42844470 updates whole-bridge regulation: E. coli proteins and an engineered LptC-LptA fusion support the structural analysis, with E. coli functional controls; LPS-null A. baylyi is an expression host, not a new organismal activity assay. The normal cache remains abstract-only; independently acquired publisher full text is documented in the shared literature consultation. PMID41285762 adds E. coli LptDEMY structural/functional context without making LptM/Y universally essential. The normal PAINT-loss check reports no IRD/IKR loss on this target lineage; this is not a whole-family uniformity claim. Default Falcon research was attempted normally and failed HTTP403 authentication; no provider report was created or overwritten. Manual source/ontology/preservation evidence is in analysis/module_audits/bacterial_lps_transport/ecoli-consultation/.
