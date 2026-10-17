# DEGS1 evidence guide

Human DEGS1 is HGNC:13709 / reviewed UniProt O15121, a 323-residue protein. The official reviewed entry has no named alternative products; shorter unreviewed search hits are not treated as established functional isoforms. The existing review has 40 source annotations representing 43 GOA records: four IMP records for GO:0042284 / PMID:30620338 share a legacy review row. Their source identities, including qualifiers, remain unchanged.

## Enzyme and cellular evidence

| Source and access | Evidence actually read | Interpretation and limits |
|---|---|---|
| [Ternes et al., PMID:11937514](https://doi.org/10.1074/jbc.M202947200); selected publicly indexed original Methods/Results | Human DES1 IMAGE2578328/AF466375 full ORF expressed from pYES2 in sur2-deficient yeast; hydrolysis and HPLC/MS of cellular sphingolipids; human delta-4 product absent from the empty-vector control | Establishes human desaturation. This is not a purified free-sphinganine substrate assay. Small hydroxylated products across human/fly/fungal constructs prevent an absolute claim that human DES1 has no hydroxylase side activity. |
| [Pant et al., PMID:30620337](https://www.jci.org/articles/view/123959); genuine publisher original | Human patient lipidomics; validated zebrafish splice-morpholino experiments, lipid ratios, MBP-positive oligodendrocytes and locomotion; original Methods | Supports cellular desaturation and myelin phenotypes. The cached extraction omits important Results/Methods despite its full-text flag; those claims were checked against the separate original. No purified human enzyme assay is inferred. |
| [Karsai et al., PMID:30620338](https://www.jci.org/articles/view/124159); genuine publisher original | Human NM_003676.3 WT/A280V EGFP constructs in HeLa cells; PDI/Tim23 imaging; patient fibroblast and HAP1 knockout lipid measurements; labeling and hydrolysis Methods | Strong ER overlap and little Tim23 overlap do not mean mitochondrial absence. Cellular labeled-base measurements support conversion of sphingolipids without establishing purified free-sphinganine turnover. The original publication cache remains abstract-only and unchanged. |
| [PMID:36951944](https://pubmed.ncbi.nlm.nih.gov/36951944/); full original XML extraction | Human fibroblast immunofluorescence, human brain compartment fractionation, mouse MAM proteomics/PhotoClick experiments, original Methods | Supports enrichment at ER–mitochondrial contact domains. Altered PS/PE, SOAT1 activity and contact geometry are consequences of disrupted lipid composition, not evidence that DEGS1 performs those other enzyme reactions or acts as a tether. |

The two former cores repeated the same desaturase activity under overlapping biosynthetic processes. One core combines GO:0042284, ceramide biosynthesis and the cytoplasmic side of the ER membrane (GO:0098554). This describes the N-acyl sphingoid reaction and its principal location without excluding other source-specific compartments. No new annotation is added to fill a core-coverage advisory.

## Retinol activity and physiological scope

[PMID:23143414](https://pubmed.ncbi.nlm.nih.gov/23143414/) was read in full-text Methods and Results. Human DES1 expression in 293T-cell homogenates increased retinol isomerization, and human DES1 was used in mouse rescue experiments. The purified GST-DES1 experiment and Müller-cell knockdown experiments used chicken DES1. These are distinct evidence types and species; none is silently relabeled as a purified human enzyme experiment.

Later [mouse Müller-cell conditional deletion, PMID:30645148](https://pmc.ncbi.nlm.nih.gov/articles/PMC6436658/), supported normal cone responses and rapid dark adaptation. Whole-retinal activity remained, so this is not equivalent to eliminating DES1 from every retinal cell. [Zebrafish degs1 knockout, PMID:32238432](https://pmc.ncbi.nlm.nih.gov/articles/PMC7212626/), produced normal tested photopic behavior at 5 dpf; assay sensitivity, age and possible compensation bound that result. Both papers' original relevant Methods and Results were read. They limit universal physiological claims without refuting the positive biochemical retinol assays or proving absence of a human role. Both existing retinol rows remain non-core, with a specific physiological question.

## Pair identity and function

The [HuRI original, PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/), describes quadruplicate pair retesting and sequence confirmation in its main Methods. A separate Supplementary Methods file was not recovered; no three-of-four threshold or pair-specific orthogonal assay is asserted.

| DEGS1 partner | Exact human pair record | Decision boundary |
|---|---|---|
| ARLN Q8WVX3-2 | IntAct [EBI-24800565](https://www.ebi.ac.uk/intact/interaction/EBI-24800565) / IM-25472-159295, validated two-hybrid; related configurations [EBI-25209560](https://www.ebi.ac.uk/intact/interaction/EBI-25209560) and [EBI-24202692](https://www.ebi.ac.uk/intact/interaction/EBI-24202692) | The official partner is a SERCA regulator, not an ATPase. Binding it does not establish DEGS1 ATPase regulation or adaptor activity. |
| SEMA4G Q9NTN9-2 | IntAct [EBI-24564431](https://www.ebi.ac.uk/intact/interaction/EBI-24564431) / IM-25472-138437, validated two-hybrid; related configurations [EBI-25059137](https://www.ebi.ac.uk/intact/interaction/EBI-25059137) and [EBI-23503629](https://www.ebi.ac.uk/intact/interaction/EBI-23503629) | The membrane-semaphorin partner class does not establish that DEGS1 is a receptor, receptor agonist or signaling adaptor. Endogenous co-compartmentalization and stoichiometry remain unestablished. |

Both positive interactions remain KEEP_AS_NON_CORE because no evidence-backed narrower molecular function was established. This follows the [explicit ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/9db646fd420946e2c8a9f325be9cd5b62b2c3d4c/projects/CLINGEN_MENDELIAN.md#curation-instructions), which is a scoped user instruction, not a change to repository-wide policy.

## Propagation, reactions and locations

PAINT node PTN001767866 carries the desaturase and ceramide-biosynthesis assertions. The current PTHR12879 tree places O15121 beneath that node. The target's own experimental evidence among the descendants is legitimate support; donor count is not used as an evidence score. ARBA00027533 has an applicable conjunction of IPR011388, IPR013866 and PTHR12879. InterPro maps O15121 to IPR005804 (68–291), IPR011388 (3–319) and IPR013866 (5–43). Their actual mappings and target matches were checked.

The four broad annotations now use MODIFY with supported specific replacements, as judgments of informativeness rather than false transfer: GO:0042284 entails catalytic activity, ceramide biosynthesis entails lipid metabolism, and ER membrane entails membrane. The useful sphingolipid pathway-level process is retained. Current GO:0009055 includes electron acceptors and enzymatic redox transformation; rejecting it solely because DEGS1 is not a mobile carrier was unjustified. It remains non-core, without inventing a source-specific electron-transfer assay.

[Reactome R-HSA-1660661](https://reactome.org/content/detail/R-HSA-1660661) contains reaction R-HSA-428259; catalyst 428230 links GO:0042284 to DEGS1 entity R-HSA-428201 at the ER membrane. The event distinguishes target assignment from reaction stoichiometry/cofactor evidence inferred from rat microsomes.

[Reactome R-HSA-6799350](https://reactome.org/content/detail/R-HSA-6799350) explicitly contains DEGS1 in input set R-HSA-6799368 through R-HSA-6799512 (specific-granule membrane) and output set R-HSA-6806323 through R-HSA-6806305 (plasma membrane). Both entities reference O15121. These context-specific TAS locations are retained non-core. The underlying granule-proteomics original was unavailable, so peptide-level evidence and fraction purity were not independently audited. An ER principal site is not contrary evidence against these modeled locations.

The [Human Protein Atlas ENSG00000143753 subcellular record](https://www.proteinatlas.org/ENSG00000143753-DEGS1/subcellular) ([raw XML](https://www.proteinatlas.org/ENSG00000143753.xml)) reports supported mitochondrial immunofluorescence with [HPA076422](https://www.proteinatlas.org/ENSG00000143753-DEGS1/antibody) and a canonical DEGS1 epitope. The XML identifies ICC/IF, supported validation and mitochondrial calls in BJ, U-251MG and U2OS; KOLF2.1J additionally has a plasma-membrane data call. These are data-record reads, not independent microscopy-image interpretation. It also lists additional locations. No additional location annotations are manufactured from that record, and immunofluorescence is not treated as a membrane-topology measurement.

## Explicit access limits

The full originals for PMID:1317856, PMID:16120614, PMID:19647031, PMID:24209621 and PMID:9188692 were not recovered after bounded publisher/repository attempts. Metadata, abstracts, redirect pages and access-denied HTML are not described as full articles. The myristoylation paper's exact recombinant construct species and fractionation controls remain unresolved.

The source-specific sphingomyelin IDA row from PMID:24209621 remains UNDECIDED. The cytoplasmic ER-face rows retain ACCEPT on explicit target-specific Reactome corroboration, and the historical plasma-membrane TAS retains KEEP_AS_NON_CORE on the independent positive exocytosis model. The source-specific experiments in the inaccessible originals remain unverified. Other broad functions explicitly supported by available evidence or independently established for DEGS1 remain accepted/non-core with their access limits stated. Titles foregrounding another enzyme or omission from an abstract do not establish misattribution.

The historical unsaturated-fatty-acid process is refined to ceramide biosynthesis using positive later human chemistry: the delta-4 bond is introduced into the sphingoid backbone, not the attached fatty-acid chain. This is not an experimental removal based on an inaccessible paper. The source annotation remains intact, with the refinement confined to its review.

## Source-specific follow-up and public locators (2026-10-17)

The [current GO:0009055 definition](https://www.ebi.ac.uk/QuickGO/term/GO:0009055) includes enzymatic redox transfer, rather than requiring an independently mobile electron carrier. Its typed ancestor is molecular function; the specific DEGS1 desaturase term has no asserted ancestor path to it. Cytochrome b5 supplies electrons to the terminal desaturase reaction. Retaining the historical broad TAS non-core does not assign DEGS1 an autonomous carrier role or establish the unrecovered 1997 assay. [FADS1 O60427](https://www.uniprot.org/uniprotkb/O60427/entry) contains a b5 domain but has no GO:0009055 among all 38 records in the [complete target query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:O60427&limit=200) captured on 2026-10-17. Comparator absence is not a contradiction of an existing DEGS1 assertion, and domain presence is not sufficient evidence to add one.

The cytoplasmic ER-face placement is stated in the [R-HSA-428259 summation](https://reactome.org/ContentService/data/query/R-HSA-428259). This corroborates the two imported topology assertions while preserving the unavailable PMID:1317856 and PMID:16120614 experiment limits. It does not turn the human PDI colocalization assay into leaflet-resolution imaging.

The exact modeled exocytosis paths can be inspected independently:

- [Event 6799350](https://reactome.org/ContentService/data/query/6799350) → input [set 6799368](https://reactome.org/ContentService/data/query/6799368) → [DEGS1 6799512](https://reactome.org/ContentService/data/query/6799512), O15121 residues 2–323 at specific-granule membrane.
- The same event → output [set 6806323](https://reactome.org/ContentService/data/query/6806323) → [DEGS1 6806305](https://reactome.org/ContentService/data/query/6806305), O15121 residues 2–323 at plasma membrane.

These literal records support contextual location without independently validating the underlying proteomic peptides or the 1997 localization assay. Exact HuRI accession, PMID and interaction-method fields identify the six linked IntAct records above; multiple discovery/validation configurations explain the different record identifiers. They do not identify a physiological signaling function.

### Short original-text anchors

These excerpts come from separately inspected originals, not from repaired or expanded publication caches. All other details in this guide are paraphrases.

- PMID:11937514, [DOI 10.1074/jbc.M202947200](https://doi.org/10.1074/jbc.M202947200), Results, desaturase activity section and Figure 4, printed page 25514: **“H. sapiens DES1, 2.1 mol %”**. The value refers to the delta-4 sphingoid base in cellular lipids from the human construct; Methods, Cloning and Sphingoid Base Analysis identify IMAGE2578328/AF466375, pYES2/sur2-deficient yeast and hydrolysis/HPLC-MS. It is not a purified free-sphinganine turnover rate. The [publicly indexed original](https://www.researchgate.net/publication/11427843_Identification_and_Characterization_of_a_Sphingolipid_D4-Desaturase_Family) provides the selected text; no whole-original or figure-pixel read is claimed.
- PMID:30620338, [DOI 10.1172/JCI124159](https://www.jci.org/articles/view/124159), Results, Splicing/subcellular localization/expression and Figure 2B–E: **“Both WT and mut DEGS1 colocalized with the ER marker”**. The named marker is PDI; Methods, Cloning and Immunohistochemistry identify the human NM_003676.3 EGFP constructs and HeLa assay. The same Results describe little Tim23 overlap. Methods, Metabolic labeling and sphingoid-base profiling explain that hydrolysis releases the lipid backbones, so the cellular d7-sphinganine experiment does not alone establish a purified free-base substrate.


## Quotation locations and source provenance (2026-10-17)

The core quotes the [cached Reactome reaction](../../../reactome/R-HSA-428259.md), Summary, once for its cytosolic ER-face placement. The quoted [UniProt O15121 catalytic reaction](DEGS1-uniprot.txt) is the CATALYTIC ACTIVITY block at source lines 145–151, supported there by ECO:0000269 with PMID:11937514 and PMID:30620338. Only flat-file line codes and wrapping are removed from that quotation; the chemical content is unchanged.

The electron-transfer row quotes the cytochrome-b5 coupling statement from PMID:23143414, Results, Identification of Isomerase-2 by Expression Screening (cached line 90). That introductory statement cites earlier work; it is not represented as a new carrier assay in that study. Its separate retinol quote comes from Results, Isomerase-2 Activities of Other Membrane Desaturases (cached line 110), where the tested human constructs and 293T-homogenate comparison bound the claim. Together these excerpts total 24 words from the paper. The longer uniqueness wording would duplicate the positive assay evidence and is not additionally quoted.

The MAM-enrichment excerpt from PMID:36951944 is attached to the core's ER-contact context. The mitochondrial annotation instead follows the [HPA subcellular record](https://www.proteinatlas.org/ENSG00000143753-DEGS1/subcellular) and its [XML data](https://www.proteinatlas.org/ENSG00000143753.xml), as described above; the MAM excerpt is not used as a substitute for that mitochondrial evidence. Reference-only support elsewhere avoids repeating the same excerpts.
