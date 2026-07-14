# AMDHD1 (Q96NU7) review notes

Human gene **AMDHD1** = amidohydrolase domain-containing protein 1 = **probable
imidazolonepropionase** (EC 3.5.2.7). UniProt entry name HUTI_HUMAN. HGNC:28577,
GeneID 144193, chromosome 12.

## Core enzymatic function (from UniProt Q96NU7, authoritative)

AMDHD1 catalyses the **third step of the universal histidine degradation pathway**:
hydrolytic cleavage of the C–N bond in 4-imidazolone-5-propanoate to form
N-formimidoyl-L-glutamate (= N-formimino-L-glutamate).

- FUNCTION: "Catalyzes the hydrolytic cleavage of the carbon-nitrogen bond in
  imidazolone-5-propanoate to form N-formimidoyl-L-glutamate. This reaction
  represents the third step of the universal histidine degradation pathway."
  [file:human/AMDHD1/AMDHD1-uniprot.txt]
- CATALYTIC ACTIVITY: "Reaction=4-imidazolone-5-propanoate + H2O =
  N-formimidoyl-L-glutamate; ... EC=3.5.2.7" [file:human/AMDHD1/AMDHD1-uniprot.txt]
- PATHWAY: "Amino-acid degradation; L-histidine degradation into L-glutamate;
  N-formimidoyl-L-glutamate from L-histidine: step 3/3."
  [file:human/AMDHD1/AMDHD1-uniprot.txt]

The catalytic-activity and EC assignments in the human entry are propagated by
similarity (ECO:0000250|UniProtKB:P42084, the characterised *Agrobacterium/*bacterial
HutI ortholog); hence UniProt labels the human protein "**Probable**
imidazolonepropionase" and Reactome notes the human enzyme's existence is inferred
from high-throughput screening (Yamada et al. 2004) rather than direct human enzyme
assay [reactome:R-HSA-70906]. The activity is nonetheless strongly supported by
family membership and phylogeny (IBA to GO:0050480 by GO_Central).

### Metal cofactor / metal binding

- COFACTOR: "Name=Zn(2+) ... Name=Fe(3+) ... Note=Binds 1 zinc or iron ion per
  subunit." [file:human/AMDHD1/AMDHD1-uniprot.txt]
- Metal-coordinating residues by similarity: BINDING 260 and BINDING 334 each ligate
  Fe(3+)/Zn(2+) [file:human/AMDHD1/AMDHD1-uniprot.txt]. Substrate-binding residues
  159, 192, 263, 336 [file:human/AMDHD1/AMDHD1-uniprot.txt].
- SIMILARITY: "Belongs to the metallo-dependent hydrolases superfamily. HutI family."
  [file:human/AMDHD1/AMDHD1-uniprot.txt]

So the enzyme is a **Zn/Fe metal-dependent amidohydrolase** (metallo-dependent
hydrolase superfamily, cd01296 Imidazolone-5PH; Pfam PF01979 Amidohydro_1). Metal
ion binding is well supported → I retain GO:0046872 metal ion binding and add
GO:0008270 zinc ion binding to core_functions (Zn is the primary catalytic metal,
per P42084 evidence).

## Localization

- SUBCELLULAR LOCATION: "Cytoplasm {ECO:0000269|PubMed:39143229}."
  [file:human/AMDHD1/AMDHD1-uniprot.txt] — experimental (cholangiocarcinoma paper).
- Reactome places the reaction in cytosol (GO:0005829, TAS) [reactome:R-HSA-70906].
- GOA has cytoplasm (GO:0005737, IEA UniProtKB-SubCell) and cytosol (GO:0005829, TAS
  Reactome). Both consistent; cytosol is the more precise soluble-enzyme location.

## Histidine catabolism pathway context

Reactome R-HSA-70921 "Histidine catabolism": His → urocanate (HAL/histidase) →
4-imidazolone-5-propanoate (UROC1/urocanase) → **N-formimino-L-glutamate (AMDHD1,
step 3)** → glutamate + formimino-THF (FTCD). AMDHD1 is the third of four steps.
[reactome:R-HSA-70921 summary: "proceeds in four steps to yield glutamate"]

GOA carries two UniPathway-derived BP variants:
- GO:0019556 L-histidine catabolic process to glutamate and formamide (IEA UniPathway)
- GO:0019557 L-histidine catabolic process to glutamate and formate (IEA UniPathway)
These two describe the two alternative downstream fates of the formimino/formamido
group; they are pathway-variant descriptors auto-emitted from the UniPathway mapping.
The parent/experimentally-supported BP is GO:0006548 L-histidine catabolic process
(IBA + TAS Reactome). NOTE: GO:0019556/GO:0019557 are NOT seeded in the ai-review
YAML (they are in the UniProt DR block but not in the GOA TSV rows), so no review row
is required for them; they are mentioned here for completeness.

## Secondary / moonlighting function (single paper)

PubMed:39143229 (Ma et al., Cell Death Differ 2025) reports AMDHD1 as a tumor
suppressor in cholangiocarcinoma that promotes TGF-beta signaling by stabilizing
SMAD4 (inhibiting its ubiquitination/proteasomal degradation) and enhancing SMAD2/3
phosphorylation; it interacts with SMAD2, SMAD3, SMAD4 [file:human/AMDHD1/AMDHD1-uniprot.txt
FUNCTION + SUBUNIT]. This paper is NOT cached locally (abstract not in publications/)
and is a single primary report; the TGF-beta/tumor-suppressor role is not (yet) an
existing GO annotation in the GOA TSV, so it does not require an annotation-review
row. It informs the description as a secondary/putative moonlighting activity but is
kept out of core_functions (single study, mechanism = adaptor/stabilizer, not the
defining enzymatic function).

## Protein-binding (IPI) annotations — KLHL23

Two GO:0005515 "protein binding" IPI rows, both with_from UniProtKB:Q8NBE8 (=KLHL23),
from the BioPlex AP-MS interactome papers:
- PMID:28514442 (BioPlex 2.0, Huttlin 2017) [publications/PMID_28514442.md]
- PMID:33961781 (BioPlex 3.0, Huttlin 2021) [publications/PMID_33961781.md]
UniProt IntAct: "Q96NU7; Q8NBE8: KLHL23; NbExp=3" [file:human/AMDHD1/AMDHD1-uniprot.txt].
Both are proteome-scale HA-FLAG AP-MS screens (HEK293T/HCT116); neither paper mentions
AMDHD1 specifically or assigns it a function — AMDHD1 is one of thousands of
bait/prey entries. KLHL23 is a Kelch-like BTB adaptor; no defined biological meaning
for AMDHD1's metabolic role. These are experimental (IPI) so per policy NOT removed;
marked MARK_AS_OVER_ANNOTATED (bare "protein binding", uninformative MF). Kept out of
core_functions per curation guideline (avoid bare protein binding).

## Evidence-code summary for review actions

- IBA GO:0050480 imidazolonepropionase activity → ACCEPT (core MF; phylogenetically
  supported, matches UniProt EC and family).
- IBA GO:0006548 L-histidine catabolic process → ACCEPT (core BP).
- IEA GO:0050480 (RHEA/EC) → ACCEPT (redundant with IBA but correct catalytic MF).
- IEA GO:0016787 hydrolase activity; GO:0016810 (C-N bonds); GO:0016812 (cyclic
  amides) → these are correct-but-general ancestors of GO:0050480. MODIFY →
  GO:0050480 (the specific catalytic term is available and evidenced).
- TAS GO:0016812 (Reactome) → same generalization; MODIFY → GO:0050480.
- GO:0006548 IEA (InterPro) and TAS (Reactome) → ACCEPT (correct BP).
- GO:0005737 cytoplasm IEA and GO:0005829 cytosol TAS → cytosol is more precise;
  keep cytosol; cytoplasm ACCEPT (parent, correct) as non-core location.
- GO:0003674 molecular_function ND (root, GO_REF:0000015) → this is the
  "no-data" placeholder now superseded by real MF annotations. REMOVE (ND root
  placeholder is obsolete once informative MF exists; it is not experimental).

## Core functions selected

1. GO:0050480 imidazolonepropionase activity (catalytic MF)
2. GO:0008270 zinc ion binding (catalytic metal cofactor)
3. GO:0006548 L-histidine catabolic process (BP)
