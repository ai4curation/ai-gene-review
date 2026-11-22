---
title: "Worked example: DCAF12"
species: [human]
---

# Worked example: DCAF12 (`Q5T6F0`)

Back to the [project page](../MOLECULAR_ADAPTOR_ACTIVITY.md).

Fifth worked example and the **ubiquitin-like ligase-substrate adaptor** child
(`GO:1990756`), on a previously unreviewed gene. DCAF12 is a clean *substrate
receptor* of a cullin-RING ligase: it recognises a C-terminal degron and presents
substrates to the CRL4 ubiquitin ligase. See the full review of DCAF12 (linked
from the gene symbol) and its notes at `genes/human/DCAF12/DCAF12-notes.md`.

## The gene in one line

UniProt: DCAF12 is the "substrate-recognition component of a DCX (DDB1-CUL4-X-box)
E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons)
pathway," recognising a C-terminal diglutamate (or Glu-Leu) degron on substrates
such as MOV10 and MAGE-A3/A6 [PMID:34065512, PMID:29779948, PMID:31267705].

## Starting state (GOA, 29 rows)

Small and almost entirely on-target — the informative terms are already present:

- MF: `GO:1990756` ubiquitin-like ligase-substrate adaptor activity (IDA ×3).
- Complex: `GO:0080008` Cul4-RING E3 ubiquitin ligase complex, plus the
  CUL4A/CUL4B-specific complex terms (`part_of`).
- Process: `GO:0140627` ubiquitin-dependent protein catabolic process via the
  C-end degron rule pathway (IDA ×3); `GO:0016567` protein ubiquitination.
- 3 bare `GO:0005515` rows — all to the same partner, **DDB1** (`Q16531`).

## What the decision rules produced

29 annotations → ACCEPT 21, KEEP_AS_NON_CORE 5, REMOVE 3.

This example's distinctive move is **`in_complex`, not `has input`, for a
ligase-substrate adaptor**:

1. **The `protein binding` rows are all the adaptor–ligase docking interaction.**
   All three `GO:0005515` rows bind **DDB1**, the adaptor through which DCAF12
   joins the CRL4 (DDB1-CUL4-RBX1) complex. Binding DDB1 is complex assembly, not
   a distinct function, and it is already captured by the `part_of` Cul4-RING
   complex annotations — so the bare rows are `REMOVE`d under the protein-binding
   policy (the same call as RPTOR's MLST8 rows). Here it is especially clean
   because *every* `protein binding` row is that one structural contact.

2. **The substrate relationship lives on the ligase complex, not as a process on
   the substrate.** DCAF12's effects on autophagy (`GO:0010506`,
   `acts_upstream_of`), T-cell activation, proliferation and miRNA silencing
   (`GO:0060964`, via degradation of the RISC helicase MOV10) are all downstream
   consequences of degrading a specific substrate — kept `KEEP_AS_NON_CORE`, not
   promoted to core. This is the CLAUDE.md participation test: DCAF12 *performs*
   substrate recognition and ubiquitin targeting; the pathways its substrates sit
   in are not its own functions.

Core function: `GO:1990756` ubiquitin-like ligase-substrate adaptor activity,
`in_complex` `GO:0080008` Cul4-RING E3 ubiquitin ligase complex,
`directly_involved_in` `GO:0140627` the C-end degron pathway.

## What this example adds beyond the others

- **The "enzyme" is a multi-subunit ligase and the adaptor is one subunit of it.**
  Unlike RPTOR (which binds a separate kinase) or BICD1 (which binds a motor),
  DCAF12 *is part of* the catalytic machine it serves. The right modelling is
  `in_complex` the CRL4 complex (recorded via `part_of`), with the MF naming the
  substrate-receptor role — the adaptor and the enzyme are members of one complex.
- **Degron recognition is the `has input` here.** The adaptor's "input" is the
  degron-bearing substrate (MOV10, MAGE-A3/6); the project's rule 4 (name the
  bridged partners) is satisfied by the C-terminal degron substrates, recorded in
  the rationale rather than as an annotation on the substrate.
- **A small, modern, on-target gene still needs the policy.** Even at 29
  annotations with no legacy cruft, the only `protein binding` rows were the
  DDB1 docking contact — showing the "partner identity decides REMOVE vs refine"
  triage applies regardless of gene size or age.
