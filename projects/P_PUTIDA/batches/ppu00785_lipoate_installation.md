---
title: "PSEPK ppu00785 endogenous protein lipoylation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00785: Endogenous protein lipoylation

This batch separates cofactor installation from the many lipoate-dependent
enzymes grouped under KEGG `ppu00785`. The reusable module is
[Endogenous protein lipoylation](../../../modules/endogenous_protein_lipoylation.html):
LipB transfers octanoyl from octanoyl-ACP to a protein lipoyl domain, and LipA
inserts the two sulfur atoms that complete the protein-bound cofactor.

The KEGG map contains 19 KT2440 genes, but only `lipB` and `lipA` catalyze these
two installation reactions. The remaining map members are lipoylated carrier
proteins or components of enzyme systems that use the installed cofactor. A
third selected locus, `PP_4797`, is not a KEGG member; it was promoted as a
diagnostic because its automated UniProt name says "Lipoyl synthase" even
though its 54-residue sequence is an ArfA-family ribosome-rescue protein.

## Workflow Status

- [x] Partition all 19 KEGG candidates by role.
- [x] Fetch `lipA`, `lipB`, and diagnostic `PP_4797` with current GOA records.
- [x] Build a species-neutral, two-reaction LipB/LipA module.
- [ ] Complete and assess generic OpenScientist module research.
- [ ] Complete and assess PSEPK module + pathway + taxon research.
- [ ] Complete and assess all three gene-level OpenScientist reports.
- [x] Complete the initial manual review of every selected GOA row.
- [ ] Reconcile the reviews and module against the completed research.
- [ ] Validate and render all affected artifacts.
- [ ] Open and shepherd one pull request for this module.

## Pathway Satisfiability

| Order | Reaction | KT2440 implementation | Review status | Decision |
|---|---|---|---|---|
| 1 | Octanoyl-ACP + apo lipoyl-domain protein to octanoylated protein | `lipB` / PP_4801 / Q88DM4 | Curated, research running | covered |
| 2 | Octanoylated protein to lipoylated protein by sulfur insertion | `lipA` / PP_4800 / Q88DM5 | Curated, research running | covered |

**Module result: `covered`.** KT2440 has one high-confidence LipB and one
high-confidence LipA. Their adjacent genomic placement is consistent with the
two-step route, but module inclusion is grounded in the exact catalytic
functions rather than neighborhood alone.

Octanoyl-ACP production is an upstream fatty-acid-synthesis dependency. The
pyruvate, 2-oxoglutarate, branched-chain 2-oxoacid, acetoin, and glycine-cleavage
systems are downstream clients. Exogenous-lipoate salvage would require a
lipoate--protein ligase route and is outside this direct endogenous branch.

## Candidate Partition

| Bucket | Genes | Treatment |
|---|---|---|
| Core installation route | `lipB`, `lipA` | Curate here and use as exact PSEPK module exemplars |
| Glycine-cleavage carrier and clients | `gcvH1`, `gcvH2`, `gcvP1`, `gcvP2`, `gcvT-I`, `gcvT` | Lipoylated carrier proteins or client enzymes; not installation catalysts |
| 2-oxoacid/acetoin dehydrogenase clients | `aceE`, `aceF`, `acoC`, `sucA`, `sucB`, `bkdAA`, `bkdAB`, `bkdB` | Cofactor-dependent complexes; not installation catalysts |
| Shared E3 client components | `lpd`, `lpdG`, `lpdV` | Dihydrolipoyl dehydrogenases that recycle client-bound lipoamide; not biosynthetic steps |
| Diagnostic nonmember | `PP_4797` | Curate as ArfA-family ribosome rescue and exclude from lipoylation |

The machine-generated 19-gene source table is retained at
[`ppu00785_lipoate_installation.tsv`](ppu00785_lipoate_installation.tsv).

## Selected Reviews

| Gene | Locus / UniProt | Selection reason | Current decision |
|---|---|---|---|
| `lipB` | PP_4801 / Q88DM4 | Core octanoyl-transfer step | Specific MF and protein lipoylation accepted; broad acyltransferase marked over-annotated |
| `lipA` | PP_4800 / Q88DM5 | Core sulfur-insertion step | Specific MF and lipoylation processes accepted; broad catalytic and Fe-S parents de-duplicated |
| `PP_4797` | PP_4797 / Q88DM8 | False lipoyl-synthase name adjacent to `lipA/lipB` | ArfA-associated ribosome rescue accepted; excluded from module |

## Curation Decisions

- The module contains two substantive reactions and keeps molecular functions
  only on the LipB and LipA leaf annotons. It has no redundant module-level
  cytoplasm/cytosol assertions.
- LipB is the physiological octanoyl-ACP:protein transferase in this route.
  The generic `acyltransferase activity` parent adds no information beside
  `lipoyl(octanoyl) transferase activity`.
- LipA is a radical-SAM enzyme with two 4Fe-4S clusters. Its core annotation is
  `lipoate synthase activity`; cluster binding and cytoplasmic localization are
  retained only as non-core mechanistic context.
- `PP_4797` is only 54 residues and carries InterPro `IPR005589` and Pfam
  `PF03889`, both ArfA. It lacks the radical-SAM and LipA family architecture
  found in the 338-residue Q88DM5 protein.
- Client complexes are not counted as additional pathway steps simply because
  KEGG groups lipoate use and lipoate installation on the same map.

## Research

- Generic module report target:
  `modules/endogenous_protein_lipoylation-deep-research-openscientist.md`
- Species-aware report target:
  `projects/P_PUTIDA/deep-research/PSEPK__endogenous_protein_lipoylation__ppu00785-deep-research-openscientist.md`
- Gene-level report targets:
  `genes/PSEPK/{lipA,lipB,PP_4797}/*-deep-research-openscientist.md`

## Validation

Checkpoint on 2026-07-18:

- All 13 fetched GOA rows across the three selected genes have manual actions;
  no `PENDING` values remain.
- All three initial gene reviews pass schema, term, reference, and
  best-practice validation.
- The initial two-step module passes `ModuleReview` LinkML validation and the
  custom semantic validator with no warnings.
- Final research integration, rendering, and repository-wide validation remain
  to be completed before the PR is opened.
