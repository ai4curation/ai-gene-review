# CRN (CORYNE / SOL2, At5g13290; UniProt Q9LYU7) curation notes

## Identity
- SOL2 was identified from a root CLE19 suppressor screen, and CRN from shoot genetics. They are the same gene [PMID:18854335 "SOL2 encoded a receptor-like kinase protein which is identical to CORYNE (CRN)."].
- UniProt Q9LYU7 is "Inactive leucine-rich repeat receptor-like protein kinase CORYNE". The SOL2 symbol also collides with TCX2 (At4g14770); the correct entry was verified by AGI locus.
- The protein has a short extracellular region, one TM helix, and a kinase-like domain. The deep research (falcon) confirms the "short extracellular segment rather than an extracellular leucine-rich-repeat binding domain".

## Pseudokinase
- The catalytic loop is HYN instead of HRD, and the G-loop is GXDXXG. There is no in vitro autophosphorylation, and kinase-dead K146E complements crn-1 [PMID:21398569 "No activity was seen for either CRN protein, suggesting that wild-type CRN lacks autokinase activity under standard conditions."].
- The kinase-like domain is still needed for SAM signalling but not in the root [PMID:27229734].
- Decisions: the NOT protein kinase activity row is ACCEPTED. The IEA ATP binding is REMOVED, because the degenerate G-loop is predicted to inhibit ATP binding and no binding has been shown.

## Complex and trafficking
- CRN binds CLV2 via TM/juxtamembrane contacts, and the two require each other for ER export [PMID:19933383].
- It interacts weakly with CLV1 [PMID:19843317], and with CIK1-4 [PMID:29581511] and MAZZA [PMID:33909893].
- In roots, CRN stabilizes BAM3 [PMID:28607033 "CRN stabilizes BAM3 expression and thus is required for BAM3-mediated CLE45 signaling"].

## Core MF choice
- Signaling receptor complex adaptor activity (GO:0030159). It reflects the scaffold role suggested by Nimchuk 2011 [PMID:21398569 "CRN may play a scaffolding role, perhaps to aid export of CLV2 to the plasma membrane"] and the BAM3 stabilization.
- The IMP peptide receptor activity is MODIFIED to this term, because CRN has no ligand-binding ectodomain.

## Removed
- Mitochondrion (ISM), which is contradicted by the experimental plasma membrane and ER localization.
