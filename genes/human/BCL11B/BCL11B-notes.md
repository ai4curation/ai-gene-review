# BCL11B review notes

BCL11B is a nuclear sequence-specific transcriptional regulator. It can activate transcription in stimulated T cells and recruit repressive chromatin partners in another context. Stable SWI/SNF membership is supported in human T-cell extracts, but this does not imply every BCL11B pool is a BAF subunit or that BCL11B itself is a remodeling ATPase.

The proposal retains all 26 source assertions and both normal alternative products. It accepts 15 annotations, refines five molecular functions, retains two migration processes as non-core, and leaves four assertions undecided. No NEW annotation is proposed. Source qualifiers and supporting entities are unchanged.

## Mechanism and contextual evidence

- [PMID:16809611](https://pubmed.ncbi.nlm.nih.gov/16809611/) supports promoter recognition and IL2 activation. The abstract and selected original Figure 5/Discussion text distinguish recombinant DNA-binding assays, human Jurkat experiments and primary CD4+ T cells. Activation context matters; this is not a claim that all BCL11B targets are activated.
- [PMID:17245431](https://pubmed.ncbi.nlm.nih.gov/17245431/) supports HDAC1/2 and SUV39H1 binding. Selected captions distinguish transfected HEK293T complex assays from microglial promoter experiments. These are partner-binding activities; catalysis belongs to the recruited enzymes. Direct PMC access was challenged, so only the abstract, selected indexed Results and PubMed captions were inspected.
- [PMID:23644491](https://pubmed.ncbi.nlm.nih.gov/23644491/) includes mouse discovery experiments and human T-cell biochemical validation. Selected Results support stable BCL11B association with SWI/SNF. Subtype distributions and other cellular contexts remain qualified.
- [PMID:27959755](https://pubmed.ncbi.nlm.nih.gov/27959755/) links human progenitor chemokine responsiveness to developmental positioning in zebrafish. The normal text reports "increased migration of these progenitors" after BCL11B knockdown. The N441K variant reduces binding at known sites and gains a new site; describing it simply as a null would lose that distinction. The paper reports a p300-association assay, so that citation is not dismissed as a wrong-paper attribution.

## Evidence limits and unresolved assertions

PMID:23752268 explicitly names BCL11B among HDAC1 interactions in human CEM T cells. Its exact HDAC2 supplementary entry was not recovered. The two PMID:33961781 BioPlex pairs were also not independently resolved. Those three source-specific rows remain UNDECIDED, despite the separate mechanistic evidence for HDAC association. This is an access limitation, not evidence that the interactions are false.

PMID:28473536 supplies a curated sequence-specific double-stranded-DNA-binding assertion. Its abstract covers 542 human transcription factors; no individual BCL11B motif or methylation-preference claim is inferred. The underlying activity is independently supported by IL2 promoter experiments.

The transferred neuron-projection location is unresolved: neuronal developmental effects do not by themselves locate BCL11B protein in an axon or dendrite. The mouse donor localization experiment was not retrieved. The IBA ancestral placements were not reconstructed, and neither donor count nor target-self WITH/FROM is treated as a flaw.

Reactome R-HSA-9934021 is a mouse neural-progenitor BAF summary; R-HSA-9934024 includes either BCL11A or BCL11B and preserves uncertain subtype distribution. Their nucleoplasm assertions are corroborated by human nuclear evidence, not presented as new direct localization experiments.

## Reading and provenance

The reviewer read all 26 staged source objects, the normal UniProt identity/function/interaction/localization/alternative-product sections, all seven cited cached abstracts, both complete Reactome summaries, selected normal XML Results/Methods paragraphs for 27959755, selected Results/Discussion for 23644491 and Discussion for 23752268. Selected original 16809611 Figure 5/Discussion and 17245431 Results/captions were read from saved primary records and an independent PubMed retrieval. Figures as images, supplements and complete-paper audits were not performed. Normal caches and the two alternative products were preserved.

The normal 16809611 and 17245431 caches are abstract-only. Existing 23752268, 28473536 and 33961781 canonical records retain their original metadata/body form. No imported auxiliary byte is used to overwrite an existing source. Additional staged XML for the latter two studies was not needed for this proposal.

This is a temporary proposal pending independent whole-gene science review and the parent's ordinary research-provider outcome. No provider-named research file was authored. Focused canonical validation, rendering, history and publication follow only after the review/import prerequisites are closed.


## Completion update — 2026-10-01 UTC

The independent whole-gene science peer passed this proposal. The reviewed YAML is applied unchanged after exact primary and auxiliary source imports. The earlier proposal-status paragraph is retained as historical context and is superseded by this completion update.

The ordinary Falcon attempt and its perplexity-lite fallback both stopped during dependency resolution: deep-research-client[cyberian]==0.2.7rc1 could not be resolved. Neither research provider started, and no provider report was produced. Manual review therefore rests on the bounded primary-source reading documented above; it does not claim a complete-paper, supplementary-data or independent provider review. The four source-specific uncertainties remain UNDECIDED. All 26 source assertions and both normal alternative products are preserved; no NEW annotation is added.


Focused canonical validation, HTML rendering and append-only history validation passed. The rendered page embeds the exact reviewed YAML. No focused validation warnings were reported; no global validation pass is claimed. Normal UniProt, GOA and all nine reference caches remain byte-identical to the pre-application snapshot.


## 2026-10-01: HDAC-binding refinement, repression mechanism and SWI/SNF membership

BCL11B has both activating and repressive regulatory roles. Direct recognition of the IL2 regulatory site supports the existing DNA-binding transcription-factor activity, whereas the HIV-1 promoter study describes a different recruitment mechanism. Its selected Results and Discussion place CTIP2 at the viral promoter through Sp1, where it recruits HDAC1/2 and SUV39H1-containing machinery, “leading to HIV-1 silencing” [PMID:17245431](https://pubmed.ncbi.nlm.nih.gov/17245431/). The abstract's description of DNA-bound CTIP2 must therefore not be read as a direct DNA-binding assay at this promoter. This distinction is now explicit in the description, broad transcription-factor reason and core summary.

The three previously UNDECIDED HDAC rows are refined to GO:0042826 histone deacetylase binding: PMID:23752268 with HDAC2 and PMID:33961781 with HDAC1 or HDAC2. The original IPI assertions specify these partner identities, and independently read PMID:17245431 experiments substantiate association with both enzymes. The term describes the supported binding partner class, not HDAC chemistry performed by BCL11B. The precise HDAC2 supplementary entry from the CEM interactome and the two BioPlex pairs and cell assignments have still not been inspected. Those provenance limits remain in the row reasons and references; they no longer prevent a functional refinement supported by independent experiments. No purified binary HDAC interaction is claimed. The current decisions supersede the three historical pending-HDAC decisions above, which remain intact in this append-only journal.

The existing SWI/SNF membership is now represented by in_complex: GO:0016514 in the core function. Selected primary Results describe human T-cell co-sedimentation, urea stability and reciprocal immunoprecipitation after mouse discovery experiments [PMID:23644491](https://pubmed.ncbi.nlm.nih.gov/23644491/). This supports a stable complex-associated BCL11B pool; it does not assign remodeling ATPase activity, universal occupancy of every BCL11B pool, or SWI/SNF identity to the distinct viral-promoter repressive assembly. The existing eight-word SWI/SNF evidence excerpt was relocated from the annotation row to the core without increasing its source quotation budget.

No NEW annotation is added. GO:0001227 requires DNA-binding repressor activity; the inspected HIV-1 experiment supports Sp1-recruited corepression instead. GO:0003714 describes such transcription-factor-bound corepressor activity, but a separate addition is left as a specific curation question pending its source/comparator/nonredundancy assessment, rather than being substituted automatically for the requested term. Repression itself is not disputed or omitted. A proposed NEW GO:0000122 process would also be a descendant of the already represented GO:0006357 transcription-regulation process; this bounded follow-up does not add a redundant process. No comparator-based gap or completed NEW gate is claimed. The local GO-CAM index had no BCL11B/Q9C0K0 match; this absence is not treated as evidence for a new term.

The remaining neuron-projection annotation stays UNDECIDED because its ortholog localization experiment remains unavailable. All 26 source assertion objects, both alternative products, qualifiers, references and supporting entities are retained. Proposed totals are 15 ACCEPT, 8 MODIFY, 2 KEEP_AS_NON_CORE and 1 UNDECIDED. Procedural PAINT caveats and source-handling commentary were removed from selected reasons where the biology provides a shorter justification; no evolutionary placement was newly inferred.

Follow-up reading was bounded to the current complete review and notes, PMID:17245431 cached abstract and selected indexed primary Results/Discussion, PMID:23644491 cached abstract and selected Results/Discussion and cell-extract methods, PMID:23752268 Discussion, UniProt function/interaction/localization sections, and official GO definitions for the considered terms. No supplementary pair tables, figure images or whole-paper audit is claimed. The normal caches remain unchanged and the research-provider failure is not retried. Existing quote budgets are retained, with four additional words from PMID:17245431 (20 cumulative); PMID:23644491 remains at 8, PMID:16809611 at 14 and PMID:27959755 at 5. This is a TMP follow-up proposal pending independent science review; no canonical application or new history is claimed yet.


Independent science peer d8846e (ROOT) accepted this follow-up after checking all 26 source assertions, both alternative products, the selected primary experiments and the quotation inventory. Three HDAC associations are refined using independent mechanistic evidence while the original supplementary-pair limitations remain explicit. No NEW assertion was added. The reviewed proposal was applied exactly; focused canonical validation, rendering and generated history validation are recorded below when complete.


Focused canonical validation completed successfully (8f9d58; zero annotation warnings), followed by rendering (4cbd71), generated Codex EDIT history (ca9284), and history validation (1b010a). These checks close the pending application tasks above. The validation log contains the existing Python pkg_resources deprecation notice, which is a tooling notice rather than an annotation warning. All normal source files and prior history remained unchanged; no full-repository validation was run.
