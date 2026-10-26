# erg31 (UniProt O94457) notes

- Fetched accession verified O94457. Delta(7)-sterol 5(6)-desaturase, sterol desaturase family (PTHR11863), His-box di-iron enzyme [UniProt:O94457 "Belongs to the sterol desaturase family."].
- Reaction: [UniProt:O94457 "Reaction=episterol + 2 Fe(II)-[cytochrome b5] + O2 + 2 H(+) = 5-"] EC 1.14.19.20.
- Redundancy with erg32: [PMID:18310029 "Disruption of erg31(+) or erg32(+) did not cause ergosterol deficiency or tolerance to polyene drugs, indicating that the two C-5 sterol desaturases have overlapping functions"]; double deletant lacks ergosterol (UniProt disruption phenotype) and [PMID:23145048 "in Δerg6 cells, Δerg31Δerg32 cells, and Δerg5 cells, the ergosterol levels were extremely lower than that in wild-type cells"].
- GO:0000248 "C-5 sterol desaturase activity" definition problem (see genes/yeast/ERG3): its definition is the C-22 desaturation (5,7,24(28)-ergostatrienol -> 5,7,22,24(28)-ergostatetraenol + NADPH), i.e. the erg5/GO:0000249 reaction. Verified with runoak. MODIFY the IBA GO:0000248 row -> GO:0050046 (Rhea:54320), as for ERG3.
- PomBase GO-CAM 66c7d41500002088 types both erg31 and erg32 with GO:0000248 - disagreement to flag.
- Localisation: ER (ORFeome HDA) plus a Golgi call [PMID:16823372]; Golgi kept as non-core.
- Naming: erg31 has synonym erg3 in UniProt; erg32 ORF name pi075. Budding-yeast ERG3 is the single ortholog of both.
- erg31 is induced under anaerobiosis via Sre1 [PMID:16537923 "Oxygen-requiring biosynthetic pathways for ergosterol, heme, sphingolipid, and ubiquinone were primary targets of Sre1p."].
