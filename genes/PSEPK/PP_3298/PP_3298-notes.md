# PP_3298 curation notes

## 2026-07-20

- Target identity: PP_3298 / UniProtKB Q88HQ5, an unreviewed 167-aa protein
  submitted only as a CinA domain protein [UniProtKB:Q88HQ5, "SubName:
  Full=CinA domain protein"].
- Domain evidence: the target carries IPR036653, IPR008136, PF02464, and
  TIGR00199 [UniProtKB:Q88HQ5, "NCBIfam; TIGR00199; PncC_domain; 1."]. The
  local KT2440 partition places it in `orphan:domain_only_no_pathway`, so it was
  added as a manual pathway hole-fill rather than recovered from ppu00760.
- Annotation evidence: the fetched GOA file contains no annotation rows, and
  the UniProt record supplies no EC assignment, catalytic function statement,
  or PncC/NMN-amidohydrolase protein name.
- Paralog comparison: Q88ME5/pncC has the same compact family architecture but
  is specifically submitted as NMN amidohydrolase with EC 3.5.1.42 and
  GO:0019159. Those target-specific assignments are absent from Q88HQ5 and are
  not transferred here.
- Family caution: characterized bacterial PncC proteins establish that the
  family can deamidate NMN, but the same study explicitly reports inactive
  family members [PMID:21953451, "The PncC family also comprises a few members
  with a nonfunctional PncC domain, bearing multiple mutations and
  deletions."].
- Curation decision: include PP_3298 in the batch and module knowledge gap as
  an unresolved CinA-C/PncC-family paralog. Do not place it in the catalytic
  module graph, assign GO:0019159, or describe it as an NMN deamidase without
  specificity evidence.
- OpenScientist retrieval required a bounded retry: the initial
  `max_iterations=3` job timed out at the provider's 7200-second ceiling
  without a report, while the `max_iterations=2` retry completed in 5155
  seconds with both artifacts. The final report promotes NMN deamidase,
  cytoplasmic localization, and pathway physiology from a provider-computed
  38.1% alignment, an asserted motif, and negative neighborhood context, but no
  alignment or query artifact was retained. It also acknowledges that Q88HQ5
  has no direct experiment, homology is moderate, family members can be
  inactive, and substrate specificity is untested
  [file:PSEPK/PP_3298/PP_3298-deep-research-openscientist.md, "No direct
  experimental characterization of PP_3298."]. It does not compare Q88ME5/pncC,
  the better-annotated paralog in the same proteome. The stronger assignment is
  therefore rejected pending a direct product-forming specificity assay.
