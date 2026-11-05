# YAB3 (YABBY3, At4g00180; UniProt Q9XFB1) - manual literature synthesis

No deep-research API was available; this synthesis was compiled by hand from cached
publications (publications/PMID_*.md) and PubMed searches ("(YAB3 OR YABBY3) AND
Arabidopsis", 28 hits screened by title/abstract on 2026-10-28).

## Identity and domain architecture

- 240-aa YABBY family protein with an N-terminal C4-type (C2C2) zinc finger (FT ZN_FING
  30..57) and a C-terminal HMG-box-like YABBY domain (InterPro IPR006780, IPR056775,
  IPR056776; Pfam PF04690, PF24868; PANTHER PTHR31675:SF43 "AXIAL REGULATOR YABBY 3")
  [file:ARATH/YAB3/YAB3-uniprot.txt].
- FIL (YAB1) and YAB3 are the most recent gene duplication in the Arabidopsis YABBY
  family [PMID:15299139 "FIL and YAB3 represent the most recent gene duplication event
  within this family"]. They form the "YAB1 group" and act largely redundantly.

## Expression

- Polar (abaxial) expression in all lateral organ primordia from apical and flower
  meristems [PMID:10457020 "Each of these genes is expressed in a polar manner in all
  lateral organ primordia produced from the apical and flower meristems"].
- UniProt: "Expressed in abaxial regions of lateral aerial organ primordia leading to
  cotyledons, leaves, flower meristems, sepals, petals, stamen and carpels, but not in
  roots" (ECO:0000269, PMID:10457020, PMID:12417699).
- YAB3 is a direct repressed target of WUSCHEL in the SAM [PMID:23549482 "WUS directly
  binds to the regulatory regions of differentiation promoting TFs; KANADI1, KANADI2,
  ASYMMETRICLEAVES2 and YABBY3 to repress their expression"], and a direct activated
  target of SPL8 in anthers [PMID:42860685 "SPL8 directly binds the regulatory regions
  of YAB3 and TCP19 and activates their transcription"].

## Molecular function

- Transcriptional activity: in yeast, GAL4-BD:YAB3 did not activate the reporter
  [PMID:23025792 "this property is not shared with the closely related YAB3"], but in
  planta transactivation assays BD:YAB3 activated a UAS::LUC reporter [PMID:23025792
  "These results not only confirm that FIL functions as an activator in plants, but
  extend this function to the closely related YAB3 protein."]. The authors propose YABs
  are bifunctional (activator and repressor) transcription factors [PMID:23025792].
- Repressive output through co-repressors: YABs (FIL, YAB3) physically interact with
  LEUNIG, LEUNIG_HOMOLOG, SEUSS and SEUSS-LIKE proteins [PMID:19837869 "we show that YABs
  physically interact with components of a transcriptional repressor complex that include
  LEUNIG (LUG), LEUNIG_HOMOLOG (LUH), the LUG-associated coregulator SEUSS, and related
  SEUSS-LIKE proteins"]. GOA IPI rows with O48847 (LUG) and Q9FUY2 (LUH) come from this
  paper.
- DNA binding: the GOA IPI row for transcription cis-regulatory region binding comes from
  a yeast one-hybrid TF-promoter network (PMID:31806676) with the PHV (AT1G30490) and REV
  (AT5G60690) promoters; the cached text of that paper does not list individual
  interactions. Non-sequence-specific DNA binding was shown biochemically for FIL
  (PMID:11812777, cited in [PMID:23133401 "it has been previously shown in vitro that FIL
  protein binds DNA nonspecifically"]); UniProt states YAB3 "Binds DNA without sequence
  specificity", citing PMID:10457020 and PMID:12417699, whose abstracts do not mention DNA
  binding (full text not available here; recorded as a question, not a defect).
- Protein partners: NOZZLE/SPOROCYTELESS (SPL/NZZ) binds YAB3 in GST pull-downs
  [PMID:15299139 "NZZ bound FIL (FIL, FIL-myc), YAB3, and INO reproducibly and
  independently of GST"]; SPL8, YAB5, TCP19, TPL by BiFC/FRET-FLIM [PMID:42860685];
  KAN1, BIM1, MYB44 from large-scale Y2H screens (PMID:28650476, PMID:32612234,
  PMID:36088536).

## Subcellular location

- Nuclear: YAB3-mCherry co-localizes with SPL8-GFP in nuclei and YAB3-SPL8 BiFC
  signal is nuclear [PMID:42860685 "Their interactions with SPL8, as well as with each
  other, were confirmed in plant nuclei"]. UniProt annotates nucleus by similarity
  (ECO:0000250).

## Biological roles

- Abaxial cell fate specification: gain of function is sufficient for ectopic abaxial
  tissue [PMID:10457020 "Ectopic expression of either FILAMENTOUS FLOWER or YABBY3 is
  sufficient to specify the development of ectopic abaxial tissues in lateral organs"].
- Adaxial/abaxial polarity and lamina growth of leaves, redundantly with FIL, YAB2, YAB5
  and with LUG/LUH [PMID:19837869 "lug mutants enhance the polarity and growth defects of
  fil yab3 mutant leaves"].
- KNOX repression in leaves [PMID:12417699 "Mutations in these genes result in the
  derepression of the KNOX homeobox genes SHOOTMERISTEMLESS (STM), BREVIPEDICELLUS, and
  KNAT2 in the leaves"; "fil yab3 double mutants exhibit ectopic meristem formation on the
  adaxial surfaces of cotyledons and leaf blades"].
- Non-cell-autonomous control of SAM: embryonic SAM initiation and postembryonic SAM
  maintenance [PMID:19837869]; phyllotaxy and SAM central zone markers via LAS-mediated
  signals [PMID:18469164 "peripheral YAB1 activity nonautonomously and sequentially
  affects the phyllotaxis and growth of subsequent primordia and coordinates the
  expression of SAM central zone markers"].
- Fruit patterning: with FIL and JAG ("JAG/FIL activity") promotes valve and valve-margin
  identity via FUL and SHP [PMID:16192305 "FIL and YAB3 activate FUL and SHP redundantly
  with JAGGED (JAG)"], and negatively regulates BP in the replum [PMID:23133401 "we
  observed by qRT-PCR (quantitative real-time polymerase chain reaction) a significant
  increase in the expression levels of BP transcripts in the pistils of all backgrounds
  affected in JAG/FIL activity, including yab3"]. The yab3 single mutant has a mild fruit
  phenotype that is enhanced in as1 and fil backgrounds [PMID:23133401].
- Petiole/blade: YAB3 and FIL are required for ectopic blade outgrowth of bop1 bop2
  petioles [PMID:20610407].
- Vascular: YAB3 suppresses xylem and promotes phloem differentiation in abaxial domains
  in the VISUAL system [PMID:31922574, abstract only].
- Anther: SRDX-repression lines implicate YAB3 in anther morphogenesis and tapetal
  development, but these are dominant-negative chimera phenotypes, redundantly shared
  with family members [PMID:42860685].

## Interpretation

YAB3 is a nuclear YABBY transcription factor acting in the abaxial domain of lateral
organs. Its best-supported direct activity is transcriptional regulation (activator in
planta; repressor in complex with LUG/LUH/SEU), and its core process is abaxial cell
fate specification / adaxial-abaxial polarity. SAM, leaf, fruit, vascular and anther
phenotypes are downstream or non-cell-autonomous consequences, largely shared with FIL.
