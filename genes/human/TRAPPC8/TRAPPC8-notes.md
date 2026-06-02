# TRAPPC8 notes

Review started from `just fetch-gene human TRAPPC8`. The proteostasis network places TRAPPC8 under `Autophagy-Lysosome Pathway > Autophagophore initiation and elongation > Autophagy component recruitment to autophagophore > TRAPP complex component`.

Falcon deep research was requested with `just deep-research-falcon human TRAPPC8`, but the provider timed out after 600 seconds and did not produce `TRAPPC8-deep-research-falcon.md`. The review therefore relies on the cached UniProt, GOA, Reactome, publication, and PN context files listed here.

TRAPPC8 is the mammalian Trs85 ortholog and a TRAPPIII-associated TRAPP subunit. The mammalian TRAPP component paper identifies KIAA1012/TRAPPC8 as a Trs85p ortholog and says "KIAA1012 was annotated in GenBank as TRAPPC8, a Trs85p orthologue" [PMID:21525244 "C4orf41 and TTC-15 are mammalian TRAPP components with a role at an early stage in ER-to-Golgi trafficking."]. The TRAPP review lists TrappC8 as a TRAPP III-specific Trs85 ortholog and states that mammalian TRAPP III contains core TRAPP plus TrappC8, 11-13 [PMID:27066478 "TRAPP Complexes in Secretion and Autophagy."]. Accept TRAPPIII and TRAPP complex membership.

TRAPPC8 has direct mammalian autophagy evidence, unlike several shared small core subunits. The TBC1D14 paper states that "TRAPPC8, the mammalian orthologue of a yeast autophagy-specific TRAPP subunit, forms part of a mammalian TRAPPIII-like complex" and that "TRAPPC8 modulates autophagy and secretory trafficking" [PMID:26711178 "TBC1D14 regulates autophagy via the TRAPP complex and ATG9 traffic."]. It further concludes that TBC1D14/TRAPPIII maintain "the cycling pool of ATG9 required for initiation of autophagy" [PMID:26711178]. This supports including autophagy/ATG9 trafficking in the core function synthesis, even though the current seeded GOA lacks a direct autophagy process row.

TRAPPC8 also has ER-to-Golgi and collagen-cargo transport evidence. PMID:21525244 reports that C8 depletion causes Golgi fragmentation and supports an early secretory pathway role; it says C8 is a bona fide TRAPP subunit and that "C8 depletion causes Golgi fragmentation, supporting a role for the mammalian orthologue in ER-to-Golgi trafficking" [PMID:21525244]. The TMEM131 paper says "TRAPPC8-containing TRAPP III is critical for the ER-to-Golgi transport of collagen cargos" and that TMEM131 recruits TRAPP III "for the ER-to-Golgi transport of collagen cargo" [PMID:32095531 "Broadly conserved roles of TMEM131 family proteins in intracellular collagen assembly and secretory cargo trafficking."]. Therefore, accept ER-to-Golgi transport, but modify `collagen biosynthetic process` to ER-to-Golgi vesicle-mediated transport because TRAPPC8 acts in collagen cargo trafficking rather than collagen biosynthesis chemistry.

The Golgi organization row is direct but should be non-core. C8 depletion produces Golgi fragmentation in the mammalian TRAPP paper, but this is best interpreted as a consequence/readout of early secretory pathway disruption rather than the core function itself. Keep as non-core.

The COPII coat assembly and obsolete vesicle tethering annotations are over-specific. The collagen paper places TRAPPC8/TRAPP III in ER-to-Golgi transport of collagen cargo in COPII vesicles, but it does not show TRAPPC8 assembling the COPII coat. The TRAPP review says "evidence that any TRAPP complex acts as a membrane tether is currently inconclusive" [PMID:27066478]. Modify these annotations to ER-to-Golgi vesicle-mediated transport.

Generic protein binding annotations should be marked as over-annotated. The interaction evidence is specific to TRAPP architecture, TBC1D14/TRAPP, or TMEM131/TRAPPC8, and should not be represented as generic `protein binding`.

Annotation stance:
- Core: TRAPPIII/TRAPP complex membership, contributes-to TRAPP/TRAPPIII RAB1 GEF activity, ER-to-Golgi vesicle-mediated transport, ATG9/autophagy trafficking context, Golgi/cytosol/cytoplasm.
- Non-core: Golgi organization as a depletion phenotype/readout.
- Modify: collagen biosynthetic process, COPII vesicle coat assembly, and obsolete vesicle tethering to ER-to-Golgi vesicle-mediated transport.
- Mark over-annotated: generic protein binding rows.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording described autophagophore recruitment as PN-specific and directly supported for TRAPPC8 by mammalian TBC1D14/TRAPPIII/ATG9 evidence.
