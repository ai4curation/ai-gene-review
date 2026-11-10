# PGR3 (Q9SZ52) curation notes

## 2026-10-28 session
- fetch-gene resolved Q9SZ52 (TAIR AT4G31850, GeneID 829314); 7 GOA rows.
- Literature: see PGR3-deep-research-manual.md (hand-written; no deep-research API).
- Full text read: PMID:30125002 (Rojas 2018), PMID:22156165 (Zhelyazkova 2012),
  PMID:32344669 (RIC). Abstract only: PMID:15053768, 21457370, 23975900, 33439244.
- PMID:33431870 (NOT4A/PGR3) is retracted - do not use.

### Decisions
- mRNA binding (IBA, IDA): ACCEPT. Each row is as precise as its own evidence (family
  IBD; poly(A) interactome capture). The specific activity, mRNA 5'-UTR binding, is added
  as NEW (IDA, PMID:21457370 recombinant protein binding to petL 5' UTR
  [PMID:21457370 "these putative elements
were recognized by recombinant PGR3 in vitro"]; PMID:33439244 petL/ndhG 5' UTR binding).
- RNA stabilization -> MODIFY to mRNA stabilization (petL operon mRNA; rpl16-rpl14 3' end).
- translation / plastid translation (acts_upstream_of_or_within) -> MODIFY to positive
  regulation of translation; PGR3 activates translation of petL, ndhG, rps8 by binding
  their 5' UTRs; it is not a component of the translation machinery. The general plastid
  ribosome deficit is attributed to reduced rpl14/rps8 expression (Rojas 2018). Not an
  upstream error (qualifier is acts_upstream_of_or_within), so no source_defects.
- chloroplast IEA: ACCEPT (transit peptide + functions on plastid RNAs + maize ortholog in
  stroma). Added NEW chloroplast stroma (IC): Zm-PGR3 RIP from stromal extract, no TM
  segment, acts on stromal mRNAs/ribosomes.
- ND cellular_component -> MODIFY to chloroplast.
- No NEW BP terms proposed.
