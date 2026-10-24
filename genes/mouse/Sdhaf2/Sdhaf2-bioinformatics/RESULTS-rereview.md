# Sdhaf2 re-review (2026-10-21): structural-feature mapping of A0A494B8X4

Script: `map_structure_rereview.py` (PEP 723; `uv run --script map_structure_rereview.py`).
Raw output: `RESULTS-rereview-raw.txt`. Inputs are fetched live from UniProt REST
(Q9NX18 human SDHAF2 with PDB:8DYD helix features; Q8C6I2 mouse canonical; A0A494B8X4)
and InterPro (Pfam PF03937 spans). Global alignment, BLOSUM62, gap open -10, extend -0.5.

## Identity

- A0A494B8X4 (TrEMBL, Ensembl ENSMUSP00000157391.2, 135 aa) is an alternative product of
  mouse Sdhaf2 (MGI:1913322). The reviewed canonical product is Q8C6I2 (164 aa, isoform 1).
- A0A494B8X4 is identical to Q8C6I2 over residues 1-121 and then carries an unrelated
  14-residue tail (DTPEEGVGSHCRWL) in place of canonical residues 122-164. It is not the same
  as UniProt isoform 2 (VSP_026634, tail GMPYAELHLGIIR) or isoform 3 (VSP_026633, 1-94 missing).
- Pfam PF03937 (Sdh5) spans 66-141 in Q8C6I2 but only 66-124 in A0A494B8X4.

## Human structural features mapped onto A0A494B8X4

| Human Q9NX18 feature | Human interval | Retained in A0A494B8X4? |
|---|---|---|
| Mitochondrial transit peptide | 1-29 | Yes (mouse 1-27, identical to Q8C6I2) |
| Gly78 (PPGL2 G78R abolishes SDHA binding and flavination) | 78 | Yes (mouse Gly76) |
| Helices 45-49, 51-55, 63-75, 80-93, 99-110, 115-123 | | Yes, all identical to canonical |
| Helices 127-129, 130-132 | | No |
| Helix 135-145 | | No: aligned positions are the unrelated tail (2/11 identical) |
| C-terminal helices 155-157, 158-161 | | No (2 tail residues aligned, 1 identical) |

## Interpretation (limits)

The product keeps the targeting peptide, the N-terminal helical bundle and the RGxxE /
Gly78-equivalent region, but lacks the last ~43 residues of the canonical protein, including
the helix corresponding to human 135-145 and the C-terminal helical segment annotated by UniProt from
PDB:8DYD. Whether the truncated fold is stable, whether it binds SDHA,
and whether the transcript is translated at appreciable levels were not tested here; this
analysis neither demonstrates nor excludes activity.
