---
title: Deliverome GO Collaboration
species:
  - human
  - mouse
status: IN_PROGRESS
priority: high
last_reviewed: 2026-07-19
scope: Exploratory Deliverome-to-GO project focused on delivery-address semantics, internal trafficking model systems, and a human and mouse Rab7 comparison for post-internalization routing
review_sets:
  existing_human_anchors:
    - TFRC
    - CLTC
    - RAB7A
  model_system_reviews:
    - mouse/Rab7
  comparative_reviews:
    - human/RAB7A_vs_mouse/Rab7
  completed_tasks:
    - define_delivery_address_meaning
    - compare_human_RAB7A_mouse_Rab7
    - update_model_system_stance
    - harmonize_RAB7A_core_function_synthesis
    - revisit_mouse_Rab7_SynGO_annotations
  pending_tasks:
    - build_GO_derived_human_surfaceome_prior
    - select_small_delivery_address_pilot_set
    - draft_GO_CAM_like_delivery_route_template
sidecars:
  notes: DELIVEROME.md
external_sources:
  - https://deliverome.org/
  - https://ifp.org/the-deliverome-project/
  - https://deliverome.org/platform/
  - https://deliverome.org/platform/progress/
  - https://geneontology.org/docs/go-annotations/
---

# Deliverome GO Collaboration

## Overview

The Deliverome Project proposes an open atlas of human surface proteins for targeted therapeutic delivery. The public framing emphasizes surface abundance, tissue and cell-type specificity, internalization, downstream trafficking, and functional delivery outcome. This AIGR project tracks two directions:

- how GO could contribute evidence-aware vocabulary, priors, and GO-CAM structure to Deliverome-style data;
- how Deliverome data could contribute back to GO standard annotation and GO-CAMs without mixing endogenous biology with engineered delivery behavior.

This PR keeps the work scoped to project framing plus a human and mouse Rab7 comparison. It does not add a full Deliverome pilot review set.

## What "Delivery Address" Means

By "delivery address" I mean a gene product that therapeutic cargo can use as a molecular address. In practice this is usually an extracellular-facing cell-surface protein with a usable ligand-binding epitope, appropriate tissue or cell-type distribution, and a trafficking route that carries bound cargo toward a useful destination.

The address is not just "present on the membrane." The key questions are whether it internalizes, recycles, routes to lysosomes, transcytoses, or releases cargo productively.

## How GO Could Contribute

GO can provide an evidence-aware prior over plausible human delivery-address proteins before Deliverome-specific measurements are available. Useful filters include cellular-component annotations to cell surface, external side of plasma membrane, plasma membrane, receptor complexes, and endosomal compartments, plus molecular-function or biological-process annotations for receptor activity, endocytosis, transcytosis, and ligand uptake.

GO is also useful as a vocabulary for assay outputs: surface localization, receptor internalization, receptor-mediated endocytosis, recycling, lysosomal routing, transcytosis, and endosome-to-plasma-membrane transport. These terms can support data dictionaries and triage even when a particular engineered-delivery result should not become a canonical GO annotation.

GO-CAMs are especially useful where delivery value depends on a causal route:

1. ligand or cargo binding at the external side of the plasma membrane;
2. receptor internalization;
3. early endosome entry;
4. sorting toward recycling endosome, late endosome, lysosome, transcytosis, or cytosolic escape;
5. downstream endogenous or engineered payload effect.

For normal biology this can become ordinary GO-CAM curation. For engineered therapeutic cargo, the same shape is better treated as a GO-CAM-like Deliverome model outside canonical GO.

## How Deliverome Data Could Contribute To GO

Deliverome data could support standard GO annotations when the assay measures a normal property of the endogenous gene product:

| Deliverome evidence | Potential GO contribution | Curation caution |
| --- | --- | --- |
| Surface proteomics shows endogenous protein at the cell surface | Cellular-component annotations such as cell surface, external side of plasma membrane, or plasma membrane | Require localization specificity; bulk tissue data may need cell-type context |
| Internalization assay shows endogenous receptor uptake | Receptor internalization or receptor-mediated endocytosis | Engineered cargo uptake alone may be a delivery phenotype |
| Trafficking assay tracks the receptor through endosomes or lysosomes | Compartment and routing annotations when the receptor itself is observed | Do not annotate receptor destination if only payload destination was measured |
| Perturbation screen identifies delivery-routing machinery | Review genes for endocytosis, vesicle transport, recycling, lysosome targeting, or transcytosis | Separate direct trafficking machinery from indirect viability or cell-state effects |
| Low-internalization result for an expected receptor | Possible NOT annotation only in narrow cases | Failed delivery is usually not enough for a GO NOT annotation |

## Model Systems

Human and mammalian systems should be primary for delivery-address biology because useful addresses depend on human cell-surface abundance, ligand specificity, glycosylation, expression context, and safety. Good near-term systems are primary or iPSC-derived hepatocytes for ASGR1/ASGR2, polarized endothelial or epithelial barrier systems for FCGRT and TFRC transcytosis, immune and myeloid cells for FcRn and ESCRT/retromer routing, and cancer cell lines or organoids for oncology delivery targets.

Fission yeast (*Schizosaccharomyces pombe*) is useful for machinery-level internal trafficking: conserved endocytosis, ESCRT, retromer, Rab/Ypt, actin-polarity, and vacuolar/lysosomal routing. It is not a good model for human delivery addresses themselves because most address receptors and extracellular ligand-binding systems are metazoan or mammalian.

Mouse is important for pharmacokinetics, immune context, placenta/neonatal Fc receptor biology, in vivo biodistribution, and post-internalization routing. Species differences in receptor expression and ligand affinity still need explicit tracking.

The mouse Rab7/Rab7a review gives this project a concrete internal-routing model. Rab7 is not a delivery-address receptor; it is a late-endosome/lysosome routing switch that helps decide whether internalized cargo proceeds toward degradation, recycling/retrograde sorting, or productive escape. Mouse liver LysoTag/LNP evidence shows that Rab7 loss increases LNP cytosolic escape, making mouse Rab7 useful for "after internalization" questions that cannot be resolved from human surface abundance alone.

The human and mouse comparison is reassuring for GO transfer: both reviews converge on conserved Rab-family GTPase activity, early-to-late endosome maturation, endosome-to-lysosome transport, phagosome/autophagosome fusion, and retromer-dependent retrograde traffic. Human RAB7A remains the stronger disease/genetics anchor, especially for CMT2B, while mouse Rab7/Rab7a is the stronger Deliverome model-system anchor because it connects Rab7-mediated endosomal maturation to in vivo LNP escape.

| Question | Best-fit model systems | Good pilot proteins |
| --- | --- | --- |
| Human address specificity and uptake | Human primary/iPSC/organoid/cell-line panels | ASGR1, ASGR2, SORT1, TFRC, FCGRT |
| Clathrin/AP-2 uptake machinery | Human cells, yeast for conserved principles, fly/worm neurons for specialized uptake | CLTC, AP2M1, DAB2, LDLRAP1 |
| ESCRT/MVB and lysosomal routing | Human cells, pombe/budding yeast, worm and fly for organismal genetics | HGS, RAB7A |
| Retromer and recycling | Human cells, pombe/budding yeast, worm and fly neurons and epithelia | VPS35, RAB11A |
| Barrier/transcytosis delivery | Human BBB/epithelial models, mouse and zebrafish for in vivo context | FCGRT, TFRC |
| Endosomal escape versus degradative routing | Mouse liver LysoTag/LNP assays plus matched human-cell trafficking assays | RAB7A/Rab7a, HGS, VPS35 |

## GO Anchors

| Deliverome concept | Current GO anchor |
| --- | --- |
| Surface localization | GO:0009986 cell surface |
| Extracellular-facing membrane localization | GO:0009897 external side of plasma membrane |
| Plasma membrane localization | GO:0005886 plasma membrane |
| Protein localization to surface | GO:0034394 protein localization to cell surface |
| Internalization | GO:0031623 receptor internalization |
| General endocytosis | GO:0006897 endocytosis |
| Receptor-mediated uptake | GO:0006898 receptor-mediated endocytosis |
| Clathrin-dependent uptake | GO:0072583 clathrin-dependent endocytosis |
| Caveolin-mediated uptake | GO:0072584 caveolin-mediated endocytosis |
| Transcellular routing | GO:0045056 transcytosis |
| Early endosome | GO:0005769 early endosome |
| Late endosome | GO:0005770 late endosome |
| Recycling route | GO:0055037 recycling endosome |
| Lysosomal destination | GO:0005764 lysosome |
| Early-to-late endosome route | GO:0045022 early endosome to late endosome transport |
| Late endosome-to-lysosome route | GO:1902774 late endosome to lysosome transport |
| Recycling to surface | GO:0099638 endosome to plasma membrane protein transport |

## Open Questions

- What evidence threshold should Deliverome surface proteomics meet before it supports a GO cellular-component annotation?
- Can Deliverome metadata map cleanly to ECO evidence, CL/UBERON context, and GO-CAM activity units?
- How should engineered cargo and disease-state measurements be represented without polluting GO's normal-function semantics?
- Which surfaceome targets have enough literature today to build high-quality GO-CAMs before Deliverome data are released?
- Should AIGR add a reusable delivery-route summary parallel to `core_functions`?

---

# STATUS

## 2026-07-19

- [x] Create focused Deliverome project document.
- [x] Define delivery-address meaning.
- [x] Record model-system stance, including pombe for conserved internal trafficking and mouse Rab7/Rab7a for in vivo post-internalization routing.
- [x] Compare human RAB7A and mouse Rab7/Rab7a.
- [x] Harmonize human RAB7A core-function synthesis with mouse Rab7/Rab7a for early-to-late endosome maturation, late endosome membrane localization, and retromer binding.
- [x] Revisit mouse SynGO AMPA-receptor trafficking annotations from PMID:24217640.
- [ ] Build GO-derived human surfaceome prior.
- [ ] Select a small delivery-address pilot set.
- [ ] Draft a GO-CAM-like delivery route template.

# NOTES

## 2026-07-19

- Mouse Rab7/Rab7a is the best current model-system anchor for Deliverome's endosomal routing question: it provides in vivo evidence that Rab7-mediated late endosomal maturation can suppress LNP cytosolic escape by routing cargo toward degradative compartments.
- Human RAB7A and mouse Rab7/Rab7a should be kept aligned on conserved core terms, while using human for disease genetics and mouse for tissue and in vivo delivery physiology.
- The SynGO annotations from PMID:24217640 support AMPA-receptor movement toward late endosomal/lysosomal compartments during LTD, but the accessible paper text emphasizes stargazin/AP-2/AP-3A rather than Rab7 itself. These rows are retained only as non-core neuronal-context annotations, not as primary Rab7 biology.
