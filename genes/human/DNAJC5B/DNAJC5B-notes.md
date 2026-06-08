# DNAJC5B (Q9UF47) research notes

## Identity
- DnaJ homolog subfamily C member 5B; cysteine-string protein isoform beta (CSP-beta). Paralog of DNAJC5/CSPalpha.
- 199 aa. J domain (aa 19-84) [file:human/DNAJC5B/DNAJC5B-uniprot.txt "DOMAIN 19..84 /note=\"J\""]. Cysteine-string region downstream of J domain. Palmitoylated.
- Testis specific [uniprot "TISSUE SPECIFICITY: Testis specific"].

## Function / experimental data
- PMID:17034881 (Boal et al. 2007, BBA): CSP-beta interacts with the HSC70+SGTA chaperone complex; targeted to the trans-Golgi network as a non-palmitoylated CSP in clonal beta-cells; palmitoylation NOT required for membrane association.
- UniProt SUBUNIT: "Interacts with the chaperone complex consisting of HSC70 and SGTA." -> bona fide HSP70/HSC70 co-chaperone (like CSPalpha), but tissue-restricted (testis) and TGN-targeted.
- SUBCELLULAR LOCATION: Membrane; Lipid-anchor; may be associated with trans-Golgi network.

## Interactions (GOA)
- protein binding IPI with TFCP2 (Q12800) from PMID:25416956 (proteome-scale Y2H map). Uninformative HT interaction; partner is a transcription factor (CP2), not a chaperone client.

## Curation judgment
- Core MF: HSP70/HSC70 co-chaperone (Hsp70 protein binding) — supported by experimental HSC70/SGTA interaction.
- Membrane / cytoplasm localizations: ACCEPT/KEEP_AS_NON_CORE (membrane is lipid-anchored; TGN association).
- protein binding IPI (TFCP2): KEEP_AS_NON_CORE (uninformative HT).
