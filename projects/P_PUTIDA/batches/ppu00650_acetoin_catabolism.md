---
title: "PSEPK ppu00650 2,3-butanediol and acetoin catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [bdhA, acoC, acoB, acoA, PP_0556]
autolink_gene_symbols: false
---

# PSEPK ppu00650 2,3-butanediol and acetoin catabolism

- Module: `bacterial_2_3_butanediol_acetoin_catabolism`
- Core locus: PP_0552 through PP_0556
- Batch table: [ppu00650_acetoin_catabolism.tsv](ppu00650_acetoin_catabolism.tsv)

## Boundary

This locus-level batch expands the KEGG ppu00650 assignment of `bdhA` to its
adjacent acetoin-cleaving machinery. `acoC` is separately bucketed by KEGG under
lipoate metabolism, while `acoA`, `acoB`, and PP_0556 were pathway orphans in
the initial partition. The curated reusable module follows the biochemical
system rather than treating those database buckets as biological boundaries.

- BdhA-dependent 2,3-butanediol oxidation is an optional upstream entry.
- AcoA/AcoB E1 cleavage, AcoC E2 acetyl transfer, and E3 lipoyl reoxidation are separate module parts.
- AcoX is unresolved accessory context, not a catalytic module step.
- AcoR regulation and downstream acetaldehyde/acetyl-CoA metabolism are outside the module.
- The KT2440 E3 paralog remains unresolved.

## Evidence and research integration

PMID:7813883 links the P. putida PpG2 dehydrogenase and AcoABC system;
PMID:2061286 establishes the AcoA/AcoB alpha2-beta2 complex and explicitly
states that AcoX function is unknown; PMID:8110297 identifies an AcoL E3 in a
complete cross-taxon acetoin system. Accessions Q59696, Q59695, P27745,
P27746, P27747, P27748, and Q60154 were checked against UniProt. The only GOA
PTN in this batch is `PTN002264059`, whose pyruvate-specific AcoA propagation
was corrected. `PTHR43257:SF3` was retained as the verified acetoin-specific
AcoB selector.

The completed OpenScientist artifact inventory was asymmetric: only the acoC
gene report produced a usable artifact. No artifacts were present for the other
four genes, generic module research, or module+pathway+taxon synthesis. Those
research attempts were not restarted; the absence is recorded rather than
represented as completed evidence.

## Genes

| Done | Gene | Locus | UniProt | GOA rows | Curated role |
|---|---|---|---|---:|---|
| [x] | `bdhA` | PP_0552 | Q88QE2 | 4 | optional stereospecific 2,3-butanediol oxidation |
| [x] | `acoC` | PP_0553 | Q88QE1 | 1 | lipoyl E2 acetyltransferase |
| [x] | `acoB` | PP_0554 | Q88QE0 | 0 | acetoin-cleaving E1 beta subunit |
| [x] | `acoA` | PP_0555 | Q88QD9 | 3 | acetoin-cleaving E1 alpha subunit |
| [x] | `PP_0556` | PP_0556 | Q88QD8 | 0 | unresolved AcoX-family accessory protein |

## Residual gaps

- Direct KT2440 biochemistry is absent for all five proteins.
- The physiological E3 paralog and AcoX function are unresolved.
- BdhA stereoisomer and pyridine-nucleotide preferences need direct testing.
- GO lacks an acetoin-cleaving E1-specific molecular-function term; GO:0016624 is used at the assembled AcoA/AcoB annoton level.

## Completion

- [x] Reviewed every selected QuickGO row; no `PENDING` actions remain.
- [x] Reconciled UniProt, primary literature, GO, PTN, and PANTHER evidence.
- [x] Built a species-neutral four-part module with molecular functions only on leaf annotons.
- [x] Recorded incomplete OpenScientist artifact production without restarting research.
- [x] Updated the batch Markdown and TSV.
- [ ] Published as a draft pull request.
