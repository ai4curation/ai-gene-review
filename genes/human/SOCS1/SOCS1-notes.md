# SOCS1 (O15524) — Gene Review Notes

Journal of research for the SOCS1 AI gene review. Provenance recorded inline.

## Identity / domain architecture (from UniProt O15524)

- Suppressor of cytokine signaling 1 (SOCS-1); aliases JAB (JAK-binding protein),
  SSI-1 (STAT-induced STAT inhibitor 1), TIP-3. 211 aa, human, chr 16p13.
- Domain layout (UniProt feature table): disordered N-terminus (1–53, Pro-rich
  36–49); **Kinase inhibitory region (KIR), 55–66**; **Extended SH2 subdomain (ESS),
  67–78**; **SH2 domain, 79–174**; **SOCS box, 161–210** (Elongin-BC binding region
  173–182). This KIR–ESS–SH2–SOCS box layout is the canonical SOCS architecture.
- UniProt FUNCTION: "Essential negative regulator of type I and type II interferon
  (IFN) signaling, as well as that of other cytokines, including IL2, IL4, IL6 and
  leukemia inhibitory factor (LIF)... Downregulates cytokine signaling by inhibiting
  the JAK/STAT signaling pathway. Acts by binding to JAK proteins and to IFNGR1 and
  inhibiting their kinase activity... Probable substrate recognition component of an
  ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin ligase complex which mediates
  the ubiquitination and subsequent proteasomal degradation of target proteins."

## Core mechanism — JAK/STAT negative feedback

- SOCS1 was independently cloned in 1997 by three groups as a cytokine-inducible
  inhibitor of JAK/STAT signaling:
  - [PMID:9202125 "We have cloned a complementary DNA encoding a protein SOCS-1,
    containing an SH2-domain, by its ability to inhibit the macrophage differentiation
    of M1 cells in response to interleukin-6. Expression of SOCS-1 inhibited both
    interleukin-6-induced receptor phosphorylation and STAT activation."] —
    establishes negative-feedback role; "Transcription of all four SOCS genes is
    increased rapidly in response to interleukin-6... suggesting they may act in a
    classic negative feedback loop to regulate cytokine signal transduction."
  - [PMID:9202126 "we have now isolated a new SH2-domain-containing protein, JAB,
    which is a JAK-binding protein that interacts with the Jak2 tyrosine-kinase JH1
    domain... Interaction of JAB with Jak1, Jak2 or Jak3 markedly reduces their
    tyrosine-kinase activity and suppresses the tyrosine-phosphorylation and
    activation of STATs."] — direct demonstration of JAK binding (JH1 kinase domain)
    and inhibition of JAK catalytic activity. This is the basis for the
    protein-kinase-inhibitor MF (GO:0004860) and the JAK-STAT negative regulation BP.

- Mechanistic basis (crystal structure of SOCS1:JAK1 kinase domain, PMID:29662058,
  Nat Commun 2018; PDB 6C7Y — not in local cache, used via WebSearch only):
  SOCS1 inhibits JAK1/JAK2/TYK2 (but not JAK3) by its KIR acting as a pseudosubstrate
  that blocks the JAK substrate-binding groove (His54 mimics the substrate tyrosine;
  KIR wedges between the activation loop and the αG helix), while the SH2 domain docks
  onto a phosphotyrosine in the JAK activation loop. This supports protein kinase
  inhibitor activity (GO:0004860) and SH2 phosphotyrosine docking (GO:0042169 SH2
  domain binding describes the reciprocal; for SOCS1 the relevant MF is binding via
  its own SH2 to pTyr targets). UniProt DOMAIN note: "The ESS and SH2 domains are
  required for JAK phosphotyrosine binding. Further interaction with the KIR domain is
  necessary for signal and kinase inhibition."

## SOCS-box / E3 ubiquitin ligase adaptor function

- The SOCS box recruits the Elongin BC complex and a Cullin (CUL2 or CUL5)/RBX1
  scaffold, making SOCS1 the substrate-recognition subunit of an ECS (Elongin
  BC-CUL2/5-SOCS box) E3 ubiquitin ligase that targets bound substrates for
  proteasomal degradation. UniProt FUNCTION (PubMed:11278610, 11313480): "Probable
  substrate recognition component of an ECS... E3 ubiquitin ligase complex which
  mediates the ubiquitination and subsequent proteasomal degradation of target
  proteins." PATHWAY: protein ubiquitination.
- Direct experimental demonstration of SOCS1 in a functional E3 complex targeting a
  defined substrate (NF-κB RelA):
  [PMID:17183367 "COMMD1 accelerates the ubiquitination and degradation of NF-kappaB
  subunits through its interaction with a multimeric ubiquitin ligase containing
  Elongins B and C, Cul2 and SOCS1 (ECS(SOCS1))... facilitate substrate binding to the
  ligase by stabilizing the interaction between SOCS1 and RelA."] — supports
  ubiquitin-ligase-adaptor function and protein ubiquitination (GO:0016567).
- General SOCS-box principle: [PMID:16643902 "All SOCS proteins bind an Elongin BC E3
  ubiquitin ligase complex through the common Socs-box."] (this paper is principally
  about SOCS6, but states the shared SOCS-box/Elongin-BC E3 mechanism).

## Substrate / partner interactions (mostly GO:0005515 protein binding, IPI)

- The IPI GO:0005515 annotations come from large-scale interaction / network studies,
  not focused functional characterization:
  - PMID:16273093 — ErbB SH2/PTB protein-microarray network (with ERBB2/P04626).
  - PMID:16643902 — HOIL-1/SOCS6 study (with ELOC/Q15369).
  - PMID:17183367 — COMMD1/ECS(SOCS1) (with RELA/Q04206, ELOC/Q15369, COMMD1/Q8N668);
    biologically meaningful (E3 complex), but term is generic "protein binding".
  - PMID:18172216 — SOCS1 binds HIV-1 Gag (with gag/Q77YG1); full text confirms
    direct binding via SH2: [PMID:18172216 "SOCS1 can directly bind to the matrix and
    nucleocapsid regions of the HIV-1 p55 Gag polyprotein and enhance its stability and
    trafficking"]. Host-pathogen / non-core for the gene's own physiology.
  - PMID:31980649 — KRAS-rewired EGFR network AP-MS (with ELOC/Q15369).
  - PMID:32296183 — HuRI binary interactome (with SH3GL1/Q99961).
  - PMID:35512704 — cancer neoPPI screen (with SMAD4/Q13485).
  - PMID:23401859 — DCNL1/CUL2 neddylation study (with DCUN1D1/O14508, etc.).
  All are appropriately KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED: "protein binding"
  is uninformative per curation guidelines; none should be a core function.

- IGF1R / IGF1R binding: [PMID:9727029 "hSOCS-1 protein also interacted strongly with
  IGF-IR in the two-hybrid assay."] — the paper is mainly about SOCS-2, but explicitly
  assays SOCS-1 binding IGF-IR. Supports GO:0005159 (IGF receptor binding, IPI, WITH
  IGF1R/P08069) and GO:0019901 protein kinase binding (IPI, WITH JAK2/O60674) and the
  NAS GO:0046426 JAK-STAT negative regulation. These IGF/insulin-receptor links are
  real but peripheral relative to the canonical cytokine/JAK role → non-core.

## Process annotations from miRNA / immune-cell papers (IMP/ISS)

- GO:0030225 macrophage differentiation (IMP, PMID:32634427): miR-155-5p targets SOCS1;
  SOCS1 up-regulation promotes macrophage M2 polarization via PD1/PDL1 in ITP.
  [PMID:32634427 "up-regulation of SOCS1 facilitated macrophage M2 polarization"].
  Indirect (SOCS1 as a miRNA target read-out), downstream/contextual → non-core.
- GO:0045591 positive regulation of regulatory T cell differentiation (IMP,
  PMID:22387553): SOCS1 is a miR-155 target in ILT3-induced CD8+ Ts cells. The paper
  is about ILT3/miRNA-driven CD8 T-suppressor differentiation; SOCS1 appears as a
  miR-155 target, evidence for a Treg-differentiation GO term is weak from the abstract
  → UNDECIDED/KEEP_AS_NON_CORE.
- GO:0046426 JAK-STAT negative regulation (IMP, PMID:25019494): miR-221 downregulates
  SOCS1/SOCS3 to potentiate IFN's anti-HCV effect; [PMID:25019494 "SOCS1 and SOCS3,
  which are well established inhibitory factors on IFN/JAK/STAT pathway"]. Consistent
  with the core JAK-STAT-inhibitor role → ACCEPT (core).
- T-cell differentiation terms GO:0043372 (positive reg CD4 T cell diff) and GO:0043377
  (negative reg CD8 T cell diff) are IEA/ISS transferred from mouse ortholog O35716.
  Reflect SOCS1's role in T-cell homeostasis (Socs1-null phenotype); plausible but
  electronic/by-similarity → KEEP_AS_NON_CORE.

## Localization

- Cytosol (GO:0005829, TAS Reactome) and cytoplasm (GO:0005737, TAS PMID:9202126) —
  SOCS1 acts on receptor-associated JAKs in the cytoplasm; consistent, ACCEPT (cytosol
  as primary). Nucleoplasm (GO:0005654, IDA HPA) and nucleus (GO:0005634, IEA) — SOCS1
  has reported nuclear functions (e.g., binding/degrading nuclear targets such as RelA,
  p53); UniProt lists Nucleus as a location (PubMed:16410555). KEEP_AS_NON_CORE.
- Cytoplasmic vesicle (GO:0031410, IEA): UniProt notes "Detected in perinuclear
  cytoplasmic vesicles upon interaction with FGFR3" (PubMed:16410555). Condition-
  specific; KEEP_AS_NON_CORE.

## Disease / physiology context (for description, not curation commentary)

- UniProt DISEASE: Autoinflammatory syndrome, familial, with or without
  immunodeficiency (AISIMD; MIM:619375), autosomal dominant; caused by SOCS1
  haploinsufficiency / loss-of-function variants (R22W, P123R, Y154H, 64–211 del),
  which cause loss of inhibition of cytokine-induced STAT phosphorylation (IFNG/STAT1,
  IL2/STAT5, IL4/STAT6). Mouse Socs1-null die neonatally of IFN-γ-driven inflammation
  (well-established literature; context only). SOCS1 is also a tumor suppressor often
  silenced by promoter methylation (general literature).

## Summary of intended core functions

1. Protein kinase inhibitor activity (GO:0004860) — inhibits JAK1/JAK2/TYK2 catalysis
   (KIR pseudosubstrate + SH2 docking). MF, core.
2. SH2 phosphotyrosine docking onto activated JAKs/receptors (SOCS1's SH2). MF, core.
3. Negative regulation of JAK-STAT receptor signaling (GO:0046426), incl. IFN-γ. BP,
   core.
4. Substrate-recognition adaptor of ECS(SOCS1) Elongin-BC/Cul2-5 E3 ubiquitin ligase →
   substrate ubiquitination/proteasomal degradation (GO:0016567 protein
   ubiquitination). BP, core.

## Sources consulted
- UniProt O15524 (local cache).
- Cached publications: PMID 9202125, 9202126, 9727029, 16273093, 16643902, 17183367,
  18172216, 22387553, 23401859, 25019494, 31980649, 32296183, 32634427, 35512704.
- WebSearch: SOCS1:JAK1 structure (PMID:29662058 / PDB 6C7Y; Nature Communications
  2018) — mechanism only, NOT cited as supporting_text since not in local cache.
</content>
</invoke>
