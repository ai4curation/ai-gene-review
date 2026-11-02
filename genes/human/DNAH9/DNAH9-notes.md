# DNAH9 curation notes

## Deep research
Falcon deep research failed twice ("Failed to authenticate"); no deep-research
file. Review based on cached publications and UniProt.

## Biology summary (with provenance)
- Beta heavy chain of distal type 2 ODAs with DNAH5 [PMID:30471717 "DNAH9 and its
  partner heavy chain DNAH5 localize to type 2 ODAs of the distal cilium"].
- Distal versus proximal paralog split with DNAH11 [PMID:30471718 "Both signals do
  not overlap indicating a distinct distal and proximal localization of
  β-heavy chain paralogs DNAH9 (green) and DNAH11 (magenta), respectively."].
- Binds docking complex subunit ODAD1/CCDC114 via DHC1 region [PMID:30471718
  "docking of ODAs type 2 occurs via direct interaction of DNAH9 with the docking
  complex protein CCDC114"]; co-IP with DNAH5 fragments and DNAI2.
- Loss: reduced beat frequency, subtle distal waveform defect [PMID:30471717].
- Expressed in nodal pit cells (mouse) [PMID:30471718].
- Early expression in airway ciliogenesis [PMID:11104725, PMID:11839535].
- Absent from human sperm axoneme [PMID:31178125].

## Annotation decisions
- protein binding (IPI ODAD1) modified to protein-containing complex binding
  (ODAD1 is an outer dynein arm docking complex subunit, GO:0120228).
- Centriole (HPA) and sperm end piece (HPA IDA, ARBA IEA) marked over-annotated:
  conflict with PMID:31178125.
- Sperm flagellum IDA from the DNAH3 paper (PMID:39503742) left UNDECIDED: the
  cached text mentions DNAH9 only in a Discussion list of PCD-causing DNAH genes.
- dynein complex (IEA, IBA) modified to outer dynein arm.

## PANTHER / IBA check
Human DNAH9 (Q9NYC9) and mouse Dnah9 (B1AR51) have identical IBA sets (7 terms).
The beta heavy chains receive only generic dynein complex/axoneme IBAs (nodes
PTN000743491, PTN000073047), unlike the gamma chain DNAH5 which inherits outer
dynein arm from PTN002472868.

## Review follow-up (October 2026)
- GO:0120228 label checked in OLS (GO): "outer dynein arm docking complex".
- GOA has two identical protein binding IPI rows for PMID:30471718 with ODAD1
  (Q96M63), differing only in assigned_by (IntAct and UniProt). They are one claim,
  so the review carries a single row for them; this is deliberate.
- 9+2 motile cilium and distal portion of axoneme IDA rows (PMID:26909801): the
  cached abstract does not mention DNAH9, so these rows now quote PMID:30471717
  and the UniProt subcellular location instead of the PMID:26909801 title.
- dynein light intermediate chain binding (IBA, IEA) changed to REMOVE: the outer
  dynein arm has no light intermediate chain subunit, so the claim is unlikely to
  be correct rather than merely under-supported.
- microtubule-based process and microtubule-based movement set to TOO_GENERAL;
  cilium movement dropped from core_functions as it is entailed by epithelial
  cilium movement involved in extracellular fluid movement.
