# Q25022 benzimidazole-resistance-site alignment

## Checklist

- [x] The FASTA target is Q25022 / GenBank M76491 / protein AAA29168.1.
- [x] The run reused the ungapped resistance-site mapper from
  `genes/HAECO/A2TF56/A2TF56-bioinformatics/benzimidazole_resistance/`.
- [x] The comparison included full-length H. contortus A2TF56 and tub8-9, a
  susceptible H. contortus beta-tubulin isotype-1 partial fragment, and
  C. elegans BEN-1.
- [x] The analysis completed with `just all`.
- [x] The direct result is `results/resistance_sites.csv`.

## Result

The best ungapped protein alignments place full-length A2TF56 and tub8-9 over
Q25022 without indels, but neither is close enough to call Q25022 the same
full-length isotype. A2TF56 is 421/448 identical to Q25022, and the Geary et al.
tub8-9 cDNA is 420/448 identical:

```csv
A2TF56_EF198865_ABM92348,0,448,421,0.940,F,F,E,E,F,Y
M76493.1_tub8-9_AAA29170,0,448,420,0.938,F,F,E,E,F,F
```

The modern susceptible isotype-1 fragment MF034043.1 covers only the core
region from Q25022 residues 152-237, where it is 84/86 identical:

```csv
MF034043.1_susceptible_isotype1_partial,151,86,84,0.977,F,F,E,E,F,F
```

Q25022 therefore carries Phe167, Glu198 and Phe200, but this short
isotype-1-sensitive fragment is not long enough to determine whether beta 12-16
belongs to the later isotype-1 nomenclature. The safer assignment is that
Q25022 is the full-length beta 12-16 cDNA, which Geary et al. separated from the
tub8-9 class by C-terminal divergence.
