# CG45100 (A0A0B4LGP2) conservation check, 2026-10-20 re-review

Script: `blast_conservation_rereview.sh` (EBI Job Dispatcher blastp, PAM30, UniProtKB, E <= 10).
Raw output: `blast_uniprotkb_rereview.out`.

## Query

A0A0B4LGP2, 38 aa: `MLLGEYDTTRRLLFIVAVLLIVLYAKTYLLPGEDLVHN` (Phobius TM helix 12-30).

## Hits with E < 1e-10 (all uncharacterized, PE=4)

| Accession | Species | Length | Identity | E-value |
|---|---|---|---|---|
| A0A6P8KJW9 | Drosophila mauritiana | 38 | 37/38 (97%) | 3e-32 |
| A0A6P4F9I6 | Drosophila rhopaloa | 38 | 35/35 (100%) | 3e-30 |
| A0A6P4IIZ7 | Drosophila kikkawai | 38 | 34/35 (97%) | 5e-28 |
| A0AB39ZL96 | Drosophila suzukii | 38 | 34/35 (97%) | 5e-28 |
| A0A6J2TM08 | Drosophila (Scaptodrosophila) lebanonensis | 38 | 29/32 (91%) | 1e-21 |
| A0AAD4K8M0 | Drosophila rubida | 44 | 25/33 (76%) | 3e-12 |

The next hit (A0A7W0CU41, an actinobacterial ABC permease) has E = 0.058 and covers only
20 residues of hydrophobic sequence; it and all lower hits are compositional matches to the
TM segment and are not homologs.

## Interpretation

- The peptide's amino-acid sequence, including the hydrophobic segment and the flanking
  charged residues (R10-R11, K26), is conserved across Drosophilidae, from the melanogaster
  group to Scaptodrosophila. Conservation at the peptide level is consistent with (but does
  not prove) translation under purifying selection on the encoded product.
- No homolog outside Drosophilidae was found, and none of the homologs is experimentally
  characterized. There is no PANTHER family, no Pfam/InterPro domain and no PAINT node, so
  there is no characterized relative from which any function could be transferred.
- HDAC3 (or any histone deacetylase) is not among the hits, so the peptide has no detectable
  similarity to the protein encoded downstream on the same transcript; the Hdac3 association
  is positional (gene name Hdac3-5'utr, synonym Dmel_Hdac3_uORF), not homology.
