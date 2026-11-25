# Alpha PutA review handoff

Two COMPLETE reviews; all 20 ordered original annotation payloads and four raw source hashes preserved. No NEW annotations; no source/publication/provider files rewritten. Manifest includes the four pristine seed raw files for integration alongside ten authored/rendered/history files.

Actions: {'MARK_AS_OVER_ANNOTATED': 4, 'ACCEPT': 11, 'MODIFY': 2, 'KEEP_AS_NON_CORE': 1, 'REMOVE': 2}

Both focused gene validations, both history validations and both renders passed. Each gene has one stale local-ontology label advisory: current QuickGO GO:0003842 explicitly says NAD+, matching the source payload and authored core. No ontology cache changes were made by this worker. Default Falcon requests each failed HTTP403, with original failure logs retained and no fabricated provider output.

Identity: PDB3HAZ equals GH + full999-aa Q89E26; PDB5KF6 equals SM + full1233-aa F7X6I3. SIFTS independently maps each at reference coverage1.0. These are exact sequence bridges for purified recombinant proteins, not native strain physiology assays. SINMM is SM11 and must not be replaced by P95629/RHIML.

Chemistry: retain quinone-coupled PRODH and NAD+-dependent GSALDH as separate core activities. SmPutA primary explicitly assays CoQ1 and NAD+; Bj quinone coupling is supported by the established reaction-class literature, while the acceptor of every original2010 trace was not independently recovered from its inaccessible supplement. FAD is an internal cofactor, not the terminal acceptor. Both enzymes channel intermediate; neither fused sequence nor a structural domain establishes uptake or gene repression.

Bj tetramerization is experimentally real, but engineered active dimers preclude an obligatory tetramer claim. SmPutA has a concentration-dependent monomer–dimer equilibrium; its extra CTD Rossmann fold does not bind NAD+. Native membrane-face localization is a conserved-mechanism inference, not a target localization assay. Regulatory IPR025703 mappings are over-annotated for these non-RHH architectures; no negative DNA-binding assay or evolutionary-loss claim is made. Proline-biosynthesis mapping is removed as a pathway-direction error.

Both raw UniProt records place the proteins in PTHR42862:SF1, official label DELTA-1-PYRROLINE-5-CARBOXYLATE DEHYDROGENASE 2, ISOFORM A-RELATED. No family review was edited.

Manifest: manifest.txt and manifest.json. Frozen proof: preservation-proof.json. History creation uses persistent history-state.json; do not rerun scaffold commands.
