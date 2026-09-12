# fbp (Fructose-1,6-bisphosphatase class 1) — Pseudomonas putida KT2440

UniProt: Q88CY9 (F16PA_PSEPK). Gene name `fbp`; OrderedLocusName PP_5040.
Evidence level: PE 3 (Inferred from homology). Annotations are HAMAP-Rule
MF_01855 / InterPro / PANTHER electronic transfers; there is no dedicated
biochemical paper on this specific protein. The only citation in the UniProt
record is the genome sequencing paper.

## Identity and catalytic function

- The protein is fructose-1,6-bisphosphatase class 1, EC 3.1.3.11.
  [UniProt "RecName: Full=Fructose-1,6-bisphosphatase class 1 {ECO:0000255|HAMAP-Rule:MF_01855};"]
  [UniProt "EC=3.1.3.11 {ECO:0000255|HAMAP-Rule:MF_01855};"]
- It is a phosphohydrolase: D-fructose-1,6-bisphosphate 1-phosphohydrolase.
  [UniProt "AltName: Full=D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1 {ECO:0000255|HAMAP-Rule:MF_01855};"]
- Catalytic activity: hydrolyzes the 1-phosphate of fructose 1,6-bisphosphate to
  give fructose 6-phosphate and inorganic phosphate.
  [UniProt "Reaction=beta-D-fructose 1,6-bisphosphate + H2O = beta-D-fructose 6-"]
  [UniProt "phosphate + phosphate; Xref=Rhea:RHEA:11064, ChEBI:CHEBI:15377,"]

## Cofactor / metal

- Magnesium-dependent; binds 2 Mg2+ ions per subunit.
  [UniProt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420; Evidence={ECO:0000255|HAMAP-"]
  [UniProt "Note=Binds 2 magnesium ions per subunit. {ECO:0000255|HAMAP-"]
- Metal-binding residues are annotated (e.g. positions 90, 112, 114, 115, 283).
  This makes the GO:0000287 magnesium ion binding annotation a genuine molecular
  property, though it is non-core relative to the catalytic activity.

## Pathway and biological role

- Pathway: Carbohydrate biosynthesis; gluconeogenesis (UniPathway UPA00138).
  [UniProt "PATHWAY: Carbohydrate biosynthesis; gluconeogenesis."]
- FBPase catalyzes a committed, essentially irreversible step of gluconeogenesis,
  converting fructose-1,6-bisphosphate to fructose-6-phosphate. This is the key
  control point that allows synthesis of hexose phosphates from
  triose/lower-carbon precursors.
- Biological context: P. putida KT2440 catabolizes glucose via the
  Entner-Doudoroff pathway and lacks a complete EMP/glycolytic route (no
  6-phosphofructokinase running glycolytically). FBPase is therefore central to
  gluconeogenesis — building hexose-phosphates (and ultimately precursors for
  polysaccharide/cell-envelope biosynthesis) when the cell grows on
  gluconeogenic substrates such as organic acids, amino acids, or aromatics.

## Localization and quaternary structure

- Cytoplasmic / cytosolic enzyme.
  [UniProt "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01855}."]
- Homotetramer.
  [UniProt "SUBUNIT: Homotetramer. {ECO:0000255|HAMAP-Rule:MF_01855}."]
- Belongs to the FBPase class 1 family.
  [UniProt "SIMILARITY: Belongs to the FBPase class 1 family. {ECO:0000255|HAMAP-"]

## Annotation scrutiny notes

- GO:0042132 (fructose 1,6-bisphosphate 1-phosphatase activity): exact MF, core.
  Matches EC 3.1.3.11 and RHEA:11064. ACCEPT.
- GO:0016791 (phosphatase activity): true but broad parent of GO:0042132.
  MARK_AS_OVER_ANNOTATED.
- GO:0000287 (magnesium ion binding): supported by cofactor/binding-site data but
  non-core. KEEP_AS_NON_CORE.
- GO:0006094 (gluconeogenesis): correct core BP, matches PATHWAY line. ACCEPT.
- GO:0030388 (fructose 1,6-bisphosphate metabolic process) and GO:0006002
  (fructose 6-phosphate metabolic process): accurately describe the substrate and
  product metabolism of the reaction; true but general process terms — keep as
  non-core.
- GO:0006000 (fructose metabolic process): broad/loose parent; the enzyme acts on
  phosphorylated hexoses, not free fructose. KEEP_AS_NON_CORE at best.
- GO:0005975 (carbohydrate metabolic process): correct but very broad; non-core.
- GO:0005737 (cytoplasm) and GO:0005829 (cytosol): both consistent with the
  cytoplasmic localization statement; cytosol is the more specific CC. ACCEPT
  cytosol; keep cytoplasm as non-core (redundant broader CC).
- GO:0005986 (sucrose biosynthetic process): a PANTHER/TreeGrafter homology
  transfer (PTN002265199). Sucrose biosynthesis (via sucrose-phosphate synthase/
  sucrose-phosphate phosphatase) is a plant/cyanobacterial process; the PANTHER
  family PTHR11556 spans plant SBPase/FBPase. There is no evidence P. putida
  KT2440 synthesizes sucrose, and FBPase is not a sucrose-biosynthesis enzyme.
  This is a spurious over-broad homology transfer. REMOVE.
