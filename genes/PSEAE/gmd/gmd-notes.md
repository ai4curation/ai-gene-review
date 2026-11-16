# gmd (PA5453, Q51366) review notes

GDP-mannose 4,6-dehydratase, first step toward GDP-D-rhamnose (the A-band O
polysaccharide sugar donor). Purified P. aeruginosa GMD is bifunctional [PMID:19459932 "P. aeruginosa GMD is bifunctional, and can catalyze both GDP-d-mannose 4,6-dehydration and the subsequent reduction reaction to produce GDP-D-rhamnose."] and acts in A-band biosynthesis [PMID:19459932 "Genes encoding GMD and RMD are present in P. aeruginosa, and genetic evidence indicates they act in A-band O-polysaccharide biosynthesis."]. gmd was identified earlier as an A-band gene [PMID:9781879 "Gmd, a previously reported A-band enzyme, and Rmd are predicted to perform the two-step conversion of GDP-D-Man to GDP-D-Rha."].

P. aeruginosa makes GDP-D-rhamnose, NOT GDP-L-fucose: no GDP-L-fucose synthase (fcl)
is present in PAO1 (UniProt query 2026-11-05 found only lecB, a fucose-binding lectin).

## PseudoCAP IBA-seed assessment

Other seeds from .cache/paint/IBD.gaf, 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008684430 | GO:0008446 GDP-mannose 4,6-dehydratase activity | 11 | 154 (98 taxa) | GO:0008446, EXP PMID:9781879 (PseudoCAP) | SOUND | GMD activity firmly established (direct assay PMID:19459932). The PseudoCAP EXP cites PMID:9781879, which treats gmd as a previously reported enzyme; the direct demonstration is PMID:19459932. No defect (abstract of 9781879 not read in full; activity unambiguous). | worm, mouse Gmds (MGI:1891112), E. coli Gmd P0AC88, human GMDS O60547, Arabidopsis AT3G51160, fly, Dictyostelium, Trypanosoma Q387W4 | Yes |

Node term is the exact GMD activity; suits a broad 98-taxon clade. No PSEUDOCAP or
GO_CENTRAL defect on the GO:0008446 seed.

Received leaf IBA: GO:0042351 'de novo' GDP-L-fucose biosynthetic process. Seeds are
fucose producers (Arabidopsis, human GMDS, fly, Trypanosoma, Dictyostelium), not gmd.
GMD is the shared first step; the pathway identity is set by the downstream enzyme
(Fcl for fucose, Rmd for rhamnose). P. aeruginosa makes GDP-D-rhamnose, so the
GDP-L-fucose term is wrong for this gene. MARK_AS_OVER_ANNOTATED with a GO_CENTRAL
note (CHECK, PROBABLE): the GDP-L-fucose IBD should not propagate to non-fucose
lineages. The IBD itself is fine for its fucose-producing seeds.
