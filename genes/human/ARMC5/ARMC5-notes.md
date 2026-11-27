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
  - Protein ubiquitination (broad IEA).
  - Anatomical structure morphogenesis (IBA).
- MODIFY:
  - Ubiquitin protein ligase activity (IEA) → ligase-substrate adaptor: ARMC5 is the BTB receptor, not the RING subunit.
  - CUL3 binding → cullin family protein binding.
- UNDECIDED: membrane (IEA from mouse).
- REMOVE: 25 other protein-binding rows (policy). The POLR2A substrate relationship is captured by the adaptor rows.

## Review round 1 (PR #4188)
- Chromatin and chromosome are now ACCEPT, and chromatin is a core-function location. PMID:39854452 (SPT5/CUL3-ARMC5, full text) shows GFP ChIP-seq occupancy of ARMC5 at promoter-proximal regions that is CDK9-dependent, and identifies ARMC5 as the adaptor for chromatin-bound, SPT5-depleted Pol II. PMID:39667934's "mostly soluble" result is still noted.
- The CUL3 binding MODIFY now cites PMID:32023208 (BTB-dependent CUL3 binding).
- The GO:0061630 MODIFY is noted as merging into the GO:1990756 IEA row.
- Two truncated sentence-splitter quotes were replaced, and the duplicate supported_by entries removed.
- The GO:0009653 reason is reframed as a non-core developmental role.
- NRF1 (PMID:36040830) and USP7 (PMID:33544460) are cached but not used for annotations: NRF1 turnover is a single adrenal study, and USP7 regulates ARMC5 rather than being an ARMC5 activity.
