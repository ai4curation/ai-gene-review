# Rtl9 / SIRH10 / Rgag1 (mouse, Q32KG4) notes

Eutherian-specific, X-linked domesticated sushi-ichi Gag gene. Large (~1339 aa) protein; only recognizable structured module is a C-terminal PEG10/RTL1 capsid-like (Gag) domain; long N-terminal region disordered. Expressed in brain microglia; RTL9 localizes to microglial lysosomes (not secreted); required for degradation of phagocytosed fungal zymosan via its C-terminal Gag region [PMID:37834332]. GOA rows are all ND placeholders.

Calls: ND MF ACCEPT (enzymatic status unknown); ND CC MODIFY -> lysosome; ND BP MODIFY -> cellular response to molecule of fungal origin + innate immune response.

## Deep research integration (OpenScientist, 2026-10-24)

Report read as leads; checked against cached sources. No contradiction with the review calls.

- Lysosomal (not extracellular) localization corroborated by the review [PMID:42511665 "In contrast to SIRH3/RTL6 and SIRH8/RTL5, which are distributed extracellularly, SIRH10/RTL9 was predominantly localized within microglial lysosomes"]. Added to the lysosome row. The sibling RTL5/RTL6 comparator [PMID:36162816 "Both proteins are present as intra- as well as extracellular granules in the brain"] added as a reference.
- KO phenotype corroborated [PMID:42511665 "In Sirh10/Rtl9 KO mice, zymosan signals persisted in the brain after administration, suggesting that SIRH10/RTL9 contributes to the clearance of fungal-derived PAMPs in the brain"]. Added to the BP row.
- Architecture: the review had said the N-terminus is "largely disordered"; the review corroborates that most of RTL9 is instead homologous to herpesvirus-like sequences [PMID:42511665 "More than two-thirds of the protein consists of regions homologous to two distinct herpesvirus-like sequences, whereas the Gag-derived region is restricted to the C-terminal portion"]. Description updated to add this; the Gag-only "recognizable structured module" statement from UniProt is kept.
- The report (and the human RTL9 report) note human RGAG1 as a BCOR fusion partner in rare sarcomas and in Xq deletions, but these describe the locus, not protein function, so no annotation follows. Not catalytic status: still ND for MF, since no enzymatic activity is shown [PMID:37834332 states the enzymatic status cannot be determined]. The report agrees this is an open question.
- Human RTL9 (Q8NET4) report exists separately and is consistent; the mouse Gag domain is ~78% identical to human per the human report (not independently verified here).

No action changes.
