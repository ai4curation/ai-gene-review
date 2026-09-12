# ALDH18A1 (P5CS) review notes

UniProt: P54886 (P5CS_HUMAN). Gene: ALDH18A1 (synonyms GSAS, P5CS, PYCS). HGNC:9722.
Taxon: Homo sapiens (NCBITaxon:9606). 795 aa. Evidence at protein level.

## Core biology

ALDH18A1 encodes delta-1-pyrroline-5-carboxylate synthase (P5CS), the mitochondrial
**bifunctional** enzyme that catalyzes the first two committed steps of proline and
ornithine biosynthesis from L-glutamate:

- N-terminal **glutamate 5-kinase (GK)** domain (residues 1-361): L-glutamate + ATP ->
  L-glutamyl 5-phosphate + ADP. EC 2.7.2.11 (Rhea:14877). GO:0004349.
- C-terminal **gamma-glutamyl phosphate reductase (GPR) / glutamate-5-semialdehyde
  dehydrogenase** domain (residues 362-795): L-glutamyl 5-phosphate + NADPH ->
  L-glutamate 5-semialdehyde (which cyclizes non-enzymatically to P5C). EC 1.2.1.41
  (Rhea:19541). GO:0004350.

[file:human/ALDH18A1/ALDH18A1-uniprot.txt REGION 1..361 "Glutamate 5-kinase"; REGION
362..795 "Gamma-glutamyl phosphate reductase"; EC=2.7.2.11 and EC=1.2.1.41 both
ECO:0000269|PubMed:26297558].

FUNCTION (UniProt): "Bifunctional enzyme that converts glutamate to glutamate 5-
semialdehyde, an intermediate in the biosynthesis of proline, ornithine and arginine"
[file:human/ALDH18A1/ALDH18A1-uniprot.txt, "an intermediate in the biosynthesis of
proline, ornithine"].

P5C sits at a metabolic branch point: it can be reduced to proline (by PYCR1/2/L) or
transaminated to ornithine (by OAT), and ornithine feeds the urea cycle
(citrulline/arginine). Hence the enzyme is upstream of proline, ornithine, arginine and
(indirectly) citrulline. [PMID:11092761 "critical step in the biosynthesis of proline,
ornithine and arginine"].

## Isoforms

Two isoforms by alternative splicing (2-aa insert at the GK active site):
- **Long** (P54886-1, displayed): expressed in multiple tissues; insensitive to ornithine
  feedback inhibition; makes proline from glutamate.
- **Short** (P54886-2; VSP_005215, Δ239-240): high in gut, participates in arginine
  biosynthesis; inhibited by L-ornithine (Ki ~0.25 mM).
[PMID:11092761 "P5CS undergoes alternative splicing to generate two isoforms";
"The short isoform has high activity in the gut, where it participates in"; UniProt
ACTIVITY REGULATION CC].

## Localization

Mitochondrion; specifically mitochondrial matrix (direct IDA). Forms rod/ring-like
(and stress-responsive filament) structures inside mitochondria.
[PMID:32770108 "P5CS localizes in mitochondria in rod- and ring-like patterns but
diffuses inside the"; UniProt SUBCELLULAR LOCATION "Mitochondrion matrix"
ECO:0000269|PubMed:32770108].
The Reactome "mitochondrial inner membrane" placements are historical (P5CS "associated
with the inner mitochondrial membrane", R-HSA-508040) or arise from ALDH18A1 being a
LONP1 protease substrate (R-HSA-9837978 / R-HSA-9838004, "LONP1 binds/degrades
mitochondrial inner membrane proteins"). Direct experimental evidence favors the matrix,
so inner-membrane calls are treated as over-annotated/non-core localization.

## Subunit / interactions

Forms homodimers/multimers; multimerization (not catalytic activity) governs its
sub-mitochondrial localization. [UniProt SUBUNIT "Can form homodimers/multimers";
PMID:32770108 "Multimerization (but not the catalytic activity) of P5CS regulates its
localization"; PMID:26320891 disease mutant "stable and able to interact with wild-type
P5CS" -> self-association / identical protein binding GO:0042802].
IntAct binary interactions (AGTRAP/Q6RW13, CMTM5/Q96DZ9, COQ9/O75208, DARS2/Q6PI48) come
from high-throughput two-hybrid interactome maps (PMID:25416956 HuRI predecessor;
PMID:32296183 HuRI) and are generic "protein binding" (GO:0005515) IPI with no
functional interpretation -> non-core.

## Moonlighting / secondary observations

- **RNA binding** (GO:0003723, HDA, PMID:22658674): identified in a HeLa mRNA-interactome
  capture screen that flagged many "RNA-binding enzymes of intermediary metabolism".
  Real observation but not an established function -> non-core.
- **Mitochondrial respiration / stress sensing** (PMID:32770108): P5CS knockout impairs
  organization of mitochondrial respiratory complexes and lipid/purine metabolism; P5CS
  redistributes under starvation/oxidative stress. [PMID:32770108 "P5CS is required for
  mitochondrial respiratory complex organization"]. Underlies the Ensembl-transferred
  "response to temperature stimulus" IEA (from rat ortholog); non-core / weak.
- **ATP-demand-driven filament formation** (PMID:39506109, Nature 2024): not in GOA/seed;
  noted for context only.

## Disease (all caused by ALDH18A1 variants; UniProt DISEASE CCs)

- Cutis laxa, autosomal recessive, 3A / ARCL3A (MIM:219150; De Barsy-like) — R84Q etc.
  [PMID:11092761, PMID:18478038, PMID:22170564, PMID:24767728].
- Cutis laxa, autosomal dominant, 3 / ADCL3 (MIM:616603) — recurrent Arg138 de novo
  [PMID:26320891].
- Spastic paraplegia 9A, autosomal dominant / SPG9A (MIM:601162) [PMID:26026163,
  PMID:26297558].
- Spastic paraplegia 9B, autosomal recessive / SPG9B (MIM:616586) [PMID:26026163].
Metabolic hallmark of P5CS deficiency: hyperammonemia with hypoornithinemia,
hypocitrullinemia, hypoargininemia and hypoprolinemia [PMID:11092761 "Their metabolic
phenotype includes hyperammonemia, hypoornithinemia,"].

## Annotation review reasoning

Two catalytic MFs are the core functions, each supported by direct human IDA
(PMID:11092761) and IMP (PMID:26297558, variant loss-of-function):
- GO:0004349 glutamate 5-kinase activity
- GO:0004350 glutamate-5-semialdehyde dehydrogenase activity

Core BP: L-proline biosynthetic process (GO:0055129) and L-ornithine biosynthetic process
(GO:0006592), both IMP. Core CC: mitochondrion (GO:0005739) / mitochondrial matrix
(GO:0005759), IDA.

Borderline:
- GO:0019240 L-citrulline biosynthetic process (IMP): P5CS acts upstream of ornithine,
  which feeds citrulline synthesis; the deficiency lowers citrulline, but ALDH18A1 does
  not itself carry out citrulline biosynthesis. Kept as non-core (indirect/downstream).
- GO:0006536 glutamate metabolic process (IMP): correct-but-broad parent (glutamate is the
  substrate). Non-core, superseded by the specific MF/BP terms.
- GO:0008652 amino acid biosynthetic process (IEA, ARBA): true but generic parent of the
  proline/ornithine BP terms. Non-core.
- GO:0003824 catalytic activity, GO:0016301 kinase activity, GO:0016491 oxidoreductase
  activity (all IEA/InterPro): correct-but-uninformative parents of the two specific
  catalytic MFs. Over-annotated relative to GO:0004349/GO:0004350.
- GO:0005737 cytoplasm (IEA/InterPro): protein is mitochondrial-matrix; cytoplasm is a
  bacterial-family-driven, overly broad/misleading localization -> over-annotated. (This
  IEA InterPro-to-GO transfer from a family that includes cytoplasmic bacterial ProB/ProA
  is arguably removable, but I mark it over-annotated to be conservative.)
- GO:0005743 mitochondrial inner membrane (TAS, Reactome x3) / GO:0031966 mitochondrial
  membrane (IEA, Ensembl): imprecise localization vs the matrix; over-annotated.
- GO:0005515 protein binding (IPI x4 in one GOA row per PMID; HuRI Y2H): bare, generic,
  non-informative -> over-annotated per policy (not removed).
- GO:0042802 identical protein binding (IDA): supported by self-association / homomultimer
  evidence; accept as non-core (structural, not the catalytic core function).
- GO:0003723 RNA binding (HDA): non-core moonlighting.
- GO:0009266 response to temperature stimulus (IEA, Ensembl from rat): weak, non-core.

Per curation policy, experimental annotations (IDA/IMP/IPI) are never REMOVEd; only clearly
wrong IEAs are candidates. I use MARK_AS_OVER_ANNOTATED for the generic-parent IEAs and the
imprecise-localization TAS/IEA, and KEEP_AS_NON_CORE for defensible secondary functions.
