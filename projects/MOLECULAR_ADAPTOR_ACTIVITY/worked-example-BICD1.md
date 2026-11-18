---
title: "Worked example: BICD1"
species: [human]
---

# Worked example: BICD1 / Bicaudal D1 (`Q96G01`)

Back to the [project page](../MOLECULAR_ADAPTOR_ACTIVITY.md).

Fourth worked example and the **cytoskeletal adaptor** child (`GO:0008093`), on a
previously unreviewed gene. BICD1 is the textbook *dynein activating / cargo
adaptor*: it bridges the minus-end microtubule motor (dynein–dynactin) to
Rab6-bearing Golgi and secretory cargo. See the full review of BICD1 (linked
from the gene symbol) and its notes at `genes/human/BICD1/BICD1-notes.md`.

## The gene in one line

UniProt: BICD1 "regulates COPI-independent Golgi-ER transport by recruiting the
dynein–dynactin motor complex" and interacts with RAB6A/RAB6B
[PMID:12447383, PMID:20089649].

## Starting state (GOA, 54 rows)

The adaptor story is already well-annotated — this gene is light on bare
`protein binding` (3 rows) and rich in **specific binding terms for the two ends
of the bridge**:

- Motor side: `GO:0034452` dynactin binding, `GO:0045505` dynein intermediate
  chain binding, `GO:0070840` dynein complex binding (all IDA/IBA).
- Cargo side: `GO:0031267` small GTPase binding (Rab6, IPI).
- Integrative MF: `GO:0008093` cytoskeletal adaptor activity (IDA/IBA/IEA).
- Core process: `GO:0072385` minus-end-directed organelle transport along
  microtubule (IMP).

## What the decision rules produced

54 annotations → ACCEPT 29, KEEP_AS_NON_CORE 17, MODIFY 2, REMOVE 2,
MARK_AS_OVER_ANNOTATED 4.

This example adds two patterns the earlier three did not foreground:

1. **A mis-typed *structural* MF corrected to the adaptor term.** `GO:0005200`
   structural constituent of cytoskeleton (a 1997 TAS from the cloning paper) was
   `MODIFY`'d to `GO:0008093` cytoskeletal adaptor activity. BICD1 is a coiled-coil
   adaptor, not a structural cytoskeletal component — the legacy term is in the
   wrong MF branch (structural molecule activity), and the lateral correction puts
   it on the activity the modern evidence supports. This is the same class of
   lateral `MODIFY` as LDLRAP1's signaling→clathrin-cargo fix, but from the
   *structural-molecule* branch rather than a sibling adaptor term.

2. **Legacy / cross-species process annotations triaged, not trusted.** The 1997
   paper also left `GO:0006396` RNA processing and `GO:0009653` anatomical
   structure morphogenesis (both `MARK_AS_OVER_ANNOTATED`: BicD does mRNA
   *transport/localisation*, not RNA processing, and the morphogenesis term is
   vague Drosophila-era legacy), while `GO:0008298` intracellular mRNA
   localisation — a genuinely conserved BicD dynein-cargo function — was kept
   `KEEP_AS_NON_CORE`. Distinguishing "wrong" from "real but peripheral" within
   one old reference is the work here.

The two `protein binding` rows split as before: GSK3B (a kinase) → `MODIFY` to
`GO:0019901` protein kinase binding; a viral interactor and a STAT3 interactome
hit → `REMOVE`.

Core function: `GO:0008093` cytoskeletal adaptor activity — BICD1 binds the
dynein complex, its intermediate chain and dynactin at one end and Rab6 at the
other, driving minus-end Golgi-to-ER transport.

## What this example adds beyond the others

- **The motor is the "enzyme-equivalent" and Rab6 the cargo.** Like RPTOR's
  enzyme/substrate split, BICD1's partner list resolves cleanly into *motor-side*
  (dynein/dynactin) and *cargo-side* (Rab6 GTPase) contacts — the two ends the
  adaptor term integrates. The specific binding terms were already present; the
  review's job was to confirm them as core and keep the adaptor MF beside them for
  the integrative bridging (decision rule 5: a distinct event — coupling motor to
  cargo — that neither binding term states alone).
- **Old TAS/NAS annotations are the main hazard on a long-known gene**, not
  high-throughput `protein binding`. BICD1 (cloned 1997) carries legacy
  structural/RNA/morphogenesis terms that a modern mechanistic reading reassigns
  or demotes — the opposite profile from GRB2/RPTOR, whose noise was interactome
  `protein binding`.
