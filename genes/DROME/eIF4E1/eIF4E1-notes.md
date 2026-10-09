# eIF4E1 (P48598) review notes

Module context: dmel_eif4e_cup_complex (eIF4E1 bound by Cup).

Deep research: the first falcon run (with perplexity-lite fallback) failed (falcon
timeout / killed; perplexity provider unavailable). Literature below is from cached
publications.

## Molecular function
- Cap binding: [PMID:8663200 "Eukaryotic initiation factor 4E (eIF4E) is the subunit of eIF4F that binds to the cap structure at the 5' end of messenger RNA"]; [PMID:8027064 "Only the eIF-4E subunit was able to cross-link to the m7G cap structure"]
- Major embryonic isoform: [PMID:15804566 "This indicates the cap-binding activity relies mostly on eIF4E-1 during embryogenesis"]
- Functional initiation factor: [PMID:15804566 "eIF4E-1, eIF4E-2, eIF4E-3, eIF4E-4 and eIF4E-7 rescued a yeast eIF4E-deficient mutant in vivo"]
- eIF4F assembly target of miRNA repression: [PMID:25280104 "We propose that miRNAs act to block the assembly of the eIF4F complex during translation initiation"]

## Regulation by eIF4E-binding proteins
- Cup: [PMID:14685270 "Cup is an eIF4E-binding protein that blocks the binding of eIF4G to eIF4E"]
- Me31B: [PMID:36638908 "We show that Me31B interacts with eIF4E-1 and eIF4E-3 by means of yeast two-hybrid system"]
- P bodies: [PMID:36638908 "we show that Drosophila eIF4E-1 and eIF4E-3 occur in PBs along the DEAD-box RNA helicase Me31B"]

## Decisions
- eIF4G partner protein-binding rows -> MODIFY to GO:0031370; other protein binding rows (Cup, Me31B, Thor, PABP, GLD2) REMOVE as uninformative. The repressor activity belongs on the binding partners (Cup, Thor), not on eIF4E1.
- Nuclear body (PML study, PMID:11500381; abstract only, vertebrate structure) -> UNDECIDED.
- RNA metabolic process -> MODIFY to cytoplasmic translational initiation.
- NMJ / neuronal RNP localizations kept as non-core.
