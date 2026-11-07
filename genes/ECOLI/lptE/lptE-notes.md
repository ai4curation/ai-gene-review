# lptE (P0ADC1) notes

Review session 2026-10-24. No provider deep research was run (no `*-deep-research-*.md`); the review relies on the cached publications and the UniProt entry.

## Sources used
- UniProt P0ADC1 (`lptE-uniprot.txt`): lipid-anchored outer-membrane lipoprotein; binds LPS; required for LptD assembly.
- Discovery as RlpB partner of Imp/LptD [PMID:16861298 "Because RlpB does not function simply to stabilize or target Imp, we conclude that both of these proteins function together in what is likely to be the last step in LPS assembly, localization to the outer leaflet of the OM."]
- 1:1 complex, LPS binding [PMID:20203010 "We also demonstrate that LptE binds LPS specifically and may serve as a substrate recognition site at the OM."]
- Direct LPS binding and disaggregation, crystal structure [PMID:24938785 "Our results establish that LptE binds LPS specifically and that this is crucial to LptE’s function in vivo."]
- Plug inside the LptD barrel [PMID:21257904]; required for BAM-dependent LptD assembly [PMID:21257909, fetched]; disulfide-rearrangement checkpoint [PMID:26370939]; LptM [PMID:37821449]; reconstitution [PMID:29449493].

## Decisions
- LPS binding (IBA and IDA): ACCEPT. Core MF, plus NEW contributes_to GO:0015221 (the activity belongs to the LptDE complex).
- 5 bare protein-binding rows: REMOVE.
- outer membrane: MODIFY to cell outer membrane.
- GO:1990351: IBA and IDA (PMID:29449493) rows both MODIFIED to GO:0062051, same handling as lptD and lptB; core in_complex is GO:0062051. No validator warning remains.


## 2026-11-07 — cross-taxon Lpt audit, E. coli member consultation

All original annotation rows, reference findings and core roles were reassessed. Source payloads/order, qualifiers and historical NEW lifecycle remain unchanged. Targeted full-primary reading supports the existing division between LptB ATPase, membrane extractor subunit contributions, bridge transfer and terminal LptDE translocation. Abstract-only source details are not treated as disproven or silently relabeled as newly inspected full-text evidence. Generic location/assembly quotations were strengthened where appropriate; no new annotation was added. PMID42844470 updates whole-bridge regulation: E. coli proteins and an engineered LptC-LptA fusion support the structural analysis, with E. coli functional controls; LPS-null A. baylyi is an expression host, not a new organismal activity assay. The normal cache remains abstract-only; independently acquired publisher full text is documented in the shared literature consultation. PMID41285762 adds E. coli LptDEMY structural/functional context without making LptM/Y universally essential. The normal PAINT-loss check reports no IRD/IKR loss on this target lineage; this is not a whole-family uniformity claim. Default Falcon research was attempted normally and failed HTTP403 authentication; no provider report was created or overwritten. Manual source/ontology/preservation evidence is in analysis/module_audits/bacterial_lps_transport/ecoli-consultation/.
