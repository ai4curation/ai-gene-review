# IL1B review notes

## 2026-11-22 setup

- Issue handoff: human IL1B/P01584 is the remaining unreviewed ligand in the IL-1 signaling module.
- Regenerated inputs with `just fetch-gene human IL1B`.
  - Seeded 184 GOA annotations in `IL1B-ai-review.yaml`.
  - Cached UniProt and GOA snapshots in the IL1B gene folder.
- Cached all 56 GOA-cited PMIDs with `just fetch-gene-pmids human IL1B`.
- Tried generated deep research with Falcon, Perplexity Lite fallback, and Claude Code. All configured providers failed in this environment, so this review will use cached GOA references, UniProt, module/GO-CAM context, and manually recorded notes rather than a `IL1B-deep-research-*.md` file.

## Core review constraints

- Mature IL-1 beta is an extracellular IL-1 receptor agonist/cytokine. The 31 kDa cytosolic precursor is inactive until proteolytic processing; cached PMID:2950091 states that the IL-1 beta translation product must be processed before receptor binding, and cached PMID:1919436 supports chymase-mediated conversion of the precursor to an 18 kDa active species.
- CASP1 and microbial SpeB can process pro-IL-1 beta, but IL1B is the substrate, not the protease. `modules/il1_signaling.yaml` treats IL-1 beta maturation and GSDMD-pore release as an upstream optional submodule supplying mature IL-1 beta to IL1R1/IL1RAP signaling.
- The IL1beta GO-CAM review (`gocams/59cc772c00000000/59cc772c00000000-review.yaml`) accepts the IL1B terminal cytokine node but flags the direct CASP1-to-extracellular-IL1B edge as missing a GSDMD secretion step.
- The NLRP3 GO-CAM review (`gocams/635b1e3e00001811/635b1e3e00001811-review.yaml`) records the preferred bridge: cytosolic CASP1 cleavage is separate from GSDMD pore-mediated release of mature IL-1 beta.

## Cached full text

Full text is cached for these IL1B GOA-cited references:

- PMID:12483741
- PMID:15899045
- PMID:19032770
- PMID:19524870
- PMID:19593445
- PMID:20018408
- PMID:20027291
- PMID:20041150
- PMID:21559518
- PMID:25816133
- PMID:26020802
- PMID:26687115
- PMID:28331908
- PMID:28720735
- PMID:32719155
- PMID:33246504
- PMID:33883744

Most single-assay downstream-output references are abstract-only in the local cache. Those rows need conservative actions: keep established IL-1 beta outputs when the abstract is enough to identify the direct cytokine perturbation, but use `UNDECIDED` when the cached title/abstract cannot verify that IL1B itself was assayed.

## Citation defects

- PMID:28720735 resolves to an *Aspergillus fumigatus* PptA/phosphopantetheinyl-transferase paper, not an IL1B cytokine paper. Its two PHI-base TAS rows were removed, structured `WRONG_REFERENCE` source defects were recorded, and the top-level reference was marked `WRONG_IDENTIFIER`.
- PMID:19593445 is a BAD/prostate-cancer paper with no IL1B mechanical-response evidence. The UniProt IEP row was removed, a structured `WRONG_REFERENCE` source defect was recorded, and the top-level reference was marked `WRONG_IDENTIFIER`.
- PMID:26753638 is a TNF/mast-cell neuroinflammation review. Its generic mention of IL-1 release is not enough to establish IL1B-positive regulation of neuroinflammation, so the TAS row was downgraded to `MARK_AS_OVER_ANNOTATED` with a `CHECK` source defect.

## Review follow-up

- Parent/child action inversions were resolved after the first PR review: LPS response, positive regulation of proliferation, and Gram-positive defense were kept as non-core, while generic IL-1 response, NF-kappaB regulation, and ERK regulation were converted to `MODIFY` rows pointing to the more specific child terms that IL1B already carries.
- The remaining `MARK_AS_OVER_ANNOTATED` rows were split by evidence cluster rather than sharing one target-cell boilerplate reason. The adipocyte metabolic transfers from PMID:16865359, neural/synaptic transfers, barrier and junction rows, oral-cancer invasion rows, and other isolated target-cell outputs now state why each assertion is narrower, directionally inconsistent, or less direct than mature IL-1 beta cytokine activity.
