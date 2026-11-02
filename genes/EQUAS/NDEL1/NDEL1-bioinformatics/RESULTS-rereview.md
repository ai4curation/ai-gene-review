# NDEL1 (donkey): comparison of all UniProt gene models with human NDEL1

Script: `compare_gene_models_rereview.py` (run with `uv run --script compare_gene_models_rereview.py`).
Inputs: the UniProt REST stream for `gene_exact:NDEL1 AND organism_id:9793` (saved as
`donkey_ndel1_models_rereview.fasta`) and `genes/human/NDEL1/NDEL1-uniprot.txt` (Q9GZM8, 345 aa).
Per-model output is in `gene_models_rereview.json`. This analysis supersedes nothing in `RESULTS.md`;
it adds the comparison with the other donkey gene models.

## Output (verbatim from the script)

```
human Q9GZM8 length 345; residues 316-345: AVNGFDPAPPPPGLGSSRPSSAPGMLPLSV
A0A9L0IJ72 (benchmark): 481 aa; collinear with human 1-338 then 'ATSFREPTLHQSWQQCGGEGLRTQE...'; 335/345 identical pairs; LIS1 region conserved=True; sites not conserved: ['S344']
A0A9L0IW16: 391 aa; collinear with human 1-315 then 'NILQRAHTSSVLATVRWRRAPDSRG...'; 319/343 identical pairs; LIS1 region conserved=True; sites not conserved: none
A0A9L0IGZ7: 369 aa; collinear with human 1-315 then 'QEKVIFPTLFMDDSQIWVSIPARSL...'; 313/319 identical pairs; LIS1 region conserved=True; sites not conserved: ['S344']
A0A9L0K0K7: 361 aa; collinear with human 1-315 then 'NILQRAHTSSVLATVRWRRAPDSRG...'; 319/343 identical pairs; LIS1 region conserved=True; sites not conserved: none
A0A9L0JF97: 346 aa; collinear with human 1-317 then 'VLCAVVSIGDAAFLKSIFHCWLQNF...'; 315/323 identical pairs; LIS1 region conserved=True; sites not conserved: ['S344']
A0A9L0IJ59: 330 aa; collinear with human 1-315 then 'SRLPVSRLPLSGFSS...'; 313/330 identical pairs; LIS1 region conserved=True; sites not conserved: ['S344']
A0A9L0IMT2: 328 aa; collinear with human 1-315 then 'QEKVIFPTLFMGQ...'; 313/328 identical pairs; LIS1 region conserved=True; sites not conserved: ['S344']
A0A9L0J5V8: 319 aa; collinear with human 1-315 then 'EDFP...'; 312/319 identical pairs; LIS1 region conserved=True; sites not conserved: ['S344']
A0A8C4MPY8: 269 aa; collinear with human 1-264 then 'GSKRL...'; 263/269 identical pairs; LIS1 region conserved=True; sites not conserved: ['L266', 'E267', 'C273', 'S344']
A0A9L0JFV9: 85 aa; collinear with human 1-58 then 'ACSGGCWALPSPRTLRDINTGYFLF...'; 58/58 identical pairs; LIS1 region conserved=False; sites not conserved: ['S198', 'T219', 'S231', 'S242', 'T245', 'L266', 'E267', 'C273', 'S344']
```

## Interpretation

- UniProt holds ten donkey NDEL1 gene models from one Ensembl gene. All share the same N-terminal
  sequence and differ at the C-terminus, as alternative last exons would.
- The benchmark model A0A9L0IJ72 is the only donkey model that carries the human isoform-1 last exon
  (human residues 316-338, AVNGFDPAPPPPGLGSSRPSSAP). It is collinear with human isoform 1 through
  residue 338 and then replaces the final seven human residues (GMLPLSV, 339-345) with a 143-residue
  tail (donkey 339-481) that has no counterpart in any human isoform. The S344 site therefore has no
  equivalent; in the earlier pairwise alignment (`RESULTS.md`) the last seven donkey residues were
  paired with human 339-345 only by end placement.
- Every human-mapped functional region and site used in the review lies within residues 1-338 and is
  identical in the benchmark model: the LIS1-binding region (114-133), the CDK/MAPK phosphosites
  (S198, T219, S231, S242, T245), the DISC1-binding residues (L266, E267) and palmitoyl C273.
- Most other models switch at human position 315/316 to tails resembling human isoform 3
  (A0A9L0IMT2 ends QEKVIFPTLFMGQ, exactly the human isoform-3 tail) or to other unmatched tails;
  A0A8C4MPY8 (269 aa) and A0A9L0JFV9 (85 aa) are truncated models.
- The benchmark is thus an alternative gene model of donkey NDEL1: its functional core matches human
  isoform 1, and its C-terminal tail is unverified. Whether the tail is a real exon or a gene-model
  artefact (for example read-through into downstream sequence) cannot be decided from sequence alone.
