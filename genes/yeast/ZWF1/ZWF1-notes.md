# ZWF1 notes (P11412, YNL241C, MET19)

- G6PD EC 1.1.1.49 [UniProt:P11412 "Reaction=D-glucose 6-phosphate + NADP(+) = 6-phospho-D-glucono-1,5-"]; oxidative PPP step 1/3.
- MET19 = G6PD; null requires organic sulfur [PMID:2001672 "The only phenotype of such a strain is an absolute requirement for an organic sulfur source, i.e. methionine, S-adenosylmethionine (AdoMet), cysteine, glutathione or homocysteine."]; AdoMet represses ZWF1 [PMID:2001672 "results reported here show that an increase of the AdoMet pool represses the transcription of the glucose-6-phosphate dehydrogenase gene"].
- NADPH source, oxidant sensitivity [PMID:2269430 "This suggests that G6PD has a major role in NADPH production in yeast."]; decreased cytosolic NADPH/NADP+ [UniProt:P11412 "Decreases the cytosolic NADPH/NADP(+) ratio; this"].
- zwf1 suppresses gnd1 glucose-negative phenotype [PMID:7045591 "Suppression of this mutant for growth on glucose takes place by the loss of glucose 6-phosphate dehydrogenase."].
- H2O2: pos allelic to ZWF1 [PMID:7586028]; adaptation defect beyond GR [PMID:9480895 "In S. cerevisiae, G6PDH appears to play other important roles in the adaptive response to H2O2 stress besides supplying NADPH to the GR reaction."].

Decisions: ACCEPT activity (all), oxidative PPP, PPP, NADPH regeneration, cytoplasm/cytosol; KEEP_AS_NON_CORE glucose metabolic process, response to H2O2, NADP binding; MODIFY GO:0016614 -> GO:0004345.

## Autophagy (SGD description follow-up, 2026-11-01)

SGD calls Zwf1 a "negative regulator of nonselective autophagy, independent of Stb5p". The
source is Delorme-Axford et al. 2023, where zwf1 deletion modestly raised Pho8delta60 activity
under starvation [PMID:37345792 "In the zwf1 ∆ strain, we found that Pho8∆60-dependent phosphatase
activity was enhanced (>15%) relative to WT under starvation conditions, suggesting that Zwf1
functions as a negative modulator of autophagy"]. The authors explain the effect through lower
NADPH pools, so it is an indirect metabolic effect of G6PD loss. It is recorded as peripheral and
not annotated.
