# ERG13 (YML126C) notes

UniProt P54839; HMG-CoA synthase, EC 2.3.3.10; thiolase-like superfamily [UniProt:P54839].

## Evidence journal
- Mutants: [PMID:6148937 "Mutants deficient in beta-hydroxy-beta-methylglutaryl-CoA synthase belong to two unlinked complementation groups, erg 11 and erg 13."] (historical erg11 group, not CYP51); anaerobic mevalonate requirement [PMID:6148937].
- PMID:12702274 is abstract-only and about FPP synthase/dolichol; UniProt cites it for Erg13 function and an erg13 disruption phenotype ("Drastically increases HMG2 half-life") [UniProt:P54839], so curator IMP rows deferred to (ACCEPT).
- Single HMGS in yeast; no ketogenic mitochondrial isoform.

## Decisions
- Mitochondrion NAS (PMID:28904410, Hu et al. 2017 review) REMOVE: the review body (read at PMC5574775) states the HMGS and HMGR reactions "take place in the mitochondria" and the Erg12-Erg20 module in vacuoles; HMGR is demonstrably ER-membrane, no primary mitochondrial Erg13 data.
- Acetyl-CoA metabolic process (IBA/IEA) KEEP_AS_NON_CORE (substrate-level). Acyltransferase IEA MODIFY -> GO:0004421. Nucleus HDA non-core. Rest ACCEPT.
