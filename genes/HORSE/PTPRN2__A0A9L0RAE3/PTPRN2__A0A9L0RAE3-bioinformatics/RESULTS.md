# Horse PTPRN2 (A0A9L0RAE3): evolutionary grounding and residue conservation

Script: `compare_sequences.py` (Biopython global alignment, BLOSUM62, gap open -10, extend -0.5,
free end gaps). Raw output: `results.json`. Run date 2026-10-20. Sequences of mouse P80560 and rat
Q63475 are fetched live from UniProt; horse and human are read from the repository flat files.

## 1. Evolutionary placement

- A0A9L0RAE3 (1054 aa, Ensembl ENSECAP00000060972 of gene ENSECAG00000012762) is classified in
  PANTHER PTHR46106:SF5 (RECEPTOR-TYPE TYROSINE-PROTEIN PHOSPHATASE N2), the same subfamily as human
  PTPRN2 (Q92932), mouse Ptprn2 (P80560) and rat phogrin (Q63475). It is not in the PTPRN (IA-2)
  subfamily, PTHR46106:SF1 (human Q16849).
- The PAINT nodes behind the horse IBA rows are PTN000439769 (IA-2 family node; seeds mouse Ptprn2 (MGI:107418),
  rat Ptprn2 (RGD:61904) and Ptprn (RGD:620777), worm ida-1 (WBGene00002048) and fly FBgn0031294) carrying secretory granule, synapse and regulation of
  secretion, and PTN000439772 (vertebrate IA-2/IA-2beta node; seeds mouse Ptprn (MGI:102765) and Ptprn2 (MGI:107418)) carrying
  insulin secretion involved in cellular response to glucose stimulus. Horse PTPRN2 is a eutherian SF5
  member and descends from both nodes.
- No experimental GO annotation exists for any horse PTPRN2 product; every function below is inferred.

## 2. Pairwise identity to the characterised SF5 orthologs

| Comparison | Ortholog length | Aligned columns | Identical | Identity |
|---|---|---|---|---|
| horse A0A9L0RAE3 vs human Q92932 | 1015 | 1000 | 745 | 74.5% |
| horse A0A9L0RAE3 vs mouse P80560 | 1001 | 989 | 713 | 72.1% |
| horse A0A9L0RAE3 vs rat Q63475 | 1004 | 988 | 717 | 72.6% |

Identity is uneven along the protein (horse vs human, by human segment):

| Human segment | Identity |
|---|---|
| luminal precursor region 22-615 | 60.8% |
| mature IA-2beta60 chain start to TM 502-615 | 73.7% |
| cytoplasmic region 637-1015 | 92.9% |
| PTP-like domain 745-1005 | 96.2% |

The cytoplasmic PTP-like domain, which carries the characterised phosphoinositide phosphatase activity
and the sorting signals, is highly conserved. The lower identity of the luminal region is consistent
with the 39-residue longer horse model containing extra or alternative luminal sequence; this region
was not analysed further.

## 3. Functional positions (human Q92932 numbering from its UniProt FT lines)

| Human feature | Human | Horse position | Horse | Same |
|---|---|---|---|---|
| dibasic cleavage site 427-428 | KS | 425-426 | KS | yes |
| transmembrane helix 616-636 | IALTLVSLACILGVLLASGLI | 656-676 | IVLTLISVAAILGVLLASGVI | conservative |
| tyrosine-based internalization motif 666-675 | YQELCRQRMA | 705-714 | YQELCRQRMA | yes |
| WPD-loop region around substrate-binding Asp913 (910-916) | SWYDRGV | 949-955 | SWYDQGV | Asp conserved |
| PTP signature / P-loop incl. catalytic Cys945 (943-953) | VHCSDGAGRSG | 982-992 | VHCSDGAGRSG | yes |
| Q-loop around substrate-binding Gln990 (988-992) | MVQTK | 1027-1031 | MVQTK | yes |
| leucine-based sorting signal 1004-1010 | EEVNAIL | 1043-1049 | EEVNAIL | yes |
| C-terminus 1006-1015 | VNAILKALPQ | 1045-1054 | VNAILKALPQ | yes |

Result: the catalytic cysteine (horse Cys984, equivalent to human Cys945 and to the rat phogrin
cysteine whose mutation abolishes phosphoinositide phosphatase activity), the P-loop, the WPD-loop
aspartate, the Q-loop glutamine, the tyrosine-based internalization motif and the C-terminal
leucine-based sorting signal are all retained. The horse PTP-like domain therefore carries the same
residues, including the same departures from active protein-tyrosine phosphatases, as the
characterised human and rat proteins.

## Limits

Sequence comparison only; no structure prediction or assay. Conservation of the catalytic-site
residues supports, but does not prove, that the horse protein shares the phosphoinositide phosphatase
activity measured for rat phogrin.
