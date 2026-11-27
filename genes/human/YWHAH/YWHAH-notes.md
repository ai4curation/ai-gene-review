# YWHAH review notes

Manual deep research note: Perplexity was unavailable through the cached
`deep-research-client`, which reported only the `claude_code` provider. This
branch was asked not to spawn extra workers on the 2-CPU host, so no
provider-authored `YWHAH-deep-research-perplexity.md` file was created. The
review instead uses the cached GOA publications, the UniProt entry, PAINT,
PANTHER, Reactome records, and the merged YWHAB/YWHAE/YWHAZ 14-3-3 reviews as
manual research inputs.

YWHAH encodes 14-3-3 eta, one of the soluble 14-3-3 phosphoprotein adaptors.
The UniProt entry records the conserved client-binding role and identifies a
directly assayed PDPK1-inhibition branch [PMID:12177059], plus literature for
phosphorylated nuclear-receptor cofactors, GAB2, KCNK18, DAPK2, PI4KB/TBC1D22
and MEFV interactions. The GOA rows add cardiac-channel, synaptic and
glucocorticoid-specific contexts that need to be kept separate from the core
phosphoprotein-binding mechanism.

The seeded GOA file is dominated by bare `GO:0005515 protein binding` IPI rows.
Those are reviewed one row at a time, retaining the `WITH/FROM` interactor on
each row, but the action follows the project protein-binding policy: physical
interaction with a client is not by itself an informative GO molecular
function for a 14-3-3 adaptor.
