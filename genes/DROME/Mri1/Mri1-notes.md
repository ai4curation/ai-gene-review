# Mri1 notes

- 2026-10-09: Initial review of Mri1 (Q9V9X4, Swiss-Prot), methylthioribose-1-phosphate isomerase.
- No fly publications in GOA; all annotations IBA/ISS/IEA/IC. UniProt (HAMAP MF_03119): "Catalyzes the
  interconversion of methylthioribose-1-phosphate (MTR-1-P) into methylthioribulose-1-phosphate
  (MTRu-1-P)."
- Module-wide convention (methionine salvage): GO:0033353 "L-methionine cycle" (SAM cycle definition;
  GO's replacement for obsolete GO:0019509) MODIFY -> GO:0071267 L-methionine salvage; cytoplasm ->
  cytosol (IC present); nucleus kept non-core; metal cofactor terms kept non-core.
- Falcon deep research (Mri1-deep-research-falcon.md, arrived after initial commit): confirms no fly
  enzymology or mutant phenotype; activity rests on yeast/bacterial orthologs (yeast mri1 deletion
  impairs MTA-supported growth). Notes a 2026 report that Mri1 becomes sarkosyl-insoluble in fly heads
  after Funes overexpression (not a direct effect in vitro). eIF2B-like fold does not imply translation
  function. No annotation changes.
