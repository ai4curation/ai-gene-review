# Fbp1 manual deep research

Automated Perplexity deep research was unavailable for this review. This manual
file records the replacement synthesis used for the mouse Fbp1 GO annotation
review.

## Identity and reaction

Mouse Fbp1 encodes fructose-1,6-bisphosphatase 1, a class I FBPase that
catalyzes RHEA:11064 / EC 3.1.3.11, hydrolyzing fructose 1,6-bisphosphate to
fructose 6-phosphate and phosphate in the presence of divalent cations. The
mouse UniProt record describes this reaction directly and records Mg2+ as the
cofactor.

PMID:30150719 purified recombinant and native mouse liver FBP1, engineered an
AMP-insensitive G27P knock-in allele, and showed that AMP-resistant FBP1 blunts
the glucose-lowering action of AMP-mimetic inhibitors and metformin in mice. The
paper supports both the mouse enzyme activity and the placement of Fbp1 at a
rate-controlling gluconeogenic step.

PMID:16497803 expressed human FBPase in mouse liver and showed increased liver
FBPase protein/enzyme activity together with increased glycerol conversion to
glucose. The study supports a hepatic glycerol-gluconeogenesis role for FBPase
abundance in mice, although through a human transgene.

PTHR11556 was already reviewed as the fructose-1,6-bisphosphatase-related
family. Its mouse Fbp1 node, `PANTHER:PTN000168022`, soundly asserts cytoplasm,
fructose 1,6-bisphosphate 1-phosphatase activity, and gluconeogenesis; the
cytosol node `PANTHER:PTN000168034` is also sound.

## GO-CAM context

Mouse Fbp1 is the fructose 1,6-bisphosphatase activity in all four mouse Fbp1
activities in `gocams/index.tsv`. The two gluconeogenesis sibling GO-CAM models
under review are:

- `61e0e55600001225`: `gomodel:61e0e55600001225/61e0e55600002390`
- `62d0afa500000298`: `gomodel:62d0afa500000298/62d0afa500000326`

Both activities are molecular function `GO:0042132`, biological process
`GO:0006094`, cellular component `GO:0005829`, enabled by MGI:MGI:95492. This
is consistent with the mouse gene review.

The other two indexed Fbp1 activities are `62d0afa500000132`, another cytosolic
`GO:0042132` step in `GO:0006094`, and `636d9ce800002041`, whose model title
mentions positive regulation of gluconeogenesis but whose Fbp1 activity is
still typed as `GO:0042132` in `GO:0006094`.

## Propagation assessment

The core FBPase activity, gluconeogenesis participation, F6P metabolic-process
row, cytosol localization, AMP binding, Mg2+/substrate binding, and
homotetramerization are all biologically defensible for mouse Fbp1.

The broad InterPro parents `GO:0016791`, `GO:0042578`, and `GO:0005975` are
true but less informative than the exact FBPase MF and gluconeogenesis/F6P
processes already present.

The human-derived nuclear HIF transcription-factor binding and negative
transcription regulation rows are kept as plausible non-core transfers from the
human FBP1 review, while the normal mouse conservation question remains open.
The human-derived negative cell-growth and Ras rows are cancer-cell contexts,
and the xenobiotic rows are small-molecule inhibitor pharmacology rather than a
cellular response executed by Fbp1. The rat-derived response rows look like
stimulus-expression contexts, but without the RGD seed papers they are left
undecided.
