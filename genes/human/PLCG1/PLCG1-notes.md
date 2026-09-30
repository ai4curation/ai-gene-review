# PLCG1 review notes

## Session 2026-09-30 (ADAPTIVE_IMMUNITY, TCR trunk)

### Setup
- `just fetch-gene-pmids human PLCG1`: 57/57 publications cached (many abstract-only).
- `just deep-research-falcon human PLCG1 --fallback perplexity-lite` launched in parallel. Status recorded at end of this entry.

### Biology summary (with provenance)
- Core catalytic activity: PIP2 -> IP3 + DAG. [PMID:37422272 "hydrolyzes phosphatidylinositol 4,5-bisphosphate (PIP2) to produce critical second messengers, including diacylglycerol (DAG) and inositol-1,4,5-trisphosphate (IP3)"]
- Human germline S1021F gain-of-function variant increases IP3 and Ca2+ release and causes immune dysregulation. [PMID:37422272 "We demonstrated that the S1021F variant is a gain-of-function variant, leading to increased inositol-1,4,5-trisphosphate production, intracellular Ca2+ release"]
- RTK recruitment via SH2 domains: FGFR1 pY766 [PMID:1656221], PDGFRB pY1009/pY1021 [PMID:1396585], EGFR pY992/pY1068 [PMID:7993895]; SH2-dependent translocation to plasma membrane and ruffles [PMID:11331309 "The translocation of PLC gamma to the plasma membrane required the functional Src homology 2 domains"].
- Autoinhibition release by nSH2/cSH2 coordination and Y783 phosphorylation in FGFR signalling [PMID:23063561 "In the context of fibroblast growth-factor receptor signaling, the coordinated involvement of nSH2 and cSH2 domains mediates efficient phosphorylation of PLCγ1"].
- TCR: PLCG1 binds phospho-LAT by SH2 [PMID:10811803 "Grb2, Gads, and phospholipase C (PLC)-gamma1 bind LAT via Src homology-2 domains"]; ITK phosphorylates and activates it [PMID:28598420 "The subsequent recruitment of interleukin-2-induced tyrosine kinase (Itk) triggers the tyrosine phosphorylation and activation of PLC-γ1"]. SLP-76 Y173 is needed for PLCG1 phosphorylation in T and mast cells [PMID:21725281].
- EGF-induced Ca2+ rise requires PLCG1 [PMID:22454520 "Downregulation of PLCγ1 also inhibited the EGF-mediated calcium increase in PC3"].
- SH3 domain: binds proline-rich partners (TNK1, SLP-76, Sam68, WASP); reported Rac1 GEF activity in vitro [PMID:19264842 "PLC-gamma1 SH3 domain is actually a potent and specific Rac1 guanine nucleotide exchange factor in vitro"]. Treated as non-core.
- Lipase-independent mitogenic role in SCC cells [PMID:20510673].

### Framing decision
PLCG1 is broadly expressed and pleiotropic. TCR signalling is one of several core receptor contexts, alongside EGFR, FGFR and PDGFR (and VEGFR2 per Reactome). Core functions were written to reflect this rather than an adaptive-immunity-only view.

### Annotation decisions
- `protein binding` (72 IPI rows): MODIFY -> GO:0001784 phosphotyrosine residue binding where the evidence is SH2/pTyr recruitment (RTKs, LAT, BLNK, CD22, SYK, villin, EAT-2, CAV1 pY14, phosphopeptide arrays); MODIFY -> GO:0070064 proline-rich region binding for SH3 interactions (TNK1, SLP-76, Sam68, WASP, SH3 peptide array PMID:17474147); MODIFY -> GO:0031267 small GTPase binding for RAC1; REMOVE for co-IP/AP-MS/PLA/BioID-only hits, AKT1 (PLCG1 is the substrate), INSR (binding mechanism unresolved: SH2 vs PH-EF), SR-BII (not physiological), EEF1A2, THEMIS, GRB2, SOS1, Tespa1, FGFR2 (SH3 binding to C terminus; site nature not stated).
- C-type glycerophospholipase activity -> MODIFY to GO:0004435, matching PLCG2 review.
- COP9 signalosome IDA (PMID:22561606, abstract only): the abstract describes the TCR signalosome, not CSN. UNDECIDED (cannot see full text; do not overrule).
- Lysophospholipase C (ISS from rat): UNDECIDED; no human evidence found.
- miR-30 paper (PMID:27464494, abstract only): EC proliferation KEEP_AS_NON_CORE; EC apoptosis UNDECIDED.
- Downstream phenotypes (migration, angiogenesis, EC migration, IL10/inflammatory response): KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED (Reactome FCGR3A-IL10 row), per necessity-vs-participation guidance.
- NEW: GO:0008543 FGFR signaling pathway (PMID:23063561) and GO:0048008 PDGFR signaling pathway (PMID:1396585). Participation test: PLCG1 is the catalytic effector that performs PIP2 hydrolysis within these pathways; comparable to its existing EGFR signaling annotation.

### Validation
- `just validate human PLCG1`: valid, no errors or warnings.

### Deep research status
- The falcon deep-research job (`just deep-research-falcon human PLCG1 --fallback perplexity-lite`) was still running after about 35 minutes, when this review was completed. The perplexity-lite fallback is not available here: sibling runs logged "Provider 'perplexity' not available". This review therefore relies on the cached publications and UniProt, not deep research. If `PLCG1-deep-research-falcon.md` appears later, check it against the core functions above.
- Update: the falcon run finished at 13:59 UTC, after the review, and wrote `PLCG1-deep-research-falcon.md`. A quick scan agrees with the review: it describes PIP2 hydrolysis downstream of EGFR (pTyr992), FGFR, PDGFR and the TCR; the SH3 domain binding proline-rich partners; the dynamin-1 GEF activity as secondary; and a nuclear PLCG1 fragment. It says nothing about COP9 signalosome or lysophospholipase C, so those rows stay UNDECIDED.
