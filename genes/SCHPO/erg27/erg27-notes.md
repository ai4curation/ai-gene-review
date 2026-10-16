# erg27 (SPBC1709.07; UniProt O74732) notes

- Identity: 3-keto-steroid reductase, SDR family ERG27 subfamily (PANTHER PTHR43647:SF1) [UniProt:O74732 "Belongs to the short-chain dehydrogenases/reductases (SDR)"]. Fetched accession verified as O74732 (ERG27_SCHPO).
- Reaction (by similarity to S. cerevisiae Q12452): [UniProt:O74732 "Reaction=3-dehydro-4alpha-methylzymosterol + NADPH + H(+) = 4alpha-"] EC 1.1.1.270.
- Complex: [UniProt:O74732 "SUBUNIT: Heterotetramer of erg25, erg26, erg27 and erg28 (By"] - by similarity only.
- No S. pombe-specific experimental data in GOA; all 9 annotations are IBA/IEA/ISS.
- Budding-yeast ortholog review (genes/yeast/ERG27): core MF GO:0000253, BP GO:0006696 + GO:0036197, ER membrane, in C-4 demethylation complex. Kept consistent. Budding-yeast Erg27 also stabilises Erg7 in lipid particles [PMID:12842197 "Erg27p is required for oxidosqualene cyclase (Erg7p) activity"] - not tested in S. pombe; IBA lipid droplet kept as non-core.
- Schizosaccharomyces may also C-24 methylate lanosterol before demethylation (eburicol route) [PMID:8586261 "the transmethylation process on the C-24 may occur directly on lanosterol and not only on zymosterol"], so Erg27 may also act on 24-methylated 3-keto intermediates.
- PomBase GO-CAM 66c7d41500002088: erg27 enables GO:0000253 in ER membrane, part_of GO:0006696, -> erg6. Agrees.
- Decision: GO:0033764 (ARBA) MODIFY -> GO:0000253; everything else ACCEPT except LD (non-core).
