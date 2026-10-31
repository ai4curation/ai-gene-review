# PMCHL2 notes (Q9BQD1, Putative pro-MCH-like protein 2)

## 2026-10-04 Tier 3 over-annotation audit (claude-code)

### Does the product exist?
- UniProt: PE5 (Uncertain); CAUTION "Could be the product of a pseudogene". Tissue: testis, not brain.
- HGNC (REST, fetched 2026-10-04): "pro-melanin concentrating hormone like 2 (pseudogene)", locus_type `pseudogene`, 5q13.2, Entrez 5370.
- Origin: duplication of a ~92 kb segment containing PMCHL1 from 5p14 to 5q13 in the hominid lineage [PMID:11181993 "PMCHL2 arose 5 to 10 Ma by an event of duplication involving a large chromosomal region encompassing the PMCHL1 locus"]; [PMID:19068116 "PMCHL2 arose by duplication of a 92 kb fragment (in grey) encompassing PMCHL1 onto chromosome 5q13."].
- Truncation: 5'-truncated version of PMCH, like PMCHL1 [PMID:11070051 "They correspond to a 5'-end truncated version of the MCH gene"].
- Expression: not transcribed in brain [PMID:11070051 "we provided strong evidence for the expression of the PMCHL1 gene but not the PMCHL2 gene in the human fetal, newborn, and adult brains"]; [PMID:9729295: brain antisense product "derived from the 5p (pMCHL1), not the 5q (pMCHL2) locus"]. Testis only [PMID:19068116 "Thus, PMCHL1 transcripts are found in testis and fetal brain and are more abundant than PMCHL2 transcripts that are observed only in testis."].
- Protein: Schmieder 2008 antiserum to the VMCH-p8 N-terminal epitope detected nothing in human adult testis, and nothing in HEK293 cells transfected with ORF1-bearing PMCHL1/2 sequences [PMID:19068116 "This strongly suggests that these putative proteins are not translated in vivo in the human and macaque tissues that we tested."]. Note: the PMCHL2 N-terminus is KTKKK rather than KPKKK, so the epitope may differ slightly; the paper does not say whether its antiserum recognises the PMCHL2 variant. Treat protein absence for PMCHL2 as likely but slightly less directly shown than for PMCHL1.

### Sequence vs parent PMCH (PMCHL2-bioinformatics/RESULTS.md)
- Q9BQD1 2-86 aligns to PMCH 81-165 (83.5% identity); PMCH 1-80 incl. signal peptide absent.
- MCH-like segment: M150T, R160Q, P161R; Cys retained. NEI-like: I132T, amidated I143 retained.

### Propagation routes
- IBA GO:0031777, GO:0032227: PANTHER PTN002636265 (IBD taxon:117571 Euteleostomi, seed RGD:3358 rat Pmch); PMCHL2 in PTHR12091:SF1 with PMCHL1.
- IEA GO:0030354, GO:0007268: InterPro2GO IPR005456. GO:0007165, GO:0045202: GOC inter-ontology inference.
- (No NAS extracellular row, unlike PMCHL1.)

### Decision
All 6 rows REMOVE. No core function.
