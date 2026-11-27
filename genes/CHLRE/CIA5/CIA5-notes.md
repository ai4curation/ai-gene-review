# CIA5 (CCM1) notes — Chlamydomonas reinhardtii, UniProt Q9FED4

## Deep research

- 2026-10-03: `scripts/deep_research_wrapper.py CHLRE CIA5 falcon --fallback perplexity-lite`
  run once. Falcon returned HTTP 402 Payment Required; the perplexity-lite fallback
  failed because the perplexity provider is not available in this environment. Not
  retried. No deep-research file exists; the review is built from the cached primary
  literature below.

## GOA status

- The GOA file for Q9FED4 has a header only: no existing GO annotations. All
  annotations in the review are `NEW` proposals.
- UniProt entry is unreviewed (TrEMBL, "CCM1-A"), only Gene3D "Classic Zinc Finger"
  and MobiDB disorder regions. Gene model CHLRE_02g096300v5.

## Identity and structure

- Cloned independently as Ccm1 and Cia5 in back-to-back PNAS papers.
  [PMID:11287669 "we isolated a nuclear regulatory gene, Ccm1, encoding a 699-aa
  hydrophilic protein with a putative zinc-finger motif in its N-terminal region and
  a Gln repeat characteristic of transcriptional activators"]
- cia5 lesion is His54 in the zinc finger. [PMID:11287669 "His-54 within the putative
  zinc-finger motif of the CCM1 is crucial to its regulatory function"]
- Two zinc sites, each binding 1 Zn. [PMID:18202004 "1 mol of zinc is bound to 1 mol
  of amino acid regions 1-71 and 72-101 of CCM1, respectively"]; C2H2 finger at
  ~35-70 [PMID:42448334 "one in a C2H2 zinc finger between amino acids 35 and 70"].
- Complex of 290-580 kDa [PMID:18202004].
- Volvox ortholog, 51% identity, conserved zinc region, putative NLS/NES, C-terminal
  LXXLL [PMID:21253860]. Lineage-restricted [PMID:42488443].

## Expression / regulation of CIA5 itself

- mRNA and protein constitutive in high and low CO2 [PMID:11309511 "is present
  constitutively in low and high CO2 conditions"]; therefore thought to be activated
  post-translationally [PMID:22634760].
- C-terminal 54-aa truncation complements but causes constitutive expression of
  CO2-responsive genes [PMID:11309511].
- Degraded by proteasome under Zn deficiency [PMID:42448334 "its encoded protein
  undergoes proteasomal degradation under Zn deficiency"].

## Localization

- Nuclear: CCM1-mGold in ccm1-1 [PMID:41637450 "Confocal microscopy revealed strong
  nuclear signals in both transformants under HC and VLC conditions (Fig. 3A)."].
  Earlier report (Wang et al. 2005, Can J Bot; not in PubMed) cited by PMID:42448334.

## Interactors

- CBP1 = ZNG3 (Cre16.g684650), CobW/WW-domain COG0523 GTPase, constitutive nuclear
  partner. Shimamura 2026 [PMID:41637450] calls it CBP1 and shows it represses 27 of
  41 CCM1-dependent genes under high CO2; Kusi-Appiah 2026 [PMID:42448334] calls it
  ZNG3, shows proteasomal co-degradation in low Zn.
- GDH1/2 co-purify more weakly [PMID:41637450].

## Regulon

- Almost all LCI genes require CCM1 [PMID:15235119]. ~25% of transcriptome affected by
  CIA5 and/or CO2 [PMID:22634760]. Includes HLA3, LCIA, LCIB, LCIC, CAH1, CAH3, LCR1
  [PMID:22634760, PMID:42488443], LHCSR3 and PSBS [PMID:37031262], and the pyrenoid
  kinase KEY1 [PMID:42488443].

## DNA binding: the key decision

- PMID:22634760 (2012): sequences recognized by the "putative DNA binding domain"
  unknown.
- PMID:41637450 (2026 PNAS): "direct DNA binding has not been demonstrated, suggesting
  that CCM1 operates in conjunction with other nuclear factors."
- PMID:42488443 (2026 review): cites Chen and Spalding 2026 (Plant Mol Biol Rep,
  doi:10.1007/s11105-025-01670-7) — RBSS + gel shift with purified full-length CIA5,
  GC-rich 9-bp motif (GGGGCGGGG per publisher abstract found by web search) in
  promoters of three CIA5-dependent genes. Not indexed in PubMed; publisher page not
  retrievable here, so not cached and not used as direct evidence.
- Decision: do NOT assert GO:0003700 DNA-binding transcription factor activity or
  GO:0043565 sequence-specific DNA binding. A single in vitro study, unavailable for
  verification, with no in vivo occupancy data. Recorded as a suggested question.
  Positive regulation of DNA-templated transcription (GO:0045893, IMP) is proposed,
  because the effect is transcriptional and CIA5 is a nuclear regulator whose own
  C-terminal state determines target transcription [PMID:11309511].

## Cellular response to carbon dioxide (GO:0071244)

- The stimulus is CO2 limitation. GO has no "low CO2" term; GO:0071244 is the
  closest. Comparator check (QuickGO, exact, experimental): Candida RCA1, UME6, FLO8
  and yeast CST6 (transcription regulators mediating CO2 responses) carry GO:0071244 or
  GO:0010037 by IMP, so annotating a CO2-responsive transcription regulator to this
  term follows existing practice. CIA5 passes the participation test as the regulator
  that converts CO2 status into transcriptional output.
- Module `modules/pyrenoid_ccm.yaml` assertion (no MF, process GO:0071244) is
  supported.
