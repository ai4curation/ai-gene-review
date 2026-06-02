# PDCD6IP notes

## Review focus

PDCD6IP encodes ALIX/AIP1, a Bro1-domain ESCRT accessory/adaptor protein. The key curation issue is that GOA contains many generic protein-binding records and many pathway contexts. The core biological picture is not undifferentiated binding: ALIX links cargo/adaptors and membrane-remodeling sites to CHMP4/ESCRT-III, supporting MVB/late-endosomal sorting, exosome biogenesis, midbody cytokinesis, membrane repair, and selected viral-budding pathways.

## Direct evidence

- UniProt summarizes ALIX as a multifunctional ESCRT-associated adaptor: a "Class E VPS protein involved in concentration and sorting of cargo proteins of the multivesicular body (MVB)" and an "Adapter for a subset of ESCRT-III proteins, such as CHMP4" [UniProt:Q8WUM4 "Class E VPS protein involved in concentration and sorting of cargo proteins of the multivesicular body (MVB)"] [UniProt:Q8WUM4 "Adapter for a subset of ESCRT-III proteins, such as CHMP4"].
- Katoh et al. identified the ALIX-CHMP4 connection in the endocytic/MVB pathway and concluded that "CHMP4b and Alix participate in formation of multivesicular bodies by cooperating with SKD1" [PMID:12860994 "CHMP4b and Alix participate in formation of multivesicular bodies by cooperating with SKD1"].
- Dores et al. support cargo-specific MVB/lysosomal sorting: activated PAR1 sorts into MVB ILVs through an ALIX/ESCRT-III pathway independent of receptor ubiquitination, and "ALIX binds to a YPX3L motif of PAR1 and recruits ESCRT-III to mediate MVB/lysosomal sorting" [PMID:22547407 "ALIX binds to a YPX3L motif of PAR1 and recruits ESCRT-III to mediate MVB/lysosomal sorting"].
- Baietti et al. support the exosome role: syntenin interacts with ALIX and "Syntenin exosomes depend on the availability of heparan sulphate, syndecans, ALIX and ESCRTs" [PMID:22660413 "Syntenin exosomes depend on the availability of heparan sulphate, syndecans, ALIX and ESCRTs"].
- Morita et al. support the cytokinesis/midbody role. The abstract states that the "ESCRT-III-binding protein Alix is recruited to the midbody of dividing cells through binding Cep55" and that interfering with Alix/Cep55/ESCRT-III/TSG101 strongly inhibits cytokinesis [PMID:18641129 "ESCRT-III-binding protein Alix is recruited to the midbody of dividing cells through binding Cep55"].
- Viral budding is well supported as a pathogen-exploitation context. Earlier HIV/EIAV work found that "interactions between ESCRT-I and ESCRT-III are bridged by AIP-1/ALIX" and that EIAV YPDL-type L-domain function depends on AIP-1/ALIX [PMID:14519844 "interactions between ESCRT-I and ESCRT-III are bridged by AIP-1/ALIX"].
- Murrow et al. support basal autophagy and endolysosomal trafficking. They found that ATG12-ATG3 interacts with ALIX and controls ALIX-mediated late endosome distribution, exosome biogenesis, and viral budding; they also state that "Alix is functionally required for efficient basal, but not starvation-induced, autophagy" [PMID:25686249 "Alix is functionally required for efficient basal, but not starvation-induced, autophagy"].

## Annotation decisions

- Accept as core: MVB assembly / MVB-lysosomal sorting, exosome biogenesis/assembly/secretion, macroautophagy or basal autophagic flux where tied to ALIX/ATG12-ATG3 endolysosomal function, cytokinesis/midbody abscission/Flemming body, and specific molecular functions such as calcium-dependent protein binding, proteinase activated receptor binding, and homodimerization when supported.
- Keep viral budding as non-core rather than the primary function. It is a strong microbial-infection/pathogen-hijacking context, but the endogenous ALIX roles are ESCRT adaptor functions in MVB/exosome/cytokinesis/autophagy.
- Mark GO:0005515 protein binding as over-annotated. The meaningful interactions are ALIX-CHMP4, ALIX-TSG101, ALIX-CEP55, ALIX-PAR1, ALIX-syntenin/syndecan, ALIX-ATG12-ATG3, ALIX-PDCD6, and viral late-domain binding, not generic protein binding.
- Retain the NOT annotations for nucleus organization, metaphase chromosome alignment, and mitotic spindle assembly as negated/non-core records; they should not be converted into positive PDCD6IP functions.
- Keep broad or peripheral locations/processes such as cytoplasm/cytosol, extracellular region, centrosome, melanosome, tight junction, focal adhesion, immunological synapse, ER exit site, membrane, actomyosin/tight-junction polarity, and centrosome duplication as non-core unless directly tied to the core ESCRT adaptor functions.
- Modify the obsolete ubiquitin-independent MVB protein-catabolism term to current MVB sorting/endolysosomal sorting wording while preserving the PAR1/ALIX-specific biology.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording framed the endogenous proteostasis-network core as ALIX-mediated ESCRT adaptor activity in endolysosomal/exosome and cytokinetic membrane-remodeling pathways.
