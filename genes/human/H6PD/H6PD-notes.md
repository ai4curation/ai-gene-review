# H6PD (human, O95479) review notes

## Summary of verified biology

H6PD is the endoplasmic-reticulum lumen paralog of cytosolic G6PD. It is a bifunctional
enzyme with an N-terminal hexose-6-phosphate dehydrogenase domain and a C-terminal
6-phosphogluconolactonase domain.

- UniProt FUNCTION places H6PD in the ER lumen and describes the first two oxidative
  pentose-phosphate-branch reactions: G6P + NADP+ -> 6PGL + NADPH, then 6PGL -> 6PG.
- PMID:18628520 assayed wild-type and apparent cortisone reductase deficiency H6PD
  mutants in HEK293 microsomes, measuring NADPH generation from G6P plus NADP+. Four
  disease variants had no detectable H6PDH activity above background.
- PMID:12858176 originally tied H6PD to ER-lumenal NADPH regeneration and reported that
  CRD-associated H6PD exon 5 mutations attenuated or abolished H6PDH activity in
  cell-lysate assays with surrogate galactose 6-phosphate; PMID:18628520 later
  re-tested R453Q and reported no detectable H6PDH catalytic defect for that variant.
- PMID:23132696 identified further H6PD alleles in two girls with apparent cortisone
  reductase deficiency and confirmed loss of H6PDH activity in mutant expression
  studies.
- H6PD supplies ER-lumenal NADPH to HSD11B1, allowing 11beta-HSD1 to run as an
  oxoreductase that converts cortisone to cortisol. Human H6PD loss therefore causes
  apparent cortisone reductase deficiency through cofactor deprivation rather than by
  directly converting a steroid.
- H6PD has broad dehydrogenase specificity, including free-glucose and other
  sugar-phosphate reactions inherited from mouse H6pd or characterized on human H6PD
  in UniProt/RHEA rows. These are kept as non-core or removed when GOA projects them
  to overly generic EC-bucket activities, rather than made core functions.

## PANTHER PTHR23429

Human H6PD is `PANTHER:PTHR23429:SF7`. The family review already separated the H6PD
ER-lumenal clade from the cytosolic G6PD branch:

- `PTN000604427` is the root IBD for `GO:0004345`, `GO:0006006`, and `GO:0009051`.
  H6PD receives those rows; O95479 is one of the direct PAINT seeds.
- `PTN001159891` is the H6PD-clade IBD for `GO:0005783` endoplasmic reticulum and
  the paired IRD that stops the inherited cytosol assertion on the H6PD lineage.
- No PAINT row covers H6PD's 6-phosphogluconolactonase domain, so that activity is
  handled only in the gene review from UniProt/mouse orthology evidence.

## Cortisol-Cortisone Shuttle

`modules/cortisol_cortisone_shuttle.yaml` already modeled HSD11B1 and HSD11B2 as
the cortisone-to-cortisol and cortisol-to-cortisone steps. H6PD is a real third
component of the HSD11B1 directionality module because it produces ER-lumenal NADPH;
the module now has an H6PD NADPH-supply part feeding HSD11B1.

## Deep Research

No provider-generated H6PD deep-research file was available in this checkout. The
review was grounded in the fetched GOA/UniProt records, the PTHR23429 PAINT table,
the existing G6PD family review, the cortisol-cortisone shuttle module, and the two
GOA-cited full-text H6PD papers cached as PMID:18628520 and PMID:23132696, plus the
UniProt-cited human H6PD enzymology paper PMID:12858176.
