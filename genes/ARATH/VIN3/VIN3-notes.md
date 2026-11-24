# VIN3 curation notes

## Session 2026-10-05 (vernalization_flc_silencing module)

- Q9FIE3, At5g57380. Falcon deep research failed (agentapi missing / timeout).
- Founding paper: [PMID:14712276 "Here we identify a gene with a function in the measurement of the duration of cold exposure and in the establishment of the vernalized state."]
- PHD-PRC2: [PMID:18854416 "during prolonged cold a PHD-PRC2 complex forms composed of core PRC2 components (VRN2, SWINGER"] plus VRN5, VIN3, VEL1.
- Heterodimer with VRN5: [PMID:17174094 "VRN5 and VIN3 form a heterodimer necessary for establishing the vernalization-induced chromatin modifications"].
- Not an H3 reader: [PMID:36174674 "using ITC and NMR spectroscopy, we were unable to detect binding of the purified VIN3 PHD superdomain nor of its minimal PHD finger to various modified and unmodified histone H3 tail peptides."] An earlier pull-down claimed H3 binding (cited within that paper); the quantitative assays supersede it. IBA histone H3 reader activity was therefore REMOVED.
- VEL polymerization: [PMID:36351412 "Mutations blocking polymerization of this VEL domain prevent Polycomb silencing at FLC."]; in vivo: [PMID:40858112 "VIN3 VEL polymerization produces higher-order nuclear VIN3 assemblies in vivo, which promote multivalent chromatin association and efficient H3K27me3 nucleation."]. Basis for the NEW GO:0140693 molecular condensate scaffold activity.
- VRN5 bridges VIN3 to PRC2: [PMID:40858112 "it is required to physically connect VIN3 with PRC2"].
- Nucleation vs spreading: [PMID:28818969 "a subset of Polycomb repressive complex 2 factors nucleate silencing in a small region within FLC"].
- Hypoxia (secondary): [PMID:19392705 "VIN3 is required for the survival of Arabidopsis thaliana in response to hypoxic stress"].

## Decisions
- IBA constitutive heterochromatin formation -> MODIFY to facultative heterochromatin formation (GO:0140718), since this is Polycomb silencing.
- Protein binding: VIL1/VEL1 rows -> MODIFY to protein heterodimerization activity; VRN2 and 14-3-3 rows -> REMOVE.
