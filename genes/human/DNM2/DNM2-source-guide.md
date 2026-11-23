---
title: DNM2 source and assay guide
gene: DNM2
annotation_scope:
  imported_annotations: 171
  new_annotations: 0
---

# DNM2 source and assay guide

This guide locates the evidence supporting the review. Reference assessments distinguish selected original passages from abstract-only access. Machine cache variants retain their original text and flags; the effective shared-cache selection is described below. Primary citations, rather than this guide, support the biological assertions.

## Motor and membrane-remodeling evidence

| Source and locator | Evidence and boundary |
|---|---|
| [PMID:24970086](https://pmc.ncbi.nlm.nih.gov/articles/PMC4601533/), Figure 3C/E/G–I and adjacent Results | Purified human DNM2/NME2 association and GTPase experiments support the human motor mechanism. Figure 3G fission uses rat-brain dynamin; neighboring DNM1 experiments are separate. The initial normal cache was abstract-only; the PMC original was independently read. |
| [PMID:36445308](https://pmc.ncbi.nlm.nih.gov/articles/PMC9712776/), Results Figures 1–2; Methods, recombinant Dyn2 purification and SUPER-template fission | Human Dyn2 isoform 1 was expressed in Sf9. Purified fission and membrane polymers support motor activity. C2C12/L6 muscle-cell transport and phosphorylation experiments are rodent contexts. |
| [PMID:34744632](https://pmc.ncbi.nlm.nih.gov/articles/PMC8563704/), Protein preparation, lipid binding, polymerization and GTPase Methods/Results | Full-length and PH constructs are rat DNM2 P39052 ba/IIBA. Mutation-specific lipid-binding and polymerization effects do not imply universal loss of every motor property. |
| [PMID:19605363](https://pmc.ncbi.nlm.nih.gov/articles/PMC2781994/), Actin-bundle reconstitution and U2-OS depletion/rescue Methods/Results | Purified rat DNM2, rabbit actin and bovine Arp2/3 establish direct biochemical remodeling. Human-cell depletion and rat rescue are separate; possible endocytic contributions to the cellular phenotype remain unresolved. |
| [PMID:32315611](https://pubmed.ncbi.nlm.nih.gov/32315611/), Recycling-endosome, LC3 and DNM2 construct/protein Methods/Results | Human endogenous experiments support the cellular role. HA-DNM2 Addgene34684 is rat; gifted GFP species is unresolved. Current OriGene TP323585 matches human P50570-1 before the tag, without establishing the historical lot. The accepted manuscript supplies the operative original. |
| [PMID:24135484](https://pmc.ncbi.nlm.nih.gov/articles/PMC3882057/), Constructs and BIN1 tubulation Results | Human IOH53617 is expressed in COS7 and zebrafish. Mutant interference with BIN1-driven tubulation is not a purified autonomous human DNM2 tubulation experiment. |
| [PMID:29437695](https://pmc.ncbi.nlm.nih.gov/articles/PMC5891424/), SNX18 WT/W38K, ATG9A and recycling-endosome Results | Human-cell association and trafficking support the recruitment context. The gifted dynamin template species is unresolved. |
| [PMID:35620056](https://pmc.ncbi.nlm.nih.gov/articles/PMC9127447/), Protein purification and actin/lipid reconstitution Methods/Results | Rat recombinant/transfected DNM2 and human podocytes are separate. K562E disrupts lipid interaction while retaining ring/actin properties in the reported assays. |

The core uses GO:0061791 GTPase motor activity. PH-domain phospholipid binding and partner recruitment are mechanisms within this motor unit. Existing process coverage includes scission, receptor-mediated endocytosis, macroautophagy and actin-bundle organization. No additional process annotation is manufactured from necessity alone.


### Current ontology and comparator check (2026-10-18 UTC)

[The is_a-only QuickGO ancestry query](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061791/ancestors?relations=is_a) places GTPase motor activity below GTPase activity. The definition requires mechanical activity driven by GTP hydrolysis. DNM2 human hydrolysis/fission and membrane-polymer evidence supports that refinement; rat and human assays retain their source boundaries. The narrower GO:1990606 definition additionally specifies twisting, which is not assumed from every fission assay.

The following complete current human queries used the verified UniProt accession and the indicated term plus is_a/part_of descendants. Counts are records, not independent experiments:

| Human gene | Accession | GTPase activity branch | Motor activity branch |
|---|---|---:|---:|
| DNM1 | Q05193 | 7 | 0 |
| DNM2 | P50570 | 8 | 0 |
| DNM3 | Q9UQ16 | 3 | 0 |
| DNM1L | O00429 | 6 | 0 |
| OPA1 | O60313 | 12 | 0 |
| MFN1 | Q8IWA4 | 4 | 0 |
| MFN2 | O95140 | 3 | 0 |

[Reproduce the DNM2 motor query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:P50570&goId=GO:0061791&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=200); substitute each accession and GO:0003924 for the paired comparison. [The complete all-taxon motor query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO:0061791&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=200) returns four PomBase records on this date: msp1/P87320 (TAS) and fzo1/Q9USY7 (ISM) to GO:0061791, plus dnm1/Q09748 and vps1/Q9URZ5 (both TAS) to GO:1990606. Official identities confirm dynamin-family comparators. These records demonstrate real use of the motor branch in this protein family while preserving the observed absence in the human records. The query is not itself biochemical evidence for DNM2, and human non-use is not claimed to be a curator mistake.

The two autophagy sources resolve different stages. The [2020 accepted manuscript](https://www.repository.cam.ac.uk/items/9d75f0e3-c39a-4b5c-9a59-0dd1f3325530), Results section on DNM2-mutant accumulation and Figure 5D–E, reports unchanged numbers of open phagophores but accumulation of completed autophagosomes and fewer autolysosomes. Live imaging shows failure to detach LC3 vesicles from RAB11A-positive tubules. The adjacent ATG9A/ATG16L1 and SNX18 controls explicitly distinguish this release step from early ATG9A trafficking. Row 121 is therefore refined to [GO:0016236 macroautophagy](https://www.ebi.ac.uk/QuickGO/term/GO:0016236), without assigning double-membrane formation or closure. The [2018 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC5891424/), Figures 3/4 and WT/W38K experiments, independently supports DNM2-dependent ATG9A carrier generation and ATG16L1 delivery for [GO:0000045 autophagosome assembly](https://www.ebi.ac.uk/QuickGO/term/GO:0000045) in row 122. The core uses macroautophagy once and describes both stages. Neither route is claimed to supply every autophagosome.

The current [GO:0097352 maturation definition](https://www.ebi.ac.uk/QuickGO/term/GO:0097352) specifies removal of PI3P and Atg8/LC3 after closure, which was not established here. [GO:0061906 localization](https://www.ebi.ac.uk/QuickGO/term/GO:0061906) concerns transport to or maintenance at a cellular location; detachment alone does not demonstrate that process. [GO:1905037 organization](https://www.ebi.ac.uk/QuickGO/term/GO:1905037) concerns constituent assembly, arrangement or disassembly, which would still infer an organizational step from the 2020 release endpoint. These terms are not substituted merely because their names sound like later stages.

## Interactions and repeated partners

[The executable interaction analysis](DNM2-bioinformatics/interactions/README.md) provides public dataset URLs, exact snapshot digests, literal MITAB fields, AP-MS edge identifiers and OpenCell accession groups. It separates all incident records from the subset selected by the imported source annotations. A missing MITAB match is an unresolved database join, not a negative experiment.

| Partner/context | Review interpretation |
|---|---|
| GRB2, ITSN1, SNX9 and other mapped SH3 partners | Domain-resolved SH3/PRD experiments establish class specificity. Later binary screens or AP-MS observations keep their own assay scope; they are not relabeled as interface mapping. |
| DNM1 | Dynamin-family binding is supported across independent sources; neither the AP-MS nor OpenCell group identifies a purified heteromer stoichiometry. |
| SNX33 | Positive association remains generic non-core binding in all three source contexts. |
| GABARAP, GABARAPL1, GABARAPL2 and LC3B | Official ubiquitin-like modifier identity plus positive association supports GO:0032182. This does not assign conjugating activity to DNM2. |
| BAG3 and SDCBP | Documented scaffold function informs the partner class. DNM2 is not assigned their client-folding or adaptor roles. |
| QARS1 and FLAD1-2 | Positive sequence-resolved HuRI pairs bind proteins with independently established catalytic activity. GO:0019899 means binding to an enzyme; it does not require regulation of its catalysis. DNM2 is not assigned tRNA charging or FAD metabolism. |
| UBASH3A-2, SEC23A, CTNND2, Nef and PSTPIP1 | Positive interactions are retained with source-specific limits; no unsupported enzymatic, receptor or adaptor class is substituted. CTNND2 is not beta-catenin. |

PMID:16696976 is especially qualified: MINT identifies PRD/SH3 fragments, but some original protein taxids were unspecified and human homolog accessions were supplied by curation. This does not authenticate a human recombinant template. In PMID:22022388, a sequenced human SH-SY5Y-derived clone supports NPRAP/CTNND2 association; its historical isoform label is not automatically a modern UniProt product ID.

## Localization, processes and propagation

[HPA DNM2 localization](https://www.proteinatlas.org/ENSG00000079805-DNM2/subcellular) supports cytosol and Golgi. Selected membrane pools are supported by the original trafficking studies. Cytoplasm replacements retain cytosol and recycling-endosome membrane. Clathrin-coated pits are plasma-membrane invaginations outside the defined cytoplasm and remain in their own positive rows/core. The cytoskeleton mapping is refined to microtubule; focal adhesions are junctions and retain their separate positive detection. This is a source-specific compartment distinction, not exhaustive distribution in every cited cell. Urinary-vesicle proteomics and focal-adhesion proteomics retain their contextual detections despite incomplete recovery of the target supplementary rows.

The [PANTHER family PTHR11566](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR11566) path to DNM2 contains all eight literal PAINT ancestral assertions. PTN000170013 grounds the GTPase/cytoplasm/microtubule placements; PTN008520579 the plasma-membrane placement; PTN000902093 the synaptic-vesicle-budding/synapse placements; PTN002611550 receptor internalization. These are ancestral placements, not pairwise transfers or donor-count scores.

[PMID:11076973](https://pubmed.ncbi.nlm.nih.gov/11076973/) provides Drosophila affinity/cosedimentation context. [PMID:21210813](https://pubmed.ncbi.nlm.nih.gov/21210813/) directly examines rat neuronal growth cones, domain perturbations and adhesions, with separate HeLa antibody controls. Neither is a purified human neuronal assay. [PMID:21195118](https://pubmed.ncbi.nlm.nih.gov/21195118/) supports mitotic phosphorylation and cytokinesis, which does not by itself settle the historical G2/M transition assertion.

The Reactome sources can be inspected at their exact event pages, including [dynamin-mediated scission R-HSA-8868661](https://reactome.org/content/detail/R-HSA-8868661), [Golgi scission R-HSA-421835](https://reactome.org/content/detail/R-HSA-421835), [Golgi-to-lysosome scission R-HSA-432707](https://reactome.org/content/detail/R-HSA-432707), [BAR-domain recruitment R-HSA-8868236](https://reactome.org/content/detail/R-HSA-8868236), and [NOSTRIN trafficking R-HSA-203625](https://reactome.org/content/detail/R-HSA-203625). The review preserves each cited event and nested target assignment. A rate-limited API endpoint is not treated as a biological negative. ARBA condition reconstruction remains incomplete and is identified as such in the propagation review.

## Products and source access

[UniProt P50570](https://www.uniprot.org/uniprotkb/P50570/entry) defines five official products, with lengths 870, 866, 866, 870 and 869 residues. The alternative sequence features are preserved exactly. Historical aa/ab/ba/bb and named disease constructs require sequence reconciliation before product-specific conclusions; similar lengths or a human cell host are insufficient. No product is declared universally inactive.

The table below reports effective publication-cache availability, not a claim that every paragraph of a full cache was read. Additional independently recovered original scope is stated above and in each reference assessment.

| PMID | Normal cache | Primary access addition or important limit |
|---|---|---|
| [PMID:10101292](https://pubmed.ncbi.nlm.nih.gov/10101292/) | Abstract only | No independent full-original claim. |
| [PMID:10893263](https://pmc.ncbi.nlm.nih.gov/articles/PMC2185575/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:11583995](https://pmc.ncbi.nlm.nih.gov/articles/PMC2715172/) | Abstract only | Indexed primary Results/Discussion; direct page recovery challenged. |
| [PMID:14985334](https://pubmed.ncbi.nlm.nih.gov/14985334/) | Abstract only | No independent full-original claim. |
| [PMID:15048127](https://pubmed.ncbi.nlm.nih.gov/15048127/) | Abstract only | No independent full-original claim. |
| [PMID:15703209](https://pmc.ncbi.nlm.nih.gov/articles/PMC1073683/) | Full text available | Shared full-text cache selected; separately recovered PMC Methods/Results read. |
| [PMID:15731758](https://pubmed.ncbi.nlm.nih.gov/15731758/) | Abstract only | No independent full-original claim. |
| [PMID:16227997](https://pubmed.ncbi.nlm.nih.gov/16227997/) | Abstract only | No independent full-original claim. |
| [PMID:16325581](https://pubmed.ncbi.nlm.nih.gov/16325581/) | Abstract only | No independent full-original claim. |
| [PMID:16551695](https://pubmed.ncbi.nlm.nih.gov/16551695/) | Abstract only | No independent full-original claim. |
| [PMID:16636290](https://pmc.ncbi.nlm.nih.gov/articles/PMC1459014/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:16696976](https://pubmed.ncbi.nlm.nih.gov/16696976/) | Abstract only | No independent full-original claim. |
| [PMID:17257598](https://pmc.ncbi.nlm.nih.gov/articles/PMC1861834/) | Abstract only | Operative original passages read in the independently fetched full-text variant; effective shared cache is abstract-only. |
| [PMID:17412836](https://pmc.ncbi.nlm.nih.gov/articles/PMC1871867/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:17676042](https://pubmed.ncbi.nlm.nih.gov/17676042/) | Abstract only | No independent full-original claim. |
| [PMID:18353773](https://pubmed.ncbi.nlm.nih.gov/18353773/) | Abstract only | No independent full-original claim. |
| [PMID:18388313](https://pubmed.ncbi.nlm.nih.gov/18388313/) | Abstract only | Indexed publisher Methods/Results; direct page failed. |
| [PMID:18480402](https://pmc.ncbi.nlm.nih.gov/articles/PMC2488309/) | Abstract only | No independent full-original claim. |
| [PMID:19056867](https://pmc.ncbi.nlm.nih.gov/articles/PMC2637050/) | Abstract only | Target supplementary identification unresolved. |
| [PMID:19380743](https://pmc.ncbi.nlm.nih.gov/articles/PMC2670881/) | Abstract only | No independent full-original claim. |
| [PMID:19605363](https://pmc.ncbi.nlm.nih.gov/articles/PMC2781994/) | Abstract only | Independently recovered original reconstitution and U2-OS Methods/Results read; purified rat protein and human-cell depletion/rat rescue remain distinct. |
| [PMID:19623537](https://pubmed.ncbi.nlm.nih.gov/19623537/) | Abstract only | No independent full-original claim. |
| [PMID:20711168](https://pmc.ncbi.nlm.nih.gov/articles/PMC2944065/) | Abstract only | Separately recovered PMC original Methods/Results. |
| [PMID:21423176](https://pmc.ncbi.nlm.nih.gov/articles/PMC3279191/) | Full text available | Selected Methods read; DNM2 supplementary row unresolved. |
| [PMID:21525035](https://pubmed.ncbi.nlm.nih.gov/21525035/) | Abstract only | No independent full-original claim. |
| [PMID:21706016](https://pubmed.ncbi.nlm.nih.gov/21706016/) | Abstract only | No independent full-original claim. |
| [PMID:21900206](https://pubmed.ncbi.nlm.nih.gov/21900206/) | Abstract only | No independent full-original claim. |
| [PMID:21988832](https://pmc.ncbi.nlm.nih.gov/articles/PMC3261708/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:22022388](https://pmc.ncbi.nlm.nih.gov/articles/PMC3194794/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:22623184](https://pubmed.ncbi.nlm.nih.gov/22623184/) | Abstract only | No independent full-original claim. |
| [PMID:23533145](https://pmc.ncbi.nlm.nih.gov/articles/PMC3773505/) | Full text available | Selected Methods read; DNM2 supplementary row unresolved. |
| [PMID:24135484](https://pmc.ncbi.nlm.nih.gov/articles/PMC3882057/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:24970086](https://pmc.ncbi.nlm.nih.gov/articles/PMC4601533/) | Abstract only | Separately recovered PMC original Figure 3 and Results. |
| [PMID:27107012](https://pmc.ncbi.nlm.nih.gov/articles/PMC4848762/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:29437695](https://pmc.ncbi.nlm.nih.gov/articles/PMC5891424/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:31980649](https://pmc.ncbi.nlm.nih.gov/articles/PMC6981206/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:32315611](https://pubmed.ncbi.nlm.nih.gov/32315611/) | Abstract only | Separately recovered accepted manuscript; construct-specific limits above. |
| [PMID:33713620](https://pmc.ncbi.nlm.nih.gov/articles/PMC7923941/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:33961781](https://pmc.ncbi.nlm.nih.gov/articles/PMC8165030/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:34744632](https://pmc.ncbi.nlm.nih.gov/articles/PMC8563704/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:35271311](https://pmc.ncbi.nlm.nih.gov/articles/PMC9119736/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:36445308](https://pmc.ncbi.nlm.nih.gov/articles/PMC9712776/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:40205054](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137143/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:7590285](https://pubmed.ncbi.nlm.nih.gov/7590285/) | Abstract only | No independent full-original claim. |
| [PMID:11076973](https://pmc.ncbi.nlm.nih.gov/articles/PMC2169433/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:15014125](https://pmc.ncbi.nlm.nih.gov/articles/PMC6729477/) | Abstract only | No independent full-original claim. |
| [PMID:18425118](https://pmc.ncbi.nlm.nih.gov/articles/PMC2851549/) | Full text available | Existing main full text preserved; actual read scope is abstract-only. |
| [PMID:18923138](https://pmc.ncbi.nlm.nih.gov/articles/PMC2592655/) | Abstract only | No independent full-original claim. |
| [PMID:21195118](https://pubmed.ncbi.nlm.nih.gov/21195118/) | Abstract only | No independent full-original claim. |
| [PMID:21210813](https://pmc.ncbi.nlm.nih.gov/articles/PMC3278041/) | Full text available | Selected passages only; see reference assessment. |
| [PMID:35620056](https://pmc.ncbi.nlm.nih.gov/articles/PMC9127447/) | Full text available | Selected passages only; see reference assessment. |

Positive generic binding without an evidenced finer class remains non-core under the [explicit ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/57106c38a03129a6c24f833761f784cbed11a98a/projects/CLINGEN_MENDELIAN.md#curation-instructions). The biological review is independent of provider availability; failed provider attempts did not produce a substitute provider-named report. The two inherited core quotes remain unchanged. Three additional short assay excerpts appear once each in YAML rows 119, 122 and 156; this guide adds no publication quotations.

### Shared publication reconciliation

The existing DNM1 source versions are reused for PMID:15703209 (full text) and PMID:17257598 (abstract only). The initial DNM2 fetch produced the opposite availability pattern; those genuine variants were retained as provenance. In particular, the detailed Myo1E/DNM2 evidence from PMID:17257598 was actually read in the independently fetched full original even though the shared publication cache is abstract-only. PMID:18425118 retains the existing full cache, while this review read only its abstract. No source text was spliced or rewritten to change availability.
