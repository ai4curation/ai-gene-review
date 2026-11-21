# TOMM22 review notes

## 2026-11-04: DeepTMHMM2 S20 topology audit

Source: [DeepTMHMM2 v1](https://doi.org/10.64898/2026.08.24.746435), supplied workbook `media-1.xlsx`, S20 row 20, Q9NS69. Author evidence category: **No**. These are the authors' predictions, with one-based inclusive coordinates:

`Cytoplasmic(1-47); interfacial(48-84); Cytoplasmic(85-142)`

**Assessment: Reject predicted topology change; refine broad terms.** PMID:10982837 directly establishes human TOMM22 as an integral outer-membrane protein with N terminus in the cytosol and C terminus in the intermembrane space. S20 classifies its non-spanning prediction as No. Retain the single-pass topology, accept root mitochondrion annotations, and refine generic membrane to outer membrane rather than calling a true broad location over-annotated.

The complete source row, workbook hash and cross-gene decisions are retained in [the audit](../../../projects/DEEPTMHMM2.md). Membrane-contact geometry is considered separately from organelle localization and molecular function; no new function/process annotation is derived from this prediction.
