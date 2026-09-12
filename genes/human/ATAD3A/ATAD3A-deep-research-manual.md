# ATAD3A manual deep research synthesis

Falcon deep research was requested but timed out after 600 seconds, and the configured Perplexity fallback failed with an insufficient-quota 401 error. This manual synthesis is therefore based on the cached UniProt record, GOA, local publication cache, and the Proteostasis PN projection report.

Manual synthesis decision: ATAD3A is not currently supported as a direct mitophagy cargo-marking or PINK/PRKN pathway factor.

## Core function

ATAD3A encodes a mitochondrial AAA+ ATPase located mainly at the mitochondrial inner membrane, enriched near inner/outer membrane contact sites and associated with mitochondrial nucleoids. The core evidence supports mitochondrial organization, ATP hydrolysis, mitochondrial nucleoid organization, mtDNA maintenance, and support of mitochondrial protein synthesis.

Key support:

- PMID:20154147 shows membrane topology and mitochondrial organization functions. The abstract states that "The N-terminal domain interacts with the OM" and that a "central transmembrane segment (TMS) anchors the protein in the IM and positions the C-terminal AAA(+) ATPase domain in the matrix." It also states that "ATAD3A regulates dynamic interactions between the mitochondrial OM and IM sensed by the cell fission machinery."
- PMID:17210950 identifies ATAD3 as a nucleoid-associated AAA+ protein. The abstract reports that "human ATAD3 is a component of many, but not all, mitochondrial nucleoids" and that ATAD3 RNAi "altered the structure of mitochondrial nucleoids and led to the dissociation of mitochondrial DNA fragments held together by protein, specifically, ones containing the D-loop region."
- PMID:22453275 links ATAD3 to mitochondrial protein synthesis. The abstract reports that "Both proteins are demonstrated to be required for mitochondrial protein synthesis in human cultured cells, and the major binding partner of ATAD3 is the mitochondrial ribosome." It further states that altered ATAD3 expression perturbs mtDNA maintenance and replication.

## Context-specific functions

ATAD3A also participates in several context-specific mitochondrial signaling settings. PMID:39116259 reports that ATAD3A interacts with PERK during ER stress, forms mitochondria-ER contact sites, and attenuates local PERK signaling to preserve mitochondrial protein synthesis. These observations support the existing PERK inhibitor and mitochondria-associated ER membrane contact-site annotations, but they are not the central evolved function of ATAD3A.

PMID:37832546 places ATAD3A in the response to mitochondrial DNA breaks. The paper reports that mtDSBs trigger an integrated stress response via DELE1 and HRI and identifies ATAD3A as potentially relaying signals from impaired mitochondrial genomes to the inner membrane. This supports HRI-mediated/integrated stress response signaling more directly than a generic DNA damage response term.

PMID:31522117 supports a role in mitochondrial antiviral innate immune signaling through a prohibitin/CLPB/MAVS/AKAP1/ATAD3A scaffold. This is plausible and experimentally supported, but it is context-specific relative to the core mitochondrial organization/nucleoid/translation role.

PMID:20332122 supports mitochondrial localization, cell growth, and anti-apoptotic phenotypes in lung adenocarcinoma cells. These are retained as non-core phenotypic or disease-context annotations.

## Proteostasis PN projection

The Proteostasis PN projection file maps ATAD3A to GO:0000423 mitophagy from a PINK/PRKN mitophagy cargo-marking category. I reviewed this conservatively and did not add mitophagy as a proposed new term. The strongest ATAD3A literature does not show ATAD3A acting as a mitophagy receptor, PINK1/PRKN cargo-marking factor, mitochondrial ubiquitination factor, LC3 recruitment factor, or direct executor of mitochondrial autophagic clearance.

PMID:30914652 provides important mitochondrial dynamics evidence and mentions disease-associated mitochondrial damage/mitophagy context, but the direct ATAD3A findings are Drp1 interaction, ATAD3A oligomerization, mitochondrial fragmentation, mtDNA lesion, bioenergetic defects, and cell death. That evidence is insufficient for a direct mitophagy annotation.

Recommended expert question: Does endogenous ATAD3A have any direct PINK1/PRKN-dependent cargo-marking, receptor-regulatory, or mitophagic-flux role that is separable from secondary consequences of mitochondrial fragmentation and mtDNA damage?
