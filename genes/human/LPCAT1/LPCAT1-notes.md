# LPCAT1 review notes

## 2026-11-04: DeepTMHMM2 S20 topology audit

Source: [DeepTMHMM2 v1](https://doi.org/10.64898/2026.08.24.746435), supplied workbook `media-1.xlsx`, S20 row 7, Q8NF37. Author evidence category: **Peripheral**. These are the authors' predictions, with one-based inclusive coordinates:

`transit_peptide(1-5); Cytoplasmic(6-40); interfacial(41-66); Cytoplasmic(67-97); interfacial(98-110); Cytoplasmic(111-254); interfacial(255-261); Cytoplasmic(262-534)`

**Assessment: Correct conflicting topology rationale.** PMID:21498505 explicitly reports monotopic topology for human LPCAT1 and LPCAT2, consistent with ER bilayer and lipid-droplet monolayer association. Correct the review row that instead repeats single-pass type II topology, retaining the ER membrane term. Record the incompatible UniProt description as a source defect. Do not turn the S20 five-residue transit-peptide prediction into a mitochondrial targeting claim.

The complete source row, workbook hash and cross-gene decisions are retained in [the audit](../../../projects/DEEPTMHMM2.md). Membrane-contact geometry is considered separately from organelle localization and molecular function; no new function/process annotation is derived from this prediction.
