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
- Treat bactericidal NO production as a NOS2 core output: human alveolar
  macrophages inoculated with Mycobacterium bovis BCG upregulated iNOS and lost
  killing activity after L-arginine-pathway inhibition [PMID:9284131], and
  enterohemorrhagic Escherichia coli modulated IFN-gamma-induced human enterocyte
  NOS2/iNOS expression and NO production [PMID:18390757].
- Keep the Leishmania major IgE immune-complex paper as a protozoan/macrophage
  iNOS context but not as support for bacterial defense or Fc-gamma receptor
  signaling [PMID:7544003].
- A second review pass kept `GO:0045776 negative regulation of blood pressure`
  as a non-core NOS-family vascular-tone output instead of a bad-PAINT call, and
  changed the `PMID:7544003` Fc-gamma receptor/phagocytosis row to REMOVE with a
  `WRONG_TERM` source defect because that paper describes IgE immune complexes
  and CD23 rather than Fc-gamma receptor signaling.
- Added a `NEW` `GO:0008270 zinc ion binding` row for the conserved NOS2
  Zn(2+) site annotated in the UniProt feature table.
