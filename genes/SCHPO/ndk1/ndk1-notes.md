# ndk1 (SPAC806.07; UniProt P49740) notes

## Experimental (S. pombe)
- Izumiya & Yamamoto 1995 (abstract-only): [PMID:7499258 "The gene product exhibited NDK activity and cross-reacted with antibodies raised against rat NDK."]; [PMID:7499258 "Disruption of ndk1 greatly reduced the cellular NDK activity but caused no obvious phenotype in cell growth and sexual development of the organism."]; C116 allele [PMID:7499258 "the mutant gene product showed no NDK activity"] and acts dominant-negatively on mating [PMID:7499258 "a mutated allele of ndk1 could inhibit sexual development in a dominant-negative manner"].
- Activity: [UniProt:P49740 "Reaction=a ribonucleoside 5'-diphosphate + ATP = a ribonucleoside 5'-"]; [UniProt:P49740 "FUNCTION: Major role in the synthesis of nucleoside triphosphates other"].

## Location
- HDA cytosol + nucleus (PMID:16823372). Mitochondrion IBA and IMS ISO derive from S. cerevisiae Ynk1 [PMID:12472466 "a small fraction of total NDPK activity encoded by YNK1 is present in the intermembrane space (IMS) of mitochondria"]; untested in S. pombe -> non-core.

## GO-CAMs
- 69a0c46f00003691: two ndk1 activities (GO:0004550, cytosol), part_of UTP biosynthesis (GO:0006228) and CTP biosynthesis (GO:0006241).
- 6796b94c00000009 (phospholipid synthesis): GO:0004550 part_of CTP biosynthesis (CTP for CDP-DAG/CDP-choline/ethanolamine).
- Consistent with review; core BPs chosen as GO:0009142 + GO:0006228 to match S. cerevisiae YNK1 review.

## Decisions
- All MF/BP rows accepted; IMP CTP biosynthetic process deferred to curator (full text unavailable).
- Nucleus, mitochondrion, IMS kept non-core.
