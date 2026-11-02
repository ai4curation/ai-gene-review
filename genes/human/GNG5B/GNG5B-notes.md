# GNG5B notes (A0A804HLA8, G protein subunit gamma 5B)

## 2026-10-04: Tier 3 audit (MICROPROTEINS project)

### Locus status
- HGNC:24826 (REST, 2026-10-04): locus_type **gene with protein product**, Xq23. Its previous
  symbol is GNG5P2, so the locus was reclassified from pseudogene to protein-coding. MANE
  Select is ENST00000697560.1 / NM_001396022.1. There is also CCDS94650.1.
- Ensembl ENSG00000133136: protein_coding, with a single-exon MANE transcript (a retrocopy
  of GNG5) and a 3-exon transcript. Both encode the same 68 aa.
- UniProt: PE 3 (Inferred from homology). The entry was created in 2021 (Swiss-Prot 2022).
  Function, subunit and location are all by similarity (ECO:0000250/ECO:0000305) to GNG2
  (P63212, bovine) and GNG12 (Q9UBI6), and none come from this locus.
- Expression: GTEx v8 (which still uses GENCODE v26 and calls it processed pseudogene
  GNG5P2) gives a max median of 0.29 TPM (pituitary/brain), against about 275 TPM for GNG5.
  Bgee (via UniProt DR line) reports expression in testis male germ line stem cells and 66
  other cell types or tissues. The locus is transcribed at a low level, and quantification
  is confounded by 94% identity to GNG5.
- No peptide-level evidence was found (UniProt cites none; my automated PeptideAtlas query
  failed).
- PubMed: 0 hits for GNG5B or GNG5P2 (2026-10-04).

### GOA "experimental" row
- None of the 8 GOA rows (QuickGO live check, 2026-10-04) is experimental. The only row that
  is not IBA or IEA is **plasma membrane, ISS (ECO:0000250), GO_REF:0000024, assigned by
  UniProt, with/from UniProtKB:P63212**. P63212 is *bovine GNG2*, not GNG5. It is therefore a
  similarity transfer made through the Ggamma family by UniProt curation (the
  SUBCELLULAR LOCATION line "{ECO:0000250|UniProtKB:P63212}"). It is not locus-specific and
  does not even come from the parent GNG5. A census that counts ECO:0000250 as experimental
  would misclassify it.

### Residue comparison (GNG5B-bioinformatics/RESULTS.md)
- 64/68 identical to GNG5. Substitutions: S4F, M10T, R18Q, R25S.
- CaaX CSFL is retained. C65 (geranylgeranyl and methyl ester) and the SFL propeptide are
  identical.
- Gbeta interface mapped from 1GP2 (gamma2/beta1): 33 of 36 contact positions are identical.
  M10T, R18Q and R25S lie in the N-terminal coiled-coil helix. R18 aligns to gamma2 K20,
  which is already variable in the family.
- Conclusion: no residue-level loss. If the protein is made it is expected to be a
  functional Ggamma, but that remains untested.

### Propagation routes
- IBA G protein activity and IBA GPCR signalling come from PTN008551661 (donors include
  bovine GNG2 P63212, Drosophila Ggamma1 FBgn0004921, mouse MGI:102705, rat RGD:620805).
- IBA heterotrimeric G-protein complex comes from PTN001013516 (donors GNG2, GNGT1, GNGT2,
  rat).
- The IEA rows come from InterPro2GO on IPR001770/IPR015898/IPR036284 and from the UniProt
  SubCell mapping SL-0039.
- The ISS row is UniProt curation by similarity to bovine GNG2.

### Action logic
- Following the Tier 3 rule, the product may exist (protein-coding, MANE, intact ORF,
  transcribed at a low level), but every function claim is inherited and untested. All rows
  are therefore MARK_AS_OVER_ANNOTATED, not REMOVE. The PAINT node placement looks correct,
  because GNG5B sits inside the Ggamma5 clade with an intact interface. The weak point is
  evidence that the product exists, not the phylogeny. If peptides unique to GNG5B are
  detected, the CC/MF rows could be upgraded to ACCEPT.
- No core_functions are asserted.
