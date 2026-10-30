# SMIM45 notes

## 2026-10-08 — initial review (MICROPROTEINS Tier 2)

UniProt A0A590UK83 (SMI45_HUMAN), PE2, 68 aa, one predicted TM helix (7-27). Former
symbol LINC00634. HGNC protein-coding.

### Key finding: the GOA experimental rows describe a different ORF

- SMIM45 mRNA is **bicistronic**. "SMIM45 is also a bicistronic gene, encoding both an
  ancient 68 aa microprotein and a human-specific, de novo 107 aa protein [7]."
  [PMID:42194976]. The 68-aa ORF is ultra-conserved: "The 68 aa sequence has been traced
  as far back as the elephant shark" [PMID:38612733]. The 107-aa ORF arose de novo in
  primates.
- UniProt history (UniSave): entry versions 1-11 (2019_10 to 2023_01) carried sequence
  version 1 = **107 aa** (MSMAACPEAP...; same UniParc UPI0000197840 as the deleted 2014
  entry Q6ICG7/YV028_HUMAN). From entry version 12 (2023_03) the sequence was replaced by
  the **68-aa** ORF (UPI00002078AF, shared with dog, rat, etc. orthologues). The FUNCTION,
  SUBCELLULAR LOCATION and GO rows from PMID:36593289 (GOA date 20230214, i.e. made on the
  107-aa sequence) were carried over unchanged to the 68-aa product.
- PMID:36593289 (An et al. 2023) studied the 107-aa ORF: the gene "encodes a putative
  protein of 107 amino acids located in both cytoplasm and nucleus". The KO genotyping
  primer (KO-GT-F: ATGTCTATGGCTGCCTGTCCTG) starts at the ATG of the 107-aa ORF, and the
  ORF-RT-F primer also lies inside it (SMIM45-bioinformatics/RESULTS.md). Over-expression
  used "The ORF sequence of ENSG00000205704 and the human codon-optimized HA" tag.
  Conclusion: localization (nucleus, cytoplasm) and neuron-maturation phenotype belong to
  the 107-aa product, not to the 68-aa protein the accession now represents.
- Corroboration: An et al. 2025 [PMID:41219895] call it "SMIM45-107aa" and cite the
  nuclear/cytoplasmic localization of the 107-aa peptide from PMID:36593289. Delihas 2024
  [PMID:38612733]: "In somatic brain tissues, only the 68 aa ORF is translated and not the
  107 aa ORF [3]; thus, there is no translational readthrough."
- Note also the paper's direction of effect: KO accelerates maturation, OE delays it, i.e.
  a negative regulator — so even for the 107-aa product `neuron maturation` is at best
  coarse.

### 68-aa SMIM45 protein itself
- No functional study. Ribo-seq evidence for translation (Delihas citing NCBI/Ensembl).
  Predicted single-pass membrane protein (hydrophobic segment VYLVISVLILVGFGACIYYF).
- Other LINC00634 literature (colon cancer prognosis PMID:40713515; retracted glioma
  signature PMID:36248415) is RNA-level/correlative and not used.

### The 107-aa product
- Has no UniProtKB accession (Q6ICG7 deleted 2014). Under the repo's alternative-ORF
  convention it would need its own folder once UniProt gives it an accession. Its reported
  functions: nucleus/cytoplasm, delays neuronal maturation in organoids/mice
  [PMID:36593289]; binds and stabilises MTDH in HCC cells [PMID:41219895].

### Actions
- IDA nucleus, IDA cytoplasm, IMP neuron maturation: REMOVE (sequence-replacement error;
  evidence is about the 107-aa ORF). Not a disagreement with the curator's reading of the
  paper, which was correct for the sequence at the time.
- IEA nucleus/cytoplasm (SubCell): REMOVE, same root cause.
- IEA membrane: ACCEPT (TM prediction on the current 68-aa sequence).
