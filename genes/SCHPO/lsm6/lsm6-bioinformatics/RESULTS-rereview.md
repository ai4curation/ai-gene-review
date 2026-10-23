# lsm6 (Q9UUI1) re-review: composition of the PMID:26292707 spliceosome structure

Script: `check_3jb9_composition.py` (run with `uv run --script check_3jb9_composition.py`,
2026-10-21; raw output in `check_3jb9_composition.out`). It queries live UniProt REST for
every entry cross-referencing PDB 3JB9 (the S. pombe spliceosome model of Yan et al. 2015,
PMID:26292707) and QuickGO for annotations citing PMID:26292707 on lsm6 and on the
canonical Sm-ring proteins.

## Results

- 27 UniProt entries cross-reference PDB 3JB9. They include all seven canonical Sm-ring
  proteins (smb1, smd1, smd2, smd3, sme1, smf1, smg1) and U2 snRNP proteins (lea1, msl1).
- Q9UUI1 (lsm6) in 3JB9: False. No Lsm-named protein is among the 3JB9 entries.
- The UniProt entry for Q9UUI1 lists PDB 3SWN, 4EMK, 6PPN, 6PPP, 6PPQ and 6PPV (Lsm
  ring structures) and no spliceosome structure.
- QuickGO: lsm6 carries three PomBase annotations citing PMID:26292707 (GO:0030620 U2
  snRNA binding IDA; GO:0005682 U5 snRNP IDA; GO:0005686 U2 snRNP EXP). smf1 (O59734, the
  SmF paralog in the same PANTHER family PTHR11021, subfamily distinct from Lsm6 SF1) and
  smb1, smg1, sme1 carry none.

## Interpretation

The deposited model of the paper behind the three U2/U5 annotations contains SmF (smf1)
but not Lsm6, and no Lsm2-8 subunit. The U2/U5 Sm rings described in the paper are the
canonical SmB/D1/D2/D3/E/F/G rings. The annotations on lsm6 are therefore probably
attached to the wrong gene product; smf1 (SmF) is the most likely intended target,
because SmF and Lsm6 belong to the same SmF/LSm6 family. This is a query for PomBase,
not a certainty: the curator may have used information not visible in the deposited model.
