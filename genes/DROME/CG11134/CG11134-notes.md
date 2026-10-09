# CG11134 notes

- 2026-10-09: Initial review of CG11134 (Q9VY93, Swiss-Prot), probable methylthioribulose-1-phosphate
  dehydratase (MtnB subfamily; human APIP, yeast MDE1 orthologs).
- No fly publications in GOA; all annotations IBA/ISS/IEA/IC. Zn2+ cofactor (HAMAP MF_03116).
- metal ion binding -> zinc ion binding (already annotated).
- Module-wide convention (methionine salvage): GO:0033353 "L-methionine cycle" (SAM cycle definition;
  GO's replacement for obsolete GO:0019509) MODIFY -> GO:0071267 L-methionine salvage; cytoplasm ->
  cytosol (IC present); nucleus kept non-core; metal cofactor terms kept non-core.
- Falcon deep research (CG11134-deep-research-falcon.md, arrived after initial commit): no fly
  kinetics, localization or loss-of-function data; activity rests on B. subtilis MtnB and human APIP
  (cytoplasmic). Cautions against multifunctional dehydratase/enolase annotation. No annotation changes.
