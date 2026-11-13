# hemL (P23893) notes, Escherichia coli K-12

## Sources and deep research

- Deep research was not available: the one attempted provider run for this batch
  (`just deep-research ECOLI hemA --provider perplexity`, 2026-11-10) failed with a missing
  template error ("All providers failed"), so no provider was run for hemL. No
  deep-research file exists; this review uses the UniProt record and cached abstracts.
- PMID:1643048 was missing from the cache and was fetched with `just fetch-gene-pmids`.
  PMID:2045363, PMID:1643048, PMID:15757895 and PMID:16858726 are abstract-only in the
  cache; PMID:24561554 has full text.

## Function

- hemL encodes GSA aminotransferase (GSA-AM): [PMID:2045363 "The pure protein efficiently
  converted GSA to ALA."]; mutants require ALA [PMID:2045363 "Ethylmethane
  sulfonate-induced mutants of E. coli AB354 which required ALA for growth were isolated"].
- Mechanism via PMP/PLP forms and DAVA/DOVA intermediates [PMID:1643048 "both substances are
  reaction intermediates"]; K265 is the PLP lysine (K265R mutant 2% activity, UniProt FT).
- Homodimer [PMID:2045363 "which indicates a homodimeric alpha2, structure of the protein"].
- Complex with HemA for channeling [PMID:15757895].
- Y2H hit with GlcC (P0ACL5) in the proteome-scale screen PMID:24561554; no functional
  interpretation; bare protein binding removed per policy.
- Induction by low Mg2+ via PhoQ/PhoP (UniProt, PMID:12813061, not cached; not used for GO).

## Verdict summary

- GO:0042286 (IBA, IDA x2, IEA): ACCEPT, core.
- GO:0003824 (ARBA): MODIFY -> GO:0042286.
- GO:0030170 PLP binding (IBA, IDA, IEA): KEEP_AS_NON_CORE (cofactor; same as PSEPK hemL).
- GO:0042803 homodimerization: KEEP_AS_NON_CORE.
- GO:0005829 cytosol HDA: ACCEPT; GO:0005737 cytoplasm IEA: MODIFY -> cytosol.
- GO:0006783 heme biosynthetic process (UniRule IEA), GO:0033014 (InterPro2GO): ACCEPT.
- GO:0005515 x2: REMOVE (policy).
