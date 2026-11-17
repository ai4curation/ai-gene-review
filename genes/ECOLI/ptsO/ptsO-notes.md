# ptsO / NPr (E. coli K-12, P0A9N0) notes

## Provenance

- Deep research could not be generated: no deep-research provider API key is
  configured in this session, so `just deep-research ECOLI ptsO` was not run and no
  `-deep-research-*.md` file exists. The review is based on the UniProt record, the
  GOA table and the cached abstracts of PMID:7876255, PMID:10473571, PMID:21605551
  and PMID:19400808.

## Findings

- NPr is the HPr paralogue encoded in the rpoN operon [PMID:7876255 "Two of these
  genes encode proteins homologous to Enzyme IIAFru and HPr of the
  phosphoenolpyruvate:sugar phosphotransferase system. We designate these proteins
  IIANtr (ptsN) and NPr (npr)."].
- Purified NPr exchanges phosphate with PTS proteins in vitro [PMID:7876255 "Purified
  IIANtr and NPr exchange phosphate appropriately with Enzyme I, HPr, and Enzyme IIA
  proteins"].
- EI(Ntr) phosphorylates NPr but not HPr [PMID:10473571].
- Dephosphorylated NPr binds LpxD and is proposed to inhibit lipid A synthesis
  [PMID:21605551 "unphosphorylated NPr decreases lipid A biosynthesis by inhibiting
  LpxD activity"]. This is an accessory, phosphostate-dependent output.

## Curation decisions

- GO:0009401 IBA is removed (NPr is the EI(Ntr)-specific carrier of a regulatory
  chain, PAINT node PTN002135312 is seeded by the sugar-PTS HPr proteins).
- GO:0016772 rows are refined to GO:0016775 (phosphoryl transfer from NPr His16 to the
  IIA(Ntr) histidine, a nitrogenous acceptor). GO has no dedicated term for the
  PTS phosphocarrier step.
- Bare protein binding with LpxD is replaced by enzyme inhibitor activity.
