# GO-CAM YeastPathways_YEAST-FAO-PWY compared with yeast genome-scale metabolic models

Run `uv run python gem_compartments.py [CACHE_DIR]` to regenerate
`gem_compartments.md`. The script downloads iMM904 (BiGG) and yeast-GEM (tag
v9.1.1) into a cache outside the repository; the models are not committed. It
uses the same model sources as the YeastPathways_PWY-5177 comparison.

## Question

The GO-CAM places all eleven fatty acid oxidation activities in the cytosol
and gives DCI1 the delta3-delta2-enoyl-CoA isomerase step alongside ECI1. Where
do the two curated yeast reconstructions put these gene products, and which
gene do they give the isomerase steps?

## Findings (from gem_compartments.md)

1. **The beta-oxidation core is peroxisomal in both models.** Every POX1,
   ECI1, DCI1, FOX2 and POT1 reaction is in the peroxisome (iMM904 [x],
   yeast-GEM [p]). Neither model has a cytosolic reaction for these genes.
2. **The activators differ by gene, as the gene reviews say.** In yeast-GEM,
   FAA2 is mostly peroxisomal (9 of 10 reactions), FAA1 and FAA4 are mostly in
   ER membrane and lipid particle, FAA3 mostly in the cell envelope, and FAT1
   spans transport (cytosol/extracellular), ER, lipid particle and
   peroxisome. iMM904 has no membrane compartments for these and puts FAA1, FAA3
   and FAA4 in the cytosol and FAA2 in the peroxisome.
3. **DCI1 is treated differently by the two models.** yeast-GEM gives DCI1 only
   delta(3,5)-delta(2,4)-dienoyl-CoA isomerase reactions (r_2301, r_2302) and
   ECI1 alone the EC 5.3.3.8 delta3-delta2 isomerase reactions (r_2295-r_2300),
   matching the DCI1 and ECI1 reviews. iMM904 has no separate isomerase
   reactions: in every lumped fatty acid oxidation reaction (FAO141p_even etc.)
   DCI1 appears as an OR-alternative to ECI1, the same substitution the GO-CAM
   makes.
4. **FOX2 EC numbers** are EC 4.2.1.119 / 1.1.1.n12 ((3R)-specific) in yeast-GEM
   and the (S)-specific EC 4.2.1.17 / 1.1.1.35 in iMM904, as found for
   YeastPathways_PWY-5177.

## Interpretation

yeast-GEM 9.1.1 agrees with the gene reviews on every point the GO-CAM gets
wrong: peroxisomal location of the oxidation core, membrane locations of the
Faa1/Faa4 activators, DCI1 as the dienoyl-CoA isomerase, and (3R) FOX2
chemistry. iMM904 shares the GO-CAM's DCI1 and FOX2 errors, which suggests a
common origin in pathway-database reaction assignments.

Limitations: genes are matched by locus in the GPR string, and compartments are
those of a reaction's metabolites; a transport reaction therefore spans two
compartments. EC numbers are as annotated in each model.
