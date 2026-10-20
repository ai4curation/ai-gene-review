---
title: "Reactome MF verdict vocabulary"
---

# Reactome MF verdict vocabulary

[Back to Reactome-GO Alignment](../REACTOME.md)

**Bottom line:** every `Reactome:R-*` row should be classified at the same
granularity as the Reactome object that supports it. Reaction-like events can
support molecular functions on the protein that executes the chemistry or
transport; pathway containers can support only pathway/BP context; complex
events need the active member separated from scaffold, assembly, and regulatory
members. These verdicts give the inventory a compact way to count the repeated
cases before each affected gene review receives its final `ACCEPT`, `MODIFY`,
`MARK_AS_OVER_ANNOTATED`, `REMOVE`, or `UNDECIDED` action.

## Verdicts

| Verdict | Use when | Typical curation action |
|---------|----------|-------------------------|
| `reaction_mf_exact` | The stable ID is a catalyzed reaction or transport event, the gene product is the executor, and the GO MF matches the event chemistry or transported substrate class at the right specificity. | `ACCEPT` |
| `reaction_mf_refine` | The event is mechanistically sound evidence for the gene product, but the exported or local GO term is too broad, too narrow, or missing a substrate qualifier implied by the reaction. | `MODIFY` |
| `reaction_context_only` | The Reactome event is good evidence for localization or non-core pathway context on the executor, but it is not the row that should carry the molecular-function assertion. | `ACCEPT` or `KEEP_AS_NON_CORE` for CC/BP rows; keep out of MF counts |
| `complex_active_member` | A protein complex executes the reaction and this gene product is the catalytic, transport, receptor, or adaptor subunit that directly supplies the MF. | `ACCEPT`, often with explicit complex context |
| `complex_contributes_to` | The member is required for a complex MF but does not itself contain the active site or transport pore. | `MODIFY` to a `contributes_to` activity when available |
| `complex_over_export` | Reactome or GOA flattened a complex-level MF onto a scaffold, accessory, assembly, or regulatory subunit that does not perform the activity. | `MARK_AS_OVER_ANNOTATED` or `REMOVE` |
| `wrong_executor` | The Reactome event or GOA row names a real reaction, but the MF belongs to the redox partner, transfer partner, catalytic partner, or carrier rather than to this gene product. | `REMOVE` |
| `regulator_not_executor` | The gene product regulates or accelerates a reaction but is not itself the GTPase, kinase, transporter, or other executor named by the MF. | `REMOVE` |
| `wrong_transport_mechanism` | The gene product moves cargo by vesicle selection, sorting, or another non-channel/non-carrier mechanism, while the GO term asserts movement across a lipid bilayer. | `REMOVE` |
| `wrong_go_branch` | The Reactome reaction is assigned to the wrong molecular-function branch, such as an oxygen-acceptor methyltransferase exported as an S-methyltransferase. | `REMOVE` or `MARK_AS_OVER_ANNOTATED` |
| `obsolete_go_term` | The row uses an obsolete GO molecular-function term even if the underlying reaction evidence is otherwise interpretable. | `REMOVE` or `MODIFY` |
| `activity_contradicted` | The stable ID comes from a family or legacy event that is contradicted by direct evidence for this paralog or by explicit NOT annotations on the same gene. | `REMOVE` |
| `contested_direct_activity` | The Reactome event records a historical direct-activity model that has been weakened by newer mechanism work and should not be treated as settled. | `MARK_AS_OVER_ANNOTATED` or `UNDECIDED` |
| `nonphysiological_side_activity` | The reaction has weak in-vitro support but is not a physiological or representative function of the gene product. | `MARK_AS_OVER_ANNOTATED` or `KEEP_AS_NON_CORE` |
| `pathway_container_bp` | The stable ID names a Reactome pathway and the gene product performs one of the pathway's molecular steps, making the BP assertion valid but less precise than the direct MF. | usually `KEEP_AS_NON_CORE` |
| `pathway_container_overreach` | A pathway stable ID is being used as if it were a reaction, or the pathway/BP assertion only reflects downstream necessity, a substrate role, or generic membership. | `MARK_AS_OVER_ANNOTATED`, `MODIFY`, or `REMOVE` |
| `input_product_only` | The entity linked to the event is only consumed, produced, or carried by the reaction and does not catalyze, transport, recruit, or structurally enable the step. | `REMOVE` for executor-like MF/BP rows |
| `black_box_gap` | Reactome records that the reaction occurs but has no assigned catalyst or transporter, and AIGR has a plausible candidate from gene reviews. | feed into `REACTOME_GAP_FILLING`, not an automatic GO row |
| `boundary_mismatch` | A transport or membrane event uses the right substrate class but the GO term, compartment, or direction crosses a different boundary than Reactome. | `MODIFY` or `UNDECIDED` |
| `insufficient_event_detail` | The cached Reactome Markdown is a pathway summary or free-text statement that does not expose enough participants, compartments, or catalyst roles to decide. | `UNDECIDED` until the event graph can be checked |

## Counting Rules

- Count the Reactome stable ID itself, not only the GO term. One GO term can be
  clean for a reaction stable ID and over-broad for a pathway-container stable
  ID.
- Classify pathway stable IDs before comparing MFs. A pathway container that
  mentions the reaction family is still not one individual MF event.
- Assign `complex_active_member`, `complex_contributes_to`, or
  `complex_over_export` only after checking which entity supplies the active
  site, pore, receptor binding, adaptor recruitment, or structural cofactor
  activity.
- Use `input_product_only` for substrates and products that are necessary but
  passive. Those relationships belong on the executor through `has input`, not
  as a process annotation on the substrate.
- Use `black_box_gap` for missing Reactome participants. It is a Reactome
  curation candidate first; a new GO annotation still needs ordinary gene-level
  evidence.
- Keep manual splits for `REMOVE` and `MARK_AS_OVER_ANNOTATED` rows in
  [`mf_manual_verdicts.tsv`](mf_manual_verdicts.tsv). A review action alone
  does not distinguish a wrong GO branch from a regulator/executor swap or a
  paralog-specific contradiction.

## Pilot Calibration

The first purine nucleotide interconversion pilot establishes two positive
controls and one exclusion:

| Stable ID | Verdict | Reason |
|-----------|---------|--------|
| `R-HSA-111524`, `R-HSA-73794`, `R-HSA-73792`, `R-HSA-76590` | `reaction_mf_exact` | Each stable ID is a direct soluble reaction and its chemistry matches the local ADSS, IMPDH, GMPS, or AMPD MF. |
| Same four reaction IDs on human gene-review cytosol rows | `reaction_context_only` | The rows in completed reviews are accepted CC rows, not MF rows, even though the same event also matches a local MF. |
| `R-HSA-73817` | `pathway_container_bp` | The stable ID names a purine biosynthesis pathway; it can support BP context but is excluded from one-to-one reaction/MF matching. |

## MF Failure-Mode Calibration

The first manual pass over `MARK_AS_OVER_ANNOTATED` and `REMOVE` MF rows split
37 previously blank rows:

| Failure mode | Rows | Typical example |
|--------------|------|-----------------|
| `reaction_mf_refine` / `broad_parent_or_duplicate` | 19 | Correct Reactome reaction, but exported to a broad parent such as `GO:0008168` methyltransferase activity |
| `activity_contradicted` | 5 | A Reactome family event assigned to a paralog whose direct biochemistry contradicts the family activity |
| `contested_direct_activity` | 3 | Historical MAGT1/TUSC3 magnesium-transporter events versus newer OST-B oxidoreductase evidence |
| `regulator_not_executor` | 3 | RGS or GAP regulators exported as the substrate GTPase |
| `wrong_executor` | 2 | A redox or cofactor-transfer partner receiving the enzyme or carrier MF |
| `wrong_go_branch` | 2 | Correct chemical event mapped to the wrong GO branch |
| `nonphysiological_side_activity` | 1 | A weak in-vitro steroid reaction exported as an SRD5A3 MF |
| `obsolete_go_term` | 1 | An old ATPase-coupled anion transporter term on CFTR |
| `wrong_transport_mechanism` | 1 | AP-4 cargo selection exported as transmembrane protein transport |
