# gpsA (Q88FC9) — Pseudomonas putida KT2440 (PSEPK)

Glycerol-3-phosphate dehydrogenase [NAD(P)+], biosynthetic. Locus PP_4169.
UniProt entry GPDA_PSEPK; evidence level PE 3 (inferred from homology), annotated by HAMAP-Rule MF_00394.

## FUNCTION
GpsA catalyzes the NAD(P)H-dependent reduction of the glycolytic intermediate
dihydroxyacetone phosphate (DHAP, glycerone phosphate) to sn-glycerol 3-phosphate (G3P),
the committed precursor for glycerophospholipid (membrane) biosynthesis.

- [UniProt "Catalyzes the reduction of the glycolytic intermediate"]
- [UniProt "dihydroxyacetone phosphate (DHAP) to sn-glycerol 3-phosphate (G3P), the"]
- [UniProt "key precursor for phospholipid synthesis."]

The physiologically relevant direction in vivo is the biosynthetic (reductive) direction,
DHAP -> G3P (the catalytic activity reactions are written in the oxidative direction but
flagged right-to-left as physiological).

- [UniProt "PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:11094;"]

## CATALYTIC ACTIVITY
EC 1.1.1.94. The enzyme can use either NAD(H) or NADP(H):

- NAD form: [UniProt "sn-glycerol 3-phosphate + NAD(+) = dihydroxyacetone phosphate"] / [UniProt "+ NADH + H(+); Xref=Rhea:RHEA:11092,"]
- NADP form: [UniProt "sn-glycerol 3-phosphate + NADP(+) = dihydroxyacetone phosphate"] / [UniProt "+ NADPH + H(+); Xref=Rhea:RHEA:11096,"]
- EC number: [UniProt "EC=1.1.1.94 {ECO:0000255|HAMAP-Rule:MF_00394};"]

Active site: proton acceptor at residue 191. Multiple binding residues for NADPH and for
sn-glycerol 3-phosphate are annotated (e.g. NADPH-binding at 14, 15, 35, 108, 140, 255, 279, 281;
G3P-binding at 108, 136, 191, 244, 254, 255, 256).

- [UniProt "ACT_SITE        191"]
- [UniProt "/note=\"Proton acceptor\""]

## NAD(P) BINDING / FOLD
Member of the NAD-dependent glycerol-3-phosphate dehydrogenase family, with an
N-terminal NAD(P)-binding Rossmann-like domain.

- [UniProt "Belongs to the NAD-dependent glycerol-3-phosphate"]
- [UniProt "dehydrogenase family. {ECO:0000255|HAMAP-Rule:MF_00394}."]
- InterPro/Gene3D: NAD(P)-binding Rossmann-fold domain (3.40.50.720).

## PATHWAY
Membrane lipid metabolism; glycerophospholipid metabolism. UniPathway UPA00940.

- [UniProt "Membrane lipid metabolism; glycerophospholipid metabolism."]

## SUBCELLULAR LOCATION
Cytoplasm.

- [UniProt "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00394}."]

## Curation reasoning (annotation review)

Core molecular function: glycerol-3-phosphate dehydrogenase [NAD(P)+] activity (GO:0047952,
EC 1.1.1.94). The Rhea-derived NAD+-specific (GO:0141152) and NADP+-specific (GO:0141153)
terms are accurate sub-activities reflecting the dual cofactor specificity and are accepted.

Core biological process: the biosynthetic role — production of sn-glycerol 3-phosphate as the
precursor for membrane phospholipids. GO:0046167 (glycerol-3-phosphate biosynthetic process)
and GO:0046474 (glycerophospholipid biosynthetic process) best capture this. GO:0006072
(glycerol-3-phosphate metabolic process) and GO:0006650 (glycerophospholipid metabolic process)
are correct but broader parents — kept as non-core.

Over-annotations / broad terms relative to the specific dehydrogenase activity:
- GO:0016616 (oxidoreductase activity, acting on CH-OH group, NAD or NADP as acceptor): true but
  broad parent of GO:0047952 -> over-annotated.
- GO:0051287 (NAD binding): the enzyme does bind NAD(P), but this is a broad cofactor-binding term;
  marked over-annotated given the specific activity terms are present. (It also under-represents the
  NADP usage.)

Likely incorrect / spurious homology transfers:
- GO:0005975 (carbohydrate metabolic process): InterPro transfer; GpsA is a lipid-precursor enzyme,
  not a carbohydrate-metabolism enzyme. The "glycolytic intermediate" DHAP substrate is incidental.
  -> MODIFY toward the glycerophospholipid biosynthetic process, or REMOVE as a misleading parent.
- GO:0046168 (glycerol-3-phosphate catabolic process): this biosynthetic isozyme (gpsA) produces G3P;
  it does not catabolize it. G3P catabolism is performed by the distinct GlpD/GlpABC respiratory
  G3P dehydrogenases. This InterPro transfer to the family conflates biosynthetic and catabolic roles.
  -> REMOVE (wrong direction for this gene).

## References
- file:PSEPK/gpsA/gpsA-uniprot.txt (UniProt Q88FC9, HAMAP-Rule MF_00394)
- PMID:12534463 — KT2440 genome sequence (source of gene model/locus PP_4169); not enzyme-specific.
