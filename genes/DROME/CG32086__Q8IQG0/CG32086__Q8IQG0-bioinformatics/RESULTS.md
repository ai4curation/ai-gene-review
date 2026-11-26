# CG32086-RA (Q8IQG0): EF-hand loop and GFG-motif analysis

Date: 2026-10-21. Script: `gfg_motif_scan.py` (run with `uv run gfg_motif_scan.py`); raw output in
`gfg_motif_scan-output.txt`. Sequences are fetched live from UniProt REST. Family placement, isoform
identity and local alignments for this gene were analysed earlier in
`genes/DROME/CG32086/CG32086-bioinformatics/RESULTS-rereview.md` and are not repeated here.

## 1. Sequences

| Accession | Length | Note |
|---|---|---|
| Q8IQG0 | 491 | fly CG32086-RA, PTHR12086:SF12 |
| Q8N7U6 | 833 | human EFHB/CFAP21, PTHR12086:SF12 |
| Q7KUG5 | 497 | fly FBgn0053489, PTHR12086:SF12 |
| Q8MST3 | 530 | fly FBgn0053490, PTHR12086:SF12 |

## 2. EF-hand calcium-binding loop

PROSITE PS00018 matches: human EFHB has one, at 610 (DVDNDGFINYLE). Q8IQG0 and the two fly SF12 paralogs
have none.

A global alignment of Q8IQG0 to human EFHB (BLOSUM62, gap open -11, extend -1, free end gaps) aligns the
whole fly protein (1-491) to human 248-739, with 28% identity over 447 aligned pairs. At the human canonical
loop the aligned fly residues are:

| Loop position | Human (residue) | Fly (residue) |
|---|---|---|
| 1 (ligand) | D610 | L340 |
| 3 (ligand) | D612 | V342 |
| 5 (ligand) | D614 | E344 |
| 7 (ligand) | F616 (backbone) | C346 |
| 9 (ligand) | N618 | N352 (after a 4-residue fly insertion) |
| 12 (ligand) | E621 | D355 |

In the fly protein the loop's first and third positions are not acidic (Leu and Val instead of Asp and Asp),
the glutamate at position 12, the bidentate ligand of canonical EF-hands, is aspartate, and an insertion
interrupts the loop. So the fly protein does not keep the calcium-binding loop that human EFHB has. This
removes the sequence basis for transferring calcium-sensor activity to it. It does not show that the protein
binds no metal: non-canonical loops exist, and the Pfam PF25325 domain fold is retained.

## 3. GFG motif

PMID:38538594 named a glycine-phenylalanine-glycine (GFG) signature for the microtubule-binding repeats of
Chlamydomonas FAP21 and human EFHB. The script finds no contiguous GFG, or looser G-[FYW]-G, tripeptide in
any of the four sequences, including human EFHB. In the published alignment the signature residues are
therefore not a contiguous tripeptide, and a tripeptide scan cannot test whether the fly protein keeps GFG
repeats. **This part of the analysis is inconclusive**, and nothing in this review relies on it.

## Conclusion

Q8IQG0 lacks the one canonical calcium-binding EF-hand loop of human EFHB. Its first and third
coordinating aspartates are replaced by hydrophobic residues and the loop carries an insertion. This argues
against propagating the calcium-sensor activity of human EFHB to the fly protein. Whether the fly protein
keeps the GFG microtubule-binding repeats was not settled by this sequence-motif scan.
