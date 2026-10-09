# Adi1 notes

- 2026-10-09: Initial review of Adi1 (Q6AWN0, Swiss-Prot; DADI1, CG32068), acireductone dioxygenase.
- Chou et al. 2014 [PMID:25037729] (full text): "We found that the enzymatic activity of ADI1 is required
  for normal egg production, and human ADI1 is functionally exchangeable for this effect."; "The
  fecundity defect in Dadi1 mutants was rescued by adding methionine under dietary restriction.";
  hADI1-E94A (inactive) did not rescue.
- Positive regulation of reproductive process (CACAO IMP) marked over-annotated: methionine fully
  rescues, so Adi1 is a metabolic supplier, not a regulator.
- Ni-ARD activity / nickel binding kept non-core (off-pathway); iron ion binding -> ferrous iron binding.
- Plasma membrane ISS (from human ADI1/MTCBP-1 MT1-MMP binding) marked over-annotated.
- Module-wide convention (methionine salvage): GO:0033353 "L-methionine cycle" (SAM-cycle definition;
  GO's replacement for obsolete GO:0019509) MODIFY -> GO:0071267 L-methionine salvage (Adi1 already has
  the IMP); cytoplasm -> cytosol (IC present); nucleus kept non-core.
- Falcon deep research (Adi1-deep-research-falcon.md, arrived after initial commit): restates Chou et
  al. 2014 findings (about 20-30% fewer eggs under restriction; 64% lower ovarian methionine and reduced
  SAM in mutants; human ADI1 but not the E94A mutant rescues) and the metal-dependent Fe/Ni reaction
  split. Subcellular location of fly Adi1 untested. No annotation changes.
