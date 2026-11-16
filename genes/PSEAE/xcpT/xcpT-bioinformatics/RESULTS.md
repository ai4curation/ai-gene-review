# PAINT node leaf composition for the XcpT/XcpU/HxcT and XcpQ/HxcQ/XqhA seed nodes

Script: `node_leaves.py` (run `python3 -I node_leaves.py .` in this folder).
It queries the QuickGO annotation API for every annotation whose WITH/FROM is
the PAINT node, for the node's IBD term, and classifies each leaf protein by
its UniProt protein name or gene symbol (coarse, name-based; most names are
automatic). Raw rows: `node_leaves.tsv`; summary: `node_summary.txt`.
Run date: 2026-11-05 (QuickGO current release).

IBD seeds (from `.cache/paint/IBD.gaf`, column 8):

- PTN000764351 GO:0015627: Q00514 (XcpT), Q9I5P4 (PA0681/HxcT), Q00515 (XcpU)
- PTN000764351 GO:0015628: Q00515 (XcpU), Q00514 (XcpT)
- PTN000768388 GO:0015627: P35818 (XcpQ), Q9I5P0 (PA0685/HxcQ), Q9I2M7 (XqhA)
- PTN000768388 GO:0015628: P35818 (XcpQ)

## Summary (copied from node_summary.txt)

PTN000764351 GO:0015627 (XcpT/XcpU/HxcT pseudopilin node): 642 proteins; T2SS-named=639, T4P/MSHA/TCP-named=2, generic/other=1
PTN000764351 GO:0015628 (XcpT/XcpU/HxcT pseudopilin node): 642 proteins; T2SS-named=639, T4P/MSHA/TCP-named=2, generic/other=1
PTN000768388 GO:0015627 (XcpQ/HxcQ/XqhA GspD secretin node): 181 proteins; T2SS-named=132, T4P/MSHA/TCP-named=1, generic/other=48
PTN000768388 GO:0015628 (XcpQ/HxcQ/XqhA GspD secretin node): 22 proteins; T2SS-named=19, generic/other=3

## Reading

- PTN000764351 (PTHR30093, GspG-type major pseudopilins): 601 of 642 leaves
  are named "Type II secretion system core protein G" and almost all others
  carry GspG/GspH names. Only two leaves are named as pilus proteins: Vibrio
  cholerae TcpA (Q60153, toxin-coregulated pilin) and Shewanella MshD
  (Q8EA06, MSHA minor pilin). The node term fits the clade, with negligible
  leakage. XcpU (a GspH minor pseudopilin) sits under this GspG node because
  PANTHER assigns it to PTHR30093:SF44; the T2SS terms are true of it as well.
- PTN000768388 (PTHR30332, GspD secretins): 132 of 181 leaves carry T2SS or
  GspD names, one is named "Type IV pilus assembly protein PilQ" (EDD73_1057),
  and 48 carry only domain names (NolW-like, secretin-like, LysM, SPOR). Many
  of the domain-named leaves are from Planctomycetota, Verrucomicrobiota and
  other lineages whose secretins have not been assigned to a system. The node
  term fits the named majority; whether the domain-named minority are T2SS
  secretins cannot be told from names.

Caveat: classification is by name only and does not establish function. I did
not inspect the tree topology.
