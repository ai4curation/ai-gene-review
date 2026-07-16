# GLS2 (Glutaminase 2, liver-type / LGA / GAB) — review notes

UniProt: Q9UI32 (GLSL_HUMAN). Gene: GLS2 (synonym GA). Human, NCBITaxon:9606.

## Identity and enzymology

- GLS2 is the **liver-type / L-type phosphate-activated glutaminase** (glutaminase 2),
  distinct from the kidney-type GLS. RecName "Glutaminase liver isoform, mitochondrial";
  EC 3.5.1.2 [file:human/GLS2/GLS2-uniprot.txt "RecName: Full=Glutaminase liver isoform, mitochondrial"].
- Catalyzes the phosphate-activated hydrolysis of L-glutamine to L-glutamate + ammonium:
  `L-glutamine + H2O = L-glutamate + NH4(+)` (Rhea:15889, EC 3.5.1.2)
  [file:human/GLS2/GLS2-uniprot.txt "Reaction=L-glutamine + H2O = L-glutamate + NH4(+)"].
  GO:0004359 "glutaminase activity" is defined exactly as this reaction (OLS: "Catalysis of the reaction: L-glutamine + H2O = L-glutamate + NH4+.").
- 602 aa precursor with an N-terminal mitochondrial transit peptide (residues 1–14)
  [file:human/GLS2/GLS2-uniprot.txt "TRANSIT         1..14"], catalytic glutaminase domain,
  and a C-terminal pair of ankyrin repeats (ANK 1 518–547, ANK 2 552–581)
  [file:human/GLS2/GLS2-uniprot.txt "REPEAT          518..547"].
- Quaternary structure: homotetramer, dimer of dimers
  [file:human/GLS2/GLS2-uniprot.txt "Homotetramer, dimer of dimers (Probable)"].

## Subcellular location and tissue distribution

- Mitochondrion [file:human/GLS2/GLS2-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion"];
  experimentally localized to mitochondria (IDA, MGI) and to mitochondrial matrix (Reactome, ARBA).
- Liver-enriched; also brain and pancreas; not in heart, placenta, lung, skeletal muscle, kidney
  [file:human/GLS2/GLS2-uniprot.txt "Highly expressed in liver. Expressed in brain and"].
  Originally cloned from ZR-75 breast-cancer cells and shown to be the liver-type isoenzyme,
  present in liver, brain and pancreas by Northern blot
  [PMID:10620514 "the gene is present in human liver, brain and pancreas"].
- Expression significantly reduced in hepatocellular carcinomas
  [file:human/GLS2/GLS2-uniprot.txt "Expression is significantly reduced in hepatocellular"].

## Function: p53 target, energy metabolism, antioxidant defense

- GLS2 is a **p53 target gene**. Two 2010 PNAS companion papers established this:
  - Hu et al. (PMID:20378837, full text available): "we identify glutaminase 2 (GLS2) as a
    previously uncharacterized p53 target gene"; "GLS2 encodes a mitochondrial glutaminase
    catalyzing the hydrolysis of glutamine to glutamate"; "GLS2 regulates cellular energy
    metabolism by increasing production of glutamate and alpha-ketoglutarate, which in turn
    results in enhanced mitochondrial respiration and ATP generation"; "GLS2 regulates
    antioxidant defense function in cells by increasing reduced glutathione (GSH) levels and
    decreasing ROS levels, which in turn protects cells from oxidative stress
    (e.g., H(2)O(2))-induced apoptosis."
  - Suzuki et al. (PMID:20351271, abstract only): "a p53 target gene, phosphate-activated
    mitochondrial glutaminase (GLS2), a key enzyme in conversion of glutamine to glutamate, and
    thereby a regulator of glutathione (GSH) synthesis and energy production"; "Elevated GLS2
    facilitates glutamine metabolism and lowers intracellular reactive oxygen species (ROS)
    levels"; "High ROS levels following GLS2 knockdown also coincide with stimulation of
    p53-induced cell death"; "overexpression of GLS2 reduces the growth of tumor cells and
    colony formation."
- UniProt FUNCTION: "Plays an important role in the regulation of glutamine catabolism.
  Promotes mitochondrial respiration and increases ATP generation ... by catalyzing the
  synthesis of glutamate and alpha-ketoglutarate. Increases cellular anti-oxidant function via
  NADH and glutathione production. May play a role in preventing tumor proliferation."
  [file:human/GLS2/GLS2-uniprot.txt "Plays an important role in the regulation of glutamine"].
- Induced by p53 at protein and mRNA level under stressed and non-stressed conditions
  [file:human/GLS2/GLS2-uniprot.txt "Up-regulated by P53 (at protein and mRNA level) under both"].
- Tumor-suppressive tendency (opposite of oncogenic GLS/kidney-type in some contexts): GLS2 lost
  in HCC and brain tumors; overexpression reduces colony formation (Hu 2010 discussion).

The GOA IMP annotations to **regulation of apoptotic process (GO:0042981)** and **reactive oxygen
species metabolic process (GO:0072593)**, both from PMID:20351271 (MGI, acts_upstream_of_or_within),
reflect these downstream regulatory phenotypes rather than the direct molecular function. They are
genuine but non-core (they are consequences of the enzymatic activity + p53 axis), so kept as
non-core.

## Protein interactions (PDZ / C-terminus)

- The C-terminal `-ESXV` motif of human glutaminase L mediates PDZ-domain interactions with
  alpha1-syntrophin (SNTA1) and a glutaminase-interacting protein (GIP = TAX1BP3), shown by
  yeast two-hybrid [PMID:11163757 "association with human"; "the sequence -ESXV as essential for
  the interaction"]. UniProt records the SNTA1/TAX1BP3 interactions
  [file:human/GLS2/GLS2-uniprot.txt "Interacts with the PDZ domain of TAX1BP3"].
  The GOA IPI for PMID:11163757 uses WITH=UniProtKB:O14907 (TAX1BP3).
- High-throughput IntAct interactions: PMID:32296183 (HuRI binary interactome) with O00291 (HIP1)
  and Q6GPH4 (XAF1); PMID:33961781 (BioPlex) with O00291 (HIP1). These are "protein binding"
  (GO:0005515) IPI annotations from proteome-scale screens; GLS2 is not named in the cached main
  text (data are in supplementary networks). Kept as MARK_AS_OVER_ANNOTATED — uninformative
  molecular-function terms per curation policy (never REMOVE an IPI protein-binding).

## Core function summary

1. **Glutaminase activity (GO:0004359)** — mitochondrial phosphate-activated hydrolysis of
   L-glutamine to L-glutamate + ammonia (EC 3.5.1.2). This is the defining molecular function.
2. **L-glutamine catabolic process (GO:0006543)** and **L-glutamate biosynthetic process
   (GO:0097054)** — the biological process the enzyme carries out (glutamine → glutamate,
   feeding alpha-ketoglutarate into the TCA cycle; in liver, ammonia for the urea cycle).
3. Localized to the **mitochondrion / mitochondrial matrix (GO:0005739 / GO:0005759)**.

Note: GO:0006537 "glutamate biosynthetic process" (as annotated in the UniProt DR line, IBA) is
**OBSOLETE** (duplicate term). The current equivalent is GO:0097054 "L-glutamate biosynthetic
process", which is what I use in core_functions. GO:0006537 does not appear in the GOA TSV /
existing_annotations, so no existing annotation needs rewriting for this.
