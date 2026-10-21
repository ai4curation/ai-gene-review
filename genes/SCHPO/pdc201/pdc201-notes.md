# pdc201 (SPAC3G9.11c, UniProt O42873, PDC4_SCHPO) notes

- Clusters with ScPdc1/5/6 [PMID:25102102 "The Pdc201 and Pdc202 cluster together, along with three reported PDCs of S. cerevisiae (ScPdc1, 5, 6;"]. PANTHER PTHR43452:SF36.
- Stationary-phase induction via Phx1 [PMID:25102102 "Expression of pdc201+ and pdc202+ genes increased markedly during stationary phase, by about 500-fold and 50-fold, respectively."].
- PDC activity in stationary cells is Phx1 dependent [PMID:25102102 "PDC enzyme activity increased during stationary phase in wild type, but decreased in the mutant"].
- Protein up from ~7,000 to ~52,000 copies/cell in quiescence [PMID:25102102 "Pdc201 increases from ~7000 copies per cell during growth to ~52,000 copies during quiescence"].
- Chronological survival: deletion lowers, overexpression raises [PMID:25102102 "the Δpdc201 and Δpdc202 mutations reduced cell viability in the stationary phase"]; [PMID:25102102 "overproduction of either Pdc201 or Pdc202 increased the long-term viability of both the wild type and Δphx1 mutant"].
- UniProt: no gene name; fetched with `-u O42873`. Cytoplasm + nucleus from ORFeome.
- GO-CAM gomodel:678073a900000393: enables GO:0004737, part_of GO:0019660; the pdc201 activity has RO:0002413 (provides input for) edges to downstream activities, and the phx1 activity has RO:0002407 causal edges to the pdc activities.
- Review: nucleus rows KEEP_AS_NON_CORE; lifespan phenotypes not turned into NEW annotations (downstream of metabolic activity).
