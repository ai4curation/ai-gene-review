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
- REMOVE: LCN2 and MEOX2 protein binding (policy).
- NEW: ubiquitin-like ligase-substrate adaptor activity (IMP, PMID:34285210), the core MF.

## 2026-10-05 bounded HuRI policy follow-up

This appendix supersedes only the earlier decision to remove the LCN2 and MEOX2 protein-binding rows solely for genericity. The [explicit ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/500686f1/projects/CLINGEN_MENDELIAN.md#L2976-L2978) retains supported, biologically correct generic binding as KEEP_AS_NON_CORE when a more specific molecular function is not established. It is a documented user-directed exception to the general annotation-reviewer informational-exclusion rule.

Both source assertions remain unchanged: PMID:32296183 IPI, with P80188 (LCN2) and Q6FHY5 (MEOX2), respectively. The exact reviewed Q8WXI3 UniProt interaction entries list these partners with NbExp=3. That is corroborating curated interaction metadata, not proof of three independent physiological replications. The complete cached HuRI abstract and the selected generation/results paragraph were read: human ORF yeast two-hybrid screening was followed by pairwise retesting and sequence confirmation, with study-level benchmarking and orthogonal validation. The exact ASB10 supplementary target rows, assay orientation, expression controls and pair-specific orthogonal tests were not independently inspected. The two short YAML quotations describe the overall protocol, not a separately verified ASB10 target experiment.

LCN2 binding does not by itself identify a ubiquitination substrate or receptor activity. MEOX2 binding likewise does not establish ubiquitination, DNA binding or transcriptional regulation by ASB10. No evidence-backed more specific ASB10 molecular function is assigned to either edge. These two reports are retained as non-core associations through the preserved experimental curation, exact UniProt corroboration and inspected assay methodology, with those access limits explicit.

The other fifteen decisions, three historical NEW proposals, three alternative products, all twenty-two references, description and core function are preserved from merged PR #4214. Their original scientific judgments and existing quotations are not newly independently approved by this bounded follow-up. The old notes remain an exact prefix. The missing HTML artifact is addressed by the repository's normal renderer; DRAFT reflects the observed validation advisories, not a new unresolved decision. No additional NEW assertion, source-cache replacement, provider report or history record is authored here. A standard EDIT record and canonical rendering belong to the accepted canonical application.
