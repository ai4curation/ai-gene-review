# SHMOOSE (C0HM83) ORF location and genetic-code check

Scripts: `locate_orf.py` (output `locate_orf.out`), `overlaps.py` (output `overlaps.out`).
Both fetch the human mtDNA reference (rCRS, NC_012920.1) from NCBI at run time.

- The 58-aa UniProt sequence is found once, on the heavy-strand-encoded (+) sense of rCRS,
  starting at m.12234 (ATG) and ending with a TAA stop at m.12408-12410.
- Annotated features overlapped (all + strand): MT-TS2 (tRNA-Ser(AGY), 12207-12265),
  MT-TL2 (tRNA-Leu(CUN), 12266-12336) and the 5' end of MT-ND5 (12337-14148), in a reading
  frame different from ND5 (offset reported in `overlaps.out`).
- The ORF contains no codon whose meaning differs between the standard (table 1) and
  vertebrate mitochondrial (table 2) codes (no TGA, ATA, AGA or AGG), so it gives the same
  58-aa product whether translated by cytosolic or mitochondrial ribosomes. The genetic code
  therefore does not tell us where SHMOOSE is translated (contrast MOTS-c).
- Codon 47 occupies m.12372-12374 (GAC = Asp in rCRS); the m.12372G>A (rs2853499) allele
  gives AAC = Asn, i.e. the D47N variant.
