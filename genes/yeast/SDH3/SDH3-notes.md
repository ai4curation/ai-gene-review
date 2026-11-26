# SDH3 (YKL141W, P33421) notes

Evidence journal for the review; sources are UniProt and cached publications.

- Large cytochrome b (CybL) membrane-anchor subunit of complex II [UniProt:P33421 "Membrane-anchoring mono-heme cytochrome b subunit of"].
- Quinone site / heme: [PMID:9822678 "The membrane intrinsic domain, consisting of Sdh3p and Sdh4p, is proposed to bind two molecules of ubiquinone and one heme."]; [PMID:9929002 "The cytochrome is not detectable in mitochondria isolated from SDH3 and SDH4 deletion strains."]
- Heme ligands and dispensability: [PMID:18028869 "we constructed an S. cerevisiae strain expressing a mutant enzyme lacking the two heme axial ligands, Sdh3p His-106 and Sdh4p Cys-78"]; [PMID:18028869 "Our results strongly suggest that heme is not required for electron transport from succinate to quinone nor is it necessary for assembly of the S. cerevisiae SDH."]
- Moonlighting in TIM22: [PMID:22152483 "We have identified a further subunit of the carrier translocase (TIM22 complex) that surprisingly is identical to subunit 3 of respiratory complex II, succinate dehydrogenase (Sdh3)."]; [PMID:22152483 "Sdh3 forms a subcomplex with Tim18 and is involved in biogenesis and assembly of the membrane-integral subunits of the TIM22 complex."]

Curation decisions
- Two core functions: (1) complex II membrane anchor/quinone site (MF ubiquinone binding GO:0048039, contributes_to GO:0008177); (2) TIM22 complex subunit (GO:0042721, GO:0045039).
- No GOA row for ubiquinone binding or heme binding on SDH3, although Sdh4p has both by IBA/ISS. Heme binding (His-106 axial ligand, PMID:18028869) is an obvious gap, and ubiquinone binding is a plausible one; neither was added as NEW, and both are recorded here.
- IEA 'electron transfer activity' was kept as non-core: yeast heme is dispensable for electron transfer.
- Tim18 is the paralog-like partner of Sdh3 in TIM22 (analogous to Sdh4). This is a useful module-level observation: SDH3 is shared between complex II and TIM22.
