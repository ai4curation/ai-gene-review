# EFEMP2 evidence notes

EFEMP2 encodes fibulin-4, a secreted extracellular matrix protein. The current human reference is O95967, 443 residues. Its principal experimentally supported mechanism is organization of elastic-fiber components: fibulin-4 binds pro-lysyl oxidase and tropoelastin and helps bring enzyme and substrate together. Lysyl oxidase performs the oxidative chemistry. Matrix assembly, component concentration and tissue context influence the resulting cross-links and fiber organization.

The review retains all 162 imported assertions and their source references, partners, qualifiers and product scope. There are 15 ACCEPT, 81 KEEP_AS_NON_CORE, 58 MODIFY, seven UNDECIDED and one MARK_AS_OVER_ANNOTATED decisions. No new annotation or quotation is added. The [source guide](EFEMP2-source-guide.md) distinguishes the available original experiments from unresolved source-specific claims. The [evidence extracts](EFEMP2-evidence/README.md) preserve database records, sequence checks and target-table measurements with reproducible extraction.

## Elastic-fiber mechanism and experimental reagents

[PMID:19570982](https://pubmed.ncbi.nlm.nih.gov/19570982/) supports interactions among fibulin-4, the LOX propeptide and tropoelastin, including concentration-dependent ternary organization. Its human fibulin-4 constructs are described literally as residues 26–418, 26–217 and 98–303. Those historical boundaries are not equated with the current 443-residue reference sequence. Fibrillin-1 can compete with this organization. The reported human ARPE19 fibulin-4 knockdown reduced expression by about 70% and modestly increased desmosine, whereas the rat RFL6 knockdown concerned fibulin-5. These experiments do not support a universal monotonic relation between fibulin-4 abundance and total cross-link content.

[PMID:19855011](https://pubmed.ncbi.nlm.nih.gov/19855011/) links pro-LOX recruitment to elastic-fiber organization through binding experiments, human fibroblast localization and mouse loss-of-function findings. Its ternary assay used purified tropoelastin with HEK293T-conditioned pro-LOX; it was not a fully purified three-protein system. Supplementary construct details were unavailable. Cell-line species, protein construct species and current natural-product identity are therefore kept separate.

These complementary observations support one **enzyme-substrate adaptor activity** core (GO:0140767), elastic fiber assembly (GO:0048251) and extracellular matrix location (GO:0031012). The core captures the physical organizing contribution rather than assigning LOX catalysis to EFEMP2. Two existing binding assertions are refined to the adaptor activity; no redundant NEW row is needed. Broader structural contributions are described within the same mechanism.

The mouse knockout and matrix-binding experiments in [PMID:16478991](https://pubmed.ncbi.nlm.nih.gov/16478991/) support conserved elastic-fiber assembly. Its human EFEMP2/elastin cell-lysate coimmunoprecipitation and purified mouse fibulin-4/bovine elastin experiment are different evidence. The in-vitro recombinant elastin-like-polypeptide system in [PMID:18973305](https://pubmed.ncbi.nlm.nih.gov/18973305/) and the fibrillin specificity experiments in [PMID:19349279](https://pubmed.ncbi.nlm.nih.gov/19349279/) further delimit matrix assembly and binding contexts.

## Collagen, vascular cells and accessory properties

Mouse Efemp2 loss and E57K studies support collagen-fibril and vascular-cell effects, retained as contextual process annotations. The actual studies distinguish matrix architecture from changes in smooth-muscle maturation, proliferation and angiotensin signaling ([PMID:20019329](https://pubmed.ncbi.nlm.nih.gov/20019329/), [PMID:23636094](https://pubmed.ncbi.nlm.nih.gov/23636094/), [PMID:26178373](https://pubmed.ncbi.nlm.nih.gov/26178373/), [PMID:26711913](https://pubmed.ncbi.nlm.nih.gov/26711913/)). Angiotensin-pathway inhibition can suppress hyperproliferation and aneurysm phenotypes without repairing the elastic-fiber defect.

[PMID:26220971](https://pubmed.ncbi.nlm.nih.gov/26220971/) documents aortic collagen disorganization and reduced mature cross-links, with largely retained LOX processing. Fibulin-4 did not stimulate the tested PCOLCE/BMP1 cleavage reaction. These findings support matrix organization without establishing EFEMP2 protease activity or a universal direct collagen-cross-linking mechanism.

Heparin binding, multimerization, proteolytic susceptibility and cell-adhesion observations are retained at the reported assay scope ([PMID:23782690](https://pubmed.ncbi.nlm.nih.gov/23782690/)). Susceptibility to cleavage is not protease activity. An unestablished cell receptor is not inferred from adhesion. These properties do not require a second core function merely to mirror each annotation.

## Protein interactions and partner classes

The 120 imported generic-binding records were assessed individually. Exact source-linked pair records are joined by target accession, partner accession and publication. The extract records methods, taxon fields, negative flags, reference-sequence checksums and fragment features. Sixteen alternative partner sequences were reconstructed from official sequence edits and matched to the corresponding FASTAs. A correct reference checksum is not authentication of an archived experimental insert, and a full reference sequence is not a reason to ignore an explicitly recorded fragment.

Supported partner-class refinements describe binding to that class. They do not transfer the partner's enzymatic, transcriptional, receptor or transport activity to EFEMP2. Binary assay positives are not discarded merely because fibulin-4 is secreted or because a native extracellular complex has not been demonstrated. Under the [ClinGen project policy](../../../projects/CLINGEN_MENDELIAN.md), a supported generic protein-binding record remains KEEP_AS_NON_CORE when no informative evidence-backed refinement is available.

Several boundaries matter:

- The IL16 N-terminal fragment excludes its mature cytokine region. Truncated FTO, ANAPC11 and transporter products also prevent unqualified transfer of the full protein's partner class.
- Four keratin-associated proteins have inferred keratin-filament locations, but their hair interfilamentous-matrix roles do not securely establish them as cytoskeletal protein components for GO:0008092. Their positive binding records remain non-core; no requirement that a partner itself polymerize is imposed.
- Human SLC16A5/MCT6 transport of bumetanide and other drugs in Xenopus oocytes supports a transporter-binding refinement despite uncertainty about its physiological substrate ([PMID:16174808](https://pubmed.ncbi.nlm.nih.gov/16174808/)).
- CNNM3's TRPM7 regulatory role and the unresolved distinction from independent transport prevent a confident transporter-class refinement here. The positive pair is retained, and the curated phylogenetic inference is not declared false ([PMID:34928937](https://pubmed.ncbi.nlm.nih.gov/34928937/), [PMID:36972446](https://pubmed.ncbi.nlm.nih.gov/36972446/)).

One source mismatch is explicit. [PMID:22919265](https://pubmed.ncbi.nlm.nih.gov/22919265/) assays PITX2 with a Delta-N36 EFEMP2 construct, including reciprocal COS-7 coimmunoprecipitation. The imported record instead names LOX/P28300. Its original partner and citation are preserved, and the paper's actual generic binding evidence is retained as non-core. No transcription-factor-binding refinement is placed on this LOX-tagged record. Independent LOX evidence from PMID19570982 and PMID19855011 remains valid.

The abstract of [PMID:27339457](https://pubmed.ncbi.nlm.nih.gov/27339457/) identifies several extracellular partners, but full target-specific tables were unavailable. The imported aggregate additionally includes TGFB1 and LOXL2, whose exact assay attribution was not resolved. It remains one imported source object; no unsupported source splitting or claim of biological falsity is made.

## Locations, tables and inherited assertions

The original [PMID:28327460](https://pubmed.ncbi.nlm.nih.gov/28327460/) publisher workbook detects EFEMP2 in matrix preparations from five of six donors. Table I physical row 29 gives donor 1 as not detected; repeated-experiment values are not recast as integer unique-peptide counts. Table VII row 95 is expression-cluster context, not another protein measurement.

The [PMID:19199708](https://pubmed.ncbi.nlm.nih.gov/19199708/) supplementary workbook lists an EFEMP2 precursor at physical row 284 of the sheet labeled `Paratid Exosomes`: three sequences, five spectra and 6.3% sequence coverage. This positive fraction observation is non-core. It does not establish an essential vesicle function, and the incomplete article cache is not described as complete Methods access.

Seven source-specific locations remain undecided where narrower target evidence could not be verified: basement-membrane assertions, two additional extracellular-vesicle sources, the ARBA non-collagenous basement-membrane compartment and the MatrisomeDB interstitial-matrix assertion. General extracellular localization neither proves nor disproves these narrower assignments. The ovarian-tissue assay in [PMID:25885889](https://pubmed.ncbi.nlm.nih.gov/25885889/) scores cytoplasmic granules and perivascular staining, rather than specifically resolving the non-collagenous compartment of solid-phase basement-membrane extracellular matrix; that narrower attribution is marked over-annotated without denying the observed staining.

Current PANTHER data place EFEMP2 in PTHR24034:SF96. The 1104-node tree and 1104-sequence MSA contain the exact 443-residue human sequence below both literal IBD nodes: PTN001170088 for extracellular matrix and PTN002778230 for elastic-fiber assembly. Descendant donor paths are explicit. The target's presence among donor evidence is expected and not circular. The normal UniProt-derived PTHR24050 lookup is retained as downloaded source provenance, separately from the current tree reconstruction.

Reactome's saved paths explicitly reach EFEMP2/O95967 residues 24–443 through `hasMember` and complex-component relations. These are curated assembly-model memberships, not new purified-protein assays.

## Access and provenance

Reference identifiers and titles retain their downloaded source identity. A bibliographically verified reference can still leave a specific target attribution unresolved; those limits are stated in each reference assessment. Abstract-only committed caches are not relabeled as full text because an external original was separately recovered. Failed supplementary or publisher routes are not treated as article evidence.

The configured Falcon research attempt failed with HTTP 403, and its attempted Perplexity-lite fallback failed with HTTP 401 for insufficient quota. No provider report was invented. Literature notes and original-source assessment supplied the evidence review. Downloaded publication, GOA, UniProt and other machine-source bytes remain unchanged.

## Follow-up: binding scope and consistent location claims

The 39 challenged partner-class refinements were checked against 125 literal interaction records, official partner functions/domains and recorded constructs. Their scope is association with an identified class of protein, not transfer of the partner's activity to EFEMP2 or proof of a native intracellular complex. The [ClinGen binding policy](../../../projects/CLINGEN_MENDELIAN.md) permits evidence-backed class refinements and retains supported generic binding as non-core where a more informative class is not justified. Secretion alone does not demonstrate that a reported assay interaction is false. The [source guide](EFEMP2-source-guide.md) now distinguishes the pair, partner-class and native-context evidence explicitly.

Three action changes were made. The PMID:27339457 aggregate is refined to extracellular matrix binding on its LTBP interaction evidence, preserving all seven imported partners and the missing-full-Methods limitation. The urinary exosome annotation is retained as non-core consistently with independently observed parotid-fraction EFEMP2, while its own unrecovered supplementary target row remains explicitly unverified. The ovarian-staining annotation for the non-collagenous basement-membrane compartment becomes unresolved, matching the unresolved electronic claim: positive cytoplasmic/perivascular staining does not resolve that compartment, but does not refute it either.

All 162 imported source dictionaries, source qualifiers, the single official product and integrated adaptor core are retained. No annotation or quotation is added. Exact cache hashes/header lines and original-access locators make the evidence checkable without implying that an abstract-only cache contains unavailable Methods or supplementary tables.
