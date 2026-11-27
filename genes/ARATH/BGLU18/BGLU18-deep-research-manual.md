# BGLU18 (At1g52400, AtBG1, BGL1) - manual literature synthesis

No deep-research provider was available for this session; this file was compiled manually from
the cached publications in `publications/` and PubMed searches ("BGLU18 Arabidopsis", 15 hits).

## Identity

- UniProtKB Q9SE50 (BGL18_ARATH), 528 aa, glycoside hydrolase family 1 (GH1), PANTHER
  PTHR10353:SF179. Signal peptide 1-26, C-terminal ER-retention motif 525-528, catalytic
  Glu207 (proton donor) and Glu422 (nucleophile).
- Synonyms: AtBG1 / BG1 (Lee et al. 2006), BGL1 (Stotz et al. 2000). Member of GH1 subfamily III
  together with BGLU19-BGLU25 (PYK10 = BGLU23), all ER-retained
  [PMID:30696747 "The Arabidopsis genome contains eight members of BGLU subfamily III"].

## Molecular function: ABA-glucose ester beta-glucosidase

- Lee et al. 2006 (Cell) identified AtBG1 as the enzyme that releases active ABA from ABA-GE
  [PMID:16990135 "Here we report that AtBG1, a beta-glucosidase, hydrolyzes glucose-conjugated, biologically inactive ABA to produce active ABA."].
- UniProt curated: E207Q abolishes ABA-GE hydrolysis (MUTAGEN, ECO:0000269 PMID:16990135); no
  activity on zeatin glucoside.
- Kato-Noguchi & Tanaka 2008 measured ABA-GE beta-glucosidase activity in crude seedling extracts
  (pH optimum 6.0, Km 0.41 mM) [PMID:17923167 "The pH optimum of this enzyme in crude extract of Arabidopsis seedlings was 6.0"].
  This is a tissue activity, not a purified BGLU18 measurement (abstract only).
- Activation by stress-induced polymerisation
  [PMID:16990135 "Dehydration rapidly induces polymerization of AtBG1, resulting in a 4-fold increase in enzymatic activity."].
- Han et al. 2020: activity in leaf petioles depends on ER dynamics; BGLU18 shifts from ER bodies
  to the microsomal ER under dehydration
  [PMID:31761937 "Collectively, these results uncover a direct relationship between ER body number and BGLU18-mediated ABA-GE hydrolysis activity."].
- Possible second activity: thioglucosidase (atypical myrosinase) for 4-methoxyindol-3-ylmethyl
  glucosinolate, shown only in the bglu18 pyk10 double mutant
  [PMID:30696747 "These results suggest that 4MI3G is hydrolyzed by BGLU18 and/or PYK10, but not by TGG1 and TGG2"].
  Hornbacher et al. 2022 could not confirm glucobrassicin breakdown
  [PMID:36388588 "However, the certain involvement of BGLU18 in the breakdown of glucosinolates could not be demonstrated"].

## Location

- ER lumen; main cargo of wound/JA-inducible ER bodies and of leaf ER bodies
  [PMID:19147648 "BGLU18 protein was exclusively localized in ER bodies formed directly at the wounding site on cotyledons"],
  [PMID:30696747 "These results indicate that two types of β-glucosidases, BGLU18 and PYK10/BGLU23, are accumulated in L-ER bodies."],
  [PMID:34110257 "PYK10 (BGLU23) and BGLU18 are the most abundant ER body proteins."].
- Proteomic hits in nucleus, chloroplast, peroxisome, vacuole and plasmodesmata are high-throughput
  and conflict with the ER-retention signal; peroxisomal authors nevertheless argued against
  co-purification artefacts (PMID:17951448).

## Biological roles

- ABA homeostasis and drought/salt tolerance: loss of AtBG1 causes defective stomatal movement,
  early germination, stress sensitivity and lower ABA (PMID:16990135); loss delays dehydration-induced
  ABA accumulation (PMID:31761937).
- JA/ABA cross-talk: MYC2-ABI5 activates BGLU18 in detached leaves (PMID:40088448, abstract);
  MYB47/MYB95 regulate BGLU18 in JA-inducible ER bodies (PMID:41006709).
- Inducible ER body formation: bglu18 knockouts fail to form wound-induced ER bodies (PMID:19147648).
- Defence: L-ER bodies (BGLU18 + PYK10) protect leaves against isopod herbivory (PMID:30696747);
  ER bodies negatively regulate immunity to Pseudomonas (PMID:34110257).

## Expression

- Induced by ABA, dehydration, wounding and salt (UniProt INDUCTION); down-regulated by aphid
  feeding [PMID:23144921 "BGL1, commonly induced by JA, was down-regulated after feeding by either M. persicae or B. brassicae in all water treatments."].
