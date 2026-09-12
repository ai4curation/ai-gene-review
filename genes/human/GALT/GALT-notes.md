# GALT (human) — gene review notes

UniProt: P07902. Gene: GALT (galactose-1-phosphate uridylyltransferase). Chr 9p13.

## Core biology (verified)

GALT catalyses the **third, central step of the Leloir pathway** of galactose
catabolism:

  alpha-D-galactose 1-phosphate + UDP-alpha-D-glucose <=> alpha-D-glucose 1-phosphate + UDP-alpha-D-galactose
  (Rhea:RHEA:13989, EC 2.7.7.12)

- MF = **GO:0008108** UDP-glucose:hexose-1-phosphate uridylyltransferase activity.
  UniProt CATALYTIC ACTIVITY block cites ECO:0000269|PubMed:22461411 and PubMed:27005423.
- **Double-displacement ("ping-pong") mechanism** through a covalent uridylyl-enzyme
  intermediate: UMP is transferred onto active-site **His186** (HPH motif, His-Pro-His,
  residues 184–186), forming a phospho-His–UMP intermediate with release of glucose-1-P;
  the intermediate then transfers UMP to gal-1-P to form UDP-Gal.
  [PMID:27005423 "In the first step, hydrolysis of the UDP-sugar substrate results in a phospho-histidine bond between uridine monophosphate (UMP) and His166 (His186 in hGALT) from the active site motif 'HPH' (residues 164-166), with the release of hexose 1-phosphate"]
  [PMID:22461411 "the enzyme catalyzes the above-mentioned reaction through a double displacement mechanism ... to form an uridylyl-enzyme intermediate"]
- **Homodimer**, obligate; each active site formed by residues from BOTH subunits.
  [PMID:27005423 "hGALT is an obligate dimer, where each active site is formed by both dimeric subunits"]
  UniProt SUBUNIT: "Homodimer. {ECO:0000269|PubMed:27005423}."
- **Zinc binding** = structural, not catalytic. hGALT crystal structure (PDB 5IN3) shows
  ONE divalent metal site per monomer (Glu202, His301, His319, His321), ~20 Å from the
  active site, preferring Zn2+; Zn2+ stabilises the protein and prevents aggregation.
  UniProt COFACTOR annotates "Binds 2 zinc ions per subunit" (ECO:0000305|PubMed:27005423).
  [PMID:27005423 "the observed hGALT metal site is located ~20 A away from the active site ... Altogether our findings suggest hGALT contains one Zn2+ binding site, which confers stability to the protein"]
  Note: the E. coli enzyme has separate Zn (catalytic-stabilising) and Fe sites; those
  residues are NOT all conserved in human GALT — so zinc here is structural.
- **Localization: cytosol** (GO:0005829). Cytosolic metabolic enzyme (Reactome TAS;
  IBA cytoplasm).

## Disease (dismech Galactosemia.yaml + literature)

GALT deficiency causes **classic galactosemia (type I; OMIM 230400)** — autosomal
recessive, ~1/50,000 newborns (US screening). Most severe galactosemia form:
- Neonatal toxicity on milk (lactose->galactose): jaundice, hepatomegaly/liver failure,
  cataracts, renal failure, bleeding diathesis, **E. coli sepsis**, death within days if
  untreated.
  [PMID:22461411 "If the affected neonates are not treated in time, they will suffer from severe hepatic and renal failure, bleeding diatheses and E. coli sepsis, which can lead to death within days of birth"]
- Driven by accumulation of galactose-1-phosphate (and galactitol); reduced UDP-hexoses
  and disturbed glycosylation.
- Treatment = dietary galactose restriction; but long-term complications persist despite
  diet: cognitive/IQ deficits, speech dyspraxia, ataxia, premature ovarian insufficiency.
  [PMID:22461411 "long-term complications such as IQ deficits, ataxia, speech dyspraxia, and premature ovarian insufficiency persist in many patients with a galactose-restricted diet"]
- >300 disease mutations; ~60% missense. Most common p.Gln188Arg (Q188R) — active-site
  variant, ~10% residual activity, aggregation-prone. p.Ser135Leu common in Africans;
  p.Lys285Asn common in Europeans. [PMID:1897530; PMID:27005423]

## Annotation-by-annotation reasoning

- GO:0008108 (MF, uridylyltransferase): CORE. Supported by IBA, IEA(EC/RHEA), IDA
  (PMID:27005423 covalent intermediate in structure), EXP (PMID:1897530, PMID:22461411
  kinetics), TAS(Reactome). ACCEPT all instances.
- GO:0033499 (BP, Leloir catabolism): CORE. IBA + TAS(Reactome). ACCEPT.
  (Note: current ontology primary label is "galactose catabolic process via UDP-galactose,
  Leloir pathway"; GOA/stub carries older "beta-D-galactose ..." label — keep as-is,
  existing-annotation ids are trusted.)
- GO:0006012 (BP, galactose metabolic process): parent of the Leloir catabolic term.
  IEA + IDA(PMID:27005423) + TAS(PMID:1427861). Correct but less specific than GO:0033499.
  ACCEPT the direct/experimental ones; broad but not wrong.
- GO:0006011 (BP, UDP-alpha-D-glucose metabolic process): IDA PMID:27005423. GALT consumes
  UDP-glucose as the uridylyl donor -> ACCEPT (accurate; the substrate is UDP-Glc).
- GO:0008270 (MF, zinc ion binding): IEA + IDA(PMID:27005423). Real (2 Zn2+/subunit,
  structural). ACCEPT / keep as non-core structural function.
- GO:0005829 (cytosol) TAS x2, GO:0005737 (cytoplasm) IBA: ACCEPT (correct localization).
- GO:0005794 (Golgi apparatus) IDA PMID:20605918: SUSPECT. PMID:20605918 is about **Lyn
  kinase / ACSL3 Golgi export** — GALT is not in the abstract; this is a spurious/
  mis-propagated CC. GALT is a soluble cytosolic Leloir-pathway enzyme with no established
  Golgi role. -> REMOVE (contradicts established cytosolic localization; no independent
  support). This is an IEA/IDA CC error, appropriate to remove per guidelines.
- GO:0005515 (protein binding) IPI x (many): all from large-scale interactome maps
  (PMID:16189514, 25416956, 25910212, 26871637, 28514442, 32296183, 33961781). Bare,
  uninformative; no specific functional partner established. Per guidelines avoid
  'protein binding'. -> MARK_AS_OVER_ANNOTATED / keep non-core; do NOT remove (IntAct
  detections are real) but not a core function.

## Deep research
falcon deep-research file did NOT land within the 8-minute poll window; review grounded
in UniProt, GOA, dismech Galactosemia.yaml, and cached PMIDs (structure PMID:27005423,
kinetics PMID:22461411, mutation PMID:1897530, gene PMID:1427861).
