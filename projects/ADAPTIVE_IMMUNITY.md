---
title: "Adaptive Immunity"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
---

# Adaptive Immunity

**Bottom line:** this project covers the adaptive immune system in human:
how antigen is processed and shown on MHC, how T and B cell receptors are built
by V(D)J recombination and signal, how co-stimulation and checkpoints set the
response, how T and B cells differentiate, and how antibodies are diversified
and act. We divided it into 12 areas, each grounded in GO biological process
terms, with 105 human anchor genes. Only 19 of the 105 have a review (12
COMPLETE, 5 DRAFT, 2 IN_PROGRESS), mostly cytokine-signaling and T helper
transcription-factor genes from the [AUTOIMMUNE](AUTOIMMUNE.md) project. The
core machinery of the area has no review at all: MHC class I and II
presentation, V(D)J recombination and T cell cytotoxicity are 0 reviewed, and
the T cell receptor module's seven grounded proteins (CD3, LCK, ZAP70, LAT,
PLCG1, NFATC1) are all unreviewed. Four adaptive signaling modules exist, all
DRAFT, and nothing yet models antigen presentation or receptor gene
recombination. The next step is to review the T cell receptor trunk and the MHC
class I pathway; both already have human GO-CAM models to check the reviews
against.

The counts come from [coverage.md](ADAPTIVE_IMMUNITY/coverage.md), which
`ADAPTIVE_IMMUNITY/scripts/coverage.py` generates from the scope file
`ADAPTIVE_IMMUNITY/areas.yaml`, the gene reviews, the modules and
`gocams/index.tsv`. Re-run the script after new reviews land; do not edit the
counts by hand.

## Scope

In scope: processes that depend on somatically rearranged antigen receptors
(GO:0002460, under GO:0002250 adaptive immune response), and the machinery
that builds, triggers, regulates and executes them. Out of scope: innate
pattern recognition, inflammasomes, interferon induction and complement,
except where a gene is also an adaptive anchor (for example the Fc receptors
that carry out antibody effector function). Innate-immune work already has its
own projects: [cGAS-STING](CGAS_STING_PATHWAY.md),
[NLRP3 inflammasome](NLRP3_INFLAMMASOME.md) and
[C. elegans surveillance immunity](CAEEL_SURVEILLANCE_IMMUNITY.md).

## Areas

Reviewed / anchor genes per area, from [coverage.md](ADAPTIVE_IMMUNITY/coverage.md).

| Area | GO grounding | Modules | Reviewed |
|---|---|---|---:|
| MHC class I antigen processing and presentation | GO:0019885 | none | 0/8 |
| MHC class II antigen processing and presentation | GO:0019886 | none | 0/7 |
| V(D)J recombination | GO:0033151 | none | 0/7 |
| T cell receptor signaling | GO:0050852 | [t_cell_receptor_signaling](../modules/t_cell_receptor_signaling.html) | 2/14 |
| T cell co-stimulation and inhibitory checkpoints | GO:0031295 | none | 3/9 |
| IL-2 and common gamma-chain cytokine signaling | GO:0038110 | [jak_stat_signaling](../modules/jak_stat_signaling.html) | 5/11 |
| Helper and regulatory T cell differentiation | GO:0046632 | none | 5/9 |
| T cell mediated cytotoxicity | GO:0001913 | none | 0/7 |
| B cell receptor signaling | GO:0050853 | [b_cell_receptor_signaling](../modules/b_cell_receptor_signaling.html) | 3/12 |
| B cell differentiation and germinal center | GO:0030183, GO:0002467 | none | 1/10 |
| Class switch recombination and somatic hypermutation | GO:0045190, GO:0016446 | none | 1/6 |
| Antibody transport and Fc receptor effector signaling | GO:0006959 | [Fc-gamma](../modules/fc_gamma_receptor_signaling.html), [Fc-epsilon](../modules/fc_epsilon_receptor_signaling.html) | 0/7 |

A gene can anchor more than one area (BCL6 and IRF4 each appear
twice), so the per-area gene counts add up to 107, not 105.

## Existing resources

- **Gene reviews.** COMPLETE reviews exist for CD247 (the TCR zeta chain),
  CD8A, CD28, CTLA4, GATA3, LYN, PIK3CD, PLCG2, JAK1, STAT3, STAT5A and STAT5B.
  AICDA, BACH2, IL2RA, IRF4 and STAT4 are DRAFT; IL7R and PTPN22 are
  IN_PROGRESS.
- **Modules.** Four adaptive modules, all DRAFT: T cell receptor signaling
  (0 of 7 grounded proteins reviewed), B cell receptor signaling (1 of 7),
  Fc-gamma and Fc-epsilon receptor signaling (1 of 7 each). The JAK-STAT module
  (8 of 10) covers the signaling half of the IL-2 area.
- **GO-CAM models.** 53 of the 105 anchor genes appear in at least one human
  GO-CAM activity. Relevant cached models include MHC class I peptide loading,
  MPEG1 (perforin-2) pore formation for antigen cross-presentation, the IL-2,
  IL-7 and IL-15 signaling pathways, T-helper 17 lineage commitment, CD70-CD27
  in T cell activation, CD72 and BCR co-stimulation, and viral inhibition of
  TAP (HSV-1 ICP47, HCMV US6, EBV BNLF2a) and of TCR signaling via LAT (HSV-1
  US3). Read the matching models before proposing any new process annotation;
  they are the curators' own statement of each gene's role.

## Curation rules for adaptive-immune genes

1. **Separate the activity from the pathway.** Give each protein its own
   molecular function (peptide antigen binding for MHC, ABC-type peptide
   antigen transporter activity for TAP, protein tyrosine kinase activity for
   LCK/ZAP70/SYK, a scaffold activity for LAT/BLNK, endonuclease activity for
   RAG1 and DCLRE1C, DNA cytosine deamination for AICDA) and use the pathway terms as process. Replace generic
   `protein binding` IPI rows with an informative term or remove them; they
   were 144 of the 174 removals in AUTOIMMUNE.
2. **Pleiotropic DNA repair genes are non-core here.** PRKDC, LIG4, NHEJ1, UNG,
   MSH2, MSH6, POLH and REV1 act in V(D)J recombination, class switching or
   hypermutation, but their core function is general DNA repair. Keep the
   adaptive process terms as non-core; the lymphocyte-specific enzymes (RAG1,
   RAG2, DNTT, AICDA) are the core members.
3. **Knockout phenotypes record necessity, not participation.** Mouse
   knockouts put terms such as `T cell differentiation`, `B cell proliferation`
   or `immunoglobulin production` on almost any gene whose loss blocks
   lymphocyte development. Ask which protein performs the step before accepting
   or proposing such a term, per `CLAUDE.md`.
4. **Ligands, antigens and substrates do not perform the step.** A peptide is
   not `involved_in` antigen processing, and a cytokine is not `involved_in`
   the receptor signaling it triggers unless it does part of the work. Run the
   comparator check from `CLAUDE.md` before proposing such a term with `NEW`.
5. **Check propagation carefully.** MHC, KIR, Fc receptor and immunoglobulin
   families expand and diverge by lineage, and many adaptive genes have no
   ortholog outside jawed vertebrates. Review ISO and IBA rows against the
   ortholog relation and node placement ([IBA review](IBA_REVIEW.md),
   [ISO failure taxonomy](ISO.md)).
6. **Viral immune evasion is annotated on the viral protein.** The TAP and LAT
   inhibitors above get symbiont-mediated suppression terms; the host protein
   gets no term for being targeted.

## Plan

- [x] Define the scope: 12 areas, GO grounding and 105 anchor genes
      (`ADAPTIVE_IMMUNITY/areas.yaml`, symbols checked against HGNC).
- [x] Generate the coverage tables (`scripts/coverage.py` → `coverage.md`).
- [ ] Review the T cell receptor trunk: CD3D, CD3E, CD3G, LCK, ZAP70, LAT,
      LCP2, PLCG1, NFATC1. This also grounds the T cell receptor module.
- [ ] Review the MHC class I pathway: HLA-A, B2M, TAP1, TAP2, TAPBP, ERAP1,
      and check them against the MHC class I peptide loading GO-CAM.
- [ ] Review the B cell receptor trunk (CD79A, CD79B, SYK, BTK, BLNK, CD19) and
      V(D)J recombination (RAG1, RAG2, DCLRE1C, DNTT).
- [ ] Finish the co-stimulation and checkpoint area (CD80, CD86, ICOS, PDCD1,
      CD274, LAG3) and the MHC class II and cytotoxicity areas.
- [ ] Scope new modules for MHC class I presentation, MHC class II
      presentation and V(D)J recombination, which have GO terms but no module.
- [ ] Move the TCR, BCR and Fc receptor modules out of DRAFT as their grounded
      proteins are reviewed.
- [ ] Re-run `coverage.py` and update the bottom line after each batch.

## Related projects

- [Autoimmune genetics](AUTOIMMUNE.md): 20 immune-regulation risk genes,
  including CD28, CTLA4, IL2RA, IL7R, PTPN22, STAT4, BACH2 and IRF4, which are
  anchor genes here.
- [ICAM-3 receptor activity obsoletion](ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.md):
  the ICAM3 ligand and its LFA-1 receptor, which mediate T cell adhesion to
  antigen-presenting cells.
