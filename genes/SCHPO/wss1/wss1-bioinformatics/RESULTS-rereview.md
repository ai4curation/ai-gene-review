# wss1 WLM paralog / PANTHER placement check (re-review, 2026-10-21)

Script: `wlm_paralogs_rereview.py` (run with `uv run --script wlm_paralogs_rereview.py`).
It queries UniProt for all Pfam PF08325 (WLM) proteins in S. pombe (taxon 284812) and
S. cerevisiae S288c (taxon 559292), and reports PANTHER assignments and the HExxH zinc
motif plus the next downstream His (third zinc ligand candidate). Raw output:
`wlm_paralogs_rereview.tsv`.

## Output (2026-10-21)

```
284812	O94580	wss2 wss1b SPCC1442.07c	282	PTHR47795:SF1;PTHR47795;	H202-E203-H206; next H at 209
284812	Q9P7B5	wss1 SPAC521.02	262	PTHR46622;PTHR46622:SF1;	H96-E97-H100; next H at 106
559292	P38838	WSS1 YHR134W	269	PTHR46622;PTHR46622:SF1;	H115-E116-H119; next H at 125
```

## Interpretation

- S. pombe has exactly two WLM proteins. Q9P7B5 (wss1, SPAC521.02) and budding-yeast
  WSS1 (P38838) are both in PANTHER subfamily PTHR46622:SF1, so they are placed in the
  same subfamily, the Wss1 clade.
- The second fission-yeast WLM protein, O94580 (gene names wss2 / wss1b, SPCC1442.07c),
  is classified in a different PANTHER family (PTHR47795). Experimental data published for
  S. pombe "Wss1b" (crystal structures of its protease domain) therefore concern the
  paralog Wss2, not Q9P7B5, and are not subfamily-level evidence for Q9P7B5.
- Q9P7B5 and P38838 share the same zinc-motif arrangement: HExxH followed by a third His
  six residues downstream (Q9P7B5 H96/E97/H100/H106; P38838 H115/E116/H119/H125). This
  matches the UniProt PROSITE-derived catalytic site and Zn ligand annotation for Q9P7B5.
  Wss2 differs in spacing (H202/E203/H206, next His at 209; UniProt places a ligand at 212).
- The Q9P7B5 benchmark accession is the full-length, reviewed canonical product (262 aa,
  sequence version 2); it has the complete WLM domain (8-195) and the C-terminal SIM.
