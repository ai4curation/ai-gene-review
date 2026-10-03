# dsbA notes

## 2026-10-02

Falcon deep research could not run in this EC2 worktree because `agentapi` was
not on `PATH` and no supported provider API key was available. These manual
notes therefore use the fetched UniProt record, the GOA-seeded PubMed cache, and
the DsbAB module literature.

DsbA is the soluble periplasmic oxidase arm of the DsbA/DsbB oxidative-folding
relay. The discovery paper found that `dsbA` mutants secreted beta-lactamase,
alkaline phosphatase, and OmpA in forms that "largely lack disulfide bonds",
and identified DsbA as a 21 kDa periplasmic Cys-Pro-His-Cys protein resembling
known disulfide oxidoreductases [PMID:1934062]. Purified DsbA stimulated
disulfide bond formation in reduced E. coli alkaline phosphatase and reduced
bovine ribonuclease A in vitro, directly supporting a DsbA oxidoreductase
activity toward folding substrates [PMID:1429594].

Mechanistically, oxidized DsbA donates its active-site disulfide to substrate
cysteines and becomes reduced. Kadokura and Beckwith detected DsbA-PhoA
mixed-disulfide intermediates in vivo and concluded that co-translational
disulfide formation by a thioredoxin-family member proceeds through the
enzyme-substrate mixed disulfide [PMID:19766568]. DsbB then reoxidizes DsbA:
the DsbB-DsbA crystal structure describes DsbB as the E. coli membrane protein
that oxidizes the periplasmic dithiol oxidase DsbA [PMID:17110337], and an
independent trapped ternary complex showed wild-type DsbB, Q8, and DsbA
covalently linked in a DsbB reaction intermediate [PMID:18775700].

The historical `protein disulfide isomerase activity` rows should not be read
as assigning DsbA to the DsbC/DsbD repair branch. The in vivo and in vitro DsbA
evidence supports disulfide introduction into exported substrates; DsbC/DsbD
reduction and isomerization of incorrect disulfides sit beside, not inside, the
DsbA oxidase step. Generic DsbA-DsbB and DsbA-PhoA `protein binding` rows are
real physical intermediates but are less informative than the corresponding
redox function.
