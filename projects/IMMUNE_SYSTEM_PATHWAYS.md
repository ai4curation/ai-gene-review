---
title: "Immune System Pathways"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
collections: [IMMUNE_SYSTEM]
species: [human, mouse, worm]
---

# Immune System Pathways

**Bottom line:** this is the umbrella project for immune signaling and effector
pathways. It ties together the immune projects that already exist (autoimmune
risk genes, cGAS-STING, the NLRP3 inflammasome, *C. elegans* surveillance
immunity and others), the 15 draft immune signaling modules under `modules/`,
and the human GO-CAM models of the same pathways. It also sets one
shared scope: 12 pathway areas, each tied to GO biological process terms and a
list of 145 human anchor genes (receptor, adaptor, kinase, effector, key
brake). Of those 145 genes, 31 have a review (24 COMPLETE, 5 DRAFT, 2
IN_PROGRESS) and 114 have none. The gaps are uneven. Cytokine and interferon
signaling are best covered, because the AUTOIMMUNE project reviewed JAK-STAT and
cytokine-receptor genes. Pattern-recognition receptors are almost untouched
(TLR2-9, MYD88, NOD1/2 and RIG-I have no review), and antigen presentation,
complement and phagocyte killing have no module and almost no reviews. Every
module is DRAFT and most of their grounded proteins have no review, so the next
step is to review the anchor genes area by area, starting with the TLR and
cytosolic nucleic-acid sensing trunks, and use those reviews to finish the
modules.

The per-gene numbers above come from
[coverage.md](IMMUNE_SYSTEM_PATHWAYS/coverage.md), which
`IMMUNE_SYSTEM_PATHWAYS/scripts/coverage.py` generates from the scope file
`IMMUNE_SYSTEM_PATHWAYS/areas.yaml`. Re-run the script after new reviews
land; do not edit the counts by hand.

## Why an umbrella project

Immune pathways share components more than most areas. TRAF6, TBK1, the IKK
complex, the JAK kinases and the STATs each sit in several pathways, so one
review serves many projects. Reviewing pathway by pathway in separate projects
risks repeating that work and making different calls on the same gene. Immune
genes also attract a few systematic annotation problems, listed below. One
scope, one gene list and one set of curation rules keep those calls
consistent.

## Pathway areas

Each area is grounded in GO biological process terms and linked to the
modules and projects that already cover it. Counts are anchor genes with a
review / anchor genes in the area (from [coverage.md](IMMUNE_SYSTEM_PATHWAYS/coverage.md)).

| Area | GO grounding | Modules | Projects | Reviewed |
|---|---|---|---|---:|
| Toll-like receptor signaling | GO:0002224 | [toll_like_receptor_signaling](../modules/toll_like_receptor_signaling.html) | — | 1/12 |
| NLR signaling and inflammasomes | GO:0035872 | [nlr_signaling](../modules/nlr_signaling.html) | [NLRP3 inflammasome](NLRP3_INFLAMMASOME.md), [Chimeric mRNA](CHIMERIC_MRNA_IMMUNITY.md) | 3/13 |
| Cytosolic nucleic-acid sensing | GO:0039529, GO:0140896 | [rig_i_signaling](../modules/rig_i_signaling.html) | [cGAS-STING](CGAS_STING_PATHWAY.md), [KW-1110 TRAF](KW_1110_TRAF_KW2GO.md) | 4/11 |
| Interferon signaling | GO:0060337, GO:0060333 | [type I IFN](../modules/type_i_interferon_signaling.html), [type II IFN](../modules/type_ii_interferon_signaling.html), [JAK-STAT](../modules/jak_stat_signaling.html) | — | 4/13 |
| NF-kappaB and TNF signaling | GO:0007249, GO:0033209 | [nfkb_canonical_signaling](../modules/nfkb_canonical_signaling.html), [tnf_signaling](../modules/tnf_signaling.html) | — | 3/12 |
| Interleukin and chemokine signaling | GO:0019221 | [il1](../modules/il1_signaling.html), [il6](../modules/il6_signaling.html), [chemokine](../modules/chemokine_signaling.html) | [Autoimmune](AUTOIMMUNE.md) | 8/17 |
| T cell receptor signaling and co-stimulation | GO:0050852 | [t_cell_receptor_signaling](../modules/t_cell_receptor_signaling.html) | [Autoimmune](AUTOIMMUNE.md) | 5/15 |
| B cell receptor and Fc receptor signaling | GO:0050853 | [BCR](../modules/b_cell_receptor_signaling.html), [Fc-epsilon](../modules/fc_epsilon_receptor_signaling.html), [Fc-gamma](../modules/fc_gamma_receptor_signaling.html) | — | 1/12 |
| Antigen processing and presentation | GO:0019882 | none | — | 0/9 |
| Complement activation | GO:0006956 | none | — | 1/15 |
| Lymphocyte diversification and cytotoxicity | GO:0002250 | none | — | 1/8 |
| Phagocyte killing and antimicrobial effectors | GO:0045087 | none | — | 0/8 |

Two further immune threads sit outside the vertebrate pathway areas but belong
in the collection:

- **Invertebrate immunity.** [C. elegans surveillance immunity](CAEEL_SURVEILLANCE_IMMUNITY.md)
  covers a system with no NF-kB, inflammasome or adaptive arm, built on
  p38 MAPK signaling and surveillance of the host's own core processes.
- **Host-pathogen and prokaryotic immunity.**
  [Parasite immune modulators](PARASITE_IMMUNE_MODULATORS.md) (host-directed
  suppressors), [anti-CRISPR proteins](ANTI_CRISPR.md), [SNIPE](SNIPE.md)
  anti-phage defence and [prokaryotic immunity term prediction](PROKARYOTIC_IMMUNITY_TERM_PREDICTION.md).

## Existing resources

- **Modules.** 15 immune signaling modules, all `DRAFT`. Their grounded
  proteins are mostly unreviewed: 0 of 7 in the T cell receptor module and 0 of
  6 in the chemokine module have a review, while JAK-STAT is the exception (8
  of 10). See the module table in [coverage.md](IMMUNE_SYSTEM_PATHWAYS/coverage.md).
- **GO-CAM models.** The cached production models include many curated human
  immune pathways, among them MYD88-dependent and -independent TLR4 signaling,
  NOD2 signaling, the NLRP3, NLRP1, AIM2 and non-canonical (CASP4) inflammasomes,
  cGAS-STING signaling in the cytosol and nucleus, and single-cytokine models
  for most interleukins from IL-1β to IL-33, as well as a large set of virus-host models
  (poxvirus, herpesvirus) that inhibit these pathways. 99 of the 145 anchor
  genes appear in at least one human GO-CAM activity; `gocams/index.tsv` is the
  join key. These models are the curators' own statement of each gene's role and
  should be read before proposing any new process annotation.
- **Gene reviews.** Complete reviews exist for the shared hubs TRAF6, TBK1,
  STING1, JAK1, STAT1, STAT2 and STAT3, and for NLRP3, GSDMD, CASP4, IFIH1 and
  the co-stimulation genes CD28 and CTLA4 (from AUTOIMMUNE) and CD247.

## Curation rules for immune genes

These come from patterns already seen in the reviews above and in the
repository-wide guidance in `CLAUDE.md`.

1. **Separate the activity from the pathway.** A signaling protein carries one
   specific molecular function (a signaling adaptor, a protein kinase, a
   ubiquitin ligase, a pattern-recognition receptor for a named ligand), and
   takes pathway terms as process. Replace generic `protein binding` IPI rows with an
   informative function term or remove them; they were 144 of the 174 removals
   in AUTOIMMUNE.
2. **Hubs are core in every pathway they transduce, not in every pathway they
   touch.** TRAF6, TBK1 and the IKK subunits collect process annotations from
   every screen that perturbed them. Keep the pathways the protein actually
   transmits, and mark downstream consequences (cytokine production, cell
   differentiation) as non-core or over-annotated.
3. **Ligands and substrates do not perform the step.** A cytokine is not
   `involved_in` the processing that matures it, and a complement component is
   annotated to complement activation only where it does part of the work (C3's
   thioester chemistry is the worked example in `CLAUDE.md`). Run the
   comparator check before adding such terms with `NEW`.
4. **Watch phenotype-driven process terms.** Knockout mice give immune process
   annotations such as `inflammatory response`, `defense response to virus` or
   `T cell differentiation` that record necessity, not participation. Treat these
   as non-core unless the protein acts in the process directly.
5. **Check propagation across species.** Immune genes evolve fast and
   families expand by lineage (TLRs, NLRs, KIRs, interferons, MHC). Review ISO
   and IBA rows against the node placement and the ortholog relation, following
   [IBA review](IBA_REVIEW.md) and the [ISO failure taxonomy](ISO.md).
6. **Record virus-host modulation on the pathogen side.** Viral inhibitors of
   these pathways are annotated with symbiont-mediated suppression terms on the
   viral protein (see [KW-1110](KW_1110_TRAF_KW2GO.md)); the host gene does not
   get a term for being targeted.

## Plan

- [x] Define the scope: 12 areas, GO grounding and 145 anchor genes
      (`IMMUNE_SYSTEM_PATHWAYS/areas.yaml`).
- [x] Generate the coverage tables (`scripts/coverage.py` → `coverage.md`).
- [x] Register the `IMMUNE_SYSTEM` project collection and add the existing
      immune projects to it.
- [ ] Review the pattern-recognition trunks first: TLR4, TLR3, MYD88, TICAM1,
      IRAK4, MAP3K7 (TLR), and RIGI, MAVS, CGAS, IRF3 (cytosolic sensing). Each
      of these already appears in several GO-CAM models.
- [ ] Review the NF-kappaB core (CHUK, IKBKB, IKBKG, NFKBIA, NFKB1, RELA),
      which every innate area above depends on.
- [ ] Review the T cell receptor and B cell receptor trunks (LCK, ZAP70, LAT,
      SYK, BTK, CD79A/B); their modules have 0 of 7 and 1 of 7 grounded
      proteins reviewed.
- [ ] Scope modules for antigen processing and presentation (MHC class I
      loading), complement activation and the phagocyte NADPH oxidase, which have
      GO terms and GO-CAM models but no module.
- [ ] Move the immune modules from `DRAFT` as their grounded proteins are
      reviewed, and check each against the matching GO-CAM models.
- [ ] Re-run `coverage.py` and update the bottom line after each batch.

## Related projects

The member list of the `IMMUNE_SYSTEM` collection appears below. Related work
that is not a member: [Allergens](ALLERGENS.md) (reviewed for native function,
not for immune roles), [ICAM-3 receptor activity obsoletion](ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.md)
and [hypochlorous acid obsoletion](HYPOCHLOROUS_ACID_OBSOLETION.md) (GO term
changes affecting leukocyte adhesion and neutrophil myeloperoxidase genes).
