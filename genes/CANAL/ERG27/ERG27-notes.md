# CANAL ERG27 notes

## 2026-11-17 PTHR43647 Erg27 review

The first `just fetch-gene CANAL ERG27` pass produced a header-only GOA file because the QuickGO request path was brittle; a direct Q5A888 QuickGO query without expanded taxon names returns 17 rows. I backfilled those rows into `ERG27-goa.tsv` before reviewing the file so that the CGD IMP/IGI rows from PMID:15552648 and PMID:17604452, the GO-Central IBAs, the UniProt ISS/IEA rows, and the EnsemblFungi complex row are all represented.

The exact activity node is one of the cleanest in the family: its seeds are CGD `CAL0000174882` and SGD `S000004090`, and Q5A888 is itself the `C. albicans` Erg27 seed in `PTHR43647:SF1`. The direct abstract-only *C. albicans* paper states that ERG27 is "required for sterol C-4 demethylation", that the null loses 3-keto reductase and oxidosqualene cyclase activities, and that repressing it compromised sterol synthesis [PMID:15552648 "required for sterol C-4 demethylation"; "complete loss of both 3-keto reductase and oxidosqualene cyclase"; "compromising all sterol synthesis"].

The current PAINT/UniProt lipid-droplet rows are plausible and consistent with loss of oxidosqualene cyclase activity after C. albicans ERG27 repression, but I kept them non-core because the demonstrated enzymatic activity is the ER C-4 demethylation reductase. CGD's `GO:0071466` xenobiotic-response IMP is probably an over-read of the radicicol CaFT hit from PMID:17604452 rather than a separate Erg27 pathway role. No C. albicans Erg27 paper found in this review directly localizes the protein; PMID:15552648 covers ERG27 isolation, expression, essentiality, 3-keto reductase activity, and oxidosqualene cyclase loss, while PMID:17604452 is a pooled chemical-genetic fitness screen.
