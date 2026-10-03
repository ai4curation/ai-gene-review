# IFT81 notes (human, Q8WYA0)

## Deep research status
DRSTATUS

## Summary
- IFT81/IFT74 tubulin module [PMID:23990561 "Here, we found that the two core IFT proteins IFT74 and IFT81 form a tubulin-binding module and mapped the interaction to a calponin homology domain of IFT81 and a highly basic domain in IFT74."]; affinity [PMID:23990561 "HsIFT81N bound tubulin with a dissociation constant (Kd) of 16 μM via a highly conserved, positively charged surface patch, which was enhanced 18-fold by IFT74N (Fig. 1G and fig. S3)."]; required for ciliogenesis [PMID:23990561 "Knockdown of IFT81 and rescue experiments with point mutants showed that tubulin binding by IFT81 was required for ciliogenesis in human cells."]
- Direct IFT81-IFT74 interaction conserved [PMID:15955805 "Yeast-based two-hybrid and three-hybrid analyses were then used to show that IFT81 and IFT74/72 directly interact to form a higher order oligomer consistent with a tetrameric complex."]
- RABL2B binds the IFT74/81 C-termini [PMID:28625565 "Additional mapping revealed that RABL2B binds to the C-terminal portions of both IFT74 and IFT81, distinct from the N-terminal tubulin cargo binding domains of IFT74/81 (Fig."]
- SRTD19 [PMID:27666822 "In mutant chondrocytes, the mutations led to low levels of IFT81 and mutant cells produced elongated cilia, had altered hedgehog signaling, had increased post-translation modification of tubulin, and showed evidence of destabilization of additional anterograde transport complex components."]

## Key curation decisions
- ACCEPT core: tubulin binding (IDA/IBA/IEA), IFT-B, intraciliary transport involved in cilium assembly, anterograde IFT, cilium assembly.
- MODIFY: protein binding with RABL2B (Q9UNT1) -> small GTPase binding (GO:0031267).
- REMOVE: protein binding with IFT74 (complex-internal), IFT-A IDA.
- KEEP_AS_NON_CORE: regulation of smoothened signaling (indirect), spermatogenesis, sperm flagellum assembly, sperm midpiece/principal piece, centrosome/centriole/MTOC, cytoplasm.

## HPA cilium atlas vs module role
HPA v25: Primary cilium (Approved), Basal body (Approved), Centrosome (Approved); main location Cytosol. The cytosolic main call reflects the large unassembled/cytoplasmic pool; ciliary and basal body calls fit the IFT-B role. No GO_REF:0000052 rows. Module role "IFT-B core; tubulin binding" and role_description "IFT81-IFT74 bind tubulin cargo" are fully consistent with core_functions (MF tubulin binding; intraciliary transport involved in cilium assembly; anterograde IFT; IFT-B complex). IFT81 (with IFT74) is the one IFT-B subunit pair for which the module's "IFT cargo adaptor" function is directly demonstrated.

## Shared IFT background

- IFT particles are built from two biochemically distinct complexes, IFT-A and IFT-B [PMID:15955805 "IFT particles contain multiple copies of two distinct protein complexes, A and B, which contain at least 6 and 11 protein subunits, respectively."]
- Motors: kinesin-2 drives anterograde and dynein-2 drives retrograde movement [PMID:15955805 "Anterograde movement of particles away from the cell body is mediated by kinesin-2, whereas retrograde movement away from the flagellar tip is powered by cytoplasmic dynein 1b/2."]
- IFT-B core vs peripheral: high-salt core contains IFT88, IFT81, IFT74/72, IFT52, IFT46, IFT27 [PMID:15955805 "revealing a 500-kDa core that contains IFT88, IFT81, IFT74/72, IFT52, IFT46, and IFT27."]; IFT172 is peripheral [PMID:15955805 "This result demonstrates that the complex B subunits, IFT172, IFT80, IFT57, and IFT20 are not required for the core subunits to stay associated."]
- Human IFT-B architecture by VIP: 10 core + 6 peripheral subunits [PMID:26980730 "we determined the overall architecture of the IFT-B complex, which can be divided into core and peripheral subcomplexes composed of 10 and 6 subunits, respectively."]
- IFT-B is the train backbone [PMID:36354106 "The IFT-B complex constitutes the backbone of polymeric IFT trains carrying cargo between the cilium and the cell body."]; IFT-B1 carries cargo sites, IFT-B2 binds inactive dynein-2 [PMID:36354106 "The IFT-B complex organizes into IFT-B1 and IFT-B2 parts with binding sites for ciliary cargo and the inactive IFT dynein motor, respectively."]
- Directionality: [PMID:27932497 "Intraflagellar transport (IFT)-A and -B complexes mediate retrograde and anterograde ciliary protein trafficking, respectively."] — but IFT-A also mediates ciliary entry of GPCRs [PMID:27932497 "Thus the data presented here demonstrate that the IFT-A complex mediates not only retrograde trafficking but also entry into cilia of GPCRs."]

## GOA curation issue common to all IFT-B subunits

Every IFT-B subunit annotated from PMID:26980730 (Katoh et al. 2016, an IFT-B architecture paper) carries an IDA to GO:0030991 *intraciliary transport particle A*. This contradicts the paper's own content (which supports the GO:0030992 IFT-B IPI rows from the same paper) and the established biochemistry. Marked REMOVE as a genuinely contradicted claim (likely batch term-selection error), not as second-guessing assay data.
