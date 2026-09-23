# acgA focused report incorporation, 2026-09-20

The complete [OpenScientist report](acgA-hypotheses/function-hypothesis-go-0001653/openscientist.md)
and its decision/provenance CSVs were read after the full-gene re-review.
GO:0001653 remains **UNDECIDED**, and the report reference is **DISPUTED**.
No source annotations were changed and no new report was requested.

The report usefully collects the intramolecular osmosensor reconstitution
(PMID:14718564), spore-germination phenotype (PMID:8798577), CHASE architecture
and natriuretic-receptor descendant evidence for the ancestral assertion. Its
explicit caveat is: “no such negative binding assay exists.” These observations
do not show that ACG has lost every peptide response.

The report's stronger claim — “no primary study links it to ACG” — omits
PMID:21602484. The cached primary abstract and discussion state: “SDF-1 apparently
acts through the adenylyl cyclase ACG to activate the cyclic AMP (cAMP)-dependent
protein kinase A (PKA) and trigger the production of more SDF-1.” The discussion
also describes acgA-null strains forming fruiting bodies and secreting SDF-2,
which argues against loss of SDF-1 secretion being merely an early developmental
block. The cache lacks a complete Results extraction, and attempted alternate
PMC/Europe PMC retrieval was blocked. Direct ACG/SDF-1 binding remains unresolved;
pathway dependency is not itself receptor recognition. The report's assertion
that the two proteins act only at different stages is contradicted by this
terminal-differentiation work and the prespore role of ACG.

The PAINT table was re-read. **PTN000229249 is a node in PTHR11920**, not a family
ID as labeled in the report. GO:0001653 has an IBD there. At Dictyostelia node
PTN000938100, IRDs explicitly block GO:0004383, GO:0006182 and GO:0007168, while
adenylate cyclase receives an IBD. There is no corresponding peptide-receptor
IRD. This is a deliberate separation of catalytic/signaling functions in the
tree, not an automatic similarity transfer that can be rejected because only
other descendants have ligand-binding experiments.

The remaining human follow-up is the original concrete question: whether ACG
recognizes SDF-1 itself or is activated downstream of another receptor. The
existing report has been fully incorporated with its limitations; another
identical report would not resolve the missing experiment.
