# DOCK2 review notes

## 2026-10-17 — molecular function, products and signaling

DOCK2 is a hematopoietic RAC guanine-nucleotide exchange factor. The human DOCK2–ELMO1 structure/biochemistry and patient-cell phenotypes support one integrated exchange and RAC-regulation unit, with cytosol as a positively supported functional pool. ELMO1 regulates accessibility of the catalytic machinery: removing its N-terminal region increases exchange in a purified assay but has a different effect on productive signaling in cells. These are assay-dependent regulatory observations, not a second catalytic activity. See [PMID:32651375](https://pubmed.ncbi.nlm.nih.gov/32651375/) and [PMID:26083206](https://pubmed.ncbi.nlm.nih.gov/26083206/).

The official alternative products are 1830 and 336 residues. The short product lacks the canonical C-terminal DHR2 region; its molecular activity remains unresolved rather than demonstrated absent. Historical full-length constructs and the 431-residue catalytic fragment do not establish equal activity of both natural products. The human 2YIN deposition is GECGD followed by canonical residues 1192–1622. The full-length 6TGC/6TGB sequences contain 524 unresolved positions; all 1306 known residues match, but this is not an exact all-residue sequence check. No unresolved position is treated as a mutation.

GO:0005096 requires acceleration of GTP hydrolysis. The imported electronic DHR2 inference conflates that activity with nucleotide exchange, despite the same InterPro record describing the GEF mechanism. Removing this mapping leaves all supported exchange annotations intact. The mouse T-cell paper supports RAC activation and synapse phenotypes; its inaccessible full text is not characterized as a wrong-gene experiment. The broad signaling annotations are refined to the performed positive RAC-regulation step, with no additional NEW process.

## Binary interactions and their scope

The [source record extract](DOCK2-source-data/README.md) preserves 46 literal interaction assertions and 142 matching curated records. The two older RAC1 papers have positive MINT records, including a DOCK2 1115–1680 binding-associated fragment and a separately unspecified construct taxon. They are not rejected because their abstracts foreground DOCK180. Full original access remains limited.

HI-II-14 and HuRI support binary associations with sequence-confirmed reference reagents. They do not establish a native cellular pathway, coexpression or stoichiometry for every pair. Established partner classes justify specific binding terms for enzymes, an E3 ligase, a DNA-binding transcription factor, a signaling scaffold and keratins. No partner activity is assigned to DOCK2 itself. Keratin monomer binding is not automatically binding to an assembled intermediate filament.

The full-length MTUS2 partner and short Q5JR59-3 product are distinct claims: the short sequence lacks the mapped MAPRE1/KIF2C regulatory interaction regions, so its positive association remains generic. PCSK5-2 retains its peptidase domain and catalytic residues, but the two-hybrid assay does not test processing or activity in the secretory pathway. GOLGA6L9 and TENM4 separately carry sufficient-binding-region features; their reference-sequence checksums are not proof of full-length reagents.

Positive generic interactions are retained outside the core where a narrower justified class is not established. This applies the explicit [ClinGen project binding instruction](https://github.com/ai4curation/ai-gene-review/blob/50db4d61a99d7a30369f7bae9c38845894441872/projects/CLINGEN_MENDELIAN.md#curation-instructions). Different partner identities and tested products are different biological claims; a source-specific limit does not negate DOCK2 protein binding in general.

## Ortholog evidence and the ASC addendum

The actual PAINT target lineage reaches the IBD nodes for exchange, small-GTPase binding, cytoplasm, plasma membrane, migration and myoblast fusion. The experimental donor records and exact IBD assertions were checked. A short donor list is not weak evidence, and the target's own experimental annotation is legitimate grounding. Conserved myoblast-fusion evidence is retained contextually without relabeling zebrafish/fly experiments as human DOCK2 assays.

The recovered [2011 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3178750/) Figure 6 and uptake Methods show positive mouse Dock2 loss/rescue evidence for soluble-antigen and particle uptake. The [2012 addendum](https://doi.org/10.1038/ni.2389) limits the proposed ASC-to-Dock2 relationship to some ASC-null mouse lines and leaves the cause unresolved. It explicitly retains the DOCK2 uptake/rescue findings. No particular passenger mutation, retraction or invalidation of every DOCK2 result is inferred. The reference assessment flags the disputed general upstream interpretation while preserving the direct observations.

## Compartment evidence

Reactome resolves the exact human Q92608 participant, including residues 1–1830 and compartment. DOCK2 is a `hasMember` of a `CandidateSet` in the RAC2 exchange model, not an experimentally measured RAC2 reaction merely by virtue of model membership. The cytosol annotation is positively supported by the participant record and is not exclusive of regulated membrane association.

The granule-lumen and extracellular assertions have exact target-containing Reactome paths. They are retained as curated contextual pools, with explicit limits because the primary target-proteomics table was not recovered. Jurkat F-actin colocalization supports a cytoskeletal pool but not direct actin binding. The membrane-enriched YTS screen is compatible with peripheral association. The separate B-cell-exosome assertion remains UNDECIDED because the target-specific table could not be recovered; no contamination or misattribution is claimed.

## Source preservation and access

All 77 seeded source dictionaries, including reference IDs, evidence codes, partners and qualifiers, remain unchanged. No NEW annotations are proposed. The review has 9 ACCEPT, 50 KEEP_AS_NON_CORE, 16 MODIFY, one REMOVE and one UNDECIDED decision. One integrated core and both official products are represented. Provisional DRAFT reflects retained generic-binding assertions; final status is determined by normal repository checks.

Normal isolated fetching and publication caching were performed. The genuine Falcon attempt failed authentication and the configured perplexity-lite fallback returned insufficient quota; no provider text was fabricated. Source caches and their flags remain unchanged. Separate original recovery is documented in the [source evidence guide](DOCK2-source-evidence.md), including cases where a `full_text_available` cache omits Methods. Short exact source anchors occur once each in the review YAML; reference-only support elsewhere avoids duplicating those quotations.
