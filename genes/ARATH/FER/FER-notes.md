# FER (FERONIA) — Arabidopsis thaliana — Curation Notes

UniProt: Q9SCZ4 (FERON_ARATH). Locus AT3G51550. 895 aa precursor; signal peptide
1-27; extracellular malectin-like ectodomain (~28-447) with tandem malectin-like
folds; single-pass TM (448-468); cytoplasmic Ser/Thr protein kinase domain
(536-810). Synonyms SIRENE/SIR/SRN. Member of the CrRLK1L (Catharanthus roseus
RLK1-like) receptor kinase subfamily. PDB structures of ectodomain (6A5B, 6A5E)
and kinase domain (7XDV/W/X/Y, 9UBI) exist.

## Core molecular identity

- **Receptor Ser/Thr kinase.** UniProt RecName "Receptor-like protein kinase
  FERONIA"; EC=2.7.11.1; PROSITE Ser/Thr kinase family; catalytic activity Rhea
  RHEA:17989 (Ser) and RHEA:46608 (Thr). Active-site proton acceptor at Asp-661;
  ATP-binding K-565 (the K565R mutation abolishes kinase activity).
  [Q9SCZ4 uniprot: "RecName: Full=Receptor-like protein kinase FERONIA"; "EC=2.7.11.1";
  "MUTAGEN 565 K->R: Loss of kinase activity."]
- **Genuine active kinase but with kinase-independent (scaffolding) outputs.**
  FER autophosphorylates (IDA in PMID:17673660; in vitro Thr autophosphorylation
  at T559/T664, PMID:36053485). However, kinase-inactive FER rescues the pollen
  tube overgrowth (reception) defect while failing to restore RALF1-induced root
  growth inhibition — i.e. some signaling is kinase-independent/scaffolding.
  [PMID:31867824 "Kinase-inactive mutants of FER rescue the pollen tube overgrowth
  defect in fer mutants, but cannot restore the sensitivity to exogenous RALF1 in
  root elongation"]
- **NOT a tyrosine kinase.** UniProt and Rhea assign Ser/Thr activity only. The
  IEA GO:0004714 "transmembrane receptor protein tyrosine kinase activity" comes
  from InterPro IPR045272 (ANXUR1/2-like) mapped through a generic Tyr/Ser-Thr
  catalytic domain signature (PK_Tyr_Ser-Thr, PF07714). Plant CrRLK1Ls are Ser/Thr
  (RD) kinases. This is an over-propagated electronic mis-mapping; the correct
  receptor MF is GO:0004675 transmembrane receptor protein serine/threonine kinase
  activity.

## Ligand and co-receptors

- **RALF peptides are the ligands.** RALF1 binds FER directly (its ectodomain) and
  triggers phosphorylation/activation; fer mutants lose RALF-induced root growth
  inhibition, Ca2+ mobilization and apoplastic alkalinization.
  [PMID:24458638 "a secreted peptide, RALF ... suppresses cell elongation of the
  primary root by activating the cell surface receptor FERONIA"; "specific binding
  of RALF to FERONIA and reduced binding and insensitivity to RALF-induced growth
  inhibition in feronia mutants"; "RALF specifically bound to GST-ectoFER"]
- Multiple RALFs act through FER in different contexts: RALF1/RALF23 (vegetative,
  immunity, flowering), RALF6/7/16/36/37 (polytubey block, PMID:35050671),
  RALF33 (wound-induced root regeneration, PMID:40323783).
- **GPI-anchored co-receptors LLG1/LORELEI (LRE).** Bind FER extracellular
  juxtamembrane region; required for FER ER->PM trafficking and for FER-ROP
  signaling; llg1 and fer phenocopy.
  [PMID:26052747 "LORELEI and the seedling-expressed LRE-like GPI-AP1 (LLG1) bind
  to the extracellular juxtamembrane region of FER"; "loss of LLG1 function induces
  cytoplasmic retention of FER"; "LLG1 is a component of the FER-regulated RHO
  GTPase signaling complex"]
- **CrRLK1L partners HERK1 / ANJEA** form heterocomplexes with FER+LRE at the
  filiform apparatus for pollen tube reception.
  [PMID:31867824 "Both ANJ and HERK1 associate with FER and its proposed co-receptor
  LORELEI (LRE) in planta"]

## Downstream signaling: ROPGEF -> RAC/ROP -> NADPH oxidase ROS

- FER was found via ROPGEF1 as bait; FER is an upstream regulator of RAC/ROP
  GTPase signaling driving NADPH-oxidase-dependent ROS for polarized root hair
  growth; fer mutants have reduced active RAC/ROP and ROS.
  [PMID:20876100 "FER as an upstream regulator for the RAC/ROP-signaled pathway
  that controls ROS-mediated root hair development"; "FER was pulled down by ROP2
  GTPase in a guanine nucleotide-regulated manner"]
- This places FER as a cell-wall-integrity / cell-surface sensor whose output is
  ROP-driven ROS; the FER-LLG1-ROPGEF-RAC/ROP-RbohD module is a tetrameric complex.
  [PMID:26052747 "GTP-bound activated RAC/ROPs recruit NADPH oxidases to mediate
  downstream ROS-dependent processes"]

## Localization

- Plasma membrane, single-pass type I; accumulates asymmetrically at the synergid
  filiform apparatus.
  [PMID:17673660 "FER encodes a synergid-expressed, plasma membrane-localized
  receptor-like kinase ... accumulates asymmetrically in the synergid membrane at
  the filiform apparatus"]
- IDA PM (PMID:29042459 is a study of the PM H+-ATPase; FER co-localizes/IDA at PM).
  HDA plasma membrane (PMID:14506206, 17644812) from PM proteomics — consistent.
- HDA "plasmodesma" (PMID:21533090, plasmodesmal proteome) and HDA "plasma membrane"
  from a Golgi LOPIT study (PMID:22923678) are large-scale proteomics localizations;
  PM is the well-supported functional location. Plasmodesmal detection is plausible
  (PM is continuous through plasmodesmata) but non-core.
- ISM "extracellular region" (GO_REF:0000122, AtSubP prediction) is an electronic
  whole-protein localization prediction; FER is a single-pass PM protein with an
  extracellular ectodomain, so "extracellular region" as the cellular location is
  misleading — plasma membrane is correct.

## Biological processes (experimental, by gene)

- **Pollen tube reception / fertilization (core reproductive function).** fer
  synergids fail to arrest the pollen tube which overgrows; FER controls MLO/NORTIA
  relocalization.
  [PMID:17673660 "in the ... mutant feronia (fer), fertilization is impaired; the
  pollen tube fails to arrest and thus continues to grow inside the female gametophyte"]
- **Polytubey block / prevention of polyspermy** via septum FER-ANJ-HERK1 sensing
  pollen-tube RALF6/7/16/36/37. [PMID:35050671]
- **Cell elongation / vegetative growth** (with HERK1/THE1, largely BR-independent);
  fer RNAi dwarfs. [PMID:19383785 "fer RNAi mutants displayed striking dwarf
  phenotypes"; "functions cooperatively with, but largely independent of the BR pathway"]
- **Negative regulation of cell expansion via RALF1->FER->AHA2.** RALF1-FER inhibits
  PM H+-ATPase (AHA2 pSer899), raising apoplastic pH and suppressing root cell
  elongation. [PMID:24458638 "causes phosphorylation of plasma membrane H(+)-ATPase 2
  at Ser(899), mediating the inhibition of proton transport"]
- **Root hair development (ROS-mediated).** [PMID:20876100]
- **Defense response to fungus (powdery mildew susceptibility).** fer is PM-resistant.
  [PMID:21071669 "Homozygous fer mutants also display PM resistance, revealing a new
  function for FER"]. Note GOA term is GO:0050832 defense response to fungus with
  qualifier acts_upstream_of_or_within; FER actually promotes susceptibility (loss
  confers resistance) — the directionality is captured by the broad term + qualifier.
- **Negative regulation of ABA signaling** via ROP11/ARAC10 -> ABI2 activation;
  fer is ABA-hypersensitive. [PMID:22908257 "suppress the abscisic acid (ABA)
  response through activation of ABI2"]
- **BR and ethylene responsiveness (hormone crosstalk) in hypocotyls.**
  [PMID:20400488 "altered responsiveness to brassinosteroids ... extreme
  responsiveness to even low levels of ethylene"]
- **RALF1-regulated stomatal movement** (G protein/AGB1 dependent); IGI with AGB1.
  [PMID:29301953 "RALF1 regulates stomatal apertures and does so in a G
  protein-dependent manner ... AGB1 ... interacts with ... FERONIA"]
- **Flowering time / link to circadian clock.** FER mRNA oscillates, up-regulated by
  CCA1; fer-4 flowers late; FER affects AS of FLC/MAF. IEP "circadian regulation of
  gene expression". [PMID:31948398 "FER ... controls the flowering time"; "FER mRNA
  levels exhibit an oscillating pattern with a diurnal rhythm and that the clock
  oscillator CCA1 ... up-regulates the expression of FER"]
- **Wound-induced root-tip regeneration** via RALF33-FER-TPR4-ERF115. [PMID:40323783]
- **Immunity / mRNA nucleocytoplasmic transport** via FER-NPL4; PM nanodomain
  organization via FER-CAR. [PMID:40348341; PMID:36527240]

## Annotation review decisions (summary)

- MF kinase activity (GO:0004672 protein kinase; GO:0004674 / GO:0106310 Ser/Thr;
  IDA GO:0004672 from PMID:17673660): ACCEPT / KEEP. Core.
- GO:0004714 transmembrane receptor protein tyrosine kinase activity (IEA, InterPro):
  MODIFY -> GO:0004675 transmembrane receptor protein serine/threonine kinase
  activity. FER is Ser/Thr, not Tyr. The receptor-kinase framing IS core; just the
  tyrosine specificity is wrong.
- GO:0005524 ATP binding (IEA): ACCEPT (kinase). Non-core supporting.
- GO:0005886 plasma membrane: ACCEPT (core location). Multiple IDA/HDA.
- GO:0005576 extracellular region (ISM): MARK_AS_OVER_ANNOTATED (single-pass PM
  protein; PM is correct location, not extracellular region).
- GO:0009506 plasmodesma (HDA): KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI, 9 records): all KEEP_AS_NON_CORE (uninformative
  bare term; real interactions are RALF ligands, LLG1/LRE, ROPGEF1, HERK1/ANJ, etc.,
  better captured by specific MF/BP). Do not treat as core.
- BP terms (pollen tube reception, defense response to fungus, neg reg cell growth,
  root development, response to ethylene/BR, neg reg ABA, stomatal movement,
  circadian reg of gene expression, post-embryonic development, autophosphorylation):
  ACCEPT or KEEP_AS_NON_CORE per centrality. Pollen tube reception, neg reg cell
  growth (cell-wall integrity/RALF), and protein autophosphorylation are closest to core.
- No REMOVE actions: the only clearly-wrong electronic term (GO:0004714) is best
  handled by MODIFY (the receptor-kinase essence is correct), and the ISM
  extracellular term by MARK_AS_OVER_ANNOTATED. No UNDECIDED needed: every cited
  paper was readable (full text or informative abstract) and consistent with FER.

## Provenance note

All quotes above are verbatim substrings of the cached publications in
`publications/PMID_*.md` or of `genes/ARATH/FER/FER-uniprot.txt`. GO term
definitions for GO:0004675 verified via EBI OLS4 API
(label "transmembrane receptor protein serine/threonine kinase activity").
