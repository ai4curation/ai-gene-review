# EGR2 source and evidence guide

This guide separates imported annotation provenance, actual experimental scope, and the content available in each publication cache. Cached abstracts remain abstracts even where an original was independently inspected. The source records and inherited quotations are preserved except for the three explicitly documented excerpt-occurrence retirements; no replacement quotation was introduced.

## Experimental evidence and access

| Source | Public locator and actual scope | Limits relevant to the review |
| --- | --- | --- |
| PMID:12687019 | [Original](https://doi.org/10.1038/sj.onc.1206222), selected Methods/Results and Figure 5: human SW480 adenoviral EGR2, promoter reporters, wild-type/mutant motifs, nuclear-extract EMSA, competition and anti-Egr2 supershift. | Direct human activation/binding evidence, not purified EGR2; exact natural product of the historical 1.4-kb insert unresolved. Some BNIP3L coordinate descriptions are inconsistent and are not reproduced. |
| PMID:14532282 | [Original](https://pmc.ncbi.nlm.nih.gov/articles/PMC4291123/), Experimental Procedures and Results/Figures 1–5: explicit murine Krox20 ORF and N-terminal constructs; HCF-1-dependent reporter activation and cellular recruitment/motif controls. | The authors did not detect stable association in their attempted purified binding assays. Human host cells and human reference ROGIDs do not establish a human Krox20 insert. HCFC1 is a coactivator, not a sequence-specific DNA-binding TF. |
| PMID:17717711 | [Publisher](https://doi.org/10.1007/s10048-007-0094-0), authentic complete abstract and bibliographic preview. | Operative functional-assay body was not recovered; an apparent PDF download was HTML challenge content. Specific variant assay results are not invented. Clearly correct DNA-binding/activation annotations retain independent human support from PMID:12687019. |
| PMID:19651900 | [Original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2747983/), Materials and Methods and Figure 2C–F/associated Results: human Jurkat-library screen, co-IP and GST-WWP2-WW-region/His-EGR2 pull-down, GST/PPXY controls, HECT-dependent ubiquitination. | WWP2 is the E3 ubiquitin ligase and EGR2 its regulated substrate. Every recombinant EGR2 insert was not mapped to a natural human product. Main figure captions/text, not blot pixels, were inspected. |
| PMID:21836637 | [Main original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3185338/), complete operative text and captions; [supplement](https://static-content.springer.com/esm/art%3A10.1038%2Fembor.2011.152/MediaObjects/44319_2011_BFEMBR2011152_MOESM1_ESM.pdf), both pages as text and page 1 visually, including reagents and reaction conditions. | Purified mouse Krox20/E1/UBC9/NAB2 with human SUMO1 and ATP. The substoichiometric experiment supports E3 catalytic participation, not a measured kinetic constant or purified human EGR2 assay. Main Figure 2 pixels were not inspected. Supplement SHA-256: `d33a3e80239ec42680c7f7f80d3b5a1c058f41ca5d472edb98d428c1da432b90`. |
| PMID:28473536 | [Original](https://doi.org/10.1126/science.aaj2239), independently inspected human TF cohort Methods. | The exact EGR2 supplement row/construct and methylation-preference class were not recovered. The positive IDA function is retained with curator deference and independent human DNA-binding evidence; no target-specific SELEX number is claimed. |
| PMID:9537424 | [PubMed](https://pubmed.ncbi.nlm.nih.gov/9537424/), complete authentic abstract. | Human hereditary-neuropathy variants are distinguished from mouse hindbrain/Schwann-cell background. No operative original-body read is claimed. |
| PMID:17938205 | [Original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2169423/), selected Methods, promoter/ChIP context, and complete targeted Results/Figure 5 caption concerning SFN and EGR2 localization. | Mouse EGR2/CITED1 constructs and mouse ErbB2 promoter. SFN redistributes/sequesters EGR2 itself: positive cytoplasmic localization is retained, whereas the assigned export-process role conflates cargo with transport participation. No transport velocity or export-complex assay is inferred. |
| PMID:18396140 | [Original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2430156/), selected Methods/Results, Figure 2D/E interaction assays and differentiation experiments. | KLF4 is the independently established DNA-binding partner class. Co-IP and GST pull-down are positive; every Krox20 insert was not sequence-mapped. The separate two-hybrid supplement was not read, and cooperation/additive reporter effects are not described as a new synergistic mechanism. |

The remaining donor references below were read as complete authentic abstracts and metadata, not full original bodies: PMID:10068633 (Schwann-cell differentiation), PMID:11509834 (jaw-opener musculature and innervation context), PMID:16054051 (adipogenesis), PMID:22147266 (C2C12 transcription-regulator screen; Egr2 target table not independently inspected), PMID:25344368 (aortic-valve phenotype and collagen regulation), PMID:7903221 (rhombomere development), PMID:7935840 (peripheral myelination), PMID:8093858 (HoxB2 regulatory evidence), and PMID:9806922 (Hoxa1/Krox20 developmental interaction). Their literal current mouse donor assertions remain in the database replay. A title foregrounding another gene or a missing table is not treated as evidence of curator misattribution.

## Database provenance and interpretation

The [portable evidence results](EGR2-bioinformatics/RESULTS.md) and [input manifest](EGR2-bioinformatics/input-manifest.json) contain official URLs, exact hashes, full source fields and reproducible joins.

- PAINT: [PTHR23235 tree](https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR23235), target MSA, and the complete frozen [IBD source](https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf). Four literal ancestral assertions reach the exact 476-aa human target. Self-grounding and donor count are not failure criteria.
- Ortholog source: [mouse Egr2/P08152](https://www.uniprot.org/uniprotkb/P08152/entry) and the complete [QuickGO query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:P08152&limit=200&page=1), containing 92 records. The source-role objection for export preserves the real donor IDA and observed relocation.
- Interaction source: [IntAct target query](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/id:P11161?format=tab27), all 11 records. Independent classes are in [HCFC1/P51610](https://www.uniprot.org/uniprotkb/P51610/entry), [WWP2/O00308](https://www.uniprot.org/uniprotkb/O00308/entry) and [mouse KLF4/Q60793](https://www.uniprot.org/uniprotkb/Q60793/entry). Reference checksums and assayed features remain separate from construct identity.
- Reactome: all 12 literal imported event IDs resolve through saved component/member paths to [human EGR2 entity R-HSA-977385](https://reactome.org/content/detail/R-HSA-977385). Its own compartment is nucleoplasm. Expression outputs are not assigned an autoregulatory function, alternative members are not simultaneous binding assertions, and models are not counted as independent microscopy experiments.
- Ontology: current [coactivator binding GO:0001223](https://www.ebi.ac.uk/QuickGO/term/GO:0001223), [DNA-binding transcription-factor binding GO:0061629](https://www.ebi.ac.uk/QuickGO/term/GO:0061629) and [protein export from nucleus GO:0006611](https://www.ebi.ac.uk/QuickGO/term/GO:0006611) definitions and typed ancestors are preserved in the replay. The coactivator and DNA-binding partner classes are distinct.

The [ClinGen project policy](../../../projects/CLINGEN_MENDELIAN.md) retains supported generic protein-binding assertions as non-core when a specific evidence-backed replacement is unavailable. Here the HCFC1 class is established, so a specific coactivator-binding refinement is supported without requiring a purified native interface.

## Selected publication-cache identities

The links below identify exact cache files. The full-text column describes the file metadata, not the extent of every original-body read. The experimental-access table above governs the actual claim scope. None of these cache bytes or flags was manually rewritten.

| Reference/cache | Cache full text | SHA-256 |
| --- | --- | --- |
| [PMID:7903221](../../../publications/PMID_7903221.md) | false | `24873525bc96a85a7d46e1249c6c52d3944cecd984589424f883e313d9100736` |
| [PMID:7935840](../../../publications/PMID_7935840.md) | false | `cea155ab75a7ec4cd51bf07d2a674c8b029da8ca9fb6840a375a0eee865a054d` |
| [PMID:8093858](../../../publications/PMID_8093858.md) | false | `4f704466fc849dda76cbb03fe5339bc14bd12a91c388f836d468040ff8fdf869` |
| [PMID:9537424](../../../publications/PMID_9537424.md) | false | `bb11c5d9da2dd21d506b8085f2c5b4b337853ac9b68eec62b90c1378f1674a53` |
| [PMID:9806922](../../../publications/PMID_9806922.md) | false | `1d09405e57e137e88535359a1550d1ee3936ee97421b9c3b29784baf685821e6` |
| [PMID:10068633](../../../publications/PMID_10068633.md) | false | `af9a1b96b70140e0fe60c427daced6d327bf3e340e3d91564106838b58950c9a` |
| [PMID:11509834](../../../publications/PMID_11509834.md) | false | `d1f66a602efe05f9c17a7344fdf55254f6e40a858b0ca03b138643eca04a7f29` |
| [PMID:12687019](../../../publications/PMID_12687019.md) | false | `f1fdac2becbd32c4844a9995ee31da460affb2b5d8130b0ddd95fcb8185cd460` |
| [PMID:14532282](../../../publications/PMID_14532282.md) | false | `31688292f546fae6ebafa174d77e8024490d55cddcf699e4428a35420f981bc4` |
| [PMID:16054051](../../../publications/PMID_16054051.md) | false | `d7fe2940035b9fc4cf4f7207d2b54636a4b5bf9c384faed452d4bcb428153503` |
| [PMID:17717711](../../../publications/PMID_17717711.md) | false | `3ae35710f73e4919c51140bd8a29467b7338fcc2be6794e70ab50b21741cc101` |
| [PMID:17938205](../../../publications/PMID_17938205.md) | false | `70be7bea28dda32be61dc41e26e7fb31791eec5c4fbc67796b23fdba908c9680` |
| [PMID:18396140](../../../publications/PMID_18396140.md) | true | `d5c21823ff8aa345d738879c8b96a79f684c0da194182cd099d4c5cbf496b48e` |
| [PMID:19651900](../../../publications/PMID_19651900.md) | false | `ff3dcf2052d246b803bfa125c7813b26c7248e5b3441801257ee1a65ae7ce464` |
| [PMID:21836637](../../../publications/PMID_21836637.md) | false | `4f7df0117fd7d5b8288b289b396f463d78228e487b76b3849c9d1d72d47b989f` |
| [PMID:22147266](../../../publications/PMID_22147266.md) | false | `06efe11ddb90212978d139f48695094e939a0bc6f8169296f0d5f57e72d2f7d4` |
| [PMID:25344368](../../../publications/PMID_25344368.md) | false | `99810cbd33e14074187302b17517535f83ecab180e0b0db2a8f6b55d2f8880d3` |
| [PMID:28473536](../../../publications/PMID_28473536.md) | true | `1a180e2daaebaa6a90ffa80c561ad35834aafca6e0402d38fcee6ef8d6efc426` |

The normal acquisition archives, historical source contexts and provider outcomes remain preserved. Ten additional citation caches were fetched after a complete path-ownership check; the existing PMID:22147266 cache was reused exactly. The five historical source keys absent from the normally regenerated GOA snapshot remain in the review with `retired: true`. This records source lifecycle only: their scientific decisions, source identifiers and inherited evidence are unchanged. The two newly fetched source contexts remain active. The [previous GOA snapshot](EGR2-bioinformatics/source-snapshots/EGR2-goa-before.tsv) and [reconciliation record](EGR2-bioinformatics/source-snapshots/reconciliation.json) preserve the comparison; the current GOA file is the byte-exact normal fetch output, with no hand-edited rows.

## Integrated functions and natural products

The transcriptional core includes positive regulation of myelination (GO:0031643) and Schwann-cell differentiation (GO:0014040), supported by the mouse loss-of-function abstracts PMID:7935840 and PMID:10068633 and human myelinopathy evidence. The saved official structural ontology relations do not make these processes redundant with positive regulation of RNA polymerase II transcription.

The SUMO core names [human NAB2, UniProtKB:Q15742](https://www.uniprot.org/uniprotkb/Q15742/entry) as the conserved substrate. Its official record identifies Homo sapiens (taxon 9606); the defined biochemical experiment in PMID:21836637 still used mouse Egr2 and mouse Nab2 with human SUMO1. The human substrate identifier expresses the ortholog inference and does not relabel that experiment as a human purified-pair assay. Long and Short EGR2 retain their distinct 476- and 426-residue sequence boundaries; functional equivalence is not established.
