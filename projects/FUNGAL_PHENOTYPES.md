---
title: "Fungal growth and knockout phenotype resources"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [SCHPO, yeast]
autolink_gene_symbols: false
---

# Fungal growth and knockout phenotype resources

**Bottom line:** we surveyed fungal datasets that record how strains or
mutants grow on defined carbon and nitrogen sources, to see whether they can
serve as evidence in gene reviews. Two kinds exist. Species-level growth
profiles, such as FUNG-GROWTH, say what a fungus can eat but not which gene
does the work. Mutant phenotype data does name genes. For our two largest
fungal gene sets it is already curated and downloadable: 147 of 149 reviewed
*S. pombe* genes and 222 of 224 reviewed *S. cerevisiae* genes have curated
mutant phenotypes, and 64 and 61 of them respectively have a carbon- or
nitrogen-source growth phenotype other than ordinary growth on glucose. Almost
all of those come from two high-throughput screens that GO curators have not
turned into annotations, and most hits are indirect (spindle checkpoint and
respiratory-assembly mutants failing on alternative carbon sources). They are
evidence of necessity, not participation, so they can support or question an
annotation but should not create one.

## Species-level growth: FUNG-GROWTH

[FUNG-GROWTH](https://www.fung-growth.org/) (de Vries et al. 2025,
*Microbiol Resour Announc*, doi:10.1128/mra.00378-25) holds growth profiles
for 398 fungi across the kingdom, most with a public genome, on about 36
substrates: 10 monosaccharides, 5 oligosaccharides, 11 polysaccharides, 7
crude plant biomasses and controls. Growth is scored against glucose and
no-carbon plates. It is meant to sit beside JGI MycoCosm CAZyme annotations.

- The site is an Angular front end on Westerdijk's BioloMICS web service
  (`webservices.bio-aware.com/cbsdatabase`, website id 87). The service
  answers a version request, but we found no documented export or data
  endpoint, so bulk download would need the authors' help.
- Use in reviews: a species that cannot grow on a substrate argues against
  annotating its genes to that substrate's degradation pathway, the same check
  as "pathway absent from organism" in prediction reviews. It cannot support
  an annotation for any single gene.

## Mutant phenotypes for reviewed yeast genes

`scripts/phenotype_overlap.py` (in [FUNGAL_PHENOTYPES/](FUNGAL_PHENOTYPES/))
joins every `genes/SCHPO` and `genes/yeast` review, by the PomBase or SGD
cross-reference in its UniProt record, to the PomBase single-locus haploid
phenotype file (FYPO terms) and SGD's `phenotype_data.tab` (APO terms). Output:
`FUNGAL_PHENOTYPES/data/reviewed_gene_phenotypes.tsv`, one row per reviewed
gene with its phenotype counts, its nutrient phenotypes and their references,
and the review actions on its IMP rows.

| | *S. pombe* (PomBase) | *S. cerevisiae* (SGD) |
|---|---|---|
| Reviews with a database cross-reference | 149 | 224 |
| ...with any curated mutant phenotype | 147 | 222 |
| ...with a non-glucose carbon/nitrogen-source phenotype | 64 | 61 |

A phenotype counts as nutrient utilisation when its label names a carbon or
nitrogen source. Rows about glucose (the standard medium, so a general growth
defect) and "normal growth" rows are excluded.

### Where the nutrient phenotypes come from

| Screen | Organism | Reviewed genes with a hit | Cited in our GOA files |
|---|---|---|---|
| Rodríguez-López et al. 2023, PMID:37787768, deletion library across many conditions | *S. pombe* | 61 | 0 |
| VanderSluis et al. 2014, PMID:24721214, prototrophic deletion collection on 4 carbon × 7 nitrogen sources | *S. cerevisiae* | 50 | 0 |
| Dudley et al. 2005, PMID:16729036, 4,710 mutants under 21 conditions | *S. cerevisiae* | 17 | 0 |
| Malecki et al. 2016, PMID:27887640, and Malecki & Bähler 2016, PMID:27918601, respiratory growth screens | *S. pombe* | 6 and 5 | 0 |

Across PomBase as a whole, Rodríguez-López 2023 supplies 11,403 of these
non-glucose nutrient rows, covering 2,610 genes; in SGD, VanderSluis 2014
supplies 2,553 rows over 1,417 genes.

### What the hits look like

Most are indirect. Spindle checkpoint genes (*bub1*, *mad3*) and autophagy
genes (*atg2*, *atg5*) show altered growth on galactose or on lysine and
proline nitrogen sources; mitochondrial assembly factors (ATP10, ATP11,
COX20, COX23) fail on glycerol and lactate because they are needed for
respiration, not because they act on those carbon sources. Under the
participation rule in `CLAUDE.md`, a knockout growth defect shows that a gene
is necessary, and necessity is not evidence of taking part in the process.
This is the likely reason curators have left the screens out of GO.

Suggested use in reviews:
- Corroborate an existing pathway annotation when the mutant fails on the
  pathway's own substrate.
- Flag a pathway annotation for a second look when the mutant grows normally
  on that substrate.
- Do not propose `NEW` process terms from these phenotypes alone.

## Other fungal knockout datasets

A survey of knockout and transposon fitness datasets in filamentous fungi
and other yeasts, and of which can be downloaded, is in progress. The
bacterial Fitness Browser (Price et al. 2018, PMID:29769716), the closest
model for this kind of data, could not be fetched from our environment
(Cloudflare challenge).

## Reproducing

    uv run python projects/FUNGAL_PHENOTYPES/scripts/phenotype_overlap.py

Downloads are cached in `tmp/fungal_phenotypes/` (gitignored).
