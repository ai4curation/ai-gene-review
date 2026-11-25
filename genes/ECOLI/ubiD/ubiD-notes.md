# ubiD (P0AAB4, E. coli K-12) review notes

## Sources
- No deep-research provider output (provider API keys unavailable); built from UniProt, cached abstracts
  (PMID:4897112, PMID:782527, PMID:28057757), PMID:18304323 and the PTHR30108 PAINT file.

## Findings
- ubiD mutant extracts lack the activity [PMID:4897112 "Cell extracts from the mutant strain carrying the
  ubiD(-) allele lack 3-octaprenyl-4-hydroxybenzoate decarboxylase activity."]
- Native activity partly soluble, phospholipid/Mn2+ stimulated [PMID:782527 "a considerable proportion of the
  carboxylyase activity could be separated from the membrane fraction"].
- Recombinant UbiD needs reconstitution with reduced prFMN [PMID:28057757 "Formation of holoUbiD requires
  reconstitution in vitro of the apoUbiD with reduced prFMN."]; no turnover detected with tested substrates and
  the structure suggests a possible non-prenylated substrate (open question, noted in reference_review).

## Decisions
- Cytoplasm IBA (root node PTN000764648) MODIFY to cytosol (subnode PTN000764659 gives cytosol).
- Plasma membrane IEA KEEP_AS_NON_CORE (UniProt inference from the 1976 phospholipid dependence).
- Carboxy-lyase IEA MODIFY to GO:0008694.
- Mn binding, hexamerization, identical protein binding KEEP_AS_NON_CORE; prFMN binding ACCEPT.
