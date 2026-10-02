# AKR1D1 primary-source and PAINT checks

All 41 original source rows, UniProt chemistry, source abstracts and available Reactome event summaries were reviewed. Full primary studies of disputed substrate scope were read. Source annotation fields are preserved; no NEW row is added.

## Direct enzyme and structure evidence

PMID:21255593 full PMC article: recombinant purification, substrate/product methods, all Results, kinetic tables and Discussion were read. Exact excerpt: “5β-Reduced products were identified directly with all the C18-C27 steroid substrates except for aldosterone.” The aldosterone product lacked an authentic standard and was inferred from chromatography. Purified AKR1D1 reduced androgen, progestogen, glucocorticoid and bile-acid intermediates; substrate inhibition and assay conditions explain some earlier apparent negatives. Testosterone catalytic efficiency was comparable to the tested bile-acid intermediate rather than negligible. These are direct enzyme steps in hormone metabolism, not merely downstream endocrine phenotypes.

PMID:18407998 full PMC structural study: NADP+/substrate complexes and active-site mutagenesis were read. Glu120 rather than the histidine of other AKRs helps position/protonate the Delta4-3-ketosteroid for C4–C5 reduction. Y58F and E120A mutants lost measured activity. The unusual steroid geometry provides a mechanistic distinction from C3 carbonyl reduction, but a structural explanation of predominant chemistry is not a universal negative test of every aldose or alcohol-forming side reaction.

PMID:7508385 accessible abstract reports strong bile-acid-precursor reduction and smaller but significant cortisol/testosterone turnover in transfected COS cells. It does not justify excluding androgen/C21-steroid metabolism. Its full text was not obtained, so the broader digestion interpretation is unresolved rather than confidently rejected from the abstract.

PMID:11342103 accessible abstract and UniProt reaction mapping were checked. RHEA:53484 records a 17-ketosteroid/alcohol conversion linked to this citation, whereas the abstract emphasizes steroid 5beta-reduction. The full relevant experiments were not accessible. Leave the exact 17beta-HSD and independently inferred alcohol-dehydrogenase capacities unresolved; do not treat steroid specialization as proof of loss.

## Reaction mapping and ancestry

Live GO:0047086 is oxygen/NADPH-dependent progesterone-to-testosterone-acetate monooxygenation, not ordinary ketosteroid reduction. PTHR11732 actually places this at PTN000199026, which lies on the target P51857 path to PTN002482523. Live QuickGO source IDAs for human C1/C2/C3 cite PMID:21232532. Its expression-focused abstract does not prove the absence of an assay in the full paper. Root PTN000198921 places aldose reduction; that term requires aldose/alditol chemistry rather than merely an AKR fold. PTN000199134 places androgen metabolism with target P51857 experimental grounding; inclusion of the target is valid descendant evidence, not circularity. AKR1D1-paint-lineage.json stores the exact path and node-matched IBD rows. No matching target-path loss was recovered.

Five available Reactome events, R-HSA-192033, 192067, 193746, 193821 and 193824, explicitly convert a Delta4-3-oxosteroid to a 5beta-3-oxosteroid with NADPH. The carbonyl remains intact; alcohol dehydrogenase is the wrong reaction mapping for those events. GO:0047787 is the direct replacement. R-HSA-193755 could not be fetched (both content page and ContentService returned 404); its molecular-function assertion remains UNDECIDED rather than assuming the event has exactly the same chemistry. Its cytosol annotation is independently established by the other source events and primary evidence.

Bile-acid synthesis is one branch of cholesterol breakdown and involves monocarboxylic-acid products. A catalyst can participate by acting on a pathway intermediate; it need not directly bind cholesterol or the final bile acid. Broad cholesterol-catabolic and monocarboxylic-acid-metabolic terms are therefore retained alongside specific bile-acid synthesis. Digestion remains a separate process-scope question.

No target-specific existing OpenScientist report was found. The aldose-monooxygenase-and-alcohol-reduction-specificity request is gated under launcher session 45234, without assuming remote submission. These questions remain open for report and human review.
