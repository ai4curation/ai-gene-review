# Efr3a (mouse, Q8BG67) sequence comparison

Script: `compare_sequences.py` (run with `uv run python compare_sequences.py`);
raw output in `compare_sequences_output.txt`. Sequences and PANTHER
cross-references are fetched live from UniProt REST.

## Family placement

- Q8BG67 mouse Efr3a: PANTHER PTHR12444:SF1 (PROTEIN EFR3 HOMOLOG A)
- Q14156 human EFR3A: PANTHER PTHR12444:SF1, the same subfamily as mouse Efr3a
- Q6ZQ18 mouse Efr3b: PANTHER PTHR12444:SF4 (paralog subfamily)
- Q15517 human CDSN (corneodesmosin): PANTHER PTHR23207, an unrelated family

## Identity to mouse Efr3a (global alignment, % of shorter sequence)

- human EFR3A: 97.3% identity, 819 aligned positions
- mouse Efr3b: 63.2% identity
- human CDSN: 22.5% identity, which is background level for a global alignment against a low-complexity Gly/Ser-rich protein

## Residues tested experimentally on the mouse protein

- Residues 6-9 of Q8BG67 are CCCC, the palmitoylated cysteine cluster mutated (C6S/C7S/C8S/C9S) in mouse EFR3A constructs by Nakatsu et al. 2012 (PMID:23229899).
- K50, R53, R61, R68 and R70 are all present in Q8BG67, matching the basic-patch quintuple mutant of murine EFR3A-GFP made by Wu et al. 2014 (PMID:24360784).

## Interpretation

Mouse Efr3a and human EFR3A are orthologs in the same PANTHER subfamily and are near-identical, so the human structural and recruitment data can be transferred.

Human CDSN is in a different PANTHER family with no detectable relationship to Efr3a; GO terms transferred from CDSN to Efr3a have no evolutionary basis.
