# gal1 (SPBPB2B2.13, UniProt Q9HDU2) notes

## Identity
- UniProt: Galactokinase, EC 2.7.1.6 by similarity to S. cerevisiae GAL1 (P04385); GHMP kinase family, GalK subfamily [UniProt:Q9HDU2].
- In the silenced subtelomeric gal cluster [PMID:21075050 "gal7+, gal10+, and gal1+ are localized close to a chromosomal terminal repressed by gene silencing in S. pombe"]; strongly induced by galactose in the galactose-assimilating mutant [PMID:21075050 "were highly expressed and dramatically induced by addition of galactose"].

## Evidence
- No direct S. pombe enzyme assay found. Overexpression of gal7, SPBPB2B2.13, gal10 and gal1 permits growth on galactose [PMID:21075050 "these transformants grew on galactose medium"].
- UniProt FUNCTION also transfers from S. cerevisiae GAL1 the ability to "induce the transcription of the gal genes" (by similarity). S. pombe has no GAL4/GAL80/GAL3 switch, so this transfer is doubtful; not present in GOA.

## Location
- HTP YFP: cytoplasm/cytosol [PMID:16823372].

## GO-CAM
- 6796b94c00002484: gal1 enables GO:0004335 (IBA), cytosol (HDA), part_of GO:0033499. Consistent with this review.

## 2026-11-12 audit (to COMPLETE)
- No deep-research provider file was available for this gene; none was generated. Literature check: cached abstracts PMID:21075050, PMID:19942659, PMID:16823372; a web search for S. pombe gal-cluster silencing found no further gal1-specific primary paper (no direct galactokinase assay reported).
- PMID:21075050 abstract lists "gal7+, SPBPB2B2.13, gal10+ and gal1+" although SPBPB2B2.13 is gal1 itself; treated as a wording slip.
- Rewrote the carbohydrate phosphorylation (GO:0046835) reason: not an ancestor of GO:0033499, kept non-core as in the S. cerevisiae GAL1 review.
- Actions kept consistent with genes/yeast/GAL1 (cytoplasm/cytosol ACCEPT; galactose metabolic process TOO_GENERAL; kinase/phosphotransferase TOO_GENERAL). ATP binding kept non-core (budding yeast review ACCEPTs it; both are defensible).
- No PAINT IRD/IKR on the gal1 lineage (`just paint-losses SCHPO gal1`).
