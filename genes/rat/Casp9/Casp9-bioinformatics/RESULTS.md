# Casp9 (rat, Q9JHK1): residue conservation versus human CASP9 (P55211)

Script: `align_human_rat.py` (Biopython global alignment, BLOSUM62, gap open -10,
extend -0.5), run from the repository root. Raw output: `alignment_output.tsv`.

## Results

- Human CASP9 is 416 aa and rat Casp9 is 454 aa; all 416 human positions align,
  325 identical (78.1% of aligned positions). The extra rat length lies in the
  CARD-p20 linker, which carries repeated PVVLGP-like motifs.
- Catalytic dyad conserved: human His237 maps to rat His275 and human Cys287 maps
  to rat Cys325, both inside an identical QACGG/SHGCQAS context. These match the
  rat entry's PIRSR ACT_SITE features at 275 and 325.
- Human Tyr153 (phosphorylated by ABL1 after DNA damage) maps to rat Tyr191.
- Human Thr125 (MAPK1 site) maps to rat Thr163.
- Human Ser196 (the AKT1 inhibitory phosphosite) is NOT conserved: the aligned
  rat residue is Trp234 (human RRRFSSLHFMV, rat QHRFCWLRFMV).

## Interpretation

The rat protein retains the catalytic residues of an active initiator caspase,
so transfer of cysteine-type endopeptidase activity from human and mouse is
sound. The ABL1 site is conserved, so ABL1-dependent regulation could apply in
rat, but the AKT1 site is absent, so AKT-mediated inhibitory phosphorylation of
caspase-9 described for human CASP9 should not be assumed for rat.
