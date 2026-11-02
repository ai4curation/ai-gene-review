# GLT-1 TM1 protonation-site re-check (2026-10-21 re-review)

Script: `tm1_site_rereview.py` (run with `uv run --script tm1_site_rereview.py`; sequences fetched live from UniProt).

Method: global pairwise alignment (BLOSUM62, gap open -10, extend -0.5) of each protein to E. coli XylE (P0AGF4), reporting the residue aligned to XylE Asp27, the TM1 protonation site of the proton-coupled sugar porter.

| accession | protein | aligned position | residue |
|---|---|---|---|
| Q1K4S3 | GLT-1 (N. crassa, PTHR48022:SF92) | 48 | V |
| Q5B0S0 | MstE (A. nidulans AN5860, PTHR48022:SF92) | 67 | S |
| Q7S0I5 | HGT-1 (N. crassa) | 52 | D |
| Q7S3Q4 | HGT-2 (N. crassa) | 35 | D |
| P11166 | GLUT1 (human uniporter, control) | 29 | N |

Interpretation: the reference XylE residue is D27 and the GLUT1 control maps to its known Asn29, so the alignment recovers the expected position. GLT-1 has a non-protonatable Val48 at this site, and the characterised low-affinity glucose transporter MstE from the same PANTHER subfamily (SF92) has a non-acidic Ser. The high-affinity Neurospora HGT-1 and HGT-2 retain Asp. This independently reproduces the earlier OpenScientist observation for GLT-1 and adds that the non-acidic residue is shared by the SF92 relative MstE. A single-residue diagnostic is asymmetric (an acidic residue is not sufficient for symport, as GLUT2 shows), so absence of an acidic residue argues against, but does not prove the absence of, proton coupling.
