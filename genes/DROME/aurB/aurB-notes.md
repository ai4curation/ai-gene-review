# aurB (Drosophila melanogaster) curation notes

Accession: Q9VKN7 (Aurora kinase B; FBgn0024227).

Deep research: `aurB-deep-research-falcon.md` (falcon; the wrapper logged a 600 s timeout but the run completed and wrote the file). It confirms aurB (= ial) is distinct from the centrosomal Aurora A, and adds that the CPC activates Polo at centromeres via Aurora B phosphorylation of Polo T182. Consistent with removing the Aurora A-derived centrosome/spindle-pole IBA rows.

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
- Centrosome IBA row removed: donors are Aurora A-type kinases; fly Aurora B is a passenger (spindle pole: see revision below).
- Midbody abscission IMP (PMID:23948252) modified to negative regulation of mitotic cytokinesis (sign).
- Post-translational protein modification modified to protein phosphorylation.
- Correct-but-general rows (nuclear division, sister chromatid segregation, protein kinase activity, chromosome, spindle, cytoskeleton, chromatin organization, chromosome condensation) modified to the specific terms aurB already carries (or meiotic chromosome condensation for the oocyte screen).
- Revision after PR review: spindle pole IBA changed from REMOVE to UNDECIDED. Its donors are PTN000681968 plus mouse Aurka, human/dog/bovine AURKA, Xenopus Aurora A, C. elegans air-1, Dictyostelium Aurora and mouse Aurkb (MGI:107168), so the node is not purely Aurora A; fly Aurora B has no reported spindle-pole localization, but that absence is not sufficient to remove it. The centrosome IBA REMOVE stands (all donors Aurora A-type).
- Midbody abscission -> negative regulation of mitotic cytokinesis loses the abscission step; GO has no negative regulation of midbody abscission term.
