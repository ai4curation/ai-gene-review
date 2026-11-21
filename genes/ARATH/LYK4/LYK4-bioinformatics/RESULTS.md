# LYK4 kinase-domain residue check against CERK1

**Question.** The review removes electronic protein kinase annotations because LYK4 "lacks key
catalytic residues". Which residues, and does the target really lack them?

**Method.** `align_to_anchor.py` (run: `uv run --no-project align_to_anchor.py
genes/ARATH/CERK1/CERK1-uniprot.txt genes/ARATH/LYK4/LYK4-uniprot.txt LYK4_vs_CERK1` from the repository
root, with paths adjusted) globally aligns the full-length LYK4 sequence to *Arabidopsis* CERK1
(A8R7E6), a LysM receptor kinase whose Ser/Thr phosphorylation activity UniProt records from
experiment, using BLOSUM62 with gap open -10 and extend -0.5. It then reports the LYK4 residues
facing CERK1's catalytic-loop aspartate (its UniProt ACT_SITE, in the HRD motif) and the
Mg2+-binding aspartate of its DFG motif. Both sequences come from the cached UniProt records
(sequence version 1).

**Result** (`LYK4_vs_CERK1.residues.tsv`, alignment `LYK4_vs_CERK1.aln.fasta`):

```
role	anchor_acc	anchor_pos	anchor_res	target_acc	target_pos	target_res	status	target_context
catalytic-loop aspartate (HRD)	A8R7E6	441	D	O64825	467	D	RETAINED	PYVHRDLNS
Mg2+-binding aspartate (DFG)	A8R7E6	459	D	O64825	485	S	LOST	RAKIGSLGS
```

**Interpretation.** LYK4 keeps the HRD aspartate that UniProt annotates as its active site, but
has lost the DFG aspartate that coordinates Mg2+-ATP. The review's claim of missing catalytic
residues therefore holds, for the DFG residue rather than the annotated ACT_SITE. A missing DFG
aspartate is consistent with, but does not by itself prove, loss of kinase activity; the review's
conclusion also rests on the published biochemistry.
