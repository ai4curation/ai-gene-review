# ACSF3 manual research notes

## 2026-11-15 — initial curation

Human ACSF3 (HGNC:27288; UniProt Q4G176) was seeded with the native fetch command. All 32 native annotation contexts, including reference IDs and partner identifiers, are retained. No NEW annotations are proposed. Falcon authentication and fallback Perplexity quota failures prevented a provider report; the following is manual primary-source research, not provider-generated deep research.

### Biochemistry and the older fatty-acid assignment

[PMID:21846720, Mammalian ACSF3 protein is a malonyl-CoA synthetase](https://pubmed.ncbi.nlm.nih.gov/21846720/) reports purified human enzyme specificity: "No detectable activity was found with other dicarboxylic acids (oxalate or succinate) or with the fatty acids (butyrate, octanoate, laurate, palmitate, oleate, or lignocerate)." Malonate is the preferred substrate; methylmalonate is also activated. ATP, CoA and magnesium are required. The paper directly revisits the earlier COS-1 whole-cell-lysate assay in PMID:17762044 and considers the reported C24 activation likely indirect. This is positive contrary evidence, not an inference from an absent abstract sentence. The four VLCFA/long-chain-CoA native assignments are removed. The broad fatty-acid metabolism and CoA-ligase terms remain biologically sound but are TOO_GENERAL beside existing specific annotations.

[PMID:21841779, Exome sequencing identifies ACSF3 as a cause of combined malonic and methylmalonic aciduria](https://pubmed.ncbi.nlm.nih.gov/21841779/) demonstrates malonate and methylmalonate activation with purified GST-tagged ACSF3, mitochondrial localization in human fibroblasts, and correction of the abnormal patient-cell metabolic phenotype by ACSF3 complementation. The variable clinical spectrum is not used to manufacture additional GO functions.

[PMID:21642549, Malonyl-CoA synthetase, encoded by ACYL ACTIVATING ENZYME13](https://pmc.ncbi.nlm.nih.gov/articles/PMC3160029/) has a plant-focused abstract but directly tests recombinant human ACSF3. The recovered full text states: "The recombinant human ACSF3 protein indeed had malonyl-CoA synthetase activity as determined by the coupled-enzyme spectrophotometric assay as well as by our HPLC-based assay." The Results heading is "AAE13 Is the Founding Member of a Novel Phylogenetic Clade of the Eukaryotic AAE Superfamily"; see Supplemental Figure 1. Human catalytic activity supports the native molecular-function and malonate-entry-step annotations. Arabidopsis growth/toxicity phenotypes are not human experiments.

The first native fetch of PMID:21642549 was abstract-only; a second native fetch to a staging directory recovered full text. The original 2,582-byte source (SHA256 2a4c1a5c0bb510ddb03b7394704421197d40d90c53e31e503f9f97a9d81c0c9e) was preserved in Git blob 3f71e3a695ff21164045e345360cf6953c98fe4c and recovery ref refs/recovery/clingen-acsf3-20261115/pmid21642549-abstract-v1 before replacement. The native full-text source is 57,546 bytes, SHA256 192bf8a1c0456cece1213a7f56d024adc1e118a7ce917c6a24ff07933a3b655c. No publication text was manually edited.

### Physiological role and limits of the mtFAS model

[PMID:28479296, The Mammalian Malonyl-CoA Synthetase ACSF3 Is Required for Mitochondrial Protein Malonylation and Metabolic Efficiency](https://pmc.ncbi.nlm.nih.gov/articles/PMC5482780/) provides human HEK293T knockout/rescue evidence. Malonate accumulates about fivefold, and ACSF3 re-expression rescues mitochondrial lysine malonylation. Total-cell malonyl-CoA is not a compartment-specific measurement. This supports malonyl-CoA donor production; it does not demonstrate protein malonyltransferase activity. DLAT/DLST lipoylation remains detectable without ACSF3.

The 2011 HEK293T knockdown experiment in PMID:21846720 reduced malonate-derived acyl-ACP synthesis in isolated mitochondria. It supports a catalytic contribution to mtFAS, not sole or universal necessity. [PMID:28986507](https://pubmed.ncbi.nlm.nih.gov/28986507/) reports strong combined effects of ACSF3 knockdown and mitochondrial ACC1 disruption on lipoylation; its accepted manuscript was inspected at https://oulurepo.oulu.fi/bitstream/10024/21907/1/nbnfi-fe2017112855099.pdf, while the native cache remains abstract-only. Lipoylation is an indirect pathway endpoint.

[PMID:42874924](https://pubmed.ncbi.nlm.nih.gov/42874924/) is a 2026 mouse knockout study supporting metabolic editing of malonate/methylmalonate and redundant malonyl-CoA generation. Only the abstract was accessible; no uninspected full-text assay details are asserted. [PMID:42239141](https://pmc.ncbi.nlm.nih.gov/articles/PMC13228397/) is a 2026 PREPRINT using rodent cells and reports ACSF3-independent malonate entry into mtFAS. Its status and species limit extrapolation. The combined evidence warrants retaining context-dependent human mtFAS contribution while avoiding essential/sole-source claims. No NEW protein-malonylation, lipoylation or broad metabolic-regulatory process term is asserted from perturbation necessity.

### Compartment and phylogenetic evidence

Primary human microscopy and fractionation establish mitochondria, not a precise submitochondrial compartment. The native matrix TAS statement was separately verified at https://reactome.org/content/detail/R-HSA-5696007 and catalyst entity https://reactome.org/content/detail/R-HSA-5696011, which identifies human Q4G176 in mitochondrial matrix. This verifies curated provenance; it is not a new matrix-localization experiment. The cached reaction summary omits this field, and its older VLCFA chemistry is adjudicated separately.

PTHR43201 metadata and native PAINT assertions were inspected without trusting machine-generated family descriptions as evidence. The retained family topology does not resolve native PTN001185560, PTN000644304 and PTN001186584 placements. Human target-level functions are experimentally supported; clade-wide scope remains unresolved. The human protein appearing among its own IBA sources is legitimate descendant evidence, not circularity or an evidential defect. No GO-CAM index match for ACSF3/Q4G176 was present in the pinned base.

### Pair-specific interaction audit

All ten native protein-binding rows have positive pair-specific evidence and are retained as KEEP_AS_NON_CORE under the project policy. The indexed UniProt interaction lines are additional corroboration. IntAct experiment records establish the cited assay contexts; AP-MS/co-IP association does not prove direct molecular contact, and heterologous assays do not establish endogenous colocalization or a core regulatory role. Raw spectra and figure images were not reanalysed.

The bounded [IntAct PSICQUIC Q4G176 query](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/id%3AQ4G176?format=tab27&firstResult=0&maxResults=200) returned 80 records (536,142 bytes; SHA256 6e89f624e321d48823b43e75019a0c5ee37df15a9dbe5129ec0cbca039d242c2). Twenty-two exact PMID/partner-matched records cover native rows 1–9. All matching records were non-negative. Responses were parsed in memory; no complete API snapshot was retained.

| Native row | PMID | Partner | Verified experiment or deposited edge |
|---|---|---|---|
| 1 | 23864651 | GLP1R (UniProtKB:P43220) | intact:EBI-61301910 / imex:IM-30241-1; intact:EBI-61302616 / imex:IM-30241-103; intact:EBI-63256753 / imex:IM-30241-191; intact:EBI-63256049 / imex:IM-30241-163 |
| 2 | 28514442 | KCTD14 (UniProtKB:Q9BQ13) | intact:EBI-21889149 / imex:IM-25778-9429 |
| 3 | 32296183 | MATN4 isoform 2 (UniProtKB:O95460-2) | intact:EBI-23191824 / imex:IM-25472-48342; intact:EBI-23416956 / imex:IM-25472-61077; intact:EBI-24516600 / imex:IM-25472-134066 |
| 4 | 32296183 | TRIM27 (UniProtKB:P14373) | intact:EBI-22375563 / imex:IM-25472-3551; intact:EBI-22833268 / imex:IM-25472-28550; intact:EBI-24312907 / imex:IM-25472-114333 |
| 5 | 32296183 | RAB28 (UniProtKB:P51157) | intact:EBI-23882173 / imex:IM-25472-86623; intact:EBI-24783436 / imex:IM-25472-157781; intact:EBI-24173628 / imex:IM-25472-104890 |
| 6 | 32296183 | KRT40 (UniProtKB:Q6A162) | intact:EBI-22404344 / imex:IM-25472-5115; intact:EBI-22861732 / imex:IM-25472-30102; intact:EBI-24330525 / imex:IM-25472-115885 |
| 7 | 32296183 | PPP1R13B (UniProtKB:Q96KQ4) | intact:EBI-24846255 / imex:IM-25472-11620; intact:EBI-22979582 / imex:IM-25472-36544; intact:EBI-24387740 / imex:IM-25472-122325 |
| 8 | 33961781 | LONP1 (UniProtKB:P36776) | intact:EBI-54768061 / imex:IM-29278-13129 |
| 9 | 33961781 | KCTD14 (UniProtKB:Q9BQ13) | intact:EBI-54790054 / imex:IM-29278-15787 |
| 10 | 40205054 | LONP1 (UniProtKB:P36776) | NDEx 95bc75d5-d1d1-11ee-8a40-005056ae23aa; edge 629534; ACSF3 bait → LONP1 |

For native row 10, PMID:40205054 Data Availability identifies the [U2OS AP-MS NDEx network](https://www.ndexbio.org/viewer/networks/95bc75d5-d1d1-11ee-8a40-005056ae23aa). The read-only interconnect query `searchString=ACSF3 LONP1`, `searchDepth=1`, `edgeLimit=20`, `save=false` returned exactly two nodes and one edge. Nodes 629532 (ACSF3) and 553338 (LONP1) are linked by edge 629534, with ACSF3 marked as bait. The 7,982-byte response had SHA256 290ad37b8f1720fe8cc77c5e72bfe6ff105e8df61d3c95c709b8deea7c1c51bc. No per-edge AP-MS score was supplied by the subnetwork. The current IntAct response lacked this PMID context, so the primary deposited data supplied its verification.

### Validation and outstanding scientific questions

The 32 native contexts and immutable UniProt/GOA hashes are checked against the original seed inventory. Schema, terms, references, every supporting-text occurrence and history will be checked before delivery. Biological uncertainties retained in the review concern substrate flux partitioning and assay-specific interaction significance; complete annotation assessment does not imply every upstream image, raw spectrum or phylogenetic node was inspected.

### PAINT loss check and final synthesis

The project lineage-loss helper was used in cache-only mode. PTHR43201.json.gz was absent, so its lineage result is UNCHECKABLE_MISSING_TREE. The retained IBD.gaf (SHA256 0c672914e10c1f79d3fb365077d843a92e518eb6eee2aac00c67150274adf569) contains the three positive native IBD records. No target-lineage absence of IRD/IKR losses can be inferred without topology. No tree download or cache replacement was attempted.

Final synthesis uses one core catalytic unit: malonyl-CoA synthetase activity initiating malonate clearance in the mitochondrial matrix. The matrix description is explicitly present in the introduction of PMID:28479296 and in the inspected Reactome entity; neither is presented as a newly inspected matrix-localization experiment. Context-dependent mtFAS contribution remains in the description and native annotations. No direct malonyltransferase or new process assertion is introduced. All 32 native rows are assessed: 16 ACCEPT, 10 KEEP_AS_NON_CORE, 2 TOO_GENERAL, and 4 REMOVE. COMPLETE denotes completion of annotation assessment, with the source and topology limitations above retained.

### Local validation results

`just validate human ACSF3` passed schema, authored term and best-practice checks. Its ten generic protein-binding warnings are retained deliberately under the project-specific policy: all ten assay contexts are verified and retained as non-core, with no supported mechanistic replacement. The reference validator checked 53 snippets and 14 titles with no issues (11 snippets skipped by that validator); the separate canonical walker checked all 77 supporting-text occurrences with zero unchecked or failing quotes. Native history validation and canonical in-memory rendering passed. The source-impact audit searched all 54,338 tracked YAML/YML files at the pinned base and found no pre-existing references or affected quote contexts for the nine new cache files. The original abstract-only PMID21642549 remains recoverable and is contained in the recovered full-text source.

### Independent scientific follow-up

The final action distribution supersedes the earlier draft counts above: **17 ACCEPT, 10 KEEP_AS_NON_CORE, 1 TOO_GENERAL and 4 REMOVE**. CoA-ligase activity is retained as ACCEPT because it identifies an informative catalytic class; the more specific malonate activity does not erase that information. The generic PAINT node does not establish substrate specificity across its broad scope, so its native row is not mechanically refined. This follows the maintainer ruling in CLAUDE.md on 2026-11-14. Fatty-acid metabolism remains TOO_GENERAL because the direction is unspecified.

The overturned 2007 finding now explicitly names the superseded catalytic claim rather than the historically true existence of the COS-1 experiment. The BioPlex reference assessment now records completed KCTD14 verification through IntAct EBI-21889149 / IM-25778-9429. Native identities, source bytes and all 77 quotations are unchanged.

### Repository review follow-up (PR #6404, review 5911562865)

Five structured source defects now record the confirmed legacy assertions: one FlyBase-assigned human experimental GO row, the UniProt Q4G176 RHEA:33639 catalytic association, two Reactome-derived GO rows, and the obsolete UniProt CC:FUNCTION preference sentence on the cited UniProt file reference. The Rhea reaction definition and whole Reactome pathways are not proposed for deletion. The historical indirect-assay interpretation is recorded as cause OTHER; a hedge-to-assertion causal chain was not demonstrated. All defects are NOT_REPORTED; no upstream report was submitted. Sources themselves remain unchanged.

The three fatty-acid biosynthetic process rows are now consistently KEEP_AS_NON_CORE. Their observed human catalytic contribution remains supported, while the central core remains malonate clearance and the physiological mtFAS contribution is context dependent. This supersedes earlier action counts: **14 ACCEPT, 13 KEEP_AS_NON_CORE, 1 TOO_GENERAL and 4 REMOVE**, all 32 native contexts preserved, no NEW annotations.

A suggested question records methylmalonate-specific GO coverage without guessing an identifier or declaring that no suitable ontology term exists. PMID21642549 supplies an independent full-text reassessment of the original COS-1 interpretation, strengthening the removal and finding-review evidence. The UniProt transit peptide is explicitly labelled predicted (ECO:0000255), not experimental matrix proof. The uninspected PMID34800366 supplementary row is recorded as UNVERIFIED, and selected binding rationales clarify the unresolved endogenous compartment.

The canonical quote checker verified 112 supporting-text occurrences after these changes, with zero unchecked or failing quotations.
