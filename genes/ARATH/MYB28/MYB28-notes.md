# MYB28 review notes

- 2026-10-28: fetched Q9SPG2 (Swiss-Prot, TAIR AT5G61420, GeneID 836263) - matches requested
  accession. 21 GOA rows. No deep-research provider available; manual synthesis in
  MYB28-deep-research-manual.md.
- Core: R2R3-MYB DNA-binding transcription activator, nucleus, regulation of glucosinolate
  biosynthetic process (aliphatic, Met-derived). GO has no "positive regulation of glucosinolate
  biosynthetic process" nor an aliphatic-specific term; kept GO:0010439 and paired it with
  GO:0045893 positive regulation of DNA-templated transcription. [PMID:17420480 "PMG1/Myb28 is
  apparently a master transcription factor"]
- GO:0003700 rows MODIFIED to GO:0001216 DNA-binding transcription activator activity
  (transactivation of GSL promoters, PMID:17521412; reciprocal transactivation PMID:18042203).
- GO:0006355 IEP row (PMID:17420480): the paper actually shows MYB28 activates targets
  (knockout/overexpression), so MODIFY to GO:0045893.
- Defense/biotic rows (fungus, ISR, response to bacterium, insect) are downstream consequences of
  glucosinolate production or expression responses: kept as non-core; broad ARBA terms (response
  to stress, response to other organism) TOO_GENERAL since entailed by defense response to fungus
  / induced systemic resistance kept here.
- Sulfur deficiency direction is contradictory between PMID:17420480 (down) and PMID:23792303
  (up); keep GO:0010438 as non-core.
- Did not propose NEW defense-response-to-insect: evidence is via metabolite output
  (mutant/overexpression phenotype), fails the NEW bar.
