# tusE curation notes

## Functional assignment

PP_3996/Q88FT6 is the TusE-family terminal sulfur carrier in the contiguous
PP_3993-PP_3996 `tusD-tusC-tusB-tusE` locus. The target retains the terminal
cysteine noted by the OpenScientist sequence analysis and has the local
IPR007453 DsrC/TusE family assignment.
[file:PSEPK/tusE/tusE-uniprot.txt "DR   InterPro; IPR007453; DsrC/TusE."]

The mechanistic assignment comes from the reconstituted *E. coli* relay: TusE
promotes TusA-to-TusD sulfur transfer and interacts with MnmA-tRNA.
[PMID:16387657 "TusE also interacts with an MnmA-tRNA complex."] No direct
KT2440 sulfur-transfer experiment was identified, so the species assignment is
based on family, conserved residue, and operon context.


## 2026-11-07 — complete source-aware review

All original rows and historical NEW proposals are retained in their original order and source payload. The review now distinguishes target-specific family/curated-site inference from E. coli experiments; no KT2440 assay is invented. The soluble location is inferred from the conserved reaction/complex context, not ARBA-only annotation. Broad true rows are refined where ontology ancestry supports it; covalent sulfur-carrier and sulfurtransferase terms are not treated as a false hierarchy.

Covalent sulfur carriage downstream of TusBCD toward the MnmA–tRNA reaction; conserved KT2440 role without assuming that direct MnmA persulfide loading has been experimentally resolved.

Evidence and exact source/access limits are in [the consultation](../../../analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/evidence.md). A reproducible frozen-sequence alignment independently checks conserved sites rather than quoting generated provider claims. Existing OpenScientist material is discovery provenance. A normal Falcon attempt for this gene failed HTTP403 authentication; the actual log is retained at `analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/falcon-tusE.log`. No provider report was fabricated.

The earlier notes are preserved as historical text. Where they describe C5 modification as obligatorily downstream, assert a directly established KT2440 reaction or operon expression, or equate carrier with a catalytic GO descendant, this append and the current review supersede that wording. No NEW annotation was added to fill a core-coverage warning.

## 2026-11-07 — PR6199 source-specific follow-up

TusE assignment is grounded in target PTHR37010:SF1 and the PIRSR006223-50 Cys110 persulfide site, rather than the broader TIGR03342 DsrC/TusE/DsvC grouping alone. The frozen PP_3993–PP_3996 records and their distinct TusD/C/B/E classifications support neighborhood and a matched relay inference; they do not demonstrate cotranscription or native KT2440 flux. Cytosol is inferred from the conserved soluble relay. The former OpenScientist LOW_QUALITY reference assessment is preserved exactly in review-round1-consultation/superseded-assertions.json; it remains historical context and is not used as primary evidence.
