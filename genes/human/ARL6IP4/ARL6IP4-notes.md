# ARL6IP4 (SR-25 / SRrp37) review notes

## Sources
- Affinage record: trust gates clear; four cited papers, all checked.
- PubMed alias recall (ARL6IP4, SRrp37, SFRS20) returned 11 hits, mostly expression-signature papers; the functional literature is PMID:19582790 (SRrp37), PMID:10708573 (cloning), PMID:11884129 (HSV splicing inhibitor), PMID:28105234 (cyclophilin A).
- Location: nucleoli and nuclear speckles by antibody immunofluorescence and myc-tag [PMID:19582790 "demonstrated that SRrp37 was localized in nucleoli and nuclear speckles."]. HPA main location is nucleoplasm, with an additional mitochondria call. No OpenCell line was found.

## Decisions
- RNA binding (two mRNA interactome captures) → ACCEPT, used as the core MF.
- Nucleus TAS → ACCEPT (the cloning paper's prediction, later confirmed by imaging).
- Nucleolus, nuclear speck IEA (UniProt SubCell, from PMID:19582790) → ACCEPT.
- RNA splicing TAS → MODIFY to GO:0000381 regulation of alternative mRNA splicing, via spliceosome, based on the minigene reporter results [PMID:19582790 "we found that SRrp37 modulated alternative 5' and 3' splicing in vivo."].
- SRPK1/SRPK2 protein binding (5 rows, 4 independent studies) → MODIFY to protein kinase binding.
- IKBKG and FOS protein binding → REMOVE (policy).
