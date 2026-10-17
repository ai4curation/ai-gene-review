# DEGS1 evidence guide

Human DEGS1 is HGNC:13709 / reviewed UniProt O15121, a 323-residue protein. The official reviewed entry has no named alternative products; shorter unreviewed search hits are not treated as established functional isoforms. The existing review has 40 source annotations representing 43 GOA records: four IMP records for GO:0042284 / PMID:30620338 share a legacy review row. Their source identities, including qualifiers, remain unchanged.

## Enzyme and cellular evidence

| Source and access | Evidence actually read | Interpretation and limits |
|---|---|---|
| [Ternes et al., PMID:11937514](https://doi.org/10.1074/jbc.M202947200); selected publicly indexed original Methods/Results | Human DES1 IMAGE2578328/AF466375 full ORF expressed from pYES2 in sur2-deficient yeast; hydrolysis and HPLC/MS of cellular sphingolipids; human delta-4 product absent from the empty-vector control | Establishes human desaturation. This is not a purified free-sphinganine substrate assay. Small hydroxylated products across human/fly/fungal constructs prevent an absolute claim that human DES1 has no hydroxylase side activity. |
| [Pant et al., PMID:30620337](https://www.jci.org/articles/view/123959); genuine publisher original | Human patient lipidomics; validated zebrafish splice-morpholino experiments, lipid ratios, MBP-positive oligodendrocytes and locomotion; original Methods | Supports cellular desaturation and myelin phenotypes. The cached extraction omits important Results/Methods despite its full-text flag; those claims were checked against the separate original. No purified human enzyme assay is inferred. |
| [Karsai et al., PMID:30620338](https://www.jci.org/articles/view/124159); genuine publisher original | Human NM_003676.3 WT/A280V EGFP constructs in HeLa cells; PDI/Tim23 imaging; patient fibroblast and HAP1 knockout lipid measurements; labeling and hydrolysis Methods | Strong ER overlap and little Tim23 overlap do not mean mitochondrial absence. Cellular labeled-base measurements support conversion of sphingolipids without establishing purified free-sphinganine turnover. The original publication cache remains abstract-only and unchanged. |
| [PMID:36951944](https://pubmed.ncbi.nlm.nih.gov/36951944/); full original XML extraction | Human fibroblast immunofluorescence, human brain compartment fractionation, mouse MAM proteomics/PhotoClick experiments, original Methods | Supports enrichment at ER–mitochondrial contact domains. Altered PS/PE, SOAT1 activity and contact geometry are consequences of disrupted lipid composition, not evidence that DEGS1 performs those other enzyme reactions or acts as a tether. |

The two former cores repeated the same desaturase activity under overlapping biosynthetic processes. One core now combines GO:0042284, ceramide biosynthesis and ER membrane. This describes the N-acyl sphingoid reaction and its principal location without excluding other source-specific compartments. No new annotation is added to fill a core-coverage advisory.

## Retinol activity and physiological scope

[PMID:23143414](https://pubmed.ncbi.nlm.nih.gov/23143414/) was read in full-text Methods and Results. Human DES1 expression in 293T-cell homogenates increased retinol isomerization, and human DES1 was used in mouse rescue experiments. The purified GST-DES1 experiment and Müller-cell knockdown experiments used chicken DES1. These are distinct evidence types and species; none is silently relabeled as a purified human enzyme experiment.

Later [mouse Müller-cell conditional deletion, PMID:30645148](https://pmc.ncbi.nlm.nih.gov/articles/PMC6436658/), supported normal cone responses and rapid dark adaptation. Whole-retinal activity remained, so this is not equivalent to eliminating DES1 from every retinal cell. [Zebrafish degs1 knockout, PMID:32238432](https://pmc.ncbi.nlm.nih.gov/articles/PMC7212626/), produced normal tested photopic behavior at 5 dpf; assay sensitivity, age and possible compensation bound that result. Both papers' original relevant Methods and Results were read. They limit universal physiological claims without refuting the positive biochemical retinol assays or proving absence of a human role. Both existing retinol rows remain non-core, with a specific physiological question.

## Pair identity and function

The [HuRI original, PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/), describes quadruplicate pair retesting and sequence confirmation in its main Methods. A separate Supplementary Methods file was not recovered; no three-of-four threshold or pair-specific orthogonal assay is asserted.

| DEGS1 partner | Exact human pair record | Decision boundary |
|---|---|---|
| ARLN Q8WVX3-2 | IntAct EBI-24800565 / IM-25472-159295, validated two-hybrid; related configurations EBI-25209560 and EBI-24202692 | The official partner is a SERCA regulator, not an ATPase. Binding it does not establish DEGS1 ATPase regulation or adaptor activity. |
| SEMA4G Q9NTN9-2 | IntAct EBI-24564431 / IM-25472-138437, validated two-hybrid; related configurations EBI-25059137 and EBI-23503629 | The membrane-semaphorin partner class does not establish that DEGS1 is a receptor, receptor agonist or signaling adaptor. Endogenous co-compartmentalization and stoichiometry remain unestablished. |

Both positive interactions remain KEEP_AS_NON_CORE because no evidence-backed narrower molecular function was established. This follows the [explicit ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/9db646fd420946e2c8a9f325be9cd5b62b2c3d4c/projects/CLINGEN_MENDELIAN.md#curation-instructions), which is a scoped user instruction, not a change to repository-wide policy.

## Propagation, reactions and locations

PAINT node PTN001767866 carries the desaturase and ceramide-biosynthesis assertions. The current PTHR12879 tree places O15121 beneath that node. The target's own experimental evidence among the descendants is legitimate support; donor count is not used as an evidence score. ARBA00027533 has an applicable conjunction of IPR011388, IPR013866 and PTHR12879. InterPro maps O15121 to IPR005804 (68–291), IPR011388 (3–319) and IPR013866 (5–43). Their actual mappings and target matches were checked.

The four TOO_GENERAL decisions are judgments of informativeness, not false transfer: GO:0042284 entails catalytic activity, ceramide biosynthesis entails lipid metabolism, and ER membrane entails membrane. The useful sphingolipid pathway-level process is retained. Current GO:0009055 includes electron acceptors and enzymatic redox transformation; rejecting it solely because DEGS1 is not a mobile carrier was unjustified. It remains non-core, without inventing a source-specific electron-transfer assay.

[Reactome R-HSA-1660661](https://reactome.org/content/detail/R-HSA-1660661) contains reaction R-HSA-428259; catalyst 428230 links GO:0042284 to DEGS1 entity R-HSA-428201 at the ER membrane. The event distinguishes target assignment from reaction stoichiometry/cofactor evidence inferred from rat microsomes.

[Reactome R-HSA-6799350](https://reactome.org/content/detail/R-HSA-6799350) explicitly contains DEGS1 in input set R-HSA-6799368 through R-HSA-6799512 (specific-granule membrane) and output set R-HSA-6806323 through R-HSA-6806305 (plasma membrane). Both entities reference O15121. These context-specific TAS locations are retained non-core. The underlying granule-proteomics original was unavailable, so peptide-level evidence and fraction purity were not independently audited. An ER principal site is not contrary evidence against these modeled locations.

The Human Protein Atlas ENSG00000143753 record reports supported mitochondrial immunofluorescence with HPA076422 and a canonical DEGS1 epitope. It also lists additional locations. No additional location annotations are manufactured from that record, and immunofluorescence is not treated as a membrane-topology measurement.

## Explicit access limits

The full originals for PMID:1317856, PMID:16120614, PMID:19647031, PMID:24209621 and PMID:9188692 were not recovered after bounded publisher/repository attempts. Metadata, abstracts, redirect pages and access-denied HTML are not described as full articles. The myristoylation paper's exact recombinant construct species and fractionation controls remain unresolved.

The two cytoplasmic ER-leaflet rows (PMID:1317856 and PMID:16120614), the source-specific sphingomyelin IDA row (PMID:24209621), and the plasma-membrane TAS row from PMID:9188692 are UNDECIDED. Other broad functions explicitly supported by available evidence or independently established for DEGS1 remain accepted/non-core with their access limits stated. Titles foregrounding another enzyme or omission from an abstract do not establish misattribution.

The historical unsaturated-fatty-acid process is refined to ceramide biosynthesis using positive later human chemistry: the delta-4 bond is introduced into the sphingoid backbone, not the attached fatty-acid chain. This is not an experimental removal based on an inaccessible paper. The source annotation remains intact, with the refinement confined to its review.
