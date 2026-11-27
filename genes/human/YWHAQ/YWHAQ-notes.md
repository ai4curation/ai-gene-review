# YWHAQ review notes

Manual deep research note: Perplexity was unavailable through the cached
`deep-research-client`, which reported only the `claude_code` provider. This
branch was asked not to spawn extra workers on the 2-CPU host, so no
provider-authored `YWHAQ-deep-research-perplexity.md` file was created. The
review instead uses the cached GOA publications, the UniProt entry, PAINT,
PANTHER, Reactome records, and the merged YWHAB/YWHAE/YWHAZ 14-3-3 reviews as
manual research inputs.

YWHAQ encodes 14-3-3 theta/tau, a conserved dimeric 14-3-3 adaptor. UniProt
records the same phosphoserine/phosphothreonine client-recognition mechanism
as for the rest of the family and names direct interactions with RGS7, PDPK1,
DAPK2, PI4KB/TBC1D22 proteins, INAVA, MARK kinases and MEFV. The seeded GOA
file also carries Reactome BAD, GLUT4, PKN and TP53 pathway contexts shared
across 14-3-3 isoforms.

The seeded GOA file is dominated by bare `GO:0005515 protein binding` IPI rows.
Those are reviewed one row at a time, retaining the `WITH/FROM` interactor on
each row, but the action follows the project protein-binding policy: physical
interaction with a client is not by itself an informative GO molecular
function for a 14-3-3 adaptor.
