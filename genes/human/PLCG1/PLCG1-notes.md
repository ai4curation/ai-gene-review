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

## Deep research integration (falcon)

Session 2026-10-01. Report: `PLCG1-deep-research-falcon.md` (Edison/falcon; 28 citation tags, but only 6 distinct sources: Hajicek 2019 eLife, Chen & Simons 2021 Sci Signal review, Kanemaru & Nakamura 2023 Biomolecules review, Zeng 2020 bioRxiv preprint, and two unpublished theses, Duarte 2023 and Nanna 2026). No PMIDs given; DOIs resolved through PubMed.

### Claim classification (about 30 substantive claims)
- **Confirms review (~18):** PIP2 -> IP3 + DAG catalysis, Ca2+-dependence; IP3 -> ER Ca2+ release, DAG -> PKC; cytosolic/autoinhibited at rest; Y783 phosphorylation relieves autoinhibition (plus Y771, Y775, Y1253); RTK recruitment via SH2 (EGFR pY992, PDGFR pY1021, FGFR1 pY766); TCR/LAT/ITK coupling; Ca2+/calcineurin/NFAT and DAG/PKC/RasGRP/ERK arms; plasma membrane translocation; ruffles/lamellipodia/migration; SH3 binding proline-rich partners (SOS, dynamin-1, SLP-76); dynamin-1 GEF activity; Rac1 activation via SH3; EGF-induced migration; angiogenesis and T cell phenotypes as downstream (non-core) outcomes; gain-of-function cancer mutations.
- **Adds something new (5):** (1) structural detail of autoinhibition (regulatory array over the catalytic core; cSH2-C2 clasp displaced by pY783); (2) VEGFR2 (KDR) pY1175 docking and the PLCG1-PKC-ERK route in endothelial cells; (3) LAT condensate/phase-separation scaffolding and CD45 protection; (4) focal adhesion localization with GIT1/beta-PIX/FAK; (5) nuclear ~120 kDa PLCG1 fragment.
- **Conflicts with review (1):** SH3 domain binds AKT (review REMOVEd the AKT1 protein-binding row, reading PMID:16525023 as AKT binding and phosphorylating PLCG1).
- **Not relevant or unsupported (~6):** domain boundary table; cell-cycle regulator induction (Cdk4, cyclin D1, p27 export); erythropoiesis; PKC feedback on EGFR T654; DLL4/Notch tip/stalk selection; JAK2/GRB2/FAK SH2 partners. These come from reviews/theses or describe downstream pleiotropy.

### Claims adopted (and where)
- Autoinhibition mechanism -> `description`; `core_functions[0].supported_by` with two verbatim quotes from PMID:31889510 (Hajicek 2019, full text cached via `just fetch-pmid`).
- VEGFR2 -> `description`; NEW `existing_annotations` row GO:0048010 vascular endothelial growth factor receptor signaling pathway (IDA, PMID:11387210, Takahashi 2001 EMBO J, full text cached); GO:0048010 added to `core_functions[0].directly_involved_in`; KDR added to the SH2 core function with PMID:11387210 support. NEW bar: PLCG1 performs the PIP2 hydrolysis step (catalytic effector, not substrate). Comparator check (QuickGO): PRKCB, PRKD1, PRKD2, PTK2, SRC, FYN, VAV1 carry GO:0048010 in human, so effectors do get the term. The review already listed VEGFR2 as a core receptor context (PDGFR NEW row reason, core function text) without a term. Caveat noted: the experiments used human KDR in mouse/bovine endothelial cells and a pan-PLC-gamma antibody.
- LAT condensate scaffolding -> `description`; `core_functions[1].supported_by` (PMID:33929486, the peer-reviewed J Cell Biol 2021 version of the preprint the report cites; plus a verbatim quote from the report). No new MF annotation; raised as a question instead.
- References added: the falcon report (reference_review LOW_QUALITY: secondary, theses, no PMIDs), PMID:11387210, PMID:31889510, PMID:33929486.

### Claims not acted on (and why)
- Focal adhesion and nuclear fragment localizations: only supported by reviews (Chen & Simons; Kanemaru & Nakamura) in the report; no primary paper checked. Raised as a question; no NEW CC terms.
- SH3-AKT binding: from a thesis (Duarte 2023) only; conflicts with the review's reading of PMID:16525023. Raised as a question; AKT1 row left as is.
- Erythropoiesis, cell-cycle regulators, Notch tip/stalk, PKC-EGFR feedback: downstream or pleiotropic, review-sourced only.

### UNDECIDED rows
- The report does not mention COP9 signalosome (GO:0008180), lysophospholipase C (GO:0140324) or endothelial apoptosis, so it offers no primary leads for them. COP9 and lysophospholipase C stay UNDECIDED (the Tespa1 paper PMID:22561606 and the rat donor evidence are still not available as full text).
- GO:2000353 positive regulation of endothelial cell apoptotic process (PMID:27464494): changed UNDECIDED -> KEEP_AS_NON_CORE. This was not prompted by the report: the earlier reason said the direction could not be read from the abstract, but the paper's title ("MiR-30s Family Inhibit the Proliferation and Apoptosis ... Through Targeting ... PLCG1") states it, which matches the curator's positive-regulation term. Now handled the same way as the sibling proliferation row from the same paper.

### Report errors / weaknesses detected
- The domain table is labelled "human PLCgamma1", but the structural source (Hajicek 2019) solved **rat** PLC-gamma1 (P10686). The report never says the structure is human, but it presents the structural data as human.
- Hajicek 2019 is listed under "Recent Developments (2023-2024 Sources)".
- Zeng et al. is cited as a 2020 bioRxiv preprint; it was published as J Cell Biol 2021 (PMID:33929486). Minor detail: the paper says nSH2 binds LAT Y132; the report's "Tyr132 and Tyr171" cross-linking was not checked.
- Two of the six sources are unpublished theses ("Unknown journal"); no PMIDs anywhere. No hallucinated PMIDs (none given); all four DOIs resolved to real papers.

### Validation
- `just validate human PLCG1`: valid, all validations passed.
