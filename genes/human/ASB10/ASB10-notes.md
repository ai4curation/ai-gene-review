# ASB10 review notes

## Sources
- Affinage: trust gates clear.
- Key papers:
  - PMID:34285210 (full text): ASB10 ubiquitylates TEM8 in breast cancer cells.
  - PMID:22156576 (full text): eye localization; outflow facility; glaucoma variants.
  - PMID:23901248 (full text): trabecular meshwork degradation machinery.
  - PMID:40399264 (full text): mouse heart; HSP70 stabilization.
- 5 Reactome cytosol rows from CRL5 neddylation/CAND1/CSN reactions. The cached summaries do not name ASB10; each row's summary names its own reaction.

## Decisions
- ACCEPT: nucleus, cytoplasm and cytosol (IDA, IEA, TAS).
- MARK_AS_OVER_ANNOTATED: intracellular signal transduction (InterPro SOCS-box IEA).
- KEEP_AS_NON_CORE: protein ubiquitination (broad UniPathway IEA).
- KEEP_AS_NON_CORE: LCN2 and MEOX2 protein binding (explicit ClinGen campaign binding instruction; see appendix).
- NEW: ubiquitin-like ligase-substrate adaptor activity (IMP, PMID:34285210), the core MF.

## 2026-10-05 bounded HuRI policy follow-up

This appendix supersedes only the earlier decision to remove the LCN2 and MEOX2 protein-binding rows solely for genericity. The [explicit ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/500686f1/projects/CLINGEN_MENDELIAN.md#L2976-L2978) retains supported, biologically correct generic binding as KEEP_AS_NON_CORE when a more specific molecular function is not established. It is a documented user-directed exception to the general annotation-reviewer informational-exclusion rule.

Both source assertions remain unchanged: PMID:32296183 IPI, with P80188 (LCN2) and Q6FHY5 (MEOX2), respectively. The exact reviewed Q8WXI3 UniProt interaction entries list these same IntAct-derived partner edges with NbExp=3. That is pair-specific curated interaction metadata, not an independent source or proof of three independent physiological replications. The complete cached HuRI abstract and the selected generation/results paragraph were read: human ORF yeast two-hybrid screening was followed by pairwise retesting and sequence confirmation, with study-level benchmarking and orthogonal validation. The exact ASB10 supplementary target rows, assay orientation, expression controls and pair-specific orthogonal tests were not independently inspected. The two PMID:32296183 YAML quotations describe the overall protocol; the two UniProt quotations name the specific LCN2 and MEOX2 edges.

LCN2 binding does not by itself identify a ubiquitination substrate or receptor activity. MEOX2 binding likewise does not establish ubiquitination, DNA binding or transcriptional regulation by ASB10. The official [GO:0008134 definition](https://flybase.org/cgi-bin/cvreport.pl?cvterm=GO%3A0008134&rel=is_a) describes binding a transcription factor; it does not require ASB10 itself to regulate transcription. MEOX2 identity therefore makes the optional partner-class refinement plausible, but it is deferred because the exact assayed construct and pair-specific controls remain uninspected, not because those controls are known to be absent. No evidence-backed more specific ASB10 molecular function is assigned to either edge. These two reports are retained as non-core associations through the preserved experimental curation, exact UniProt interaction lines and inspected assay methodology, with those access limits explicit.

The other fifteen decisions, three historical NEW proposals, three alternative products, all twenty-two references, description and core function are preserved from merged PR #4214. Their original scientific judgments and existing quotations are not newly independently approved by this bounded follow-up. The normal repository status is DRAFT: [the status calculation](https://github.com/ai4curation/ai-gene-review/blob/4703f04cb40e6d24b0d6d775189642015de83c8b/src/ai_gene_review/status_manager.py#L70-L77) maps any validation warning to DRAFT. The three advisories are the two retained generic-binding rows and the pre-existing unused Affinage report; none represents a new unresolved annotation decision. This supersedes the earlier COMPLETE wording, while the published history remains unchanged. A legacy COMPLETE example does not override the current status algorithm. No additional NEW assertion, source-cache replacement or provider report is authored here.
