# B3GALT6 review notes

## Initial research and source inventory (2026-09-30)

Human B3GALT6 is UniProt Q96L58, HGNC:17978, NCBI Gene 126792. The normal UniProt record contains a 329-residue type II membrane protein and no alternative-products section. The imported normal seed has 29 distinct annotation objects. Raw UniProt and GOA files are preserved.

The ordinary gene-fetch attempt failed before producing a seed. The established recovery workflow supplied the exact normal seed and source records. Five previously absent auxiliary records were imported: PMID:11551958, PMID:23664117, PMID:23664118, PMID:29443383 and Reactome:R-HSA-1971475. Three existing reference caches and both existing PANTHER exports were retained. All five seeded PMID caches are abstract-only. The existing PMID:25331875 cache also contains only an abstract, repeated beneath a Full Text heading; that heading does not establish full-body availability.

One `just deep-research-falcon human B3GALT6 --fallback perplexity-lite` attempt exited unsuccessfully and produced no provider report. Its cause was not established; diagnostic output was suppressed because verbose provider diagnostics may contain credentials. The research below is manual research, not a provider-generated report.

## Direct biochemical role

[PMID:11551958](https://pubmed.ncbi.nlm.nih.gov/11551958/) identifies GalT-II as the enzyme adding the second galactose to the proteoglycan linker. The paper's complete available abstract reports the donor/acceptor specificity, a HeLa S3 knockdown phenotype and medial-Golgi localization. B3GALT6 acts on a Gal-Xyl acceptor, unlike related enzymes using terminal glucosamine or galactosamine. The normal UniProt topology places its catalytic region in the lumen. Full article figures and supplementary data were not read.

The precise core terms are [GO:0047220](https://amigo.geneontology.org/amigo/term/GO%3A0047220), the GalT-II molecular activity, and [GO:0120532](https://amigo.geneontology.org/amigo/term/GO%3A0120532), synthesis of the common GAG-protein linker. The latter is part of the chondroitin, dermatan, heparan and heparin proteoglycan pathways. B3GALT6 performs the sugar-transfer step itself. This supports participation without assigning downstream polymerization, epimerization or collagen-assembly chemistry. No Q96L58 match was found in the local GO-CAM index.

[PMID:23664117](https://pubmed.ncbi.nlm.nih.gov/23664117/) connects biallelic B3GALT6 dysfunction to skeletal and connective-tissue disease. In addition to the complete abstract, the official PubMed Figure 2 legend was read: it describes wild-type Golgi localization, altered localization of a start-site mutant and reduced GalT-II activity for tested variants. The normal cache remains abstract-only; figure pixels and complete Methods were not inspected.

[PMID:23664118](https://pubmed.ncbi.nlm.nih.gov/23664118/) reports impaired GAG priming and decorin glycanation in patient fibroblasts, together with reduced heparan sulfate. Its complete abstract supports the common-linker contribution to multiple GAG classes. Wound-repair and collagen-organization phenotypes are downstream consequences, not additional direct molecular activities.

[PMID:29443383](https://pubmed.ncbi.nlm.nih.gov/29443383/) distinguishes ER-retained mutant proteins from variants that traffic normally. The complete abstract was read. Individual localization images and enzyme-assay tables were not available in the cache, so their curated annotations retain explicit source limits and independent biochemical support. Mutant ER retention does not imply that wild-type B3GALT6 normally functions in ER quality control.

[PMID:19946888](https://pubmed.ncbi.nlm.nih.gov/19946888/) profiles the membrane proteome of YTS NK-like cells. The full cached abstract was read, but B3GALT6-specific peptide rows were not independently verified. The broad membrane observation is consistent with established topology and is retained with curator deference.

## Regulation, compensation and citation limits

[PMID:25331875](https://pubmed.ncbi.nlm.nih.gov/25331875/) separates FAM20B-mediated xylose phosphorylation from GalT-II-mediated galactose transfer. The normal abstract and selected indexed original Results/Methods were read. The excerpts describe purified MBP-GalT-II and defined acceptors, but did not resolve the construct's exact species/accession. Do not turn acceptor phosphorylation into a B3GALT6 kinase annotation.

[PMID:40857410](https://insight.jci.org/articles/view/179474) provides more recent evidence for residual GAG synthesis and B3GAT3-dependent bypass in tested contexts. Selected original Results, Methods and legends were read, including human enzyme constructs and human-cell experiments separately from mouse tissue models. This qualifies claims of universal abolition after B3GALT6 loss. Its single ordinary cache-fetch attempt failed with a DNS error; reference integration awaits normal-cache recovery. No figure pixels or supplements were inspected.

The normal UniProt record explicitly cautions that the cDNAs in PMID:9892646 were switched, while its cofactor field and the normal Reactome reaction cite that historical work for manganese. The original correction was not independently recovered. Consequently, the review does not infer a metal-binding activity from that citation or claim to have resolved the historical experiment. This is a bounded citation question, not a conclusion drawn from the article title.

The prospective review preserves all 29 source assertions. Three broad electronic annotations are proposed for refinement to existing specific terms; these are changes to source assertions, not NEW pathway assertions. The independent consultation will assess those refinements and the source-specific limitations before canonical review integration.


## Additional primary evidence and final annotation consultation (2026-09-30 UTC)

The independent annotation reviewer assessed all 29 source annotations and the core-function synthesis, with no required biological changes. The final proposal retains 25 ACCEPT, three MODIFY and one KEEP_AS_NON_CORE decisions, with no NEW annotations or product assertions. The two short core-function quotations were expanded within their original cached abstracts for clearer support.

[PMID:40857410](https://insight.jci.org/articles/view/179474), *B3GALT6 mutations lead to compromised connective tissue biomechanics in Ehlers-Danlos syndrome*, supplies additional primary evidence. Selected original Results and Methods were read, including human placenta-derived truncated enzyme constructs expressed in E. coli, human HeLa and patient-fibroblast experiments, and the distinct mouse ATDC5 matrix model. The normal recovered record preserves its full-text metadata and content; figures and supplements were not independently inspected. Purified human B3GALT6 catalyzes the GalT-II reaction. Separately, B3GAT3/GlcAT-I can bypass the missing second galactose and contribute to residual GAG synthesis. This glucuronosyltransferase reaction belongs to B3GAT3. The Y182C cellular phenotype leaves residual variant activity and/or compensation possible; not all residual synthesis is assigned exclusively to bypass. These findings support the description's emphasis on efficient linker synthesis without implying complete elimination of every GAG after B3GALT6 loss. Mouse collagen-XII and pseudotissue effects do not establish a new human collagen-modifying enzyme activity. AlphaFold/Rosetta/molecular-dynamics analyses are models, not an experimentally solved atomic structure.
