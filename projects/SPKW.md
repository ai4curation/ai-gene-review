# SwissProt Keywords (SP KW) Unique Terms Project

## Overview

This project focuses on reviewing genes that have unique or unusual SwissProt Keyword (SP KW) terms. These keywords often highlight specialized functions that may require careful curation to ensure GO annotations properly capture the biology.

## Goals

1. Review genes with unique SP KW terms to ensure GO annotations are complete and accurate
2. Identify cases where GO terms may be missing or over-annotated relative to UniProt keywords
3. Propose new GO terms where gaps exist

## Tasks

### Phase 1: Initial Gene Set

- [x] Review human MAP3K5 - COMPLETE (Dec 23)
- [x] Review human PHF23 - COMPLETE (Dec 23)
- [~] Review human SIRT2 - IN PROGRESS (Dec 23)

## Status

Started: 2025-12-23
- MAP3K5: Complete
- PHF23: Complete (DRAFT status) - negative regulator of autophagy via LRSAM1 degradation
- SIRT2: In progress - passes validation with warnings, needs supporting_text additions

## Notes

**Selection criteria:**
- Genes with SP KW terms that are rare or unique across the proteome
- Focus on keywords that suggest specialized molecular functions or biological processes

**Gene-specific notes:**

- **MAP3K5**: Review completed Dec 23
- **PHF23**: Review completed Dec 23 - core function is negative regulation of autophagy through promoting ubiquitination and degradation of LRSAM1. PHD zinc finger domain mediates protein interactions.
- **SIRT2**: Review in progress Dec 23 - NAD-dependent protein deacetylase and demyristoylase. Core functions include histone deacetylation (H4K16), tubulin deacetylation, and cell cycle regulation. Also has efficient demyristoylase activity. Review has 170+ existing annotations covering multiple evidence types. Remaining work: add supporting_text to reference findings.
