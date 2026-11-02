# Fer3HCH (CG4349, Q9VYH1) notes

## 2026-10-09 review session (module dmel_ferritin_complex)

- Deep research: Fer3HCH-deep-research-falcon.md.
- Mitochondrial ferritin, testis-enriched; tagged protein targets mitochondria
  [PMID:16571656 "an epitope-tagged version localizes to mitochondria in transfected cells."].
- All ferroxidase-center residues conserved [Fer3HCH-deep-research-falcon.md "It retains all seven residues of the canonical ferritin ferroxidase center"];
  my own sequence check: E35, Y42, E70, H73, E114, Q148 present (human FTH1 E27/Y34/E62/H65/E107/Q141).
- Overexpression harms iron-deficient flies [PMID:16571656 "the viability of iron-deficient flies is compromised by overexpression of mitochondrial ferritin"].
- Per deep research, overexpressed Fer3HCH forms homopolymers but was relatively iron-poor; it protects
  against paraquat and rescues pink1 mitochondrial morphology defects in dopaminergic neurons.

## Decisions
- cytoplasm (IBA) -> MODIFY to mitochondrial matrix (mitochondrial ferritin).
- iron ion transport (IEA) -> MARK_AS_OVER_ANNOTATED (secreted-ferritin property).
- ferroxidase activity accepted (conserved center); no ferritin complex (GO:0070288) proposed, as the
  fly mitochondrial ferritin is not part of the secreted H/L heteropolymer.
