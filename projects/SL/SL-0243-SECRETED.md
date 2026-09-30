---
title: "SL-0243 Secreted"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, yeast, ACET2, DESRO, METEA, PSEPK, SALTY, STAAU]
autolink_gene_symbols: false
---

# SL-0243 Secreted → GO:0005576

89 SL-unique annotations reviewed, **13 with a hard issue (15%)** — the largest location
outside the generic ones. Unlike [SL-0162](SL-0162-MEMBRANE.md) and
[SL-0090](SL-0090-CYTOSKELETON.md), granularity is only part of the story here. This location
exposes a **third failure mode**, and it is the one with the clearest fix.

## Pattern C — family-rule and sequence-feature propagation

Where the two other subprojects find terms that are true-but-vague, SL-0243 finds terms that
are **false for this organism** because a location true of some family members was attached to
the whole family by rule:

> **PSEPK eno** — "The HAMAP rule MF_00318 attaches Secreted/Cell surface locations to all
> family members because enolase moonlights as a surface plasminogen-binding protein in
> numerous pathogens. There is no experimental evidence that the *P. putida* KT2440 enolase is
> secreted."
>
> **METEA eno** — "a rule-propagated moonlighting annotation with no organism-specific support
> in AM1 … recommends against transferring pathogen-derived surface/secreted enolase
> localization to this non-pathogenic methylotroph."
>
> **yeast THI22** — "Pure prediction from a signal-peptide/SubCell mapping, not experimental.
> THI22's paralogs THI20/THI21 function in the cytosol, and there is no evidence THI22 is
> secreted."
>
> **human PGRMC1** — `REMOVE`. "No biological evidence supports a free extracellular pool of
> PGRMC1; the protein is membrane-anchored throughout its life cycle. Annotation appears to be
> a SwissProt-keyword automation artefact."

This is exactly SPKW's "subclade divergence" pattern (family keyword ignores
subfunctionalisation), transplanted from the process branch to the component branch. The
enolase pair is the textbook case: a genuine moonlighting surface localization in pathogens,
propagated by a HAMAP rule to a soil bacterium and a methylotroph where nothing supports it.

**Why this matters more than the granularity cases.** Under-specification produces annotations
that are useless. Rule propagation produces annotations that are *wrong*, and wrong in a way
that is invisible to any structural check — the term is specific, the mapping is correct, and
the only thing at fault is the taxonomic scope of the source rule.

## Pattern D — secreted is the wrong frame for the biology

Three cases where "extracellular region" is defensible on the letter and misleading in
substance:

- **SALTY slrP** — "UniProt 'Secreted' keyword mapping is imprecise for a T3SS effector that
  is directly delivered into host cells. The supported functional locations are host cell
  cytoplasm and host cell endoplasmic reticulum."
- **STAAU lytN** — "technically defensible but uninformative and partly misleading for a
  cross-wall enzyme. Frankel et al. showed externally added purified LytN does not complement
  a *lytN* mutant."
- **ACET2 P71143 (SdbA)** — "tethered to the cell surface via its three SLH domains … The
  protein does not freely diffuse."

A protein that transits the secretory pathway to reach a tethered, injected, or wall-embedded
destination gets "Secreted", and the GO mapping turns that into "extracellular region". The
transit is being annotated instead of the destination.

## Pattern A also present

The remaining flags are ordinary under-specification: ACET2 celK and celS should be
GO:0043263 cellulosome; DESRO K9IWR0 and K9J2R0 should be GO:0005615 extracellular space;
human MUC1 should be extracellular space, "already annotated with experimental evidence (HDA)".

## Proposed action

Unlike the granularity subprojects, this one has a targeted intervention that would work:
**audit the small number of family rules that attach `Secreted` or `Cell surface` to
housekeeping enzyme families.** HAMAP MF_00318 (enolase) alone accounts for two of the 13
flags in this corpus and would account for far more at GOA scale — enolase is universal.

No annotations were changed under this subproject; all 13 had already been flagged by prior
reviews. The value here is the pattern, not new verdicts.
