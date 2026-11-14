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


## 2026-11-06 independent annotation audit

The original annotation payloads, including inherited NEW proposals, and frozen UniProt/GOA bytes were preserved. Every row and the core synthesis were reassessed. An initial provider-unspecified invocation was rejected by the CLI; the subsequent explicit Falcon request genuinely reached the provider and failed HTTP403 authentication. No provider report was written. PAINT lineage checks completed after retrying a concurrent cache-download race for the E. coli targets; no IRD/IKR loss was found.

Official QuickGO defines GO:0015035 as “Catalysis of the reaction: a protein with reduced sulfide groups = a protein with oxidized disulfide bonds.” Its reversible equation includes physiological protein oxidation despite the reductase label. GO:0015035 is a descendant of GO:0015036 and GO:0016491. GO:0016672 instead specifies a sulfur-containing donor and quinone acceptor; it is not a descendant of GO:0015035 or GO:0009055. These are distinct specificity axes, not interchangeable granularity levels. Definitions and is_a/part_of ancestor responses were saved in the ignored original-five audit cache from https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015035 and corresponding term/ancestors endpoints.

The oxidative core is directly supported by purified-substrate assays [PMID:1429594: “Purified DsbA markedly stimulated disulfide bond formation of E. coli alkaline phosphatase”] and full-text mixed-disulfide intermediates [PMID:19766568]. A separate assay establishes actual isomerization by reduced DsbA [PMID:8155639: “This conversion is the result of breaking and re-forming two disulfide bonds.”; “Kinetic analysis of the reaction yielded a Km of 43 microM and a kcat of 0.2 min-1.”]. The quantitative catalysis and undetectable uncatalyzed reaction warrant KEEP_AS_NON_CORE, not deletion or replacement of the isomerase claim. The reduced-enzyme preparation and artificial IGF-I substrate bound the observation; no native IGF-I pathway is inferred. The full-text native study assigns DsbA mainly to oxidation and DsbC to isomerization [PMID:8917542]. The original1934062 full text remains inaccessible, so the review does not claim it excludes rearrangement. Antibiotic-response rows remain UNDECIDED: the7628442 abstract discusses DsbD and other dsb mutants, while the exact DsbA assay table was not recovered; title focus is not proof of misattribution.

Current action counts: {"ACCEPT": 8, "KEEP_AS_NON_CORE": 2, "MODIFY": 4, "NEW": 1, "REMOVE": 2, "UNDECIDED": 2}.
