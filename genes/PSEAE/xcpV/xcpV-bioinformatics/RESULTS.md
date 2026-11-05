# PAINT node leaf composition for the XcpS, XcpW and XcpV seed nodes

Script: `node_leaves.py` (run `python3 -I node_leaves.py .` in this folder).
It queries the QuickGO annotation API for every annotation whose WITH/FROM is
the PAINT node, for the node's IBD term, and classifies each leaf protein by
its UniProt protein name or gene symbol (coarse, name-based; most names are
automatic). Raw rows: `node_leaves.tsv`; summary: `node_summary.txt`.
Run date: 2026-10-28 (QuickGO current release).

## Summary (copied from node_summary.txt)

PTN000768597 GO:0015628 (XcpS/GspF seed): 911 proteins; T2SS-named=846, T4P/MSHA/TCP-named=7, generic/other=58
PTN002218419 GO:0015628 (IBA node on XcpW/GspJ in current GOA): 618 proteins; T2SS-named=542, T4P/MSHA/TCP-named=2, generic/other=74
PTN002446812 GO:0015628 (XcpW/GspJ seed node in PAINT seed file): 0 proteins;
PTN002446181 GO:0015627 (XcpV/GspI seed): 49 proteins; T2SS-named=14, T4P/MSHA/TCP-named=14, generic/other=21

## Reading

- PTN000768597 (GspF): leaves are overwhelmingly named as T2SS GspF proteins; a
  handful are named PilC/HofC/MshG (type IV pilus or MSHA platform proteins of
  the same PTHR30012 family). Node term fits the clade, with minor leakage.
- PTN002218419 (GspJ): leaves are overwhelmingly GspJ-named; the IBA on XcpW in
  current GOA comes from this node, not from PTN002446812.
- PTN002446812: no current QuickGO annotation cites this node, although the
  PAINT seed file lists it as the XcpW seed node. The seed node and the
  propagating node differ (PANTHER tree version change is the likely cause; not
  verified).
- PTN002446181 (GspI): of 49 leaves only 14 are named as T2SS proteins; 14 are
  named type IV pilus PilV, MSHA MshD or pilin (including Neisseria
  gonorrhoeae NGO_0453 PilV, a type IV pilus minor pilin), and 21 carry only a
  generic prepilin-type domain name. The node appears to span the GspI/PilV
  split, so T2SS terms are propagated to type IV pilus minor pilins.

Caveat: classification is by name only and does not establish function.
