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

## Follow-up: stereochemistry and compartments of the gene products in the GEMs

`uv run python gem_gene_audit.py [CACHE_DIR]` regenerates `gem_gene_audit.md`,
which tallies the stereodescriptor of every 3-hydroxyacyl-CoA participant on
FOX2, PHS1 and ERG10 reactions (read from the metabolite name) and the
compartments of those reactions. FOX2 (MFE-2) and PHS1 both act on
(3R)-3-hydroxyacyl-CoA, which their UniProt catalytic activities state
(RHEA:26526 and RHEA:32711 for FOX2; RHEA:45812 for PHS1).

1. **iMM904 gives FOX2 the wrong stereochemistry throughout.** All 12
   3-hydroxyacyl-CoA participants of the FOX2 hydratase (ECOAH4p-ECOAH11p) and
   dehydrogenase (HACD4p-HACD10p) reactions are (S), and the reactions carry
   the (S)-specific ECs 4.2.1.17 (enoyl-CoA hydratase) and 1.1.1.35
   ((S)-3-hydroxyacyl-CoA dehydrogenase), not EC 4.2.1.119. This is the same
   error as the GO-CAM's FOX2 activities. Because the (S) intermediates are
   produced and consumed only by FOX2 in the peroxisome, the network still
   balances: the error affects annotation and cross-referencing, not flux.
2. **yeast-GEM 9.1.1 is mixed for FOX2.** 28 participants are (R), 6 are (S)
   (the C14, C16 and C26 hydratase and dehydrogenase pairs, e.g. r_2250 with
   r_0057, r_2251 with r_2268, r_2253 with r_2270) and 2 (C18) are unspecified.
   All carry EC 4.2.1.119 / 1.1.1.n12, so for these six the metabolite
   contradicts the reaction's own EC.
3. **yeast-GEM gives PHS1 no (R) intermediate.** Of its seven ER dehydratase
   reactions (EC 4.2.1.134), three use (S) metabolites (r_2168, r_2169, r_2174)
   and four use unspecified ones. EC 4.2.1.134 is the very-long-chain
   (3R)-3-hydroxyacyl-CoA dehydratase.
4. **Both models place an ERG10 reaction in the mitochondrion** (iMM904
   ACACT1m, yeast-GEM r_0104) as well as the cytosol. Experimental evidence
   reviewed for ERG10 places the enzyme in the cytosol: Hiser et al. 1994
   (PMID:7989303) describe ERG10 as encoding the cytoplasmic acetoacetyl-CoA
   thiolase. The same abstract reports that erg10 null extracts have no
   detectable acetoacetyl-CoA thiolase activity, so any mitochondrial
   acetoacetyl-CoA thiolase activity would have to come from Erg10 too.
   Whole-cell extracts cannot settle the location, so the mitochondrial
   reaction is unsupported rather than refuted. Kornblatt and Rudney (1971,
   PMID:5571829, PMID:5571830) separated two thiolase forms, but only their
   titles are cached, so which form is which cannot be checked here.

Point 4 also tempers the POT1 suggestion above: the erg10 null result is from
standard growth conditions, where POT1 (oleate-induced) is expected to be low,
so it neither supports nor rules out POT1 acting on acetoacetyl-CoA.
