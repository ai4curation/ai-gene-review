---
title: "microTrait Framework Integration"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, PIPELINE]
---

# microTrait Framework Integration

**Project type:** Rule review — incorporate microTrait's HMM→trait rules as first-class
reviewable rules alongside UniRule/ARBA.
**Status:** Scoped; enabling schema change landed. **Blocked on input data from Ulas**
(the rule table), then rule review begins. See the
[rule-review plan](MICROTRAIT/microtrait-rule-review-plan.md).

## Direction (decided)

- **First deliverable: microTrait rule review** — treat each microTrait rule like a
  UniRule/ARBA rule and assess it for GO-annotation quality. This angle reuses the most
  existing tooling (`rules/`, the `RuleReview` schema class, the rule-review templates).
- **Data source: files provided by Ulas** — the curated rule table (HMM/gene → trait
  predicate logic) rather than scraping the public repo's packaged HMM DB. See the plan
  doc for the exact input format needed.
- The **trait → GO crosswalk emerges as a byproduct**: reviewing a rule requires judging
  which GO term(s) its asserted trait corresponds to, so each review records that mapping.

## Schema enablement (done)

`RuleReview` previously only recognized `ARBA`/`UNIRULE`. Two additive enum values now make
microTrait rules first-class (`src/ai_gene_review/schema/gene_review.yaml` + regenerated
datamodel):

- `RuleTypeEnum.MICROTRAIT` — a microTrait rule.
- `ConditionTypeEnum.HMM` — a profile-HMM presence/absence condition (use `negated` for
  absence). microTrait antecedents are HMM/gene presence logic, not InterPro/FunFam domains.

A microTrait `RuleReview` object therefore constructs and validates today; only the rule
*content* awaits Ulas's table.

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

## Phased plan

- **Phase 0 — scope + schema enablement.** ✅ Done (this page; `MICROTRAIT`/`HMM` enum values).
- **Phase 1 — ingest Ulas's rule table.** ⏳ *Blocked on input.* Convert the provided rule
  table into per-rule `RuleReview` YAML stubs under `rules/microtrait/<rule_id>/`. Format
  and workflow specified in the [rule-review plan](MICROTRAIT/microtrait-rule-review-plan.md).
- **Phase 2 — review rules.** For each rule, assess the HMM logic, the asserted trait, the
  GO term the trait maps to, and the appropriate `action`. The trait→GO mappings recorded
  here accumulate into a reusable crosswalk (byproduct).
- **Phase 3 — exemplar gene reviews (optional follow-on).** Use reviewed trait context as a
  prior when curating microbial exemplar genes.

## Open item — CAZy overlap

microTrait bundles dbCAN CAZy HMMs, and this repo already has a curated `cazy2go` mapping in
`projects/GLYCOBIOLOGY`. Any microTrait rule whose logic rests on CAZy families must
**reuse `cazy2go` for its trait→GO judgment rather than re-deriving it**, so the two do not
diverge. The plan doc records this as a hard constraint on CAZy-based rules.

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
