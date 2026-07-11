# NAGLU (P54802) review notes

## Summary
NAGLU = alpha-N-acetylglucosaminidase, a lysosomal exoglycosidase of glycoside hydrolase
family 89 (CAZy GH89). It catalyses hydrolysis of terminal non-reducing
alpha-N-acetyl-D-glucosamine residues in N-acetyl-alpha-D-glucosaminides (EC 3.2.1.50),
a step in the stepwise exolytic lysosomal degradation of heparan sulfate. Deficiency
causes mucopolysaccharidosis type IIIB (MPS IIIB / Sanfilippo syndrome B), a lysosomal
storage disorder with severe CNS degeneration. A dominant NAGLU variant (I403T) also
causes axonal Charcot-Marie-Tooth disease type 2V (CMT2V).

## Key evidence
- UniProt P54802 FUNCTION: "Involved in the degradation of heparan sulfate."
  [file:human/NAGLU/NAGLU-uniprot.txt]
- CATALYTIC ACTIVITY: "Hydrolysis of terminal non-reducing N-acetyl-D-glucosamine
  residues in N-acetyl-alpha-D-glucosaminides.; EC=3.2.1.50"
  [file:human/NAGLU/NAGLU-uniprot.txt]
- SUBCELLULAR LOCATION: Lysosome. SIMILARITY: glycosyl hydrolase 89 family.
  [file:human/NAGLU/NAGLU-uniprot.txt]
- PMID:8650226 (Zhao et al. 1996) — cloned NAGLU cDNA/gene; "Sanfilippo syndrome type B
  is a lysosomal storage disorder caused by deficiency of alpha-N-acetylglucosaminidase".
  This is the ProtInc/PINC TAS source for the MF, lysosome, and nervous-system-development
  annotations. Abstract-only in cache; full text read by curator.
- Reactome R-HSA-1678742 "NAGLU hydrolyses Heparan sulfate chain(4)": NAGLU "hydrolyses
  the non-reducing, terminal N-acetyl-D-glucosamine residue from heparan sulfate".
- Reactome R-HSA-2024096 "HS-GAG degradation": lysosomal degradation of heparan
  sulfate/heparin; parent pathway for GO:0030200 annotation.

## GO term choices
- Core MF: GO:0004561 alpha-N-acetylglucosaminidase activity (exact GOA term; def matches
  UniProt catalytic activity and EC 3.2.1.50). CONFIRMED current label via OLS.
- Core BP: GO:0030200 heparan sulfate proteoglycan catabolic process (present in GOA as
  Reactome TAS; def = breakdown of heparan sulfate proteoglycans). CONFIRMED current label.
- Core location: GO:0043202 lysosomal lumen and GO:0005764 lysosome (both in GOA).

## Annotation dispositions
- MF alpha-N-acetylglucosaminidase (GO:0004561) across IBA/IEA-EC/Reactome-TAS/ProtInc-TAS:
  ACCEPT — core catalytic function, strongly supported.
- Lysosome (GO:0005764) / lysosomal lumen (GO:0043202): ACCEPT — core location.
- GO:0030200 HS proteoglycan catabolic process (Reactome TAS): ACCEPT — core BP.
- GO:0030202 heparin proteoglycan metabolic process (IBA): heparin is a highly sulfated HS
  variant; NAGLU acts on both. MODIFY to HS catabolic process (GO:0030200) as the more
  accurate primary process; keep as valid but not the best label.
- GO:0005773 vacuole (IBA): ACCEPT — the yeast/broad-lineage generalization of lysosome
  used by GO_Central for the family; correct but less specific than lysosome.
- GO:0070062 extracellular exosome (HDA/IDA, x3): KEEP_AS_NON_CORE — bulk proteomics
  detection in urinary/prostatic exosomes; secretion is real but peripheral to lysosomal
  function.
- GO:0007399 nervous system development (ProtInc TAS, PMID:8650226): MARK_AS_OVER_ANNOTATED
  — the CNS phenotype is a downstream consequence of HS storage, not a direct developmental
  role of the enzyme.
- GO:0048731 system development (ARBA IEA): MARK_AS_OVER_ANNOTATED — very general ML-derived
  term, same disease-phenotype conflation, not informative.
- GO:1901135 carbohydrate derivative metabolic process (ARBA IEA): MODIFY — correct but
  extremely general; HS catabolic process is the specific term.
