# CSN5 (Q9XZ58) catalytic-site and PANTHER placement check

Script: `check_csn5.py` (run with `uv run --no-project python check_csn5.py ../CSN5__Q9XZ58-uniprot.txt <repo>/.cache/panther`).
Raw output: `results.txt`. Inputs are the UniProt flat file in this folder and the PANTHER 19.0
per-organism sequence classification files.

## JAMM motif

The Q9XZ58 sequence is 327 residues. The JAMM metal ligands are intact: His135, His137 and Asp148
are present, and the motif region 135-148 reads HSHPGYGCWLSGID, matching the HxH...SxxD JAMM consensus.

## PANTHER subfamily placement

PANTHER 19.0 places Q9XZ58 in PTHR10410:SF6 (COP9 SIGNALOSOME COMPLEX SUBUNIT 5), the same subfamily
as human COPS5 (Q92905), mouse Cops5 (O35864), C. elegans csn-5 (P91001), S. pombe csn5 (O94454),
S. cerevisiae RRI1 (Q12468) and Dictyostelium csn5 (Q54PF3). The other JAMM/MPN proteins of the family
sit in different subfamilies: PSMD14 (O00487) in SF43, yeast RPN11 (P43588) in SF5, BRCC3 (P46736)
in SF34 and EIF3H (O15372) in SF3. CSN6 (Q9VCY3) is in a separate family, PTHR10540.

## Interpretation

Functions established for CSN5 orthologs in SF6 (cullin deNEDDylation within the COP9 signalosome)
can be transferred to Q9XZ58 on subfamily grounds. Functions characterised in other subfamilies,
such as the proteasomal deubiquitinase activity of PSMD14/RPN11 or the K63-specific deubiquitinase
activity of BRCC3, are not subfamily functions of CSN5 and are not transferred on this basis.
