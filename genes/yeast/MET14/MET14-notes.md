# MET14 (YKL001C, Q02196) notes

Evidence journal (UniProt and cached publications).

- APS kinase EC 2.7.1.25 [UniProt:Q02196 "FUNCTION: Catalyzes the synthesis of activated sulfate."]; P-loop ATP site 31-38, phosphoserine intermediate at S105 (by similarity).
- Enzyme purified from S. cerevisiae [PMID:3019265 "Adenylylsulphate kinase (EC 2.7.1.25, ATP:adenylylsulphate 3'-phosphotransferase) has been isolated from Escherichia coli and from Saccharomyces cerevisiae."]; activated by thiols/thioredoxin [PMID:3019265 "Preincubation of the isolated enzyme from either source in the presence of thioredoxin plus DTT, reduced glutathione or DTT increased the activity significantly."].
- Genetic requirement [PMID:197388; PMID:1101032].
- Cdc14 co-purification in the KPI network [PMID:20489023]: protein-binding row REMOVED as uninformative. A possible phosphatase-substrate link is untested.


## 2026-10-26 complete fungal-member reassessment

Reassessed all 24 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

APS kinase transfers phosphate from ATP to APS, producing PAPS. PMID:1654509 identifies the MET14 structural gene; PMID:3019265 reports purified kinase behavior and thiol-dependent activation. ATP is an actual substrate, so its binding is core rather than peripheral. Thiol activation does not establish thioredoxin as an obligatory electron donor to this phosphorylation step. The true broad sulfur-amino-acid metabolic claim is refined to the already supported biosynthetic term. PMID:22234534 engineering effects on glutathione production are pathway-flux effects, not evidence that this kinase catalyzes glutathione peptide assembly.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids yeast MET14` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-yeast-MET14-*.log`.
