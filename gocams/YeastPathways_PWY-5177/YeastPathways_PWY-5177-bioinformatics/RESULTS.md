# GO-CAM YeastPathways_PWY-5177 compared with yeast genome-scale metabolic models

Run `uv run python gem_check.py [CACHE_DIR]` to regenerate `gem_reactions.md`.
The script downloads iMM904 (BiGG) and yeast-GEM (tag v9.1.1) into a cache
outside the repository; the models themselves are not committed.

## Question

The GO-CAM depicts three cytosolic steps (crotonyl-CoA -> (S)-3-hydroxybutanoyl-CoA
-> acetoacetyl-CoA -> 2 acetyl-CoA) enabled by PHS1 or FOX2, FOX2, and ERG10, as part
of glutaryl-CoA degradation. Do the two curated yeast metabolic reconstructions
represent these steps, and with which genes, compartments and directions?

## Findings (from gem_reactions.md)

1. **No glutaryl-CoA degradation in either model.** No reaction in iMM904 or
   yeast-GEM 9.1.1 involves glutaryl-CoA or glutaconyl-CoA (the only "glutaryl"
   metabolite is 3-hydroxy-3-methylglutaryl-CoA of the mevalonate pathway).
2. **ERG10 direction.** iMM904 encodes the Erg10 reactions in the condensation
   direction only (cytosolic ACACT1r and mitochondrial ACACT1m, "forward only":
   2 acetyl-CoA -> acetoacetyl-CoA + CoA). yeast-GEM keeps them reversible
   (r_0103, r_0104). Neither model uses Erg10 for a catabolic route.
3. **The C4 tail of the GO-CAM exists in yeast-GEM, but in the peroxisome.**
   yeast-GEM has FOX2 hydrating trans-but-2-enoyl-CoA (crotonyl-CoA) to
   (R)-3-hydroxybutanoyl-CoA (r_2254), FOX2 oxidising (R)-3-hydroxybutanoyl-CoA to
   acetoacetyl-CoA (r_2271), and POT1, not ERG10, cleaving acetoacetyl-CoA with CoA
   to 2 acetyl-CoA (r_2283), all in compartment [p] as the last turn of
   beta-oxidation. That is the same chemistry as the GO-CAM, with the opposite
   stereochemistry at C3, a different compartment and a different thiolase.
4. **FOX2 is only peroxisomal** in both models (all reactions in [x] in iMM904,
   [p] in yeast-GEM).
5. **PHS1** is absent from iMM904 GPRs. In yeast-GEM its seven reactions are all
   in the ER membrane [erm] (long-chain 3-hydroxyacyl-CoA dehydration of fatty
   acid elongation); it has no C4 reaction.

## Interpretation

Both reconstructions agree with the gene reviews: FOX2 is a peroxisomal
(3R)-specific enzyme, PHS1 is an ER elongation enzyme, and Erg10 runs towards
acetoacetyl-CoA synthesis. yeast-GEM suggests that, if the C4 steps are kept,
the thiolysis of acetoacetyl-CoA in a FOX2-dependent chain belongs to POT1 in the
peroxisome. This is a model-based inference, not experimental evidence that
POT1 performs this C4 step in vivo, and it does not by itself show that Erg10
never cleaves acetoacetyl-CoA.

Limitations: the script matches genes by GPR string and C4 metabolites by name
(yeast-GEM) or BiGG id (iMM904); a reaction annotated with an unexpected
metabolite name would be missed. iMM904 is fetched unversioned from BiGG, so its
sha256 is recorded in the output.
