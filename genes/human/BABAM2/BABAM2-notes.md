# BABAM2 notes

## 2026-10-05 review (PAINT, affinage)

- BRE/BRCC45 is the UEV-domain adaptor of BRCA1-A and BRISC. It bridges BABAM1 to the rest of the complex [PMID:21282113 "Here, we found that the two complexes are assembled in a similar manner and NBA1 and BRE interaction is critical for maintaining the integrity of both of the complexes."].
- REMOVE: peroxisome signal sequence receptor activity (TAS). [PMID:11676476 "We propose that the function of BRE and its isoforms is to regulate peroxisomal activities."] Carrying a PTS1 does not make BRE a receptor.
- MODIFY the TNFRSF1A IPI to GO:0005164 and the FAS IPI to GO:0005123 (PMID:15465831). The TNF/apoptosis rows are non-core, and UniProt notes these effects may be indirect.
- Response to vitamin B6 is marked as an over-annotation (SHMT2 is the sensor). The IEP DNA damage response row is non-core.

## 2026-10-05 revision (reviewer round 1)

- Nucleus/nucleoplasm rows now quote UniProt's Nucleus line, with no unrelated paper quotes.
- NEW GO:0030674 adaptor activity (IDA, PMID:19261748) is the core MF of both complexes. It is supported by the BABAM1 bridging and by USP7 recruitment [PMID:29416040 "We show that BRE facilitates deubiquitylation of CDC25A by recruiting ubiquitin-specific-processing protease 7 (USP7) in the presence of DNA damage."].
- Fas: an earlier Y2H found no Fas binding (PMID:9737713), and the later PMID:15465831 reports binding. The MODIFY to GO:0005123 follows the later direct data, and the discrepancy is noted in the row.
- Signal transduction is marked as an over-annotation. GO:0044818 is accepted because it is a parent of the core GO:0007095.
- GOA has 70 lines. Two GO:0000152/IDA/PMID:14636569 lines are identical and the stub collapses them to one row; 69 rows were reviewed.
