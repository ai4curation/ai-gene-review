# GET3 notes

Falcon deep research supports GET3 as the central ATPase of the yeast GET pathway: "Functionally, ATP hydrolysis is required for productive insertion because a hydrolysis-deficient Get3 mutant remains substrate-bound and is inactive in insertion assays" [file:yeast/GET3/GET3-deep-research-falcon.md].

The canonical mechanism is a cytosolic homodimeric targeting cycle: "Get3 is described as a **Zn2+-stabilized homodimer** whose dimer interface forms a **composite hydrophobic groove**" that binds the tail-anchor TMD [file:yeast/GET3/GET3-deep-research-falcon.md].

Falcon distinguishes the core GET pathway from secondary roles. Stress-induced holdase/chaperone activity is real but non-core: "under oxidative stress or ATP depletion, Get3 is converted from ATPase targeting factor into an **ATP-independent holdase chaperone**" [file:yeast/GET3/GET3-deep-research-falcon.md].

The Falcon report did not find direct support for Erd2/HDEL-mediated Golgi-to-ER retrograde transport as a primary GET3 function, so the corresponding GOA rows should stay non-core [file:yeast/GET3/GET3-deep-research-falcon.md].

## 2026-10-01 current GOA and IBA refresh

`just fetch-gene yeast GET3 --force` refreshed GET3 from 64 saved source rows to 73 current GOA rows, adding 18 current assertions and leaving nine old exact-source rows absent from current GOA. The missing old rows are preserved with `retired: true`.

All three current IBA rows trace to two nodes in the cached `interpro/panther/PTHR10803/PTHR10803-paint.tsv` export. `PANTHER:PTN000085951` supports conserved Get3/TRC40 ATP hydrolysis activity, and `PANTHER:PTN000085952` supports eukaryotic GET-complex membership and tail-anchored membrane protein insertion into the ER. Budding-yeast GET3 appears as a seed on these nodes, which is direct experimental grounding for the PAINT placement rather than circular evidence.

The 2026-10-01 current GOA refresh added mostly split generic `GO:0005515 protein binding` rows against GET pathway interactors and tail-anchored clients from existing GET-pathway publications. Those rows were reviewed as `REMOVE`, and the older generic protein-binding rows were also migrated from the legacy `MARK_AS_OVER_ANNOTATED` action to `REMOVE`; the physical interactions are real, but the naked parent term does not identify a distinct molecular function.

The obsolete `GO:0051082 unfolded protein binding` row from the oxidative-stress paper is no longer present in GOA and is retained as retired provenance with `MODIFY` to the live `GO:0044183 protein folding chaperone` row now present in GOA. That is still an interim approximation: the UNFOLDED_PROTEIN_BINDING project needs a general holdase chaperone term for this in-situ stress state because `GO:0140309 unfolded protein holdase activity` is a carrier-holdase term for escort to a specified destination or acceptor.

I searched for 2024-2026 GET3/YDL100C papers. A 2025 study showed that the soluble GET pre-targeting proteins and Get3 assemble into glucose-starvation-induced, chaperone-rich cytosolic GET bodies, and that the structures are resolved by NADH [PMID:39976550, "Our data reveal that the pre-targeting complex components, Sgt2 and the Get4-Get5 heterodimer, and the Get3 ATPase play important roles in the assembly of these structures in Saccharomyces cerevisiae"]. This supports a stress-state redistribution of the existing GET machinery, not a change to the core ATP-dependent tail-anchored protein insertion annotation set.
