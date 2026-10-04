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
- **No NEW.** The adhesion-mediator MF has only rat/zebrafish evidence.
