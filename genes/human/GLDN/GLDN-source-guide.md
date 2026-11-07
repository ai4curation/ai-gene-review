# GLDN source guide

Official source access checked on 2026-11-06.

- [Human UniProt record](https://rest.uniprot.org/uniprotkb/Q6ZMI3.json) and [QuickGO product annotations](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:Q6ZMI3&limit=100).
- [Human Protein Atlas subcellular record](https://www.proteinatlas.org/ENSG00000186417-GLDN/subcellular).
- [Official Matrisome human list page](https://sites.google.com/uic.edu/matrisome/matrisome-annotations/homo-sapiens), linking the [human masterlist](https://docs.google.com/spreadsheets/d/12OslOlOhQQtHMOUKAFFgAQXL2zYX-g9q/edit). The downloaded XLSX has SHA256 `20ecc253f84628e17d45cba9242b5cca9aa5520f326d43212a354e4e311cf838`; target row locator: sheet1, row63.
- [PMID:16039564 author-hosted original](https://www.weizmann.ac.il/mcb/peles/sites/mcb.peles/files/2023-01/eshed_neuron2005.pdf).
- [PMID:20188654 author-hosted original](https://www.weizmann.ac.il/mcb/peles/sites/mcb.peles/files/2023-01/feinberg_neuron2010.pdf).
- [PMID:17485493 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064815/).
- [PMID:22009740 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3234976/).
- [PMID:24719088 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3983794/).
- [PMID:36399478 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC9825471/).

Failed retrievals were retained separately from successful originals. Europe PMC XML failures did not establish that the articles lacked accessible full text. Reference reviews state the actual reading scope. No generated provider report was created.

Reference availability flags describe the local publication caches. Reference-review notes separately identify original material read outside those caches.

## Original-source evidence

PMID:16039564, Figure 4D–H, p.220 (adult rat sciatic nerve): “no gold particles were detected
in the axon”. Author-hosted PDF read; normal cache is abstract-only.

PMID:20188654, Figure 4B and Clustering Experiments: Gldn-Fc was antibody-preclustered before mouse DRG exposure; NF186 enabled channel recruitment. This assay tests an engineered extracellular fusion, without identifying a natural human isoform.

## Annotation scope

[GO:0045162](https://www.ebi.ac.uk/QuickGO/term/GO:0045162) is a channel-localization process under ion-channel clustering, not a descendant or ancestor of either existing signal transduction or heterotypic cell-cell adhesion. The proposed human ISS/involved_in row is an explicit reviewer inference. The actual mouse IMP and rat ISO comparator annotations say acts_upstream_of_or_within; their qualifiers are retained in the evidence record and are not silently relabeled.

The comparison queried extracellular organizers AGRN and TNR in human, mouse and rat where reviewed records were available. The exact-term result includes human AGRN TAS and mouse/rat Gldn; none of the tested TNR records has the term. An additional BCAN query was also empty. These bounded annotation observations provide context, not proof of either function or curator error. The local GO-CAM index has no GLDN/Q6ZMI3/Q8BMF8/Q80WL1 match.

[GO:0033268](https://www.ebi.ac.uk/QuickGO/term/GO:0033268) explicitly denotes an axon part and descends from axon. Replacing axon with this narrower term would preserve the disputed compartment inference. Nodal association is retained in the biological description; a curator question records the unresolved representation of perinodal extracellular material. DAG1/SPOCK1 comparator annotations do not by themselves settle that compartment distinction.

The signaling IBD is PANTHER:PTN000573635 at AN0, with GLDN at AN489/PTN002509188 on its descendant path. Its three source identifiers and actual placement remain literal. No GLDN-specific evolutionary loss has been established, and family-level generated prose does not establish one. Retaining this broad IBA does not transfer MYOC's particular receptor mechanism.

The [review evidence record](GLDN-review-evidence.json) preserves the literal comparator rows, ontology responses, PAINT assertion and source locators.
