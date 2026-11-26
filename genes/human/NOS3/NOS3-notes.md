# NOS3 review notes

Seed: NOS3, a reviewed human Swiss-Prot nitric-oxide synthase in PANTHER
PTHR43410.

`just deep-research-claude-code human NOS1` failed before a NOS1 provider file
could be written because the only configured deep-research provider in this
runtime was not logged in. The same provider/session limitation applied to the
NOS family, so no provider-style deep-research file was created for NOS3. The
review used the fetched UniProt record, GOA-seeded publication caches, Reactome
records, the cached PTHR43410 family review, and
`interpro/panther/PTHR43410/PTHR43410-paint.tsv`.

`just paint-losses human NOS3` reported that P29474 is not a leaf of the cached
PTHR43410 tree and therefore losses could not be checked at the leaf level; no
IRD or IKR loss was reported for the NOS3 lineage.

Main curation decisions:

- Keep nitric-oxide synthase activity, the L-arginine-to-NO process and all
  catalytic cofactor-binding rows as the NOS3 core.
- Keep Golgi, Golgi-membrane, caveola and plasma-membrane rows because eNOS
  lipidation and trafficking place its main endothelial activity at these
  compartments.
- Keep vasodilation, blood-pressure, angiogenesis and aortic-valve rows as
  eNOS-specific vascular signaling, but keep developmental and endothelial-cell
  migration rows non-core where they reflect one tissue context or downstream NO
  signaling.
- Mark uncoupled superoxide production as over-annotated rather than a normal
  evolved NOS3 activity, and remove every bare `GO:0005515` row under the
  project protein-binding policy while preserving each high-throughput
  interaction row separately.
