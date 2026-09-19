# ARHGAP6 bioinformatics: are the 22 `protein binding` rows 22 findings or one?

## Question

Half of ARHGAP6's GOA rows (22 of 44) are `GO:0005515 protein binding`
(IPI) from a single reference. Treating them as that many independent findings
would overstate the evidence. The testable alternative -- that they report **one**
binding determinant -- predicts that every partner is a PDZ-domain protein and
that ARHGAP6's C-terminus is a PDZ-binding motif.

## Method

Partner accessions are parsed from the WITH/FROM column of the
`GO:0005515` rows of `../ARHGAP6-goa.tsv` (the repository's own GOA download),
not typed into the script. Each is then checked for PDZ domains by two
independent signals: UniProt `Domain` features naming PDZ, and the InterPro
cross-reference `IPR001478`. The target's C-terminal residues are read from its
UniProt sequence and classified by the stated rule below.

Class rule, stated so the call is auditable: a C-terminal **class I** PDZ-binding
motif is `-X-S/T-X-phi-COOH` -- serine or threonine at position -2, hydrophobic
residue at position 0.

```
uv run check_pdz_interactome.py
uv run check_pdz_interactome.py --self-test
```

## Result (run 2026-09-18)

**ARHGAP6 (O43182) C-terminus: `...LPETLV`** -- class I motif by the rule above: **yes** (position -2 = `T`, position 0 = `V`).

Partners parsed from the GOA file: **22**. Carrying at least one PDZ domain: **22**.

| partner | acc | PDZ `Domain` features | InterPro IPR001478 |
|---|---|---|---|
| APBA1 | Q02410 | 2 | yes |
| APBA2 | Q99767 | 2 | yes |
| DLG1 | Q12959 | 3 | yes |
| DLG2 | Q15700 | 3 | yes |
| DLG3 | Q92796 | 3 | yes |
| DLG4 | P78352 | 3 | yes |
| FRMPD2 | Q68DX3 | 3 | yes |
| GRIP1 | Q9Y3R0 | 7 | yes |
| GRIP2 | Q9C0E4 | 7 | yes |
| IL16 | Q14005 | 4 | yes |
| LNX2 | Q8N448 | 4 | yes |
| MAGI1 | Q96QZ7 | 6 | yes |
| MAGI2 | Q86UL8 | 6 | yes |
| MAST2 | Q6P0Q8 | 1 | yes |
| MPDZ | O75970 | 13 | yes |
| NHERF4 | Q86UT5 | 4 | yes |
| PATJ | Q8NI35 | 10 | yes |
| PDZK1 | Q5T2W1 | 4 | yes |
| SCRIB | Q14160 | 4 | yes |
| SNX27 | Q96L92 | 1 | yes |
| TJP1 | Q07157 | 3 | yes |
| WHRN | Q9P202 | 3 | yes |

## Interpretation

**Every one of the 22 partners is a PDZ-domain protein**, and
ARHGAP6 ends in a canonical class I PDZ-binding motif. The 22 GOA rows
are therefore one binding determinant reported 22 times, not 22 independent
interactions -- and they came from one assay in one paper.

For curation this bears on how much the rows are worth, not on whether they are
true. They are real measurements. But `protein binding` is the least informative
molecular-function term available, the partners are scaffolds rather than
substrates, and nothing in the set speaks to what ARHGAP6 *does*. They belong in
the review as non-core.

## Caveats

- A shared binding determinant is not evidence that the interactions are
  biologically equivalent: affinity, expression overlap and localisation differ
  between partners, and none of that is examined here.
- PDZ-domain content is a property of the partners. That the assay recovered only
  PDZ proteins may reflect the assay's design rather than ARHGAP6's selectivity;
  this script cannot distinguish those and does not try.
- The motif class rule is the textbook one. A C-terminal sequence matching it is
  a *candidate* ligand; this is sequence evidence, not a binding measurement.

