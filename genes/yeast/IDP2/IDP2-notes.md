# IDP2 notes (P41939, YLR174W)

- Cytosolic NADP+-IDH, EC 1.1.1.42 [UniProt:P41939 "Reaction=D-threo-isocitrate + NADP(+) = 2-oxoglutarate + CO2 + NADPH;"].
- One of three compartment-specific paralogs [PMID:19854152 "mitochondrial IDP1 [1], cytosolic IDP2 [2], and peroxisomal IDP3 [3, 4]"].
- Authentic Idp2 fractionates with cytosol; peroxisomal only when a PTS1 is appended [PMID:19854152 "IDP2 was located almost entirely in the cytosolic fraction"].
- Bidirectional kinetics; main isocitrate/2-OG flux on nonfermentable carbon [PMID:15574419 "through the IDP2-catalyzed reaction in cells grown with a nonfermentable carbon source (glycerol and lactate)"].
- NADPH source for antioxidant defence with Zwf1 [PMID:19854152 "are the predominant cytosolic sources of NADPH for thiol-based antioxidant systems"]; [PMID:15001388 "IDP2, whether located in mitochondria or in the cytosol, provided the highest level of defense"].
- Glutamate link is precursor supply only: relocated IDPs can support glutamate synthesis [PMID:15001388 "the IDP isozymes are functionally interchangeable for glutamate synthesis"], but 2-OG for glutamate during glucose growth is mainly from mitochondrial IDH [PMID:15574419].

Decisions: REMOVE IBA mitochondrion, peroxisome, TCA cycle (paralog/compartment over-propagation); MODIFY NAD binding -> NADP binding, NADP+ metabolic process -> NADPH regeneration; RCA L-glutamate biosynthesis -> MARK_AS_OVER_ANNOTATED.
