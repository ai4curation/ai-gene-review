# APT1 (YML022W, UniProt P49435) notes

## Function
- APRT EC 2.4.2.7 [UniProt:P49435]; "The enzyme catalyzes the Mg-dependent condensation of adenine and 5-phosphoribosylpyrophosphate (PRPP) to yield AMP." [PMID:9357956]
- "only APRT1 had detectable APRT activity" and "We conclude that APT1 is the functional gene in S. cerevisiae and that APT2 is a pseudogene." [PMID:9864350]
- Dimeric short APRT, crystal structure [PMID:11535055].
- "Exogenous adenine enters metabolic pathways primarily via the function of either AAH or adenine phosphoribosyltransferase (APRT; EC 2.4.2.7)." [PMID:1577682]
- apt1 mutants selected as 8-azaadenine resistant [PMID:6392474].

## Pathway / YeastCyc
- ADENPRIBOSYLTRAN-RXN in PWY3O-1/2220/285 lists APT1 and APT2. APT2 inclusion is a YeastCyc error (Apt2 inactive, not expressed).
- GO convention: "adenine salvage" (literal definition = forming adenine) is used for APRTs; accepted.

## Decisions
- Core MF GO:0003999; BP GO:0044209 AMP salvage + GO:0006168 adenine salvage; cytoplasm.
- KEEP_AS_NON_CORE adenine/AMP binding IBA and nucleus HDA/IEA. REMOVE protein binding (Apt2) x2.
