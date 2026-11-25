# Exact historical clone versus genome record identity

These public UniProt JSON records preserve the ordinary source lookups used to distinguish the published clones from later H16 genome proteins. Run `uv run python genes/CUPNE/gbd/gbd-source-analysis/verify_published_sequences.py` to reproduce the comparison; `--refresh` explicitly fetches current records from the public API.

Q59104 and Q0KBD6 have identical 382-residue sequences. Their accession records differ in strain/taxon aggregation, so the original published Q59104 is retained. Q9RBF6, the published SHF3 GabD clone, differs at 11 of 483 positions from H16 GabD1/Q0K2K1; these must not be silently interchanged. These comparisons establish sequence identity/difference only, not substrate specificity, evolutionary placement, or identical native expression. The primary paper and BRENDA evidence establish chemistry. The JSON records' embedded GO lines are not used as support.
