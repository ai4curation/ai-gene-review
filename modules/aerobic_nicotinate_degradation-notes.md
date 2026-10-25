# Aerobic nicotinate degradation audit

## 2026-10-25: boundary and literature search

The target is the six-reaction nicotinate-to-fumarate route through 6-hydroxynicotinate, 2,5-dihydroxypyridine, N-formylmaleamate, maleamate and maleate. Nicotinate uptake, cofactor maturation, transcriptional control and downstream fumarate metabolism are outside its catalytic boundary. Nicotine is a different substrate; shared lower-pathway enzymes do not demonstrate a complete nicotinate pathway.

Relevant comparative reviews identified are PMID:33281798 (2020, hybrid nicotine catabolism, including an explicit nicotinate comparison) and PMID:42618148 (2026, nicotinic acid metabolism in Bordetella). The latter is cached abstract-only and supports differences among Bordetella lineages rather than detailed enzyme assignments. Initial retrieval of PMID:33281798 encountered HTTP429; a later supported retry succeeded and cached full text. Both comparative references are now curated in the module. Module Perplexity research failed with insufficient quota; no provider report was fabricated. Existing real Falcon gene reports are being reused and critically checked against primary evidence.

The principal P. putida KT2440 study is PMID:18678916. Its full PMC text is available to manual reading although supported cache refreshes currently return the abstract. The initial seven representatives are being reviewed individually. Primary characterization distinguishes experimentally assayed NicD/NicF from the original homology assignment of NicE/MaiA. A conserved-residue numbering discrepancy in the old paper does not imply a new sequence or justify copying coordinates into the current record.

Cross-species leads and safeguards:

- Bordetella bronchiseptica NicC has direct mechanistic evidence (PMID:27218267 and PMID:30810301); current reviewed accession and historical construct/locus names need explicit linkage.
- Bordetella NicX has an early meeting-abstract report; the strength of target-specific evidence and current locus mapping are being assessed. PSEPK NicX structural work PMID:33637718 supersedes a purely modeled three-ligand Fe-site account.
- The first reaction may use differing fused/split electron-transfer architectures. Predicted Bordetella NicB1/NicB2 assignments in PMID:29485696 must not be described as individually purified-subunit experiments.
- Pseudomonas S16 Iso/MaiA is a useful directly assayed shared-reaction comparator. PMID:22530095 reports that S16 lacks nicAB and did not degrade nicotinate in the tested resting-cell assay; it must not become evidence of a complete native nicotinate route.
- PANTHER labels for the actual proteins are often misleading. The verified family placements must be combined with reaction-specific constraints; a label such as geranylgeranyl diphosphate reductase or aldehyde dehydrogenase does not establish the nicotinate chemistry.

The final module will retain only supported pathway representations and distinguish comparative proteins from demonstrated native route components. Family/variant modeling and step-specific evidence integration follow the ongoing gene reviews.

## Integration of completed gene reviews

All 12 member/comparator reviews are complete and retain 42 pre-existing annotation rows (including two previously proposed NEW rows); no new annotation rows were manufactured for this audit. Seven KT2440 proteins define the complete native route; RB50 NicC and NicX add independently qualified reaction representatives. BB1776, BB1783 and S16 Iso remain reviewed comparators outside the demonstrated full entry/route representation.

The scope is narrowed from Bacteria to Pseudomonadota (NCBITaxon:1224, current OLS label checked), reflecting the native route and cross-genus evidence. This is an evidence envelope with a complete enzyme-set constraint, not a universal trait or a clade-origin claim. The full PMC2516282 distribution discussion compares Pseudomonas with Burkholderiales; the 2018 Bordetella study supplies native pathway physiology. The two-component entry representation is explicitly limited to the characterized architecture. No guessed PAINT node or untested split complex is asserted.

Eight PANTHER subfamily identifiers were read from actual UniProt records and their exact official labels checked against panther.obo. All seven catalytic/subunit roles have FAMILY selectors with required function constraints; NicC spans two subfamilies. Reaction-specific free text replaces three overly broad GO molecular functions, while Rhea preserves exact chemistry. Every reaction and all five edges carry primary findings; the comparative review is also used at the shared lower steps.

Source caveats: PMID:18678916 Methods says maleate for the NicD product, contradicting its own Results/diagram (maleamate). PMID:38104959 introduction says 2,6-DHP but its scheme/experiments establish 2,5-DHP; the structural ligand is a contaminant. RB50 NicC accession A0A0H3LKL4 is explicit in the 2019 paper despite locus-name variation. RB50 NicX has meeting-abstract product evidence, not a full structural paper. The S16 negative nicotinate test is condition-specific. Full cached text is available for the 2020 comparative review; the 2026 Bordetella review remains abstract-only.

Integration QA confirmed NicC/NicX chemistry and scope. Ontology gaps and uneven source coverage are recorded as notes, leaving only the unresolved entry-complex division of labor as a biological knowledge gap. Rhea evidence states stoichiometry; primaries support FAD/Fe dependence.

## PR 5544 follow-up (2026-10-25)

Live QuickGO checks on 2026-10-25 found no exact terms using EC 1.17.2.1, EC 3.5.1.106, EC 3.5.1.107 or the corresponding substrate-specific activity names. Nicotinate dehydrogenase GO:0050138 remains the NADP-specific reaction. All 14 direct children of GO:0016725 were inspected: acceptor classes include NAD/NADP, oxygen, disulfide, quinone and iron-sulfur protein, but no generic cytochrome-acceptor child. GO:0047111 is formate-specific and cannot substitute. Thus GO:0016725 remains the supported parent for cytochrome-linked NicAB; search non-retrieval is reported as a current search result, not proof that no future ontology term can exist.

Gene follow-up adds one supported RB50 NicC process proposal, removes the contradicted KT2440 MaiA tetramer transfer, and retains unresolved NicD membrane localization without off-topic evidence. Core pathway reactions, family selectors and taxonomic scope are unchanged. Original annotation fields are preserved. Broad RB50 entry-comparator activities remain explicitly less resolved than assayed KT2440 NicAB. Module changes are editorial citation/spacing corrections only.
