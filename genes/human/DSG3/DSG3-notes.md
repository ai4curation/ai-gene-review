# DSG3 (P32926) — curation notes

Deep-research providers are unavailable in this environment (`just deep-research-falcon`
fails with "agentapi not found in PATH"; the perplexity provider is not configured).
Research below is from the cached publications, the UniProt record and PubMed.

## Architecture and localization

Desmoglein-3 is a desmosomal cadherin: signal peptide and propeptide, four extracellular
cadherin (EC) domains plus an EC anchor, a single transmembrane helix, and a cytoplasmic
tail with the intracellular anchor and cadherin-like sequences that engage plakoglobin and
plakophilins. The adhesive ectodomain faces the extracellular space, so the protein is
accessible from outside the cell — the basis of pemphigus vulgaris autoantibody binding.

UniProt subcellular location: cell membrane (single-pass type I), cell junction/desmosome,
cell junction/tight junction, and cytoplasm.
[file:human/DSG3/DSG3-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:19717567, ECO:0000269|PubMed:30949721, ECO:0000269|PubMed:31835537}; Single-pass type I membrane protein"]

There are two documented pools: the desmosomal pool, and a detergent-soluble,
non-junctional pool at the cell surface that carries much of the signalling activity.
[PMID:22294297 "it is the detergent-soluble, non-desmosomal Dsg3 that regulates the activity of Src and its association with E-cadherin in adherens junction formation"]
[PMID:18343367 "p120ctn does not localize to desmosomes, but colocalizes with Dsg3 at the cell surface"]

Conclusion for GO: plasma membrane and desmosome are the core locations, with the
adhesive domain extracellular. Cytoplasm reflects the cytoplasmic tail / soluble pool;
the Reactome cytosol assignment comes from the caspase-released cytoplasmic fragment
(R-HSA-201631, "Caspase-mediated cleavage of Desmoglein 3"). Cornified envelope is a
pathway-level Reactome/ARBA assignment, not a DSG3 localization experiment, and DSG3 is
expressed in the basal and spinous layers with only weak granular-layer expression.

## Functions

- Calcium-dependent desmosomal adhesion; knockout mice lose telogen hairs through
  acantholysis around the telogen club.
  [PMID:9701552 "showed loss of cell adhesion (acantholysis) between the cells surrounding the telogen club and the basal layer of the outer root sheath epithelium"]
- Homodimer; trans-interaction measured by AFM/laser tweezers.
  [file:human/DSG3/DSG3-uniprot.txt "SUBUNIT: Homodimer (PubMed:19717567)."]
- Junction assembly under mechanical strain, with a DSG3/PKP1/YAP1/YWHAG complex that
  retains phospho-YAP at the membrane.
  [PMID:31835537 "Dsg3 formed a complex with phospho-YAP and sequestered it to the plasma membrane"]
- Upstream regulation of Rac1/Cdc42 and cortical actin.
  [PMID:22796473 "our results reveal an important novel function for Dsg3 in promoting actin dynamics through regulating Rac1 and"]
- Suppression of p38MAPK and hence of keratinocyte migration and wound closure.
  [PMID:26763450 "Human keratinocytes after silencing of Dsg3 as well as primary cells isolated from Dsg3 knockout animals exhibited accelerated migration"]

## Protein-binding rows

Per the protein-binding policy, bare GO:0005515 rows are either MODIFYed to an
informative molecular function or REMOVEd as uninformative. Interactors here are PKP2
(PMID:11790773), CTNND1/p120 (PMID:18343367), DSC3 (PMID:19717567), CDH1 (PMID:22294297),
RAC1 (PMID:22796473) and the PKP1/YAP1/YWHAG complex (PMID:31835537).
