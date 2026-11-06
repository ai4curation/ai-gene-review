# Hsero_1011 notes

## 2026-11-04 session (Claude, AI-assisted)

- Fetched with `just fetch-gene HERSS <accession> --alias Hsero_1011`: the gene-name lookup
  failed because the UniProt stream endpoint returned 503, so the accession route was used.
- No provider deep-research file was generated (no provider API keys in this session).
  The review rests on the UniProt record, the cached pathway papers
  [PMID:27059806] (abstract only) and, for fdeE, [PMID:39107441] (full text), the
  KEGG queries in `genes/HERSS/Hsero_1007/Hsero_1007-bioinformatics/`, and the P.
  putida ortholog reviews (PSEPK PP_3195-PP_3206) with their committed alignments.
- Literature search (PubMed E-utilities, 2026-11-04): "naringenin Herbaspirillum"
  (13 hits), "fdeE naringenin" (2: PMID:27059806, PMID:39107441), "Hsero_1007"
  (1: PMID:27059806). Pathway-relevant hits cached: PMID:23125118 (fde operon induced
  by naringenin; fdeA and fdeR mutants cannot degrade naringenin), PMID:27059806
  (fdeE, fdeC, fdeG mutants), PMID:27878922 (FdeR activator), PMID:39107441 (purified
  FdeE). Only FdeE has been assayed biochemically; only fdeA, fdeC, fdeE, fdeG and fdeR
  have been mutated.
- Context: written for the module `modules/bacterial_flavonoid_degradation.yaml`.

## 2026-11-06 — comparative fde audit

Read the 2013 full paper through its author-uploaded copy; its fdeA mutation is probably polar. Preserve the distinction between locus-level inference and exact catalytic assignment. See modules/bacterial_flavonoid_degradation-notes.md for source access and comparative boundaries.

## 2026-11-06 — late-component participation reassessment

The inherited GO:0046275 proposal is withdrawn and explicitly `retired: true`: the FAH fold supports multiple reaction classes, while the proposed R13078/R13079 transformations are untested. Locus induction, whole-operon phenotypes and similarity to another unassayed candidate do not establish this product's individual step. Original source fields and row position are preserved; retirement records curator withdrawal, not an upstream GOA disappearance. The former process-only core block is removed, and the unresolved role remains a knowledge gap. The same-role BRADU comparator bll6422 likewise asserts no process annotation. See `analysis/module_audits/bacterial_flavonoid_degradation/round1-source-review.md`.
