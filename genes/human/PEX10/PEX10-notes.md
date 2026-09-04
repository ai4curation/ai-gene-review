# PEX10 (O60683) curation notes

## 2026-09-04 — Finishing pass (PAINT no-IBA project)

Completed the review pass over all existing annotations; status moved IN_PROGRESS → COMPLETE
(validation clean, zero warnings). The draft was already in good shape — every action was
assigned and evidence-cited. Changes made:

1. **Cleared the `in_complex` warning by adding an `action: NEW` annotation for GO:0000151
   (ubiquitin ligase complex)** (IDA, PMID:35768507). core_functions declared PEX10 in the
   ubiquitin ligase complex but GOA carries no complex-membership CC term. The complex is
   structurally demonstrated
   [PMID:35768507 "Recycling requires receptor modification by a membrane-embedded ubiquitin
   ligase complex comprising three RING finger domain-containing proteins (Pex2, Pex10 and
   Pex12)"] and biochemically supported — PEX12 complex formation dramatically augments
   PEX10's E3 activity
   [PMID:24662292 "Here, we report that RING finger of human Pex10p possesses ubiquitin
   ligase activity with E2 UbcH5C and that the E3 activity is dramatically augmented by
   formation of a Pex10p complex with Pex12p"], with co-IP support from PMID:10837480.

2. **Changed the PMID:10837480 GO:0005515 (protein binding, IPI) action from MODIFY to
   MARK_AS_OVER_ANNOTATED.** The previous MODIFY proposed GO:0061630 (ubiquitin protein
   ligase activity) as a replacement, but the IPI evidence in that paper supports complex
   assembly (PEX10–PEX12/PEX2/PEX5 interactions), not catalysis; the catalytic MF is already
   independently annotated with IDA. The complex membership the binding data actually
   supports is now recorded via the NEW GO:0000151 annotation. This also matches the
   treatment of the identical PMID:10837480 protein-binding annotation on PEX2.

3. **Cited the deep research file** (`file:human/PEX10/PEX10-deep-research-falcon.md`) in
   the references list and in the NEW GO:0000151 annotation — its synthesis of 2024 reviews
   (Kumar et al., Skowyra et al.) frames the heterotrimeric PEX2/PEX10/PEX12 ligase/
   retrotranslocon as the central concept for PEX10 annotation, and distinguishes PEX10+PEX12
   RADAR polyubiquitination from PEX2's monoubiquitination role — which corroborates the
   KEEP_AS_NON_CORE calls on the RADAR-related terms (GO:0006515, GO:0043161).

Everything else was reviewed and left as drafted: the ACCEPTs on the import/recycling core
(GO:0016558, GO:0016562, GO:0061630, GO:0000209) are all backed by verbatim full-text quotes;
the MARK_AS_OVER_ANNOTATED on GO:0034614 (cellular response to ROS, PMID:26344566) is
justified because in that paper ATM is the ROS sensor and PEX10 merely executes its
constitutive E3 function downstream (contrast PEX2, which has independent ROS-sensor
evidence in PMID:34903883 and keeps the term as non-core).

Final action tally: 34 ACCEPT, 3 KEEP_AS_NON_CORE, 2 MARK_AS_OVER_ANNOTATED, 1 NEW,
0 REMOVE, 0 UNDECIDED, 0 PENDING.

Notable curation finding: PEX10 receives no IBA for its E3 ligase activity or receptor
recycling despite these being deeply conserved and experimentally grounded in human — only
GO:0016558 and GO:0005778 come through IBA. See
interpro/panther/PTHR23350/PTHR23350-review.yaml for the family-level analysis.
