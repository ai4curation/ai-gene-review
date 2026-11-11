# EML1: reproducible source, sequence and database evidence

The offline replay reconciles all 39 source annotations to 39 normalized GOA TSV rows, with no duplicate join groups. The separate bootstrap also verified the raw API context count, which this replay does not reconstruct. Qualifiers, evidence codes, reference IDs and WITH/FROM values participate in the join.

Official sequence reconstruction gives O00423-1 at 815 residues and O00423-3 at 834 residues; both match separately captured FASTAs. Human O00423 and mouse Q05BC3 displayed sequences exactly match their PANTHER MSA entries. This establishes identity, not equal activity of natural products or a match to every historical construct.

All three literal IBA assertions trace to IBD nodes on the human path: PTN001010531 for microtubule organization and mitotic spindle, and PTN000347035 for microtubule binding. The captured family table has nine records and no recorded loss on that path; this is a version-bounded table observation. Complete donor captures contain 28 mouse Q05BC3, 18 human O95834 (EML2), and 16 fly Q9VUI3 records. Experimental source grounding is preserved separately from inferred records.

GO:0008017 microtubule binding is an is_a descendant of GO:0015631 tubulin binding. The structured core uses the specific polymer-binding term, while its description separately records TAPE-mediated soluble-tubulin association from PMID:24706829. The ontology relationship does not collapse the distinct domains or ligand states demonstrated experimentally; the remaining distinction is also recorded as an ontology question. ARBA00044431 and ARBA00043642 predicates and outputs are reproduced, but exact target FunFam clause matching was not independently established.

The 37-record IntAct and 54-record BioGRID snapshots corroborate eight imported source-specific protein pairs. The FXR1 pair is resolved by BioGRID 3018756 and 3018857. A separate, explicitly selected BioPlex EML1-to-NUDC edge supplies corroboration; the subset is not a whole-network survey. These data distinguish source identities and assay methods but do not establish every pair as a direct native contact or transfer partner molecular functions to EML1.

The program generates these projections from the archived inputs; expected scientific decisions are not hardcoded. Primary experiments, calcium binding, affinity, endogenous human distribution and equivalence of products are outside its scope. No article bodies or figures are redistributed in the custom archive.
