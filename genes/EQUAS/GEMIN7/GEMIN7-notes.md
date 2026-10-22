# GEMIN7 (donkey, Equus asinus) - A0A9L0ICL9

DONKEY40 cohort review. Unreviewed TrEMBL entry, 206 aa, "Gem-associated protein 7"; PANTHER PTHR14679:SF1; Pfam Gemin7; Sm domain 140-206.

## Sources
- Donkey UniProt `GEMIN7-uniprot.txt` (ARBA function/subunit/location text).
- Donkey GOA `GEMIN7-goa.tsv`: 7 IEA rows (2 TreeGrafter GO_REF:0000118: spliceosomal snRNP assembly, Sm-like protein family complex; 3 SubCell; 1 InterPro2GO; 1 combined RNA binding).
- Human ortholog Q9H840 UniProt fetched to `GEMIN7-bioinformatics/human-Q9H840-uniprot.txt`. No human/mouse GEMIN7 review in repo.
- Cached (abstract-only): PMID:12065586, PMID:15939020, PMID:17178713, PMID:18984161.

## Sequence
- Donkey 76-206 align ungapped to complete human GEMIN7 (1-131) at 87.79% identity; 75-residue N-terminal extension [file:EQUAS/GEMIN7/GEMIN7-bioinformatics/RESULTS.md].

## Biology
- Component of SMN complex; colocalizes with SMN in cytoplasm and gems; binds SMN and Gemin6; binds Sm proteins, especially SmE [PMID:12065586 "Gemin7 is a component of the SMN complex and colocalizes with SMN in the cytoplasm and in gems"].
- Gemin6-Gemin7 heterodimer with Sm folds, no Sm sequence similarity [PMID:15939020 "Although Gemin6 and Gemin7 have no significant sequence similarity with Sm proteins, both adopt canonical Sm folds."].
- SMN, Gemin8 and Gemin7 form the centre of the SMN complex [PMID:17178713 "SMN, Gemin8, and Gemin7 in its center"].
- SMN complex catalyses snRNP core formation [PMID:18984161 "the SMN complex as a catalyst of spliceosomal snRNP formation"].

## Decisions
- ACCEPT: spliceosomal snRNP assembly, nucleoplasm, cytoplasm, SMN-Sm protein complex, Gemini of Cajal bodies, Sm-like protein family complex.
- MARK_AS_OVER_ANNOTATED: RNA binding (Sm-domain InterPro mapping; no GEMIN7 RNA-binding evidence).
- NEW: SMN complex (GO:0032797), human IDA exists; not in donkey GOA.
