# PMCHL1 notes (Q16048, Putative pro-MCH-like protein 1)

## 2026-10-04 Tier 3 over-annotation audit (claude-code)

### Does the product exist?
- UniProt: PE5 (Uncertain); CAUTION "Could be the product of a pseudogene"; PMID:9729295 found only antisense PMCHL1 transcripts in brain.
- HGNC (REST, fetched 2026-10-04): name "pro-melanin concentrating hormone like 1 (pseudogene)", locus_type `pseudogene`, 5p14.3, Entrez 5369.
- Origin: chimeric primate-specific gene. [PMID:11181993 "the PMCHL1 gene was created near 25 million years ago (Ma) by a complex mechanism of exon shuffling through retrotransposition of an antisense MCH messenger RNA coupled to de novo creation of splice sites"]. Retroposition into an intron of CDH12 30-35 Mya [PMID:19068116 "the initial retroposition event took place within an intron of the brain cadherin (CDH12) gene"].
- Truncation: [PMID:11070051 "They correspond to a 5'-end truncated version of the MCH gene"]; [PMID:8326825 "no sequence identity was found in the N-terminal and 5' end non-coding regions"]. The 1993 paper nevertheless called it a variant gene "rather than a pseudogene" because RNAs were detected.
- Brain transcripts are antisense: [PMID:9729295 "Thus, there is no evidence that the MCH peptide-precursor molecule is produced in the brain by the human-variant pMCHL loci."]
- Viale 2000 (PMID:11070051, abstract only): sense unspliced PMCHL1 RNAs carry a novel ORF that "may produce an NLS-containing protein of 8 kDa named VMCH-p8"; translated in vitro and in transfected COS cells only.
- Schmieder 2008 (PMID:19068116, full text): ORF1 = VMCH-p8, NLS KPKKK at N-terminus, 72 aa per the paper (UniProt Q16048 is 86 aa; the N-terminus MLSQKPKKKH matches the NLS, so Q16048 is the VMCH-p8 ORF or a close variant; length difference unresolved). Antiserum against the N-terminal 13 aa detected no protein in human testis, fetal/newborn brain, or macaque brain, nor in HEK293 cells transfected with ORF1-bearing PMCHL1/2 sequences ["This strongly suggests that these putative proteins are not translated in vivo in the human and macaque tissues that we tested."]. Authors propose mRNA-like ncRNA function. Caveat they state: possible expression below detection threshold.
- No proteomics/ribo-seq evidence found in UniProt cross-references (MassIVE listed only as a DR line; no PeptideAtlas/PRIDE). Not further pursued.

### Sequence vs parent PMCH (bioinformatics, PMCHL1-bioinformatics/RESULTS.md)
- Q16048 2-86 aligns to PMCH 81-165 (81% identity). PMCH 1-80 (signal peptide 1-21 + N-terminal pro-region) absent.
- No signal peptide: N-terminus is the charged putative NLS. So no secretory-pathway entry, no prohormone-convertase processing, no secreted MCH/NEI.
- MCH-like region: 4 substitutions (M150T, R152S, R160Q, P161S, PMCH numbering); disulfide Cys retained. NEI-like region: I132T and C-terminal amidated I143V.

### Propagation routes
- IBA GO:0031777 and GO:0032227: PANTHER PTN002636265 (IBD in IBD.gaf, taxon:117571 Euteleostomi; seed RGD:3358 rat Pmch). PMCHL1 sits in PTHR12091:SF1 (PRO-MCH-LIKE PROTEIN 1-RELATED), a primate-only subfamily derived from PMCH; descends from the node by retroposition, but the copy lacks the secretory signal and is likely non-coding. Recommendation: block SF1 at the PAINT node (NOT annotation / exclude pseudogene subfamily).
- IEA GO:0030354 and GO:0007268: InterPro2GO IPR005456 (Prepro-melanin_conc_hormone) match. GO:0007165 and GO:0045202: GOC inter-ontology inference from those.
- NAS GO:0005576 extracellular region: UniProt from PMID:8326825 (1993 assumption of a secreted prohormone).

### Decision
All 7 rows REMOVE. No core function. 
