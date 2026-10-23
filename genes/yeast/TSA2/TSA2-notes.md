# TSA2 (YDR453C, Q04120) notes

Module context: `glutathione_thioredoxin_redox_systems`, thiol_peroxidase_step, variant typical_2cys_prx (TSA1/TSA2), MF GO:0140824, BP GO:0042744, cytosol. Not present in the YeastPathways summary (no YeastCyc reaction rows; no RCA annotations in GOA). No S. cerevisiae GO-CAM contains TSA2 (gocams/index.tsv).

## Evidence
- Identity: typical 2-Cys Prx, AhpC/Prx1 subfamily; 196 aa; PANTHER PTHR10681:SF171 [UniProt:Q04120].
- Activity: recombinant Tsa2 and Tsa1 have similar kcat/Km for H2O2 and organic peroxides [PMID:15210711 "the recombinant proteins showed similar in vitro efficiencies (K(cat) /K(m)) in the removals of both kinds of peroxide"]; EC 1.11.1.24 [UniProt:Q04120]. Rate constant ~10^7 M-1 s-1 for H2O2, peroxidatic Cys47 pKa 6.3 [PMID:17210445 "pKa of the peroxidatic cysteine of Tsa1 and Tsa2 (Cys47) as 5.4 and 6.3, respectively"].
- Thioredoxin-supported: [PMID:10681558 "Three novel isoforms showed a distinct thiol peroxidase activity supported by thioredoxin"] (cTPx II = TSA2 in that nomenclature).
- Physiology: low abundance, peroxide-inducible; tsa2 null is sensitive to tBHP but H2O2-resistant (catalase compensation) [PMID:15210711 "these cells were highly sensitive to tert-butylhydroperoxide (TBHP)"].
- Hetero-oligomers with TSA1, functional in the cytosol [PMID:41807831 "these results confirm that Tsa1 and Tsa2 assembles into functional hetero-oligomers in the yeast cytosol"]; [PMID:41807831 "Even substoichiometric incorporation of Tsa2 strongly stabilizes the decameric state."].
- Chaperone switch (shared with TSA1) [PMID:15163410 "cPrxI and II, which display diversity in structure and apparent molecular weights (MW), can act alternatively as peroxidases and molecular chaperones"].
- Redundancy: quintuple Prx-null viable but oxidant-sensitive [PMID:15051715 "peroxiredoxin-null yeast cells were more susceptible to oxidative and nitrosative stress"].

## Reference issue
- PMID:9888818 (Jeong et al. 1999) describes "type II TPx" of 176 aa with Cys62/Cys120 and no homology to TPx I [PMID:9888818 "Comparison of the predicted sequence of 176 amino acids of type II TPx with that of the 195 residues of TPx, now renamed type I TPx"]. This is AHP1 (176 aa), not TSA2. UniProt cites it for the TSA2 alias "TPx type Ib", so the full text mentions TSA2. SGD's 2013 TSA2 rows from this paper (IMP GO:0034599, IDA GO:0051920) may stem from the old "TSA II" = AHP1 naming (PMID:10681558 calls AHP1 "TSA II/AHPC1"). IMP row marked UNDECIDED; IDA row accepted because the function is independently established.

## Decisions
- GO:0008379 (obsolete) rows -> MODIFY to GO:0140824.
- Bare protein binding (TSA1 interactor) -> REMOVE; the association is captured by GO:0051291 IPI.
- Chaperone/heat/protein stabilization/oligomerization -> KEEP_AS_NON_CORE.
- Core: GO:0140824 in cytosol, H2O2 catabolism, cell redox homeostasis.
