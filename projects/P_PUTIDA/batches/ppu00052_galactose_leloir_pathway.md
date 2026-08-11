---
title: "PSEPK ppu00052 Leloir pathway satisfiability batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [galE, PP_1165]
autolink_gene_symbols: false
---

# PSEPK ppu00052: Leloir pathway satisfiability

- Module: `galactose_leloir_pathway`
- Pathway context: KEGG `ppu00052` (galactose metabolism)
- Focused genes: 2
- Broad membership-table candidates: 8
- Satisfiability result: canonical Leloir pathway absent

## Boundary

The canonical Leloir pathway requires four reactions: aldose mutarotation,
galactokinase, galactose-1-phosphate uridylyltransferase, and UDP-glucose
4-epimerase. KT2440 has GalE and an aldose 1-epimerase-family candidate, but no
identifiable GalK or GalT. The KEGG bucket also contains glucokinase,
phosphomutases, and nucleotide-sugar enzymes whose different reactions do not
fill those holes.

This batch therefore records pathway absence. It does not relabel Glk as a
galactokinase, infer GalT from GalU, or assign phosphomutases to the missing UMP
transfer reaction.

## Status

- [x] Audit the complete PSEPK metadata table for GalM/GalK/GalT/GalE candidates.
- [x] Confirm that GalK and GalT cannot be identified from gene names, EC numbers, GO terms, or family metadata.
- [x] Curate the GalE review and remove the unsupported full-Leloir process propagation.
- [x] Retain PP_1165 as an aldose-epimerase candidate without asserting galactose specificity.
- [x] Revise the reusable four-reaction module to remove disease-specific framing and module-level cytosol.
- [ ] Complete module + `ppu00052` + PSEPK OpenScientist research.
- [x] Complete GalE OpenScientist research.
- [x] Validate the module and focused gene reviews.
- [x] Render the focused gene review and batch page.
- [x] Open draft PR #2485.

## Focused Genes

| Gene | Locus | UniProt | Candidate role | First-pass result |
|---|---|---|---|---|
| `PP_1165` | PP_1165 | Q88NP2 | aldose 1-epimerase candidate | Existing review retains only carbohydrate epimerase-level function; galactose specificity is unresolved |
| `galE` | PP_3129 | Q88I72 | UDP-glucose 4-epimerase | Retain exact reaction; remove TreeGrafter Leloir-pathway propagation because the pathway is incomplete |

## Excluded Bucket Members

| Gene | Reason it does not fill a Leloir hole |
|---|---|
| `glk` | Glucokinase EC 2.7.1.2, not galactokinase EC 2.7.1.6 |
| `cpsG` | Phosphomannomutase used in GDP-mannose biosynthesis |
| `pgm` | Phosphoglucomutase acting downstream of glucose 1-phosphate, not GalK or GalT |
| `galU` | UDP-glucose pyrophosphorylase; does not transfer UMP between galactose 1-phosphate and UDP-glucose |
| `algC` | Phosphomannomutase/phosphoglucomutase for envelope precursor metabolism |
| `PP_0501` | Generic NAD-dependent epimerase/dehydratase family protein without GalE or Leloir-step evidence |

## Evidence Notes

The module remains a reusable four-reaction definition with exact human
exemplars and PSEPK GalE as a bacterial epimerase exemplar. GalE family
membership is not sufficient to infer Leloir catabolism because the same
UDP-sugar reaction serves nucleotide-sugar and envelope biosynthesis.

The completed GalE OpenScientist report supports a canonical group-1
UDP-glucose/UDP-galactose epimerase and places PP_3129 in an exopolysaccharide
biosynthesis/export neighborhood. This strengthens the interpretation that its
main KT2440 role is biosynthetic UDP-galactose supply for surface glycans.

The broad candidate inventory and its exact metadata are retained in
[`ppu00052_galactose_leloir_pathway.tsv`](ppu00052_galactose_leloir_pathway.tsv).
