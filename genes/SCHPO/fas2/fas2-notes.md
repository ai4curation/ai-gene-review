# fas2 (SPAC4A8.11c, lsd1, UniProt Q10289) notes

Fetch: `just fetch-gene SCHPO fas2` fetched the correct accession (FAS2_SCHPO, Q10289, 1842 aa).

## Naming
- Synonym lsd1 (large and small daughter). [PMID:11470243 "The lsd1(+) gene is the homologue of the budding yeast FAS2 gene encoding the fatty acid synthase alpha-subunit"].
  Alpha subunit as in S. cerevisiae FAS2 - composition congruent with budding yeast.
- UniProt AltName p190/210: the protein purified as a DNA strand-exchange stimulating activity [PMID:8188691 "we report the purification of p190/210 from S. pombe cells and its identification as fatty acid synthase (FAS)"];
  the authors consider an in vivo recombination role "highly unlikely". No GO annotation; not used.

## Evidence
- Complex & activity: PMID:9693066 (co-expression with fas1, purified alpha6beta6 with >4000 mU/mg).
- Essential; lsd phenotype rescued by palmitate (PMID:8769419).
- ts alleles accumulate C30 (melissoyl) phospholipids; palmitate rescue (PMID:11470243).
- Domains [UniProt:Q10289]: ACP (PF18325), KR (adh_short), KS, PPT (ACPS).

## GO-CAM (gomodel:678073a900002931)
- fas2 enables GO:0004315, GO:0008897, GO:0004316, GO:0000036 in cytosol. Agrees with this review.

## Decisions (consistent with genes/yeast/FAS2)
- GO:0004312 rows -> MODIFY to GO:0004321.
- mitotic nuclear membrane biogenesis and palmitic acid biosynthetic process: KEEP_AS_NON_CORE.
- Core: contributes_to GO:0004321 in GO:0005835; partial MFs GO:0004315, GO:0004316, GO:0000036, GO:0008897; BP GO:0042759; cytosol.
