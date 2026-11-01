# P (pericarp color1, P1) in maize: manual literature synthesis

No deep-research provider was available for this session; this summary was
written by the reviewer from cached publications (`publications/PMID_*.md`)
and PubMed searches. UniProt entry reviewed: C6G8B2 (TrEMBL, B73,
Zm00001eb014290, GeneID 542272). The Swiss-Prot entry P27898 (Myb-related
protein P) is the same gene; its first 250 residues are identical except one
(see `P-bioinformatics/RESULTS.md`).

## Identity and structure

- P1 encodes an R2R3-MYB transcription factor [PMID:22702356 "The P1 gene
  encodes an R2R3-MYB transcription factor that regulates the accumulation of
  a specific group of flavonoids in maize floral tissues, the flavones and the
  phlobaphenes"].
- The p locus is a compound locus of duplicated MYB genes p1 and p2
  [PMID:23113982 "The p locus is a complex of duplicated MYB-homologous genes
  p1 and p2 on chromosome 1"]; the duplication produced genes with different
  tissue specificity [PMID:11148280 "p1 transcripts accumulate in kernel
  pericarp, cob, tassel glumes, and silk, whereas p2 transcripts are found in
  developing anther and silk"].
- C6G8B2 has two Myb repeats (residues 9-61, 62-116), a disordered middle
  region and a C-terminal P_C domain (Pfam PF06640) (UniProt record).

## DNA binding and transcriptional activation

- P binds a CCT/AACC motif and directly activates A1 (DFR) but not Bz1
  [PMID:8313474 "P encodes a Myb homolog that recognizes the sequence CCT/AACC"]
  [PMID:8313474 "P binds to and activates transcription of the A1 gene required
  for 3-deoxy flavonoid and phlobaphene biosynthesis, but not the Bz1 gene
  required for anthocyanin biosynthesis"]. Abstract only in cache.
- P binds the same a1 promoter sites as C1 and activates without the bHLH
  co-activators B/R [PMID:9144964 "The two C1 binding sites in the a1 promoter
  are also bound by P"]; [PMID:15347654 "In contrast, the R2R3 MYB protein P1
  activates a subset of the C1-regulated genes independently of R"].
- Zmf3'h1 (pr1) is a direct P1 target, by EMSA with recombinant P1 MYB domain
  and ChIP in pericarps [PMID:23113982 "Using a combination of EMSA and ChIP
  experiments, we established that the Zmf3'h1 gene is a direct target of
  P1"]; its mRNA accumulation requires functional p1 [PMID:23113982 "Zmf3'h1
  mRNA accumulation requires a functional p1 allele"].
- ChIP-seq plus RNA-seq: ~1500 putative direct targets including F2H1, and
  binding can lead to activation or repression [PMID:22822204 "Unexpectedly,
  the binding of P1 to gene regulatory regions can result in both gene
  activation and repression"]. P1 is "the major regulator for a set of genes
  involved in flavonoid biosynthesis" [PMID:22822204].

## Biological role

- P1 controls phlobaphene pigments in pericarp and cob glumes and C-glycosyl
  flavones (maysin) and 3-deoxyanthocyanidins in silks [PMID:23113982,
  PMID:22822204]. The enzymes (CHS/C2, CHI1, DFR/A1, F3'H1/Pr1, F2H1) perform
  the biosynthetic steps; P1 regulates their transcription.
- UV-B: in leaves of high-altitude landraces P1 is UV-B induced and binds the
  CHS (C2) promoter more after UV-B, but B73 and W23 show almost no expression
  [PMID:22702356 "P1 is induced by UV-B, both at the transcript and at the
  protein levels, in contrast to B73 or W23, which showed almost undetectable
  expression levels, and very low induction by UV-B"].
- Expression of p1 is controlled epigenetically (paramutation, DNA and H3K9
  methylation of a distal enhancer, modifier Ufo1) [PMID:23055943,
  PMID:12663550]; this concerns regulation of the gene, not the protein's
  activity.

## Gaps

- No direct localization experiment for P1 protein was found; nuclear location
  rests on TF function and ChIP from nuclei.
- The mechanism by which P1 represses some direct targets is unknown.
- The C-terminal sequence differs between C6G8B2 and P27898; which is correct
  is unresolved.
