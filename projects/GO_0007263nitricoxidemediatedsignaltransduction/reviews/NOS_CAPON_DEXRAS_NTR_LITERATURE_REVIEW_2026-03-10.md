# NOS/CAPON/Dexras signaling literature review for NTR decision

Date: 2026-03-10
Scope: Evaluate whether GO needs a new term for NOS/CAPON/Dexras (RASD1/Dexras1) signaling biology.

## Question

Is a new GO term (NTR) warranted for the mechanism described in the nNOS-CAPON-Dexras literature, especially around PMID:11086993?

## Core evidence reviewed

### Foundational mechanism papers

- PMID:11086993 — Dexras1 is coupled to nNOS through CAPON; Dexras1 is activated by NO donors and NMDA-stimulated NO synthesis; nNOS/CAPON/Dexras1 ternary complex supports targeted NO signaling.
- PMID:16908409 — NMDA receptor–NO signaling controls neuronal iron homeostasis via Dexras1 (functional pathway extension from the foundational mechanism).

### Follow-up pathway/phenotype literature (representative)

- PMID:25129479 — CAPON-nNOS coupling as anxiolytic target.
- PMID:29858554 — stress/anxiety phenotypes tied to nNOS-CAPON-Dexras1 coupling.
- PMID:29577585 — nNOS-CAPON interaction in amyloid-β neurotoxicity.
- PMID:36212606 — ketamine/depression model involving nNOS-CAPON-Dexras1 complex.
- PMID:39749632 — S-nitrosylation of Dexras1 in post-stroke recovery.
- PMID:27237129 — review of NOS1AP/CAPON in neurological/psychiatric disease context.

These papers support a recurring biological motif: localized nNOS output is scaffolded by CAPON/NOS1AP to regulate Dexras1-driven intracellular signaling outcomes.

## Current annotation/term fit snapshot

For rat Rasd1 (UniProtKB:Q9JKF8), QuickGO currently includes (for PMID:11086993):

- GO:0071732 cellular response to nitric oxide (IDA)
- GO:0098989 NMDA selective glutamate receptor signaling pathway (IDA)
- GO:0141124 intracellular signaling cassette (IDA)

And no evidence-backed mapping to GO:0007263 for the corrected PMID pair.

## Gap analysis

### What existing terms capture well

- **NO exposure/response aspect**: GO:0071732
- **Neuronal upstream context**: GO:0098989
- **Generic signaling role**: GO:0141124

### What is not captured very specifically

- The mechanistic intersection “NO-dependent activation of a Ras-family signaling effector (Dexras1) via nNOS-CAPON scaffolding.”

## NTR decision

## Recommendation: **Defer NTR for now (not strictly required for current curation)**

Reasoning:

1. Current terms are sufficient to represent the corrected Rasd1 assertion without forcing an incorrect GO:0007263 assignment.
2. Evidence is currently concentrated around a narrow mechanism and limited gene set; this can be represented by multi-annotation composition (NO response + NMDA pathway + intracellular signaling).
3. A high-quality NTR is better justified when broader curation demand is demonstrated across multiple genes/species/papers where existing terms repeatedly lose mechanistic fidelity.

## If NTR demand increases

If repeated curation pressure emerges, candidate term concept:

- Suggested label: **nitric oxide-dependent Ras protein signal transduction**
- Suggested parent(s):
  - GO:0007265 Ras protein signal transduction
  - (cross-product/logical relation to nitric-oxide-mediated signaling or cellular response to nitric oxide)
- Suggested definition sketch:
  - “Any Ras protein signal transduction process in which nitric oxide acts as a necessary upstream signaling input for Ras-family GTPase activation.”

## Practical curation guidance now

- For Rasd1 + PMID:11086993:
  - Prefer **TRANSFER** from GO:0007263 to GO:0071732 (as already recommended in project files).
  - Keep supporting pathway context with GO:0098989 and broad intracellular signaling terms where evidence supports.
- Do not open NTR yet unless additional curated cases show systematic mismatch with existing ontology granularity.
