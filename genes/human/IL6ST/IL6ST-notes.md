# IL6ST notes

Deep research with Falcon/Perplexity-lite was unavailable in the shared runtime, so this review was assembled from `just fetch-gene` output, cached publications, Reactome entries, UniProt P40189, PANTHER and GO-CAM 5f46c3b700002685.

- IL6ST/gp130 is the shared signal-transducing beta receptor for IL-6-family cytokines. In IL-6 signaling, two IL-6:IL6R complexes recruit two gp130 molecules into the 2:2:2 hexameric complex [PMID:12829785 "hexameric, interlocking assembly mediated by a total of 10 symmetry-related, thermodynamically coupled interfaces"].
- gp130 forms homodimeric IL-6 and IL-11 receptor complexes and heterodimeric complexes with LIFR or OSMR for CNTF, LIF and OSM family signaling; the shared core function is cytokine receptor activity at the plasma membrane, not ligand cytokine activity.
- Human IL11RA requires gp130 for IL-11 signaling [PMID:8637716 "absolute requirement of gp130 for signalling"], and OSM can signal through LIFR:gp130 or OSMR:gp130 receptor complexes [PMID:8999038 "a heterodimer of gp130 and OSMRbeta"].
- The soluble gp130 isoform binds IL-6:soluble-IL6R complexes and antagonizes trans-signaling, but this is a receptor-decoy activity, not `GO:0005125` cytokine activity.
- PANTHER propagation to IL6ST is broadly sound for gp130-family receptor activities and signaling pathways; the weak rows are interaction terms such as `ciliary neurotrophic factor receptor binding` where the corresponding receptor-activity term captures the biology better.

## GO-CAM 5f46c3b700002685

- The model correctly places gp130/IL6ST at the plasma membrane downstream of extracellular IL-6:soluble-IL6R and upstream of JAK1.
- `GO:0015026` coreceptor activity is a defensible generic GOA term for papers that assayed gp130 recruitment by a ligand-binding alpha chain or partner receptor, but it underspecifies gp130 in this trans-signaling GO-CAM. IL6ST is the signal-transducing cytokine receptor chain for the membrane complex; the final GO-CAM consistency PR should keep the activity but ask whether `GO:0004896` cytokine receptor activity or an IL-6/gp130-family descendant is the better type.
- The model activity had already flagged PMID:12433365 on the gp130 `has_input` edge to JAK1 and PMID:21990364 on the gp130-to-JAK1 causal edge as weak/misattached for those edge claims.
