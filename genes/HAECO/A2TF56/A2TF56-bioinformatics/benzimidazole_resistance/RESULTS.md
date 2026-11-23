# A2TF56 benzimidazole-resistance-site alignment

## Checklist

- [x] The script takes the FASTA path, target id, and residue positions as
  command-line arguments.
- [x] The script writes only to stdout and has no hardcoded output path.
- [x] The script was run on a full-length H. contortus tub8-9 cDNA, a partial
  susceptible H. contortus beta-tubulin isotype-1 fragment, and C. elegans
  BEN-1.
- [x] The analysis completed with `just all`.
- [x] The direct result is `results/resistance_sites.csv`.

## Result

The best ungapped protein alignment maps the susceptible H. contortus isotype-1
fragment MF034043.1 onto A2TF56 residues 152-237. At the benzimidazole
resistance sites, MF034043.1 has the susceptible F/E/F pattern at positions
167, 198, and 200, while A2TF56 carries F/E/Y.

```csv
query,offset,compared,matches,identity,target_167,query_at_167,target_198,query_at_198,target_200,query_at_200
MF034043.1_susceptible_isotype1_partial,151,86,85,0.988,F,F,E,E,Y,F
```

The older H. contortus tub8-9 full-length cDNA M76493.1 also carries Phe at
the target's position 200, as does C. elegans BEN-1:

```csv
M76493.1_tub8-9_AAA29170,0,448,444,0.991,F,F,E,E,Y,F
Q18817_BEN1,0,444,422,0.950,F,F,E,E,Y,F
```

This supports describing A2TF56 as an H. contortus beta-tubulin isotype-1
sequence with the F200Y benzimidazole-resistance substitution and with the
other two common resistance positions, 167 and 198, unchanged.
