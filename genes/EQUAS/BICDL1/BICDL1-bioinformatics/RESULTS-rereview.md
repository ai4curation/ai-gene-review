# BICDL1 donkey gene-model comparison (re-review, 2026-10-21)

Script: `compare_isoforms_rereview.py` (stdlib only; fetches UniProt and Ensembl REST live). Raw output: `RESULTS-rereview.txt`.

Diagnostic segments: CC1 box `AARLG`; SEG_CORE, a central coiled-coil segment of canonical human Q6ZP65 (`KMLSDRKRELEHRL`, human 256); SEG_ALT, the extra exon of human isoform 2 (`DDDSLEEQIRQTSEDSRALREL`).

| accession | source | length | CC1 | SEG_CORE | SEG_ALT |
|---|---|---|---|---|---|
| A0A9L0JLY3 | donkey, benchmark | 573 | 114 | absent | 394 |
| A0A9L0K8K5 | donkey (Ensembl canonical) | 626 | 114 | 261 | 447 |
| A0A9L0JCR9 | donkey | 622 | 114 | 257 | 443 |
| A0A8C4LG90 | donkey | 589 | 114 | 261 | 447 |
| A0A9L0I4K1 | donkey | 574 | 114 | 257 | absent |
| Q6ZP65 | human Swiss-Prot | 573 | 113 | 256 | absent |
| A0JNT9 | mouse Swiss-Prot | 577 | 116 | 259 | absent |

All five donkey products are translations of one Ensembl gene, ENSEASG00005007623. Ensembl marks transcript ENSEAST00005058854 (ENSEASP00005061163, 626 aa, UniProt A0A9L0K8K5) as canonical. The benchmark A0A9L0JLY3 is ENSEAST00005044452 (ENSEASP00005050982), which is not the canonical transcript.

Interpretation: the benchmark product is the only donkey model that lacks SEG_CORE. That segment is present in human and mouse Swiss-Prot canonical sequences and in every other donkey model. The benchmark therefore represents an alternative splice form of donkey BICDL1, which skips a central coiled-coil exon and includes the isoform-2-type exon. Its length matches human canonical (573 aa) only by coincidence. It keeps the N-terminal CC1 box and the C-terminal region (the Rab6-binding region in mouse). Whether this transcript exists in vivo is not known.
