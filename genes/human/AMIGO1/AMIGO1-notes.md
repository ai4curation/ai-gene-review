# AMIGO1 (Q86WK6) review notes

## 2026-10-04: PAINT/affinage review

AMIGO1 has two roles: developmental adhesion molecule, and adult Kv2 auxiliary subunit.
- **Adhesion:** rat AMIGO binds the AMIGO family [PMID:12629050 "A homophilic and heterophilic binding mechanism is shown between the members of the AMIGO family."]
- **Kv2.1 auxiliary subunit in mouse:** [PMID:22056818 "AMIGO increases Kv2.1 conductance in a voltage-dependent manner in HEK cells."]
- **Restricted to Kv2 channels in adult mammalian brain:** (PMID:29403353).
- **No human experimental data.** Every non-HuRI row is inferred from rat (Q80ZD7) or mouse (Q80ZD8).

Decisions:
- **Kv2 regulator, channel complex, potassium-transport, somatic-membrane, adhesion and fasciculation rows: ACCEPT.**
- **Myelination (ISS/IEA): MARK_AS_OVER_ANNOTATED.** The rat source is IEP: expression rises at myelination onset.
- **Kept as non-core:**
  - axonogenesis and neurite-outgrowth rows (culture assay);
  - brain development;
  - axon;
  - cellular response to L-glutamate (rat IDA; really Kv2.1 relocalization);
  - pericellular basket (rat staining).
- **38 HuRI protein-binding rows: REMOVE.**
- **NEW GO:0098632 cell-cell adhesion mediator activity (ISS from rat Q80ZD7)**, added in round 1 as the MF counterpart of the accepted adhesion BP rows.

## Round 1 (PR #4000 review)

- **Zebrafish evidence cited.** PMID:24904058: knockdown disrupts fasciculated tracts.
- **Dendrite rows** now cite "primarily present on the cell bodies and proximal dendrites" (PMID:29403353) and PMID:21938721.
- **GO:0015459 rows (IBA, IEA, ISS): MODIFY to GO:0099104 potassium channel activator activity**, since all the evidence is an increase in conductance. The IBA row carries propagation_review NO_FAILURE_CORE / GRANULARITY_MISMATCH.
- **core_functions** now has GO:0099104 with in_complex GO:0008076, plus an adhesion core with GO:0098632 (changed from GO:0098631 in round 2).
- **Neurite-growth rows** now cite in vivo evidence: horizontal-cell axons are smaller in the knockout (PMID:35169021). They stay non-core as cell-type-specific effects.

## Round 2 (PR #4000 review)

- **propagation_review was on the wrong rows.** My builder applied it to all three GO:0015459 rows. Only the IBA row passes through a PAINT node, so it is now confined there (verified by reading the file back).
- **Dendrite citation removed from axonogenesis rows.** PMID:21938721 (dendritic growth) is no longer cited on GO:0007409 or GO:0050772 and is kept on GO:0010976 only.
- **Adhesion MF:** NEW and core MF changed to GO:0098632, the cell-cell term the comparator argument actually supports.
- **Description:** the Kv2.1 effect is stated as a voltage-dependent conductance increase, without an uncited activation-shift claim.
