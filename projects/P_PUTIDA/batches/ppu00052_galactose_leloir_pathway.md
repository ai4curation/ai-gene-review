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
- [x] Complete and document annotation-reviewer passes for both selected genes.
- [x] Verify cross-species PANTHER membership and PAINT nodes from local canonical data.
- [x] Complete module + `ppu00052` + PSEPK OpenScientist research (1,689.92
  seconds; 28 minutes 9.92 seconds).
- [x] Complete GalE OpenScientist research.
- [x] Complete final validation and rendering after research ingestion.
- [ ] Obtain external review of the non-draft wave136 PR.

## Focused Genes

| Gene | Locus | UniProt | Candidate role | First-pass result |
|---|---|---|---|---|
| `PP_1165` | PP_1165 | Q88NP2 | aldose 1-epimerase candidate | Existing review retains only carbohydrate epimerase-level function; galactose specificity is unresolved |
| `galE` | PP_3129 | Q88I72 | UDP-glucose 4-epimerase | Retain exact reaction; remove TreeGrafter Leloir-pathway propagation because the pathway is incomplete |

## Annotation-reviewer pass

All six fetched GOA rows were reviewed on 2026-09-01 against UniProt, available
gene-level research, and the focused pathway boundary. Every row has an
explicit action and row-level support; none remains PENDING or UNDECIDED.

| Gene | Rows | ACCEPT | KEEP_AS_NON_CORE | MODIFY | REMOVE |
|---|---:|---:|---:|---:|---:|
| `PP_1165` | 3 | 0 | 2 | 1 | 0 |
| `galE` | 3 | 1 | 1 | 0 | 1 |

For PP_1165, generic isomerase activity is narrowed only to carbohydrate
racemase/epimerase activity; no galactose substrate claim is made. For GalE,
the exact UDP-glucose 4-epimerase reaction is retained while the electronic
complete-Leloir process propagation is removed because the two committed
upstream reactions are absent.

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

## Family and evolutionary grounding

| Step | PANTHER grounding | Bacterial exemplar | Human exemplar | PAINT node |
|---|---|---|---|---|
| GalM mutarotation | `PTHR10091:SF0` | E. coli P0A9C3 | Q96C23 | `PTN000009552` |
| GalK phosphorylation | `PTHR10457:SF7` | E. coli P0A6T3 | P51570 | `PTN000048421` |
| GalT uridylyl transfer | `PTHR11943:SF1` | E. coli P09148 | P07902 | `PTN000235304` |
| GalE UDP-sugar recycling | `PTHR43725` | E. coli P09147; PSEPK Q88I72 | Q14376 | not asserted for the shared family |

All labels are verbatim local PANTHER ontology labels, including the historical
`GALACTOKINASE-RELATED` label for SF7. Membership is verified in the refreshed
local index. GalE remains at the parent family because E. coli/human GalE are
SF47 while PSEPK Q88I72 is assigned to heterogeneous SF53; narrowing would
exclude the concrete PSEPK epimerase or assert a misleading subfamily.
Local PAINT node `PTN000041817` verifies UDP-glucose 4-epimerase activity for
the E. coli/human clade, but no local evidence places Q88I72 under that node;
it is therefore not asserted as a shared ancestral node in the module.

## Research provenance

- Existing PP_1165 Asta retrieval:
  `genes/PSEPK/PP_1165/PP_1165-deep-research-asta.md` (retrieval was not
  gene-specific enough to support substrate assignment).
- Existing GalE OpenScientist report:
  `genes/PSEPK/galE/galE-deep-research-openscientist.md`.
- Module + pathway + taxon OpenScientist report:
  `projects/P_PUTIDA/deep-research/PSEPK__galactose_leloir_pathway__ppu00052-deep-research-openscientist.md`
  (completed 2026-09-01 in 1,689.92 seconds with eight citations and HTML/PDF
  artifacts).

The module-level report independently found no identifiable GalK or GalT and
classified the focused catabolic route as unsatisfiable. It also retained
PP_1165 as substrate-uncertain and treated GalE as insufficient to establish
catabolic pathway coverage. Its broader suggestion that PP_0501 is a second
GALE is not adopted here: the local PP_0501 evidence does not establish that
specific reaction, so PP_0501 remains outside this focused selected-gene set.
