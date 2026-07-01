---
title: "Genome-wide validation: system-level plausibility of annotation sets"
maturity: SCOPING
tags: [PIPELINE]
autolink_gene_symbols: false
---

# Genome-wide validation

**Per-gene review asks "is *this* annotation right?" Genome-wide validation asks a question no
single annotation can answer: could the *whole set* of functions annotated to an organism
actually coexist in a living cell? We score a genome's annotation set against system-level
constraints — every essential function present (completeness), every functional dependency
satisfied (coherence), and no mutually exclusive functions co-occurring (consistency) — and
turn each violation into a specific, reviewable curation lead.**

## Bottom line

- **A new validation altitude.** Existing repo QC works one gene, one term at a time. This
  project validates the *annotation set of an entire genome/proteome* as a system, catching
  errors that are invisible per-protein (a pathway missing its committed step; a function that
  can't belong to this organism's lineage).
- **Constraints already encoded in GO, not hand-authored rules.** Completeness draws on
  minimal-genome essential-function sets; coherence reuses GO `has_part` (RO:0000051) axioms
  and MetaCyc pathway structure; consistency reuses GO taxon constraints (`only_in_taxon` /
  `never_in_taxon`). The validator is a reasoner over existing axioms, so it scales across
  genomes without per-organism curation.
- **Sharpest as a predictor QC.** Curated model-organism annotations largely satisfy these
  constraints; genome-scale *computational predictions* systematically violate them. That makes
  this a natural, cheap screen over the prediction-set work already in this repo.
- **Every violation is a lead, not just a score.** A missing coherence dependency points at a
  specific unannotated step; a taxon-constraint violation flags a specific over-propagated
  annotation — output a reviewer can act on, in the same spirit as
  [Pathway satisfiability](PATHWAY_SATISFIABILITY.md).

## Why genome-scale

GO annotation, prediction, and evaluation are overwhelmingly *reductionist*: they assign and
score functions one protein at a time, treating each annotation as an independent fact. But an
organism is not a random bag of proteins — it is an evolved system with functional
requirements and constraints. A prediction method can be accurate per-protein yet produce a
genome-scale annotation set that could not describe any viable organism (missing DNA
replication; a late pathway step with no upstream enzymes; photosynthesis and neuron
development in the same genome).

This gap is the motivation of Tawfiq, Kulmanov & Hoehndorf (2026), whose completeness /
coherence / consistency framework (GAEF) we adopt and extend here, and it is the same gap that
[Pathway satisfiability](PATHWAY_SATISFIABILITY.md) attacks on the eukaryotic, context-resolved
side. Genome-wide validation is the umbrella that generalizes both to a genome-scale QC pass.

## The three criteria

| Criterion | Question | Axiom source | A violation means |
|---|---|---|---|
| **Completeness** | Are functions essential for life present? | minimal-genome essential-function set (mapped to GO) | the genome lacks a process no viable cell can omit — likely an annotation gap |
| **Coherence** | Are functional dependencies satisfied? | GO `has_part` (RO:0000051) + MetaCyc pathway structure | a step/function is annotated but a required part/precursor is annotated nowhere in the genome |
| **Consistency** | Are mutually exclusive functions absent together? | GO `in_taxon` / `only_in_taxon` / `never_in_taxon` constraints | two functions restricted to disjoint lineages are annotated to one genome — an over-propagation |

Each has a **protein-level** form (both functions on one protein) and a **genome-level** form
(the dependent/exclusive function anywhere in the proteome); GO's true-path rule already
enforces the protein-level coherence, so the novel signal is genome-level.

**Presence ≠ flux / capacity.** As in Pathway satisfiability, presence is used asymmetrically:
absence of a required part is strong evidence of a gap; presence only permits a route. A
"complete and coherent" genome is a necessary, not sufficient, condition for viability.

## How it connects to existing work

This project is an umbrella; it should reuse and link, not re-implement:

- [Pathway satisfiability](PATHWAY_SATISFIABILITY.md) — the module-logic engine
  (`src/ai_gene_review/module_logic.py`) that already tests pathway coherence and emits
  abduction leads. Genome-wide coherence is this engine run over *all* pathway/`has_part`
  dependencies for a genome rather than a single curated module.
- [Metabolic Model Analysis](METABOLIC_MODEL_ANALYSIS.md) — GEM gene-protein-reaction
  associations as an independent EC/MF validation source; a complementary, quantitative
  coherence check.
- [Validating E. coli predictions](VALIDATING_ECOLI_PREDICTIONS.md) — the per-prediction
  validity taxonomy this framework screens *in bulk* at genome scale.
- [Reactome gap filling](REACTOME_GAP_FILLING.md) — pathway-hole reasoning that overlaps with
  the coherence "missing required part" signal.

## Pilots

Start bacterial, where the constraints are strongest and the gold standard is cleanest; the
engine is organism-agnostic.

1. **E. coli K-12 (gold standard) — [Pilot 1, first result](GENOME_WIDE_VALIDATION/pilot-ecoli/README.md).**
   Coherence implemented end-to-end on the EcoCyc GAF using GO `has_part` axioms:
   **86.8% coherence**, and the 17 violations triage into a genuine biological gap
   (denitrification lacking nitrous-oxide reductase), annotation-granularity gaps (complex /
   MF sub-terms), and probable over-annotations (eukaryote/viral terms on E. coli) — every one
   a reviewable lead. Runs from public data; see the pilot README and its `RESULTS.md`.
2. **A minimal genome (JCVI syn3.0 / *Mycoplasma*).** Small, tractable, and the natural source
   of the completeness essential-function set — a strong signal for completeness/coherence.
3. **Predictor sweep.** Run one or more genome-scale prediction sets (e.g. InterPro2GO,
   DeepGO-family) through the same criteria and quantify the curated-vs-predicted gap.

## Plan (scoping)

- [x] Extract the dependency set (asserted GO `has_part` pairs) and score a genome's GAF for
      coherence — done in [Pilot 1](GENOME_WIDE_VALIDATION/pilot-ecoli/README.md). *Next:* add
      ELK/relation-graph inferred pairs and the MetaCyc-derived pathway routes.
- [ ] Define the essential-function set from a minimal genome and map to GO classes.
- [ ] Score a whole genome's annotation set for completeness / consistency too (coherence done);
      emit per-genome scores + per-violation leads.
- [x] Run the E. coli coherence pilot; sanity-check against expectations (86.8% coherence,
      violations interpretable). *Next:* the minimal-genome pilot.
- [ ] Feed violations back as curation leads / prediction-review inputs.
- [ ] Decide whether to interoperate with or reproduce GAEF
      (github.com/bio-ontology-research-group/GAEF) rather than reimplement.

## Open questions

- **Axiom coverage.** GO `has_part` between processes is sparse and unevenly curated — a
  coherence "failure" can be a real gap *or* a missing axiom. How do we separate the two
  (cross-check with sequence-level tools like GapMind / Pathway Tools before calling a gap)?
- **Annotation gap vs biological gap.** A set-based check never looks at sequence, so it cannot
  by itself distinguish "gene absent" from "gene present but unannotated." Which follow-up
  (BLAST/HMM step search) resolves flagged coherence gaps?
- **Taxon scope.** The three criteria are cleanest for free-living bacteria/archaea/eukaryotes;
  how far do they hold for obligate symbionts, reduced genomes, and community-dependent
  auxotrophs?

## References

- Tawfiq R, Kulmanov M, Hoehndorf R. *Evaluating completeness, coherence, and consistency of
  genome-scale function annotations.* Briefings in Bioinformatics, 2026, 27(3):bbag336.
  [doi:10.1093/bib/bbag336](https://doi.org/10.1093/bib/bbag336). Software (GAEF):
  <https://github.com/bio-ontology-research-group/GAEF>.
