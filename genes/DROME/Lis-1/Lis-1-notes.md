# Lis-1 (Drosophila melanogaster, Q7KNS3) — review notes

## 2026-09-27 — initial review (claude-code)

Sources: UniProt Q7KNS3, cached GOA-cited publications (full text for PMID:16107559, 22764052, 23918939,
21041636, 18946501, 22808215, 28837701, 26265702, 25694447, 18758451, 21943192; abstract-only for the rest).
Deep research (falcon) was not yet available when this review was written.

### Core biology
- Lis1 physically associates with dynein and dynactin in fly extracts [PMID:16107559 "Using anti-Lis1 antibodies, we could immunoprecipitate both dynein and dynactin subunits"].
- Lis1 recruits dynein-dynactin to mRNA cargo and promotes dynein-dynactin association [PMID:23918939 "Furthermore, we provide evidence that Lis1 levels regulate the overall association of dynein with dynactin."].
- Required for dynein-dynactin recruitment to nuclear surface and spindle poles in male germ cells [PMID:22764052 "LIS-1 colocalizes with dynein-dynactin at the nuclear surface and spindle poles of male germ cells and is required for recruiting dynein-dynactin to these sites."].
- Nuclear migration: oocyte nucleus positioning, with genetic interactions with Glued and Dhc [PMID:10993674 "DLis1 shows genetic interactions with the Glued and Dynein heavy chain subunits of the dynein/dynactin complex"]; with BicD/Egl in oocyte determination [PMID:10559989].
- Mitosis: centrosome separation, spindle assembly, poleward stripping of Rod from kinetochores [PMID:16107559].
- Neurons: neuroblast proliferation, dendrite arborization, axonal transport [PMID:11056531]; retrograde transport of Neuroglian [PMID:28837701] and Dscam restriction [PMID:18946501].
- Fly Lis1 does not bind the fly PAF-AH alpha homolog [PMID:10737922], so the PAF-AH regulatory-subunit role of human LIS1 is not supported in flies.
- Lineage-/tissue-specific: Lis1 binds and stabilises Mad in GSCs (co-IP in S2 cells) [PMID:21041636].

### Decisions
- MF: added NEW GO:0140659 cytoskeletal motor regulator activity (matches human PAFAH1B1 review and nucleokinesis module).
- protein binding (Mad) -> MODIFY to GO:0046332 SMAD binding.
- dynein complex / dynactin complex (part_of) -> MODIFY to GO:0005875 microtubule associated complex: LIS1 is a transient regulator, not a stoichiometric subunit; association captured by GO:0070840.
- Muscle cell cellular homeostasis (PMID:21256839): UNDECIDED; abstract-only and does not mention Lis1.
- Developmental processes (oogenesis, fusome, dendrite, border cell migration, GSC) kept as non-core.
