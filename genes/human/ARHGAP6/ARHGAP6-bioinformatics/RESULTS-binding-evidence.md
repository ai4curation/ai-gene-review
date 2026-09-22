# ARHGAP6 bioinformatics: what PMID:36115835 measured, per partner

## Question

All 22 of ARHGAP6's `GO:0005515 protein binding` rows cite
PMID:36115835. The repository's policy is that a generic `protein binding` row
should be replaced by a more informative molecular function **when the cited
paper supports one**, so the curation decision needs to know, per partner, what
that paper actually measured. Its cached full text never names ARHGAP6 -- the
interactions are in the supplementary peptide library -- so the question cannot
be answered by reading the main text.

## Method

Partner accessions come from the WITH/FROM column of the `GO:0005515` rows of
`../ARHGAP6-goa.tsv`. IntAct's curated record for each pair is then read from
its REST API and filtered to this publication, reporting the **interaction
detection method** and **interaction type** it records.

```
uv run check_binding_evidence.py
uv run check_binding_evidence.py --self-test
```

## Result (run 2026-09-20, IntAct snapshot released 2025-08-28T14:08:27.479+0000)

| partner | acc | detection method (PSI-MI) | interaction type |
|---|---|---|---|
| APBA1 | Q02410 | holdup assay (MI:2437) | direct interaction |
| APBA2 | Q99767 | holdup assay (MI:2437) | direct interaction |
| DLG1 | Q12959 | holdup assay (MI:2437) | direct interaction |
| DLG2 | Q15700 | holdup assay (MI:2437) | direct interaction |
| DLG3 | Q92796 | holdup assay (MI:2437) | direct interaction |
| DLG4 | P78352 | holdup assay (MI:2437) | direct interaction |
| FRMPD2 | Q68DX3 | holdup assay (MI:2437) | direct interaction |
| GRIP1 | Q9Y3R0 | holdup assay (MI:2437) | direct interaction |
| GRIP2 | Q9C0E4 | holdup assay (MI:2437) | direct interaction |
| IL16 | Q14005 | holdup assay (MI:2437) | direct interaction |
| LNX2 | Q8N448 | holdup assay (MI:2437) | direct interaction |
| MAGI1 | Q96QZ7 | holdup assay (MI:2437) | direct interaction |
| MAGI2 | Q86UL8 | holdup assay (MI:2437) | direct interaction |
| MAST2 | Q6P0Q8 | fps (MI:0053), holdup assay (MI:2437) | direct interaction, physical association |
| MPDZ | O75970 | holdup assay (MI:2437) | direct interaction |
| NHERF4 | Q86UT5 | holdup assay (MI:2437) | direct interaction |
| PATJ | Q8NI35 | holdup assay (MI:2437) | direct interaction |
| PDZK1 | Q5T2W1 | holdup assay (MI:2437) | direct interaction |
| SCRIB | Q14160 | holdup assay (MI:2437) | direct interaction |
| SNX27 | Q96L92 | fps (MI:0053), holdup assay (MI:2437) | direct interaction, physical association |
| TJP1 | Q07157 | holdup assay (MI:2437) | direct interaction |
| WHRN | Q9P202 | holdup assay (MI:2437) | direct interaction |

## Interpretation

**Every partner is supported by at least one direct binding measurement, and
every pair is typed `direct interaction`.** Two methods appear, and both
measure binding directly rather than inferring it from a complex:
- `fps` (MI:0053 fluorescence polarization spectroscopy)
- `holdup assay` (MI:2437 holdup assay)

The holdup assay in this paper is a chromatographic retention measurement of a
recombinant PDZome library against a library of C-terminal PDZ-binding motif
peptides. So what was measured for each partner is the affinity between that
partner's PDZ domain and ARHGAP6's C-terminal motif, not an unspecified
association.

2 partner(s) carry a second, orthogonal measurement as well: MAST2, SNX27. That is additional corroboration of the same
determinant, not a different claim -- it does not split the set.

Taken with `RESULTS-pdz-interactome.md` (all partners carry PDZ domains;
ARHGAP6 ends in `...LPETLV`, a class I motif), the informative molecular
function these rows report is **`GO:0030165 PDZ domain binding`**. That is a
restatement of the measurement, not an inference from it: no adaptor,
scaffolding or signalling role is implied, and none would be supported.

## Caveats

- IntAct's `direct interaction` type reflects the curator's reading of the assay;
  it is evidence about what was measured, not an independent replication.
- A holdup measurement is made on an isolated domain and a synthetic peptide. It
  establishes that the motif and the domain bind, not that the full-length
  proteins meet in a cell.
- This script says what kind of binding was measured. It does not weigh affinity,
  and nothing here ranks the partners.

