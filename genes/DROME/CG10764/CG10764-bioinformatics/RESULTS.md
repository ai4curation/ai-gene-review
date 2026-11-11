# CG10764 (A1ZAT2) catalytic-residue scan

Script: `catalytic_motifs.py` (stdlib only; `python3 catalytic_motifs.py`). Raw output:
`catalytic_motifs_output.txt`. Input: the UniProt flat file `../CG10764-uniprot.txt`
(523 aa; SignalP signal peptide 1-18; two PROSITE PS50240 Peptidase S1 domains, 38-265 and 274-517).

## Domain 1 (38-265): complete catalytic triad

- His: SAAHC motif, H78
- Asp: NDIGLL motif, D121
- Ser: GDSGGP motif, S214

These positions agree with the UniProt PROSITE-ProRule ACT_SITE features (78, 121, 214).
The residue six positions N-terminal to the catalytic Ser (chymotrypsin position 189 equivalent)
is D208, the S1-pocket Asp typical of trypsin-like (Arg/Lys at P1) S1A proteases. This is a
sequence-based prediction of P1 preference only; no activity or substrate has been measured.

## Domain 2 (274-517): protease-like domain, not catalytic

- No TAAHC-type His motif; the corresponding segment reads IIAAATD (residues 339-345).
- An Asp motif is present (NDIAVL, D385).
- No GDSGG-type Ser motif; the corresponding region reads VVGGMNANG (474-482).

Lacking both His and Ser of the triad, domain 2 cannot be a catalytically active serine
protease domain. This agrees with PMID:30367934, which classifies SP77 (CG10764) among
proteins that "contain a PD and a PLD".

## Limitations

Motif scanning by regular expressions; no structural model or alignment to a reference
chymotrypsin was used, so the exact aligned positions in domain 2 are approximate.
