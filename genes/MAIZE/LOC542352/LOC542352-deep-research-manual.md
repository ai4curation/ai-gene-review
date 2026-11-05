# LOC542352 (Zea mays) - manual literature research

Deep-research API providers were not available in this session; this file records the
literature search done by hand (PubMed searches, NCBI Gene links, cached publications).

## Identity

- UniProtKB A0A804Q7E0 (TrEMBL, unreviewed), 163 aa, gene model Zm00001eb299370 (B73 v5,
  chromosome 7), RefSeq NP_001105399.2 / NM_001111929.2, NCBI GeneID 542352.
- NCBI Gene names it "pathogenesis related protein 4" with aliases PR-1, prp4, PR1,
  "pathogenesis-related protein class I"; v4 id Zm00001d018738, v3 id GRMZM2G465226
  (NCBI Gene esummary, retrieved 2026-10-28).
- Domain content: a single CAP/SCP domain (Pfam PF00188, SMART SM00198, residues 25-159),
  CDD cd05381 CAP_PR-1, PROSITE CRISP_1 and CRISP_2 signatures, PANTHER PTHR10334
  (CYSTEINE-RICH SECRETORY PROTEIN-RELATED); SignalP predicts a signal peptide at 1-23
  [file:MAIZE/LOC542352/LOC542352-uniprot.txt].
- The sequence is strongly acidic (very few Lys/Arg residues), so this is an acidic PR-1,
  distinct from the basic maize PRms protein of Casacuberta et al. 1991 [PMID:1714315
  "a basic form of a protein from germinating maize seeds having a high homology with the
  group of PR-1 from tobacco"].
- The C-terminus ends ...CSYNPPGNVVGESPY, matching the conserved "CNYxPxGNxxGxxPY" end of
  plant PR-1 proteins from which the CAPE immune-signalling peptides are released in tomato
  and Arabidopsis (sequence observation; no maize CAPE has been tested).

## What PR-1 proteins do (family level)

- PR-1 proteins bind sterols and inhibit sterol-auxotrophic oomycetes by sterol sequestration
  [PMID:27747953 "we provide genetic and biochemical evidence for the capacity of PR-1 proteins
  to bind sterols, and demonstrate that the inhibitory effect on pathogen growth is caused by
  the sequestration of sterol from pathogens"] (tomato/tobacco proteins; abstract only).
- Review: [PMID:28743380 "Recent reports have emerged demonstrating that PR-1 proteins possess
  sterol-binding activity, harbour an embedded defence signalling peptide, and are targeted by
  plant pathogens during host infection."]

## Maize PR-1 literature

- Morris et al. 1998: chemical inducers of SAR (BTH etc.) and pathogen infection induce maize
  PR-1 and PR-5 [PMID:9650297 "These genes are also coordinately activated by pathogen
  infection and function as indicators of the defense reaction."]. Abstract only; NCBI Gene
  links this paper to GeneID 542352, but from the abstract alone I cannot confirm which maize
  PR-1 paralog was cloned.
- Saleem et al. 2025 expressed a maize PR-1 in E. coli and reported antifungal activity
  against Fusarium oxysporum, but the clone was NM_001159109.2, a different maize PR-1 gene
  [PMID:40866506 "The gene sequence of PR-1 from Z. mays was downloaded from NCBI (Gen Bank ID:
  NM_001159109.2)."]. Not evidence for LOC542352 specifically.
- Soderlund et al. 2009 full-length cDNA collection [PMID:19936069] provides transcript
  evidence only.

## Symbol-collision papers (NOT about this gene)

- PMID:23113982 (Sharma et al. 2012) and PMID:21385724 (Sharma et al. 2011) are about the
  maize red aleurone1 locus, symbol pr1, which encodes the flavonoid 3'-hydroxylase ZmF3'H1
  [PMID:23113982 "The maize (Zea mays) red aleurone1 (pr1) encodes a CYP450-dependent
  flavonoid 3'-hydroxylase (ZmF3'H1)"]. The full text of PMID:23113982 was read; it contains no
  mention of pathogenesis-related proteins, CAP domains or LOC542352. NCBI Gene nevertheless
  links PMID:21385724 (with a GeneRIF) to GeneID 542352, evidently because of the "PR1"
  alias of this PR-1 gene colliding with the pr1 (F3'H) locus symbol.
