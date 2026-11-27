# ARHGAP29 review notes

ARHGAP29 (PARG1; human UniProt Q52LW3) is a Rho-family GAP. The original [PARG1 study](https://pubmed.ncbi.nlm.nih.gov/9305890/) reports hydrolysis-accelerating activity with preference for Rho over Rac/Cdc42. Activation refers to the substrate's GTPase reaction; the resulting GDP-bound state reduces signaling. The current [GO:0005096 definition](https://amigo.geneontology.org/amigo/term/GO:0005096) already includes Rho-GAP activity, so an obsolete Rho-specific identifier is unnecessary. One principal GAP core is used; no NEW annotation or downstream developmental process is proposed.

## Sources and read scope

The complete normal PMID9305890 abstract and official PubMed identity were read. During source preparation, targeted publisher-indexed GAP Results and Figure5 described a purified GST-GAP domain and substrate preference; the complete cloning and Methods were not recovered. The UniProt human record associates this cloning study with ARHGAP29. The abstract also supports C-terminal binding to PTPL1 PDZ4, which is a different partner from the Radil experiment below. The normal publication cache remains abstract-only.

For [PMID23209302](https://pmc.ncbi.nlm.nih.gov/articles/PMC3518219/), the abstract, targeted PDZ interaction Results, Figure1/3 legends and construct/MS Methods were read. The work includes human cellular prey and human/mouse Radil bait descriptions. The ARHGAP29-specific Figure3B pixels and TablesS1/S2 have not been read. A KIF14-centered narrative does not establish a wrong-gene annotation. The PDZ-binding row remains UNDECIDED rather than borrowing the PTPL1 experiment to close a Radil-specific evidence gap.

For [PMID25468996](https://pmc.ncbi.nlm.nih.gov/articles/PMC4972397/), the canonical abstract and partial HTML body were read; the separate recovered XML was consulted during source preparation for GFP-localization Results and relevant Methods. That richer recovered record did not replace the existing cache. The screen used GFP constructs in human MKN28 cells, but the ARHGAP29-specific Supplemental Table2 assignment remains unread. Its source-specific cytoplasm IDA remains UNDECIDED.

For [PMID26780829](https://elifesciences.org/articles/11394), the target complex-formation Results, full Figure3 supplement3 caption and construct Methods were read. YFP-ARHGAP29 coimmunoprecipitated with FLAG-Rasip1 in U2OS cells; HEG1 depletion did not abolish the association. The gifted construct has no explicit accession/species in the inspected Methods, and the human host is not proof of construct origin. Broad protein-complex association is retained as non-core context without inventing stoichiometry, an isolated binary interface or a named core complex.

The official human RHOA-GAP event includes ARHGAP29 among supported GAPs and identifies a cytosolic catalyst set. The [event page](https://reactome.org/content/detail/R-HSA-8981637) distinguishes catalysis-supporting evidence from binding-only screening and lists both cytosol and plasma membrane across the reaction. The whole-reaction compartment list is not assigned wholesale to ARHGAP29. The cached [RHO GTPase cycle](https://reactome.org/content/detail/R-HSA-9012999) summary explains GAP-mediated inactivation; other Rho-dependent outcomes are not asserted as direct ARHGAP29 functions.

The current Human Protein Atlas summary reports cytoplasmic expression and includes cytosol among additional subcellular locations. The [target summary](https://www.proteinatlas.org/ENSG00000137962-ARHGAP29) also lists other pools. This independently supports the general location, without claiming the original PMID25468996 target image or exclusive cytosolic residence was verified.

## Decisions and limitations

All fourteen original annotations and both seeded alternative products are retained. Ten rows are ACCEPT, two UNDECIDED, one KEEP_AS_NON_CORE and one MODIFY. The broad InterPro signal-transduction annotation is refined to the existing negative-small-GTPase-regulation term. The GAP contributes the actual regulatory step; this is participation evidence, not merely necessity inferred from a knockout.

Exact PAINT topology/IBD and historical ARBA conditions were not reconstructed. The three PAINT reviews retain the actual seeded PTN004470214 or PTN002689839 source and mark its tracing unresolved; independent target evidence supports the biological assertions. The target's occurrence in its own donor set is expected grounding, not circularity. No isoform-specific function is inferred without mapping the tested construct.

The configured deep-research attempt failed during source preparation and produced no provider report. Normal source records were recovered through the repository fetch workflow; there is no authored provider-branded research file. Unread target-specific evidence remains explicit and is not converted into an incorrectness claim.


## Reviewer followup: endothelial signaling and craniofacial development

The earlier two UNDECIDED decisions above record the initial review. Both are
now ACCEPT with explicit deference to the original experimental curator:
independent evidence establishes cytoplasmic localization and PDZ-domain binding.
The original localization supplement and Radil-specific interaction record remain
unread. PTPL1 binding corroborates the molecular function; it is not presented as
verification of the Radil experiment. The complex-association rationale now relies
on the reported positive coimmunoprecipitation, without treating a missing construct
accession as evidence against that result. All 14 original source assertions and
both product records remain intact; no NEW annotation is added.

The [1997 biochemical study](https://pubmed.ncbi.nlm.nih.gov/9305890/) joins two
observations: Rho-directed GAP activity and C-terminal binding to PTPL1 PDZ4.
The [2005 Rap2 study](https://pubmed.ncbi.nlm.nih.gov/15752761/) identifies human
PARG1 as a putative Rap2 effector through a separate region of the protein.
Its GTP-dependent interaction and fibroblast cytoskeletal results suggest
regulation of the GAP; they do not establish a universal activation mechanism.
Only the complete abstract of that study was read.

The [2011 tubulogenesis study](https://pubmed.ncbi.nlm.nih.gov/21396893/) tests
ARHGAP29 depletion in human umbilical vein endothelial cells in three-dimensional
matrix. Loss of lumen formation accompanies altered GTPase signaling, contractility
and matrix adhesion. The cultured human depletion experiments are distinct from
the paper's mouse Rasip1 knockout and mouse endothelial colocalization assays.
The abstract, targeted primary Results/Discussion and the complete main Experimental
Procedures were read in the recovered normal body. Supplementary protocols and
image pixels were not independently audited. This supports a role in human
endothelial morphogenesis, without asserting that every in-vivo stage of vessel
formation requires ARHGAP29.

The [2013 barrier study](https://pubmed.ncbi.nlm.nih.gov/23798437/) connects
Rap1, RASIP1/RADIL and ARHGAP29 to Rho-dependent actomyosin tension. Human
endothelial depletion reduces electrical barrier resistance; Rho/ROCK inhibition
or depletion supports the proposed signaling order. Target Results, Discussion
and the short main Methods were read. Detailed supplementary protocols remain
unread. The authors did not consistently detect a bulk Rho-GTP reduction after
Rap1 activation, so local regulation should not be restated as a demonstrated
global decrease. The later HEG1/RASIP1 study provides the separately inspected
ARHGAP29 coassociation evidence already described above.

The [2012 cleft study](https://pubmed.ncbi.nlm.nih.gov/23008150/) combines human
case/control variant analysis with mouse craniofacial expression studies.
Rare potentially damaging human variants implicate ARHGAP29 in nonsyndromic cleft
lip with or without cleft palate. Reduced expression in Irf6-deficient mice
suggests a developmental relationship; it does not demonstrate direct IRF6
regulation in human cells. The complete abstract, expression/sample/sequencing/statistics
Methods and target Results were read in the recovered normal body. Truncating
variants also occurred in unaffected relatives, and the aggregate associations
did not survive the paper's multiple-testing threshold. This early study is
supporting evidence; it does not independently establish fully penetrant inheritance.
The project's ClinGen inventory separately records the gene-disease association.

These findings expand the biological summary while retaining the existing GAP
core and negative-regulation process. Rho-specific pathway membership is kept
because the GAP performs the switch-regulation step itself. No new vascular or
craniofacial process annotation is inferred from perturbation phenotypes alone.


The four additional publication records were recovered by the normal fetcher without
source authoring. The 2011 and 2012 records contain XML-derived full text; the 2005
and 2013 records are abstract-only. Reference and quotation availability flags
follow those actual records, while external reading is documented separately.
