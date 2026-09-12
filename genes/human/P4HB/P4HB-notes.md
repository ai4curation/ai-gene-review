# P4HB (PDI / PDIA1) research notes

UniProt: P07237. EC 5.3.4.1 (protein disulfide isomerase). Prototypical ER thioredoxin-fold
redox protein. Multidomain: a-b-b'-a' thioredoxin-like domains with two catalytic CXXC (a, a')
active sites; C-terminal KDEL ER-retention.

## Core multifunctional biology (well-established)
- Catalyzes formation, breakage and REARRANGEMENT of disulfide bonds [uniprot "This multifunctional
  protein catalyzes the formation, breakage and rearrangement of disulfide bonds"]. PDI activity
  EXP/IDA/TAS (PMID:15720785, 15225124, 21091435, 32149426, 2846539). EC 5.3.4.1.
- Also has thiol oxidase activity (GO:0016972 IDA PMID:21091435, with ERO1B) and protein-disulfide
  REDUCTASE activity (GO:0015035 EXP/IDA PMID:21308844, 16677074, 21670307). At the cell surface
  acts as a reductase cleaving disulfide bonds of cell-attached proteins.
- Redox-dependent CHAPERONE: at high concentration + FAM20C phosphorylation inhibits aggregation
  of misfolded proteins (chaperone); at low concentration facilitates aggregation (anti-chaperone)
  [uniprot]. protein folding in ER (GO:0034975 IDA PMID:21091435), response to ER stress, ER
  chaperone complex.
- STRUCTURAL beta-subunit of prolyl 4-hydroxylase: forms alpha2beta2 tetramer with P4HA1/2; P4HB
  is the structural subunit, contributes_to procollagen-proline 4-dioxygenase activity (GO:0004656
  IDA/TAS PMID:7753822, 2846539), part of procollagen-proline 4-dioxygenase complex (GO:0016222),
  peptidyl-proline hydroxylation (GO:0018401) [uniprot "Interacts with P4HA2, forming a
  heterotetramer... where P4HB plays the role of a structural subunit"].
- STRUCTURAL subunit of microsomal triglyceride transfer protein (MTTP/MTP): heterodimerizes with
  MTTP (GO:0046982 IDA PMID:23475612; partner P55157=MTTP), stabilizes/retains it in ER without
  contributing to catalysis [uniprot]. protein-containing complex.
- ERN1/IRE1A regulation: FAM20C-phosphorylated PDI binds ERN1 and attenuates its activity
  (UPR regulation) [PMID:32149426].
- Cell-surface/immune roles: LGALS9 receptor retaining PDI at Th2 cell surface, increasing reductase
  activity, enhancing T cell migration (GO:2000406 IDA PMID:21670307); integrin binding (P05106=ITGB3);
  positive regulation of viral entry (HIV gp120 reduction; GO:0046598 IMP PMID:21670307); IL-12/IL-23
  signaling (Reactome TAS).
- beta-actin Cys374 interaction regulating actin (cytoplasmic/cytoskeletal pool): actin binding
  GO:0003779 (IPI PMID:24415753 P60709=ACTB), positive regulation of cell adhesion/spreading,
  lamellipodium/cytoskeleton localization [PMID:24415753 "Protein disulfide isomerase directly
  interacts with beta-actin Cys374 and regulates..."].
- Insulin processing (GO:0030070 IEA/TAS).

## Subcellular location
ER (primary), ER lumen, melanosome, cell membrane (peripheral; cell surface, shedding), ERGIC,
extracellular (NAS/exosome), focal adhesion/cytoskeleton/lamellipodium (actin pool). RNA binding
(HDA, mRNA interactome) — non-core.

## Action plan
- PDI activity GO:0003756 (EXP/IDA/TAS/IEA): ACCEPT core MF.
- protein-disulfide reductase activity GO:0015035 (EXP/IDA/IEA): ACCEPT (core; cell-surface reductase).
- thiol oxidase activity GO:0016972 (IDA): ACCEPT (with ERO1).
- procollagen-proline 4-dioxygenase activity GO:0004656 (IDA contributes_to/TAS): ACCEPT — structural
  beta-subunit; contributes_to is correct (not catalytic itself).
- procollagen-proline 4-dioxygenase complex GO:0016222 (IDA): ACCEPT (structural subunit).
- peptidyl-proline hydroxylation GO:0018401 (IDA acts_upstream): KEEP_AS_NON_CORE (process via complex).
- protein heterodimerization GO:0046982 (IDA, MTTP): ACCEPT (MTTP structural subunit).
- ER chaperone complex GO:0034663 / protein-containing complex GO:0032991: KEEP_AS_NON_CORE.
- protein folding / protein folding in ER / response to ER stress: KEEP_AS_NON_CORE (process; PDI
  MF is core). Actually protein folding in ER is fairly core for PDI — ACCEPT-ish but keep as MF is core.
- integrin binding GO:0005178 (IPI/IEA), enzyme binding, complex binding: KEEP_AS_NON_CORE.
- actin binding GO:0003779 (IPI ACTB): KEEP_AS_NON_CORE (cytoplasmic moonlighting pool).
- cell-adhesion/spreading/T-cell migration/viral entry/IL signaling: KEEP_AS_NON_CORE (moonlighting/surface).
- insulin processing: KEEP_AS_NON_CORE.
- regulation of oxidative-stress apoptosis / cellular response to hypoxia (IMP 12095988 UBQLN1): KEEP_AS_NON_CORE.
- ER / ER lumen / melanosome / plasma membrane / external side PM / ERGIC / focal adhesion /
  cytoskeleton / lamellipodium / cytosol / extracellular / exosome: ACCEPT ER/ER-lumen primary;
  others KEEP_AS_NON_CORE. Redundant Reactome ER-lumen TAS -> KEEP_AS_NON_CORE.
- RNA binding HDA: KEEP_AS_NON_CORE.
- protein binding IPI block: KEEP_AS_NON_CORE; MODIFY MTTP partners (P55157) to protein heterodimerization
  or keep; MARK_AS_OVER_ANNOTATED the broad screens (32296183, 32814053).
