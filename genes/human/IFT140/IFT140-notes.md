# IFT140 notes (human, Q96RY7)

## Deep research status
DRSTATUS

## Summary
- IFT-A core subunit [PMID:27932497 "we show that the IFT-A complex is divided into a core subcomplex, composed of IFT122/IFT140/IFT144, which is associated with TULP3, and a peripheral subcomplex, composed of IFT43/IFT121/IFT139, where IFT139 is most distally located."]; human IFT-A cryo-EM [PMID:36775821 "Here we report cryo-EM structures of human IFT-A complexes in the presence and absence of TULP3 at overall resolutions of 3.0-3.9 Å."]
- Retrograde IFT [PMID:22503633 "IFT140 is one of the six currently known components of the intraflagellar transport complex A (IFT-A) that regulates retrograde protein transport in ciliated cells."]; trypanosome IFT140 RNAi [PMID:30388400 "In the retrograde mutant IFT140 RNAi , trains travel into the new flagellum but fail to be recycled to the base."]
- Membrane-protein import with TULP3 [PMID:20889716 "IFT-A is linked to retrograde ciliary transport, but, surprisingly, we find that the IFT-A complex has a second role directing ciliary entry of TULP3."]; [PMID:20889716 "TULP3 and IFT-A, in turn, promote trafficking of a subset of G protein-coupled receptors (GPCRs), but not Smoothened, to cilia."]; [PMID:36775821 "TULP3, the cargo adapter, interacts with IFT-A through its N-terminal region, and interface mutations disrupt cargo transport."]
- Localization mainly at base [PMID:27932497 "In control RPE1 cells, IFT140 staining was mainly found at the base, with weak staining along cilia (Figure 4F)"]; centrosome [PMID:23418020 "Although flag-tagged IFT140 localizes to centrosomes in the majority of cells examined, mutant protein carrying the p.V292M missense change was absent from centrosome in most cells (Fig."]
- IFT-A KO (non-IFT122) in RPE1 has minor ciliogenesis effects [PMID:29220510 "whereas KO of other IFT-A genes had minor effects on ciliogenesis but impaired ciliary protein trafficking."]
- Disease: MSS/JATD, RP80, PKD9 [PMID:34890546 "IFT140 is a core component of the intraflagellar transport-complex A, responsible for retrograde ciliary trafficking and ciliary entry of membrane proteins; bi-allelic IFT140 variants cause the syndromic ciliopathy, short-rib thoracic dysplasia (SRTD9)."]

## Key curation decisions
- ACCEPT: IFT-A (6 rows), retrograde IFT (4), protein localization to (non-motile) cilium (5), protein carrier activity contributes_to (2), cilium/basal body/axoneme/ciliary tip/non-motile cilium, cilium assembly.
- KEEP_AS_NON_CORE: intraciliary anterograde transport (IDA x2): IFT-A rides anterograde trains and is needed for GPCR entry, but anterograde motility is kinesin-2/IFT-B driven; also centrosome/centriole, photoreceptor terms. For PMID:40472089 the cached text shows only TULP3 work, so the curator's full-text reading is deferred to.
- MODIFY: regulation of cilium assembly (IMP PMID:22503633) -> cilium assembly.
- REMOVE: protein binding (4 rows; IFT-A partners IFT122/WDR19).
- Note: local GO version labels GO:0140597 as "protein carrier chaperone" (GOA still "protein carrier activity").

## HPA cilium atlas vs module role
HPA v25: Basal body (Supported) only; main location Basal body. This matches the observation that IFT-A is concentrated at the ciliary base with weak axonemal signal (Hirano et al. 2017), and the GO_REF:0000052 basal body row is accepted. The module places IFT140 in the IFT-A annoton with process "intraciliary retrograde transport" and role_description "Retrograde train component and adaptor for membrane-protein entry with TULP3". The core functions agree, but argue that ciliary membrane-protein import (IFT-A/TULP3; GO:0097499 protein localization to non-motile cilium, contributes_to protein carrier activity) should be a second process on the IFT-A annoton, not only text in role_description. Also, the stage label "axoneme extension by IFT" fits IFT-A less well than IFT-B: non-IFT122 IFT-A knockouts have only minor ciliogenesis defects.

## Shared IFT background

- IFT particles are built from two biochemically distinct complexes, IFT-A and IFT-B [PMID:15955805 "IFT particles contain multiple copies of two distinct protein complexes, A and B, which contain at least 6 and 11 protein subunits, respectively."]
- Motors: kinesin-2 drives anterograde and dynein-2 drives retrograde movement [PMID:15955805 "Anterograde movement of particles away from the cell body is mediated by kinesin-2, whereas retrograde movement away from the flagellar tip is powered by cytoplasmic dynein 1b/2."]
- IFT-B core vs peripheral: high-salt core contains IFT88, IFT81, IFT74/72, IFT52, IFT46, IFT27 [PMID:15955805 "revealing a 500-kDa core that contains IFT88, IFT81, IFT74/72, IFT52, IFT46, and IFT27."]; IFT172 is peripheral [PMID:15955805 "This result demonstrates that the complex B subunits, IFT172, IFT80, IFT57, and IFT20 are not required for the core subunits to stay associated."]
- Human IFT-B architecture by VIP: 10 core + 6 peripheral subunits [PMID:26980730 "we determined the overall architecture of the IFT-B complex, which can be divided into core and peripheral subcomplexes composed of 10 and 6 subunits, respectively."]
- IFT-B is the train backbone [PMID:36354106 "The IFT-B complex constitutes the backbone of polymeric IFT trains carrying cargo between the cilium and the cell body."]; IFT-B1 carries cargo sites, IFT-B2 binds inactive dynein-2 [PMID:36354106 "The IFT-B complex organizes into IFT-B1 and IFT-B2 parts with binding sites for ciliary cargo and the inactive IFT dynein motor, respectively."]
- Directionality: [PMID:27932497 "Intraflagellar transport (IFT)-A and -B complexes mediate retrograde and anterograde ciliary protein trafficking, respectively."] — but IFT-A also mediates ciliary entry of GPCRs [PMID:27932497 "Thus the data presented here demonstrate that the IFT-A complex mediates not only retrograde trafficking but also entry into cilia of GPCRs."]

## GOA curation issue common to all IFT-B subunits

Every IFT-B subunit annotated from PMID:26980730 (Katoh et al. 2016, an IFT-B architecture paper) carries an IDA to GO:0030991 *intraciliary transport particle A*. This contradicts the paper's own content (which supports the GO:0030992 IFT-B IPI rows from the same paper) and the established biochemistry. Marked REMOVE as a genuinely contradicted claim (likely batch term-selection error), not as second-guessing assay data.
