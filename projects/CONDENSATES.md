---
title: "Biomolecular Condensates"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, worm, SCHPO, mouse]
genes: [SQSTM1, NFE2L2, LGALS3, TARDBP, TP53, pgl-1, pgl-2, pgl-3, meg-2, meg-3, meg-4, mid1, Ccnt1]
---

# Biomolecular Condensates

Membraneless compartments — stress granules, P granules, P-bodies, the nucleolus, PML
bodies, nuclear speckles, the phagophore assembly site — are among the most heavily
annotated structures in this corpus and among the least *informatively* annotated. This
project is the cross-cutting home for that problem: it does not own a condensate, it owns
the curation question that every condensate raises.

That question is simple to state. **Being in a condensate is a location. Making one is a
function.** GO annotation, and this repository along with it, records the first almost
exclusively and the second almost never.

## The state of the corpus

A scan of every `*-goa.tsv` and `*-ai-review.yaml` in the repository (see the
[GO and annotation audit](CONDENSATES/CONDENSATES-go-audit.md), regenerable from a
committed script) gives the shape of the problem:

| | Count |
|---|---|
| Gene folders carrying at least one condensate-space CC term | 238 |
| Reviewed condensate-space annotations | 399 |
| Gene folders with `GO:0005730` nucleolus | 89 |
| Gene folders with `GO:0140693` molecular condensate scaffold activity (MF) | 9 |
| Gene folders with `GO:0140694` membraneless organelle assembly (BP) | 1 |

Eighty-nine genes are placed *in* the nucleolus; nine genes in the entire corpus are said
to *scaffold* any condensate at all. The asymmetry is not a curation backlog — it reflects
GO's own shape, where the compartments are richly subdivided and the activities that build
them are represented by a single molecular-function term.

Reviewers have already registered their discomfort without being asked to. Of 399 reviewed
condensate-space annotations, **146 (37%) were downgraded or worse** — 121
`KEEP_AS_NON_CORE`, 17 `MARK_AS_OVER_ANNOTATED`, 8 `REMOVE`. Nucleolus alone accounts for
45 non-core, 9 over-annotated, and 3 removed. That is a consistent, repository-wide signal
that condensate localization, taken alone, is being judged uninformative about function —
gene by gene, with no shared framework behind it. Supplying that framework is what this
project is for.

## Three ontology problems

**1. GO has no class for "biomolecular condensate."** The nearest candidate,
`GO:0043228` membraneless organelle, cannot serve: the ribosome (`GO:0005840`) and the
cytoskeleton (`GO:0005856`) are both descendants of it. Neither is a phase-separated
condensate. So there is no term that picks out the set this project is about, and no way
to ask "which of my genes are condensate proteins?" without a hand-curated list — which is
exactly what the audit script has to maintain.

**2. Condensates that are not classified as such.** `GO:0000407` phagophore assembly site
is *not* under membraneless organelle, though the PAS was shown in 2020 to be a liquid-like
Atg-protein condensate ([PMID:32025038](https://pubmed.ncbi.nlm.nih.gov/32025038/)). The
inverse error to problem 1: a real condensate sitting outside the grouping. See
`MODULE:phagophore_assembly_site`, which models it as one.

**3. Terms that assume a membrane the structure does not have.** `GO:0034045` phagophore
assembly site membrane defines "a cellular membrane associated with the phagophore assembly
site" — but the PAS is a condensate, and the term additionally carries *phagophore* and
*isolation membrane* as related synonyms, which are the name and synonym of the separate
term `GO:0061908`. Two cellular components, the same two strings. Recorded in full as a
knowledge gap on the PAS module.

## Working principles

These are the commitments this project proposes; they are drafts until tested against a
batch.

1. **Scaffold, client, or regulator — say which.** A protein that phase-separates and
   nucleates the compartment (`GO:0140693`) is doing something categorically different from
   one that partitions into it. Reviews should decide which, and say so in
   `core_functions`, not leave a bare CC term to imply it.
2. **Condensate CC alone is rarely a core function.** The corpus already behaves this way
   (37% downgraded). Make it explicit rather than rediscovered per gene.
3. **Prefer the material claim over the compartment claim.** "Drives phase separation of X"
   is checkable; "localizes to structure Y" often reflects a fixation artefact or an
   overexpression phenotype.
4. **Demand condensate-grade evidence.** In-vitro droplet formation at non-physiological
   protein or salt concentrations, and puncta in overexpressing cells, are weaker than FRAP
   recovery, 1,6-hexanediol sensitivity with controls, and endogenous-tag imaging. Flag the
   distinction in `review.reason`.
5. **Model condensates as modules, not just locations.** A condensate has composition,
   assembly, and disassembly. `MODULE:phagophore_assembly_site` is the first worked example
   in this repository.

## Existing assets

| Asset | Kind | Status |
|---|---|---|
| [CAEEL_P_GRANULES](CAEEL_P_GRANULES.md) | per-condensate project (worm germ granules) | `IN_PROGRESS`; pgl-1, pgl-2, pgl-3, glh-1, meg-2, meg-3, meg-4 reviewed with no PENDING or UNDECIDED annotations |
| [STRESS_GRANULES](STRESS_GRANULES.md) | per-condensate project (human SGs) | `SCOPING`; self-described stub, 5 of ~12 candidates have gene folders |
| `MODULE:phagophore_assembly_site` | module | `DRAFT`; the corpus's only condensate modeled as a module |
| `projects/CONDENSATES/scripts/scan_condensate_annotations.py` | audit script | regenerates every number on this page |

### Relationship to the per-condensate projects

STRESS_GRANULES and CAEEL_P_GRANULES stay standalone; they are not folded in as sub-pages.
Each is a domain project with its own species scope, gene list, and disease framing, in the
same mould as PEROXISOME or ER_PHAGY, and CAEEL_P_GRANULES is already in progress with
reviewed genes — absorbing it would bury finished work and break its index entry. This page
is the cross-cutting layer above them: shared principles, shared ontology issues, and the
corpus-wide audit that no single condensate project would produce.

The P-granule work is also the methodological precedent worth generalising. It is the only
place in the corpus where curators asserted `GO:0140693` as a **new** annotation rather than
accepting an existing one — meg-2, meg-3, meg-4, and pgl-2 all carry `NEW`, four of the five
`NEW` scaffold annotations in the repository. That is principle 1 already being applied,
before it was written down.

## Proposed first batch

Genes that already carry `GO:0140693` are the natural calibration set: small, cross-species,
and already reviewed, so the batch tests the principles rather than the pipeline.

- **SQSTM1** — six scaffold annotations, five IDA, all `ACCEPT`; also the corpus's only
  `GO:0140694` gene. The best-supported scaffold in the repository and the reference case.
- **NFE2L2**, **LGALS3** — IDA scaffold annotations, `ACCEPT`; test whether the evidence
  meets principle 4.
- **TP53** and its orthologues — the mouse and rat orthologues were reviewed
  `KEEP_AS_NON_CORE` and `MARK_AS_OVER_ANNOTATED` respectively, both on ISS/ISO. A live
  disagreement about whether a scaffold function propagates by similarity at all.
- **Ccnt1**, **mid1** — non-human scaffold annotations; check taxon-appropriateness.
- **TARDBP** — heavily condensate-associated and disease-relevant, and a bridge to
  STRESS_GRANULES.

## Open questions

- Should `GO:0140693` have children distinguishing homotypic self-assembly from
  heterotypic client recruitment? Nine genes is too few to tell; the batch should decide.
- Is a "biomolecular condensate" CC grouping class worth requesting, given that the
  membrane/no-membrane axis already exists and cuts differently?
- What is the minimum evidence standard for a scaffold assertion, and should reviews record
  it structurally (e.g. as a knowledge-gap `boundary`) rather than in prose?
- Do IEA/ISS/ISO scaffold annotations survive scrutiny anywhere? Of the 22 in the corpus, 8
  are non-experimental and they account for every non-`ACCEPT` outcome.
