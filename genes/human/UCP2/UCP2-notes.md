# UCP2 (SLC25A8, P55851) — review notes

Deep research: falcon timed out (all providers failed). Review grounded in UniProt, GOA, cached papers.

## Function
- C4-dicarboxylate (malate, oxaloacetate, aspartate)/phosphate+H+ antiporter of the inner mitochondrial
  membrane [PMID:24395786 "UCP2 reconstituted in lipid vesicles catalyzed the exchange of malate, oxaloacetate, and aspartate for phosphate plus a proton from opposite sides of the membrane."; "by exporting C4 compounds out of mitochondria, UCP2 limits the oxidation of acetyl-CoA-producing substrates such as glucose and enhances glutaminolysis, preventing the mitochondrial accumulation of C4 metabolites derived from glutamine."].
  Core MF chosen: dicarboxylate:phosphate antiporter activity (GO:0015364), via MODIFY of antiporter activity.
- Fatty-acid-activated proton conductance and chloride transport in reconstitution
  [PMID:26182433 "transported protons in the presence of physiologically-relevant fatty acid (FA) activators."]; physiological uncoupling is debated.
- Does not mediate adaptive thermogenesis (UniProt) -> UCP1-derived IBA thermogenesis/uncoupler terms MARK_AS_OVER_ANNOTATED
  (PANTHER nodes PTN001183920, PTN000642156 grounded in Ucp1 MGI:98894 / RGD:3931).

## Disease (dismech: Hyperinsulinemic_Hypoglycemia, relationship_type DISPUTED)
- [PMID:19065272 "UCP2 knockout mice exhibit an hyperinsulinemic"]; impaired-function variants in two children with CHI
  [PMID:19065272 "Functional assays in yeast and in insulin-secreting cells revealed an impaired activity of"] — variants were parentally inherited;
  causality regarded as unresolved.
- Alignment note: dismech describes UCP2's normal role as "leaks protons across the inner mitochondrial membrane";
  current biochemical evidence favours C4-metabolite export as the principal activity. Both limit glucose-driven ATP
  generation, so the disease logic is unchanged, but the dismech wording is the older model.
- MICU1/Ca2+ uptake annotation (PMID:27642082) left UNDECIDED: abstract suggests UCP2/3 restore, not inhibit, uptake.
