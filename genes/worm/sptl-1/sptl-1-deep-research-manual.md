# sptl-1 (C. elegans, P91079) - manual literature research

No deep-research API was available; this summary was compiled by hand from cached publications,
PubMed searches ("sptl-1 elegans sphingolipid") and the UniProt record.

## Identity and family
- sptl-1 = C23H3.4 (formerly spt-1), Swiss-Prot SPTC1_CAEEL, 458 aa, PE 3 (inferred from homology).
  [PMID:15340492 "The spt-1 (C23H3.4) gene encodes a predicted C. elegans homolog of serine-palmitoyl transferase subunit 1."]
- Class-II PLP-dependent aminotransferase fold (Pfam PF00155; PANTHER PTHR13693:SF2 SERINE PALMITOYLTRANSFERASE 1).
- Pairwise alignment (sptl-1-bioinformatics/RESULTS.md): 50.3% identity to human SPTLC1, 30.1% to SPTLC2;
  Asn297 sits at the SPTLC2 K379 PLP Schiff-base lysine position, so SPTL-1 is the non-catalytic LCB1-type subunit.
- UniProt (by similarity): "The catalytic core is composed of a heterodimer of sptl-1 and sptl-2 or sptl-1 and sptl-3".

## Biochemical role in the worm
- SPTL-1 is "predicted to condense a fatty acid with serine to form the long-chain-base (LCB) sphinganine as
  the first committed step in de novo sphingolipid synthesis" [PMID:21926990].
- C. elegans sphingoid bases are C17 iso-branched; sptl-1 is "required for d17iso-SPA biosynthesis" and
  d17iso-SPA suppresses sptl-1(RNAi) L1 arrest [PMID:23705068 "supplementation with d17iso-SPA, but not mmBCFAs, also suppressed the L1 arrest phenotype caused by feeding RNAi of sptl-1"].
- LC-MS/MS: "RNAi targeting the first key enzyme (SPT) in the de novo sphingolipid biosynthesis pathway caused a
  decrease of nearly all sphingolipids in Caenorhabditis elegans." [PMID:38704027]
- sptl-1 loss "alleviates sphingosine accumulation" in sphk-1 mutants [PMID:41191545, abstract].

## Phenotypes
- Intestinal apicobasal polarity conversion with ectopic lateral lumens at L1 arrest; phenocopied by
  sptl-2;sptl-3 double RNAi, myriocin and fumonisin B; partially rescued by glycosphingolipids; ER and Golgi
  distended [PMID:21926990 "sptl-1(RNAi) intestinal sections revealed vesicle paucity, along with distended endoplasmic reticular (ER) and Golgi membranes"].
- "sptl-1(−) disrupts all sphingolipid biosynthesis and its phenotype is ... highly pleiotropic" [PMID:23705068].
- HSAN1 model: SPTL-1(C121W) (= SPTLC1 C133W) homozygotes show "the same larval lethality and epithelial polarity
  defect as observed in sptl-1(RNAi) animals"; heterozygotes show neuronal polarity defects; dominant-negative on
  overexpression, lowering glucosylceramide [PMID:31138658, abstract].

## Localization
- No direct C. elegans data. Orthologs are ER membrane proteins; [PMID:38704027 "SPTL-1 is the C. elegans ortholog of
  the catalytic subunit of human serine palmitoyltransferase, which is located on the ER (26, 32)."] (note: the
  "catalytic subunit" wording is imprecise; SPTL-1 is the SPTLC1-type subunit).
