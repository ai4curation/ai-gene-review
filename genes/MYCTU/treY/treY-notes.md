# treY (Rv1563c, P9WQ21) curation notes

- Deep research: no provider API keys were available in this session, so no
  `-deep-research-<provider>.md` was generated. The review rests on the
  UniProt record, GOA, cached PMID:10658666 (abstract only) and Reactome.
- De Smet et al. 2000 demonstrated three trehalose pathways in mycobacteria,
  including TreY-TreZ [PMID:10658666 "from glycogen-like alpha(1-->4)-linked
  glucose polymers (the TreY-TreZ pathway)"].
- P9WQ21 is the sole seed of PAINT node PTN008498486 (PTHR10357) for
  GO:0047470, GO:0005992 and GO:0030980
  [file:interpro/panther/PTHR10357/PTHR10357-paint.tsv].
- Reactome places the TreY reaction in the cytosol; the compartment was fetched
  with `treY-bioinformatics/reactome_compartment.py`
  [file:MYCTU/treY/treY-bioinformatics/RESULTS.md "compartment: cytosol"].
- Alpha-glucan catabolism kept as non-core; trehalose biosynthesis is core.
