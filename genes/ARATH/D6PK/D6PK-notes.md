# D6PK (D6 PROTEIN KINASE, AGC1-1, PK64; At5g55910; UniProt Q9FG74) notes

Identity verified: UniProt Q9FG74 "Serine/threonine-protein kinase D6PK", OrderedLocusNames At5g55910.
Deep research: falcon failed (Edison API 429, 2026-10-05).

## Activity and localization
- Basal PM, colocalizes with PINs; phosphorylates PINs [PMID:19168677 "D6PK localizes to the basal (lower) membrane of Arabidopsis root cells, where it colocalizes with PIN1, PIN2 and PIN4."; "D6PK phosphorylates PIN proteins in vitro and in vivo"].
- Activates PIN-mediated efflux; kinase-dead inactive [PMID:24948515 "a kinase-dead variant of D6PK could not activate auxin efflux in this system"].
- Lipid binding through polybasic motif [PMID:27836964 "We further show that D6PK directly binds polyacidic phospholipids through a polybasic lysine-rich motif in the middle domain of the kinase."].
- Planar polarity switch at root-hair initiation [PMID:27251533].

## Physiology
- Phototropism via PIN3/4/7 [PMID:23709629 "phototropic hypocotyl bending is strongly dependent on the activity of D6PKs and the PIN proteins PIN3, PIN4, and PIN7"]; gravitropism [PMID:29490064].

## Decisions
- Specific phosphoinositide-binding rows KEEP_AS_NON_CORE (non-selective polyacidic lipid binding); GO:1901981 accepted.
- PMID:14749726 (Anthony 2004) abstract is about AGC2-1/OXI1; D6PK-PDK1 binding row removed as GO:0005515 regardless.
- NEW GO:2000012 regulation of auxin polar transport (IDA PMID:24948515).


## Polar auxin transport source audit — 2026-10-26

This dated audit supersedes conflicting earlier shorthand. All 40 original annotation payloads, including qualifiers and inherited NEW rows, were retained exactly. Every row was reconsidered against the target biology and cited sources. Actual Falcon and fallback provider attempts failed; the orchestration logs are preserved in `.cache/module-audit-logs/auxin-polar-fetch/provider-publication-results.json`. Existing provider reports, where present, served only as discovery aids. Manual primary-source inspection and normally fetched caches support the decisions below. No provider report was fabricated.

D6PK is a PIN-activating serine/threonine kinase with basal plasma-membrane recruitment. Direct transport activation and native polar localization are distinct from a general PIN polarity-switch mechanism. PMID:24948515 oocyte assays identify tested carrier/kinase pairs; no all-PIN combinatorial inference is made. Full PMID:38278951 adds CXX(X)P S-acylation and PDK1-dependent recruitment/phosphorylation mechanism; these are not merely transplanted PID properties.

ATP binding is core catalytic substrate recognition. Phosphatidylinositol phosphate and phosphatidic-acid binding contribute to membrane recruitment. The actual public Fig.5 image and caption for PMID:27251533 were inspected at https://www.nature.com/articles/nplants2015162/figures/5 (normal caption cache retained); GST-D6PK lipid-strip binding is compared with GST control. Positive in-vitro binding to less physiologically established lipids, including PIP3, is retained non-core rather than declared false because native plant abundance is uncertain. This does not manufacture a native PIP3 signaling pathway. PMID:27836964 supports the polybasic domain; full publisher retrieval was unavailable, so details beyond the abstract are not newly claimed from it.

Nucleus IBA/ISM remain UNDECIDED; membrane recruitment is not a nuclear exclusion experiment. PTN000682243 is retained from the original assertion, with unavailable target-resolved ancestral placement disclosed rather than invented. The inherited NEW regulation-of-auxin-polar-transport annotation is retained. General cell-periphery/basal-region/kinase terms are refined to supported membrane or catalytic terms; no root-organelle narrowing is used.

Final actions: 18 ACCEPT, 9 KEEP_AS_NON_CORE, 6 MODIFY, 1 NEW, 4 REMOVE, 2 UNDECIDED. This panel contains no negated source rows; there are no manufactured NOT assertions. Exact-row payload proof and focused validation are recorded in `.cache/module-audit-logs/auxin-polar-six-*`. Reciprocal scientific consultation with the parallel annotation reviewer confirmed source-specific localization, integral binding and substrate-assay distinctions.
