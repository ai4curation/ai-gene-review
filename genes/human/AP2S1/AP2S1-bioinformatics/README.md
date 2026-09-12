# AP2S1 sigma2 dileucine-pocket residue check

Tests the residue claims made in `../AP2S1-ai-review.yaml` for the AP-2 sigma subunit's
acidic dileucine binding site, and measures how sigma2-specific those residues are.

## Run

```bash
uv run python check_sigma2_pockets.py     # writes RESULTS.md and results.json
```

Requires `mafft` on PATH (`brew install mafft`). Every protein sequence is fetched live
from the UniProt REST API at run time; nothing is cached in the repository and no result
is hardcoded. Re-running regenerates `RESULTS.md`, `results.json`,
`human_sigma_paralogs.fasta` and `human_sigma_paralogs.aln.fasta`.

## What it checks

1. Do the eight residues Kelly et al. 2008 (PMID:19140243) identify as building sigma2's
   dileucine pockets and basic L-4 patch actually occur at those positions in human
   AP2S1 (P53680)?
2. The co-crystal's sigma2 chain is the mouse orthologue, so does the numbering transfer?
   Human P53680, rat P62744 and mouse P62743 are compared over the full chain.
3. How conserved are those positions across the eight human AP-complex sigma subunits
   (AP2S1, AP1S1, AP1S2, AP1S3, AP3S1, AP3S2, AP4S1, AP5S1), aligned with MAFFT L-INS-i?

Results are reported as measured, including where they do not match expectation.
