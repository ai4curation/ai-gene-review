# IFT74 notes (human, Q96LB3)

## Deep research status
Falcon deep research succeeded on the second attempt (IFT74-deep-research-falcon.md; first run timed out at 600 s with no available fallback; rerun with --timeout 2400). It agrees that IFT74's direct molecular role is tubulin binding with IFT81 plus IFT-B organization, and adds 2023 patient studies (Bakey et al., Fassad et al.; not cached) showing an exon-2 (first 40 residues) deletion that separates IFT-B association from tubulin/microtubule binding [file:human/IFT74/IFT74-deep-research-falcon.md "Selected IFT-B subunits, including IFT81, still co-precipitated with exon-2-deleted IFT74, whereas the deleted protein bound microtubules much less effectively in vitro."], with very short motile airway cilia and skeletal ciliopathy. This strengthens beta-tubulin binding as the core MF and supports keeping motile cilium as a correct location.

## Summary
- IFT74 = CMG-1; GFP fusion vesicular [PMID:11683410 "A CMG-1-green fluorescent protein (GFP) chimera was observed to target to an intracellular vesicular compartment."]
- Tubulin module with IFT81 [PMID:23990561 "Thus, IFT81N appears to bind the globular domain of tubulin to provide specificity, and IFT74N recognizes the β-tubulin tail to increase affinity (Fig. 1H)."]; [PMID:23990561 "Here, we have shown that the two core IFT proteins IFT74 and IFT81 form a tubulin-binding module required for ciliogenesis, which suggests a role of IFT74/81 in the transport of tubulin within cilia."]
- RABL2B docking [PMID:28428259 "We also show that RABL2 interacts, in its GTP-bound state, with the intraflagellar transport (IFT)-B complex via the IFT74-IFT81 heterodimer and that the interaction is disrupted by a mutation found in male infertile mice (Mot mice) with a sperm flagella motility defect."]
- Disease: MMAF/infertility [PMID:33689014 "IFT74 encodes for a core component of the IFT machinery that is essential for the anterograde transport of tubulin."]; Joubert [PMID:33531668 "Attenuated ciliogenesis; altered distribution of IFT proteins and ciliary membrane proteins, including ARL13B, INPP5E, and GPR161"]

## Key curation decisions
- ACCEPT core: beta-tubulin binding (IDA/IBA/IEA), IFT-B, intraciliary transport involved in cilium assembly, anterograde IFT, cilium assembly, HPA basal body.
- MODIFY: protein binding with RABL2B -> small GTPase binding.
- REMOVE: protein binding with IFT-B partners, IFT-A IDA.
- MARK_AS_OVER_ANNOTATED: chromatin binding and nucleus (IEA from mouse Ift74 IDA, PMID:20545763/16705683 not reviewed).
- KEEP_AS_NON_CORE: Golgi and centriolar satellite (HPA), cytoplasmic vesicle (EXP/IEA), acrosomal vesicle, motile cilium, centrosome.

## HPA cilium atlas vs module role
HPA v25: Basal body (Supported), Centriolar satellite (Supported); main locations Basal body, Centriolar satellite, Golgi apparatus. HPA makes no primary-cilium (shaft) call for IFT74, whereas the module places IFT74 in anterograde trains along the axoneme. This is not a contradiction: IFT-B subunits are concentrated at the ciliary base and only sparsely distributed in moving trains, so antibody sensitivity favours the base; the atlas also stresses cell-type and single-cilium heterogeneity [PMID:41005307 "We found that 69% of the ciliary proteome is cell-type specific, and 78% exhibited single-cilia heterogeneity."]. GO_REF:0000052 rows: ciliary basal body (ACCEPT), centriolar satellite and Golgi (KEEP_AS_NON_CORE). Core functions agree with the module role "IFT-B core; tubulin binding".

## Shared IFT background

- IFT particles are built from two biochemically distinct complexes, IFT-A and IFT-B [PMID:15955805 "IFT particles contain multiple copies of two distinct protein complexes, A and B, which contain at least 6 and 11 protein subunits, respectively."]
- Motors: kinesin-2 drives anterograde and dynein-2 drives retrograde movement [PMID:15955805 "Anterograde movement of particles away from the cell body is mediated by kinesin-2, whereas retrograde movement away from the flagellar tip is powered by cytoplasmic dynein 1b/2."]
- IFT-B core vs peripheral: high-salt core contains IFT88, IFT81, IFT74/72, IFT52, IFT46, IFT27 [PMID:15955805 "revealing a 500-kDa core that contains IFT88, IFT81, IFT74/72, IFT52, IFT46, and IFT27."]; IFT172 is peripheral [PMID:15955805 "This result demonstrates that the complex B subunits, IFT172, IFT80, IFT57, and IFT20 are not required for the core subunits to stay associated."]
- Human IFT-B architecture by VIP: 10 core + 6 peripheral subunits [PMID:26980730 "we determined the overall architecture of the IFT-B complex, which can be divided into core and peripheral subcomplexes composed of 10 and 6 subunits, respectively."]
- IFT-B is the train backbone [PMID:36354106 "The IFT-B complex constitutes the backbone of polymeric IFT trains carrying cargo between the cilium and the cell body."]; IFT-B1 carries cargo sites, IFT-B2 binds inactive dynein-2 [PMID:36354106 "The IFT-B complex organizes into IFT-B1 and IFT-B2 parts with binding sites for ciliary cargo and the inactive IFT dynein motor, respectively."]
- Directionality: [PMID:27932497 "Intraflagellar transport (IFT)-A and -B complexes mediate retrograde and anterograde ciliary protein trafficking, respectively."] — but IFT-A also mediates ciliary entry of GPCRs [PMID:27932497 "Thus the data presented here demonstrate that the IFT-A complex mediates not only retrograde trafficking but also entry into cilia of GPCRs."]

## GOA curation issue common to all IFT-B subunits

Every IFT-B subunit annotated from PMID:26980730 (Katoh et al. 2016, an IFT-B architecture paper) carries an IDA to GO:0030991 *intraciliary transport particle A*. This contradicts the paper's own content (which supports the GO:0030992 IFT-B IPI rows from the same paper) and the established biochemistry. Marked REMOVE as a genuinely contradicted claim (likely batch term-selection error), not as second-guessing assay data.
