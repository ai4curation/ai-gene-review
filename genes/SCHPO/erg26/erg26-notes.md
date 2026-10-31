# erg26 (SPBC3F6.02c, UniProt O43050) notes

Module: `ergosterol_biosynthesis` (C-3 sterol dehydrogenase/C-4 decarboxylase); S. cerevisiae ortholog ERG26 (P53199). Fetch verified: O43050.

## Evidence
- 3-beta-HSD family; reaction [UniProt:O43050 "Reaction=4beta-methylzymosterol-4alpha-carboxylate + NADP(+) = 3-"]; ER membrane peripheral (ORFeome) [PMID:16823372].
- All activity evidence is by similarity/phylogeny; no S. pombe biochemistry.

## Curation decisions
- Golgi HDA (ORFeome) kept non-core; generic CH-OH oxidoreductase IEA MODIFY -> GO:0000252.
- PomBase GO-CAM uses GO:0005783 ER (not ER membrane) for erg26.
- UniProt PANTHER xref is PTHR43245 (BIFUNCTIONAL POLYMYXIN RESISTANCE PROTEIN ARNA) / SF51 (SDR42E2) - surprising family names for the NSDHL/ERG26 descriptor in the module.
