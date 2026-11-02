# MET3 (YJR010W, P08536) notes

Evidence journal (UniProt and cached publications).

- ATP sulfurylase EC 2.7.7.4; first step of sulfate assimilation [UniProt:P08536 "FUNCTION: Catalyzes the first intracellular reaction of sulfate"].
- Recombinant enzyme active [PMID:10092498 "The specific activity of the purified enzyme was estimated to 140 U/mg."]. Gel filtration suggested an octamer (PMID:10092498); UniProt (crystal structures PMID:11157739, PMID:14983089) gives a homohexamer, with a C-terminal APS-kinase-like domain that is inactive and used for oligomerization [UniProt:P08536 "DOMAIN: The oligomerization domain is distantly related to APS kinases,"].
- Genetic requirement for sulfate assimilation [PMID:197388; PMID:1101032].
- Mitochondrion HDA (2 proteomes): non-core, probably co-purification.
- MET3 overexpression lowered GSH, whereas MET14/MET16 overexpression raised it [PMID:22234534 "The intracellular GSH content of MET14 and MET16 over-expressing strains increased up to 1.2 and 1.4-fold higher than that of the parental strain, respectively, whereas those of APA1 and MET3 over-expressing strains decreased."].


## 2026-10-26 complete fungal-member reassessment

Reassessed all 25 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

ATP sulfurylase makes APS and pyrophosphate from sulfate and ATP; it does not perform the separate APS-kinase step. PMID:11157739 full text directly resolves a hexamer (two stacked rings); PMID:10092498 earlier solution mass suggested an octamer. The description preserves that experimental distinction. The kinase-like C-terminal region supports oligomerization and lacks the separate kinase activity. Broad sulfur metabolism and sulfur-amino-acid metabolism rows are refined to supported biosynthetic descendants, without denying their original biological truth. Upstream sulfate activation performs work in the multistep hydrogen-sulfide biosynthetic route. Native methionine auxotrophy and peripheral expression/localization assertions were reviewed with their original sources; general early genetic abstracts (PMID:1101032, PMID:197388) are not treated as detailed proofs of every named gene-step mapping.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids yeast MET3` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-yeast-MET3-*.log`.
