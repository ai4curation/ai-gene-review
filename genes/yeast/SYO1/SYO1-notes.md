# SYO1 curation notes

## 2026-09-29 - IBA source alignment

- Hydrated the `PTHR13347` family cache and rechecked all three SYO1 IBA rows
  against the current PAINT snapshot.
- `PTN001410872` currently carries `GO:0006606` protein import into nucleus and
  `GO:0042273` ribosomal large subunit biogenesis IBD assertions seeded by
  SGD:SYO1 and human HEATR3. These transfers are still core and supported for Syo1.
- The older `GO:0051082` unfolded protein binding IBA no longer appears on the
  current PAINT node. The row remains correctly marked `MODIFY` to the more
  informative `GO:0140597` protein carrier chaperone term because Syo1 is a
  dedicated Rpl5/Rpl11 carrier rather than a generic unfolded-protein-binding factor.
- Searched 2025-2026 PubMed and the broader web for `SYO1`, `YDL063C`,
  `Syo1`, and symportin papers. No new S. cerevisiae SYO1-specific primary paper
  superseded the cached 2012/2015/2023 5S RNP mechanistic evidence.
