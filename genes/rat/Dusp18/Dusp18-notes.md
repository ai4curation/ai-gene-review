# Dusp18 (rat, Q6AXW7) review notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene rat Dusp18`; accession Q6AXW7 confirmed (RGD:1306929, GeneID 305477).
  28 GOA rows (the two duplicate nucleus ISS rows were merged by the seeder).
- Only rat experimental paper: Rardin et al. 2008 [PMID:18385140], full text read. Endogenous
  rat kidney DSP18 is a peripheral protein of the mitochondrial inner membrane on the IMS side
  ["DSP18 is a mitochondrial IMS protein, which is peripherally associated with the IM
  predominantly along the cristae"].
- Ortholog enzymology: human [PMID:12591617, PMID:12408986] (abstract only), murine
  [PMID:18385140], human protein substrates Src pY416 [PMID:38346942] and USF1 pT100 [PMID:38992029].
- Checked human (Q8NEJ0) and mouse (Q8VE01) GOA in QuickGO: human nucleus/cytoplasm IDA come from
  PMID:12408986 (N-tagged overexpression); human nucleoplasm is HPA IDA (GO_REF:0000052). Mouse
  cytoplasm/mitochondrion/IMS rows are ISS from rat Q6AXW7 (PMID:18385140), so the rat cytoplasm
  ISS from Q8VE01 is circular (rat -> mouse -> rat). Mouse negative regulation of bone resorption
  is IMP PMID:38346942.
- Ontology checks (OAK): GO:0017017 is_a GO:0008138 and GO:0033549; GO:0008138 is_a GO:0004721 (not
  a child of GO:0004725 or GO:0004722); GO:0035335/GO:0035970 is_a GO:0006470.

Decisions:
- Core MF GO:0008138; GO:0004725 and GO:0004722 accepted (both halves demonstrated on protein
  substrates in orthologs). phosphatase activity -> MODIFY to GO:0008138; dephosphorylation ->
  MODIFY to peptidyl-tyrosine/threonine dephosphorylation.
- MAPK phosphatase (InterPro2GO) marked over-annotated: no MAPK docking motifs, no activity on
  MAPKs in cells, SAPK/JNK absent from mitochondria.
- Nucleus/nucleoplasm marked over-annotated: endogenous protein is mitochondrial; nuclear signal
  from N-tagged overexpression.
- Cytoplasm -> MODIFY to mitochondrial intermembrane space (true as an ancestor, but the specific
  location is known); NEW IDA row for GO:0005758 from PMID:18385140.
- Negative regulation of bone resorption KEEP_AS_NON_CORE (mouse knockout + Src mechanism).
