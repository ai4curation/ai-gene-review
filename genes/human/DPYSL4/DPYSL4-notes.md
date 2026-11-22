# DPYSL4 review notes


## 2026-09-20 full-gene IBA re-review

All 17 annotations assessed: IBA cytosol, positive cyclic-amide and negative pyrimidine/dihydropyrimidinase assertions; broad catalytic mappings; cytoplasm; five protein-interaction rows; filamin binding; Reactome cytosol; nervous-system development.

The DPYSL4 UniProt caution and comparative CRMP2 structure/CRMP5 assay support loss of ancestral dihydropyrimidinase catalysis. Existing DPYSL2 OpenScientist report is incorporated as comparative evidence, not a target-specific assay. The cyclic-amide rejection and source NOT assertions remain.

Newly retrieved primary PMID:23443259 (full text) reports histone H4 deacetylation by mouse CRMP3/DPYSL4 and by purified full-length/truncated recombinant preparations; methods also name commercial DPYSL4 reagent. This is a different reaction from cyclic-amide hydrolysis. Broad GO:0016787 and GO:0016810 now UNDECIDED, not REMOVE based solely on missing ancestral catalytic residues.

Pending root-owned distinct adjudication: confirm target/construct species and identity, purity/contamination controls, reproducibility and relevance to human O14531 before restoring the broader hydrolase terms. No speculative HDAC NEW was added. Description scopes pseudoenzyme status to dihydropyrimidinase and records the separate reported activity with human uncertainty.

Filamin binding and neuronal-development source assertions remain accepted; abstract-only citations naming a family member were not used to invent misattribution claims. Generic protein-binding rows removed as uninformative, not biologically disproven.

Verified the proximate IBA PANTHER nodes from cached WITH/FROM fields and revised structured propagation metadata to match final decisions; no relationship-field reasoning, donor-count argument, or invented topology reconstruction was used.


## 2026-09-21: focused report incorporated and primary controls rechecked

Read the entire new CRMP3/deacetylase OpenScientist report. Independent read-only review by annotation_review_localization and root comparison with the full PMID:23443259 article support retaining GO:0016787/GO:0016810 as UNDECIDED. The paper tests full-length CRMP3, p54 and D domain; full-length has the strongest activity. HEK293 constructs are EGFP fusions purified with anti-EGFP; Sf9 constructs are His6/S-tagged and use native nickel affinity purification. The report conflates those procedures and incorrectly invokes truncation-only evidence. EGFP/empty-vector, inactive C-terminal-fragment, CRMP4-negative and HDAC6-positive controls and two expression systems are meaningful positive evidence.

The concrete remaining gap is intrinsic enzyme attribution: the native-H4 assay uses HEK293 whole-cell lysate (Methods; Fig4 calls the substrate a nuclear extract) and the protein preparation is not compositionally demonstrated to exclude an associated deacetylase. TSA sensitivity is consistent with the reaction and raises an alternative explanation, not proof of contamination. Loss of the ancestral dihydropyrimidinase metal center and NOT on that child activity do not negate every possible hydrolase reaction. No broad NOT is proposed.

Materials lists Abnova Cat.0980513, but no unambiguous assay/species/construct mapping was verified. Modern human products cannot establish the identity of that old reagent. The main series concerns cloned mouse CRMP3; no direct human assay is inferred. The provider's reported exact alignment identities and residue map have no delivered code/alignment artifacts and are not adopted as reproduced measurements. Native physiological importance, human transfer and catalytic attribution remain specific follow-up questions. No duplicate report was launched.
