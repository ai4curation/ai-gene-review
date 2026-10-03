# BRSK2 review notes

## 2026-10-03 — initial annotation assessment

BRSK2 (Q8IWQ3; HGNC:11405; NCBI Gene:9024), also called SAD-A, was reviewed from its normal imported UniProt/GOA seed and cached primary literature. The candidate preserves all 48 source annotation objects, all 17 reference identities/titles (10 PMID and seven GO_REF), and all six recorded alternative products. There are 50 raw GOA rows: two pairs differ only in curator/date metadata and were already collapsed by the normal seeder. The source has no negated or isoform-specific annotation rows. No raw source, existing publication cache, family export or provider-generated file was edited.

The candidate has 19 ACCEPT, 20 KEEP_AS_NON_CORE and nine UNDECIDED decisions, no REMOVE, MODIFY or NEW, and one molecular-function core. Status is DRAFT: the supported COPS5 protein-binding row produces an expected normal policy warning. DRAFT does not mean the 48 rows are unassessed; UNDECIDED explicitly records the remaining evidence limits.

### Research and access

The normal PMID command passed with all 10 PMIDs already cached. The first normal deep-research launcher failed while resolving its client, before any provider ran. The documented installed-client override then used the installed 0.2.7rc1 client for one falcon attempt with perplexity-lite fallback; both failed, with a DNS failure reported. No provider output was produced and no manually authored file is represented as a provider result. These notes and the candidate are manual curation, not a synthetic research report.

| Source | Material actually read and usable boundary |
| --- | --- |
| [PMID:14976552](https://pubmed.ncbi.nlm.nih.gov/14976552/) | Complete cached abstract. It explicitly includes human BRSK2 among LKB1-activated kinases. Full PMC access failed; isolated magnesium/ATP-binding measurements were not inspected. |
| [PMID:18268107](https://pubmed.ncbi.nlm.nih.gov/18268107/) | Cached Results, Methods, relevant figure captions and discussion. SAD A/B double-knockout mouse hippocampal neurons lose normal polarized microtubule organization. Rat experiments and mouse SAD double-knockout experiments are distinguished. The combined knockout does not isolate BRSK2, and presynaptic clustering is background attributed to earlier work. |
| [PMID:21985311](https://pubmed.ncbi.nlm.nih.gov/21985311/) | Complete cached abstract. BRSK1/2 are directly included in the tau S262/S356 kinase comparison. MARK1/SIK cellular inhibitor findings are not generalized to BRSK2. The abstract does not identify every construct's species. |
| [PMID:22609399](https://pubmed.ncbi.nlm.nih.gov/22609399/) | Complete cached abstract reports COPS5/Jab1 interaction by GST pull-down and immunoprecipitation plus perinuclear colocalization. BRSK2 is the substrate of stimulated ubiquitin-dependent turnover. |
| [PMID:22669945](https://pubmed.ncbi.nlm.nih.gov/22669945/) | Complete cached abstract explicitly reports SAD-A binding and phosphorylation of PAK1 Thr423, secretion effects and MIN6 cytoskeletal remodeling. Full PMC access failed; finer construct details were not inspected. |
| [PMID:22713462](https://pubmed.ncbi.nlm.nih.gov/22713462/) | Complete abstract and official corrigendum listing. BRSK2 depletion enhances ER-stress apoptosis; both wild-type and kinase-dead overexpression are protective. The full original paper and the content of the 2012 BBRC 426(4):667 correction were not recovered. No claim that the correction is trivial, nor that the paper is invalid, is made. |
| [PMID:23029325](https://pubmed.ncbi.nlm.nih.gov/23029325/) | Cached Methods/Results and localization/cell-cycle evidence. Mitotic centrosomal localization is distinguished from interphase. A static G2/M fraction cannot resolve entry, exit or arrest flux. Cdc25C phosphorylation is described as unpublished/submitted work and is not treated as an assay established in this paper. |
| [PMID:23907667](https://pubmed.ncbi.nlm.nih.gov/23907667/) | Complete cached abstract plus publisher preview. VCP interaction and increased CD3-delta after BRSK2 depletion are explicit. Full relevant microscopy, ATP-hydrolysis and extraction/retrotranslocation assays were inaccessible. |
| [PMID:28386764](https://pubmed.ncbi.nlm.nih.gov/28386764/) | Relevant cached tau review and kinase table; treated as secondary evidence, with primary corroboration from PMID:21985311. |
| [PMID:36931259](https://pubmed.ncbi.nlm.nih.gov/36931259/) | Complete cached abstract of the human 14-3-3 study. The target-specific BRSK2–YWHAE matrix/result was not inspected. UniProt lists the interaction, but this does not substitute for reading its assay. |

The `full_text_available` cache flag and the sections actually inspected are distinct. Failure to obtain complete experiments is recorded per assertion; a title focused on another family member is not treated as proof of curator error.

### Molecular mechanism and core synthesis

BRSK2 has the UniProt-supported N-terminal protein kinase domain, UBA region and KA1 domain architecture. LKB1 activation and direct downstream phosphorylation distinguish its own catalytic work from the separate fact that LKB1 phosphorylates BRSK2. Tau kinase activity, ATP binding and magnesium use are aspects of the same kinase mechanism, not independent duplicated cores. The single GO:0004674 protein serine/threonine kinase core connects to established neuronal polarity, with the SAD A/B double-knockout attribution limit explicit. No intrinsic ATPase, ubiquitin ligase, protease or degradation-catalyst activity is inferred.

The PAK1/insulin-secretion, cell-cycle and VCP/ERAD observations remain context-specific non-core biology. The secretion term is direction-neutral: the UniProt record also records a distinct inhibitory CDK16-associated context, and one beta-cell stimulation experiment does not establish uniform stimulation across phosphorylation states or isoforms. The six source products are retained without assigning untested functions to individual isoforms.

### Propagation, ontology and unresolved assertions

The actual cached `PTHR24346-paint.tsv` records were joined for the five IBA rows. GO:0007409, GO:0030010 and GO:0050321 are placed at PTN000679673; centrosome is at PTN001217017, and G2/M transition at PTN008613667. The full ancestral tree/MSA was not independently reconstructed. Human BRSK2 occurring in its own descendant list is legitimate experimental grounding, not circular evidence; the number of donors is not used as a strength score. The conserved core/context decisions follow the biological evidence rather than mechanically discounting IBA.

Official records identify Q69Z98 as mouse Brsk2 and D3ZML2 as rat BRSK2. The specific distal-axon transfer remains UNDECIDED because neuronal function alone cannot establish that precise location and the donor assay was not inspected. By contrast, the [official GO:0090176 definition/parents](https://amigo.geneontology.org/amigo/term/GO%3A0090176) place that assertion in planar polarity, a more restrictive scope than the axon-dendrite polarity experiments inspected; the exact donor experiment remains unresolved. [GO:0060590](https://amigo.geneontology.org/amigo/term/GO%3A0060590) requires ATP-hydrolysis modulation, which VCP binding and ERAD substrate abundance alone do not establish.

GOA labels GO:1904152 obsolete, whereas the local March 2026 ontology and an indexed official June 2026 record retain its older definition. Direct current access did not establish replacement metadata. Preserve the machine-sourced ID and label; do not invent a replacement. Its biological retrotranslocation assertion is independently uncertain because extraction was not separated from other ERAD steps in the accessible abstract.

The apoptosis row is UNDECIDED rather than reversed: the abstract supports protection and does not establish a kinase-dependent apoptotic execution step, but the full experimental scope and correction remain unavailable. The two vesicle-clustering rows remain UNDECIDED. An additional uncached [PMID:16630837 abstract](https://pubmed.ncbi.nlm.nih.gov/16630837/) emphasizes SAD-B; this is a retrieval limit and reason to trace the exact chain, not proof that BRSK2 was never tested. No new publication cache or annotation was manufactured from that lookup. No GO-CAM index entry was found for Q8IWQ3/BRSK2 in the inspected local index.

### Binding policy and provenance

The COPS5 interaction is retained as non-core under the user's explicit ClinGen task instruction, documented in the [current project curation instructions](https://github.com/ai4curation/ai-gene-review/blob/main/projects/CLINGEN_MENDELIAN.md#curation-instructions). This is an intentional task-specific departure from informational exclusion of generic binding; it does not change repository-wide policy or imply maintainer sign-off. The YWHAE row is UNDECIDED because its relevant experiment was not inspected, not because generic binding is forbidden.

Codex `/root/bloc_followup` authored the integrated assessment; `/root/bloc_followup/brca1_late_binding` supplied a disclosed 16-row cell-cycle/ER consultation. ROOT's distinct whole-gene science peer is pending. The candidate's two seven-word core quotations are exact cached substrings; reference and row supports otherwise use reference-only citations, avoiding repeated quotations. Normal focused candidate schema, best-practices, reference and ontology validation passed with one expected generic-binding warning. Canonical authored YAML/notes, render and history have not yet been applied.

## 2026-10-03 — canonical application

ROOT completed the distinct whole-science peer of all 48 decisions, 17 references, six products and the single core. The exact reviewed YAML and notes were applied after checking source preimages. Normal canonical validation passed with one expected supported-generic-binding warning, and the standard codex/gpt-6 CREATE history was scaffolded and validated. Status remains DRAFT with nine UNDECIDED assertions; no uncertainty was converted into evidence of absence. The prior candidate-stage statements above record the earlier stage. Raw source records, cached publications and previous histories were preserved. No provider output, remote publication or external maintainer approval is claimed by this application.

## 2026-10-03 — structured neuronal-process coverage

The single kinase core now explicitly lists axonogenesis (GO:0007409) and regulation of axonogenesis (GO:0050770), matching the existing ACCEPT decisions and their conserved SAD-kinase interpretation. Establishment of cell polarity remains a separate process link. The [official axonogenesis entry](https://amigo.geneontology.org/amigo/term/GO:0007409) describes axon formation; it does not subsume polarity establishment. The [official regulation entry](https://amigo.geneontology.org/amigo/term/GO:0050770) has a regulates relation to axonogenesis and an is_a relation to regulation of neuron projection development (GO:0010975). The broader regulation term is therefore covered by the specific regulatory link and is not repeated as another core process.

This is alignment of the structured synthesis with already reviewed source assertions, not a new annotation or a second catalytic core. The retained core description and evidence explicitly limit the mouse loss experiments to combined SAD A/B deficiency; no exclusive human BRSK2 effect, new direction of regulation, or direct phosphorylation of a new substrate is inferred. All 48 annotation objects and decisions, 17 reference records, six products, two short quotations and nine explicit uncertainties are unchanged. Existing sources and earlier histories are preserved.

The focused core-process correction passed independent scientific review and normal canonical validation with one expected generic-binding warning. The page was regenerated and a standard EDIT history record was validated. Biological status remains DRAFT.
