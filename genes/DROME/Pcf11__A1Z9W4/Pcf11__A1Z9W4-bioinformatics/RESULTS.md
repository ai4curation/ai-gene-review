# Pcf11 (A1Z9W4) sequence comparison

Script: `compare_pcf11.py` (fetches UniProt FASTA live; Biopython local alignment, BLOSUM62).
Raw output: `compare_pcf11.out.txt`. Domain coordinates are from the InterPro API for A1Z9W4.

## Evolutionary placement

A1Z9W4 is assigned to PANTHER subfamily PTHR15921:SF3 (PRE-MRNA CLEAVAGE COMPLEX 2 PROTEIN PCF11), the same subfamily as human PCF11 (O94913), budding yeast Pcf11 (P39081), fission yeast SPAC4G9.04c (Q10237) and worm pcf-11 (Q09345), in the PANTHER 19.0 classification files. SCAF8 (Q9UPN6) sits in a different subfamily (SF7). Transfer from the characterised human and yeast Pcf11 proteins is therefore within one subfamily.

## Fly Pcf11 products

| Accession | Length | Shared N-terminal prefix with A1Z9W4 |
|---|---|---|
| A1Z9W4 | 1953 | 1953 |
| Q8IGR2 | 573 | 372 |
| C0P8M6 | 86 | 62 |

A1Z9W4 is the long (>200 kDa) Pcf11 product. The 573-residue product (RB class) shares residues 1-372 of A1Z9W4, which include the whole CID (InterPro IPR047415, residues 17-149) and the alpha-helical region (PF20845, residues 190-224). The anti-Pcf11 antibody used in the fly studies was raised against residues 1-283, so it recognises the long and the RB products alike.

## Conserved regions

| A1Z9W4 region | Partner | Aligned columns | Identity (%) |
|---|---|---|---|
| CID 17-149 | human PCF11 O94913 | 125 | 49.6 |
| CID 17-149 | yeast Pcf11 P39081 | 103 | 35.0 |
| 1400-end | human PCF11 O94913 | 173 | 40.5 |
| 1400-end | yeast Pcf11 P39081 | 127 | 29.1 |

A C2H2-like pattern match is found at A1Z9W4 residues 1368-1390 (CSSCGVRFPPEQTIKYSQHLDWH). It matches human PCF11 residues 1343-1365 (CYSCGMRFTTSQTDVYADHLDWH) and yeast Pcf11 residues 421-445, which suggests that the first Pcf11 zinc finger is conserved in the long fly product. A1Z9W4 also carries the Pcf11 C-terminal domain (PF21936, residues 1465-1509). The pattern scan only finds sequence motifs: it shows neither zinc binding nor RNA binding.

## Interpretation

The long product A1Z9W4 has every region that defines Pcf11 proteins: the N-terminal CID, the helical region, the conserved zinc-finger motif and the C-terminal domain. In human and yeast Pcf11 these regions are needed for CTD binding, RNA binding and the Clp1/Cbc partnership. Fly experiments in which only the N-terminal region was tested (CTD binding, dismantling of elongation complexes) apply to A1Z9W4 because A1Z9W4 contains that region. The Cbc co-immunoprecipitation was done with the >250 kDa band, which corresponds to the long products that include A1Z9W4.
