# KMO (kynurenine 3-monooxygenase) — review notes

UniProt: O15229 (KMO_HUMAN); HGNC:6381; EC 1.14.13.9; 486 aa. Human, chromosome 1.
Source files used: `KMO-uniprot.txt`, `KMO-goa.tsv`, and cached publications under `publications/`.

## Core identity and function

KMO is **kynurenine 3-monooxygenase** (a.k.a. kynurenine 3-hydroxylase, K3H), an
**FAD-dependent, NADPH-dependent flavin monooxygenase** that hydroxylates
**L-kynurenine to 3-hydroxy-L-kynurenine** using O2 and NADPH.

- Catalytic activity / cofactor / EC, from UniProt:
  [file:human/KMO/KMO-uniprot.txt "Reaction=L-kynurenine + NADPH + O2 + H(+) = 3-hydroxy-L-kynurenine + NADP(+) + H2O"],
  [file:human/KMO/KMO-uniprot.txt "Name=FAD; Xref=ChEBI:CHEBI:57692"],
  [file:human/KMO/KMO-uniprot.txt "EC=1.14.13.9"].
- Enzyme class described in the original cloning paper:
  [PMID:9237672 "Kynurenine 3-monooxygenase, an NADPH-dependent flavin monooxygenase, catalyses the hydroxylation of L-kynurenine to L-3-hydroxykynurenine"].
- One non-covalently bound FAD per enzyme molecule:
  [PMID:10672018 "to contain one molecule of non-covalently bound FAD per molecule of enzyme"].
- FAD-dependence and OMM location stated explicitly in the structure paper:
  [PMID:23575632 "KMO is a flavin adenine dinucleotide (FAD)-dependent monooxygenase and is located in the outer mitochondrial membrane where it converts l-kynurenine to 3-hydroxykynurenine"].

## Subcellular location

Outer mitochondrial membrane, multi-pass membrane protein.
- [file:human/KMO/KMO-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion outer membrane"] and
  [file:human/KMO/KMO-uniprot.txt "Multi-pass membrane protein"].
- Rat-liver-mitochondria basis stated by Reactome: [reactome:R-HSA-71200 "The localization of KMO to the outer mitochondrial membrane is inferred from studies of the enzyme in rat liver mitochondria (Okamoto et al. 1967)"].
- Note: the Reactome display text confusingly opens with "Cytosolic kynurenine 3-monooxygenase (KMO)" but its own summary then places the enzyme on the outer mitochondrial membrane; the authoritative UniProt/experimental call is OMM.
- Transmembrane domains (TM 385-404, 425-445) are required for enzymatic activity:
  [file:human/KMO/KMO-uniprot.txt "Transmembrane domains are required for enzymatic activity"].
- Detected in the high-confidence human mitochondrial proteome (HTP): PMID:34800366
  (large quantitative MS dataset; KMO is one of the catalogued mitochondrial proteins — consistent with, but less specific than, the OMM call).

## Pathway position: branch-point gatekeeper of the kynurenine pathway

KMO sits at the committed branch of the kynurenine pathway. Its product 3-hydroxykynurenine
feeds toward **quinolinate → NAD+** (de novo NAD+ biosynthesis from tryptophan), while the
competing branch produces the neuroprotective metabolite **kynurenic acid (KYNA)**.

- UniProt pathway: [file:human/KMO/KMO-uniprot.txt "Cofactor biosynthesis; NAD(+) biosynthesis; quinolinate from"] "L-kynurenine: step 1/3" (UPA00253, UER00328).
- "Required for synthesis of quinolinic acid, a neurotoxic NMDA receptor antagonist":
  [file:human/KMO/KMO-uniprot.txt "Required for"] ... "synthesis of quinolinic acid".
- Kmo-knockout mice: kynurenine backs up, flux is diverted to KYNA; KMO is the "gatekeeper":
  [PMID:26752518 "KMO is normally the predominant pathway for metabolism of kynurenine"],
  [PMID:26752518 "There is preferential diversion of kynurenine metabolism to kynurenic acid in the Kmonull mice"],
  [PMID:26752518 "KMO is the key gatekeeper enzyme that determines the metabolic fate of kynurenine"].

Because loss/inhibition of KMO **raises** KYNA, KMO is NOT itself an enzyme "involved in
kynurenic acid biosynthesis" — the GOA IEA to GO:0034276 (kynurenic acid biosynthetic
process, transferred from a rat ortholog) is biologically backwards and is removed here.

## Side / uncoupled activity: NAD(P)H oxidase, H2O2 production

Under uncoupling (notably in the presence of certain inhibitors or when the substrate is
absent/product present), the reduced flavin reacts with O2 to make H2O2 rather than
hydroxylating substrate — an experimentally documented but non-physiological side reaction,
not the evolved core function.
- Uncoupling / peroxide formation: [PMID:10672018 "suggesting an uncoupling effect of"] "3-hydroxykynurenine with peroxide formation".
- Inhibitor (UPF 648) accelerates H2O2 ~20-fold: [PMID:23575632 "Binding UPF 648 was found to accelerate hydrogen peroxide formation by a factor of ~20-fold compared to reactions in absence of UPF 648"].
- The GO:0016174 (NAD(P)H oxidase, H2O2-forming) IDA annotations (PMID:23575632, PMID:29429898)
  capture this real-but-non-core activity → kept as non-core.

## Structure / mechanism

- FAD/NAD(P)-binding Rossmann fold (Gene3D 3.50.50.60; Pfam PF01494 FAD_binding_3); aromatic-ring
  hydroxylase family, KMO subfamily [file:human/KMO/KMO-uniprot.txt "Belongs to the aromatic-ring hydroxylase family. KMO"].
- PDB 5X68: human KMO 1-374 in complex with FAD; multiple FAD-binding residues and L-kynurenine
  substrate-binding residues annotated (e.g. Arg85/Tyr99 substrate binding; mutation abolishes activity).
- Active-site mutagenesis (PMID:29208702): R85A/K, Y99A, N363D, Y398A/F abolish KMO activity;
  C-terminal ~110 aa essential for activity (allosteric tunnel binds Ro 61-8048).

## Disease / drug-target context

Major CNS drug target. KMO inhibition shifts kynurenine flux toward neuroprotective KYNA and
away from neurotoxic 3-HK/quinolinate; beneficial in Huntington's, Alzheimer's, Parkinson's
models, cerebral malaria, and acute pancreatitis-associated multi-organ failure.
- [PMID:23575632 "Inhibition of kynurenine 3-monooxygenase (KMO) ... leads to amelioration of Huntington's-disease-relevant phenotypes in yeast, fruitfly and mouse models, as well as in a mouse model of Alzheimer's disease"].
- Acute-pancreatitis MODS therapeutic target (GSK180 inhibitor): [PMID:26752518 "kynurenine-3-monooxygenase (KMO), a key enzyme of tryptophan metabolism, is central to the pathogenesis of AP-MODS"].

## Annotation-review decisions (summary)

Core functions retained:
- GO:0004502 kynurenine 3-monooxygenase activity (MF) — IDA×several, IBA, TAS.
- GO:0071949 FAD binding (MF, cofactor) — IDA.
- GO:0005741 mitochondrial outer membrane (location) — EXP, IBA, TAS, ISS.
- GO:0034354 'de novo' NAD+ biosynthetic process from L-tryptophan / GO:0006569 L-tryptophan
  catabolic process / GO:0019805 quinolinate biosynthetic process (BP).

Kept as non-core / over-annotated:
- GO:0050660 flavin adenine dinucleotide binding — redundant IEA duplicate of GO:0071949.
- GO:0016174 NAD(P)H oxidase, H2O2-forming (IDA) — real uncoupled side activity, not core.
- GO:0031966 mitochondrial membrane — less-specific parent of OMM.
- GO:0005739 mitochondrion (HTP) — correct but less specific.
- GO:0019674 NAD+ metabolic process, GO:0009435 NAD+ biosynthetic process — broad parents of
  the specific de-novo-NAD+/quinolinate terms.
- GO:0014049 / GO:1903296 (positive regulation of glutamate secretion / neurotransmission),
  GO:0032496 / GO:0071222 (response to / cellular response to LPS), GO:0071347 (cellular
  response to IL-1) — indirect/inflammatory electronic transfers from the rat ortholog; over-annotations.

Removed (clearly-wrong IEA):
- GO:0005576 extracellular region — an OMM multi-pass membrane enzyme is not extracellular;
  spurious ortholog-transfer.
- GO:0034276 kynurenic acid biosynthetic process — biologically backwards (KMO diverts flux
  AWAY from KYNA; its loss raises KYNA).
</content>
</invoke>
