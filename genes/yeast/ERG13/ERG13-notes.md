# ERG13 (YML126C) notes

UniProt P54839; HMG-CoA synthase, EC 2.3.3.10; thiolase-like superfamily [UniProt:P54839].

## Evidence journal
- Mutants: [PMID:6148937 "Mutants deficient in beta-hydroxy-beta-methylglutaryl-CoA synthase belong to two unlinked complementation groups, erg 11 and erg 13."] (historical erg11 group, not CYP51); anaerobic mevalonate requirement [PMID:6148937].
- PMID:12702274 is abstract-only and about FPP synthase/dolichol; UniProt cites it for Erg13 function and an erg13 disruption phenotype ("Drastically increases HMG2 half-life") [UniProt:P54839], so curator IMP rows deferred to (ACCEPT).
- Single HMGS in yeast; no ketogenic mitochondrial isoform.

## Decisions
- Mitochondrion NAS (PMID:28904410, Hu et al. 2017 review) REMOVE: the review body (read at PMC5574775) states the HMGS and HMGR reactions "take place in the mitochondria" and the Erg12-Erg20 module in vacuoles; HMGR is demonstrably ER-membrane, no primary mitochondrial Erg13 data.
- Acetyl-CoA metabolic process (IBA/IEA) KEEP_AS_NON_CORE (substrate-level). Acyltransferase IEA MODIFY -> GO:0004421. Nucleus HDA non-core. Rest ACCEPT.

## 2026-11-21 PTHR43323 alignment

- Re-checked the three ERG13 IBA rows against the local `PTHR43323` PAINT
  review: `PTN000222418` carries both the conserved HMG-CoA synthase activity
  and broad acetyl-CoA-process assertions, while fungal `PTN000933803`
  carries the ergosterol-biosynthesis assertion.
- The ERG13 self-seed on the PAINT rows is direct experimental grounding for
  the ancestral placement, not circular evidence.
- PubMed searches for 2024-2026 `Saccharomyces cerevisiae` ERG13/HMG-CoA
  synthase papers found newer metabolic-engineering and CRISPR
  essential-gene targeting uses of ERG13, but no paper that changes the
  native HMG-CoA synthase activity, cytosolic mevalonate role, or IBA calls.
