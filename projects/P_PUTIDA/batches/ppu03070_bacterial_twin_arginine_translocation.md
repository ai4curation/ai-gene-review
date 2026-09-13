---
title: "PSEPK twin-arginine protein translocation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [tatA-I, tatB-I, tatC-I, tatA-II, tatB, tatC-II]
autolink_gene_symbols: false
---

# PSEPK twin-arginine protein translocation

This batch curates the Tat branch represented across the KEGG protein-export
and bacterial-secretion maps. The six Tat proteins have primary assignment to
KEGG `ppu03060` (Protein export), not `ppu03070`; this historically named batch
is retained as project bookkeeping and to preserve the experimentally grounded
link to downstream Xcp type II secretion. Sec export, type II secretion, and
type VI secretion remain separate modules. The reusable Tat model is
`modules/bacterial_twin_arginine_translocation.yaml`; this page records its
Pseudomonas putida KT2440 instantiation.

## Boundary

The module contains three substantive parts:

1. TatC-dependent twin-arginine signal recognition and membrane scaffolding.
2. TatB-dependent receptor-complex organization.
3. Assembly of the TatA/TatB/TatC translocon and proton-motive-force-dependent
   folded-protein passage.

Substrate folding/cofactor installation, signal-peptide cleavage, and the
downstream functions of exported proteins are outside the boundary.

`GO:0009977` is assigned only to the final assembled-complex annoton. TatA,
TatB, and TatC each contribute to that activity, but none is modeled as an
independent transporter. The shared bacterial plasma-membrane location is
stated once in module context rather than repeated on every leaf.

## Status

- [x] Fetch both PSEPK `tatABC` loci from UniProt and GOA.
- [x] Complete and document an annotation-reviewer pass for all six selected genes.
- [x] Repair the species-neutral module boundary, MF placement, and shared location.
- [x] Verify PANTHER family membership and PAINT nodes from local canonical data.
- [x] Complete OpenScientist module + pathway + taxon research (1,478 seconds;
  completed without cancellation or timeout).
- [x] Complete final validation and rendering after research ingestion.
- [ ] Obtain external review of the non-draft PR.

## Focused Genes

| Gene | Locus | UniProt | Module role |
|---|---|---|---|
| `tatC-I` | PP_1039 | Q88P14 | TatC receptor/scaffold, system I |
| `tatB-I` | PP_1040 | Q88P13 | TatB receptor organization, system I |
| `tatA-I` | PP_1041 | Q88P12 | TatA translocation assembly, system I |
| `tatA-II` | PP_5016 | Q88D13 | TatA translocation assembly, system II |
| `tatB` | PP_5017 | Q88D12 | TatB receptor organization, system II |
| `tatC-II` | PP_5018 | Q88D11 | TatC receptor/scaffold, system II |

## Annotation-reviewer pass

All 38 fetched GOA rows were reviewed on 2026-09-01 against each gene's UniProt
record, PMID:23530902 where applicable, existing deep research, and the repaired
module. Every row has an explicit action, rationale, and row-level supporting
text; none remains PENDING or UNDECIDED.

| Gene | Rows | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY |
|---|---:|---:|---:|---:|---:|
| `tatA-I` | 6 | 4 | 1 | 1 | 0 |
| `tatB-I` | 5 | 2 | 2 | 0 | 1 |
| `tatC-I` | 7 | 4 | 0 | 3 | 0 |
| `tatA-II` | 7 | 5 | 1 | 1 | 0 |
| `tatB` | 6 | 3 | 2 | 1 | 0 |
| `tatC-II` | 7 | 4 | 0 | 3 | 0 |

The single MODIFY is the generic membrane annotation on the less-completely
annotated TatB-I record, replaced by bacterial plasma membrane. Broad parent
processes are kept as correct non-core annotations where a more informative
Tat-specific process is present; generic membrane terms remain over-annotated
where a plasma-membrane term is available.

## Family and evolutionary grounding

| Role | PANTHER subfamily | Cross-species exemplar | PSEPK exemplars | PAINT node |
|---|---|---|---|---|
| TatC receptor/scaffold | `PTHR30371:SF0` | E. coli K-12 P69423 | Q88P14, Q88D11 | `PTN000769484` |
| TatB receptor organization | `PTHR33162:SF1` | E. coli K-12 P69425 | Q88P13, Q88D12 | `PTN002109144` |
| TatA translocation assembly | `PTHR42982:SF1` | E. coli K-12 P69428 | Q88P12, Q88D13 | `PTN002452729` |

The PANTHER labels are the official local ontology labels, including the
historical chloroplastic wording on `PTHR33162:SF1`. Readable TatA/TatB/TatC
role names remain in `preferred_term`. The PAINT nodes are taken from the local
IBD exports and are seeded by the listed E. coli proteins; no PTN was inferred
from memory.

## PSEPK satisfiability

The two intact `tatABC` loci satisfy all three module roles. PMID:23530902
provides direct KT2440 evidence that both complete Tat systems can transport
UxpB. It does not isolate individual subunit mechanisms or establish broader
locus-specific substrate sets. The first locus is induced under phosphate
limitation, but this does not justify assigning exclusive cargo or conditions
to either reusable module instance.

The OpenScientist report independently recovers duplicate satisfiability and
the `ppu03060` pathway boundary. Its suggestion to encode the duplicated operon
architecture in the generic module is intentionally handled here instead: the
module remains species-neutral and reusable, while this batch records two
PSEPK instantiations. Its sequential step narrative is also represented as
constituent TatC and TatB roles feeding the final TatABC assembly, without
asserting that a TatBC receptor is built in a strict TatC-then-TatB sequence.

The exact UniProt symbol for PP_5017 is `tatB` and is retained here. The
OpenScientist protein-export report's `tatB-II` relabel suggestion is treated as
a non-authoritative naming proposal, not as a source-annotation change. The
report's suggestion to place `GO:0009977` on TatA is likewise not adopted for
an isolated subunit: the transporter MF is asserted only on the assembled
TatABC leaf annoton.

## Research provenance

- Existing gene-level OpenScientist report:
  `genes/PSEPK/tatA-II/tatA-II-deep-research-openscientist.md`.
- Completed module + pathway + taxon OpenScientist report (2026-09-01; 1,478
  seconds; 10 citations; HTML and PDF artifacts retained):
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_twin_arginine_translocation__ppu03070-deep-research-openscientist.md`.
