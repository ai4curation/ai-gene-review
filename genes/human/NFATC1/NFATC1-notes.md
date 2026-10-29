# NFATC1 (human, O95644) review notes

Context: ADAPTIVE_IMMUNITY project, T cell receptor trunk (after LCK, ZAP70, LAT, LCP2, PLCG1).
Framing kept pleiotropic: T cell cytokine genes, osteoclast differentiation, heart valves.

## Sources
- Falcon deep research (`NFATC1-deep-research-falcon.md`, auto-generated; cites reviews without PMIDs, used for background only).
- UniProt O95644; cached publications for all GOA PMIDs (`just fetch-gene-pmids human NFATC1`, 19/19 cached),
  plus PMID:12479813 and PMID:10358178, which were already in the cache.

## Key biology (with provenance)
- Rel homology DNA-binding domain; NMR structure of human NFATC1 DBD on IL2 ARRE2
  [PMID:9506523 "solution structure of the binary complex formed between the core DNA-binding domain of human NFATC1 and the ARRE2 DNA site from the interleukin-2 promoter"].
- Cytoplasmic when phosphorylated; calcineurin dephosphorylation drives nuclear import
  [PMID:16511445 "In resting cells, NFAT proteins are heavily phosphorylated and reside in the cytoplasm"].
- Calcineurin docking via two sites (PxIxIT, LxVP) [PMID:10860980 "second Cn-binding element in NFATc"; PMID:24954618 LxVP peptide binds CnA].
- IL2 [PMID:8202141 "indicating that NF-ATc is required for IL-2 gene expression"].
- Osteoclasts (mouse) [PMID:12479813 "NFATc1 may represent a master switch for regulating terminal differentiation of osteoclasts, functioning downstream of RANKL"];
  PU.1 partner at cathepsin K [PMID:15304486].
- Valves (mouse KO) [PMID:12370307 "Disruption of the NFATc1 gene resulted in embryonic lethality due to aberrant heart valve formation"].
- Chromatin-restricted complexes with JUN, CREB1, ATF1/2/3 [PMID:25609649].

## Decisions
- 66 GOA rows + 2 NEW. Protein binding IPI rows: PPP3CA -> MODIFY to GO:0030346 PP2B binding;
  JUN/ATF1/ATF2/ATF3/CREB1 -> MODIFY to GO:0061629; OGT, HOMER2, HOMER3, DVL1, HOXC13 -> REMOVE (uninformative; NFATC1 is client/substrate).
- FK506 binding (TAS, PMID:8702849) REMOVED: FK506 binds FKBP12; the paper only shows CsA sensitivity.
- Negative regulation of inflammatory response (PMID:35930205) MARK_AS_OVER_ANNOTATED: NFAT dependence shown only with CsA; anti-inflammatory outcome inferred.
- TAS PMID:10821850 is about "NFAT1" (usually NFATC2); accepted since the MF is correct, flagged in reference_review.
- Valve morphogenesis, Wnt repression, VSMC differentiation, p38 binding, nuclear body, intracellular signal transduction -> KEEP_AS_NON_CORE.
- NEW: GO:0030316 osteoclast differentiation (PMID:12479813; TF does the program's work, comparator SPI1 carries GO:0030316 in human GOA);
  GO:0032743 positive regulation of interleukin-2 production (PMID:8202141).
- Core MF: GO:0001228 (activator), GO:0061629 (partner TF binding), GO:0030346 (calcineurin docking).

## Deep research integration (falcon)

Report (`NFATC1-deep-research-falcon.md`) cites reviews by DOI/page only. DOIs of the primary studies it relies on
were resolved via PubMed esearch and cached: PMID:42568576 (Sampere-Birlanga 2026), PMID:38346075 (Chaudhry 2024),
PMID:39629220 (Yang 2024/2025), PMID:38926604 (Sato 2024), PMID:34943970 (Patil 2021); all full text.
Reviews it leans on (not fetched, not used for annotation): Cai 2021 (DOI 10.3389/fcvm.2021.635172),
Patterson 2021 Hemato, Kitamura 2021 IJMS, Thiel 2021 Cells, Oliveira 2026, Zheng 2024 (PMID:38310228), Wu 2024 TIBS.

Claim classification (~30 substantive claims):
- Confirms review (~17): NHR/RHR/TAD architecture; GGAA(A) core motif; weak monomeric DNA binding and AP-1 cooperativity;
  PxIxIT and LxVP calcineurin docking (VIVIT competes); phospho-masked NLS; Ca2+/CaM-calcineurin activation;
  GSK3/CK1/DYRK rephosphorylation and export; p38 phosphorylation; IL2/IL4 targets; autoregulated P1 alphaA isoform;
  osteoclast master regulator downstream of RANKL; valve/endocardial requirement; VSMC/vascular gene regulation;
  CsA/FK506 act on calcineurin, not NFATC1 (consistent with REMOVE of FK506 binding).
- Adds something new (~6): NFATc1/alphaA promotes survival of exhausted CD8+ T cells [PMID:42568576 "Chronic antigen
  receptor stimulation induces the expression of NFATc1/αA, a short isoform of NFATc1 that promotes TEX cell survival."];
  persistent MCMV memory inflation [PMID:38346075]; TH2 polarization and DC priming [PMID:39629220 "Nfatc1's absence in
  CD4+ T cells directly hampered TH2 cell polarization and functionality"]; histone gene repression [PMID:38926604];
  NFATc1-EZH2 complex in PDAC [PMID:34943970]; beta-cell targets (Simonett 2021, NFATC2-focused).
- Conflicts with review: none substantive.
- Not relevant / unsupported (~7): cancer roles (CRC EMT/SNAI1, prostate, HCC FasL tumour suppression, FLT3-ITD AML,
  CML imatinib resistance, VEGF/COX-2/CXCR7 angiogenesis), RA therapeutic targeting, pharmacology (A-285222, INCA-6),
  diabetic atherosclerosis (CD137/OX40) - disease/pathway context, not GO-relevant or review-level only.

Adopted:
- description: alphaA isoform induced by chronic stimulation promoting exhausted CD8+ T cell survival; contribution
  to TH2 differentiation (PMID:42568576, PMID:38346075, PMID:39629220).
- core_functions (pleiotropic programs): added supported_by quotes from PMID:42568576 and PMID:39629220.
- references: report title fixed and reference_review added (MEDIUM / LOW_QUALITY); five primary papers added with
  findings and reference_review.
- suggested_questions: histone repression / GO:0000122; direct targets (TOX, BCL2L11/BCL2) of alphaA in exhaustion.
- suggested_experiments: test direct histone gene repression in non-transformed human cells.

Not acted on:
- No existing-annotation action changed (report offers no primary evidence against any decision).
- No NEW annotations. Histone repression (GO:0000122) rests on one Sci Rep study in MCF7 cells (knockdown + ChIP),
  so raised as a question rather than asserted. Exhaustion/TH2/memory evidence is mouse genetic necessity evidence for
  broad immune processes; the existing T cell framing (IL2 production NEW, cytokine gene activation) already covers
  the TF's direct role, so no further BP terms proposed. EZH2 interaction is cancer-context and would be protein binding.

Report errors / overstatements detected:
- Domain/NLS claims cited to Oliveira 2026 (a neurodegeneration review) and Hui 2023 (about NFAT3/NFATc4 in cardiac
  hypertrophy) - off-target citations for NFATC1-specific statements (the claims themselves are generic and correct).
- Beta-cell targets cited to Simonett 2021, whose title is about NFATC2 targets; the report itself concedes NFATC1
  directness is uncertain.
- "NFATc1/alphaA ... repressing the pro-apoptotic protein Bim": PMID:42568576 only reports Bcl2l11 "slightly increased"
  in NFATc1-deficient cells and speculates on the Bim/Bcl-2 ratio.
- TOX induction by NFATc1 is attributed to Sampere-Birlanga 2026, which cites it from earlier work (its ref 24).
- "embryonic lethality ... and organ hypoplasia" (Kitamura review) not verified against primary KO papers; valve
  defect lethality is supported (PMID:12370307).
