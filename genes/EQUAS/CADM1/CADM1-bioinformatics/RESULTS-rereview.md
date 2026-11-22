# CADM1 (donkey): benchmark entry vs other products of the same gene (re-review, 2026-10-21)

## Method

The UniProt gene-centric record for A0A9L0IX39 (proteome UP000694387) was downloaded from
`https://rest.uniprot.org/genecentric/search?query=accession:A0A9L0IX39&format=json` on
2026-10-21 and saved as `donkey-CADM1-genecentric-rereview.json`. The script
`compare_isoforms_rereview.py` compares each product with the gene-centric canonical
product. Run from this folder:

```
uv run --script compare_isoforms_rereview.py
```

## Output (isoform_comparison_rereview.txt)

```
Gene-centric canonical: A0A9L0IJE9 (473 aa), C-terminus QNNSEEKKEYFI
A0A9L0IJE9	473 aa	prefix shared with canonical: 473	C-term: EGGQNNSEEKKEYFI
A0A9L0IX39	390 aa	prefix shared with canonical: 335	C-term: RHKGLFSLTSSPRIK <- benchmark
A0A9L0IKY6	417 aa	prefix shared with canonical: 335	C-term: EGGQNNSEEKKEYFI
A0A8C4LG30	372 aa	prefix shared with canonical: 335	C-term: ASNGKGDHTSKSLLL
A0A8C4LBJ1	444 aa	prefix shared with canonical: 362	C-term: EGGQNNSEEKKEYFI
A0A9L0JLU5	455 aa	prefix shared with canonical: 372	C-term: EGGQNNSEEKKEYFI
A0A9L0JM59	446 aa	prefix shared with canonical: 335	C-term: EGGQNNSEEKKEYFI
A0A8C4PJC1	380 aa	prefix shared with canonical: 335	C-term: PTAELHLVEMTFKTR
vs A0A9L0IKY6: identical for first 379 residues; benchmark then reads 'LFSLTSSPRIK', A0A9L0IKY6 reads 'TYFTHEAKGADDAADADTAIINAEGGQNNSEEKKEYFI'
```

## Interpretation

The donkey CADM1 gene has eight UniProt products, all Ensembl transcript models of one gene.
The gene-centric canonical product is A0A9L0IJE9 (473 aa), which ends in the EYFI PDZ-binding motif.
The benchmark A0A9L0IX39 (390 aa) is an alternative product of the same gene, not a separate gene.
It is identical to the short-stalk product A0A9L0IKY6 for its first 379 residues (signal peptide, three Ig-like domains, stalk, transmembrane helix and juxtamembrane segment).
It then ends in an 11-residue alternative tail (LFSLTSSPRIK) in place of the 38-residue cytoplasmic tail that carries the protein 4.1-binding region and the C-terminal EYFI PDZ-binding motif.
The canonical cytoplasmic tail is therefore encoded by the donkey gene; the benchmark entry is a tail-truncated alternative transcript model whose existence as a protein has not been tested.
