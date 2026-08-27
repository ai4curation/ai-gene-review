# LRP2 literature notes

## Identity, topology, and proteoform boundary

The reviewed human target is UniProtKB P98164, a 4,655-residue precursor with a
signal peptide, very large extracellular LDLR-family repeat region, one
transmembrane helix, and a cytoplasmic tail
[file:human/LRP2/LRP2-uniprot.txt]. This is a single-pass type-I receptor
architecture suited to apical cargo binding and endocytosis. The reviewed record
has no curated `ALTERNATIVE PRODUCTS` section or `VAR_SEQ` feature and gives one
RefSeq protein, NP_004516.2. Reports of extracellular-domain shedding,
cytoplasmic-tail processing, endosomal soluble forms, or non-human splice
products should not be recast as named human P98164 isoforms. PANTHER
PTHR22722:SF11 is the LRP2-specific subfamily represented across human, mouse,
rat, and pig; broader LDLR-family assignments are not safe evidence of an exact
LRP2 function. PDB 9CWM covers full-length human LRP2 as a two-chain 3.3-A
cryo-EM structure, but the current record has no associated publication, so it
is architecture evidence rather than literature-backed functional evidence.
PDB 2M0P is instead an NMR structure limited to residues 1103-1148
[file:human/LRP2/LRP2-uniprot.txt].

## Core endocytic mechanism

Recent cryo-EM directly explains the receptor cycle. Endogenous LRP2 purified
from mouse kidney adopted a surface ligand-binding conformation and an endosomal
ligand-shedding conformation [PMID:36750096 Structures of LRP2 reveal a molecular
machine for endocytosis, "conformation for ligand binding at the cell surface and for ligand shedding in"].
The structure is a pH-regulated homodimer, and some human deleterious missense
variants map to sites predicted to impair dimer assembly. The mechanism is
strongly conserved and directly structural, but the purified receptor was mouse,
whereas the variant interpretation was mapped onto human alleles.

The cytoplasmic tail recruits pathway-specific adaptors. ARH/LDLRAP1 bound the
first FXNPXY motif and followed megalin through coated pits and recycling
endosomes [PMID:14528014 The adaptor protein ARH escorts megalin to and through
endosomes, "We found that ARH also binds"]. Functional
uptake was tested with megalin minireceptors in canine kidney cells. PSD-95/DLG4
binding was mapped to the megalin C-terminal PDZ-binding motif
[PMID:12713445 Selective interaction of megalin with PSD-95-like MAGUK proteins,
"binding of the C-terminus of megalin"], largely using yeast and overexpression
assays. These results support selective adaptor/scaffold interactions, not a
single constitutive signaling-receptor complex.

## Renal and epithelial cargo uptake

Direct experiments establish a broad but cargo-specific uptake repertoire:

- gp330/LRP2 bound clusterin from human milk with high affinity, whereas LRP1 did
  not bind in the same assays; receptor-expressing cells internalized and
  degraded clusterin [PMID:7768901 Identification of glycoprotein 330 as an
  endocytic receptor for clusterin, "endocytosed and degraded radiolabeled apoJ."].
- Rabbit megalin bound transcobalamin-vitamin-B12 with high affinity and rat
  systems internalized the complex [PMID:8710919 Megalin-mediated endocytosis of
  transcobalamin-vitamin-B12 complexes, "endocytosed in a RAP-inhibitable manner"].
  The human B12-homeostasis interpretation is conserved-pathway inference.
- Renal microvillar-membrane experiments identified megalin as an insulin-binding
  and internalizing receptor [PMID:9773776 Megalin is an endocytic receptor for
  insulin, "procedures, it was also shown that megalin is able to internalize insulin into"]. The
  abstract does not identify the tissue preparation as human.
- Metallothionein bound megalin but not cubilin, and rat brush-border/yolk-sac
  systems supported uptake [PMID:15126248 Megalin mediates renal uptake of heavy
  metal metallothionein complexes, "First, MT binds megalin, but not"]. This
  defines the receptor route; downstream human toxicity is not directly tested.
- Human kidney imaging and primary tubular cells, biochemical binding, and mouse
  knockout collectively support proximal-tubule survivin reuptake
  [PMID:23825075 Renal uptake of survivin is mediated by megalin, "binds megalin and cubilin and that megalin knockout mice lose survivin through"].
  The authors explicitly left the physiological function of tubular survivin
  unresolved.

Reactome curates human LRP2/CUBN uptake of vitamin-D-binding-protein cargo,
retinoid transport, and transcobalamin-cobalamin uptake. These are useful human
pathway syntheses, but their primary experimental bases include non-human models.
The direct studies above support `receptor-mediated endocytosis`; they do not
mean that every LDLR-family ligand, vitamin, hormone, metal, or protein is an
LRP2 cargo.

## Brain, hormone, and amyloid boundaries

A mixed rodent/human study reported leptin binding at choroid-plexus epithelium
and transport into brain [PMID:17324488 Megalin mediates the transport of leptin
across the blood-CSF barrier, "demonstrate that circulating leptin is transported into the brain by binding to"].
Its aging/Alzheimer observation is a correlation between lower megalin and poor
leptin entry, not proof that LRP2 loss causes human Alzheimer disease. Likewise,
miR-146a overexpression reduced LRP2 and Akt activation while increasing
apoptosis in SH-SY5Y cells [PMID:27241555 MicroRNA-146a represses LRP2
translation, "significantly decreased Lrp2 expression"]. That cultured-cell
regulatory model is non-core and does not establish patient-level causality.

For amyloid cargo, LRP2 did not bind A-beta1-40 alone; binding required a
clusterin-A-beta complex [PMID:9228033 Interaction of clusterin-amyloid-beta with
LRP2, "Abeta alone did not bind directly to LRP-2"]. LRP2-expressing cells then
internalized and degraded that complex. This supports carrier-dependent complex
clearance, not direct A-beta receptor activity or demonstrated prevention of
human neurodegenerative disease.

## Human tissue localization and disease

Human placental staining placed LRP2 mainly in first- and third-trimester
cytotrophoblasts and endolysosomal structures, with limited syncytiotrophoblast
signal [PMID:27798286 Megalin in human placental cytotrophoblasts, "predominantly expressed in cytotrophoblasts"].
The authors specifically argued that maternal nutrient uptake is unlikely to be
the main placental role. This is direct human localization but does not identify
the physiological cytotrophoblast cargo.

Human genetics establishes LRP2-related
Donnai-Barrow/facio-oculo-acoustico-renal syndrome: variants were found in six Donnai-Barrow families and one
facio-oculo-acoustico-renal family [PMID:17632512 Mutations in LRP2 cause
Donnai-Barrow and facio-oculo-acoustico-renal syndromes, "mutations in six families with Donnai-Barrow syndrome and one family with"].
The pleiotropic syndrome demonstrates organismal importance across kidney,
brain, eye, ear, and development, but individual phenotypes cannot be assigned
to a specific ligand solely from the disease association. No medical-treatment
claim follows from this curation.

## Structural ligand and assay boundaries

The human CR10 NMR structure shows how the polybasic drug gentamicin can engage
an acidic common ligand-binding motif [PMID:23275343 Gentamicin binds to the
megalin receptor, "Gentamicin binds to megalin with low affinity"]. This is
direct binding to one isolated human repeat plus modeling, not a full-length
receptor affinity or trafficking assay. It clarifies receptor biology and is
not used here to recommend or design a medical intervention.

Proteomic exosome studies (PMID:19056867 and PMID:23533145) and interactome maps
(PMID:28514442 and PMID:33961781) are screen-level observations. They can place
LRP2 in a sample or candidate network but do not establish a core exosomal role,
stable complex, or functional consequence. Broad BBB and lysosomal reviews
(PMID:17897319, PMID:26590417, PMID:30280653) provide context only.

## Paralog and species limits

LRP2 is a megalin-family multiligand receptor, not interchangeable with LRP1,
LRP1B, LDLR, or other LDLR-family proteins. Direct comparisons show paralog
specificity: LRP1 did not bind clusterin in PMID:7768901 and had no measurable
TC-B12 affinity in PMID:8710919. Conversely, generic clathrin machinery and
family architecture should not be promoted to LRP2-specific binding or signaling
claims. Human conclusions must distinguish direct human tissue/genetic evidence
from conserved mechanisms demonstrated in mouse, rat, rabbit, canine, or mixed
models.
