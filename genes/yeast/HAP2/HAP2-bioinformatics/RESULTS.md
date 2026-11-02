# HAP2 (P06774) bioinformatics: PANTHER subfamily placement

## Method

`panther_subfamily.py` (run with `uv run --script panther_subfamily.py > panther_subfamily.json`)
queries the PANTHER `geneinfo` web service (PANTHER release 19) for the family and
subfamily of S. cerevisiae HAP2 (P06774), N. crassa NCU03033 (Q7SGY4) and human NFYA
(P23511). The raw output is in `panther_subfamily.json`.

## Results

| accession | organism | PANTHER family | PANTHER subfamily |
|---|---|---|---|
| P06774 | S. cerevisiae HAP2 | PTHR12632 | PTHR12632:SF6 |
| Q7SGY4 | N. crassa NCU03033 | PTHR12632 | PTHR12632:SF6 |
| P23511 | human NFYA | PTHR12632 | PTHR12632:SF6 |

HAP2, NCU03033 and human NFYA are all placed in the same PANTHER subfamily,
PTHR12632:SF6 (NUCLEAR TRANSCRIPTION FACTOR Y SUBUNIT ALPHA). The UniProt and InterPro
PANTHER cross-references for P06774 and Q7SGY4 give only the family PTHR12632 with no
subfamily; the subfamily assignment comes only from the PANTHER service.

## Interpretation

Because the three proteins share a subfamily, the core NF-YA/HAP2 properties, CCAAT-box
recognition as part of the HAP2/3/5 (NF-YA/B/C) heterotrimer and subunit assembly
through the conserved core, can be transferred within this subfamily. The
yeast-specific HAP4-dependent activation of respiratory genes depends on HAP4, a
Saccharomycetaceae-type activation subunit. Subfamily membership alone does not
show that this regulon is conserved.
