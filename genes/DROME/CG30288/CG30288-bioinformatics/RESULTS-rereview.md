# CG30288 (Q8IRK6) sequence checks, re-review 2026-10-21

Script: `sequence_features_rereview.py`, run on the cached `CG30288-uniprot.txt` (282 aa, sequence version 2). No external tools, no alignment; positions come from the UniProt feature table, and residues are read off the sequence.

## Output

```
length	282
act_site	83	H	context=VLTAEHCISPM
act_site	132	D	context=SNPGYDIGLLR
act_site	225	S	context=SCKGDSGGPLS
ser195_segment	219-228	DSCKGDSGGP
S1_pocket_pos189	219	D
activation_site	42-43	R-|-IDGG
propeptide	24-42	length=19	GRLLENDCGTTSSNGYRAR
cysteines	13,31,68,84,106,111,152,199,212,221,254
```

## Interpretation

- The catalytic triad is intact: His83 (TAEHC), Asp132 and Ser225 in the canonical GDSGGP motif.
- The residue six positions N-terminal of the catalytic serine, at the position of chymotrypsinogen Asp189 at the base of the S1 pocket, is Asp219 (segment DSCKGDSGGP). An Asp at this position is the classical trypsin-like determinant, which favours Arg/Lys at P1. This argues against the chymotrypsin (EC 3.4.21.1) name, which comes from a PROSITE-ProRule assignment and not from a measurement. The inference is from one residue; specificity was not measured.
- The protease domain begins with IDGG, preceded by Arg42. This is a predicted zymogen activation site cleaved after Arg, i.e. by a trypsin-like protease.
- The propeptide between the signal peptide (1-23) and the protease domain (from 43) is only 19 residues long. That is too short for a clip domain (about 35-55 residues, three disulfides), so CG30288 has a single protease domain and is not a CLIP-domain protease. This disagrees with UniProt's ARBA-only statement "CLIP subfamily". Cys31 in the propeptide could form the chymotrypsinogen-type Cys1-Cys122 interchain bond (candidate partner Cys152); this connectivity is not verified.
