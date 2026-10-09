# SMXL6 (At1g07200, UniProt Q9LML2) curation notes

Context: `strigolactone_signaling_shoot_branching` module. Falcon deep research failed (all
providers); notes from cached publications.

## Function
- SMXL6/7/8 are co-orthologs of rice D53 and promote shoot branching [PMID:26546447 "SMXL6, SMXL7, and SMXL8 are co-orthologs of rice D53 that promote shoot branching"].
- SL induces D14/MAX2-dependent ubiquitination and degradation [PMID:26546446 "Exogenous application of the SL analog rac-GR24 causes ubiquitination and degradation of SMXL6, 7, and 8; this requires D14 and MAX2."].
- EAR-motif/TPR2-dependent transcriptional repression; BRC1 repressed [PMID:26546446 "D53-like SMXLs exhibit TPR2-dependent transcriptional repression activity and repress the expression of BRANCHED1."].
- Nuclear [PMID:26546446 "the GFP-SMXL6, GFP-SMXL7, and GFP-SMXL8 proteins colocalized with SV40NLS-mCherry"].
- SMXL6 binds DNA directly at SMXL6/7/8 promoters [PMID:32528176, abstract only].
- SMXL7 functions in the nucleus; EAR partly dispensable [PMID:27317673].
- Drought: smxl6,7,8 triple more drought resistant [PMID:32295207]; DWA1 interaction and SnRK2.3 promoter binding [PMID:37759806].

## Curation decisions
- protein folding chaperone (IBA from deep Clp node, P9WPC9) and derived protein folding (IEA): REMOVE (functional divergence of SMXL clade).
- ATP binding / ATP hydrolysis (InterPro): MARK_AS_OVER_ANNOTATED (not demonstrated).
- protein binding (D14, DWA1): REMOVE as uninformative (interactions themselves real).
- Cytoplasm (AtSubP): over-annotated; chloroplast (SMXL6 AtSubP): REMOVE.
- NEW: GO:0003714 transcription corepressor activity (IDA), GO:2000032 regulation of secondary shoot formation (IMP), GO:1902348 cellular response to strigolactone (IDA); GO:0000976 transcription cis-regulatory region binding (IDA, PMID:32528176).
