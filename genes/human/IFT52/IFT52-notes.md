# IFT52 notes (human, Q9Y366)

## Deep research status
Falcon deep research succeeded (IFT52-deep-research-falcon.md; first run, ~15 min). Its conclusions agree with this review: [file:human/IFT52/IFT52-deep-research-falcon.md "Direct human genetics and knockout/rescue experiments strongly establish IFT52 as an IFT-B scaffold required for ciliary assembly and anterograde transport."] It also reports (Ishida 2022, Tasaki 2025; not cached here) that IFT52 knockout in RPE1 cells abolishes mother-centriole recruitment of IFT88/IFT38 and ciliogenesis, and (Dupont 2019) a proposed extraciliary centrosome-cohesion role in mouse IMCD3 cells that remains less established; consistent with keeping centrosome/centriole rows as non-core.

## Summary
IFT52 is an IFT-B1 core hub subunit [PMID:28625565 "IFT52 is a critical bridge between the IFT-B1 to the IFT-B2 subcomplexes (Taschner et al., 2016), and also links two IFT-B1 subcomplexes (IFT81/74/22/27/25 and IFT88/70/52/46) (Taschner et al., 2014)."]
- SRTD16 patient cells: [PMID:27466190 "The IFT52 mutant cells synthesized a significantly reduced amount of IFT52 protein, leading to reduced synthesis of IFT74, IFT81, IFT88 and ARL13B, other key anterograde complex members."]; [PMID:27466190 "These data demonstrate that IFT52 is essential for anterograde complex integrity and for the biosynthesis and maintenance of cilia."]
- Photoreceptor ciliary base, with SANS/USH1G [PMID:31637240 "Quantitative immunofluorescence microscopy revealed the co-localization of SANS with IFT20, IFT52, and IFT57 particularly at ciliary base of wild type mouse photoreceptor cells."]

## Key curation decisions
- ACCEPT: IFT-B complex, anterograde IFT (IMP PMID:27466190, NAS), intraciliary transport, cilium assembly, cilium/basal body/ciliary base/tip.
- REMOVE: protein binding (4 rows), IFT-A IDA (PMID:26980730).
- KEEP_AS_NON_CORE: centrosome/centriole, motile cilium, photoreceptor cilium terms, dendrite terminus (neuronal ciliary base).

## HPA cilium atlas vs module role
HPA v25: Primary cilium (Approved), Basal body (Approved); main location Microtubules. Consistent with the module role (IFT-B subunit of anterograde trains, stage 4). Only Approved-grade reliability; no GO_REF:0000052 rows exist for IFT52. Core functions agree with the module's process (intraciliary anterograde transport, cilium assembly) and complex; as for IFT88, no cargo-adaptor MF is asserted because IFT52's demonstrated role is structural bridging within IFT-B.

## Shared IFT background

- IFT particles are built from two biochemically distinct complexes, IFT-A and IFT-B [PMID:15955805 "IFT particles contain multiple copies of two distinct protein complexes, A and B, which contain at least 6 and 11 protein subunits, respectively."]
- Motors: kinesin-2 drives anterograde and dynein-2 drives retrograde movement [PMID:15955805 "Anterograde movement of particles away from the cell body is mediated by kinesin-2, whereas retrograde movement away from the flagellar tip is powered by cytoplasmic dynein 1b/2."]
- IFT-B core vs peripheral: high-salt core contains IFT88, IFT81, IFT74/72, IFT52, IFT46, IFT27 [PMID:15955805 "revealing a 500-kDa core that contains IFT88, IFT81, IFT74/72, IFT52, IFT46, and IFT27."]; IFT172 is peripheral [PMID:15955805 "This result demonstrates that the complex B subunits, IFT172, IFT80, IFT57, and IFT20 are not required for the core subunits to stay associated."]
- Human IFT-B architecture by VIP: 10 core + 6 peripheral subunits [PMID:26980730 "we determined the overall architecture of the IFT-B complex, which can be divided into core and peripheral subcomplexes composed of 10 and 6 subunits, respectively."]
- IFT-B is the train backbone [PMID:36354106 "The IFT-B complex constitutes the backbone of polymeric IFT trains carrying cargo between the cilium and the cell body."]; IFT-B1 carries cargo sites, IFT-B2 binds inactive dynein-2 [PMID:36354106 "The IFT-B complex organizes into IFT-B1 and IFT-B2 parts with binding sites for ciliary cargo and the inactive IFT dynein motor, respectively."]
- Directionality: [PMID:27932497 "Intraflagellar transport (IFT)-A and -B complexes mediate retrograde and anterograde ciliary protein trafficking, respectively."] — but IFT-A also mediates ciliary entry of GPCRs [PMID:27932497 "Thus the data presented here demonstrate that the IFT-A complex mediates not only retrograde trafficking but also entry into cilia of GPCRs."]

## GOA curation issue common to all IFT-B subunits

Every IFT-B subunit annotated from PMID:26980730 (Katoh et al. 2016, an IFT-B architecture paper) carries an IDA to GO:0030991 *intraciliary transport particle A*. This contradicts the paper's own content (which supports the GO:0030992 IFT-B IPI rows from the same paper) and the established biochemistry. Marked REMOVE as a genuinely contradicted claim (likely batch term-selection error), not as second-guessing assay data.
