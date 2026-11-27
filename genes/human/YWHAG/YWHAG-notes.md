# YWHAG review notes

Manual deep research note: Perplexity was unavailable through the cached
`deep-research-client`, which reported only the `claude_code` provider. This
branch was asked not to spawn extra workers on the 2-CPU host, so no
provider-authored `YWHAG-deep-research-perplexity.md` file was created. The
review instead uses the cached GOA publications, the UniProt entry, PAINT,
PANTHER, Reactome records, and the merged YWHAB/YWHAE/YWHAZ 14-3-3 reviews as
manual research inputs.

YWHAG encodes 14-3-3 gamma, a ubiquitous dimeric adaptor that binds
phosphoserine- and phosphothreonine-bearing client proteins. UniProt summarizes
the conserved function as client binding with consequent modulation of client
activity, and names several human branches with direct evidence: WDR24/GATOR2
regulation [PMID:36732624], BEST1-dependent glutamate secretion [PMID:29121962],
PKP1/desmosome regulation [PMID:29678907], ABL1 and MDM4 retention or
modulation [PMID:15696159, PMID:16511572], and the mitochondrial
protein-quality-control branch reported in PMID:22532927.

The seeded GOA file is dominated by bare `GO:0005515 protein binding` IPI rows.
Those are reviewed one row at a time, retaining the `WITH/FROM` interactor on
each row, but the action follows the project protein-binding policy: physical
interaction with a client is not by itself an informative GO molecular
function for a 14-3-3 adaptor.

The IEA vesicle, synapse and presynapse rows are Ensembl ortholog projections
from rat Ywhag, not direct human YWHAG measurements; the review treats them as
peripheral or over-annotated client-context locations because cached human YWHAG
evidence establishes a soluble cytosolic 14-3-3 adaptor with inducible
mitochondrial-matrix recruitment but not a core vesicle or synaptic site.
