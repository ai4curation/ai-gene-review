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
it models the conserved octanoyl-transfer and sulfur-insertion chemistry as a
direct LipB-LipA route plus separately characterized Bacillus and human
GcvH-relay variants.

The KEGG map contains 19 KT2440 genes, but only `lipB` and `lipA` catalyze these
two installation reactions. The remaining map members are lipoylated carrier
proteins or components of enzyme systems that use the installed cofactor. A
third selected locus, `PP_4797`, is not a KEGG member; it was promoted as a
diagnostic because its automated UniProt name says "Lipoyl synthase" even
though its 54-residue sequence is an ArfA-family ribosome-rescue protein. The
taxon-level research identified a fourth selected locus outside the KEGG
bucket, `PP_0423`, whose BPL/LPL-family assignment makes it an uncertain
salvage-or-GcvH-relay candidate.

## Workflow Status

- [x] Partition all 19 KEGG candidates by role.
- [x] Fetch `lipA`, `lipB`, `PP_4797`, and `PP_0423` with current GOA records.
- [x] Build a species-neutral module with direct and GcvH-relay variants.
- [x] Complete and assess generic OpenScientist module research.
- [x] Complete and assess PSEPK module + pathway + taxon research.
- [x] Complete and assess all four gene-level OpenScientist reports.
- [x] Complete the initial manual review of every fetched GOA row.
- [x] Reconcile the reviews and module against the completed research.
- [x] Validate and render all affected artifacts.
- [x] Open draft pull request #2181 for this module.
- [ ] Finish checks and move pull request #2181 out of draft.

## Pathway Satisfiability

| Order | Reaction | KT2440 implementation | Review status | Decision |
|---|---|---|---|---|
| 1 | Octanoyl-ACP + apo lipoyl-domain protein to octanoylated protein | `lipB` / PP_4801 / Q88DM4 | Curated, research assessed | covered |
| 2 | Octanoylated protein to lipoylated protein by sulfur insertion | `lipA` / PP_4800 / Q88DM5 | Curated, research assessed | covered |

**Module result: `covered`.** KT2440 has one high-confidence LipB and one
high-confidence LipA. Their adjacent genomic placement is consistent with the
two-step route, but module inclusion is grounded in the exact catalytic
functions rather than neighborhood alone.

`PP_0423` / Q88QR5 is assigned to the LipM/LipL family, but the same PANTHER
subfamily contains both characterized LipM and LipL proteins. Gene-level
research favors an LplA-type salvage hypothesis but explicitly retains
ligase-versus-transferase ambiguity. PP_0423 therefore does not yet satisfy a
relay implementation or establish salvage. The direct route remains covered
independently of this unresolved candidate.

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
| Uncertain non-bucket BPL/LPL candidate | `PP_0423` | Review salvage-ligase versus relay-transferase hypotheses; do not assign a specific reaction without discriminating evidence |
| Diagnostic nonmember | `PP_4797` | Curate as ArfA-family ribosome rescue and exclude from lipoylation |

The machine-generated 19-gene source table is retained at
[`ppu00785_lipoate_installation.tsv`](ppu00785_lipoate_installation.tsv).

## Selected Reviews

| Gene | Locus / UniProt | Selection reason | Current decision |
|---|---|---|---|
| `lipB` | PP_4801 / Q88DM4 | Core octanoyl-transfer step | Specific MF and protein lipoylation accepted; broad acyltransferase marked over-annotated |
| `lipA` | PP_4800 / Q88DM5 | Core sulfur-insertion step | Specific MF and lipoylation processes accepted; broad catalytic and Fe-S parents de-duplicated |
| `PP_0423` | PP_0423 / Q88QR5 | BPL/LPL-family candidate found by taxon-level research | Salvage-ligase versus relay-transferase role left unresolved; no GO term inferred from computational evidence alone |
| `PP_4797` | PP_4797 / Q88DM8 | False lipoyl-synthase name adjacent to `lipA/lipB` | ArfA-associated ribosome rescue accepted; excluded from module |

## Curation Decisions

- The module is defined by shared chemistry rather than by one organism's
  topology. It contains a two-reaction direct route and separate three-reaction
  Bacillus and human GcvH-relay variants.
- Molecular functions occur only on leaf reaction annotons. The module has no
  redundant module-level cytoplasm/cytosol assertions.
- LipL and LIPT1 use broad `acyltransferase activity` only because GO lacks a
  precise term for their physiological GcvH-to-client amidotransfer reactions;
  exact Rhea reactions and UniProt exemplars carry the specificity.
- LipB is the physiological octanoyl-ACP:protein transferase in this route.
  The generic `acyltransferase activity` parent adds no information beside
  `lipoyl(octanoyl) transferase activity`.
- LipA is a radical-SAM enzyme with two 4Fe-4S clusters. Its core annotation is
  `lipoate synthase activity`; cluster binding and cytoplasmic localization are
  retained only as non-core mechanistic context.
- `PP_4797` is only 54 residues and carries InterPro `IPR005589` and Pfam
  `PF03889`, both ArfA. It lacks the radical-SAM and LipA family architecture
  found in the 338-residue Q88DM5 protein.
- `PP_0423` carries InterPro `IPR050664` and PANTHER `PTHR43679:SF2`, but those
  identifiers group LipM and LipL activities together. OpenScientist favors a
  salvage-ligase hypothesis but does not close the activity ambiguity. It
  remains a candidate, not a second satisfied route.
- Client complexes are not counted as additional pathway steps simply because
  KEGG groups lipoate use and lipoate installation on the same map.

## Research

- Generic module report target:
  `modules/endogenous_protein_lipoylation-deep-research-openscientist.md`
- Species-aware report target:
  `projects/P_PUTIDA/deep-research/PSEPK__endogenous_protein_lipoylation__ppu00785-deep-research-openscientist.md`
- Gene-level report targets:
  `genes/PSEPK/{lipA,lipB,PP_4797,PP_0423}/*-deep-research-openscientist.md`

## Validation

Checkpoint on 2026-07-18:

- All 13 fetched GOA rows across `lipA`, `lipB`, and `PP_4797` have manual actions;
  no `PENDING` values remain.
- The `PP_0423` review records its empty GOA set and deliberately leaves its
  exact core activity unresolved after assessing the salvage-ligase and
  relay-transferase hypotheses.
- The revised three-variant module passes `ModuleReview` LinkML validation. The
  custom semantic validator reports only its expected inability to validate
  InterPro labels through the current OAK prefix configuration.
- All four selected gene reviews validate without warnings and all affected
  gene, module, and project pages have been regenerated. The sole module
  warning is the documented OAK configuration gap for InterPro label lookup.
