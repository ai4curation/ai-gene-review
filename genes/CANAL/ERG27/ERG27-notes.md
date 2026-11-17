# CANAL ERG27 notes

## 2026-11-17 PTHR43647 Erg27 review

The current GOA fetch for *Candida albicans* `ERG27` has no rows, but the PAINT leaf GAF does project four `PTHR43647` IBAs to Q5A888: `GO:0000253` 3-beta-hydroxysteroid 3-dehydrogenase (NADP+) activity from `PTN002462496`, and `GO:0006696` ergosterol biosynthetic process, `GO:0005789` endoplasmic reticulum membrane, and `GO:0005811` lipid droplet from `PTN002462498`.

The exact activity node is one of the cleanest in the family: its seeds are CGD `CAL0000174882` and SGD `S000004090`, and Q5A888 is itself the `C. albicans` Erg27 seed in `PTHR43647:SF1`. The direct abstract-only *C. albicans* paper states that ERG27 is "required for sterol C-4 demethylation" and that repressing it compromised sterol synthesis [PMID:15552648 "required for sterol C-4 demethylation"].

I proposed the lipid-droplet PAINT row because current PAINT does project it to this protein, but kept it out of `core_functions`. It comes from the budding-yeast Erg27 lipid-particle pool, where Erg27 stabilizes Erg7, and is less certain for *C. albicans* than the ER C-4 demethylation role.
