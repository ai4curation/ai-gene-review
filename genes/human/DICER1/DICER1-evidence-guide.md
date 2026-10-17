# DICER1 evidence guide

## Identity, products and scope

[HGNC:17098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17098) and [UniProt Q9UPY3](https://www.uniprot.org/uniprotkb/Q9UPY3/entry) identify human DICER1. The three official products reconstruct to 1922, 1829 and 820 amino acids from the displayed sequence and VAR_SEQ features. Imported product identifiers, names and source annotations are preserved. Historical 1912-aa constructs, experimental domain deletions and tagged proteins are not automatically assigned to a current natural product.

The review preserves all 140 seeded source annotation objects, including the negative RISC row and the separate contributes-to pre-miRNA-binding row. Four duplicate pairs in the 144-row QuickGO response were collapsed by the normal bootstrap. One integrated RNase III core covers performed pre-miRNA processing, siRNA processing and RISC assembly in the cytosolic loading system. No NEW annotation is proposed. Cytosol is nonexclusive: nuclear, perinuclear and extracellular observations are assessed separately.

Supported generic interactions are retained as non-core when no justified specific term is available, under the [explicit ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/bff21ea8eb90bc3e07bb2fbedf14c25d37080161/projects/CLINGEN_MENDELIAN.md#curation-instructions). Partner-class refinements describe the binding partner; they do not transfer its catalytic activity to Dicer. Missing relevant experimental detail produces uncertainty, not a claim that an interaction is false.

## Core experiments and natural products

- [PMID:12411504](https://doi.org/10.1093/emboj/cdf578), Results on human Dicer cloning, dsRNA cleavage and binding, and Methods on purification: a historical 1912-aa human clone was produced in Sf9 cells. Long dsRNA and precursor hairpins were processed; binding was separated from catalysis. This is direct target evidence, not an exact current-isoform alignment.
- [PMID:12411505](https://www.embopress.org/doi/full/10.1093/emboj/cdf582), ATP-depletion/K70A experiments and construct Methods: recombinant human and mammalian immunoprecipitate assays establish cleavage without added ATP under tested conditions. These results do not establish a standalone ATPase/helicase core or prove universal absence of nucleotide binding.
- [PMID:16357216](https://doi.org/10.1101/gad.1384005), Results on dissociation, Figure 7 and processing/cleavage Methods, recovered from author-posted original text: active AGO2 can be released from Dicer, but the source also retains active AGO2 on Dicer with a different precursor. The negative imported RISC row is retained as a source-specific mature-effector observation; it must not become universal exclusion from dynamic complexes. Mouse FLAG-AGO2 in initial human-cell experiments is distinguished from later human AGO2 constructs.
- [PMID:18178619](https://doudnalab.org/Publications/pnas-105-512.pdf), Figures 1–4 and purification Methods: purified human Dicer, AGO2 and TRBP reconstitute processing/loading. The precursor substrate is Drosophila pre-let-7. Its affinity measurement belongs to the complex, matching the imported contributes-to row; Dicer-only binding is grounded separately. AGO2 performs target slicing.
- [PMID:18508075](https://pubmed.ncbi.nlm.nih.gov/18508075/) and [PMID:25549615](https://pubmed.ncbi.nlm.nih.gov/25549615/) separate Dicer substrate binding from cleavage. Engineered domain variants and loop-mutated RNA substrates are not natural products. Failure to detect ATP binding/hydrolysis in a tested preparation is recorded without inferring loss of the entire helicase-like fold.
- [PMID:20615407](https://pubmed.ncbi.nlm.nih.gov/20615407/) identifies the neuroblastoma-associated splice transcript. [PMID:25911188](https://doi.org/10.1007/s11033-015-3878-6), original Methods, Figure 4 and dicing Results recovered from author-posted text, tests sequence-verified human FLAG constructs and pre-miR-549. Anti-FLAG-enriched t-Dicer retains asymmetric cleavage, with lower expression and increased sample input distinguished from equal enzyme concentrations. The experiments do not establish universal inactivity, a dominant-negative effect on every substrate, or activity of the separate 820-aa product.

## Interaction and source-integrity boundaries

The [15973356 original](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2944926/) and [16142218 original](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1369185/) were recovered separately because their normal caches are abstract-only. They establish TRBP–Dicer association with cellular and purified-protein evidence. Their different depletion/stability results are not collapsed into a universal rule. The 15973356 siRNA mobility shift is positive for TRBP and the complex but negative for Dicer alone under those conditions; the standalone Dicer siRNA-binding assertion remains unresolved.

The [14749716 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC1298981/) was recovered beyond the incomplete cached body. It supports Dicer interactions with AGO2 and PIWIL1. The [17932509 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2247381/) and human affinity-purification experiments in PMID:19716330 distinguish AGO1-containing complexes from AGO2-containing complexes. AGO1 is not given AGO2's nuclease class. Enzyme-binding refinements for AGO2, PIWIL1, ADAR1 and ALOX5 retain the original cellular, fragment or reconstituted-complex limits. ATPase-binding refinements for DHX9 and DHX58 use independently verified ATP-hydrolysis activity, not a helicase-like name alone.

[PMID:21903422](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3253658/) has genuine Results/Methods omitted from the normal cached body. Exact human IntAct nonexpanded coimmunoprecipitation records EBI-6124533 (PKR) and EBI-6125302 (DHX58) are distinct from spoke-expanded discovery records. They support kinase/ATPase partner classes without purified-contact claims. A metadata-listed 2011 erratum remains an access limitation; its scope is not assumed irrelevant.

[PMID:25446899](https://pubmed.ncbi.nlm.nih.gov/25446899/) reports Dicer immunoprecipitation with AGO2/TRBP in cancer-exosome preparations. The [2025 expression-of-concern text](https://mdanderson.elsevierpure.com/en/publications/erratum-cancer-exosomes-perform-cell-independent-microrna-biogene-2/), PMID:40930611, identifies Dicer Figure 3A lane reuse and other figure concerns, an institutional recommendation for retraction, authors' disagreement and ongoing journal review. No retraction or individual falsification of Figure 3J/K is inferred. The reference is DISPUTED and its two source-specific exosomal rows are unresolved; independent ordinary loading-complex evidence does not validate the exosomal preparation.

[PMID:28159509](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5363195/) independently detects protected DICER cargo in human pericardial-fluid vesicle preparations. Filtration/ExoQuick enrichment, immunoblotting and protection lost on sonication support contextual localization, with purity limits. No extracellular catalytic or angiogenic core is inferred.

[PMID:28546213](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5551500/) establishes TSN-mediated mature-miRNA decay. Actual Figure 1A shows TSN with AGO2/GW182; Dicer appears in a different knockdown panel. The relevant supplementary reciprocal-IP material was not recovered. All three listed Dicer pairs remain unresolved, without a misattribution claim or assignment of TSN catalysis to Dicer.

[PMID:40205054](https://www.nature.com/articles/s41586-025-08878-3) supplies a primary AP-MS network through its Data Availability section: NDEx UUID 95bc75d5-d1d1-11ee-8a40-005056ae23aa. The exact AGO1 bait node 552592, DICER1 prey node 550352 and edge 610082 support a measured association. This is not inferred map proximity. U2OS tagged-bait Methods, gene/product resolution limits and the unexplained node metadata field are kept distinct. [PMID:41039152](https://www.nature.com/articles/s41586-025-09648-x) corrects an equation and does not identify this pair.

[BioPlex, PMID:33961781](https://pmc.ncbi.nlm.nih.gov/articles/PMC8165030/), Methods on purification, bait QC and CompPASS-Plus, uses gene-level aggregation and tagged affinity purification. Exact target interaction records, not overall network quality, ground the PRKRA/AGO2/AGO1 pairs. AP-MS does not establish direct contact, an isoform-specific interaction or invariant stoichiometry. [PMID:28904190](https://pmc.ncbi.nlm.nih.gov/articles/PMC5686741/) supports tagged Nipah-M association but did not detect an effect on miRNA processing. [PMID:29657270](https://pubmed.ncbi.nlm.nih.gov/29657270/), two-hybrid Results, cellular coimmunoprecipitation Results, Discussion of full-length testing, and construct/IP Methods, supports a positive Dicer-fragment interaction and RNase-resistant association of cellular Dicer with expressed Flag-TWEAK. Full-length Dicer was negative in yeast two-hybrid; that does not refute the positive observations, but cellular co-recovery does not exclude a protein bridge. Overexpression-dependent localization and processing effects leave native access to transmembrane or soluble TWEAK unresolved. The original protein-association annotation is therefore retained as non-core; cytokine identity alone does not resolve these limitations sufficiently for the whole-product cytokine-binding refinement. No receptor or signaling activity is assigned.

## Propagation, pathway and compartment evidence

The saved PANTHER tree places human PTN002495246 below PTN000383725, PTN001029377 and PTN000383726. The protected PAINT IBDs are assessed as ancestral-function judgments. The target in a WITH/FROM list is legitimate experimental grounding. No inference is rejected for donor count, and no target residue loss is invented.

[PMID:20223951](https://pubmed.ncbi.nlm.nih.gov/20223951/) directly demonstrates apoptotic DNase activity of a caspase-generated worm DCR1 fragment. The GO:0004530 and GO:0006309 IBDs at PTN001029377 are retained non-core: the target is in the clade and no contradictory human loss or node-placement defect was established. Human activation/fragment correspondence remains a mechanistic question, not a basis for overturning the phylogeny.

Mouse donor studies [20463238](https://pubmed.ncbi.nlm.nih.gov/20463238/) and [20805985](https://pubmed.ncbi.nlm.nih.gov/20805985/) delete Dicer in Schwann cells, with differentiation/myelination defects and timing-dependent proliferation findings. [20648646](https://pubmed.ncbi.nlm.nih.gov/20648646/) tests primary rat Schwann cells and rat neuron coculture; human cells are used to produce viral reagent. These sources support developmental context, not human direct assays or neuron-intrinsic Dicer structure. Changes in steady-state transcription-factor mRNA do not resolve RNA polymerase II transcription-rate regulation.

Official InterPro entries, target coordinates and mappings support the PAZ, dsRNA-binding, dimerization and RNase III architecture. The IPR011545 ATP-binding mapping remains unresolved against target assay limits. Six current ARBA rule records were inspected, but target FunFam execution was not independently reproduced. Specific biological conclusions are grounded in direct target or traced donor evidence, not a claim of a new classifier run.

GO:0051239 is refined to four already-supported regulatory descendants: [GO:0010626](https://www.ebi.ac.uk/QuickGO/term/GO:0010626), [GO:0014040](https://www.ebi.ac.uk/QuickGO/term/GO:0014040), [GO:0031643](https://www.ebi.ac.uk/QuickGO/term/GO:0031643), and [GO:0032720](https://www.ebi.ac.uk/QuickGO/term/GO:0032720). QuickGO is_a/part_of paths checked on 2026-10-17 connect each to GO:0051239. GO:0032290 has no such path and remains a separate peripheral-myelin-formation assertion. The Schwann-cell sources above ground the first three roles, retaining species and developmental-stage limits. [PMID:26435691](https://pubmed.ncbi.nlm.nih.gov/26435691/), Figures 2–4 and cell-culture Methods, grounds the fourth in human Huh7 cells: DICER knockdown increases TNF mRNA responses to LPS, reduces mature miR-125b/miR-130a, and their expression reverses the TNF increase. This context does not imply universal regulation in every cytokine-producing cell. The replacement set corrects specificity without adding a NEW process or claiming to reproduce ARBA target-condition execution.

Typed Reactome event/member/component paths resolve to [DICER1/Q9UPY3 entity 203820](https://reactome.org/content/detail/R-HSA-203820) in [cytosol 70101](https://reactome.org/content/detail/70101). Dicer's precursor cleavage is separated from Argonaute passenger-strand removal and target slicing. The MITF-dependent expression event has Dicer as an output, not its transcriptional catalyst. [PMID:19729508](https://pubmed.ncbi.nlm.nih.gov/19729508/) directly tests Dicer cleavage of a tRNA–HIV RNA hybrid; this does not establish that all tRNA-derived fragments require Dicer.

The [Human Protein Atlas DICER1 record](https://www.proteinatlas.org/ENSG00000100697-DICER1/subcellular) supports cytosolic localization in its target metadata. Image pixels were not independently reinterpreted. [PMID:21858095](https://pubmed.ncbi.nlm.nih.gov/21858095/) and [PMID:33328224](https://pubmed.ncbi.nlm.nih.gov/33328224/) support human nuclear pools with different cellular contexts. The glioblastoma circular-RNA association depends on RBM3 and does not establish direct Dicer circular-RNA binding. Perinuclear and extracellular pools remain nonexclusive.

## Access ledger

Normal publication caches are immutable. A cache flag reports retrieval status; it does not prove that every Methods/Results section is present, nor that a separately recovered original was unavailable. The table separates those facts. “Selected original” means the claim-bearing Methods/Results or figure/caption were read; it does not claim every supplement or figure pixel was inspected. No provider text was invented after the configured research service failed authentication/quota checks.

| PMID | Normal cache | Evidence access used |
|---|---|---|
| [12411504](https://pubmed.ncbi.nlm.nih.gov/12411504/) | full_text_available: true | Selected complete cached original; independent core consultation. |
| [12411505](https://pubmed.ncbi.nlm.nih.gov/12411505/) | full_text_available: false | Selected publisher original; independent core consultation. |
| [12526743](https://pubmed.ncbi.nlm.nih.gov/12526743/) | full_text_available: false | Accessible abstract plus independent target biology/interaction records; no full original assay read claimed. |
| [14749716](https://pubmed.ncbi.nlm.nih.gov/14749716/) | full_text_available: true | Cached body incomplete; selected separately recovered publisher original. |
| [15973356](https://pubmed.ncbi.nlm.nih.gov/15973356/) | full_text_available: false | Selected separately recovered official PMC original, including binding/processing distinctions. |
| [16142218](https://pubmed.ncbi.nlm.nih.gov/16142218/) | full_text_available: false | Selected separately recovered official PMC original. |
| [16357216](https://pubmed.ncbi.nlm.nih.gov/16357216/) | full_text_available: false | Selected author-posted original and explicit release/retention passages; independent consultation. |
| [16424907](https://pubmed.ncbi.nlm.nih.gov/16424907/) | full_text_available: false | Selected separately recovered PMC original. |
| [17452327](https://pubmed.ncbi.nlm.nih.gov/17452327/) | full_text_available: false | Accessible abstract plus independent target biology/interaction records; no full original assay read claimed. |
| [17507929](https://pubmed.ncbi.nlm.nih.gov/17507929/) | full_text_available: false | Abstract only; complete Dicer multi-partner experiment unresolved. |
| [17531811](https://pubmed.ncbi.nlm.nih.gov/17531811/) | full_text_available: false | Accessible abstract plus independent target biology/interaction records; no full original assay read claimed. |
| [17920623](https://pubmed.ncbi.nlm.nih.gov/17920623/) | full_text_available: false | Accessible abstract plus independent target biology/interaction records; no full original assay read claimed. |
| [17932509](https://pubmed.ncbi.nlm.nih.gov/17932509/) | full_text_available: false | Selected separately recovered PMC original. |
| [18178619](https://pubmed.ncbi.nlm.nih.gov/18178619/) | full_text_available: false | Selected author-hosted original PDF; supplement and figure pixels not independently read. |
| [18325616](https://pubmed.ncbi.nlm.nih.gov/18325616/) | full_text_available: false | Accessible abstract plus independent target biology/interaction records; no full original assay read claimed. |
| [18508075](https://pubmed.ncbi.nlm.nih.gov/18508075/) | full_text_available: true | Selected cached original Methods/Results. |
| [19022417](https://pubmed.ncbi.nlm.nih.gov/19022417/) | full_text_available: true | Selected cached original Methods/Results. |
| [19701182](https://pubmed.ncbi.nlm.nih.gov/19701182/) | full_text_available: true | Selected cached original Methods/Results. |
| [19716330](https://pubmed.ncbi.nlm.nih.gov/19716330/) | full_text_available: true | Selected cached original Methods/Results. |
| [19804757](https://pubmed.ncbi.nlm.nih.gov/19804757/) | full_text_available: true | Selected cached original Methods/Results. |
| [19820710](https://pubmed.ncbi.nlm.nih.gov/19820710/) | full_text_available: true | Selected cached original Methods/Results. |
| [20869963](https://pubmed.ncbi.nlm.nih.gov/20869963/) | full_text_available: false | Accessible abstract plus independent target biology/interaction records; no full original assay read claimed. |
| [21753850](https://pubmed.ncbi.nlm.nih.gov/21753850/) | full_text_available: true | Selected cached original Methods/Results. |
| [21858095](https://pubmed.ncbi.nlm.nih.gov/21858095/) | full_text_available: true | Selected cached original Methods/Results. |
| [21903422](https://pubmed.ncbi.nlm.nih.gov/21903422/) | full_text_available: true | Selected recovered original and exact IntAct pairs; erratum scope not recovered. |
| [22105995](https://pubmed.ncbi.nlm.nih.gov/22105995/) | full_text_available: false | Abstract only; relevant Dicer-specific assay unresolved. |
| [23322395](https://pubmed.ncbi.nlm.nih.gov/23322395/) | full_text_available: false | Accessible abstract plus independent target biology/interaction records; no full original assay read claimed. |
| [23622242](https://pubmed.ncbi.nlm.nih.gov/23622242/) | full_text_available: true | Selected cached original Methods/Results. |
| [23661684](https://pubmed.ncbi.nlm.nih.gov/23661684/) | full_text_available: true | Selected cached original Methods/Results. |
| [23741051](https://pubmed.ncbi.nlm.nih.gov/23741051/) | full_text_available: true | Selected cached original Methods/Results. |
| [25446899](https://pubmed.ncbi.nlm.nih.gov/25446899/) | full_text_available: true | Selected original plus expression of concern; scientific reliability DISPUTED. |
| [25549615](https://pubmed.ncbi.nlm.nih.gov/25549615/) | full_text_available: true | Selected cached original Methods/Results. |
| [25557550](https://pubmed.ncbi.nlm.nih.gov/25557550/) | full_text_available: true | Selected cached original Methods/Results. |
| [26435691](https://pubmed.ncbi.nlm.nih.gov/26435691/) | full_text_available: true | Selected cached original Methods/Results. |
| [26496610](https://pubmed.ncbi.nlm.nih.gov/26496610/) | full_text_available: false | Accessible abstract plus independent target biology/interaction records; no full original assay read claimed. |
| [28159509](https://pubmed.ncbi.nlm.nih.gov/28159509/) | full_text_available: true | Selected original vesicle Methods/Results; independent source consultation. |
| [28546213](https://pubmed.ncbi.nlm.nih.gov/28546213/) | full_text_available: true | Selected original and actual Figure 1 pixels; relevant supplement not recovered. |
| [28904190](https://pubmed.ncbi.nlm.nih.gov/28904190/) | full_text_available: false | Selected separately recovered PMC original. |
| [29657270](https://pubmed.ncbi.nlm.nih.gov/29657270/) | full_text_available: true | Selected cached original Methods/Results. |
| [33328224](https://pubmed.ncbi.nlm.nih.gov/33328224/) | full_text_available: true | Selected cached original Methods/Results. |
| [33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | full_text_available: true | Selected genuine original AP-MS Methods plus exact target interaction records. |
| [40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/) | full_text_available: true | Selected original Methods/Data Availability and exact primary AP-MS graph edge. |
| [15242644](https://pubmed.ncbi.nlm.nih.gov/15242644/) | full_text_available: false | Abstract/background only; attempted thesis download was HTML, not an original PDF. |
| [20615407](https://pubmed.ncbi.nlm.nih.gov/20615407/) | full_text_available: false | Abstract and bounded indexed publisher Results; no complete publisher download. |
| [40930611](https://pubmed.ncbi.nlm.nih.gov/40930611/) | full_text_available: false | Full institutional expression-of-concern text; normal cache lacks its substantive body. |
| [39875610](https://pubmed.ncbi.nlm.nih.gov/39875610/) | full_text_available: false | Actual publisher correction text. |
| [20223951](https://pubmed.ncbi.nlm.nih.gov/20223951/) | current main: content_type full_text_xml; original isolated cache: full_text_available true | Selected cached original Methods/Results. |
| [41039152](https://pubmed.ncbi.nlm.nih.gov/41039152/) | full_text_available: false | Actual publisher correction text. |
| [25911188](https://pubmed.ncbi.nlm.nih.gov/25911188/) | full_text_available: false | Selected author-posted original Methods/Results, including pre-miR-549 assay. |
| [20805985](https://pubmed.ncbi.nlm.nih.gov/20805985/) | full_text_available: true | Selected cached original Methods/Results. |
| [20648646](https://pubmed.ncbi.nlm.nih.gov/20648646/) | full_text_available: false | Selected separately recovered official PMC original. |
| [19729508](https://pubmed.ncbi.nlm.nih.gov/19729508/) | full_text_available: true | Selected cached original Methods/Results. |
| [20463238](https://pubmed.ncbi.nlm.nih.gov/20463238/) | full_text_available: true | Selected cached original Methods/Results. |

## Quotations

Four short literal cache anchors are used once each in the review: 9 words from PMID:12411504, 8 from PMID:12411505, 5 from PMID:16357216 and 6 from PMID:18178619. Supporting entries elsewhere reuse those references without repeating the excerpts. This guide and the notes add no verbatim source quotations. Evidence is assessed by experiments and provenance, not by repeating the same quotation across rows.

Five context caches became available on main during the review: 20223951, 20805985, 39875610, 40930611 and 41039152. Publication uses those existing main bytes without replacing them. The original genuine retrievals remain separate evidence: 20805985 differs only in whitespace, 39875610 and 40930611 are identical, 20223951 uses a different full-text serialization, and 41039152 adds the correction body while retaining its false availability flag. The claim-bearing 20223951 cleavage passages and 41039152 equation correction were checked in the main versions.
