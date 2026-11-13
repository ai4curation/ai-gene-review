# thiE (PP_4783, Q88DP1) curation notes

## Sources

Deep-research providers were not available in this session; no
`-deep-research-<provider>.md` file was generated. No KT2440-specific thiE
publication is in the cache (title search as for thiD). Evidence is the Swiss-Prot
record (HAMAP MF_00097), cached E. coli/yeast papers and the PTHR20857 family review.

## Evidence

- HAMAP function: "Condenses 4-methyl-5-(beta-hydroxyethyl)thiazole monophosphate
  (THZ-P) and 2-methyl-4-amino-5-hydroxymethyl pyrimidine pyrophosphate (HMP-PP) to
  form thiamine monophosphate (TMP)." [file:PSEPK/thiE/thiE-uniprot.txt]. Three Rhea
  reactions incl. the carboxylated thiazole tautomer (RHEA:47844) and
  carboxythiazole (RHEA:47848) with CO2 release.
- Mg2+: "Binds 1 Mg(2+) ion per subunit." (HAMAP).
- PANTHER subfamily SF15 THIAMINE-PHOSPHATE SYNTHASE (not SF22 TenI tautomerase).
- E. coli genetics: auxotrophs lacking thiamine phosphate pyrophosphorylase
  [PMID:6284709]. Yeast THI6 TMP-PPase biochemistry [PMID:7982968].
- Caution: PMID:8432721 abstract groups thiE with thiazole-synthesis genes; this is the
  1993 view, superseded; not used as support.

## Decisions (2026-11-12)

- GO:0000287 Mg binding: KEEP_AS_NON_CORE (cofactor; consistent with THI6).
- GO:0004789 TMP synthase: ACCEPT, core.
- GO:0005737 cytoplasm: ACCEPT (no direct localisation evidence to refine).
- GO:0009228, GO:0009229: ACCEPT (see thiD notes on ontology relation).
