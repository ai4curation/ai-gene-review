# SYO1 curation notes

## 2026-09-29 - IBA source alignment

- Hydrated the `PTHR13347` family cache and rechecked all three SYO1 IBA rows
  against the current PAINT snapshot.
- `PTN001410872` currently carries `GO:0006606` protein import into nucleus and
  `GO:0042273` ribosomal large subunit biogenesis IBD assertions seeded by
  SGD:SYO1 and human HEATR3. These transfers are still core and supported for Syo1.
- The older `GO:0051082` unfolded protein binding IBA no longer appears on the
  current PAINT node after GO:0051082 was obsoleted. The row remains correctly
  marked `MODIFY` to the more informative `GO:0140597` protein carrier chaperone
  term because Syo1 is a dedicated Rpl5/Rpl11 carrier rather than a generic
  unfolded-protein-binding factor.
- Searched 2025-2026 PubMed and the broader web for `SYO1`, `YDL063C`,
  `Syo1`, and symportin papers. No new S. cerevisiae SYO1-specific primary paper
  superseded the cached 2012/2015/2023 5S RNP mechanistic evidence.

## 2026-10-01 - current GOA refresh

- Force-refreshed `SYO1` against current UniProt and GOA. The live GOA snapshot has
  9 rows; all are represented in the YAML. Four older exact source assertions are
  no longer live and were preserved with `retired: true`: the stale `GO:0051082`
  IBA, the broad UniProt-keyword `protein transport` and `ribosome biogenesis`
  rows, and the obsolete `GO:0051082` direct SGD row from Pausch 2015.
- Reviewed the newly seeded `GO:0140309` unfolded protein holdase activity row
  from PMID:26112308. It is a sound SGD replacement for the obsolete
  unfolded-protein-binding row, but the row remains a `MODIFY` because Syo1's
  more specific molecular function is `GO:0140597` protein carrier chaperone for
  the defined Rpl5/Rpl11 cargo pair.
- Rechecked `PTHR13347`: current PAINT still has only `GO:0006606` protein import
  into nucleus and `GO:0042273` ribosomal large subunit biogenesis on
  `PTN001410872`, seeded by yeast SYO1 and human HEATR3. No new PAINT assertion
  replaced the stale obsolete `GO:0051082` IBA row.
- Searched for newer 2025-2026 Syo1/HEATR3 and 5S RNP papers. A 2026 review
  reiterates the conserved Syo1/HEATR3 role but does not change the direct
  yeast calls already supported by the cached 2012, 2015, and 2023 papers.
