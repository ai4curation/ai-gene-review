
## 2026-09-21 full-gene evidence re-review

All original source assertions were read and preserved, including source term IDs and evidence. Actual PTHR45640 v19 topology places both targets below PTN000897708: P02515 ends at PTN000163333, P02516 at PTN000163334. Current IBDs for nucleus, cytoplasm, heat response and refolding were recovered, with no loss on either target path. The obsolete unfolded-protein-binding IBD is absent from the current extract; that version difference does not establish functional loss. Exact paths, current node assertions and response hashes are stored in the project audit artifacts.

Full PMID:16572729 demonstrates purified client protection, client-small-Hsp complexes and recovery after addition of ATP-supplemented reticulocyte lysate. Exact Results excerpt: “Altogether, these results demonstrate that Hsp22, Hsp23, Hsp26, and Hsp27 can maintain heat-treated luciferase in a refoldable state, from which it can be refolded by other chaperones into an active enzyme.” Luciferase recovery was54.9±2.8% with Hsp22 and30.7±6.7% with Hsp23. Hsp23 required higher concentrations for comparable aggregation suppression. Hsp23 purification used urea; parallel Hsp22 purification controls support the comparison. The holding step is actual work in refolding, even when other chaperones drive later recovery.

Live GO:0140309 is active and named unfolded protein holdase activity. Its definition allows delivery to an acceptor molecule or to a location, so the previous inter-compartment-only interpretation was false. GO:0044183 does not require ATP hydrolysis; its comment distinguishes folding from holding a client unfolded. Existing obsolete source assertions remain untouched, with specific active replacements. No new redundant annotations or ontology terms were added. Core descriptions now use the active molecular function and contain biological content rather than a pending-ontology workflow.

Full PMID:26705243 distinguishes heat-induction qPCR, cellular refolding, and HSP70-knockdown experiments. The qPCR includes both genes, cellular refolding excludes Hsp22, and HSP70 knockdown tests Hsp27 and CG14207. An Hsp23-specific requirement for HSP70 was not directly tested. Full PMID:19715580 supports insect sHsp sequence relationships rather than a new biochemical assay.

Mitochondrial localization is established by full [PMID:10896659 author-deposited paper](https://www.researchgate.net/publication/12421892_The_Small_Heat_Shock_Protein_Hsp22_of_Drosophila_melanogaster_Is_a_Mitochondrial_Protein_Displaying_Oligomeric_Organization): Hsp22-specific antisera, S2 mitochondrial-marker colocalization after heat/recovery, and heterologous matrix fractionation/protease protection. Native-cell location and heterologous submitochondrial assays are distinguished. No universal nuclear-negative assay is established. [PMID:6772504 publisher abstract](https://www.sciencedirect.com/science/article/pii/0012160680903206) explicitly includes22-kDa Hsp among proteins in nuclear/chromatin/nucleolar fractions after heat shock; full identity and purity controls remain inaccessible. The Hsp22 nucleus call is UNDECIDED, with focused OpenScientist adjudication registered as conditional-nuclear-localization. Historical fractionation may be genuine or artifactual; neither conclusion is presumed.

The existing Falcon narrative/table was read and incorporated critically. Its mitochondrial and holdase synthesis is useful; localization shorthand does not establish exclusivity. Its 2018 interaction lead was verified in full PMID:29509794: Drosophila Hsp22 is expressed in human HeLa cells, and Hsp60/mtHsp70 affinity-capture association does not prove direct handoff to either partner or native-fly interactions. The oxygen-consumption and ATP-content changes do not make Hsp22 an ATPase. Stress and lifespan source abstracts14734639/15331597 identify distinct overexpression and loss-of-expression paradigms, respectively; organismal lifespan effects remain contextual.


## Recovery PR follow-up (2026-09-22)

Restored readable GO/PMID/PTN identifiers in curation prose. For DCV1, core
localization cites the recorded UniProt topology and SGD-attributed observation;
the unrelated Rim101 report sentence no longer supports plasma-membrane location.
For YAR1, unanswered report questions are not positive evidence. For SSQ1, the
located Nop1 association remains recorded while its generic binding label is removed.
The annotation changes apply only to the relevant gene; no inherited location is
rejected solely from its best-characterized compartment.
