# WHI3 (YNL197C, P34761) review notes

## Provenance

Deep research (`just deep-research`) was unavailable in this container (no API keys), so no
`-deep-research-*.md` file exists. Literature was read directly: cached publications in
`publications/`, PubMed searches (all 15 PubMed records with "Whi3" in the title were checked),
and the PMC HTML full text of the three CACAO-cited papers (PMID:21149646, PMID:23770701,
PMID:18667435), which are abstract-only in the cache. The PMC full text was read for this
review but is not cached, so quotes in the review YAML come only from the cached abstracts.
The GONUTS wiki (gowiki.tamu.edu) pages for PMID:21149646, PMID:23770701 and PMID:18667435
were tried on 2026-10-29. Each returned only a maintenance notice ("temporarily offline while
we perform upgrades"), so the students' evidence notes could not be seen.

## Identity

- Whi3 is a 661-aa protein with a C-terminal RRM (538-625) and N-terminal Q/N-rich,
  low-complexity regions (UniProt P34761). It is partially redundant with its paralogue Whi4.
- Size-control gene: "The whi3 mutant has small cells, while extra doses of WHI3 produce large
  cells, and a large excess of WHI3 produces a lethal arrest in G1 phase. WHI3 seems to be a
  dose-dependent inhibitor of Start." [PMID:11290704]

## Molecular function: sequence-specific mRNA binding

- "Whi3 contains an RNA-recognition motif that specifically binds the CLN3 mRNA ... and
  localizes the CLN3 mRNA into discrete cytoplasmic foci" [PMID:11691832].
- RIP-chip finds hundreds of targets, enriched for membrane/exocytic and cell wall proteins;
  "Whi3-associated mRNAs are enriched in clusters of the tetranucleotide GCAU, and mutation of
  the GCAU clusters in the CLN3 mRNA caused a reduction in its association to Whi3"
  [PMID:18667435]. Cai & Futcher repeated the RIP-chip (111 targets) [PMID:24386402].

## Mechanism on targets

- mRNA destabilization: "the whi3 mutation causes a small but consistent increase in the
  abundance of hundreds of mRNAs, including the CLN3 mRNA"; CLN3 mRNA half-life increases in
  whi3 (GAL shut-off, Fig. 6); whi3 also "causes a small increase in the translational
  efficiency of CLN3 mRNA" (ribosome profiling). Proposed recruitment of Ccr4-Not
  [PMID:24386402].
- Holmes et al.: "Deletion of Whi3 resulted in an increase in the relative abundance of Whi3
  target RNAs" (abundance only, no decay measurement) [PMID:24386330].
- Translational inhibition of CLN3: the super-assembly "liberates the G1 cyclin Cln3 from
  translational inhibition" [PMID:24315096].
- Cytoplasmic retention of Cln3-Cdc28: Whi3 binds Cdc28 through its N-terminus; "Whi3
  constitutes a cytoplasmic retention device for Cln3-Cdc28 complexes" [PMID:14685274].
- Positive post-transcriptional effects (Yak1, Cln1/2, Tpk1, Tec1, Nip100 protein down, mRNA
  unchanged, in whi3 cells) [PMID:21149646, PMID:23770701]. YAK1 mRNA is not a known Whi3
  target, and Malcher et al. say the effect may be indirect (PMC full text, Discussion).
- PKA phosphorylates Whi3 Ser568, lowering its binding to CLN3 mRNA and promoting G1/S
  [PMID:23471970]; Whi3 antagonises restart from Hog1-dependent G1 delay [PMID:24096659].

## Localization

- Cytoplasm, diffuse in unstressed cells [PMID:11691832, PMID:24386402].
- ER association: Colomina et al. [PMID:18667435]; Whi3 mnemon super-assemblies sit on
  Sec61-marked ER membranes (72.5%), and Whi3-TAP partly co-fractionates with Dpm1-positive
  microsomes [PMID:35085498].
- Stress granules (Pub1 co-localization, heat shock / glucose deprivation; sedimentation
  assay) [PMID:24386330]; P-bodies/stress granules [PMID:24386402]; SG proteome
  [PMID:26777405, HDA, Whi3 not named in cached text].

## Cellular memory and ageing

- Deceptive courtship: Whi3 polyQ/polyN-driven super-assembly (mnemon) inactivates Whi3 and
  frees CLN3 translation; it stays in the mother [PMID:24315096]. Confined to the mother by ER
  diffusion barriers [PMID:35085498]. Age-dependent Whi3 aggregation causes the pheromone
  insensitivity of old cells [PMID:28302853]. P-body/Whi3 condensate network
  [PMID:41043393].

## Development and other phenotypes

- Filamentous / pseudohyphal growth: dfg screen [PMID:9055077]; Whi3 N-terminus needed for
  filamentous growth [PMID:14685274]; apical growth [PMID:19440046].
- FLO11-dependent agar adhesion lost in whi3 (Fig. 1B), FLO11 mRNA down 7-fold, PFLO11-lacZ
  down 6-fold; YAK1 high-copy suppresses [PMID:21149646, PMC full text].
- whi3 smaller cells by Coulter counter (Fig. 1A); hypersensitive to geneticin, hygromycin B
  and slightly to cycloheximide (Fig. 3), read by the authors as "suggesting that Whi3 might
  positively affect" translational elongation; increase-in-ploidy phenotype [PMID:23770701,
  PMC full text].
- Cell wall: whi3 and whi3-dRRM are Congo red/Calcofluor-sensitive, show sorbitol-remediable
  37 C growth delay, higher phospho-Slt2, and are synthetic lethal with slt2 (Fig. 4)
  [PMID:18667435, PMC full text].

## CACAO rows (6)

| Term | PMID | What paper shows | Verdict |
|---|---|---|---|
| GO:0010811 pos. reg. cell-substrate adhesion | 21149646 | whi3 loses agar adhesion (Fig 1B) | KEEP_AS_NON_CORE (indirect, via Yak1/Tec1/FLO11) |
| GO:0045893 pos. reg. DNA-templated transcription | 21149646 | FLO11 mRNA and PFLO11-lacZ down in whi3 | MARK_AS_OVER_ANNOTATED: phenotype as process; Whi3 is a cytoplasmic RBP |
| GO:0045727 pos. reg. translation | 21149646 | Yak1 protein down, mRNA unchanged (Fig 3) | MARK_AS_OVER_ANNOTATED: post-transcriptional, translation not shown, possibly indirect |
| GO:0045793 pos. reg. cell size | 23770701 | whi3 cells smaller (Fig 1A) | ACCEPT |
| GO:0045901 pos. reg. translational elongation | 23770701 | drug hypersensitivity only (Fig 3) | MARK_AS_OVER_ANNOTATED: phenotype read as process |
| GO:0071554 cell wall organization or biogenesis | 18667435 | CR/CFW sensitivity, Slt2 activation (Fig 4) | KEEP_AS_NON_CORE |
