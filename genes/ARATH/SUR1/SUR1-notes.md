# SUR1 (At2g20610, Q9SIV0) review notes

## Summary of biology
- PLP-dependent C-S lyase of core glucosinolate biosynthesis [PMID:14871316 "We report characterization of SUPERROOT1 (SUR1) as the C-S lyase in glucosinolate biosynthesis."]; sur1 "is completely devoid of aliphatic and indole glucosinolates"; recombinant enzyme active on djenkolic acid.
- High-auxin superroot phenotype is indirect: [PMID:14871316 "the \"high-auxin\" phenotype of sur1 is caused by accumulation of endogenous C-S lyase substrates as well as aldoximes, including indole-3-acetaldoxime (IAOx) that is channeled into the main auxin indole-3-acetic acid (IAA)"]. Original mutant: [PMID:8589625 "increased levels of both free and conjugated indole-3-acetic acid"].
- 2026 update: sur1 still makes significant indolic GLs, so an additional C-S lyase exists; auxin excess in sur1 depends on MYB34 [PMID:41819465].
- Family: PTHR45744 (tyrosine aminotransferase), subfamily SF15 (SUR1). SUR1-like Taraxacum C-S lyase lacks TyrAT activity but has AlaAT activity [PMID:23073363 "we detected no in vitro tyrosine aminotransferase (TyrAT) activity"].

## Decisions
- S-alkylthiohydroximate lyase (IMP), C-S lyase (IDA), glucosinolate biosynthesis (IMP), cytosol, cytoplasm, PLP binding -> ACCEPT.
- IAA biosynthesis (IMP), adventitious root development (TAS), regulation of cell growth by extracellular stimulus (IMP) -> MARK_AS_OVER_ANNOTATED: indirect consequences of IAOx shunting; SUR1 performs no step in these processes. Not REMOVE because experimental/abstract-only.
- TAT activity IBA -> MARK_AS_OVER_ANNOTATED; L-tyrosine catabolic process IBA -> REMOVE (neofunctionalized subfamily, no Tyr-catabolism phenotype). propagation_review: PROPAGATION_BAD / FUNCTIONAL_DIVERGENCE.
- transaminase activity IEA -> MODIFY to GO:0080108. amino acid metabolic process IEA -> MARK_AS_OVER_ANNOTATED.
- protein binding IPI -> REMOVE (uninformative).
- mitochondrion HDA -> MARK_AS_OVER_ANNOTATED.
- defense response to fungus IDA (PMID:32213638) -> UNDECIDED: cited paper is about ODR1/bHLH57 seed dormancy; abstract-only, no full text retrievable from Europe PMC; cannot verify.
- No NEW terms.
