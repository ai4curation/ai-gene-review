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
