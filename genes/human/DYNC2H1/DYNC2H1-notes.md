# DYNC2H1 (Q8NCM8) research notes

Cytoplasmic dynein 2 heavy chain 1 (DHC2, DHC1b), human. Catalytic AAA+ motor subunit of cytoplasmic dynein-2.

## Deep research status
DEEP_RESEARCH_STATUS_PLACEHOLDER

## Summary of function
- Dynein-2 is the retrograde IFT motor. [PMID:31451806 "Dynein-2, the ubiquitous motor for retrograde IFT, is crucial for cilia biogenesis"]
- Recombinant human DHC2 is a two-headed, minus-end-directed motor. [PMID:21723285 "both dynein-1 and dynein-2 showed minus-end-directed motor activities"; "This is the first demonstration of dynein-2 motor activity, which supports the retrograde intraflagellar transport role of dynein-2."]
- Architecture: two DHC2 copies, each with an N-terminal tail and a C-terminal AAA+ ring. [PMID:31451806 "The two copies of DHC2 span the complex, each comprising a compact N-terminal domain, an elongated tail region, and a C-terminal AAA+ motor domain."] Tails are bound by the WDR60 and WDR34 beta-propellers. [PMID:31451806 "DHC2TAIL-A and -B, are bound by the β-propeller of WDR60 and WDR34 respectively, mainly via bundle 3"] LIC3 (DYNC2LI1) binds tightly. [PMID:31451806 "DHC2, while maintaining a tight association with LIC3, did not homodimerize in the absence of the bridging IC-LC subunits and was monomeric"]
- Cycle: the motor is carried to the tip autoinhibited on IFT-B trains, then reactivated. [PMID:31451806 "Dynein-2 assembles with IFT trains at the ciliary base, moves to the tip in an inhibited state under the power of kinesin-II, then restructures to drive retrograde transport back to the cell body"]
- H1 subcomplex: [PMID:29742051 "the H1 subcomplex (the heavy chain DYNC2H1 directly interacting with the light intermediate chain DYNC2LI1)"]
- Golgi: an early report placed DHC2 at the Golgi [PMID:8666668 "DHC2 is localized predominantly to the Golgi apparatus."]. A later review presents this only as an early alternative proposal [PMID:30065109 "An alternative proposal held that dynein-2 functions in Golgi organization [15]."].
- Disease: the main cause of short-rib thoracic dysplasia (SRTD3; Jeune/SRPS). [PMID:25830415 "most of which are involved in retrograde intraflagellar transport (IFT) (IFT43, IFT122, WDR19, WDR35, TTC21B, and DYNC2H1)"]

## Key curation decisions
- GO has no dynein-2-specific complex term (checked in OLS: no hits for "cytoplasmic dynein-2"). GO:0005868 cytoplasmic dynein complex is used.
- REMOVE: male germ cell nucleus (NAS, PMID:36973253). The full text is about DYNLRB1/2 dynein-1 and never mentions DYNC2H1 or dynein-2.
- MODIFY: cytoskeletal motor activity changed to minus-end-directed MT motor activity. Protein binding (DYNC2LI1) changed to dynein light intermediate chain binding.
- MARK_AS_OVER_ANNOTATED: plasma membrane (IEA/ISS) and cilium movement involved in cell motility (IBA). For the IBA, the GOA WITH/FROM donors are axonemal DNAH heavy chains, from PTN000743491.
- Golgi apparatus and Golgi organization (IDA, 1996): KEEP_AS_NON_CORE. These are not overruled.

## HPA cilium atlas vs module role
- Module (primary_cilium_life_cycle, stage 4 axoneme_extension_ift) assigns DYNC2H1 as a dynein-2 subunit with minus-end-directed MT motor activity (GO:0008569) in intraciliary retrograde transport (GO:0035721) at the axoneme.
- HPA v25 (member_evidence.md): no cilium, basal body or centrosome call. Main locations are "Mid piece; Mitochondria" (sperm mid piece from tissue staining). The HPA cilium atlas [PMID:41005307 "Our analysis identified the subciliary locations of 715 proteins across three cell lines"] is cached as abstract only, so whether DYNC2H1 was assayed in it cannot be checked here. The member_evidence table records no ciliary call.
- Assessment: the missing HPA call most likely reflects antibody sensitivity for a very large, low-abundance heavy chain, not absence. Its three non-catalytic partners (DYNC2LI1, DYNC2I1, DYNC2I2) all have HPA primary cilium / basal body calls. The module role is strongly supported by biochemistry, structure and genetics, and core_functions agrees with it (motor activity, retrograde IFT, axoneme, cytoplasmic dynein complex). No disagreement.
