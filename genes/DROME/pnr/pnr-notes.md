# pnr (pannier, P52168) — curation notes

Automated deep research was unavailable for this review (falcon 402, OpenAI 401); no
`-deep-research-<provider>.md` file was generated. Notes below are from cached publications
(abstracts unless stated) and the UniProt record.

## Molecular function
- GATA zinc-finger TF; binds GATAAG and transactivates a GATA-dependent promoter
  [PMID:9367990 "Pnr is a transcription factor, it binds DNA, and can activate transcription of the GATA-1 target promoter"] (full text).
- N-terminal zinc finger heterodimerizes with the FOG cofactor U-shaped, which abolishes Pnr activity
  [PMID:9367990 "Pnr and Ush are found to heterodimerize through the amino-terminal zinc finger of Pnr and when associated with Ush, the transcriptional activity of Pnr is lost"].
- Coactivators/cofactors: Chip bridges Pnr to Ac/Sc-Da [PMID:11090617 "Chip cooperates with Pannier in bridging the GATA factor with the HLH Ac/Sc and Daughterless proteins to allow enhancer-promoter interactions"];
  Toutatis [PMID:16141224 "Tou acts positively to activate proneural gene expression"]; DLMO [PMID:18689881 "DLMO can physically bind CHIP and PNR through either of the two LIM domains of DLMO"];
  Med1 [PMID:30670567 "we show that Med1 acts as a coactivator for the GATA factor Pannier during thoracic development"].
  Antagonist: Islet [PMID:16259974 "Isl antagonizes Pnr activity both by dimerization with the DNA-binding domain of Pnr"].
- Two isoforms; Pnr-beta represses pnr-alpha [PMID:20709169 "also mediate autoregulation of Pnr-β and repression of pnr-α by Pnr-β"].

## Heart
- [PMID:10572044 "pannier is expressed in the dorsal mesoderm and required for cardial cell formation while repressing a pericardial cell fate"];
  synergy with Tinman; GATA4 substitutes.
- Direct Tin target and physical partner [PMID:11336505 "pannier is a direct transcriptional target of Tinman in the heart-forming region"].
- Mesodermal requirement for tinman initiation [PMID:12756184 "pannier provides an essential function in the mesoderm for initiation of cardiac-specific expression of tinman and for specification of the heart primordium"].
- Doc/Tin/Pnr cross-regulation [PMID:16221729 "co-expression of these three genes in the cardiac mesoderm, which also involves cross-regulation, plays a major role in the specification of cardiac progenitors"].
- Direct targets Hand [PMID:15975941] and nmr/Tbx20 [PMID:15733676]; adult heart function [PMID:19494035].

## Dorsal ectoderm / notum
- Dorsal closure: upstream of dpp in leading edge [PMID:11731463 "This function of pnr is necessary for the activation of the Dpp pathway in the epidermal cells implicated in dorsal closure"].
  Amnioserosa lost prematurely in strong mutants [PMID:8807299].
- Medial selector [PMID:10952895 "pnr is the principal gene responsible for this subdivision"].
- Proneural prepattern [PMID:12119094 "the selector-like gene pannier regulates the entire pattern, and is the only factor to directly activate AS-C genes"].
- Thorax closure, upstream of Doc [PMID:35562934 "By pnr knock-down, we showed that pnr was required for notal Doc expression"] (full text).

## Curation decisions
- protein binding rows: Chip/Tou/DLMO -> MODIFY to GO:0001223 transcription coactivator binding; Iswi -> REMOVE.
- Ush rows (GO:0046982, GO:0061629) -> MODIFY to GO:0001222 transcription corepressor binding (Ush is a FOG cofactor, not a DNA-binding TF).
- GO:0007350 blastoderm segmentation -> MODIFY to GO:0009953 dorsal/ventral pattern formation.
- GO:0006963 (AMP biosynthesis, RNAi screen PMID:20421637): abstract names u-shaped only -> UNDECIDED.
- GO:0042440 pigment metabolic process (from a review, preliminary data) -> MARK_AS_OVER_ANNOTATED.
- Module (cardiac_specification_network) annoton GO:0000981 in heart development: consistent with this review.
