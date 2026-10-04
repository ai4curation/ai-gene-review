# ARMC5 review notes

## Sources
- Affinage: trust gates clear. Checked against the cached full texts:
  - PMID:35687106: CRL3-ARMC5 is an RPB1 E3; nuclear-cytoplasmic shuttling.
  - PMID:38225631: most Pol II subunits accumulate; neural tube defects.
  - PMID:39667934: excess and defective early Pol II, parallel with Integrator; mostly soluble, chromatin only with crosslinker.
  - PMID:39504960: Ser5P RPB1 at the pause checkpoint.
  - PMID:35862218: SREBF via the ARM repeats; CUL3 via the BTB domain.
- Partner accessions resolved by UniProt batch query, including Q96C12 = ARMC5 itself (self-interaction).
- Mouse Armc5 (Q5EBP3) donor rows (QuickGO):
  - GO:0061630 IDA from PMID:39491648: in vitro ubiquitination by the ARMC5-CUL3 complex.
  - GO:0016020 IDA from PMID:28911199: abstract-only, membrane not mentioned.

## Decisions
- ACCEPT:
  - Ubiquitin-like ligase-substrate adaptor activity, Cul3-RING complex, proteasomal degradation, Pol II transcription initiation surveillance.
  - Nucleus and cytoplasm.
- KEEP_AS_NON_CORE:
  - Chromatin and chromosome (transient).
  - Protein ubiquitination (broad IEA).
  - Anatomical structure morphogenesis (IBA).
- MODIFY:
  - Ubiquitin protein ligase activity (IEA) → ligase-substrate adaptor: ARMC5 is the BTB receptor, not the RING subunit.
  - CUL3 binding → cullin family protein binding.
- UNDECIDED: membrane (IEA from mouse).
- REMOVE: 25 other protein-binding rows (policy). The POLR2A substrate relationship is captured by the adaptor rows.
