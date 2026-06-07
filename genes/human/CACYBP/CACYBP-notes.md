# CACYBP (Calcyclin-Binding Protein / SIP / Siah-Interacting Protein) — research notes

UniProt: Q9HB71 (CYBP_HUMAN). Synonyms: S100A6BP, SIP, S100A6-binding protein, Siah-interacting protein.
HGNC. Aliases SIP = Siah-Interacting Protein.

## Core molecular/cellular function: adaptor/bridge in a Siah1-based E3 ubiquitin ligase complex
- CACYBP/SIP serves as a molecular bridge in ubiquitin E3 complexes, participating in calcium-dependent ubiquitination and proteasomal degradation of target proteins, notably beta-catenin (CTNNB1).
  [file:human/CACYBP/CACYBP-uniprot.txt "May be involved in calcium-dependent ubiquitination and subsequent proteasomal degradation of target proteins. Probably serves as a molecular bridge in ubiquitin E3 complexes. Participates in the ubiquitin-mediated degradation of beta-catenin (CTNNB1)."]
- Component of a large E3 complex composed of UBE2D1, SIAH1, CACYBP/SIP, SKP1, APC and TBL1X; interacts directly with SIAH1, SIAH2 and SKP1.
  [file:human/CACYBP/CACYBP-uniprot.txt "Component of some large E3 complex at least composed of UBE2D1, SIAH1, CACYBP/SIP, SKP1, APC and TBL1X. Interacts directly with SIAH1, SIAH2 and SKP1."]
- Siah1 is the central component of a multiprotein E3 ubiquitin ligase complex that targets beta-catenin for destruction in response to p53; the complex comprises Siah1, SIP, Skp1, and the F-box protein Ebi.
  [PMID:16085652 "Siah1 is the central component of a multiprotein E3 ubiquitin ligase complex that targets beta-catenin for destruction in response to p53 activation. The E3 complex comprises, in addition to Siah1, Siah-interacting protein (SIP), the adaptor protein Skp1, and the F-box protein Ebi."]
- Structural basis: SIP engages Siah1 by an N-terminal dimerization domain and a consensus PXAXVXP motif; its C-terminal domain binds Skp1 and protrudes to form the scaffold bringing substrate and E2 into apposition.
  [PMID:16085652 "An N-terminal dimerization domain of SIP sits across the saddle-shaped upper surface of Siah1... The C-terminal domain of SIP, which binds to Skp1, protrudes from the lower surface of Siah1, and we propose that this surface provides the scaffold for bringing substrate and the E2 enzyme into apposition in the functional complex."]
- Both the N-terminal dimerization element and the Siah-binding element are required for mediating beta-catenin destruction.
  [PMID:16085652 "SIP engages Siah1 by means of two elements, both of which are required for mediating beta-catenin destruction in cells."]

## S100/calcyclin binding (calcium-dependent)
- Homodimer; interacts with S100 family proteins S100A1, S100A6 (calcyclin), S100B, S100P, S100A12 in a calcium-dependent manner.
  [file:human/CACYBP/CACYBP-uniprot.txt "Homodimer. Interacts with proteins of the S100 family S100A1, S100A6, S100B, S100P and S100A12 in a calcium-dependent manner"]
- The name derives from binding to calcyclin (S100A6). High-throughput S100 interaction profiling (PMID:31837246) characterized S100 family PPIs quantitatively.

## Localization
- Nucleus and cytoplasm. Cytoplasmic at low calcium; upon retinoic acid induction and calcium increase in neuroblastoma cells, localizes to both nucleus and cytoplasm; nuclear fraction may be phosphorylated.
  [file:human/CACYBP/CACYBP-uniprot.txt "Cytoplasmic at low calcium concentrations. In neuroblastoma cells, after a retinoic acid (RA) induction and calcium increase, it localizes in both the nucleus and cytoplasm."]

## Homodimerization
- X-ray crystallography and structural studies show SIP/CACYBP forms a homodimer via its N-terminal dimerization domain. [PMID:16085652]

## High-throughput / contextual annotations (protein binding IPI)
- PMID:25036637 (chaperone-cochaperone interaction network LUMIER) — generic high-throughput PPI.
- PMID:31837246 (S100ome FP assay) — supports S100 protein binding specifically.
- PMID:31980649 (EGFR network rewiring in CRC, membrane Y2H) — generic interactome.
- PMID:33961781 (BioPlex dual proteome interactome) — generic high-throughput PPI.
- PMID:36115835 (fragmentomics PDZ affinity mapping) — generic interactome.
- These collapse to generic "protein binding" (GO:0005515) and are uninformative individually.

## Exosome
- PMID:20458337 (B-cell exosome proteome) — high-throughput MS localization; not a functional localization for a nucleocytoplasmic adaptor.

## Orthology-transferred developmental/process terms (GO_REF:0000107, Ensembl Compara)
- heart development, cardiac muscle cell differentiation, response to growth hormone, positive regulation of DNA replication, cellular response to calcium ion, nuclear envelope lumen, cell body, protein domain specific binding, tubulin binding. These are automatically transferred from orthologs and are not supported by direct human mechanistic evidence; mostly over-annotations relative to the core E3-adaptor role. Cellular response to calcium ion is consistent with the calcium-dependent S100 binding mechanism but remains a broad transferred term.

## Assessment summary (core vs non-core)
- CORE: SCF/Siah1 E3 ubiquitin ligase complex membership (part_of); molecular adaptor activity (bridge); ubiquitin protein ligase binding (Siah1/Siah2); S100 protein binding (calcium-dependent, basis of the protein's named function); protein homodimerization activity; beta-catenin destruction complex; nucleus/cytoplasm localization.
- NON-CORE / contextual: heart development, cardiac muscle cell differentiation, response to growth hormone, positive regulation of DNA replication (orthology-transferred phenotypes); cellular response to calcium ion (broad).
- OVER-ANNOTATED / uninformative: protein binding (GO:0005515) generic IPI x several; extracellular exosome; tubulin binding (InterPro IEA, no direct human evidence); protein domain specific binding; nuclear envelope lumen; cell body.

## Falcon deep research findings (2026-06-07)

Synthesis of the Falcon (Edison) report, distinguishing CONFIRMS / NEW / PROVISIONAL relative to the existing review. PMIDs resolved via PubMed.

- CONFIRMS (E3 adaptor / S100A6 / beta-catenin axis): Lee et al. 2008 NMR/ITC structure of the S100A6–SIP(189–219) complex confirms strictly Ca2+-dependent S100A6 binding to the C-terminal SGS region and frames SIP as a scaffold in an SCF-like (SCF-TBL1) E3 module linking Siah-1 (E2-recruiting) to Skp1–TBL1 (substrate-recruiting). Domain architecture: N-terminal helical-hairpin (M1–N78), central CS/p23-like (Y79–K177), C-terminal SGS (E178–F229) that folds upon S100A6 binding. [PMID:18803400 "the minimal S100A6 binding region in SIP was mapped to a 31-residue fragment (Ser189-Arg219)"; "a mode of binding to S100A6 that has not previously been observed"]. This complements the existing PMID:16085652 Siah1-assembly structure and our note that the complex is a non-cullin Siah1-based RING E3, not a canonical SCF.

- NEW (S100A6 antagonizes the anti-beta-catenin/growth-suppressive function in gastric cancer): Ning et al. 2012 — overexpressed CacyBP/SIP inhibits MKN45 gastric cancer proliferation/tumorigenesis (in vitro + xenograft); a mutant lacking the S100-binding domain (ΔS100) suppresses growth even more strongly, and S100 binding negatively regulates this via beta-catenin protein level and Tcf/LEF transcription; effect is proteasome-dependent (MG132-reversible). [PMID:22295074 "S100 proteins negatively regulate CacyBP/SIP-mediated inhibition of gastric cancer cell proliferation, through an effect on beta-catenin protein expression and transcriptional activation of Tcf/LEF"]. Adds a regulatory logic (S100A6 = negative regulator) and a domain map consistent with our adaptor model. Does not change existing annotation actions.

- NEW (SUMOylation at Lys16; cytoplasmic SUMO-conjugate): Wasik & Filipek 2013 — CacyBP/SIP binds the SUMO E2 Ubc9 and is SUMO1-modified; K16R abolishes modification; atypically, the SUMO-conjugated form is enriched in the cytoplasmic, not nuclear, fraction (in murine NB2a neuroblastoma cells). [PMID:24078263 "lysine 16 is the residue which undergoes sumoylation"; "sumoylated CacyBP/SIP is present in the cytoplasmic and not in the nuclear fraction"]. NEW PTM not previously in review; rodent cell system, so treat as a regulatory-mechanism lead, not a basis for a new human GO annotation.

- PROVISIONAL / review-sourced (ERK1/2 phosphatase + PTM regulation): Filipek & Leśniak 2018 review and Wasik & Filipek 2013 report CacyBP/SIP phosphatase activity toward ERK1/2 (lowering Elk-1 phosphorylation), with activity tuned by PKC phosphorylation at Ser22/Thr23 and CKII phosphorylation at Thr184, and Ca2+/S100A6 inhibiting Thr184 phosphorylation. This is a potentially distinct molecular function (protein phosphatase / MAPK phosphatase activity) beyond the E3-adaptor role, but the primary phosphatase papers were NOT retrievable in this run and it is largely review-summarized — flag as PROVISIONAL; do NOT add a phosphatase GO annotation without primary verification. Recorded as a suggested question/experiment.

- PROVISIONAL / review-sourced (stress, nucleolar NPM1 role, regulated translocation): Reviews state CacyBP/SIP relocalizes to perinuclear/nuclear compartments on Ca2+ increase, retinoic acid, or oxidative stress; protein levels rise ~40–50% under H2O2/radicicol; required to maintain NPM1 abundance and nucleolar integrity under oxidative stress (NB2a). Consistent with our accepted nuclear/cytoplasmic localization but adds a stress-response/nucleolar angle. PROVISIONAL (review-level, rodent system) — not used to alter annotations.

- NEW context, low weight for GO (pan-cancer biomarker): Mo et al. 2024 — integrative TCGA/GTEx analysis (18,787 samples) finds CACYBP dysregulated across cancers (up in 14, down in 6), prognostic in 13, AUC>0.8 in 15/21 (overall AUC 0.95), with TMB/MSI/immune-infiltration associations and Western-blot validation in 6 paired LUAD. [PMID:38322570]. Bioinformatic/translational biomarker evidence; does not establish a mechanistic GO function and is not used to add annotations.

Attribution: PMIDs for Lee 2008 (PMID:18803400), Ning 2012 (PMID:22295074), Wasik 2013 (PMID:24078263), Mo 2024 (PMID:38322570) verified via PubMed (DOIs 10.1021/bi801233z, 10.1371/journal.pone.0030185, 10.1007/s11064-013-1155-4, 10.62347/OWVW7440).
