# MYB28 (At5g61420; HAG1/PMG1) - manual literature synthesis

No deep-research API was available for this review; this summary was compiled by hand from the
cached publications in `publications/` and the UniProt record Q9SPG2. All quotes are verbatim
from the cited source.

## Identity
- UniProt Q9SPG2 (MYB28_ARATH), TAIR AT5G61420, GeneID 836263; 366 aa R2R3-MYB transcription
  factor (two Myb_DNA-binding Pfam domains, PF00249; InterPro IPR015495 Myb_TF_plants).
  Synonyms HAG1 (HIGH ALIPHATIC GLUCOSINOLATE 1) and PMG1 (PRODUCTION OF METHIONINE-DERIVED
  GLUCOSINOLATE 1). Subgroup 12 R2R3-MYB with MYB29/HAG3, MYB76/HAG2 (aliphatic) and
  MYB34/MYB51/MYB122 (indolic).

## Function: master positive regulator of aliphatic glucosinolate biosynthesis
- Identified in a transactivation screen: "In a screen for the trans-activation potential of
  various transcription factors toward glucosinolate biosynthetic genes, we could identify the
  HAG1 (HIGH ALIPHATIC GLUCOSINOLATE 1, also referred to as MYB28) gene as a positive regulator of
  aliphatic methionine-derived glucosinolates" [PMID:17521412].
- Co-expression / omics, knockout and overexpression: "PMG1/Myb28 is apparently a master
  transcription factor, generally regulating the pathway from Met to aliphatic GSLs, and is
  necessary and sufficient for the biosynthesis of aliphatic GSLs at a basal level in
  Arabidopsis" [PMID:17420480]. In myb28 "the expression of most of the genes involved in
  aliphatic GSL biosynthesis was repressed" [PMID:17420480]; overexpression in suspension cells
  activated every aliphatic GSL structural gene and produced GSLs in dedifferentiated cells
  [PMID:17420480].
- Redundancy with MYB29: "in the absence of both, the synthesis of all aliphatic glucosinolates
  is blocked" [PMID:18446225]; myb28 blocks long-chain aliphatic GSLs [PMID:18446225].
- Reciprocal transactivation among HAG1/MYB28, HAG2/MYB76, HAG3/MYB29 and repression of indolic
  GSL regulators [PMID:18042203]. Complementation of myb28myb29 with pMYB28:MYB28 "activated AGSL
  biosynthetic genes and restored accumulation of AGSLs with short side chains" [PMID:23792303].
- Network view: MYB28/MYB29/MYB76 interplay determines aliphatic GSL profile; chemotype partly
  uncoupled from biosynthetic transcript levels [PMID:20348214].
- Direct promoter binding: in a large Y1H screen MYB28 "has been validated to interact with
  these promoters" of aliphatic GSL genes [PMID:25352272]; additional Y1H network screens
  (secondary cell wall, nitrogen metabolism) also recorded MYB28 promoter interactions
  [PMID:25533953, PMID:30356219] (supplementary data, not inspected here).
- Partners: MYC2/MYC3/MYC4 bHLH factors "interact directly with GS-related MYBs" (Y2H and
  pull-down) [PMID:23943862]; UniProt: "Can form complexes with MYC2, MYC3 or MYC4."
- Brassinosteroid repression of GSLs requires MYB28 [PMID:23580754].

## Location and expression
- Nucleus (UniProt; ECO:0000269 PubMed:17521412; PROSITE-ProRule PRU00625).
- Expressed in generative organs, mature leaves and trichomes; induced by touch/wounding in
  inflorescences, by glucose [PMID:17521412, PMID:23115560].
- Sulfur: Hirai et al. report MYB28 down-regulated under sulfur deficiency [PMID:17420480],
  whereas Li et al. report MYB28 "expression was induced by sulfur deficiency" [PMID:23792303]
  - conflicting reports on direction.
- Herbivory/biotic: aphid feeding down-regulated MYB28/29/76 transcripts [PMID:23144921];
  lepidopteran oral secretions suppress basal MYB28 expression [PMID:40546745].

## Physiological consequences (indirect, via glucosinolates)
- Overexpression reduced weight gain of Spodoptera exigua [PMID:17521412]; myb28myb29 increases
  Mamestra brassicae larval weight gain [PMID:18446225].
- myb28 hypersusceptible to Sclerotinia sclerotiorum [PMID:21418358].
- myb28myb29 lost Pseudomonas fluorescens SS101-induced resistance to Pst [PMID:23073694].
