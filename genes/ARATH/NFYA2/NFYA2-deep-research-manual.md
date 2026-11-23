# NFYA2 (At3g05690; UniProt Q9M9X4) - manual literature synthesis

No deep-research provider was available for this session. This file is a manual
synthesis from cached publications (`publications/PMID_*.md`) and PubMed searches
(query: `(NF-YA2 OR NFYA2 OR HAP2B) AND Arabidopsis`, 18 hits, Oct 2026).

## Identity and family

- NF-YA2 = AtHAP2b, one of 10 Arabidopsis NF-YA subunits of the heterotrimeric
  CCAAT-binding NF-Y (HAP) complex. Isolated by functional complementation of a
  yeast hap2 mutant [PMID:9662544 "Consequently, the clones P1, P3, and P5 were termed AtHAP2a, AtHAP2b,"];
  AtHAP2b "encodes a protein of 295 amino acids" [PMID:9662544], matching Q9M9X4 (295 aa, EMBL Y13721).
- Complementation was specific for hap2: "the three clones were unable to rescue any of
  the other yeast mutants, indicating that they were not general transcriptional
  activators" [PMID:9662544]. AtHAP2b rescued less well, correlating with a 4-aa longer
  spacer between subunit-association and DNA-binding domains [PMID:9662544].
- UniProt: subunit-association domain (SAD) 139-165, NFYA/HAP2-type DNA-binding region
  173-198 (PROSITE PRU00966); Pfam PF02045 CBFB_NFYA; PANTHER PTHR12632.

## Biochemistry

- NF-YA2 alone does not bind CCAAT; it binds the FT CCAAT element only with an NF-YB/NF-YC
  histone-fold dimer: "However, neither NF-YA2 nor NF-YA6 could individually bind the CCAAT
  probe." and "In the presence of NF-YB2/NF-YC3 dimers, NF-YA2 and NF-YA6 bound the CCAAT
  probe in a concentration-specific manner" [PMID:27977687].
- Yeast three-hybrid: NF-YA2 enters trimers with NF-YB2/NF-YC9 [PMID:27977687]; with
  NF-YB3/DPB3-1 (NF-YC10) [PMID:25490919].
- An NF-YA2/B2/C9 complex binds an NFYBE element in the SOC1 promoter (Hou et al. 2014,
  PMID:25105952, abstract only; summarised in review PMID:28119722).

## Biological roles (all transcription-regulatory, via NF-Y complexes)

1. Heat stress: NF-YA2/NF-YB3/DPB3-1 trimer co-activates DREB2A on the HsfA3 promoter in
   protoplasts in a CCAAT-dependent manner [PMID:25490919 "The transactivation assay revealed
   that a CCAAT box was necessary for HsfA3 promoter activation in protoplasts by the trimer
   of NF-YA2, NF-YB3, and DPB3-1 in protoplasts"]. Constitutive NF-YA2 OE gives heat/freezing
   tolerance [PMID:23118940 "Long-term expression of NF-YA2 confers tolerance to freezing and
   heat."], but Rao et al. 2022 report NF-YA2 OE / miR169-resistant lines are heat-sensitive
   and nf-ya2 mutants more tolerant [PMID:36050841, abstract]. Direction is context dependent.
2. Flowering time: p35S:NF-YA2 flowers early and acts through FT [PMID:27977687 "These results
   suggest that NF-YA2, like its NF-YB and NF-YC counterparts, regulates flowering by
   controlling FT expression."]; Hou et al. find NF-YA2 regulates SOC1 [PMID:25105952]; Xu et
   al. report the opposite (late flowering with miR169-resistant NF-YA2 OE, via FLC)
   [PMID:24336445, abstract].
3. Leaf growth / auxin: NF-YA2 and NF-YA10 OE increase leaf size; ChIP shows binding to CCAAT
   in YUC2 promoter and repression of YUC2 [PMID:28469131]; NF-YA2 binds ARGOS promoter as a
   repressor [PMID:41121987, abstract]; binds FT and YUC2 promoters, ambient temperature
   regulated via miR169 [PMID:29856891, abstract].
4. Root architecture: miR169defg/NF-YA2 node controls primary root growth [PMID:24533947, abstract].
5. Nutrient stress: NF-YA2 induced by low Pi, low N, high sucrose; tightly regulated
   post-transcriptionally by miR169 [PMID:23118940]. NF-YA2-SRDX repressor shows many
   CCAAT-containing targets [PMID:23118940].
6. Reproduction: Ds insertion identified in a female gametophyte screen (Pagnussat 2005,
   PMID:15634699, abstract only); Siriwardana et al. note "mutants of a few members are lethal
   (including NF-YA2)" [PMID:27977687].

## Expression

Ubiquitous (PMID:9662544, PMID:11250072 via UniProt); strong vascular, SAM, young leaves
[PMID:28469131 "NF-YA2 was expressed mainly in SAM, node and young leaves"].
Major post-transcriptional control by miR169 [PMID:23118940, PMID:24533947].
