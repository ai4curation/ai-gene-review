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
  (Updated 2026-10-17: the primary immunolocalization source is now cited directly —
  see the Review follow-up below.)
- Open question for a human: the human UGT2A1 IDA for GO:0009608 (PMID:19858781) has no
  evident experimental basis in the cited paper and may merit review on the human side.

**Stale UniProt quotes (2026-10-10):** replaced 10 `UniProtKB:P36510` supporting_text quotes (an abridged FUNCTION text no longer in the refreshed flat file) with verbatim sentences from the current FUNCTION comment in `Ugt2a1-uniprot.txt`, matched to each row (glucuronidation, xenobiotic detoxification, bile acid detoxification, olfaction).

## Review follow-up 2026-10-17

Addressed PR #4615 reviewer finding (IMPORTANT 2). The two GO:0016020 -> GO:0060170
ciliary membrane MODIFY rows previously rested only on a file: deep-research quote. Added
the primary immunolocalization source PMID:33765098 (Neiers et al., PLoS One 2021,
"The odorant metabolizing enzyme UGT2A1: Immunolocalization and impact of the modulation
of its activity on the olfactory response"; PMID verified against PubMed, full text fetched
from PMC7993815) to references with a reference_review and to both rows' supported_by, with
a verbatim immunogold-EM localization quote. Added a topology caveat to both review.reason
blocks noting that UGT family enzymes are canonically type-I ER membrane proteins with a
lumen-facing catalytic domain, so the olfactory-ciliary plasma-membrane assignment is the
non-default claim and rests on this single immunolocalization study. Action unchanged
(MODIFY). Revalidated and re-rendered.

Update (2026-10-17, re-review follow-up 2): PMID:33765098 reports a second location
besides the olfactory-ciliary plasma membrane - the endoplasmic reticulum of the
sustentacular cells (its S1 Fig immunogold EM). Per the "list all supported specific
descendants" guidance, added GO:0005789 endoplasmic reticulum membrane (QuickGO-verified
label; is_a descendant of GO:0016020) as a second proposed_replacement_term on both
GO:0016020 MODIFY rows, with the verbatim ER sentence in supported_by. Adjusted both
reason blocks so the ER pool (the canonical, expected UGT location) discharges the
type-I ER membrane topology caveat, leaving only the ciliary plasma-membrane pool as the
non-default claim.
