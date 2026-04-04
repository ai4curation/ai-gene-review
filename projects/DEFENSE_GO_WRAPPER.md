# Defense GO Wrapper

## Overview

This project adds a small in-repo translation layer between prokaryotic defense-family prediction
and AIGR/GO curation output.

The immediate goal is not to annotate defense genes automatically end-to-end. The goal is to make
family-level predictions usable in review by:

- assigning stable internal family IDs
- normalizing family labels and aliases
- attaching explicit GO mapping policy per family
- separating families that are safe to map automatically from families that still require curator review

This keeps the prediction pipeline and the GO policy layer decoupled, while still making the two
compose cleanly.

## Why This Exists

The predictor can often say that something is `CRISPR-Cas`, `restriction-modification`, `CBASS`,
`Thoeris`, or `abortive infection`, but those labels are not yet a good direct input to GO curation.

There are three different problems mixed together if we do not separate the layers:

1. Family recognition
2. Stable family identity and synonym handling
3. GO translation policy

Those should not live as ad hoc conditionals inside the predictor.

This project creates an extraction-ready wrapper in `src/ai_gene_review/defense_go/` that owns the
second and third layers.

## Design

The wrapper currently consists of:

- `src/ai_gene_review/defense_go/models.py`
  Typed models for defense families, incoming family predictions, and GO mapping suggestions
- `src/ai_gene_review/defense_go/registry.yaml`
  Versioned source-of-truth registry for stable family IDs, aliases, GO mappings, and review notes
- `src/ai_gene_review/defense_go/registry.py`
  Loader and resolver for the registry
- `tests/test_defense_go.py`
  Focused tests for alias resolution, automatic mappings, unmapped families, and registry safety

The wrapper API is intentionally narrow:

- predictor emits a family label plus optional confidence
- wrapper resolves that to a stable family record
- wrapper returns either:
  - automatic GO suggestions, or
  - review-only notes saying why automatic mapping is not yet allowed

## Initial Stable Family IDs

The first registry version includes:

- `DEFENSE_FAMILY:CRISPR_CAS`
- `DEFENSE_FAMILY:RESTRICTION_MODIFICATION`
- `DEFENSE_FAMILY:ABORTIVE_INFECTION`
- `DEFENSE_FAMILY:CBASS`
- `DEFENSE_FAMILY:THOERIS`

The ID layer is the important part. It gives us a stable target that later tools can consume
without depending on whatever exact family string the predictor or external database emitted.

## Initial GO Policy

The current registry is intentionally conservative.

Families with automatic GO mappings:

- `DEFENSE_FAMILY:CRISPR_CAS`
  Maps to `GO:0099048` `CRISPR-cas system`
- `DEFENSE_FAMILY:RESTRICTION_MODIFICATION`
  Maps to `GO:0009307` `DNA restriction-modification system`

Families currently left unmapped at the automatic layer:

- `DEFENSE_FAMILY:ABORTIVE_INFECTION`
- `DEFENSE_FAMILY:CBASS`
- `DEFENSE_FAMILY:THOERIS`

These remain review-only because the family labels are currently too broad to support reliable,
family-wide automatic GO assignment in this repo.

## Integration Plan

This project does not yet wire the wrapper into the prokaryotic immunity predictor branch. That is
intentional.

The intended integration path is:

1. Predictor emits normalized family calls and confidence
2. `ai_gene_review.defense_go.wrap_prediction(...)` resolves them to stable IDs and mapping policy
3. AIGR export code turns automatic mappings into review-ready term suggestions
4. Review-only families remain visible to curators with explicit notes instead of silent omission

Keeping those steps separate makes later extraction into a standalone repo possible, but does not
force that split now.

## Status

Completed in this unit:

- Added the `defense_go` package
- Added the first versioned registry
- Added alias resolution and conflict detection
- Added targeted tests

Deferred:

- integration into the prokaryotic immunity prediction pipeline branch
- export of wrapper output into `PredictionReview` YAML
- expansion of the registry to more defense families and GO policies
- support for evidence-code policy and provenance payloads

## Validation

- `uv run ruff check src/ai_gene_review/defense_go tests/test_defense_go.py`
- `uv run pytest tests/test_defense_go.py`
