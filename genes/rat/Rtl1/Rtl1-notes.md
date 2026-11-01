# Rtl1 / Peg11 (rat, M0R9G4) — review notes
SIRH2; full gag-pol (capsid + aspartic protease + RT + RNaseH). All GOA rows ISO/IBA/IEA from mouse. Calls mirror mouse Rtl1: placenta/labyrinth/angiogenesis/muscle/satellite-cell/Z-disc ACCEPT; gene expression MARK_AS_OVER_ANNOTATED (with propagation_review). NEW GO:0039660 structural constituent of virion (ISS). No openscientist report for rat.

## Deep research integration (OpenScientist, 2026-10-24)

An OpenScientist report has since arrived (Rtl1-deep-research-openscientist.md). Checked against cached sources:

- Correction: the review description said the protease domain has a "DSG motif". The rat UniProt sequence (M0R9G4) has DTG: ALVDTGVEG with D at residue 704, inside the "PEG10/RTL1 protease" domain 700..808. The report is right on this point (mouse and human have DSG). Description fixed. This does not change the catalytic-activity convention: no RTL1 protease activity has been shown, and sheep PEG11 protein is full length, with the authors inferring the protease is "either inactive or did not have autolytic activity" [PMID:20072617].
- The report says the protease motif "is required for function" in RTL1. Only the PEG10 motif was tested [PMID:34559199]; treated as unsupported for RTL1.
- Cell type: "It should be noted that, in contrast to Peg10, Rtl1 is only expressed in endothelial cells (Sekita et al., 2008)." [PMID:34559199]; human IHC: "IHC examinations identified RTL1, DLK1 and DIO3 protein expressions in the vascular endothelial cells and pericytes of chorionic villi, but not in the cytotrophoblasts, syncytiotrophoblasts, and stromal cells" [PMID:22917972]. Description updated; added to the angiogenesis row with the Peg10-Rtl1 interaction quote [PMID:34559199].
- Brain expression and behaviour [PMID:33484574, PMID:35567414]: rat GOA has no neural terms and these are mouse data; no NEW term proposed.
- Callipyge transgenic hypertrophy [PMID:26474044] supports the muscle role; already ACCEPTed.

No action changes. Cross-species note: human RTL1 and mouse Rtl1 use DSG, so the human description ("DSG motif") is correct; only rat differs.
