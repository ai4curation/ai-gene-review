# AP5S1 (sigma-5) structural analysis

Tests two claims made in `../AP5S1-ai-review.yaml` about what the AP-5 small subunit
contributes to the complex, using the two experimental structures that make the
comparison possible.

## Run

```bash
uv run python sigma5_structure.py     # writes RESULTS.md and results.json
```

Structures (`8YAB`, the AP-5 core bound to the SPG11 WD40-hairpin; `2JKR`, the AP-2 core
with a CD4 dileucine peptide) are downloaded from RCSB, and all sequences from UniProt,
at run time. Expected sequence lengths are asserted and deposited-versus-UniProt residue
numbering is verified per chain, so a re-released entry aborts the run rather than
silently relabelling residues. Nothing is hardcoded and no result is pre-computed.

## What it asks

1. **Which subunits does sigma-5 touch, and how much surface does each contact bury?**
   Measured as heavy-atom contacts plus Shrake-Rupley buried surface, over all four
   partner chains of 8YAB (zeta, beta5, mu5, SPG11).

2. **Is the acidic dileucine cargo site of sigma2 present and available in sigma-5?**
   The site is defined empirically as the sigma2 residues that contact the bound CD4
   peptide in 2JKR -- no residue list is typed in -- and carried onto sigma-5 by
   sequence-independent structural superposition (Combinatorial Extension). The script
   then asks whether those sigma-5 positions are free or are occupied by the zeta
   N-terminus in the assembled core.

Controls: the second sigma2 copy in 2JKR (positive), the beta5 solenoid (negative), and
a shuffled-sequence null for the pairwise sequence comparisons.

## Reproducibility note

The committed `RESULTS.md` and `results.json` were produced by the environment pinned in
`uv.lock` (Biopython 1.88); re-running `uv run python sigma5_structure.py` there
reproduces them byte for byte. Running under a different Biopython release shifts the CE
superposition slightly — RMSDs move by ~0.1-0.7 Å and individual CA-CA distances by a few
tenths of an Ångström — while the residue correspondence (which sigma-5 position each
sigma2 pocket residue maps to), the buried-surface measurements, and every count reported
in the conclusion are unchanged. Cite the counts and the mapping; treat the third decimal
of an RMSD as environment-dependent.
