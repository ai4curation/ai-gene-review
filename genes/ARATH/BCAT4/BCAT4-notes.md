# BCAT4 (At3g19710, Q9LE06) review notes

## Identity and activity
- Cytosolic class-IV PLP aminotransferase, member of the six-gene Arabidopsis BCAT family but specialized for methionine.
- Recombinant BCAT4 prefers Met and its derivatives: [PMID:17056707 "Recombinant BCAT4 showed high efficiency with Met and its derivatives and the corresponding 2-oxo acids"].
- Kinetics: [PMID:17056707 "For Met, K m and V max values were calculated to be 0.93 ± 0.08 mM"]; Leu is a poorer substrate: [PMID:17056707 "Thus, the affinity of BCAT4 to Leu is about five times lower than to Met."]
- Fails to complement yeast BCAA auxotrophy: [PMID:12068099 "No complementation was achieved with AtBCAT-4 (data not shown)."]

## In vivo role
- Two knockout alleles reduce Met-derived glucosinolates by ~50% and accumulate Met/SMM: [PMID:17056707 "This sharp increase of free Met and its transport derivative SMM further support the conclusion that BCAT4 catalyzes the initial transamination of Met in glucosinolate formation generating MTOB."]
- Residual glucosinolates are made with help from plastid BCAT3; bcat3 bcat4 double mutants have stronger loss [PMID:18162591 "This strongly suggests that BCAT3 can act as a backup of BCAT4 by transaminating Met to MTOB"].

## Localization / expression
- Cytosol by GFP and fractionation [PMID:17056707 "The green fluorescence is seen exclusively in the cytosol ( Figure 5A )."]; this separates BCAT4 from the plastid MAM step.
- Phloem-expressed, wound-inducible, light/diurnal (IEP annotations kept as non-core).

## Curation decisions
- Core MF: GO:0010326 L-methionine:oxo-acid transaminase activity (IDA, EXP, IEA all ACCEPT).
- GO:0004084 BCAA transaminase (IBA, IEA): KEEP_AS_NON_CORE (residual in vitro Leu activity; not physiological).
- GO:0009081 BCAA metabolic process (IEA): MARK_AS_OVER_ANNOTATED.
- EXP from PMID:18318836 (Funakoshi 2008, D-amino acid aminotransferase paper) is abstract-only and the abstract does not mention BCAT4; UniProt cites it for BCAT4 kinetics, so deferred to curator (ACCEPT).
- NEW: GO:0033322 L-homomethionine biosynthetic process. Participation passes (BCAT4 catalyzes the first step of the chain-elongation cycle). Comparator check: QuickGO shows zero annotations to GO:0033322 for any gene product, so no convention excludes catalysts; term is unused rather than deliberately withheld.
- No deep-research file was available at the time of review.
