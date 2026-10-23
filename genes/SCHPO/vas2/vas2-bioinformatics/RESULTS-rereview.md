# vas2 (Q9P7N2) PANTHER subfamily placement (re-review, 2026-10-21)

Script: `panther_subfamily_rereview.py` (live query of the PANTHER 19 geneinfo service; raw output in
`panther_subfamily_rereview.tsv`).

## Result

Q9P7N2 (vas2/aps1) is assigned to PTHR11753:SF5 AP COMPLEX SUBUNIT SIGMA.

S. cerevisiae APS1 (P35181) is also assigned to PTHR11753:SF5, the same subfamily as vas2.

Human AP1S1 (P61966) is in PTHR11753:SF14, AP1S2 (P56377) in SF45 and AP1S3 (Q96PC3) in SF18. The
AP-2 sigma chains (yeast Q00381, human P53680) are in SF6, and the AP-3 and AP-4 sigma chains are in
SF2, SF12 and SF57.

## Interpretation

The fungal AP-1 sigma subunits (pombe vas2 and budding yeast APS1) share a PANTHER subfamily that is
separate from the AP-2, AP-3 and AP-4 sigma subfamilies. This places vas2 among AP-1-type sigma chains
rather than with the other adaptor complexes. The vertebrate AP-1 sigma paralogs fall in separate
subfamilies, so properties specific to them (for example tissue-specific AP1S2 or AP1S3 functions) are
not transferred. Properties shared by all AP-1 sigma chains, such as forming a hemicomplex with the
gamma subunit, are consistent with this placement.

The only PAINT node in the cached PTHR11753 PAINT table is PTN000204281. It carries GO:0016192
vesicle-mediated transport (P) and GO:0043231 intracellular membrane-bounded organelle (C). Neither
AP-1 adaptor complex nor clathrin binding is propagated from that node.
