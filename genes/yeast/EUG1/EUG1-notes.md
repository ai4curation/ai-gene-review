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
  activity at 2.16% of Pdi1p. Its statement that “only Eps1p and Pdi1p have
  chaperone activity” occurs within an Eps1p-Pdi1p/Eps1p-Mpd1p complex analysis
  and does not establish whether Eug1p has chaperone activity. The Falcon report
  also records later literature proposing possible chaperone-like activity for
  Eug1p. Accordingly, the experimental unfolded-protein-binding annotation is
  left UNDECIDED without the full assay; the matching automated inference is
  also UNDECIDED rather than being treated as a core function.

- The same 2005 abstract says the yeast PDI-family reductive activities were
  reported previously in Kimura et al. 2004, *Biochemical and Biophysical
  Research Communications* 320:359-365. That earlier paper is not cached, so
  reductase-activity annotations are retained by deference to the experimental
  curators without claiming that the 2005 abstract exposes the Eug1p assays.

## Curation decisions

- Retain specific PDI/reductase annotations with explicit weak-activity and
  noninterchangeability caveats. Experimental annotations were not removed when
  the cache lacked full assay details.
- Modify the generic parent “isomerase activity” to the specific PDI term.
- Keep “response to endoplasmic reticulum stress” as non-core: EUG1 is induced
  during ER protein accumulation, but Eug1p is an effector rather than a UPR
  sensor or signaling protein.
- Leave both “unfolded protein binding” annotations UNDECIDED because the full
  direct assay is not cached, while removing both uninformative “protein
  binding” annotations.

## 2026-10-01 current-GOA / IBA review

- Forced a current `just fetch-gene yeast EUG1 --force` refresh. Current GOA
  materializes 20 rows; four older signatures are no longer live and are now
  retained with `retired: true`: the broad `GO:0016853` UniProt keyword row,
  the ARBA and IDA `GO:0051082` unfolded-protein-binding rows, and the stale
  high-throughput `GO:0005515` row from PMID:27107014.
- Rechecked all four PTHR18929 IBA rows against current PAINT. PTN000432607 is
  the PDI-family root and safely transfers ER localization, protein folding,
  response to ER stress, and protein disulfide isomerase activity to Eug1p.
  The ER-stress row remains `KEEP_AS_NON_CORE` because Eug1p is a downstream
  UPR-induced ER folding effector rather than an Ire1/Hac1-like signaler.
- Migrated both `GO:0005515 protein binding` IPI rows from the legacy
  `MARK_AS_OVER_ANNOTATED` action to `REMOVE`. The Eps1 interaction in
  PMID:16002399 is real but does not define a specific Eug1p molecular
  function, and the PMID:27107014 interaction row is no longer in current GOA.
- A 2024-2026 PubMed/Web search found no new direct EUG1/YDR518W paper that
  resolves the native client spectrum, the unresolved unfolded-protein-binding
  assays, or the exact physiological balance between Eug1p redox catalysis and
  noncatalytic chaperone-like assistance.

## Research-file provenance

The Falcon report was regenerated during this review and its citation list
changed from 32 entries to 23. The newer synthesis retains the central
Nørgaard/Xiao/Laboissière evidence and records Hacioglu et al.'s possible
chaperone-like interpretation, but it does not retain every source or assay
claim from the prior generated report. Curation decisions therefore rely on
the directly cached publications where available and explicitly mark the
remaining full-text-dependent questions UNDECIDED.

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
