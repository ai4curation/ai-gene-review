# BCL11A preliminary biological research

2026-09-30. These are manual research notes, not a generated provider report. The canonical primary seed is not yet imported. All 32 seeded annotation objects were independently read in actual178e2e; source consistency is separately checked by the actual Seed47 validator.

## Read boundaries

- Actualb216fe: complete metadata and abstracts of the four normal Seed47 publication candidates (PMIDs16704730,19153051,23644491,29606353), and the complete three Reactome candidate records. This was not a complete-paper read.
- Actualc21a2f: UniProt reference declarations and curated FUNCTION, SUBUNIT, INTERACTION, SUBCELLULAR LOCATION, ALTERNATIVE PRODUCTS, TISSUE SPECIFICITY, DOMAIN, PTM and DISEASE sections. The selected FT note lines are incomplete fragments; no complete FT/VAR_SEQ read is claimed by root. B3 separately read all product/VAR_SEQ blocks.
- `root-functional-context-web.json`: official PubMed20534004 and18681895 complete abstracts/identities; selected original2013 RAG text is superseded by the verified corrected2017 paper and must not be the evidence anchor. Other search hits are leads only.
- `root-neuronal-tetramer-primary-web.json`: original Wiley10.1002/jnr.22407 complete abstract. This does not prove a postsynaptic location; its abstract describes nuclear colocalization.
- `root-key-primary-identities-web.json`: official PubMed20623620 identity and complete abstract; official29038163 correction/republication relationship; official39607926 identity (PubMed abstract truncates) and selected PMC Results/Discussion, not a full paper or supplement audit. The independently identified2025 two-array study is a lead, not required new evidence yet.

## Mechanistic points to preserve

The principal activity is sequence-specific transcriptional regulation, with strong direct human erythroid promoter repression evidence. PMID29606353 identifies the TGACCA recognition motif and distal HBG promoter occupancy using biochemical and cellular assays. The earlier19153051 abstract reports a different proximal GGCCGG site. Preserve both original curation records; do not silently rewrite the earlier evidence or label the entire DNA-binding assertion false. The newer direct promoter mechanism should anchor the biological core.

PMID16704730 supports XL nuclear-matrix partition and BCL6-associated nuclear paraspeckles, as well as interactions among isoforms. UniProt records five products, including Q9H165-8 named isoform7/XS. Do not assume numbering is consecutive. S can reside predominantly in cytoplasm in the absence of L/XL and enter nuclear bodies upon their interaction. PMID27453576 and11161790 are needed for the human localization/variant context.

Reactome9700131 is not a random wrong-gene citation: its full summary explicitly contains a BCL11A(1–219)-ALK fusion. Its cytosol assertion cannot simply establish a native full-length BCL11A location. Keep the exact TAS source and distinguish the fusion context. Reactome9934021/9934024 concern BAF assemblies; SMARCA4 supplies ATPase chemistry. PMID23644491 reports BCL11A/B as stable BAF subunits. Do not assign BCL11A an ATPase function.

PMID39607926 identifies ZnF0-dependent tetramer formation and links it to steady-state protein production and repression. Selected original PMC discussion proposes ZnF1 degron shielding as a model. Do not turn proposed co-translational details into demonstrated facts. Detailed human assays and NuRD engagement still require bounded Methods/Results inspection after normal cache acquisition.

PMID20534004 reports glutamate/NMDA effects and Bcl11A-L/DCC-mediated restriction of neurite arborization in cultured hippocampal neurons (PubMed MeSH identifies rats). This is neuronal transcriptional context, not glutamate receptor activity. PMID20623620 identifies CASK interaction with L and S in COS cells/brain and nuclear neuronal colocalization, with perturbation of axon outgrowth. Preserve the species and isoform distinctions and do not infer a postsynaptic location merely from the CASK partner.

PMID18681895 describes interaction with UBC9, SUMO1 recruitment, nuclear-body formation and BCL11A sumoylation. It suggests participation in conjugation organization; the abstract does not demonstrate BCL11A SUMO E3 catalysis. Inspect the original experiment before deciding the inherited protein-sumoylation assertion. Substrate status alone is insufficient, but recruitment of the conjugation machinery may be a distinct mechanistic role.

Official PubMed29038163 explicitly records correction/republication of23438597 after image duplication in the original. Use the corrected record under its own identifier for contextual RAG activation. Do not use the retracted2013 search result as standalone support, and do not conclude BCL11A is exclusively a repressor in all cell types.

## Source acquisition

One normal batch started (actual0bedfe, session84143) for11161790,18681895,20534004,20623620,27453576,29038163,39423807,39607926. Exact command: `env UV_CACHE_DIR=/private/tmp/clingen-uv-cache UV_TOOL_DIR=/private/tmp/clingen-uv-tools UV_TOOL_BIN_DIR=/private/tmp/clingen-uv-bin UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1 just fetch-pmid 11161790 18681895 20534004 20623620 27453576 29038163 39423807 39607926`. At writing, its outcome is pending. No repeated normal command or remote recovery is claimed.

No new quoted supporting snippets or annotation decisions have been authored here.

The single eight-PMID normal operation completed with DNS failure, exit1 and cached0/8 (actual428af9). Actuald732fa was the sole intermediate poll; actual0bedfe was the start. All eight targets remain absent. The raw envelope filenames retain `poll2` for the terminal observation; no retry was performed. A separate fixed remote recovery is reserved as Source97 after Source96.


## Canonical seed and focused primary reading

Seed47 primary and all four absent normal publications were imported unchanged; three pre-existing Reactome caches were identical and preserved. Root read all 32 canonical source assertions in actual1f9fb8. No source-object or isoform changes are proposed.

Actuala71584 reads the complete first BAF-subunit Results section of PMID23644491 and selected affinity-purification, nuclear-extract and sedimentation Methods. Human T-cell evidence supports stable BAF membership; mouse proteomic discovery is distinguished from the human follow-up. No ATPase role is assigned to BCL11A.

Actual94acfa reads the unique PMID29606353 Results paragraphs covering domain rescue, DNA recognition/affinity, motif variants, CUT&RUN mapping, globin occupancy and promoter editing. XL, but not L, rescues repression in the tested mouse erythroleukemia system. Human HUDEP-2 and primary CD34-positive cell experiments establish distal promoter binding. The paper's statement that ZnF0 appears dispensable in its deletion/rescue assay must be considered alongside the newer tetramer study; construct and assay differences remain to be assessed before resolving that mechanistic comparison. No image/supplement audit was performed.

Actual3d5f9c reads selected PMID16704730 Results and figure captions on human isoform expression, fractionation, interactions, engineered reporter assays, nuclear paraspeckles and S-form relocalization. Forced nuclear entry through a GAL4 fusion is distinguished from native S localization. No whole-paper or figure-image claim is made.

The GO-CAM index has no BCL11A/Q9H165 match (actual0e0a6c). The official AmiGO definition and hierarchy of GO0000981 were checked in the saved transcription-term-web observation. The broader transcription-factor assertion is refined to RNA polymerase II specificity, retaining both regulatory directions. No NEW assertion is proposed.

A single Falcon attempt failed before a provider request because the offline environment could not resolve deep-research-client[cyberian]0.2.7rc1 (actualb5ce89). No provider report was produced or fabricated; these are manual notes.

The eight supplemental normal PMID records remain pending Source97. Their official identities and explicit abstract read limits are recorded separately. The corrected republished PMID29038163 replaces the retracted 2013 version; the original version is not used as standalone evidence. This draft needs source-cache reconciliation, a focused review of remaining sumoylation/postsynapse uncertainties, independent scientific peer review, validation, rendering and history before canonical application.


## Independent review precision correction

The S-isoform cytoplasmic and nuclear-body redistribution statements now name GFP-BCL11A-S, Gal4DBD-fused XL/L, and COS7 cells. The experiment does not establish the same redistribution for untagged endogenous isoforms. This correction changes no source object, action, core, product or quotation. Eight supplemental normal reference records still require reconciliation before finalization.


## Normal Source97 reference reconciliation

The eight supplemental normal records have now been recovered from the verified Source97 archive. Their exact cached titles and availability are reconciled in the review. The five records for PMIDs 11161790, 18681895, 20534004, 20623620 and 29038163 contain complete abstracts but no full text. The other three records, PMIDs 27453576, 39423807 and 39607926, contain XML-derived full text. Presence of a PMCID alone does not establish that full text was recovered; corrected PMID29038163 remains abstract-only.

The independent science lane read all five abstract-only records in full (actual54fab2). For PMID27453576, it read the complete abstract, selected construct/cellular-assay Methods and the complete missense-function Results subsection (actual9b6877). Tagged L/S localization and BRET experiments and GAL4-fused L reporter activation are kept in their HEK293/construct context. For PMID39423807, it read the complete abstract, the DNA-complex, ZnF6-affinity and mouse-globin Results, complete Discussion and matching protein/binding/mouse Methods (actual2a1356). ZnF6 supplies backbone contacts and additional binding affinity; the mouse experiments have a stated developmental-stage limitation for the human YAC comparison. For PMID39607926, it read the complete abstract, Results and Discussion text (actual6bd8f9). Stable engineered monomers can bind DNA yet fail to silence fetal globin effectively, while tetramerization supports NuRD engagement. Degron shielding and cotranslational assembly remain models. These reads do not comprise every Methods/dynamics section, any figure-image inspection, or a supplement audit.

No new annotation, action or core-function change follows from these normal records. SUMO-pathway participation remains unresolved because recruitment could differ mechanistically from being a SUMO substrate and the complete original experiment is unavailable. Postsynaptic localization remains unresolved because the CASK abstract instead documents nuclear neuronal colocalization and the original rat donor experiment was not recovered. Contextual RAG activation relies on the corrected republished article under its own identifier. The preceding construct correction specifying GFP-S, Gal4DBD-XL/L and COS7 is preserved. The 32 source objects, five products, 19 ACCEPT / 10 KEEP_AS_NON_CORE / 1 MODIFY / 2 UNDECIDED decisions, one core function and existing 15-word PMID29606353 quotation are unchanged; no new quotations were added.

This addendum supersedes the historical pending-reference statements above. Canonical application remains conditional on independent review and exclusive import of all eight normal source files with byte equality to the verified archive. Source files were only copied to TMP during this reconciliation.


## Final validation and source import

All eight Source97 normal reference records were imported with exact archive-byte equality and no overwrites (import dc6cef; postverification 2e39d3). The review and notes were then applied after the whole-gene peer, construct correction, and independent normal-reference reconciliation.

`just validate human BCL11A` passed (d80260). Its single advisory is missing structured propagation metadata on the existing IBA general transcription-factor annotation refined to the RNA polymerase II-specific term (row 4). The biological refinement is documented; the ancestral node and its sources were not inspected, so no propagation history is invented to silence this advisory. The 32 source objects and five products remain unchanged.

Rendering passed (b766e4), and the generated history record passed `just validate-history` (29ee13). The embedded review YAML is checked against the final source before publication. This is focused validation; no repository-wide validation pass is claimed.
