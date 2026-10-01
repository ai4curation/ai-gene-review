---
title: "Adaptive Immunity"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
---

# Adaptive Immunity

**Bottom line:** this project covers the adaptive immune system in human:
how antigen is processed and shown on MHC, how T and B cell receptors are built
by V(D)J recombination and signal, how co-stimulation and checkpoints set the
response, how T and B cells differentiate, and how antibodies are diversified
and act. We divided it into 12 areas, each grounded in GO biological process
terms, with 105 human anchor genes. The first batch reviewed the T cell
receptor trunk: CD3D, CD3E, CD3G, LCK, ZAP70, LAT, LCP2, PLCG1 and NFATC1, all
COMPLETE, covering 1,103 existing annotations plus 10 new ones. The T cell
receptor area is now 11 of 14 anchor genes reviewed, and all seven proteins
grounded in the T cell receptor module have a review. Across the project, 28 of
the 105 genes have a review (21 COMPLETE). The main calls were to replace
generic `protein binding` rows with the domain-level activity each paper shows
(SH2 phosphotyrosine binding, SH3 binding, scaffold/adaptor activity), to give
the CD3 chains adaptor activity that contributes to, rather than enables, the
complex's receptor activity, and to keep knockout-phenotype processes non-core.
MHC class I and II presentation, V(D)J recombination and T cell cytotoxicity
still have no reviews. The next steps are the rest of the T cell receptor area
(CD4, ITK, PTPRC), updating the T cell receptor module from the new reviews,
and the MHC class I pathway.

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
| T cell receptor signaling | GO:0050852 | [t_cell_receptor_signaling](../modules/t_cell_receptor_signaling.html) | 11/14 |
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

- **Gene reviews.** COMPLETE reviews exist for the T cell receptor trunk
  reviewed here (CD3D, CD3E, CD3G, LCK, ZAP70, LAT, LCP2, PLCG1, NFATC1) and,
  from earlier work, CD247 (the TCR zeta chain), CD8A, CD28, CTLA4, GATA3, LYN,
  PIK3CD, PLCG2, JAK1, STAT3, STAT5A and STAT5B.
  AICDA, BACH2, IL2RA, IRF4 and STAT4 are DRAFT; IL7R and PTPN22 are
  IN_PROGRESS.
- **Modules.** Four adaptive modules, all DRAFT: T cell receptor signaling
  (7 of 7 grounded proteins reviewed), B cell receptor signaling (1 of 7),
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

## T cell receptor trunk: findings

| Gene | Annotations | Accept | Non-core | Over-annotated | Modify | Remove | Undecided | New |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| human/CD3D | 62 | 45 | 14 | 2 | 0 | 1 | 0 | 1 |
| human/CD3E | 106 | 64 | 7 | 11 | 13 | 9 | 2 | 0 |
| human/CD3G | 111 | 88 | 12 | 1 | 1 | 9 | 0 | 0 |
| human/LCK | 234 | 54 | 95 | 9 | 8 | 64 | 4 | 0 |
| human/ZAP70 | 98 | 52 | 17 | 1 | 12 | 16 | 0 | 0 |
| human/LAT | 87 | 55 | 8 | 3 | 14 | 7 | 0 | 3 |
| human/LCP2 | 109 | 39 | 1 | 1 | 37 | 30 | 1 | 2 |
| human/PLCG1 | 230 | 135 | 16 | 1 | 54 | 21 | 3 | 2 |
| human/NFATC1 | 66 | 45 | 7 | 1 | 7 | 6 | 0 | 2 |
| **Total** | **1,103** | **577** | **177** | **30** | **146** | **163** | **10** | **10** |

"Annotations" counts existing GOA rows; "New" rows are additional.

- **Generic `protein binding` was most of the work.** Where the paper shows
  the mechanism, rows were changed to the domain-level activity: SH2
  phosphotyrosine binding (ZAP70 on ITAMs, PLCG1 on receptors and LAT, LCK),
  SH3 or proline-rich binding (CD3E with NCK, PLCG1, LCP2 with GADS), or
  scaffold/adaptor activity (LAT, LCP2). Screen-only hits and enzyme-substrate
  pairs were removed.
- **CD3 chains.** CD3D, CD3E and CD3G all take signaling receptor complex
  adaptor activity (GO:0030159) contributing to the complex's transmembrane
  signaling receptor activity, since antigen is bound by TCR alpha/beta. The
  contributes_to MHC class II receptor activity row is marked over-annotated on
  all three, matching the CD247 review. CD3G alone carries receptor
  internalization, for its di-leucine endocytosis motif.
- **LAT and LCP2** are adaptors in three receptor systems: T cell receptor,
  mast cell Fc-epsilon receptor and platelet GPVI; the last two were added as
  NEW on both. LAT also gains molecular condensate scaffold activity from its
  phase-separation data.
- **Pleiotropic genes stay broad.** PLCG1's core functions lead with
  growth-factor receptor signaling (EGFR, FGFR, PDGFR), and NFATC1's include
  osteoclast differentiation, with the T cell role as one context among
  several.
- **Removed as contradicted:** serine/threonine phosphatase activity on LCK
  (it has no phosphatase domain) and FK506 binding on NFATC1 (FK506 binds
  FKBP12).
- **For curators:** a COP9 signalosome annotation from PMID:22561606 on LAT and
  PLCG1 appears to mean the TCR signalosome; PMID:22732588, cited for ZAP70
  tyrosine phosphorylation, reports that ZAP70 does not phosphorylate THEMIS;
  PMID:10821850, cited for NFATC1 transcription factor activity, describes
  NFAT1. These are recorded as suggested questions or reference reviews in the
  gene files.
- **Deep research.** All nine genes have a Falcon report (CD3G's after a
  rerun with a 45-minute timeout). Most reports arrived after the reviews were
  written, so each was integrated afterwards: every substantive claim was
  sorted as confirming, adding, conflicting or unsupported, and any claim that
  changed the review was traced to its primary paper, cached and quoted. This
  added about 35 primary papers and refined descriptions and core functions,
  but changed no annotation action except two (a NEW VEGF receptor signaling
  row on PLCG1, and one PLCG1 UNDECIDED row resolved). It also caught an
  isoform-numbering error in the LAT description. The reports themselves were
  unreliable in places: wrong-paper citations (NFATC2, NFATC4 or reviews
  credited for NFATC1 facts), preprints presented as findings, and at least
  one garbled structural claim (a CD3D salt bridge to a cytoplasmic residue).
  Each gene's notes file has a "Deep research integration" section listing
  what was adopted and rejected. Open question raised by the reports: human
  gamma-delta TCR structures (PMID:38657677) contain CD3D as well as CD3G, but
  GOA gives only CD3G the gamma-delta TCR complex term.

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
- [x] Review the T cell receptor trunk: CD3D, CD3E, CD3G, LCK, ZAP70, LAT,
      LCP2, PLCG1, NFATC1 (all COMPLETE; see findings below).
- [ ] Finish the T cell receptor area: CD4, ITK, PTPRC.
- [ ] Update the T cell receptor module's annotons to the molecular functions
      chosen in the new reviews, and check them against the TCR GO-CAMs.
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
