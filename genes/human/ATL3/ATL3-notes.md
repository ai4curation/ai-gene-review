# ATL3 notes

## Review summary

ATL3 is best supported as an ER membrane atlastin GTPase whose core role is
GTP-dependent homotypic ER membrane fusion and maintenance of the branched tubular
ER network. The strongest ATL3-specific source is Bryce et al. 2023, which reports
that "purified human ATL3 catalyzes efficient membrane fusion in vitro and is
sufficient to sustain the ER network in triple knockout cells" [PMID:37102997].
Earlier ER-shaping work supports the shared atlastin role: "ATL is needed to not
only form, but also maintain, the ER network" [PMID:27619977]. Disease genetics
also points to ER morphology, with ATL3 enriched at ER branch points and the
p.Tyr192Cys variant disrupting tubular ER structure [PMID:24459106
"ATL3 proteins are enriched in three-way junctions, branch points of the
endoplasmic reticulum that connect membranous tubules to a continuous network"].

## PN proteostasis projection

The local Proteostasis Network projection reports an ATL3 candidate addition to
GO:0061709 reticulophagy from the PN path
`Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy`
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv
"ATL3 ... GO:0061709 reticulophagy ... new_to_goa"]. I reviewed this conservatively.
The seeded GOA and accessible primary sources support ER membrane fusion and ER
tubular network organization, not a direct GO reticulophagy annotation.

Bryce et al. 2023 explicitly frames the autophagy literature as unsettled context
rather than the main demonstrated activity: ATL3 "has been identified as a possible
ER-autophagy receptor that interacts with GABARAP proteins" and the authors add
that "Some of these diverse roles could stem from a primary role for ATL3 in ER
structural maintenance, but they could also indicate one or more ATL3 functions
outside of membrane fusion" [PMID:37102997]. Therefore I did not add reticulophagy
as a proposed GO annotation. I recorded the issue as a suggested expert question
and experiment to separate a possible direct receptor role from indirect effects
of altered ER morphology.

## Annotation decisions

- Accepted the ER membrane, ER tubular network membrane, ER membrane fusion,
  ER network organization, GTP binding, GTPase activity, and
  GTPase-dependent fusogenic activity annotations.
- Kept `protein homooligomerization` as non-core because dimerization is a
  mechanistic step in fusion, not ATL3's standalone biological role.
- Marked generic `protein binding` annotations as over-annotated. The ZFYVE27 and
  REEP5 interactions support ER-shaping network context, but they do not define
  ATL3's molecular function.
- Marked generic high-throughput `membrane` as over-annotated because more
  informative ER membrane annotations exist.
- Accepted the NOT annotation to ER-to-Golgi vesicle-mediated transport because
  Rismanchi et al. report that VSVG-GFP trafficking was essentially normal after
  atlastin perturbation [PMID:18270207 "secretory pathway trafficking as assessed
  using vesicular stomatitis virus G protein fused to green fluorescent protein
  (VSVG-GFP) as a reporter was essentially normal"].
