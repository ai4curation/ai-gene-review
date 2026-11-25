# PP_5276 curation notes

Q88CA5 is an unreviewed two-PLD-domain protein assigned to PANTHER
PTHR21248:SF12, the ClsC subfamily
[UniProtKB:Q88CA5, "PTHR21248:SF12; CARDIOLIPIN SYNTHASE C"]. Current UniProt
retains a generic phospholipase D-family product name and does not assign an
exact reaction.

The characterized E. coli ClsC route is chemically distinct from ClsA/ClsB:
ClsC uses phosphatidylethanolamine and phosphatidylglycerol, and loss of all
three synthases eliminates detectable cardiolipin
[PMID:22988102, "The ΔclsABC mutant lacks detectible CL"]. The same study shows
that the YmdB-ClsC system uses PE as phosphatidyl donor
[PMID:22988102, "the combined YmdB-ClsC used PE as the phosphatidyl donor"].

These family and domain data make Q88CA5 a credible PSEPK ClsC candidate, but
they do not establish the PE+PG reaction in KT2440. Broad
phosphatidyltransferase activity can be retained; exact ClsC activity and the
cardiolipin process require biochemical or genetic confirmation.

## 2026-11 update

The HKD motif scan (`PP_5276-bioinformatics/RESULTS.md`) shows that both PLD catalytic
motifs are intact (H170 and H414), at a spacing comparable to E. coli ClsC. Together with the
PTHR21248-wide cardiolipin biosynthesis node (PTN000478698, which includes E. coli ClsC
among its seeds), this is enough to accept the GO:0032049 process row, which was
previously UNDECIDED. The exact reaction stays at GO:0030572 phosphatidyltransferase
activity, because the phosphatidyl donor is untested. Q88CA5 is therefore not used as a
representative of the module's PE-plus-PG ClsC (GO:0090483) annoton; it is listed in the
module knowledge gaps instead.
