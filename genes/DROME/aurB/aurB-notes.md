# aurB (Drosophila melanogaster) curation notes

Accession: Q9VKN7 (Aurora kinase B; FBgn0024227).

Deep research: `just deep-research-falcon DROME aurB --fallback perplexity-lite` failed
(falcon timed out after 600 s; perplexity provider not available). Literature below is from
the cached publications.

## Literature journal

- RNAi in S2 cells: polyploidy, partial condensation, loss of H3S10ph and Barren recruitment,
  lagging chromatids, cytokinesis failure, reduced central-spindle microtubules
  [PMID:11266459 "Cells depleted of the Aurora B kinase show only partial chromosome condensation at mitosis"]
  [PMID:11266459 "This is associated with a reduction in levels of the serine 10 phosphorylated form of histone H3 and a failure to recruit the Barren condensin protein onto chromosomes"]
  [PMID:11266459 "The majority of treated cells also fail to undertake cytokinesis"].
- Passenger localization [PMID:11266459 "aurora B encodes a passenger protein that associates first with condensing chromatin, concentrates at centromeres, and then relocates onto the central spindle at anaphase"]
  [PMID:11266459 "the enzyme is essentially confined to the midbody during cytokinesis"].
- Substrates: MEI-S332 [PMID:16824953 "MEI-S332, which is also an excellent in vitro substrate for Aurora B kinase"];
  Lgl [PMID:25484300 "The Aurora A and B kinases directly phosphorylate Lgl to promote its mitotic relocalization"];
  Cyclin B [PMID:23948252 "This inhibition is mediated by an Aurora B-dependent phosphorylation of Cyclin B"].
- Abscission timer in the germline: Aurora B inhibits abscission (direction = negative regulation)
  [PMID:23948252 "Aurora B and Survivin regulate the number of germ cells in each Drosophila egg chamber by inhibiting abscission during differentiation"]
  [PMID:25647097 "our results indicate a negative regulation of Shrub by the Aurora B kinase during GSC abscission"].
- Oocyte condensation screen hit, off-target not excluded for Aurora B shRNA (PMID:25501812).

## Decisions

- Kinase activity rows accepted; protein kinase activity, ATP binding kept as non-core.
- Centrosome and spindle pole IBA rows removed: donors are Aurora A-type kinases; fly Aurora B is a passenger.
- Midbody abscission IMP (PMID:23948252) modified to negative regulation of mitotic cytokinesis (sign).
- Post-translational protein modification modified to protein phosphorylation.
