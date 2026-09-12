# TRAPPC5 notes

Review started from `just fetch-gene human TRAPPC5`. The proteostasis network places TRAPPC5 under `Autophagy-Lysosome Pathway > Autophagophore initiation and elongation > Autophagy component recruitment to autophagophore > TRAPP complex component`, the same PN leaf as TRAPPC1, TRAPPC3, and TRAPPC4.

Falcon deep research was requested with `just deep-research-falcon human TRAPPC5`, but the provider timed out after 600 seconds and did not produce `TRAPPC5-deep-research-falcon.md`. The review therefore relies on the cached UniProt, GOA, Reactome, publication, and PN context files listed here.

TRAPPC5 is the human ortholog of yeast Trs31 and a small TRAPP core subunit. UniProt says TRAPPC5 is a "Component of the multisubunit TRAPP (transport protein particle) complex" and may function in ER-to-Golgi vesicular transport. The mammalian TRAPP component paper states that yeast TRAPP I includes Trs31p, "with the mammalian orthologues named TRAPPC1, TRAPPC2, TRAPPC3, TRAPPC4, TRAPPC5, and TRAPPC6a/b" [PMID:21525244 "C4orf41 and TTC-15 are mammalian TRAPP components with a role at an early stage in ER-to-Golgi trafficking."]. It also reports that C2/C2L purifications contained "known human TRAPP components, including C3, C4, and C5" [PMID:21525244]. Accept TRAPP complex membership and the ER-to-Golgi transport process.

TRAPPC5 should be modeled as contributing to complex-level RAB1 GEF activity rather than independently enabling a catalytic activity. The same mammalian TRAPP paper notes that yeast TRAPP GEF/tethering activities are dependent on Bet3p, Trs31p, Trs23p, and Bet5p [PMID:21525244 "These activities are dependent on the subunits Bet3p, Trs31p, Trs23p, and Bet5p"]. Reactome states that "The TRAPPC complex acts as a guanine-nucleotide exchange factor for RAB1, activating it" [Reactome:R-HSA-5694409 "Nucleotide exchange on RAB1"] and that RAB1 exchange is stimulated by "the GEF activity of the multisubunit TRAPPC complexes II and III" [Reactome:R-HSA-8877475 "TRAPPC complexes exchange GTP for GDP on RAB1"].

The TRAPPI protein-complex annotation needs caution in human. PMID:21525244 says mammalian TRAPP differs from yeast and that their study supports the "absence of a TRAPP I-equivalent complex in mammalian cells" [PMID:21525244]. The TRAPP review similarly says "TRAPP I cannot be separated from the mammalian TRAPP II and its existence in vivo in mammalian cells is currently in question" and "there is currently no evidence for the existence of TRAPP I in mammalian cells" [PMID:27066478 "TRAPP Complexes in Secretion and Autophagy."]. Therefore, mark human TRAPPI protein complex as over-annotated, but accept TRAPPII/TRAPPIII where ComplexPortal/Reactome support them.

The PN autophagy context should be represented through TRAPPIII/TRAPP membership unless TRAPPC5-specific autophagy evidence appears. The PN mapping rationale says the TRAPP component leaf is autophagy-contextual but that the shared gene-level semantics are captured by TRAPP complex membership [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv]. Reactome links TRAPPCIII/RAB1 to pre-autophagosomal structure biology, but TRAPPC5 itself has no seeded direct autophagy process annotation.

The coat-assembly and obsolete tethering annotations are likely over-specific. Reactome supports TRAPP/COPII/RAB1 recruitment on ER-derived vesicles, but TRAPPC5 is not a COPII coat-assembly factor. The TRAPP review states that "evidence that any TRAPP complex acts as a membrane tether is currently inconclusive" [PMID:27066478]. Modify vesicle coat assembly, COPII vesicle coat assembly, and obsolete vesicle tethering to ER-to-Golgi vesicle-mediated transport.

Generic protein binding annotations from proteome-scale interactome sources are not informative for TRAPPC5. Specific interactions with TRAPPC3, TRAPPC2, CCNDBP1, or HMG20A are better captured as TRAPP complex membership or left as non-core interaction context, not as a core molecular function.

Annotation stance:
- Core: TRAPP complex membership, TRAPPII/TRAPPIII complex membership, contributes-to TRAPP complex RAB1 GEF activity, ER-to-Golgi vesicle-mediated transport, cytoplasm/cytosol, ER, and Golgi apparatus.
- Non-core: broad Golgi vesicle transport.
- Modify: vesicle coat assembly, COPII vesicle coat assembly, and obsolete vesicle tethering to ER-to-Golgi vesicle-mediated transport.
- Mark over-annotated: human TRAPPI protein complex and generic protein binding rows.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording described the TRAPP-component context as PN-specific and interpreted TRAPPC5 through TRAPP/TRAPPII/TRAPPIII complex membership and ER-Golgi trafficking rather than a broad autophagy process annotation.
