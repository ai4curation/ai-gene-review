# ATG12 evidence re-review

## 2026-09-21 full-gene review

All 55 original annotation objects, including the contributes_to qualifier, preserved. No NEW assertions added. PTHR13385 exact human leaf PTN002491519 descends from root PTN000333039; all challenged IBDs actually occur on this path. No target-specific loss is inferred from missing yeast junction components or from a general rather than cargo-receptor role.

PMN: full PMID:18701704 Fig2A explicitly tests ATG12 deletion and says ATG3/4/5/7/10/12/16 are required for GFP-Osh1 degradation. Current GO:0034727 is “Degradation of a cell nucleus by microautophagy.” Human route remains UNDECIDED and will reuse the queued ATG2A report. Glycophagy: exact fly Q9VTU1 IMP PMID:24265594 verified; full FigureS1 explicitly tests Atg12 RNAi in glycogen-rich muscle autophagosome formation. ATG12 contributes membrane-lipidation machinery, so it need not recognize glycogen to participate. Retained inherited NONCORE, with queued WIPI2 report to be cross-checked.

Full PMID:23202584 and PMID:24191030 abstract establish the ATG12 ATG3-binding surface and complex ligase role; full PMID:24954904 Fig1J shows endogenous ATG12 on GFP-LC3-negative/positive forming autophagosomes. Live GO:0034045 is obsolete and explicitly recommends existing PMID:7770114 phagophore membrane: obsolete proposal removed and four review replacements updated without touching original IDs. Broad cytoplasm/cytosol/membrane/complex/autophagy terms restored as core.

Full PMID:20723759 identifies ATG12–ATG3 and multiple potential substrates: its constructs use mouse ATG12 in human cells/mouse fibroblasts, with endogenous mouse conjugate confirmation. This refutes an exclusive single-substrate biological summary but is not a direct assay of every human sequence. PMID:22152474 abstract additionally reports unconjugated ATG12 BH3-like binding; retained as context only, without adding a new apoptosis assertion.

Full PMID:22342342 Fig7C shows ATG12 conjugation is required for TECPR1 PtdIns3P binding, supporting active maturation cofactor work. Full PMID:17709747 Fig2E tests ATG12 in HEK293 antiviral reporters with conjugation-deficient controls. Full PMID:19666601/S4 instead demonstrates incoming HCV IRES translation dependence and does not itself measure suppressed antiviral signaling. Existing immune claims retained with the independent appropriate source.

The two Reactome phagosome-location rows actually cite mitophagic autophagosome events, not LAP. Independent full PMID:19339495 Fig1D detects endogenous ATG12–ATG5 in purified RAW264.7 mouse phagosomes with ER/cytosolic marker controls; human Henle407 knockdown is a separate assay. Retain the contextual conserved location without mislabeling mouse fractionation as human.

Generic protein-binding OVER calls migrated to REMOVE for lack of functional information (not false interactions), or MODIFY protein-tag activity where the cited experiment measures conjugation. The 12 source records remain intact. No generic binding interaction is used to invent a new catalytic role.

Validation compatibility: live GO:7770114 exists and is used in the four review replacements, but the local dynamic core-location ontology predates it. Core synthesis uses its valid broader physical structure GO:0061908 phagophore; no source identifier is rewritten to fit the cache.


## Recovery review consistency follow-up (2026-09-22)

Restored readable identifiers in manual prose. Where applicable, reconciled AP3M2 reference notes with the retained contextual claim, removed unrelated PIK3C3 support from unresolved projections, separated PIK3C3 aspect-specific reasons, and documented the surviving/renamed ATG14 membrane term. Source assertion fields and verbatim quotations are unchanged.
