# SMOX (Spermine oxidase) — review notes

UniProt: Q9NWM0 (SMOX_HUMAN). Gene: SMOX (synonyms C20orf16, SMO; ORFNames UNQ3039/PRO9854).
HGNC:15862. Chromosome 20. EC 1.5.3.16.

## Core identity and reaction

SMOX is a **soluble FAD-dependent amine oxidase** of the **flavin monoamine oxidase /
polyamine-oxidase family**. It carries out the **direct back-conversion** step of polyamine
catabolism: oxidation of **free spermine to spermidine** with release of **3-aminopropanal**
and **H2O2**.

- Reaction (UniProt CATALYTIC ACTIVITY):
  [file:human/SMOX/SMOX-uniprot.txt "Reaction=spermine + O2 + H2O = 3-aminopropanal + spermidine + H2O2;"]
  Rhea:RHEA:25804; EC=1.5.3.16; evidence from PubMed:11454677, 12141946, 12398765.
- Function summary: [file:human/SMOX/SMOX-uniprot.txt "Flavoenzyme which catalyzes the oxidation of spermine to"] ... "spermidine".
- Cofactor: binds one FAD per subunit —
  [file:human/SMOX/SMOX-uniprot.txt "Binds 1 FAD per subunit."]
  (Cofactor ChEBI:CHEBI:57692 FAD; multiple FT BINDING sites: residues 35, 55, 63, 79-80,
  261, 519, 528-529.)
- Family: [file:human/SMOX/SMOX-uniprot.txt "Belongs to the flavin monoamine oxidase family."]
- Pathway: [file:human/SMOX/SMOX-uniprot.txt "Amine and polyamine degradation; spermine degradation."]
  (UniPathway UPA00211.)

## Substrate specificity — distinguishes SMOX from PAOX

SMOX acts on **non-acetylated spermine**; it does NOT require prior N1-acetylation. This is
the key distinction from PAOX (N1-acetylpolyamine oxidase), which prefers N1-acetylated
substrates.

- [PMID:12141946 "the newly identified oxidase strongly favoured spermine over N" (1)-acetylspermine]
  and "failed to act on N (1)-acetylspermidine, spermidine or the preferred PAO substrate,
  N (1), N (12)-diacetylspermine".
- Designation as spermine oxidase to distinguish from back-conversion PAO:
  [PMID:12141946 "novel flavin-containing spermine oxidase of mammalian cell origin"].
- The contrasting PAOX enzyme (PMID:12477380) has preference ranking
  "N1-acetylspermine= N1-acetylspermidine> N1,N12-diacetylspermine>>spermine", i.e. the
  opposite of SMOX; the same paper notes SMO "prefers spermine over N1-acetylspermine".
  This paper's abstract foregrounds PAOX, but curators (FlyBase) attributed the SMOX
  spermine-oxidase-activity and polyamine-catabolism IDA annotations from the full text.
- UniProt notes SMOX can also use N1-acetylspermine and spermidine with lower affinity, isoform-
  dependent: [file:human/SMOX/SMOX-uniprot.txt "Can also use N(1)-acetylspermine and spermidine as"]
  substrates. Kinetics: KM ~0.5-0.6 uM for spermine vs ~3 uM for N1-acetylspermine; kcat 27-fold
  higher with spermine.

## Induction and inhibitors

- Inducible by antitumor polyamine analogues (e.g. N1,N11-bis(ethyl)norspermine); ~5-fold mRNA,
  >3-fold activity induction in NCI H157 cells [PMID:11454677 abstract].
- Inhibited by MDL 72,527 (mammalian PAO inhibitor), not by pargyline (MAO inhibitor) or
  semicarbazide (diamine oxidase inhibitor) [PMID:11454677 abstract]. DrugBank DB04188 = MDL72527.

## Localization

- Cytoplasm and Nucleus (isoforms 1, 4, 6) per UniProt SUBCELLULAR LOCATION.
- Experimental nuclear localization of SMO/PAOh1 (isoform 1) and SMO5 (isoform 6) by confocal
  microscopy, with increased nuclear spermine oxidation producing H2O2 near DNA
  [PMID:18422650 abstract: "significant localization of SMO protein in the nucleus, as
  determined by confocal microscopy" and "increased oxidation of spermine in the nucleus
  therefore increases the production of highly reactive H2O2 in close proximity to DNA"].
- HPA immunofluorescence: cytosol (GO:0005829), nucleoplasm (GO:0005654), nuclear membrane
  (GO:0031965). SMOX has no TM domain or membrane anchor, so the nuclear-membrane signal is
  likely perinuclear (marked over-annotated in the review).

## Isoforms

Six named isoforms by alternative splicing with different substrate affinities:
1 (PAOh1/SMO, displayed), 2 (PAOh2), 3 (PAOh3, major isoform, highest affinity), 4 (PAOh4),
5, 6 (SMO5/SMOX5). Isoform 3 is the one modeled by Reactome (R-HSA-141341 "SMOX-3").
Isoform 5 (missing 1-196) may lack activity (unconfirmed per UniProt MISCELLANEOUS).

## Disease / functional significance

The H2O2 and reactive aldehyde products link SMOX to **oxidative stress, mutagenic DNA damage,
apoptosis, and inflammation-associated carcinogenesis** (e.g. gastric/colon inflammation).
[PMID:18422650 abstract: "SMO-produced reactive oxygen species are directly responsible for
oxidative stress capable of inducing apoptosis and potentially mutagenic DNA damage" and
"the potential role of spermine oxidase in inflammation-induced carcinogenesis"].

## Annotation review decisions (summary)

Core molecular function: **GO:0052901 spermine oxidase activity** (EC 1.5.3.16), supported by
EXP (PMID:11454677, 12141946, 12398765) and IDA (PMID:12477380, 18422650). Second core MF:
**GO:0071949 FAD binding** (UniProt cofactor). Core BP: **GO:0046208 spermine catabolic
process** (IDA PMID:18422650) with broader GO:0006598 polyamine catabolic process kept
non-core. Core locations: **GO:0005829 cytosol** and **GO:0005634 nucleus**.

- MODIFY: the two general **polyamine oxidase activity** (GO:0046592) IBA/IEA annotations ->
  replace with specific spermine oxidase activity (GO:0052901).
- MARK_AS_OVER_ANNOTATED (never REMOVE experimental):
  - GO:0016491 oxidoreductase activity (IEA, uninformative parent).
  - GO:0006596 polyamine biosynthetic process (TAS Reactome; SMOX is catabolic, wrong direction).
  - GO:0006805 xenobiotic metabolic process (TAS Reactome; PAO-family generalization, SMOX acts
    on endogenous spermine).
  - GO:0031965 nuclear membrane (IDA HPA; soluble protein, likely perinuclear signal).
- KEEP_AS_NON_CORE: general cytoplasm (GO:0005737) locations, nucleoplasm (GO:0005654),
  broad polyamine catabolic process (GO:0006598).
- ACCEPT: all spermine oxidase activity (GO:0052901) MF (EXP/IDA/IEA/TAS), spermine catabolic
  process (GO:0046208) BP, cytosol (GO:0005829) and nucleus (GO:0005634) core locations.

No REMOVE actions used (per policy: no REMOVE for experimental annotations or bare protein
binding; no clearly-wrong IEA present here — the questionable IEAs are general parents best
handled by MODIFY/MARK_AS_OVER_ANNOTATED).
