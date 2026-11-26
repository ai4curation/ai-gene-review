# GUD1 (Q07729, YDL238C) notes

Module: `purine_salvage_and_catabolism`, role = guanine deaminase (guanine + H2O -> xanthine + NH3, EC 3.5.4.3).
YeastCyc: GUANINE-DEAMINASE-RXN in PWY3O-1, PWY3O-285 (superpathway) and PWY3O-743; default cytosol on all.

## Evidence journal
- Activity [PMID:15565584 "we show that GUD1 (YDL238c) encodes guanine deaminase, a catabolic enzyme producing xanthine and ammonia from guanine"]
- Post-diauxic induction [PMID:15565584 "Gud1p activity was higher during post-diauxic growth"]
- Km 61.5 uM; cytoplasmic GFP; Zn by similarity [UniProt:Q07729]
- PMID:10542258 (SGD IDA, guanine catabolic process) is a 1999 paper on p51-nedasin, a neuronal NE-dlg/SAP102-binding amidohydrolase [PMID:10542258 "Nedasin has a significant homology with amidohydrolase superfamily proteins and shows identical sequences to a recently identified protein that has guanine aminohydrolase activity"]; no yeast data in abstract. Term kept (correct on other evidence); reference flagged.

## Decisions
- MF/BP/CC core rows ACCEPT. Zinc rows non-core. Generic hydrolase rows and 'guanine metabolic process' MODIFY.
- 'purine-containing compound salvage' (YeastPathways RCA x3) KEEP_AS_NON_CORE: Gud1 diverts guanine away from Hpt1 salvage; xanthine can be re-salvaged by Xpt1.
