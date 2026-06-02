# TRAPPC13 notes

Review started from `just fetch-gene human TRAPPC13`. The proteostasis network places TRAPPC13 under `Autophagy-Lysosome Pathway > Autophagophore initiation and elongation > Autophagy component recruitment to autophagophore > TRAPP complex component`.

Falcon deep research was requested with `just deep-research-falcon human TRAPPC13`, but the provider timed out after 600 seconds and no `TRAPPC13-deep-research-falcon.md` file was produced. I am completing the review using the cached primary literature, UniProt record, GOA seed, and Reactome context described below.

TRAPPC13/C5orf44 is a Trs65-related TRAPP subunit. UniProt describes it as "Part of the multisubunit TRAPP (transport protein particle) complex" and lists ComplexPortal TRAPPII entries [file:human/TRAPPC13/TRAPPC13-uniprot.txt]. The TRAPP review maps yeast Trs65 to human TrappC13/C5orf44 and says the mammalian genetic-interaction model includes TRAPP II with core TRAPP plus TrappC9-10 and TRAPP III with core TRAPP plus TrappC8, 11-13 [PMID:27066478 "TRAPP Complexes in Secretion and Autophagy."]. Accept TRAPPII and TRAPPIII complex context, while noting that the precise human complex assignment differs across sources.

TRAPPC13 should be modeled as contributing to complex-level RAB GEF/trafficking rather than independently enabling a catalytic molecular function. Reactome states that RAB1 nucleotide exchange is stimulated by "the GEF activity of the multisubunit TRAPPC complexes II and III" [Reactome:R-HSA-8877475 "TRAPPC complexes exchange GTP for GDP on RAB1"]. The TRAPP review says TRAPP acts as a Ypt/Rab GEF and specifically notes that mammalian Golgi TRAPP II acts in vitro as a Rab1, but not Rab11, GEF [PMID:27066478]. Accept ER-to-Golgi vesicle-mediated transport as the supported process for the PN TRAPP component context.

The PN autophagy context should not be converted into a TRAPPC13-specific autophagy process annotation without direct evidence. Reactome links TRAPPCIII/RAB1 to pre-autophagosomal structure biology, but the review cautions that the mammalian TRAPP III-autophagy connection was not clear in 2016 [PMID:27066478 "the connection of the mammalian TRAPP III complex to autophagy is currently not clear"]. For this draft, represent the PN context through TRAPPIII/TRAPP complex membership and RAB1/TRAPP trafficking rather than adding a direct autophagy row.

The vesicle coat assembly and obsolete vesicle tethering rows are over-specific. Reactome supports COPII-associated ER-to-ERGIC traffic and TRAPP complex RAB1 exchange, but TRAPPC13 is not shown to assemble vesicle coats. The TRAPP review says "evidence that any TRAPP complex acts as a membrane tether is currently inconclusive" [PMID:27066478]. Modify both rows to ER-to-Golgi vesicle-mediated transport.

Generic protein binding rows from TRAPP and proteome-scale interactome sources are not informative molecular-function annotations. The PMID:21453443/UniProt interactions with TRAPPC2L, TRAPPC3, and TRAPPC8 support TRAPP complex context, while PMID:33961781 is a proteome-scale AP-MS interaction map. Mark these rows as over-annotated rather than treating generic binding as a core function.

Annotation stance:
- Core: TRAPPII/TRAPPIII complex context, contributes-to TRAPP complex RAB1 GEF activity, ER-to-Golgi vesicle-mediated transport, cytoplasm and cytosol.
- Modify: vesicle coat assembly and obsolete vesicle tethering to ER-to-Golgi vesicle-mediated transport.
- Mark over-annotated: generic protein binding rows.
- No new direct autophagy annotation unless Falcon or later primary literature provides TRAPPC13-specific support.
