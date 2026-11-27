# RRB1 IBA Re-review Notes

## PAINT / IBA rows

- `GO:0005730 nucleolus`: current PTHR45903 PAINT places this at `PANTHER:PTN000523093`, seeded by SGD RRB1 itself, human GRWD1 (`UniProtKB:Q9BQ67`), and an unresolved `UniProtKB:Q386K4` seed that is present in PAINT but absent from local PANTHER entry indexes. This is consistent with the cached Rpl3-chaperone literature and remains `ACCEPT` with `NO_FAILURE_CORE`.
- `GO:0042254 ribosome biogenesis`: current PTHR45903 PAINT places this at the same `PANTHER:PTN000523093` node, seeded by SGD RRB1 and human GRWD1. The broad process transfer is biologically sound but less precise than the experimental yeast evidence: Schaper et al. reported that "Impairment of Rrb1p function results in decreased levels of free 60S ribosomal subunits" [PMID:11728313]. I left the row as `MODIFY` to `GO:0042273 ribosomal large subunit biogenesis` and added `TERM_SCOPING_PROBLEM` / `GRANULARITY_MISMATCH`.

## Literature search

Searches on 2026-09-28 for `Rrb1`, `RRB1`, `YMR131C`, `Saccharomyces`, and `yeast` did not find newer direct yeast RRB1 studies from 2023-2026. The one 2020-2026 PubMed hit was Pillet et al. 2022, which extends the dedicated-chaperone model by showing that Rrb1 or Acl4 availability tunes nascent Rpl3/Rpl4 production: "the co-translational recognition of Rpl3 and Rpl4 by their respective dedicated chaperone, Rrb1 or Acl4, reduces the degradation of the encoding RPL3 and RPL4 mRNAs in the yeast Saccharomyces cerevisiae" [PMID:35357307].

## 2026-10-01 current GOA refresh

- A forced `just fetch-gene yeast RRB1 --force` left six live GOA rows. The old UniProt keyword rows for `GO:0006364 rRNA processing` and `GO:0042254 ribosome biogenesis`, three stale high-throughput `GO:0005515 protein binding` rows, and SGD's older `GO:0051082 unfolded protein binding` row are now absent from current GOA and were marked `retired: true`.
- The old `PMID:26112308` `GO:0051082` SGD row has been superseded by a live `PMID:26112308` row for `GO:0140309 unfolded protein holdase activity`. I accepted the new row and updated the stale predecessor's replacement to the same live holdase term.
- Re-reading Pausch et al. 2015 and Pillet et al. 2022 supports a focused holdase/chaperone model for Rrb1: Pausch et al. showed that "both Rrb1 and Sqt1 interact with the very N-terminal residues of Rpl3 and Rpl10, respectively" and that these dedicated chaperones can recognize nascent ribosomal-protein clients co-translationally [PMID:26112308]; Pillet et al. showed the downstream RPL3/RPL4 mRNA-control consequences of whether nascent Rpl3 and Rpl4 are captured by Rrb1 and Acl4 [PMID:35357307].
- A fresh 2026-10-01 web/PubMed search for exact yeast `RRB1` / `Rrb1` / `YMR131C` papers did not find a newer direct Saccharomyces Rrb1 study that changes the 60S/Rpl3 holdase interpretation.

## 2026-10-05 reviewer follow-up

- Changed the retired `GO:0006364 rRNA processing` row from `ACCEPT` to
  `MODIFY` with `GO:0042273 ribosomal large subunit biogenesis` as its
  replacement. Rrb1 is necessary for 25S rRNA maturation because failed Rpl3
  chaperoning blocks early 60S assembly; the gene product itself does not
  process rRNA.
- Reworded both `GO:0140309 unfolded protein holdase activity` rationales to
  rest on the carrier/delivery part of the term: Pausch et al. support Rrb1 as
  a dedicated Rpl3 holdase that can promote nuclear import and/or assembly into
  pre-ribosomal particles, not merely prevent aggregation.
