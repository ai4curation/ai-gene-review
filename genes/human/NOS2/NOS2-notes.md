# NOS2 review notes

Seed: NOS2, a reviewed human Swiss-Prot nitric-oxide synthase in PANTHER
PTHR43410.

`just deep-research-claude-code human NOS1` failed before a NOS1 provider file
could be written because the only configured deep-research provider in this
runtime was not logged in. The same provider/session limitation applied to the
NOS family, so no provider-style deep-research file was created for NOS2. The
review used the fetched UniProt record, GOA-seeded publication caches, Reactome
records, the cached PTHR43410 family review, and
`interpro/panther/PTHR43410/PTHR43410-paint.tsv`.

`just paint-losses human NOS2` reported that P35228 is not a leaf of the cached
PTHR43410 tree and therefore losses could not be checked at the leaf level; no
IRD or IKR loss was reported for the NOS2 lineage.

Main curation decisions:

- Keep the NOS catalytic core and cofactor-binding rows as core functions.
- Keep inflammatory and antimicrobial process rows where human iNOS makes NO in
  macrophage, mucosal, hepatocyte or chondrocyte contexts, but keep local OA
  cartilage cytokine/prostaglandin effects and peroxisome-localization claims as
  non-core.
- Treat the PANTHER plasma-membrane IBA and the Reactome nucleoplasm row as
  over-extended from eNOS/nNOS or from a NOS2 gene-expression event rather than
  a durable NOS2 protein compartment.
- Remove every bare `GO:0005515` interaction row while preserving the distinct
  SPSB, HSP90 and GAPDH `WITH/FROM` entities.
