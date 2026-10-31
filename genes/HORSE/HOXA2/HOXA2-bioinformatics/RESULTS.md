# HOXA2 (horse, F7DP63) gene-model comparison

Script: `compare_gene_model.py` (PEP 723; run with `uv run --script compare_gene_model.py`).
Raw output: `results.txt`. Sequences are fetched live from UniProt REST (F7DP63, A0A9L0JBM7,
O43364, P31245) and NCBI efetch (horse RefSeq XP_001499478.2).

## Results (from results.txt)

- Lengths: F7DP63 404 aa; horse RefSeq XP_001499478.2 373 aa; donkey A0A9L0JBM7 373 aa;
  human O43364 376 aa; mouse P31245 372 aa.
- F7DP63 N-terminal segment 1-85 (not in human/mouse/RefSeq horse):
  MGMKPRMPGAALACSGAAFLWLAAALATGIWAQGPGVVVSLGTCIYLSGATPEKLMAQEGREASRAASHFPLPVAARCIAALEKP
- human N-terminal segment 1-54 absent from F7DP63: MNYEFEREIGFINSQPSLAECLTSFPPVADTFQSSSIKTSTLSHSTLIPPPFEQ
- The shared anchor TIPSLNPGSHPRHG starts at human position 55 and F7DP63 position 86.
- F7DP63 86-end vs RefSeq 55-end: lengths 319/319, identical positions 318
- YPWM hexapeptide core: human position 95, F7DP63 position 126.
- human homeodomain 143-202 found verbatim in F7DP63: True (F7DP63 start 171)

## Interpretation

F7DP63 is the Ensembl horse HOXA2 gene model (ENSECAT00000000353.4). Its first 85 residues
are not homologous to the conserved HOXA2 N-terminus present in human, mouse, donkey and the
horse RefSeq model; the conserved 54-residue N-terminus (MNYEFEREIG...) is missing. The
SignalP "signal peptide" (1-32) that UniProt reports for F7DP63 lies entirely inside this
non-conserved segment, so it is an artefact of the gene model, not a feature of horse HOXA2.
From residue 86 onward F7DP63 is identical to the RefSeq protein at 318 of 319 positions and
carries the intact YPWM (PBX-interaction) hexapeptide and a homeodomain identical to human.
F7DP63 is therefore an alternative (most likely erroneous 5'-exon) gene model of horse HOXA2,
with all DNA-binding and cofactor-interaction determinants intact; the RefSeq model
XP_001499478.2 represents the canonical product. No reviewed (Swiss-Prot) horse HOXA2 entry
exists in UniProt (query gene_exact:HOXA2 AND organism_id:9796 returns only F7DP63).
