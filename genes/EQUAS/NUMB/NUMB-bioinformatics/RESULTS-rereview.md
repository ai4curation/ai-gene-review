# NUMB (donkey A0A9L0IQ95): re-review motif and gene-model check

Reproduce: `uv run --script genes/EQUAS/NUMB/NUMB-bioinformatics/motifs_rereview.py genes/EQUAS/NUMB/NUMB-uniprot.txt genes/EQUAS/NUMB/NUMB-bioinformatics/human-P49757-uniprot.txt`
(run from the repository root; raw output in `motifs_rereview_output.txt`).

## Motif output

```
## donkey length 506
first DOMAIN feature: (37, 173)
residue 102: T (context VVDEKTKDLIV)
DPF motif start positions: [246, 469]
NPF motif start positions: [492]

## human length 651
first DOMAIN feature: (33, 193)
residue 102: T (context VVDEKTKDLIV)
DPF motif start positions: [343, 614]
NPF motif start positions: [637]
```

## Gene-model check (UniProt REST, 2026-10-21)

The donkey NUMB gene ENSEASG00005004756 has six unreviewed UniProt entries (A0A9L0IHZ0 652 aa,
A0A9L0ICJ5 638 aa, A0A9L0JAM1 603 aa, A0A9L0IQ95 506 aa, A0A8C4L519 456 aa, A0A8C4L9W9 445 aa), all
in reference proteome UP000694387 and all cross-referenced to the same Ensembl gene. The UniProt
gene-centric canonical protein for this gene is A0A9L0IHZ0 (652 aa), the counterpart of human
canonical P49757-1 (651 aa).

## Interpretation

The benchmark accession A0A9L0IQ95 is an alternative-isoform product of donkey NUMB, not the
canonical product: it corresponds to human isoform 5 (see RESULTS.md) and is 146 residues shorter
than the canonical donkey model A0A9L0IHZ0. It retains the complete PTB (PID) domain, the threonine
equivalent to human Thr-102 (the AAK1 phosphorylation site, PubMed:18657069), and the C-terminal
DPF and NPF motifs that are also present at the C-terminus of human NUMB. Those motif positions are
pattern matches only; this analysis does not test binding. The segment missing relative to the
canonical model is the region equivalent to human 219-316 plus the proline-rich-region insert
(human 366-413).
