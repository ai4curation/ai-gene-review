# Notes for DANRE ldhd

## 2026-05-09 review notes

- Core function is mitochondrial FAD-dependent D-lactate dehydrogenase activity in lactate catabolism [file:DANRE/ldhd/ldhd-uniprot.txt "acts specifically on D-lactate, not on its stereoisomer L-lactate"].
- Generic catalytic activity was modified to the specific D-lactate dehydrogenase and (2R)-2-hydroxycarboxylate dehydrogenase terms [file:DANRE/ldhd/ldhd-uniprot.txt "Reaction=(R)-lactate + FAD + H(+) = FADH2 + pyruvate"].
- FAD/flavin binding terms are kept as non-core cofactor annotations [file:DANRE/ldhd/ldhd-uniprot.txt "FAD-binding PCMH-type"].

## Re-review 2026-09-29

- Resolved the six PENDING rows added from the refreshed GOA (IBA mitochondrion, IBA D-lactate dehydrogenase (cytochrome), IBA D-lactate dehydrogenase (NAD+), IBA FAD binding, and the two GO_REF:0000120 Rhea-mapped IEA rows). Removed the two stale GO_REF:0000116 IEA rows that no longer exist in GOA, and updated the GO:0140174 label to the current GOA/ontology label "(2R)-2-hydroxycarboxylate dehydrogenase (FAD) activity".
- GO:0004458 D-lactate dehydrogenase (cytochrome) activity (IBA) -> ACCEPT: human LDHD was shown in 2024 to pass electrons from D-lactate directly to cytochrome c [PMID:38413804 "we could confirm direct electron transfer from d-lactate to cytochrome c by monitoring its haem absorbance"], and LDHD-knockout cells lose the D-lactate-driven membrane-potential response [PMID:38413804 "their response to d-lactate was blunted"]. The PAINT node (yeast DLD1 / plant DLD / vertebrate LDHD) is therefore sound.
- GO:0008720 D-lactate dehydrogenase (NAD+) activity (IBA) -> MODIFY to GO:0140170 with a propagation_review: the only experimental donor is Arabidopsis AT5G06580 (IMP, PMID:22155004, a selection-marker study); NAD-dependent D-LDHs are a distinct bacterial family [PMID:37863926 "The NAD-dependent D-LDHs were found in some bacteria and belong to the D-isomer specific 2-hydroxyacid dehydrogenase superfamily"], whereas LDHD is FAD/Mn2+-dependent [PMID:37863926 "mLDHD is an Mn2+-dependent general dehydrogenase for a broad range of D-2-hydroxyacids with small to moderate-size hydrophobic moieties at the C2 atom"].
- All D-lactate/(2R)-2-hydroxycarboxylate dehydrogenase (FAD) rows (EXP, ISS, IEA) and lactate catabolic process (IMP, IBA) ACCEPTED on the zebrafish mutant evidence [PMID:30931947 "metabolic analysis revealed elevated levels of D-lactate, but not L-lactate, in ldhd−/− larvae compared to wildtype"; "ldhd−/− uninjected embryos showed a significant D-lactate increase that was restored to baseline levels by mRNA microinjection of the wildtype LDHD sequence"]. FAD-binding rows kept as non-core. Deep-research quotes replaced by primary-literature quotes; PMID:37863926 and PMID:38413804 added with reference_review.
- Description rewritten as standalone biology; second core-function entry added for the cytochrome-coupled activity; suggested question/experiment added on the zebrafish electron acceptor.
