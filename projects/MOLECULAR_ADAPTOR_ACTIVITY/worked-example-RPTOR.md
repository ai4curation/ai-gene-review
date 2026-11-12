---
title: "Worked example: RPTOR"
species: [human]
---

# Worked example: RPTOR / Raptor (`Q8N122`)

Back to the [project page](../MOLECULAR_ADAPTOR_ACTIVITY.md).

Third worked example and the second driving a **new** review of a previously
unreviewed gene (after [LDLRAP1](worked-example-LDLRAP1.md)). RPTOR is the
prototype of the **`GO:0140767` enzyme-substrate adaptor activity** child — the
case the project's modelling rule singles out, where the adaptor's job is to
bring an **enzyme together with its substrate** (`provides input for`), not to
regulate a partner's activity. See the
full review of RPTOR (linked from the gene symbol) and its
[notes](../../../genes/human/RPTOR/RPTOR-notes.md).

## The gene in one line

RPTOR (Raptor) is the non-catalytic **substrate-presenting subunit of mTORC1**.
UniProt states it plainly: within the complex RPTOR acts both as a recruitment
adapter (binding the **Rag GTPases** to dock mTORC1 at the lysosome) and as a
**substrate-specific adapter** that binds **TOS-motif** proteins (4E-BP1, S6K1)
and directs them towards the active site of the MTOR kinase domain
(UniProtKB:Q8N122, CC:FUNCTION; mechanism in PMID:12747827, PMID:24403073).

## Starting state (GOA, 170 rows)

- **61 × `GO:0005515` protein binding** (IPI) — the largest block, almost all
  from interactome/affinity screens.
- The real adaptor MFs present: `GO:0140767` enzyme-substrate adaptor activity
  (IDA ×3), `GO:0030674` protein-macromolecule adaptor activity (IDA/IBA),
  `GO:0031267` small GTPase binding (Rag), `GO:0019901` protein kinase binding.
- A large tail of mTORC1 **downstream processes** (growth, autophagy, glycolysis,
  lipid synthesis, Pol III transcription, nutrient responses) and some
  tissue-/behaviour-level ISS rows.

## What the decision rules produced

170 annotations → ACCEPT 82, MODIFY 30, REMOVE 32, KEEP_AS_NON_CORE 22,
MARK_AS_OVER_ANNOTATED 4.

The instructive part is how the **61 `protein binding` rows split by partner
identity** — the single most useful move on an adaptor. The key discipline: a
binary interaction (an IPI hit) evidences **binding**, not the bridging
**activity**, so each row is refined to a *binding* term the partner supports
(or removed), and the `GO:0140767` enzyme-substrate adaptor *activity* is left to
the three IDA rows that actually assay the bridging:

| Interaction partner | Rows | Call | Term |
|---|---:|---|---|
| **MTOR** kinase (P42345, + mouse ortholog) | 24 | MODIFY | `GO:0019901` protein kinase binding (the **enzyme** side) |
| **S6K1 / RPS6KB1** (P23443), a protein kinase | 3 | MODIFY | `GO:0019901` protein kinase binding |
| **4E-BP1** (Q13541), **PRAS40** (Q96B36) — TOS-motif substrates, not kinases | 8 | REMOVE | bare protein binding (no specific binding term; the adaptor *activity* is already asserted by IDA) |
| everything else (MLST8, BRAF, singletons) | 24 | REMOVE | bare protein binding, per policy |

That triage reconstructs the mechanism without over-claiming: RPTOR binds the
**MTOR kinase** and the kinase substrate **S6K1** (→ protein kinase binding), and
its binding of the non-enzyme substrates 4E-BP1/PRAS40 is recorded as the
enzyme-substrate adaptor *activity* only where an assay (IDA) demonstrates the
bridging — not inferred from a two-hybrid hit.

Core functions settled on the two adapter roles: `GO:0140767` enzyme-substrate
adaptor activity (substrate presentation to MTOR) and `GO:0030674`
protein-macromolecule adaptor activity (Rag-GTPase-mediated recruitment to the
lysosomal membrane), both `in_complex` `GO:0031931` TORC1 complex.

## What this example adds beyond GRB2 and LDLRAP1

- **It exercises the enzyme-substrate / `provides input for` pattern.** GRB2 and
  LDLRAP1 are *regulatory/recruitment* adaptors; RPTOR is the substrate-presentation
  case the modelling guideline treats separately. In a GO-CAM, RPTOR's
  enzyme-substrate adaptor activity `has input` the TOS-motif substrate and
  `provides input for` the MTOR kinase activity — it does not regulate it.
- **Partner identity does the work — but only for the binding term.** Sorting a
  61-row `protein binding` pile by interactor into "the enzyme" vs "the
  substrates" vs "noise" is faster and more defensible than reading 61 papers. It
  yields the right *binding* refinement (protein kinase binding) or a REMOVE; it
  does **not** license asserting the bridging *activity* (`GO:0140767`) from a
  binary hit — that stays with the IDA rows that assay it. An earlier draft
  MODIFYed eleven substrate-binding rows to the activity term; that over-claimed
  and was corrected to three `protein kinase binding` refinements plus eight
  removals.
- **Over-annotation on a hub gene is mostly pleiotropy, handled by
  KEEP_AS_NON_CORE, not REMOVE.** mTORC1 touches growth, autophagy and metabolism;
  those experimental process rows are true and were kept non-core. Only distal
  ISS/IEA rows (social behaviour, osteoclast/odontoblast differentiation,
  xenobiotic response) were marked over-annotated — consistent with not
  overruling experimental curators.
- **`contributes_to` is the right qualifier for a non-catalytic subunit.** RPTOR's
  `contributes_to GO:0004674` protein serine/threonine kinase activity was kept:
  it credits the subunit for the complex's catalytic activity without claiming
  RPTOR is itself a kinase.

## Caveat

RPTOR is a heavily-curated hub (170 annotations, 91 references, most not in the
local publication cache), so many experimental `ACCEPT` rows are deferred to the
original curators without an added verbatim quote (the validator emits advisory
`supported_by` warnings for these). The core-function claims and the partner-based
`MODIFY` calls are grounded in cached, quote-verified references.
