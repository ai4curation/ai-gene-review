# LRSAM1 — review notes

UniProt: Q6UWE0. Gene: LRSAM1 (also Tal, "Tsg101-associated ligase"). Human.

## Domain architecture
- N-terminal leucine-rich repeats (LRR; multiple REPEAT 30-172) — substrate/target recognition (required for localizing to intracellular bacteria).
- Coiled-coil regions (254-380, 510-562) — oligomerization/interaction.
- SAM (sterile alpha motif) domain (~569-632; UniProt DOMAIN) — protein interaction.
- C-terminal RING-type zinc finger (ZN_FING 675-710) — catalytic E3 ligase domain (required for generating the bacteria-associated ubiquitin signal).
[file:human/LRSAM1/LRSAM1-uniprot.txt FT records]

## Core function (synthesized)
LRSAM1 is a RING-type E3 ubiquitin ligase with two well-supported roles:
1. Xenophagy / antibacterial autophagy: LRSAM1 is the E3 ligase responsible for anti-Salmonella autophagy-associated ubiquitination. It localizes to cytosolic intracellular bacterial pathogens (via its LRRs) and generates the polyubiquitin signal around the bacteria (via its RING), recruiting autophagy adaptors and machinery for lysosomal degradation (xenophagy). Required for bacteria-associated ubiquitination but dispensable for ubiquitination of protein aggregates.
[PMID:23245322 "We identify LRSAM1 as the E3 ligase responsible for anti-Salmonella autophagy-associated ubiquitination. LRSAM1 localizes to several intracellular bacterial pathogens and generates the bacteria-associated ubiquitin signal; these functions require LRSAM1's leucine-rich repeat and RING domains, respectively."]
[file:human/LRSAM1/LRSAM1-uniprot.txt "Bacterial recognition protein that defends the cytoplasm from invasive pathogens ... generates the bacteria-associated ubiquitin signal leading to autophagy-mediated intracellular bacteria degradation (xenophagy)"]
2. ESCRT/TSG101 regulation (as "Tal"): LRSAM1 monoubiquitinates TSG101 at multiple sites, inactivating TSG101's ability to sort endocytic (EGFR) and exocytic (HIV-1 Gag) cargos; this regulates receptor endocytosis and retroviral budding.
[PMID:15256501 "Tal, a Tsg101-specific E3 ubiquitin ligase, regulates receptor endocytosis and retrovirus budding"]
[PMID:18077552 "Regulation of Tsg101 expression by the steadiness box: a role of Tsg101-associated ligase"]
[file:human/LRSAM1/LRSAM1-uniprot.txt "mediates monoubiquitination of TSG101 at multiple sites, leading to inactivate the ability of TSG101 to sort endocytic (EGF receptors) and exocytic (HIV-1 viral proteins) cargos"]

## Catalytic activity / E3 ligase
LRSAM1 has genuine intrinsic RING E3 ligase activity (EC 2.3.2.27); demonstrated autoubiquitination and substrate ubiquitination. Unlike adaptor-only F-box proteins, the RING is catalytic, so ubiquitin-protein transferase activity (GO:0004842) and ubiquitin protein ligase activity (GO:0061630) are CORE/correct.
[file:human/LRSAM1/LRSAM1-uniprot.txt "CATALYTIC ACTIVITY ... EC=2.3.2.27"]
[PMID:23245322; PMID:15256501]

## Regulation
PHF23 (PHD finger protein 23) promotes ubiquitination and degradation of LRSAM1, negatively regulating autophagy.
[PMID:25484098 "PHF23 ... negatively regulates cell autophagy by promoting ubiquitination and degradation of E3 ligase LRSAM1"]

## Localization
Cytoplasm, punctate distribution and a submembranal ring; relocalizes to intracellular bacterial pathogens.
[file:human/LRSAM1/LRSAM1-uniprot.txt SUBCELLULAR LOCATION]

## Disease
LRSAM1 mutations cause Charcot-Marie-Tooth disease type 2P (CMT2P), an axonal peripheral neuropathy.
[PMID:27615052 "A novel missense mutation of CMT2P alters transcription machinery"]

## Annotation judgments
- Core ACCEPT: ubiquitin protein ligase activity (GO:0061630 EXP/IDA), ubiquitin-protein transferase activity (GO:0004842 IDA), protein autoubiquitination (GO:0051865), protein polyubiquitination (GO:0000209), positive regulation of xenophagy (GO:1904417), cytoplasm localization.
- KEEP_AS_NON_CORE: TSG101/ESCRT-related: ubiquitin-dependent endocytosis (GO:0070086), negative regulation of endocytosis (GO:0045806), viral budding (GO:0046755), protein catabolic process (GO:0030163), membrane (GO:0016020); positive regulation of autophagosome assembly (GO:2000786, downstream of xenophagy ubiquitination); protein ubiquitination IEA (generic).
- ubiquitin protein ligase activity IEA from EC mapping (GO_REF:0000003): ACCEPT (correct, redundant with EXP).
- protein binding (GO:0005515) — KEEP_AS_NON_CORE (uninformative bare term; many high-throughput interactome PMIDs).
- The EC-based IEA is fine because LRSAM1 genuinely has the EC 2.3.2.27 activity.
