# RRB1 IBA Re-review Notes

## PAINT / IBA rows

- `GO:0005730 nucleolus`: current PTHR45903 PAINT places this at `PANTHER:PTN000523093`, seeded by SGD RRB1 itself, human GRWD1 (`UniProtKB:Q9BQ67`), and an unresolved `UniProtKB:Q386K4` seed that is present in PAINT but absent from local PANTHER entry indexes. This is consistent with the cached Rpl3-chaperone literature and remains `ACCEPT` with `NO_FAILURE_CORE`.
- `GO:0042254 ribosome biogenesis`: current PTHR45903 PAINT places this at the same `PANTHER:PTN000523093` node, seeded by SGD RRB1 and human GRWD1. The broad process transfer is biologically sound but less precise than the experimental yeast evidence: Schaper et al. reported that "Impairment of Rrb1p function results in decreased levels of free 60S ribosomal subunits" [PMID:11728313]. I left the row as `MODIFY` to `GO:0042273 ribosomal large subunit biogenesis` and added `TERM_SCOPING_PROBLEM` / `GRANULARITY_MISMATCH`.

## Literature search

Searches on 2026-09-28 for `Rrb1`, `RRB1`, `YMR131C`, `Saccharomyces`, and `yeast` did not find newer direct yeast RRB1 studies from 2023-2026. The one 2020-2026 PubMed hit was Pillet et al. 2022, which extends the dedicated-chaperone model by showing that Rrb1 or Acl4 availability tunes nascent Rpl3/Rpl4 production: "the co-translational recognition of Rpl3 and Rpl4 by their respective dedicated chaperone, Rrb1 or Acl4, reduces the degradation of the encoding RPL3 and RPL4 mRNAs in the yeast Saccharomyces cerevisiae" [PMID:35357307].
