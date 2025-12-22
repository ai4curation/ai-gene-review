---
description: Review, either de-novo, or augment the review of an existing one. A list of deep research providers may be specified.
argument-hint: [ORGANISM] [GENE_SYMBOL] ( using [DEEP_RESEARCH_PROVIDER] )
---

Review the gene specified in $ARGUMENTS.

* ORGANISM should typically be a uniprot species code (in a few cases we use lowercase GO names)
* GENE_SYMBOL should be the human readable gene symbol for that org

IMPORTANT: you MUST consult the annotation-reviewer.md subagent for this task.

If the user specifies a deep research provider(s), make sure to perform deep research using at
least this provider(s), otherwise default to falcon.

E.g. `just deep-research-falcon ORGANISM GENE_SYMBOL`
