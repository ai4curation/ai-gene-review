---
title: "microTrait Framework Integration"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, PIPELINE]
---

# microTrait Framework Integration

**Project type:** Scoping — evaluate incorporating the microTrait trait framework as a
resource for microbial gene annotation review.
**Status:** Scoping. No data pulled yet; this page proposes how (and whether) to integrate.

## What microTrait is

**microTrait** ([ukaraoz/microtrait](https://github.com/ukaraoz/microtrait); Karaoz &
Brodie, *"microTrait: A Toolset for a Trait-Based Representation of Microbial Genomes"*,
*Frontiers in Bioinformatics* 2022, DOI
[10.3389/fbinf.2022.918853](https://doi.org/10.3389/fbinf.2022.918853),
PMC [PMC9580909](https://pmc.ncbi.nlm.nih.gov/articles/PMC9580909/)) is an R package that
translates a microbial genome sequence into a **hierarchical space of ecologically
relevant fitness traits** — energetic, resource-acquisition, resource-use, stress-tolerance,
and composite "life-history" traits.

The pipeline has two curated components that are the relevant assets for this repo:

1. **microTrait-HMM** — a database of gene-level profile HMMs (~170 MB), curated from IMG/M
   and benchmarked against KEGG orthologs with trusted-cutoff (TC) scores; plus the
   **dbCAN** domain HMMs for carbohydrate-active enzymes.
2. **microTrait rules** — a set of rules encoded in **predicate logic (AND/OR over HMM
   presence/absence)** that infer a trait from the detected genetic loci.

Traits are reported at **three granularity levels** (`trait_matrixatgranularity1/2/3`),
with the hierarchy documented in `microtrait-hierarchy.pdf` and the genomic/literature
basis for each trait catalogued in `ST8.microtrait_references.txt`. Output for a genome is
an R object holding detected genes + CAZy domains, `rule_matrix` assertions, the three
trait matrices, and derived estimates (growth rate, optimum growth temperature).

## The integration constraint

The **full pipeline is an R package requiring HMMER + the ~170 MB HMM database**, so
*running genome-scale trait inference* is not a natural fit inside this repo (which curates
GO annotations for individual gene products, not whole genomes).

The tractable, high-value assets are the **static curated artifacts**: the trait
vocabulary/hierarchy and the **HMM → gene → trait rule table**. These map cleanly onto
patterns ai-gene-review already uses. This project scopes incorporating *those*, not the
runtime pipeline.

## Where microTrait plugs into existing patterns

| Integration angle | Existing analogue in this repo | What it would produce |
|---|---|---|
| **Trait → GO crosswalk** | `projects/GLYCOBIOLOGY` cazy2go SSSOM mapping | A mapping from microTrait genes/traits → GO MF/BP terms, so trait assertions become GO-reviewable |
| **HMM → trait rule review** | `rules/` UniRule/ARBA review (predicate-logic condition sets → GO) | Reviewer assessments of microTrait rules for over-/under-annotation against GO guidelines |
| **Trait context as review evidence** | `projects/BGC.md` (cluster context as prior), `projects/ALPHAFOLD.md` (predicted structure as evidence) | Inferred trait membership used as a prior when curating microbial gene annotations |

The strongest structural affinity is with the **rules work**: microTrait rules are
predicate-logic conditions over HMM hits that assert a functional capability — the same
shape as UniRule/ARBA condition sets that this repo already reviews and crosswalks to GO.

## Proposed phased plan

- **Phase 0 (this page).** Scope and decide direction. ← current
- **Phase 1 — inventory the public assets.** Pull the trait hierarchy, rule table, and
  HMM→trait mapping from the public repo; report exact file formats, term counts, and how
  much is directly reusable without running the pipeline. Decide whether the crosswalk or
  the rule-review angle is the better first deliverable.
- **Phase 2 — trait→GO crosswalk (candidate first deliverable).** Author an SSSOM-style
  mapping from microTrait traits/genes to GO terms, mirroring `cazy2go`. This is the
  reusable substrate that later feeds both rule review and trait-guided gene reviews.
- **Phase 3 — exemplar gene reviews.** Pick microbial exemplar genes/organisms where a
  microTrait trait provides useful review context (energetic / stress-tolerance traits with
  clear GO analogues) and curate them, citing the trait basis.

## Open questions for the maintainer

- **Scope:** which of the three angles above is the intended first deliverable? (Rule
  review has the closest existing tooling; the trait→GO crosswalk is the most reusable
  substrate.)
- **Data source:** pull the trait/rule tables directly from the public
  `ukaraoz/microtrait` repo, or work from files provided by Ulas (e.g. a cleaner rules
  spreadsheet or an updated HMM→trait table than what's public)?
- **CAZy overlap:** microTrait already carries dbCAN CAZy HMMs; how should a
  microTrait→GO crosswalk relate to the existing `cazy2go` mapping in
  `projects/GLYCOBIOLOGY` to avoid divergence?

## Caveats

- microTrait traits are **genome-inferred capabilities**, not experimentally verified
  functions — treat a trait assertion as a hypothesis/prior, not evidence, exactly as BGC
  complex predictions and AlphaFold structures are treated.
- The trait vocabulary is **ecology-oriented** (fitness/life-history framing) and does not
  align 1:1 with GO; a crosswalk will be partial and will need curation, not an automatic
  join.
- Trait inference is tuned to soil microbiomes in the source publication; applicability to
  other habitats/lineages should be stated where it matters.

## References

- Karaoz U, Brodie EL. *microTrait: A Toolset for a Trait-Based Representation of Microbial
  Genomes.* Front Bioinform. 2022. DOI
  [10.3389/fbinf.2022.918853](https://doi.org/10.3389/fbinf.2022.918853); PMC
  [PMC9580909](https://pmc.ncbi.nlm.nih.gov/articles/PMC9580909/).
- Source code: [github.com/ukaraoz/microtrait](https://github.com/ukaraoz/microtrait).
