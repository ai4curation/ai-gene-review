# C0HM83 (SHMOOSE) review notes

## Identity

- UniProt C0HM83 (SHMOS_HUMAN), "Protein SHMOOSE" / "Small human mitochondrial ORF over
  serine tRNA", 58 aa, PE1, encoded on mtDNA (OG Mitochondrion). UniProt gives no gene symbol,
  so the folder and `gene_symbol` use the accession (alt-ORF convention, projects/MICROPROTEINS.md).
- Essentially one primary paper: Miller et al. 2023 Mol Psychiatry [PMID:36127429], plus an
  erratum [PMID:36658336, abstract only, content of correction not available]. Later PubMed hits
  (search "SHMOOSE", 2026-10-03: 8 records) are reviews or plasma-level association studies,
  e.g. [PMID:41883858] (Mediterranean diet vs plasma SHMOOSE/humanin, same USC group). No
  independent replication of the mechanistic findings found.

## ORF location and genetic code (bioinformatics, C0HM83-bioinformatics/RESULTS.md)

- The UniProt sequence maps once on rCRS, + (heavy-strand-encoded) sense, m.12234-12410 (incl. TAA
  stop); overlaps MT-TS2 (tRNA-Ser(AGY)), MT-TL2 (tRNA-Leu(CUN)) and the 5' end of MT-ND5 in a
  different frame. Same coordinates are given in [PMID:41883858 "SHMOOSE is encoded by a small open
  reading frame (smORF) overlapping the serine tRNA region, between nucleotides 12,234 and 12,410"].
- No TGA/ATA/AGA/AGG codons, so standard and vertebrate mitochondrial codes give the identical
  58-aa product. Paper agrees: [PMID:36127429 "SHMOOSE does not contain such mitochondrial-specific
  codon usage and is translated into identical sequences regardless of codon specificity"]. So the
  code cannot tell whether it is made by mitoribosomes or cytosolic ribosomes (unlike MOTS-c),
  and the authors leave this open [PMID:36127429 "A research area worth substantial consideration is
  whether SHMOOSE localizes to mitochondria following translation in cytoplasmic ribosomes or whether
  SHMOOSE is translated within the mitochondrial matrix by mitochondrial ribosomes"].
- My own inference (not tested): the start codon lies inside tRNA-Ser(AGY). Standard tRNA
  punctuation processing of the H-strand polycistron would separate the start from the rest of the
  ORF, so translation would need an unprocessed or alternatively processed RNA. Flag as a question.
- m.12372G>A (rs2853499) changes codon 47 GAC->AAC (D47N); synonymous for ND5 per the paper
  [PMID:36127429 "These three haplogroup SNPs at base pair positions 11467, 12308, and 12372 do not
  change the amino acid sequences of the mt-ND4 and mt-ND5 proteins"].

## Existence

- Endogenous peptide: WB ~6 kDa in mito and nuclear fractions of SH-SY5Y; absent in rho0 cells; two
  peptides by MS after IP from mitochondria [PMID:36127429 "SHMOOSE was detected in neuronal
  mitochondria and nuclei fractions at the predicted ~6kDa molecular weight"; "in rho zero cells
  (i.e., cells without mtDNA), SHMOOSE was not detected"]. Detected in CSF by ELISA.

## Variant association (not function)

- D47N associated with AD in ADNI with modest effect [PMID:36127429 "SHMOOSE.D47N carriers presented
  an odds ratio of 1.56 (case frequency: 22.9%; control frequency: 15.7%; 95% CI: 1.06–2.30;
  permutation empirical p value < 0.03)"]. rs2853499 is a haplogroup U marker; authors concede
  [PMID:36127429 "we cannot rule out other SNPs within the SHMOOSE.D47N haplogroup (i.e., Haplogroup
  U) have independent effects"]. The same base also lies in the overlapping ND5 sequence (synonymous)
  and in the H-strand transcript, so association alone cannot attribute risk to the peptide. Genetic
  association is not a GO function.

## Functional experiments (all with exogenous synthetic peptide)

- Mitofilin (IMMT, Q16891) binding: spiked synthetic peptide into lysate -> IP-MS (98 proteins, IMMT a
  top hit), reciprocal co-IP after treating cells with 1 uM peptide, and dot blot with recombinant
  proteins [PMID:36127429 "The SHMOOSE-mitofilin interaction was confirmed in vitro by treating cells
  with SHMOOSE followed by gentle lysis, reciprocal immunoprecipitation, and western blot at least three
  times"]. siRNA IMMT abolished peptide effect on superoxide. D47N still binds.
- Exogenous peptide raised basal OCR ~20% and MTT signal; protected SH-SY5Y against oligomeric Abeta42;
  ICV in rats changed hypothalamic transcriptome. These are pharmacological responses to added peptide,
  not loss-of-function of the endogenous product; no knockout/knockdown of endogenous SHMOOSE exists
  (mtDNA editing would be needed).

## GO decisions

- GO:0005515 protein binding IPI (IMMT) -> REMOVE per project policy (no informative MF; there is no
  "MICOS complex binding" GO term in QuickGO search). Interaction is reported in description.
- mitochondrion IDA + IEA -> ACCEPT.
- nucleus IDA + IEA -> KEEP_AS_NON_CORE (fractionation-only, one study, no function there).
- No NEW: OCR/neuroprotection data are exogenous-peptide pharmacology; participation test not met.
