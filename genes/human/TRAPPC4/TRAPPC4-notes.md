# TRAPPC4 notes

Review started from `just fetch-gene human TRAPPC4`. The proteostasis network places TRAPPC4 under `Autophagy-Lysosome Pathway > Autophagophore initiation and elongation > Autophagy component recruitment to autophagophore > TRAPP complex component`, the same PN leaf as TRAPPC1 and TRAPPC3.

Falcon deep research was requested with `just deep-research-falcon human TRAPPC4`. The provider timed out after 600 seconds and no `TRAPPC4-deep-research-falcon.md` file was produced, so this review is completed from the accessible UniProt, GOA, cached literature, Reactome, and local PN-context evidence.

TRAPPC4/synbindin is a core TRAPP-complex subunit with direct human disease evidence. UniProt describes TRAPPC4 as a "Core component of the TRAPP complexes" and says it plays roles in ER-to-Golgi transport and autophagy. The direct TRAPPC4 paper states that "TRAPPC4, like its yeast Trs23 orthologue, is a core component of the TRAPP complexes" and "one of the essential subunits for guanine nucleotide exchange factor activity for Rab1 GTPase" [PMID:31794024 "Deficiencies in vesicular transport mediated by TRAPPC4 are associated with severe syndromic intellectual disability."]. It also reports that reduced TRAPPC4 caused a "defect in TRAPP complex assembly and/or stability" [PMID:31794024]. Therefore TRAPP complex membership, contribution to complex-level RAB1 GEF activity, and ER-Golgi transport are core.

The strongest process evidence is ER-to-Golgi/Golgi trafficking. Patient fibroblasts with reduced TRAPPC4 showed VSVG-GFP-ts045 "significantly delayed entry into and exit from the Golgi" and wild-type TRAPPC4 restored trafficking [PMID:31794024]. Reactome states that "The TRAPPC complex acts as a guanine-nucleotide exchange factor for RAB1, activating it" [Reactome:R-HSA-5694409 "Nucleotide exchange on RAB1"] and that "TRAPPC is a multi-subunit tethering complex that facilitates ER-to-Golgi traffic" [Reactome:R-HSA-5694439 "COPII coat binds TRAPPCII and RAB1:GDP"]. Broad vesicle-mediated transport, COPII coat assembly, and obsolete vesicle tethering rows should be modified to ER-to-Golgi vesicle-mediated transport rather than accepted as-is.

Unlike TRAPPC1 and TRAPPC3, TRAPPC4 has direct autophagy evidence in the seeded GOA. The TRAPPC4 disease paper reports a "basal autophagy defect and a delay in autophagic flux" in patient fibroblasts and yeast validation with "constitutive and stress-induced autophagic defects" [PMID:31794024]. Accept the existing broad autophagy annotation as supported, while noting that the mechanism is probably TRAPP complex assembly/stability and TRAPPIII/RAB1 context rather than a standalone autophagy-specific molecular activity.

TRAPPII/TRAPPIII complex annotations are supportable for TRAPPC4. The same paper says the human TRAPP core includes TRAPPC4 and forms TRAPP II and TRAPP III through accessory proteins; yeast data conclude that low Trs23 "affects the assembly of the core TRAPP complex and likely affects assembly of TRAPP II and TRAPP III" [PMID:31794024]. These are useful complex-context annotations for the PN TRAPP leaf.

The neuronal synbindin annotations should be kept as non-core or trimmed for over-specificity. The original synbindin paper reports that synbindin is "present on membrane-bound cisterns and vesicles within the soma and dendrites" and "associated with synaptic membranes, mainly at the postsynaptic side" [PMID:11018053 "Synbindin, A novel syndecan-2-binding protein in neuronal dendritic spines."]. This supports dendrite/synapse/postsynaptic membrane localization as a non-core neuronal context. However, `synaptic vesicle`, `presynaptic active zone`, `postsynaptic density membrane`, and broad `dendrite development` are likely over-specific because the paper itself says "At present, we do not know whether synbindin acts as a downstream effector" in spine formation [PMID:11018053].

Generic `protein binding` is not useful as a TRAPPC4 function. The TRAPPI architecture paper and the ERK2 paper document specific interactions, including that "TRAPPC4 was found to bind with ERK2" [PMID:21826244 "TRAPPC4-ERK2 interaction activates ERK1/2, modulates its nuclear localization and regulates proliferation and apoptosis of colorectal cancer cells."], but the generic GO term should be marked as over-annotated. Specific biology is better represented by TRAPP complex membership and, where relevant, a non-core MAPK signaling question.

Annotation stance:
- Core: TRAPP complex membership (GO:0030008), TRAPPII/TRAPPIII membership, contributes-to TRAPP complex RAB1 GEF activity, ER-to-Golgi vesicle-mediated transport, autophagy, cytoplasm/cytosol, ER, Golgi/Golgi membrane/Golgi stack, and broad vesicle localization.
- Non-core: neuronal synbindin localization at dendrites, synapse, and postsynaptic membrane.
- Modify: broad vesicle-mediated transport, vesicle coat assembly, COPII vesicle coat assembly, and obsolete vesicle tethering to ER-to-Golgi vesicle-mediated transport.
- Mark over-annotated: generic protein binding, synaptic vesicle, presynaptic active zone, postsynaptic density membrane, and broad dendrite development.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording framed the TRAPP-component context as PN-specific and directly relevant because human patient fibroblasts and yeast Trs23 models show trafficking and autophagy defects.
