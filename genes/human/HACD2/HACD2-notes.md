# HACD2 (Q6Y1H2) review notes

## Identity and family

- HGNC:9640; UniProt Q6Y1H2; gene HACD2, synonym PTPLB (protein-tyrosine
  phosphatase-like member B). RefSeq NP_940684.1 / NM_198402.5. 254 aa,
  ER multi-pass membrane protein with 5 predicted TM helices.
  [file:human/HACD2/HACD2-uniprot.txt "RecName: Full=Very-long-chain (3R)-3-hydroxyacyl-CoA dehydratase 2"]
- Belongs to the HACD (PTPLA/PTPLB) very-long-chain fatty acid dehydratase family;
  contains a Pfam PF04387 (PTPLA) domain / InterPro IPR007482 "Tyr_Pase-like_PTPLA".
  Despite the "protein tyrosine phosphatase-like" name, it has no phosphatase activity.
  [file:human/HACD2/HACD2-uniprot.txt "Shares some similarity with tyrosine phosphatase proteins but"]
- One of four mammalian HACD paralogs (HACD1-4). HACD1 (PTPLA) is muscle-enriched;
  HACD2 (PTPLB) is the ubiquitously/broadly expressed dehydratase.
  [file:human/HACD2/HACD2-uniprot.txt "Highly expressed in testis, spleen, prostate, colon"]

## Core molecular function

- EC 4.2.1.134; a lyase. Catalyzes the dehydration of a very-long-chain
  (3R)-3-hydroxyacyl-CoA to a very-long-chain (2E)-enoyl-CoA + H2O
  (RHEA:45812). This is the THIRD step of the microsomal (ER) VLCFA
  four-step elongation cycle (condensation → reduction → dehydration → reduction).
  [file:human/HACD2/HACD2-uniprot.txt "a very-long-chain (3R)-3-hydroxyacyl-CoA = a very-long-chain"]
  [file:human/HACD2/HACD2-uniprot.txt "This enzyme catalyzes the dehydration of the"]
- Active over a broad chain-length range (C16 through C26 substrates listed as
  distinct Rhea catalytic-activity entries). KM = 121.7 uM for 3-hydroxypalmitoyl-CoA.
  [file:human/HACD2/HACD2-uniprot.txt "KM=121.7 uM for 3-hydroxypalmitoyl-CoA (at 37 degrees Celsius)"]
- Experimentally established in [PMID:18554506], which characterized all four mammalian
  HACD proteins by rescue of a PHS1-shutoff yeast strain and in vitro 3-hydroxypalmitoyl-CoA
  dehydratase assays. [PMID:18554506 "in growth suppression experiments using a PHS1-shut off yeast strain and/or in vitro 3-hydroxypalmitoyl-CoA dehydratase assays"]
  The best-supported GO MF term is GO:0102158 (very-long-chain (3R)-3-hydroxyacyl-CoA
  dehydratase activity), which matches the UniProt catalytic activity / EC exactly;
  GO:0018812 (3-hydroxyacyl-CoA dehydratase activity) is its more general parent.

## Localization

- ER membrane, multi-pass. [PMID:15024066] describes it as "an integral protein of the
  endoplasmic reticulum membrane with four membrane-spanning alpha helices"
  [PMID:15024066 "an integral protein of the endoplasmic reticulum membrane with four"]
  (UniProt topology annotates 5 TM helices). [PMID:18554506] also reports subcellular
  location (FUNCTION/SUBCELLULAR LOCATION in the paper's scope line).
  [file:human/HACD2/HACD2-uniprot.txt "Endoplasmic reticulum membrane"]

## Interactions / complex

- Part of the ER VLCFA elongase complex. UniProt SUBUNIT: "May interact with enzymes of
  the ELO family (including ELOVL1)" and may be part of a larger elongase complex; the
  enzyme-binding IDA (GO:0019899) traces to these ELOVL condensation-enzyme interactions
  reported in [PMID:18554506]. [PMID:18554506 "We also establish that HACD proteins interact with the condensation enzymes ELOVL1-7, with some preferences."]
- Interacts with TECR (the downstream trans-2-enoyl-CoA reductase, step 4) via its third
  lumenal loop; HACD2-TECR forms a stable complex ([PMID:38422897]).
  [PMID:38422897 "we identified a stable complex of human HACD2-TECR based on extensive in vitro characterizations"]
  [file:human/HACD2/HACD2-uniprot.txt "Interacts\nCC       (via the third lumenal loop) with TECR (PubMed:38422897)."]
  (Note: quote above spans two CC lines in UniProt so cannot be used verbatim as
  supporting_text; TECR interaction verified from the abstract of PMID:38422897 instead.)
- Interacts with BCAP31 (BAP31), which acts as an ER chaperone/quality-control factor
  regulating HACD2 turnover; HACD2/PTPLB turns over rapidly via the proteasome.
  [PMID:15024066 "PTPLB turns \nover rapidly through degradation by the proteasome system"]
- The IntAct-sourced GO:0005515 "protein binding" IPI annotations come from
  high-throughput interactome maps (PMID:25416956 HuRI/CCSB Y2H; PMID:32296183 HuRI;
  PMID:30021884 crosslinking-MS histone landscape) plus PMID:15024066 (BCAP31) and
  PMID:38422897 (TECR). The three HT-interactome papers' cached full text does not
  mention HACD2/PTPLB by name (interactions are in supplementary data), consistent with
  large-scale screens. Bare "protein binding" is uninformative and is marked as
  over-annotated rather than removed.

## Not a phosphatase

- GO:0004725 protein tyrosine phosphatase activity is a NOT (negated) annotation
  (IMP, PMID:15024066). Despite the PTPLB "phosphatase-like" name and a MUTAGEN of
  Pro-101 tested for phosphatase activity, HACD2 has no phosphatase activity.
  [file:human/HACD2/HACD2-uniprot.txt "it has probably no phosphatase activity"]
  [file:human/HACD2/HACD2-uniprot.txt "P->R: Does not restore any protein tyrosine"]

## Downstream biology (non-core)

- VLCFAs made by this elongation cycle are precursors of membrane lipids and lipid
  mediators, including sphingolipids/ceramides.
  [file:human/HACD2/HACD2-uniprot.txt "participates in the production of"]
  Sphingolipid biosynthetic process (GO:0030148, IGI with KAR/HSD17B12 P40857) is a
  downstream consequence of supplying VLCFAs, not the direct catalytic function — kept
  as non-core.

## Curation decisions summary

- Core MF: GO:0102158 very-long-chain (3R)-3-hydroxyacyl-CoA dehydratase activity.
- Core BP: fatty acid elongation (GO:0030497) and very long-chain fatty acid biosynthetic
  process (GO:0042761).
- Core CC: endoplasmic reticulum membrane (GO:0005789).
- GO:0080023 "(2E)-enoyl-CoA hydratase activity" (IEA/Rhea) describes the same chemistry
  under a reverse-direction hydratase name; MODIFY to the physiologically-correct
  dehydratase term GO:0102158.
- Bare GO:0005515 protein binding (5 IPI) → MARK_AS_OVER_ANNOTATED (per policy, not removed).
- Sphingolipid biosynthesis, general fatty acid biosynthetic process, long-chain
  fatty-acyl-CoA biosynthetic process, plain ER, and enzyme binding → KEEP_AS_NON_CORE.
</content>
</invoke>
