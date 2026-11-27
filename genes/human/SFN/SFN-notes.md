# SFN review notes

Manual deep research note: Perplexity was unavailable through the cached
`deep-research-client`, which reported only the `claude_code` provider. This
branch was asked not to spawn extra workers on the 2-CPU host, so no
provider-authored `SFN-deep-research-perplexity.md` file was created. The
review instead uses the cached GOA publications, the UniProt entry, PAINT,
PANTHER, Reactome records, and the merged YWHAB/YWHAE/YWHAZ 14-3-3 reviews as
manual research inputs.

SFN encodes 14-3-3 sigma, the epithelial-enriched member of the conserved
14-3-3 phosphoprotein-binding adaptor family. Like the other isoforms it forms
dimers and uses a conserved amphipathic groove to bind phosphorylated Ser/Thr
motifs in client proteins. Its best supported distinctive human branches are
epithelial and keratinocyte functions, including PKP3/desmosome control
[PMID:24124604], DAPK2, LRRK2 and other phosphorylated clients, GBP1 cytosolic
retention in innate immunity [PMID:37797010], and p53-associated G2/M
checkpoint biology [PMID:9659898].

The seeded GOA file is dominated by bare `GO:0005515 protein binding` IPI rows.
Those are reviewed one row at a time, retaining the `WITH/FROM` interactor on
each row, but the action follows the project protein-binding policy: physical
interaction with a client is not by itself an informative GO molecular
function for a 14-3-3 adaptor.
