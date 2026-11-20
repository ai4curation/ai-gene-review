# hldE bioinformatics: is there an HldD epimerase in P. putida KT2440?

`query_hldd_absence.py` asks UniProt whether *Pseudomonas putida* KT2440
(taxon 160488) encodes an ADP-heptose 6-epimerase (HldD/RfaD, EC 5.1.3.20),
and runs the identical queries against *P. aeruginosa* PAO1 (taxon 208964) as a
positive control, so that an empty result for the target can be distinguished
from a malformed query.

Run with `just` (or `python3 query_hldd_absence.py`). It needs network access and
no API key. Outputs `hldd_absence.tsv`; `RESULTS.md` holds the interpretation.

The script hardcodes no accession, count or conclusion, and exits non-zero if any
query fails, so a partial run cannot be mistaken for a negative result.
