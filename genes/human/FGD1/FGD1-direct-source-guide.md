# FGD1: direct primary evidence

The [review](FGD1-ai-review.yaml) is the decision authority. [Source records](FGD1-direct-source-records.yaml) retain the exact imported annotation keys, zero-based indices, methods and article locators. [Product boundaries](FGD1-direct-product-boundaries.yaml) distinguish the curated full chain from engineered constructs.

## Nucleotide exchange and downstream responses

[Zheng et al., 1996, PMID:8969170](https://doi.org/10.1074/jbc.271.52.33169) tests a human FGD1 DH–PH fragment, residues 330–710. The actual original Experimental Procedures, Results and Discussion, and all four figure captions were read in the [author-uploaded article](https://www.researchgate.net/publication/14238984_The_Faciogenital_Dysplasia_Gene_Product_FGD1_Functions_as_a_Cdc42Hs-specific_Guanine-Nucleotide_Exchange_Factor). The committed cache is abstract-only. The external original text was recovered, but neither a full PDF nor the original figure pixels was obtained.

The important distinctions are:

- **Figure 1, printed page 33170:** GST-GTPase pulldown detects Flag-FGD1 from NIH 3T3 lysate with Cdc42Hs. This is a cellular-lysate association assay, not a purified binary-affinity determination.
- **Figure 2A–C, pages 33170–33171:** purified fragment stimulates GDP release and GTPγS loading on Sf9 membrane-derived Cdc42Hs. Bacterially expressed Cdc42Hs does not respond in the reported comparison. This directly supports exchange-factor activity.
- **Figure 3A–C, page 33171:** microinjection into mouse Swiss 3T3 cells produces peripheral actin microspikes and shape changes; dominant-negative Cdc42 suppresses these responses. The downstream actin and filopodium terms are retained as non-core roles.
- **Figure 4, page 33172:** two NIH 3T3 fragment-expressing clones show increased endogenous JNK1 and p70 S6 kinase activity. The kinases, rather than FGD1, perform those phosphorylation assays.

GO:0043087 concerns regulation of **GTP hydrolysis**, but its strict descendant GO:0090630 specifically describes GTPase activation through GDP/GTP exchange. The reviewed replacement therefore uses GO:0090630 for the exchange assay. The broad signal-transduction row instead uses GO:0032489 to preserve the measured CDC42-specific regulatory role, as does the core process. This latter change is a mechanistic role correction: GO:0032489 is a typed descendant of GO:0051056, but not of GO:0007165. Explicit current descendant responses show no narrower typed terms under exchange-factor activity GO:0005085 or small GTPase binding GO:0031267. See [ontology evidence](FGD1-ontology-evidence.yaml) for the actual definitions, response hashes and typed arrays. No strict path from filopodium assembly to actin cytoskeleton organization was returned in the original source checks, so neither is discarded automatically as redundant.

## Human developmental genetics

[Pasteris et al., 1994, PMID:7954831](https://doi.org/10.1016/0092-8674(94)90552-5) reports positional cloning, a translocation-disrupted human FGD1 gene and cosegregating mutations in Aarskog–Scott syndrome. Its complete abstract and bibliographic identity were verified. The original operative body remained inaccessible after bounded publisher and institutional-repository attempts. An HTTP 200 repository response was an HTML application shell, not a PDF. The organ-morphogenesis annotation therefore remains UNDECIDED; a developmental disease association alone does not resolve which morphogenetic work the protein performs.

## Product and source limits

All imported annotations retain parent P98174 identity. The official full-chain feature spans 1–961, and the seed contains no natural splice or functional-product objects. Tagged 330–710 fragments are experimental constructs, not additional products. Mouse recipient cells and insect-cell protein production are distinguished from the human FGD1 sequence.

No normal cache or source annotation was edited. No publication quotations or new annotation rows were added. The genuine provider attempt produced no report; its cause was not inspected. This authored guide is not a provider research report. These decisions follow the [project curation instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions).
