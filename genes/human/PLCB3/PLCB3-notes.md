# PLCB3 review notes

## Deep research

- `just deep-research-falcon human PLCB3 --fallback perplexity-lite` did not produce a provider file in this runtime: `deep-research-client[cyberian]==0.2.12` only exposed the `claude_code` provider, so the requested `falcon` provider failed and the `perplexity` fallback was unavailable. I did not synthesize a `PLCB3-deep-research-*.md` file manually; curation below is based on the seeded GOA rows, UniProt, cached Reactome records, PAINT family context, and cached primary papers.

## Core molecular function

- PLCB3 is the human PLC-beta3 PI(4,5)P2 phospholipase. UniProt records EC 3.1.4.11 from direct PLCB3 sources including Waldo et al. 2010, Falzone and MacKinnon 2023 PNAS G beta/gamma, Falzone and MacKinnon 2023 PNAS G alpha q, and Tall et al. 1997 [PMID:20966218; PMID:37172014; PMID:37991948; PMID:9188725].
- The recent membrane assays separate the two G protein inputs. G beta/gamma increases membrane recruitment and orientation of PLCB3; nonlipidated G alpha q increases PLCB3 `kcat`; and the two can bind at the same time, supporting coincidence detection between Gq- and Gi-derived signals [PMID:37172014; PMID:37991948].
- Waldo et al. 2010 also shows that PLCB3 terminates G alpha q signaling by acting as a GAP: the EF3/4 loop accelerates GTP hydrolysis by G alpha q in a P2Y1 receptor/heterotrimeric Gq/PLCB3 reconstitution. GOA lacks this direct `GO:0005096` row, so the review adds it as `NEW` [PMID:20966218].

## Accepted non-core context

- Calmodulin binding is real from a yeast two-hybrid screen plus CaM-Sepharose and in vitro binding assays, but I treated it as regulatory/non-core because the main PLCB3 effector module is driven by G alpha q and G beta/gamma [PMID:12821674].
- Cytoplasmic/cytosolic and cytoplasmic-side-of-membrane rows are mutually compatible: PLCB3 is soluble until it partitions onto the substrate membrane surface. Nuclear and nucleoplasmic localization rows were kept as secondary pools because the core GPCR-linked reaction is membrane-surface PIP2 hydrolysis [PMID:29122926; PMID:37172014].
- Postsynaptic cytosol was kept as a neuronal context for canonical mGlu1/Gq/PLC/PKC signaling at the Purkinje-cell synapse, not as PLCB3's general location [PMID:27276689].

## Rows removed or demoted

- All bare `GO:0005515` protein-binding rows are removed under the local policy. The GNAQ interactions are represented by Gq-dependent PLCB3 activation and the OSBPL2 row remains only a reported protein-stability context [PMID:21822282; PMID:23377541; PMID:38701954].
- The DisProt `molecular adaptor activity` and `molecular function activator activity` rows from the full-length G alpha q-PLCB3 structure do not match what the paper shows. PLCB3 is a monomeric G alpha q effector in that study, not a bridge between two independent partners, and G alpha q activates PLCB3 rather than vice versa [PMID:23377541]. PLCB3's true regulator-of-G protein activity is the separate GTPase activator activity established by Waldo et al. [PMID:20966218].
- The `phospholipase C-activating serotonin receptor signaling pathway` row cites the Waldo G alpha q/PLCB3 paper, but that paper reconstituted P2Y1 receptor signaling and does not assay serotonin receptors. I kept the generic `GO:0007200` claim and flagged the serotonin-specific term as a UniProt term-selection defect [PMID:20966218].
- The `cadherin binding` HDA row comes from an E-cadherin BioID/proteomics candidate list and was demoted to over-annotation pending direct PLCB3-cadherin evidence [PMID:25468996].
- The alpha1D-adrenergic receptor blood-pressure and protein-containing-complex rows over-extend a PLCB3 TAP/MS hit near alpha-syntrophin. The physiological blood-pressure result tested syntrophin/dystrophin scaffolding of alpha1D-AR, not direct PLCB3 action [PMID:18468998].

## GO-CAM follow-up

- Sibling GO-CAM `67c10cc400004380` places the PLCB3 `GO:0004435` activity in `GO:0005737` cytoplasm. The gene review accepts cytoplasm as a coarse soluble-pool location, but the modeled PIP2 hydrolysis reaction is better placed at `GO:0098562` cytoplasmic side of membrane because PLCB3 hydrolyzes membrane PI(4,5)P2 after G alpha q or G beta/gamma recruitment.
