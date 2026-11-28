# KDM5D curation notes

Automated Falcon deep research, with the `perplexity-lite` fallback, was unavailable in this worktree. This note records the manual evidence synthesis used for the KDM5D review.

KDM5D/SMCY is the Y-linked JARID1-family H3K4me2/3 demethylase. It is covered by the founding KDM5 family demethylase paper [PMID:17320160]. Komura et al. showed that KDM5D physically associates with nuclear androgen receptor and regulates AR transcriptional activity by demethylating H3K4me3 at active marks in prostate-cancer cells [PMID:27185910]. Li et al. showed a distinct ZMYND8-JARID1D corepressor mechanism in which the two proteins co-occupy metastasis-linked genes and KDM5D knockdown raises H3K4me3 while reducing ZMYND8 occupancy [PMID:27477906].

The GOA `GO:0050681` row uses `obsolete nuclear androgen receptor binding`. Live QuickGO marks that term obsolete and recommends `GO:0016922 nuclear receptor binding` with androgen receptor supplied as the input, so the row is modified to the non-obsolete molecular-function parent rather than kept as the obsolete pre-composed AR-binding term.
