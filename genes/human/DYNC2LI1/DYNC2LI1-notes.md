# DYNC2LI1 (Q8TCX1) research notes

Cytoplasmic dynein 2 light intermediate chain 1 (D2LIC, LIC3), human.

## Deep research status
Falcon deep research succeeded (`DYNC2LI1-deep-research-falcon.md`; the first attempt with the 600 s default timed out, and the rerun with --timeout 2400 succeeded). Its summary agrees with the publication-based review below. The review's supporting quotes come from the cached publications.

## Summary of function
- Identified as a D2LIC that binds DHC2. [PMID:11907264 "D2LIC subunit interacts specifically with DHC2 (or cDhc1b) in both reciprocal immunoprecipitations and sedimentation assays."] It was originally seen at the Golgi [PMID:11907264 "D2LIC colocalizes with DHC2 at the Golgi apparatus throughout the cell cycle."].
- Part of the retrograde IFT motor across species. [PMID:12802074 "indicate that the novel LIC is a component of the cDHC1b/DHC2 retrograde IFT motor in a variety of organisms."]
- Structural role: [PMID:31451806 "LIC3 binds in a similar way to DHC2-A and -B, stabilizing the portion of the tail distal to the hinge sites"]. The Ras-like core has a conserved nucleotide-binding pocket (PMID:31451806).
- Loss of function (SRTD15 patient fibroblasts, RPE1 knockdown): [PMID:26077881 "We show that DYNC2LI1 is essential for dynein-2 complex stability, is expressed in the cartilage growth plate, and plays critical roles in the regulation of primary cilium length, retrograde IFT, and Hedgehog signaling."; "Our results demonstrate that loss of DYNC2LI1 markedly impairs retrograde IFT and leads to the accumulation of IFT proteins within the primary cilium."]
- Localization: [PMID:26130459 "Using immunofluorescence analysis in ciliated fibroblast cells we confirmed the localization of the DYNC2LI1 protein to the cytoplasm, centrosomes, as well as around the basal body, and the transition zone of the primary cilium"]

## Key curation decisions
- Core MF: dynein heavy chain binding (IBA + IDA). Contributes to minus-end-directed motor activity as a non-catalytic subunit.
- REMOVE: male germ cell nucleus (NAS; the cited paper does not mention the gene). Also protein binding with SOD1 (generic, BAG3 paper).
- MODIFY: protein binding (DYNC2H1) changed to dynein heavy chain binding.
- MARK_AS_OVER_ANNOTATED: colocalizes with cytoplasmic microtubule (ISS).
- Golgi (EXP 2002), centrosome, transition zone and regulation of cilium assembly (length phenotype) are KEEP_AS_NON_CORE.

## HPA cilium atlas vs module role
- Module stage 4: dynein-2 subunit; complex-level MF minus-end-directed MT motor activity; retrograde IFT; axoneme.
- HPA v25: Primary cilium (Supported), Basal body (Supported); main locations Cytosol and Mid piece. GOA carries the HPA rows (GO_REF:0000052) for cilium, ciliary basal body and cytosol, all reviewed (cilium/basal body ACCEPT, cytosol non-core).
- Assessment: HPA agrees with the module role (cilium plus ciliary base pool). core_functions uses contributes_to minus-end-directed MT motor activity, in cytoplasmic dynein complex, for retrograde IFT. No disagreement.
