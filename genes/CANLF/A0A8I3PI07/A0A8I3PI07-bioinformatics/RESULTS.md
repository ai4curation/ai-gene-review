# A0A8I3PI07 (dog CNNM4) — sequence comparison with human CNNM4

Script: `compare_to_human_mouse_cnnm4.py` (Biopython global alignment, BLOSUM62,
gap open -10 / extend -0.5), reading sequences from the cached UniProt flat
files in this repository. Raw output: `alignment_output.txt`.

## Results

- Dog A0A8I3PI07 is 796 aa; human CNNM4 (Q6P4Q7, Swiss-Prot canonical) is 775 aa.
- Dog vs human CNNM4: identity 0.926 over 775 aligned columns (similarity 0.961).
- Dog vs human CNNM2 (Q9H8M5): identity 0.659 over 781 aligned columns, so the
  target is a CNNM4 ortholog rather than a CNNM2-like paralog.
- Relative to human CNNM4 the dog model carries two insertions totalling ~21 aa
  near target positions ~645-670 (3 aa and 18 aa), in the C-terminal region after
  the CBS pair; no other gap block of 3 or more residues. The signal peptide,
  four-helix CNNM transmembrane domain (178..358) and the CBS pair are present.

## Interpretation

The benchmark accession is a full-length CNNM4 gene model, not a fragment. The
extra ~21 residues lie outside the transport and MgATP-binding regions and may
reflect an alternative exon or a dog-specific insertion; this analysis cannot
tell which. PANTHER places the protein in PTHR12064:SF26 (METAL TRANSPORTER
CNNM4), the same subfamily as human Q6P4Q7 and mouse Q69ZF7.
