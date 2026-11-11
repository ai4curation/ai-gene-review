# ttv-PC (D5SHU8) re-review analyses (2026-10-20)

New analyses written for the full re-review. They do not replace `../RESULTS.md` or `../results/`.
Sequences were downloaded from UniProt REST on 2026-10-20 and are kept here as FASTA files
(D5SHU8, Q9V730, Q16394 human EXT1, Q93063 human EXT2, Q9Y169 Sotv).

## 1. Mapping human EXT1/EXT2 GT-A residues onto ttv-PC (`map_gta_residues_rereview.py`, `results-rereview.json`)

Method: global BLOSUM62 alignment (gap open -10, gap extension -0.5; Biopython 1.85). Human residues
are mapped to full-length Ttv, and Ttv residues are then mapped to D5SHU8.

- D5SHU8 residue 1 aligns to Ttv residue 462, and identity over the whole of D5SHU8 is 100.0%. D5SHU8 is an N-terminally truncated product of the same gene. It has no residues from Ttv 1-461, which include the signal-anchor helix (7-25) and the N-terminal GT47 (GT-B) domain.
- Identity over human EXT1 GT-A (479-728) is 60.4% to Ttv and 42.0% to Sotv. This agrees with the PANTHER placement, where Ttv and human EXT1 share PTHR48261:SF3 and Sotv and human EXT2 share SF5.
- In D5SHU8, the DxD motif aligned to human EXT1 D565/D567 is D120/D122 (Ttv D581/D583). The residues aligned to human EXT1 R595 and R701 are R150 and R252.
- Human EXT1 V487 and P489 occupy the positions of the EXT2 uridine-stacking Tyr463 and phosphate-binding Arg465 (Li et al. 2023). In D5SHU8 the aligned residues are I24 and A26, so neither the aromatic nor the basic residue is present. Human EXT1 Q677 occupies the position of EXT2 K651; the aligned residue in D5SHU8 is G232. Caveat: the paper's pairing of EXT1 and EXT2 residues falls in a loop that is longer in EXT1. When this analysis aligns EXT2 directly with EXT1, EXT2 Y463 and R465 land on EXT1 491 and 493 rather than 487 and 489, so the positions in this loop carry about ±4 residues of alignment uncertainty.

Interpretation: ttv-PC keeps the conserved metal- and donor-binding core of the GT-A fold (DxD, R595, R701). At the uridine/phosphate positions, however, it has the same substitutions that distinguish the "weakly active" human EXT1 GT-A domain from the active EXT2 GT-A domain.

## 2. Hydropathy (`hydropathy_rereview.py`, `hydropathy-rereview.json`)

The script reports the highest Kyte-Doolittle mean over a 19-residue window.

- D5SHU8: the maximum is 1.12, at residues 17-35 (TAVIYVQIGAALGPNAALY).
- Q9V730 (control): the maximum is 1.58, at residues 7-25. This window coincides with the UniProt signal-anchor helix (TRANSMEM 7-25).

The control's annotated helix scores just under the classical 1.6 threshold, so the threshold alone does not discriminate here. D5SHU8 has no segment comparable to the control helix. Its most hydrophobic window falls inside the GT-A fold, and UniProt's own sequence-analysis tools annotate no transmembrane or signal feature on D5SHU8.

## Limitations

These are sequence analyses only. They do not show whether ttv-PC protein is made in vivo (UniProt PE 2, transcript level), whether it binds Sotv or Ttv, or whether it has any catalytic activity.
