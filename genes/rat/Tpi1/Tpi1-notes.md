# Tpi1 review notes

## Re-review 2026-10-10

- GOA refresh added three rows: GO:0004807 triose-phosphate isomerase activity IBA (PTN000474559, donors include rat Tpi1 RGD:3896 itself), GO:0004807 ISO from human TPI1 (UniProtKB:P60174; donor-split of the mouse MGI:98797 ISO row), and GO:0046166 glyceraldehyde-3-phosphate biosynthetic process IBA. All ACCEPT [UniProtKB:P48500 "Triosephosphate isomerase is an extremely efficient metabolic enzyme that catalyzes the interconversion between dihydroxyacetone phosphate (DHAP) and D-glyceraldehyde-3-phosphate (G3P) in glycolysis and gluconeogenesis."].
- Two rows retired by GOA (kept, sentence added): GO:0005829 cytosol IBA (KEEP_AS_NON_CORE) and GO:0005515 protein binding IPI PMID:16170200 (REMOVE).
- GO:0005515 protein binding (IPI, PMID:16170200): kept REMOVE but reworded per the protein-binding policy: the term is uninformative and removal does not mean the Kir6.2 interaction is false [PMID:16170200 "we identified two potential interacting proteins to be the glycolytic enzymes, glyceraldehyde-3-phosphate dehydrogenase (GAPDH) and triose-phosphate isomerase"]. No replacement MF proposed because the abstract defines no specific activity for Tpi1 in the K(ATP) complex.
- GO:0031625 ubiquitin protein ligase binding (ISO from human TPI1): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. The donor annotation is an IPI from a Parkin TAP/MS screen [PMID:19725078 "Tandem affinity purification/MS revealed 14 potential interactants of Parkin"]; added propagation_review (SOURCE_WEAK_OR_INFERRED). The human TPI1 review marks the source row the same way. The legacy row also carried a summary copied from a gluconeogenesis row; corrected.
- Replaced 21 stale UniProt quotes (UniProt rewrote the FUNCTION text; old "FUNCTION: Triosephosphate isomerase catalyzes the interconversion..." no longer present) with the current FUNCTION sentence. Checker: 0 stale.
- Description rewritten as standalone biology (removed review/curation commentary).
- Open question: does Tpi1 bind Kir6.2 directly in native cardiac membranes, and does it affect K(ATP) gating (only GAPDH and pyruvate kinase effects were shown in the abstract)?
