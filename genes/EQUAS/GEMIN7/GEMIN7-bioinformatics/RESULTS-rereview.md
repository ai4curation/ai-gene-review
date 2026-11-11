# GEMIN7 (donkey): comparison of UniProt gene-model products (re-review, 2026-10-21)

Reproduce (from this folder): `uv run --script compare_gene_models_rereview.py .`
Raw output: `compare_gene_models_rereview_output.txt`; fetched flat files: `rereview-<ACC>.txt`.

Method: the script fetches the UniProt flat files for the three donkey GEMIN7 entries
(A0A9L0ICL9, A0A9L0IFN2, A0A9L0J5X5), the horse entry A0A9L0T0I7 and human Q9H840, lists their
Ensembl cross-references, tests whether one sequence is an exact C-terminal suffix of another,
and computes ungapped identity for equal-length pairs.

## Output (summary of compare_gene_models_rereview_output.txt)

```
A0A9L0ICL9 [donkey (benchmark)] length 206   gene ENSEASG00005033816.1 (transcript ENSEAST00005038982.1)
A0A9L0IFN2 [donkey]             length 179   gene ENSEASG00005033816.1 (transcript ENSEAST00005039306.1)
A0A9L0J5X5 [donkey]             length 131   gene ENSEASG00005033816.1 (transcripts ENSEAST00005048919.1, ENSEAST00005062208.1)
A0A9L0T0I7 [horse]              length 131
Q9H840     [human (Swiss-Prot)] length 131

A0A9L0IFN2 (179 aa) == A0A9L0ICL9 residues 28-206; extension 27 aa
A0A9L0J5X5 (131 aa) == A0A9L0ICL9 residues 76-206; extension 75 aa
A0A9L0J5X5 (131 aa) == A0A9L0IFN2 residues 49-179; extension 48 aa
A0A9L0J5X5 vs A0A9L0T0I7: 130/131 identical (99.24%)
A0A9L0J5X5 vs Q9H840: 115/131 identical (87.79%)
```

## Interpretation

All three donkey entries are products of one Ensembl gene (ENSEASG00005033816.1). The benchmark
accession A0A9L0ICL9 (206 aa) is an N-terminally extended alternative transcript model: its
C-terminal 131 residues (76-206) are exactly the 131-aa donkey product A0A9L0J5X5, which has the
same length as human Q9H840 and horse A0A9L0T0I7 and starts at the conserved Met (MQTP...). The
75-residue extension has no counterpart in the human or horse proteins. A0A9L0J5X5 is therefore the
canonical-length product of donkey GEMIN7; none of the three donkey entries is Swiss-Prot reviewed.
The benchmark entry contains the complete Gemin7 region, including the Sm-like domain (donkey
140-206), so no Gemin7 domain is missing; the extension is an addition, whose translation in vivo
is not established. These are statements about predicted sequences only.
