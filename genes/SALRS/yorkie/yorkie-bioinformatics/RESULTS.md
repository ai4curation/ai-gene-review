# F2UDK1 (PTSG_06057, S. rosetta Yorkie homolog): motif and identity checks

Reviewer's own analysis (2026-10-01), not published data. Reproduce from the repository root with

```
uv run python genes/SALRS/yorkie/yorkie-bioinformatics/motif_scan.py > genes/SALRS/yorkie/yorkie-bioinformatics/motif_scan_output.txt
```

Sequences are fetched live from the UniProt REST API (F2UDK1, F2U5K0, human YAP1
P46937, Drosophila Yorkie Q45VV3, Capsaspora coYki A0A0D2WY30). Raw output:
`motif_scan_output.txt`.

## 1. Warts/LATS consensus motifs (HXRXXS/T)

F2UDK1 (714 aa) carries four HXRXXS motifs: HQRQRS (S152), HHRPSS (S283),
HQRHSS (S394) and HHRRHS (S423). The first lies N-terminal to the two WW domains
(189-222, 244-277), as YAP1 S127 does relative to its WW domains. This count matches
the published statement that "srYki has 4 putative Warts phosphorylation sites"
(PMID:38729842), supporting that F2UDK1 is the protein that review called srYki.
Motif presence is a regular-expression match only: phosphorylation has not been
tested.

Note: the canonical UniProt Yorkie sequence (Q45VV3) numbers its HXRXXS motifs at
88 and 145; the literature "S168" numbering refers to a different isoform/numbering.

## 2. TEAD-binding domain

The N-terminal YAP/Yki TEAD-binding segments contain the short motifs LxxLF (YAP1
alpha1 helix, LEALF 65; Yki LQALF 45) and PxSFF (YAP1 omega loop, PDSFF 92; Yki
PNSFF 72). Neither motif, nor SFF, occurs anywhere in F2UDK1. Local alignment of
the YAP1 (50-100) and Yki (20-80) TEAD-binding regions to the F2UDK1 N-terminus
(1-188) scored 25 and 23, no better than a control alignment of YAP1 50-100 to an
unrelated F2UDK1 region (500-714; score 27.5). We find **no recognizable
TEAD-binding motif** in F2UDK1. This agrees with PMID:38729842 ("srYki lacking
conserved residues within the alpha2 helix"), and is at odds with the 2012 statement
that all non-metazoan Yki homologs carry the N-terminal TEAD-interaction region
(PMID:22832104), which may have used a different gene model. Inconclusive for
whether srYki binds a TEAD protein: a divergent interface cannot be excluded by
motif search.

## 3. Which S. rosetta protein is the Yorkie ortholog?

PANTHER (TreeGrafter) places F2UDK1 in PTHR10316:SF68 (family "MEMBRANE
ASSOCIATED GUANYLATE KINASE-RELATED"), grafted to node PTN002569196, an
ecdysozoan node whose members are Drosophila CG42788, Anopheles AGAP003128 and a
Pristionchus gene (PANTHER 19 treeinfo API). Another S. rosetta WW protein,
F2U5K0 (PTSG_03848, three WW-domain matches, two HXRXXS-like matches), is the one
classified in the YAP1 family (PTHR17616:SF8).

Full-length local alignment scores (BLOSUM62; shuffled-sequence control in
parentheses, mean of 20):

| query | vs F2UDK1 | vs F2U5K0 |
|---|---|---|
| human YAP1 | 258.0 (98.7) | 194.5 (87.6) |
| Drosophila Yki | 226.5 (86.1) | 120.0 (74.8) |
| Capsaspora coYki | 307.0 (122.1) | 159.0 (88.0) |

F2UDK1 is the better match to all three Yorkie/YAP proteins. Much of this
similarity is in the WW domains, so the scores do not establish orthology on
their own. Together with the two-WW architecture and the four HXRXXS motifs, they
support the published assignment of PTSG_06057 as the Yorkie homolog, and indicate
that its PANTHER family placement is likely wrong. A phylogenetic analysis
(not done here) would settle it.
