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
annotation but should not create one. Beyond the two model yeasts, the only
fungal genome-wide fitness data across many carbon sources is RB-TDNAseq in
the basidiomycete yeast *Rhodotorula toruloides* (downloadable; 6,409 genes with
data); our analysis of it is in [FUNGAL_PHENOTYPES/RHOTO.md](FUNGAL_PHENOTYPES/RHOTO.md).
No filamentous-fungus knockout collection has been screened across carbon or
plant-biomass sources; there, carbon phenotypes survive only as hit lists and
figures in individual papers.

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

## Other fungal knockout and fitness datasets

We checked whether each dataset's phenotype table can actually be
downloaded. PMIDs were verified in PubMed. "Yes" means a test download
succeeded and the file opened. Conditions are summarised with carbon and
nitrogen sources flagged.

### Genome-wide fitness with many carbon sources

| Dataset | Organism | Mutants × conditions | Carbon / nitrogen sources | Download |
|---|---|---|---|---|
| Kim et al. 2021, PMID:33585414 (RB-TDNAseq; includes Coradetti 2018 data) | *Rhodotorula toruloides* | 6,409 genes with data × 27 conditions | Glucose, cellobiose, xylose, arabinose, galactose, mannose, acetate, lactate, oleic acid, p-coumarate, ferulate, benzoate, sugar alcohols, pentuloses; valine, leucine and phenylalanine as carbon sources | **Yes.** Frontiers supplement Table_2.XLSX, sheet "RB-TDNA Seq" (ids `RTO4_<n>`), CC BY |
| Coradetti et al. 2018, PMID:29521624 | *R. toruloides* | 6,558 genes | Glucose, oleic and ricinoleic acid; auxotrophy media | **Yes.** eLife supp2 xlsx, CC BY |
| Rodríguez-López et al. 2023, PMID:37787768 | *S. pombe* | 3,509 deletions × 131 conditions (450,844 rows, with p-values) | Glycerol, galactose, fructose, maltose, sucrose, mannitol, xylose, ethanol; glutamate, proline, lysine, serine | **Yes.** eLife supp1 xlsx (39 MB), CC BY. The curated subset is already in PomBase (above) |
| Yeast Phenome, Turco et al. 2023, PMID:37235661 | *S. cerevisiae* | 4,554 genes × 14,484 harmonised screens (includes Hillenmeyer 2008, Dudley 2005, Qian 2012) | YPG, YPL, YPE, galactose, raffinose, maltose and others | **Yes.** `yp_haphom_20221025.tar.gz` (637 MB) from the project's Google Cloud bucket; licence not stated |

The bacterial Fitness Browser (Price et al. 2018, PMID:29769716) is the model
for this kind of data, but its 2026 figshare archive lists only bacteria and
archaea; there is no fungal organism in it. Its site sits behind a Cloudflare
challenge and could not be fetched from our environment.

### Pathogenic yeasts

| Dataset | Organism | Scope | Download |
|---|---|---|---|
| Homann et al. 2009, PMID:20041210 | *Candida albicans* | ~160 TF knockouts × ~107 conditions, incl. no carbon source, galactose, glycerol, GABA/proline nitrogen | **Yes.** PLoS supplement s007.xls, CC BY |
| CGD phenotype file | *C. albicans* and other Candida | 27,890 curated rows, incl. Homann, Noble 2010 (PMID:20543849) and Segal 2018 transposon essentiality (PMID:30377286); ~200 carbon-source rows | **Yes.** `candidagenome.org/download/phenotype/`, updated weekly |
| Jung 2015 (PMID:25849373), Lee 2016 (PMID:27677328), Jin 2020 (PMID:32839469) | *Cryptococcus neoformans* | TF, kinase and phosphatase knockout phenomes, about 30 conditions each; mostly stress, drug and virulence; galactose only | **Yes.** Nature Communications supplements, CC BY |
| Billmyre et al. 2025, PMID:40402997 | *C. neoformans* | Transposon essentiality and fluconazole fitness for 6,975 genes; no carbon conditions | **Yes.** PLoS Biol supplement |

Other transposon sets (Grech 2019 *S. pombe* Hermes, PMID:31077324; SATAY,
PMID:28481201) cover essentiality and drugs, not nutrients.

### Filamentous fungi

No filamentous-fungus knockout collection has been screened across a panel of
carbon or plant-biomass sources. Carbon phenotypes exist only as short hit
lists or figures.

| Dataset | Organism | Scope | Download |
|---|---|---|---|
| Carrillo et al. 2020, PMID:33138786 | *Neurospora crassa* | 1,168 knockouts × 10 growth and development traits; no carbon sources | **Yes.** BMC supplement xlsx (NCU ids), CC BY |
| Son et al. 2011, PMID:22028654 | *Fusarium graminearum* | 657 TF knockouts × 17 traits, incl. minimal versus rich medium; CMC conidiation in a separate table | **Yes.** PLoS supplement, ordinal scores, CC BY |
| PHI-base (v4 CSV, PHI-base 5 export, GAF) | Pathogens, incl. *F. graminearum*, *M. oryzae*, *A. fumigatus* | 24,123 interaction rows; virulence plus an in vitro growth field; PHI-base 5 uses PHIPO, which has carbon-source terms | **Yes.** GitHub `PHI-base/data`. Licence statements conflict (CC BY vs CC BY-ND) |
| Coradetti et al. 2012, PMID:22532664 | *N. crassa* | TF knockout screen on Avicel, xylan, sucrose | Hits in text; no per-strain table found |
| Brown et al. 2013, PMID:23800192 | *Aspergillus nidulans* | Non-essential kinases and phosphatases screened for cellulase production | Results in figures only |
| Wu et al. 2020, PMID:32111691 | *N. crassa* | RNA-seq on 40 carbon sources; growth for ~8 TF mutants | Supplement xlsx not opened |
| Lu et al. 2014, PMID:25299517 | *Magnaporthe oryzae* | 104 Zn2Cys6 TF knockouts; olive oil as carbon source | Phenotypes in PDF only |
| Kun et al. 2021, PMID:34114741, and other de Vries lab papers | *Aspergillus niger* | Regulator knockouts (XlnR, AraR, ClrA/B, AmyR) on wheat bran and polysaccharides | Per-paper figures; no consolidated table |
| Furukawa et al. 2020, PMID:31969561 | *Aspergillus fumigatus* | COFUN library, 484 TF knockouts; antifungal screens, no carbon sources | Supplement not retrieved |

FungiDB's search service now needs a registered API key, so its phenotype
tracks could not be pulled. Only 1 of our 73 filamentous-fungus and *Candida*
reviews (EMENI brlA) appears in PHI-base, as expected for a pathogen database.

## Suggested next steps

1. *R. toruloides* is the best fungal test bed: genome-wide fitness on 20
   carbon sources, the same kind of data as the bacterial Fitness Browser,
   and the closest match to FUNG-GROWTH's substrate panel. The analysis in
   [FUNGAL_PHENOTYPES/RHOTO.md](FUNGAL_PHENOTYPES/RHOTO.md) maps it to UniProt,
   finds 137 genes with strong carbon-source-specific defects and lists
   candidates for the first *R. toruloides* gene reviews.
2. Extend `phenotype_overlap.py` to Candida (CGD file) and to the
   Rodríguez-López quantitative table, so reviews can quote fitness values,
   not just curated labels.
3. For *A. niger* and *T. reesei* CAZyme reviews, pair FUNG-GROWTH species
   profiles with the de Vries lab regulator knockouts, curated by hand.

## Reproducing

    uv run python projects/FUNGAL_PHENOTYPES/scripts/phenotype_overlap.py

The *R. toruloides* scripts and their order are listed on
[FUNGAL_PHENOTYPES/RHOTO.md](FUNGAL_PHENOTYPES/RHOTO.md).

Downloads are cached in `tmp/fungal_phenotypes/` (gitignored).
