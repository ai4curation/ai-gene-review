# erg5 (SPAC19A8.04; cyp61; UniProt O13820) notes

- Fetched accession verified O13820 (ERG5_SCHPO). Cytochrome P450 CYP61 (PTHR24286:SF228).
- Reaction: [UniProt:O13820 "Reaction=5-dehydroepisterol + NADPH + O2 + H(+) ="] EC 1.14.19.41 = GO:0000249 definition.
- Deletion: [PMID:18310029 "Disruption mutants of these genes were unable to synthesize ergosterol"]; [PMID:23145048 "in Δerg6 cells, Δerg31Δerg32 cells, and Δerg5 cells, the ergosterol levels were extremely lower than that in wild-type cells"]; erg5 deletants grow even with terbinafine (PMID:23145048).
- Dap1: [PMID:17276356 "We show that S. pombe Dap1 is a hemoprotein that binds and positively regulates Cyp51A1 and Cyp61A1, two P450s required for sterol biosynthesis."] -> protein binding IPI REMOVE (uninformative; same as erg11 review), the regulation sits on dap1.
- Generic MF IEA/IBA (monooxygenase, oxidoreductase, GO:0016705) -> MODIFY to GO:0000249 (GO:0000249 is not under GO:0004497 in GO). Heme/iron binding kept as non-core cofactor annotations.
- No ER membrane row in GOA (only ER ISO); core location given as ER membrane (anchored P450), consistent with module.
- Budding-yeast ERG5 review core: GO:0000249, ER membrane. Consistent.
- GO-CAM 66c7d41500002088: erg5 GO:0000249 in ER, positively regulated by dap1, -> erg4. Agrees. (SGD PWY-6075-1 and superpathway models type ERG5 only with GO:0003674.)
