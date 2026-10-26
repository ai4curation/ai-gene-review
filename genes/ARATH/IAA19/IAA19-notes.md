# IAA19 research notes

## Nuclear auxin repressor audit (2026-10-26)

PMID:14729917 directly establishes IAA19/MSG2 interaction with ARF7, a 65% reduction in auxin induction of IAA19 in nph4/arf7, and the contextual feedback model. PMID:22096563 uses ARF C-terminal-domain split luciferase and co-immunoprecipitation; its ARF4/5 versus ARF1/6/9 signal differences are not universal endogenous affinities. PMID:17675404 finds IAA19–MYB77 binding in vitro but not in four BiFC tests, while the ARF7–IAA19 nuclear BiFC positive control supports nuclear location. PMID:19719484 directly measures altered stamen-filament growth kinetics in dominant msg2-1. Feedback for IAA19 is not automatically assigned to every Aux/IAA paralog.

All 99 baseline rows were assessed, with original term/evidence/reference/partner fields and flags preserved. Bare GO:0005515 removal follows the explicit repository exception: it does not deny the measured interaction. Each affected reason identifies its original source, partner and assay context. Independently grounded functional ARF/SCF interactions are refined; homotypic binding is retained as non-core. Neither receptor-dependent degradation nor a loss-of-function phenotype alone licenses a new protein-catabolic-process annotation on an Aux/IAA substrate. No new rows were added in this audit.

The prior cis-regulatory-binding rejection inferred an unproved ARF bridge in a yeast one-hybrid screen. Normal publisher supplement retrieval found IAA12/AT1G04550 → AT5G12870 (MYB46 promoter), SupplementaryTable2 Sheet1 row445, with one of LacZ/HIS reporters activated. Table5 confirms the AUX-IAA clone. The Methods state: [PMID:25533953 "the screen was repeated to confirm the results and each clone was sequenced to reconfirm identity"]. This supports retaining non-core promoter association, with no claim that every Aux/IAA is an autonomous DNA-binding transcription factor. PAINT inheritance is respected; no node defect or lineage-specific loss is inferred from a missing canonical DNA-binding domain.

Provider provenance: parent ran actual Falcon and Perplexity-lite attempts; both authentication/provider attempts failed. Logs are .cache/module-audit-logs/auxin-fetch/ARATH-IAA19-provider.log. No provider report was fabricated. Normal gene-publication caching succeeded. Primary sources, not provider prose or GOA rows, support the decisions. CrY2H-seq correction PMID:36690743 changes the first author surname, not the interaction data. The detailed row-by-row audit is generated under IAA19-source-analysis/annotation-audit.yaml.

Final actions: ACCEPT=3, KEEP_AS_NON_CORE=4, MODIFY=14, REMOVE=78.

Original source distribution:

- GO_REF:0000002: 1 rows.
- GO_REF:0000033: 4 rows.
- GO_REF:0000120: 1 rows.
- GO_REF:0000122: 1 rows.
- PMID:11118137: 1 rows.
- PMID:12036262: 1 rows.
- PMID:14729917: 4 rows.
- PMID:17675404: 1 rows.
- PMID:19719484: 1 rows.
- PMID:21734647: 21 rows.
- PMID:22096563: 4 rows.
- PMID:24362628: 1 rows.
- PMID:28650476: 22 rows.
- PMID:32612234: 35 rows.
- PMID:9342315: 1 rows.
