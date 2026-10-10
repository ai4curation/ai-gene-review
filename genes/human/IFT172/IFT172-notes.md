# IFT172 notes (human, Q9UG01)

## Deep research status
Falcon deep research failed twice (falcon 600 s timeout with unavailable perplexity-lite fallback; then exit 137 at --timeout 2400) and succeeded on the third attempt (IFT172-deep-research-falcon.md). Additions (primary papers not cached): endogenous IFT172 at ciliary base and along the axoneme in human fibroblasts; purified IFT172 binds and remodels phospholipid membranes (Wang 2018), with membrane binding and IFT57 binding mutually exclusive [file:human/IFT172/IFT172-deep-research-falcon.md "Membrane association and binding of IFT57 to IFT172 appear mutually exclusive, suggesting a possible way to regulate when IFT172 associates with membranes versus an assembling IFT complex."]; Chlamydomonas ift172 ts mutant accumulates IFT material at the tip (turnaround role); a C-terminal U-box-like ubiquitin-binding domain (Zacharia, eLife) with no established E3 activity. None is asserted as a GO MF here; membrane binding raised as a suggested question.

## Summary
- Peripheral IFT-B (IFT-B2) subunit [PMID:15955805 "This result demonstrates that the complex B subunits, IFT172, IFT80, IFT57, and IFT20 are not required for the core subunits to stay associated."]; human VIP architecture [PMID:26980730 "we determined the overall architecture of the IFT-B complex, which can be divided into core and peripheral subcomplexes composed of 10 and 6 subunits, respectively."]
- Disease: Jeune/MZSDS [PMID:24140113 "Fibroblasts from affected individuals showed disturbed ciliary composition, suggesting alteration of ciliary transport and signaling."]; zebrafish [PMID:24140113 "Knockdown of ift172 in zebrafish recapitulated the human phenotype and demonstrated a genetic interaction between ift172 and ift80."]; isolated RP and BBS [PMID:25168386 "These findings expand the spectrum of disease associated with mutations in IFT172 and suggest that mutations in genes originally reported to be associated with syndromic ciliopathies should also be considered in subjects with non-syndromic retinal dystrophy."]
- Roles proposed from model organisms (tip turnaround in Chlamydomonas fla11; membrane binding) are not cached as primary literature here and are not asserted as core functions.

## Key curation decisions
- ACCEPT: IFT-B (IBA/IEA/IPI/ISS), intraciliary transport particle, anterograde IFT (NAS), intraciliary transport, cilium assembly (IDA PMID:24140113 etc.), cilium organization, axoneme, basal body, cilium, ciliary tip.
- REMOVE: protein binding (2), IFT-A IDA (PMID:26980730).
- MARK_AS_OVER_ANNOTATED: extracellular vesicle (HDA, CSF EV proteome).
- KEEP_AS_NON_CORE: smoothened signaling pathway (indirect), sperm midpiece/principal piece/cytoplasmic droplet.

## HPA cilium atlas vs module role
IFT172 is not in HPA v25 (no cilium/centrosome call; "not in HPA"), so the atlas neither supports nor contradicts its module placement; there are no GO_REF:0000052 rows. The module's assignment (IFT-B peripheral subunit of anterograde trains; anterograde transport and cilium assembly) rests entirely on biochemical, model-organism and human-genetic literature, which supports it. Core functions agree; no cargo-adaptor MF is asserted for IFT172.

## Shared IFT background

- IFT particles are built from two biochemically distinct complexes, IFT-A and IFT-B [PMID:15955805 "IFT particles contain multiple copies of two distinct protein complexes, A and B, which contain at least 6 and 11 protein subunits, respectively."]
- Motors: kinesin-2 drives anterograde and dynein-2 drives retrograde movement [PMID:15955805 "Anterograde movement of particles away from the cell body is mediated by kinesin-2, whereas retrograde movement away from the flagellar tip is powered by cytoplasmic dynein 1b/2."]
- IFT-B core vs peripheral: high-salt core contains IFT88, IFT81, IFT74/72, IFT52, IFT46, IFT27 [PMID:15955805 "revealing a 500-kDa core that contains IFT88, IFT81, IFT74/72, IFT52, IFT46, and IFT27."]; IFT172 is peripheral [PMID:15955805 "This result demonstrates that the complex B subunits, IFT172, IFT80, IFT57, and IFT20 are not required for the core subunits to stay associated."]
- Human IFT-B architecture by VIP: 10 core + 6 peripheral subunits [PMID:26980730 "we determined the overall architecture of the IFT-B complex, which can be divided into core and peripheral subcomplexes composed of 10 and 6 subunits, respectively."]
- IFT-B is the train backbone [PMID:36354106 "The IFT-B complex constitutes the backbone of polymeric IFT trains carrying cargo between the cilium and the cell body."]; IFT-B1 carries cargo sites, IFT-B2 binds inactive dynein-2 [PMID:36354106 "The IFT-B complex organizes into IFT-B1 and IFT-B2 parts with binding sites for ciliary cargo and the inactive IFT dynein motor, respectively."]
- Directionality: [PMID:27932497 "Intraflagellar transport (IFT)-A and -B complexes mediate retrograde and anterograde ciliary protein trafficking, respectively."] — but IFT-A also mediates ciliary entry of GPCRs [PMID:27932497 "Thus the data presented here demonstrate that the IFT-A complex mediates not only retrograde trafficking but also entry into cilia of GPCRs."]

## GOA curation issue common to all IFT-B subunits

Every IFT-B subunit annotated from PMID:26980730 (Katoh et al. 2016, an IFT-B architecture paper) carries an IDA to GO:0030991 *intraciliary transport particle A*. This contradicts the paper's own content (which supports the GO:0030992 IFT-B IPI rows from the same paper) and the established biochemistry. Marked REMOVE as a genuinely contradicted claim (likely batch term-selection error), not as second-guessing assay data.
