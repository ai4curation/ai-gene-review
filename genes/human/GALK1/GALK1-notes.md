# GALK1 (human) review notes

UniProtKB: P51570 · HGNC:4118 · Gene ID 2584 · Chromosome 17q25.1

## Core biology (verified)

GALK1 is the cytosolic ATP-dependent galactokinase that catalyses the **second step**
of the Leloir pathway (first *committed* / phosphorylation step of galactose catabolism):

- Reaction: alpha-D-galactose + ATP -> alpha-D-galactose 1-phosphate + ADP + H+ (RHEA:13553, EC 2.7.1.6)
- UniProt FUNCTION: "Catalyzes the transfer of a phosphate from ATP to alpha-D-galactose and
  participates in the first committed step in the catabolism of galactose."
  [ECO:0000269|PubMed:12694189, ECO:0000269|PubMed:7542884]
- Kinetic mechanism: ordered ternary complex, ATP binds first [PMID:12694189, PMID:14596685].
- KM ~970 uM galactose, ~34 uM ATP [PMID:12694189].
- Member of the GHMP kinase family, GalK subfamily [UniProt SIMILARITY].
- Homodimer [ECO:0000305|PubMed:15590630].
- Substrate specificity: strict at C4/C6 of the sugar ring; D-galactose and 2-deoxy-D-galactose
  are substrates, but D-glucose, D-fucose, L-arabinose, N-acetyl-D-galactosamine are NOT
  phosphorylated [PMID:14596685].

## Localization
- Cytosolic. In vitro translation shows the protein is cytosolic and NOT associated with the
  ER membrane [PMID:8908517] -> this is the basis of both the cytoplasm IDA and the NOT|membrane IDA.
- Reactome & IBA also place activity in cytosol (GO:0005829).
- HDA "membrane" (PMID:19946888, NK-cell membrane proteome) and "extracellular exosome"
  (PMID:19056867, urinary exosome proteomics) are high-throughput proteomic co-purifications;
  not the site of catalytic function. Note NOT|located_in membrane (IDA, PMID:8908517)
  directly contradicts the membrane HDA.

## Disease
- Deficiency -> Galactosemia type II (GALAC2, MIM:230200; MONDO:0009255 galactokinase deficiency),
  autosomal recessive. Hallmark = early-onset **cataracts** from galactitol accumulation in the
  lens via aldose reductase. Milder than classic (GALT) galactosemia; lacks the systemic
  hepatic/neuro toxicity. [dismech Galactosemia.yaml; PMID:3043741; PMID:12694189; PMID:14596685]
- Many disease variants characterized biochemically: P28T (Romani founder), V32M, G36R, H44Y,
  R68C, A198V (Osaka, mild), R239Q, G346S, G349S, T288M, A384P [PMID:12694189, PMID:15024738].

## Annotation review decisions (summary)
- Core MF: GO:0004335 galactokinase activity (EXP/IDA PMID:7542884, PMID:12694189; IBA; IEA) -> ACCEPT.
- ATP binding GO:0005524 (IDA PMID:12694189; IEA) -> ACCEPT (real cofactor/substrate, ordered mechanism ATP first).
- galactose binding GO:0005534 (IDA PMID:14596685) -> ACCEPT (substrate binding directly demonstrated).
- BP galactose metabolic process GO:0006012 (IBA, IEA, IMP) -> ACCEPT; GO:0033499 Leloir pathway (IEA, TAS) -> ACCEPT (more specific, correct).
- cytosol GO:0005829 (IBA, TAS x2) -> ACCEPT. cytoplasm GO:0005737 (IDA PMID:8908517, IEA) -> ACCEPT.
- NOT|membrane GO:0016020 (IDA PMID:8908517) -> ACCEPT (informative negation).
- membrane GO:0016020 (HDA PMID:19946888) -> MARK_AS_OVER_ANNOTATED (HT proteomics; contradicted by NOT IDA).
- extracellular exosome GO:0070062 (HDA PMID:19056867) -> KEEP_AS_NON_CORE (HT proteomics; not functional site).
- kinase activity GO:0016301, phosphotransferase alcohol acceptor GO:0016773 (IEA InterPro) -> MODIFY -> GO:0004335 (too generic parents).
- carbohydrate phosphorylation GO:0046835 (IEA) -> KEEP_AS_NON_CORE (correct but generic BP subsumed by galactose catabolism).
- protein binding GO:0005515 (IPI PMID:32296183, HuRI Y2H, PNRC2/Q9NPJ4) -> REMOVE (uninformative bare term; single HT Y2H interactor, no functional meaning for a soluble metabolic enzyme).
</content>
