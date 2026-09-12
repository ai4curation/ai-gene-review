# ACADM (MCAD) review notes

UniProt: P11310 | HGNC:89 | EC 1.3.8.7 | Medium-chain specific acyl-CoA dehydrogenase, mitochondrial.

## Core biology

MCAD catalyzes the first (rate-committed) step of each cycle of mitochondrial fatty acid
beta-oxidation for medium-chain acyl-CoA esters: the FAD-dependent alpha,beta-dehydrogenation
of a saturated acyl-CoA to the corresponding trans-2-enoyl-CoA, with electrons passed to the
electron-transfer flavoprotein (ETF).

- "Medium-chain specific acyl-CoA dehydrogenase is one of the acyl-CoA dehydrogenases that
  catalyze the first step of mitochondrial fatty acid beta-oxidation (FAO), breaking down fatty
  acids into acetyl-CoA and allowing the production of energy from fats" [UniProt P11310 FUNCTION].
- "The first step of FAO consists in the proR-proR stereospecific alpha, beta-dehydrogenation of
  fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their physiologic
  electron acceptor, resulting in the formation of trans-2-enoyl-CoA ((2E)-enoyl-CoA)" [UniProt P11310].
- Substrate preference C6-C12 (optimum hexanoyl/octanoyl-CoA), can extend to C14/C16:
  KM values 175 uM butyryl-CoA, 15 uM hexanoyl-CoA, 3.4 uM octanoyl-CoA [UniProt P11310 BIOPHYSICOCHEMICAL PROPERTIES, PMID:8823175].
- [PMID:19224950 "MCAD is a member of the acyl-CoA dehydrogenase (ACAD) family of flavoproteins, which catalyzes the first step of the mitochondrial β-oxidation of medium-chain fatty acids"].

## Catalysis, active site, FAD

- Catalytic base is Glu (Glu376 in mature numbering = Glu401 in precursor used by UniProt FT ACT_SITE 401).
  [PMID:1970566 "Glutamic acid 376, which has been proposed by Powell and Thorpe ... as an essential
  residue and the proton-abstracting base at the active site of the enzyme, was mutated to glutamine"];
  the Gln376 mutant "is devoid of activity (less than 0.02% that of wild type)".
- The position of the catalytic Glu determines chain-length specificity: MCAD has Glu376 on loop JK;
  LCAD/IVD have Glu255 on helix G. [PMID:8823175 "The catalytically essential glutamate residue that
  initiates catalysis by abstracting the substrate alpha-hydrogen as H+ is located at position 376
  (mature MCADH numbering) on loop JK in medium chain acyl-CoA dehydrogenase (MCADH)"].
- FAD is the bound cofactor; the WT enzyme "is a yellow protein due to the content of stoichiometric FAD"
  [PMID:1970566]. UniProt COFACTOR: FAD. Each subunit contains 1 mol FAD [PMID:3597357].

## Oligomeric state and location

- Soluble homotetramer. [PMID:3597357 "indicating a homotetrameric structure"] (native MW ~178,000;
  subunit ~44,000). UniProt SUBUNIT: "Homotetramer". Maier et al. confirm recombinant human MCAD elutes
  as a tetramer: [PMID:19224950 "Wild-type MCAD was eluted in the tetrameric form with an almost
  negligible amount of aggregates"].
- Mitochondrial matrix. [UniProt P11310 SUBCELLULAR LOCATION "Mitochondrion matrix" ECO:...PubMed:16020546].
  N.B. PMID:16020546 is the ACAD9 paper; it reports MCAD localization context only indirectly. UniProt
  cites PubMed:16020546 for the matrix location of MCAD. Mature protein after cleavage of a 25-aa transit peptide.
- GOA also has a "mitochondrial membrane" IDA (PMID:16020546) and a sperm-nucleus HDA (PMID:21630459) and
  an "axon" IDA (PMID:21237683). The axon call reflects neuronal expression: [PMID:21237683 "MCAD in the
  molecular layer and axons of specific neurons"]. The nucleus HDA is from a sperm-nucleus proteome whose
  isolation explicitly removed mitochondria; for a matrix FAO enzyme this is best treated as contaminant /
  non-core. [PMID:21630459 "sperm nuclei were obtained through CTAB treatment and isolated to over 99.9%
  purity without any tail fragments, acrosome or mitochondria"].

## ETF as physiological electron acceptor

- MCAD donates electrons to ETF; structure of the human ETF.MCAD complex solved.
  [UniProt P11310 "ETF is the electron acceptor that transfers electrons to the main mitochondrial
  respiratory chain via ETF-ubiquinone oxidoreductase" ECO:...PubMed:15159392, PubMed:25416781].
- METTL20/ETFbeta-KMT methylation of ETFbeta reduces electron transfer FROM MCAD; this is a regulatory
  observation about ETFbeta, used by GOA to support MCAD's FAO process annotation.
  [PMID:25416781 "METTL20-mediated methylation of ETFβ in vitro reduced its ability to receive electrons
  from the medium chain acyl-CoA dehydrogenase and the glutaryl-CoA dehydrogenase"].

## Disease (MCAD deficiency, ACADMD; MIM 201450)

- Most common inherited FAO disorder; common mutation c.985A>G (K304E precursor numbering; K329E by mature
  pre-cleavage convention used in older papers). [PMID:2393404 "A single A to G nucleotide replacement which
  resulted in lysine329-to-glutamic acid329 substitution of the MCAD protein was identified in all cultures
  ... this point mutation was present in 91% (31 of 34) of mutant MCAD alleles"].
- Mechanism is protein misfolding / impaired tetramer assembly with loss of function.
  [PMID:1902818 "mutant MCAD, which was demonstrated to be inactive, probably because of the inability to
  form active tetrameric MCAD"]; [PMID:19224950 "results substantiate the hypothesis of protein misfolding
  with loss-of-function being the common molecular basis in MCADD"].

## Physiology: carnitine, exercise

- MCADD patients accumulate octanoylcarnitine; they can upregulate carnitine biosynthesis during exercise.
  [PMID:16972171 "Our results suggest that MCADD patients are able to increase carnitine biosynthesis during
  exercise to compensate for carnitine losses"]. This is an indirect, secondary metabolic consequence of
  MCAD deficiency (acylcarnitine handling), NOT evidence that MCAD itself carries out carnitine biosynthesis;
  the IMP carnitine-process annotations (GO:0045329 carnitine biosynthetic process, GO:0019254 carnitine
  metabolic process CoA-linked) are downstream/indirect and should be demoted from core.

## Annotation strategy summary

- Core MF: GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity (strong EXP/IDA support).
- Core BP: GO:0006635 fatty acid beta-oxidation / GO:0033539 FAO using acyl-CoA dehydrogenase;
  GO:0051793 medium-chain fatty acid catabolic process; GO:0051791 medium-chain fatty acid metabolic process.
- Core CC: GO:0005759 mitochondrial matrix.
- Cofactor: GO:0050660 FAD binding (correct; supported by FAD content).
- General parents kept non-core/accept: GO:0003995 acyl-CoA dehydrogenase activity,
  GO:0016627 oxidoreductase activity acting on CH-CH.
- MODIFY/over-annotation candidates:
  - GO:0004466 long-chain fatty acyl-CoA dehydrogenase activity (IEA, RHEA C14/C16): MCAD's primary
    specificity is medium-chain; C14/C16 are weak secondary substrates. MARK_AS_OVER_ANNOTATED (the
    Rhea-derived "long-chain" specific MF overstates specificity; better term is the medium-chain one).
  - GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity (IEA, RHEA pentanoyl/C5): butyryl-CoA
    KM is very high (175 uM, poor substrate); this is a separate enzyme's specialty (SCAD). MARK_AS_OVER_ANNOTATED.
  - GO:0005978 glycogen biosynthetic process (IEA Ensembl ortholog): no mechanistic link; REMOVE.
  - GO:0006111 regulation of gluconeogenesis (IEA Ensembl ortholog): indirect at best; MARK_AS_OVER_ANNOTATED.
  - GO:0019254 / GO:0045329 carnitine processes (IMP PMID:16972171): indirect patient physiology;
    KEEP_AS_NON_CORE (do not REMOVE experimental IMP).
  - GO:0005634 nucleus (HDA sperm nucleus): non-core/contaminant; MARK_AS_OVER_ANNOTATED.
  - GO:0030424 axon (IDA): neuronal expression of a mito enzyme; KEEP_AS_NON_CORE.
  - GO:0031966 mitochondrial membrane (IDA PMID:16020546): MCAD is a soluble matrix protein; keep as
    non-core/over-annotated (matrix is the precise term).
  - GO:0042802 identical protein binding (IDA): captures homotetramer; do not endorse as core MF
    (uninformative). MARK_AS_OVER_ANNOTATED but note it reflects real tetramerization.
- GO:0005737 cytoplasm (IBA) and GO:0005739 mitochondrion (various): correct but general; matrix is precise.
