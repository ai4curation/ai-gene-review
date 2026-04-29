# Prokaryotic Immunity Term Prediction

## Overview

This project is about increasing automation for predicting precise biology-first GO terms for
prokaryotic immunity systems.

The immediate unit here does not try to solve end-to-end annotation. It adds the missing translation
layer between broad defense-system calls and review-ready term suggestions. In practice, the current
source being translated is family-level output from the prokaryotic immunity predictor, which emits
calls such as `CRISPR-Cas`, `restriction-modification`, `CBASS`, `Thoeris`, and `abortive infection`.

The goal is to make those outputs usable for precise review by:

- assigning stable internal family IDs
- normalizing family labels and aliases
- attaching explicit GO mapping policy per family
- separating families that are safe to map automatically from families that still require curator review

This keeps immunity-term prediction centered on the biology while still allowing multiple upstream
tools or predictors to plug into the same GO policy layer later.

## Why This Exists

The current predictor can often say that something belongs to a broad defense family, but broad
family labels are not yet a good direct input to GO curation.

There are three different problems mixed together if we do not separate the layers:

1. Family recognition
2. Stable immunity-system identity and synonym handling
3. Precise term-prediction policy

Those should not live as ad hoc conditionals inside one particular predictor or one particular
database parser.

This project creates an extraction-ready translation layer in `src/ai_gene_review/defense_go/` that
owns the second and third layers.

## Design

The current term-prediction layer consists of:

- `src/ai_gene_review/defense_go/models.py`
  Typed models for defense families, incoming family predictions, and GO mapping suggestions
- `src/ai_gene_review/defense_go/registry.yaml`
  Versioned source-of-truth registry for stable family IDs, aliases, GO mappings, and review notes
- `src/ai_gene_review/defense_go/registry.py`
  Loader and resolver for the registry
- `tests/test_defense_go.py`
  Focused tests for alias resolution, automatic mappings, unmapped families, and registry safety

The API is intentionally narrow:

- an upstream tool emits a family label plus optional confidence
- the translation layer resolves that to a stable family record
- it returns either:
  - automatic GO suggestions, or
  - review-only notes saying why automatic mapping is not yet allowed

Today, the intended upstream source is the prokaryotic immunity predictor branch. Later, the same
layer could absorb outputs from DefenseFinder, PADLOC, CasFinder, or additional learned models
without changing the downstream GO policy interface.

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

This project does not yet wire the term-prediction layer into the prokaryotic immunity predictor
branch. That is intentional.

The intended integration path is:

1. Predictor emits normalized family calls and confidence
2. `ai_gene_review.defense_go.wrap_prediction(...)` resolves them to stable IDs and mapping policy
3. AIGR export code turns automatic mappings into review-ready term suggestions
4. Review-only families remain visible to curators with explicit notes instead of silent omission

Keeping those steps separate makes the project biology-first while still leaving room to support
multiple upstream predictors and databases later.

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
