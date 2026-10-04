# Ugt2a1 review notes

## Re-review 2026-10-04

- GOA refresh (commit a3cf70b6d): no new rows and no retired rows; WITH/FROM
  (`supporting_entities`) and qualifiers backfilled on the 13 existing rows. 0 PENDING.
- All 13 rows re-audited (no protein-binding rows, no IBA challenges, no experimental REMOVEs).
  No actions changed (ACCEPT 6, MODIFY 4, KEEP_AS_NON_CORE 2, MARK_AS_OVER_ANNOTATED 1, REMOVE 1).
- GO:0009608 response to symbiont (ISO from human UGT2A1, UniProtKB:P0DTE4) stays REMOVE,
  but the reason and propagation_review were made source-specific. QuickGO shows the human
  donor row is IDA citing PMID:19858781 (cached, full text). That paper is a recombinant
  enzyme study: "Recombinant UGT2A1, UGT2A2 and UGT2A3 were expressed in baculovirus-infected
  insect cells and analyzed for glucuronidation activity towards different substrates"
  [PMID:19858781]. A full-text search for symbiont/bacteria/microbe/virus/infection found only
  the baculovirus expression system. Donor source_status set to UNRESOLVED (basis of the human
  row not identifiable from the cached text); PMID:19858781 added to references.
- GO:0016020 membrane rows (IEA, ISS) stay MODIFY -> GO:0060170 ciliary membrane (label
  verified in QuickGO); UniProt itself only says "Membrane" by similarity to P0DTE4, so the
  ciliary refinement rests on the immunogold EM summarized in the falcon deep research.
- Open question for a human: the human UGT2A1 IDA for GO:0009608 (PMID:19858781) has no
  evident experimental basis in the cited paper and may merit review on the human side.
