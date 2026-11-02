# ATG3 (donkey, A0A9L0J149) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New folder for the 314-residue donkey ATG3 product A0A9L0J149 (genes/EQUAS/ATG3 is keyed to the longer splice product A0A9L0IHI0). Created with `just fetch-gene EQUAS A0A9L0J149 --alias ATG3__A0A9L0J149`; 9 GOA rows, all electronic (8 TreeGrafter, 1 combined ARBA/InterPro, 1 SubCell). No ProtNLM2 output was consulted.

Deep research: `just deep-research-falcon EQUAS ATG3__A0A9L0J149 --fallback perplexity-lite` failed (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). Review written from cached publications and UniProt records instead.

Evolutionary grounding (ATG3__A0A9L0J149-bioinformatics/RESULTS.md): donkey, human Q9NT62, mouse Q9CPX6 and yeast P40344 are all in PANTHER PTHR12866:SF2; donkey is 98.4% identical to human and mouse, and all mapped human functional residues (Cys264 active site, Lys243 ATG12 acceptor, N-terminal amphipathic helix incl. Lys9/Lys11, LIR 104-110, LETD) are conserved. Only change in the ATG12-binding acidic region is D148E.

Experimental evidence comes from orthologs only:
- Human ATG3 is an E2 for GATE-16, GABARAP and LC3, Cys264 active site [PMID:11825910 "Site-directed mutagenesis revealed that Cys(264) of hApg3p is an authentic active-site cysteine residue"].
- Mouse Atg3 knockout: "Conjugate formation of mammalian Atg8 homologues was completely defective in the mutant mice." [PMID:18768753]
- N-terminal AH couples curvature sensing to conjugase activity [PMID:33446636].
- ATG12-ATG3 conjugate on a single lysine via ATG3 autocatalysis; mitochondrial homeostasis [PMID:20723759].

PAINT check (QuickGO, Q9NT62): human IBAs are GO:0141046 Atg8-family conjugating enzyme activity (PTN000305308), autophagosome assembly, mitophagy and nucleophagy (yeast donors), glycophagy (Drosophila donor), PAS and cytosol. Donkey TreeGrafter still carries GO:0019776 Atg8-family ligase activity, so I MODIFY it (and the general GO:0019787) to GO:0141046. Selective-autophagy process terms kept as non-core: deliberate PAINT placements, ATG3 does catalytic work in them, but they are applications of the core activity. Cytoplasm MODIFY to cytosol. No NEW terms proposed; GO:0019777 Atg12 transferase activity (autoconjugation) was considered but not added because PAINT did not propagate it and the evidence is mouse-cell only.
