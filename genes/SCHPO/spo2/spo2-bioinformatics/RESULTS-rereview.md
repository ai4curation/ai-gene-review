# Spo2 (C6Y4C2) vs Vps1302 (O42926): sequence placement and signatures (re-review, 2026-10-21)

Script: `compare_vps1302_rereview.py` (run with `uv run --script compare_vps1302_rereview.py`; queries UniProt REST FASTA and the InterPro API live).

## Output

```
Spo2 length: 133; Vps1302 length: 3131
Spo2 is identical to Vps1302 residues 2999-3131
Vps1302 residue preceding the Spo2 Met: I2998

Spo2 (C6Y4C2) signatures:
  none

Vps1302 (O42926) signatures (overlap with Spo2 segment marked):
  IPR017148	interpro	1-3042	overlap_with_spo2=44	Vacuolar protein sorting-associated protein 13, fungi
  IPR026847	interpro	1-2938	overlap_with_spo2=0	Vacuolar protein sorting-associated protein 13
  IPR026854	interpro	1-819	overlap_with_spo2=0	Vacuolar protein sorting-associated protein 13, N-terminal domain
  PF12624	pfam	1-819	overlap_with_spo2=0	VPS13-like family N-terminal region
  PIRSF037235	pirsf	1-3042	overlap_with_spo2=44	Vacuolar protein sorting-associated protein Vps13, fungal type
  PTHR16166	panther	1-2938	overlap_with_spo2=0	VACUOLAR PROTEIN SORTING-ASSOCIATED PROTEIN VPS13
  IPR056747	interpro	986-1755	overlap_with_spo2=0	VPS13-like, middle region
  PF25033	pfam	986-1755	overlap_with_spo2=0	VPS13-like family middle region
  IPR009543	interpro	1790-2363	overlap_with_spo2=0	Vacuolar protein sorting-associated protein 13, VPS13 adaptor binding domain
  PF25036	pfam	1790-2363	overlap_with_spo2=0	Vacuolar-sorting associated protein 13, adaptor binding domain
  IPR056748	interpro	2872-2938	overlap_with_spo2=0	Intermembrane lipid transfer protein VPS13-like, C-terminal
  PF25037	pfam	2872-2938	overlap_with_spo2=0	Intermembrane lipid transfer protein VPS13, C-terminal
```

## Interpretation

- All 133 Spo2 residues are identical to the last 133 residues of the Vps1302 gene model (2999-3131); Spo2 Met1 corresponds to Vps1302 Met2999.
- Spo2 itself matches no InterPro, Pfam or PANTHER signature.
- None of the VPS13 domain signatures (N-terminal chorein region, middle region, adaptor-binding domain, C-terminal region, PTHR16166 span) overlaps the Spo2 segment. The only overlap is with the whole-protein fungal-Vps13 family spans (IPR017148/PIRSF037235, 1-3042), by 44 residues at the Spo2 N-terminus.
- The "Belongs to the VPS13 family" similarity line on C6Y4C2 therefore reflects identity with the 3' end of the overlapping vps1302 gene model, not possession of any VPS13 lipid-transfer module. No VPS13-family function (lipid transfer, membrane-contact bridging) can be transferred to Spo2 on this basis.
- Whether the vps1302 gene model correctly extends through the spo2 coding region, or the spo2 product is an independently initiated transcript nested in the vps1302 3' end (as the 2008 cDNA analysis reported, per the Falcon summary of the full text), is a gene-model question this analysis cannot resolve.
