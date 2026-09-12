# FBL22 re-review notes

## 2026-09-11 — evidence and annotation audit

Reviewed all four annotation rows, the UniProt record, both original PMID records,
the existing Falcon report, and the primary source underlying its expression claim.

- **SCF binding (IBA): ACCEPT.** The phylogenetic assertion is compatible with
  the observed F-box/LRR architecture. UniProt Q9M0U6 records `FT   DOMAIN          24..71`
  with F-box as its note, five LRRs and `PE   4: Predicted;`
  ([local record](FBL22-uniprot.txt)). These are computational protein features,
  not a direct interaction assay. The retained IBA is not being replaced by a
  donor-count argument or an invented PAINT node assertion.
- **Nucleus (ISM): UNDECIDED.** AtSubP is a prediction, and the sources examined do
  not establish the location of FBL22. No compartment was added to core functions.
- **Protein catabolism (two TAS rows): REMOVE → UNDECIDED.** The previous review
  exceeded accessible evidence. [PMID:11019805, *Protein degradation in signaling*](https://pubmed.ncbi.nlm.nih.gov/11019805/)
  has an abstract discussing plant proteolysis, but accessible material does not
  adjudicate the source-specific FBL22 assignment. [PMID:11077244, *F-box proteins
  in Arabidopsis*](https://pubmed.ncbi.nlm.nih.gov/11077244/) has no abstract in
  PubMed. Publisher retrieval for both papers returned HTTP 403. The absence of
  accessible gene-specific evidence does not establish a false annotation.
  Removed paper-title quotations that had been presented as mechanistic support.
- **Expression context checked against the primary source.**
  [PMID:19168643, *Nitric oxide contributes to cadmium toxicity in Arabidopsis…*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2649387/)
  identifies At4g05490/FBL22 in the Results subsection describing class I
  NO-regulated genes: “All of these genes are up-regulated through NO”.
  This is transcript evidence. It does not demonstrate a FBL22 catalytic assay,
  substrate, or stress-tolerance phenotype, so no additional GO function was added.
  The automated cache fetch obtained only the abstract; the online PMC full text
  was accessible through the alternate `/articles/2649387/` URL. The short excerpt
  is recorded here rather than misrepresented as text present in the local cache.
- **Core synthesis.** Retained one predicted SCF-binding function; removed the
  implication that an expression change establishes stress-responsive proteolysis.
  Kept SCF assembly, localization, substrates and genetics as explicit experimental
  hypotheses. Removed unverified claims that named F-box proteins share the same
  PANTHER subfamily.

QuickGO definitions for GO:1905761, GO:0006511 and GO:0005634 were retrieved through
its ontology API on this date. Existing source IDs, terms and evidence codes were
preserved. No new GO IDs were assigned.

Publication caching completed for both original PMIDs; PMID:19168643 was fetched
through the repository CLI. A Falcon refresh with perplexity-lite fallback was
launched concurrently with caching; its outcome will be appended below. Low
compliance caused by unavailable quotations is intentionally left visible.

Independent annotation-reviewer consultation agreed with all four decisions and
the conservative core synthesis. Its evidence-presentation suggestion was applied:
the UniProt domain excerpt now includes the adjacent F-box identity, not only the
residue coordinates.

The fresh Falcon report completed successfully (474.56 seconds; no fallback was
needed). Its evidence assessment agrees with the retained domain-based hypothesis
and the limits of the 2009 expression result. The report also identifies a nearby
2026 suberization GWAS lead, explicitly without FBL22-specific causal validation;
that secondary lead was not promoted to a functional annotation. An exact excerpt
from the refreshed report now supports the qualified core synthesis. Final gene
and history validation passed; the review HTML was regenerated.
