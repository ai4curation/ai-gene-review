# YDJ1 review notes

## 2026-08-28 completion audit

- YDJ1 encodes a type-I DnaJ/Hsp40 co-chaperone whose defining molecular
  function is stimulation of the Ssa1 Hsp70 ATPase cycle [PMID:1400408, “We
  report that a purified cytoplasmic Hsp70 homolog from Saccharomyces cerevisiae,
  Hsp70SSA1, exhibits a weak ATPase activity, which is stimulated by a purified
  eukaryotic dnaJp homolog (YDJ1p).”]. The InterPro-derived ATP
  binding annotation is therefore removed: Ydj1 activates its Hsp70 partner but
  has no ATP-binding/ATPase domain of its own.

- All 49 unique nonredundant GOA signatures were reconciled exactly by GO term,
  evidence, reference, and relation qualifier. The 62 physical GOA rows collapse
  to 49 signatures because high-throughput `protein binding` annotations repeat
  the same assertions for multiple WITH/FROM partners. All eight generic protein
  binding signatures remain marked over-annotated; specific Hsp70/heat-shock
  protein binding terms capture the informative partner biology.

- All six IBA annotations were reviewed from their GOA WITH/FROM provenance.
  Cytosol, cellular response to heat, protein refolding, and obsolete unfolded
  protein binding use PTN001531327; ATPase activator activity uses PTN002376157;
  nucleus uses PTN001180221. YDJ1 is an experimental descendant source at the
  first two nodes, which is valid PAINT grounding rather than circular evidence.
  The SGD:S000005021 source at PTN001531327 and PTN001180221 is APJ1, a
  class-A/type-I Ydj1 paralog, not SIS1.
  The current local PTHR44298 PAINT table retains PTN002376157, while the other
  node identifiers remain recoverable from current GOA WITH/FROM rows.

- GO:0051082 is obsolete in live GO. For Ydj1, replacement by GO:0044183 protein
  folding chaperone is evidence-matched: the direct study found both suppression
  of thermally induced luciferase aggregation and productive Ssa1-dependent
  refolding [PMID:9774392, “Ydj1:Ssa1 could promote up to four times more
  luciferase folding than Sis1:Ssa1.”]. All three GO:0051082 assertions are
  therefore consistently modified to GO:0044183.

- The CAFA-assigned IDA `chaperone-mediated protein complex assembly` row has
  empty WITH/FROM and cites an abstract-only human p23 paper [PMID:10811660].
  The abstract demonstrates p23 chaperoning of progesterone receptor but no
  direct YDJ1 assay, so the row is marked over-annotated rather than treated as
  MOD-curated evidence or labelled a wrong-identifier citation.

- Ydj1's heat-stress quality-control role is directly supported in full text
  [PMID:25344756, “We found that ubiquitylation of heat-induced substrates
  requires the Hsp40 co-chaperone Ydj1 that is further associated with Rsp5 upon
  heat shock.”].
  ERAD and protein targeting to ER are retained as important cellular functions;
  HAP1 regulation, oxygen response, starvation-linked tRNA import, nuclear
  localization, and broad protein transport are retained as specialized non-core
  uses of the central Hsp70 co-chaperone machinery. TRC membership is marked
  over-annotated because upstream cascade participation does not establish stable
  incorporation into the Get4-Get5/Mdy2 complex.

- Most older supporting publications in the cache are abstract-only. Their
  experimental annotations were not overruled when the abstract lacked assay
  detail. Full text is locally available for PMID:19536198, PMID:23217712,
  PMID:25344756, PMID:25853343, PMID:26928762, and PMID:37968396.
