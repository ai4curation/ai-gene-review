# SEP1 (AGL2, At5g15800, P29382) notes

## 2026-10-05 — initial review (floral_organ_identity_abce module)

- Identity: UniProt P29382 SEP1_ARATH, gene SEP1/AGL2, At5g15800. Checked against the uniprot file.
- Deep research: `just deep-research-falcon ARATH SEP1` failed (HTTP 402 from the provider). No deep-research file was made, so the review uses the cached primary literature.
- E-class function: the sep1 sep2 sep3 triple mutant makes sepals in every whorl [PMID:10821278 "Triple mutant Arabidopsis plants lacking the activity of all three SEP genes produce flowers in which all organs develop as sepals."]. Adding SEP4 converts organs to leaf-like organs [PMID:15530395].
- DNA binding: AGL2 binds CArG DNA as a dimer [PMID:8597661 "AGL2 binds to DNA in vitro as a dimer"].
- Expression is in the whole floral meristem and all four organ primordia [PMID:7948914 "The AGL2 transcript is very abundant and uniform throughout the floral meristem and in the primordia of all four floral organs"]. The GOA IDA "flower development" row rests on this expression study. I changed it (MODIFY) to specification of floral organ identity, which the genetics supports.
- Partners: AGL2 was isolated as an AG K-domain interactor [PMID:9418042]. Other partners are AP1, ABS/TT16, AGL16, AGL24 and SHP2 (MADS), each MODIFY to GO:0046982. The non-MADS CrY2H hits (At3g24490 Myb/SANT; ARF46) are REMOVE as uninformative.
- Ovule: the SEP1/sep1 sep2 sep3 genotype gives ovule-identity defects [PMID:14555696]. Marked KEEP_AS_NON_CORE.
- NEW: GO:0010093 IMP from PMID:10821278. The same paper supports the existing SEP3 GO:0010093 IMP, and the triple-mutant genotype removes SEP1.
