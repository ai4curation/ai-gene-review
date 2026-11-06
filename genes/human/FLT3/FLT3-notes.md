# FLT3 (P36888) — curation notes

Deep-research providers are unavailable in this environment; research is from the cached
publications, the UniProt record and PubMed.

## Protein and localization

Class III receptor tyrosine kinase, related to KIT and CSF1R, with five extracellular
immunoglobulin-like domains, one transmembrane helix and a split intracellular kinase
domain.
[file:human/FLT3/FLT3-uniprot.txt "SUBCELLULAR LOCATION: Membrane; Single-pass type I membrane protein. Endoplasmic reticulum lumen."]
[file:human/FLT3/FLT3-uniprot.txt "Constitutively activated mutant forms with internal tandem duplications are less efficiently transported to the cell surface and a significant proportion is retained in an immature form in the endoplasmic reticulum lumen."]

Localization conclusion: **plasma membrane, ligand-binding ectodomain exposed at the cell
surface** (64 rows accepted). The ER-lumen row is kept as non-core — it describes
immature and ITD-mutant receptor — and the endosome-membrane row reflects internalisation
before degradation.

## Function

[file:human/FLT3/FLT3-uniprot.txt "Tyrosine-protein kinase that acts as a cell-surface receptor for the cytokine FLT3LG and regulates differentiation, proliferation and survival of hematopoietic progenitor cells and of dendritic cells."]
[file:human/FLT3/FLT3-uniprot.txt "FLT3LG binding leads to dimerization and activation by autophosphorylation."]
[PMID:7507245 "STK-1, the human homolog of Flk-2/Flt-3, is selectively expressed in CD34+ human bone marrow cells and is involved in the proliferation of early progenitor/stem cells."]

## Notable review decisions

- `GO:0005021 vascular endothelial growth factor receptor activity` (TAS, PMID:8394751,
  PINC) was REMOVEd with a `source_defects` entry, and the derived
  `GO:0038084 VEGF signaling pathway` (GO_REF:0000108) with it. The cited paper places
  FLT3 with CSF1R and KIT, not with the VEGF receptors; the FLT name prefix is the likely
  source of the error.
  [PMID:8394751 "presenting a strong similarity with the corresponding mouse FLT3/FLK2 protein as well as with the receptors for colony-stimulating factor 1 (CSF1R/FMS) and steel locus factor (SLFR/KIT)"]
- `GO:0035259 obsolete nuclear glucocorticoid receptor binding` was removed: an obsolete
  term, transferred from the mouse ortholog, asserting a nuclear-receptor interaction for
  a membrane kinase.
- Of 13 bare protein-binding rows, those with kinase partners (SYK ×2, ABL1, ABL2, LCK,
  FYN) were modified to protein kinase binding and the PIK3R1 row to
  phosphatidylinositol 3-kinase binding; adapters (GRB10, SLAP2, CRK, CRKL), RASA1 and the
  NEMO microarray hit were removed.
- `protein kinase activity`, `protein tyrosine kinase activity` (4 rows),
  `transmembrane signaling receptor activity`, `cell surface receptor signaling pathway`,
  `protein-containing complex` and `cellular response to cytokine stimulus` (2 rows) were
  marked TOO_GENERAL beside the specific terms retained.
- STAT5 phosphorylation was kept as non-core because UniProt notes wild-type FLT3 only
  marginally activates STAT5.
