# mstE (Q5B0S0, AN5860) bioinformatics (2026-10-21)

Two reproducible analyses, both run with `uv run --script <script>`; raw output is
saved next to each script.

## 1. PANTHER/PAINT placement (`panther_placement.py` -> `panther_placement.out`)

Fetches the live PANTHER PTHR48022 tree (pantherdb.org treeinfo service) and prints
the leaf-to-root paths of MstE and N. crassa GLT-1 (Q1K4S3), their most recent common
ancestor, the leaves of the PTHR48022:SF92 subfamily root, and whether MstE descends
from each PAINT IBD node in `interpro/panther/PTHR48022/PTHR48022-paint.tsv`.

Findings (from the output file):

- MstE leaf PTN000628302 -> PTN002766206 (Aspergillus speciation) -> PTN002362094
  (Pezizomycotina speciation; root of PTHR48022:SF92, 5 leaves) -> PTN004641278
  (Pezizomycotina duplication, SF91) -> ... -> PTN000627328 (family root, LUCA, 521 leaves).
- GLT-1 leaf PTN002362095 -> PTN001174959 -> PTN001174958 -> PTN002362094.
- The MRCA of MstE and GLT-1 is PTN002362094, a SPECIATION node: MstE and GLT-1 are
  orthologs within SF92, separated by no duplication.
- SF92 contains five leaves: MstE (A. nidulans), AFUA_2G11520 (Q4X119, A. fumigatus),
  GLT-1 (N. crassa), SS1G_13734 (A7F804, Sclerotinia) and SNOG_03012 (Q0UZ02, Parastagonospora).
- All three PAINT IBDs that reach MstE sit on the family root PTN000627328:
  GO:0016020 membrane (MstE is a seed), GO:0008643 carbohydrate transport (MstE is a seed)
  and GO:0005351 carbohydrate:proton symporter activity (MstE is NOT a seed; seeds are
  S. pombe SPCC548.07c, SGD:S000003521, A. nidulans MstA/AN8737 Q5ASJ3 and MstC/AN6669 Q5AYG1).
- The PTN001174948 plasma membrane IBD (Dikarya) does not cover MstE or GLT-1.
- No IBD in this family carries the experimentally established MstE term
  GO:0055056 D-glucose transmembrane transporter activity.

## 2. TM1 protonation-site residue (`tm1_site.py` -> `tm1_site.out`)

Global pairwise alignment (BLOSUM62, open -10, extend -0.5) of each protein to E. coli
XylE (P0AGF4); the residue aligned to XylE Asp27 (the TM1 protonation site of the
proton-coupled sugar porter; GLUT1 Asn29 in the uniporter) is reported.

| accession | protein | PANTHER SF | position | residue |
|---|---|---|---|---|
| Q5B0S0 | MstE | SF92 | 67 | S |
| Q1K4S3 | GLT-1 | SF92 | 48 | V |
| Q5AYG1 | MstC/HxtB | SF6 | 36 | D |
| C8VDD8 | HxtC | SF17 | 42 | A (window AMPYWAQTFST; the GY motif is not in register, so this mapping is unreliable) |
| Q5BCD3 | HxtE | SF40 | 35 | D |
| Q5ASJ3 | MstA/HxtD | SF6 | 36 | D |
| P11166 | human GLUT1 (uniporter control) | PTHR23503 | 29 | N |
| P32465 | S. cerevisiae HXT1 (low-affinity facilitator control) | SF75 | 82 | D |

Interpretation: the alignment recovers the expected GLUT1 Asn29, so the position is
mapped correctly for proteins whose TM1 GY motif is in register. Both SF92 members
(MstE, GLT-1) carry a non-acidic residue at the site, whereas the A. nidulans MstA/MstC
and HxtE paralogs carry Asp. The diagnostic is asymmetric: yeast HXT1, a facilitator,
also has Asp, so an acidic residue does not imply symport. A non-acidic residue argues
against, but does not prove the absence of, XylE-type proton coupling in MstE. This
result is inconclusive about MstE energetics and is not a substitute for a transport
energetics experiment.
