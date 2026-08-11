# EUG1 review notes

## Identity and scope

EUG1 is *S. cerevisiae* YDR518W / UniProt P32474, a soluble ER PDI-family
protein with two CXXS active-site motifs. The review distinguishes native Eug1p
from engineered CXXC variants and does not infer function from those mutants.

## Primary evidence

- PMID:1406650 (cached abstract only) directly describes Eug1p as a soluble ER
  protein: “The product of the EUG1 gene of Saccharomyces cerevisiae is a soluble
  endoplasmic reticulum protein”. EUG1 levels increase when native or
  unglycosylated proteins accumulate in the ER. Overexpression permits growth
  without PDI1, but only partially relieves the ER-form CPY phenotype. This
  supports an auxiliary ER folding role and UPR-responsive expression, not
  equivalence to Pdi1p.

- PMID:11485577 (cached abstract only) is the key biochemical qualification:
  “The wild-type protein showed very little activity, not only in oxidative
  refolding but also in assays where only isomerase activity was required.”
  CXXC-engineered variants approached genuine PDI activity. The authors conclude
  that general disulfide isomerization is not Eug1p's main in-vivo function.

- PMID:11157982 (cached abstract only) shows that the yeast PDI homologues are
  not functionally interchangeable. EUG1 suppression of pdi1 deletion requires
  endogenous homologues with CXXC motifs, and PDI-family mutant combinations
  impair CPY folding. This supports a cooperative redox-folding network rather
  than autonomous bulk Pdi1-like activity.

- PMID:16002399 (cached abstract only) reports Eug1p oxidative-refolding
  activity at 2.16% of Pdi1p. Its chaperone statement is specifically “although
  only Eps1p and Pdi1p have chaperone activity.” Therefore the prior review's
  claim of measurable Eug1p chaperone-like activity was removed, and generic
  unfolded-protein binding remains marked over-annotated rather than treated as
  Eug1p's core function.

## Curation decisions

- Retain specific PDI/reductase annotations with explicit weak-activity and
  noninterchangeability caveats. Experimental annotations were not removed when
  the cache lacked full assay details.
- Modify the generic parent “isomerase activity” to the specific PDI term.
- Keep “response to endoplasmic reticulum stress” as non-core: EUG1 is induced
  during ER protein accumulation, but Eug1p is an effector rather than a UPR
  sensor or signaling protein.
- Mark generic “unfolded protein binding” and “protein binding” over-annotated;
  more specific redox-folding terms describe the demonstrated biology.

## Open question

The decisive unresolved issue is native substrate specificity: which ER clients
selectively require Eug1p, and whether its CXXS domains mainly rearrange unusual
disulfides or support a distinct noncatalytic step.

## OpenScientist hypothesis research attempt

On 2026-08-11, the public `just gene-hypothesis-research` wrapper was used to
test the hypothesis that native Eug1p primarily supports specialized ER-client
folding/disulfide rearrangement rather than bulk Pdi1-like oxidation or
isomerization. OpenScientist job
`3d55e061-efef-44c7-8f37-428098e5fda6` reached the configured 7,200-second
provider timeout and was cancelled with no research or citation artifact. No
claim in this review depends on that failed run; the conclusions above remain
grounded in the directly cached literature.
