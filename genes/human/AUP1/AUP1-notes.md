# AUP1 (Ancient Ubiquitous Protein 1) — research notes

UniProt: Q9Y679 (AUP1_HUMAN), 410 aa. RecName now "Lipid droplet-regulating VLDL assembly factor AUP1".
HGNC:891. Chromosome 2.

## Domain architecture / topology
- Monotopic (hairpin) membrane protein. N-terminal hydrophobic region (~21-41) inserts as a hairpin so that BOTH termini face the cytosol. Dual-localizes to ER membrane and lipid droplet (LD) surface monolayer.
  [PMID:21127063 "AUP1 ... integrates into the LD surface in a monotopic fashion with both termini facing the cytosol"]
  [PMID:23197321 "AUP1 is inserted into the membrane of the ER in a monotopic hairpin fashion, and subsequently transported to the hemi-membrane of LDs"]
- A single N-terminal domain enables ER residence, monotopic insertion, and LD localization; a topology-changing mutation (PVG->LLL at 33-35) abolishes LD localization.
  [PMID:23197321 "A single domain localized in the N-terminal part of AUP1 enables its ER residence, the monotopic insertion, and the LD localization."]
- CUE domain (296-338): ubiquitin-binding (UBA-like). Required for interaction with ERAD machinery and misfolded substrates, ubiquitination, LD clustering, and AMFR binding; NOT required for LD localization.
  [file:human/AUP1/AUP1-uniprot.txt "The CUE domain is required for interaction with the ER quality control machinery and misfolded substrates, ubiquitination, lipid clustering and interaction with AMFR but is not required for localization to lipid droplets."]
- C-terminal G2BR (G2 binding region, ~379-410): binds and recruits the E2 conjugase UBE2G2. Distinct from CUE.
  [PMID:21127063 "AUP1 contains a C-terminal domain with strong homology to a domain known as G2BR, which binds E2 ubiquitin conjugases. We show that AUP1, by means of its G2BR domain, binds to Ube2g2."]

## Core molecular/cellular function: ERAD E2 adaptor
- AUP1 is a component of the mammalian HRD1-SEL1L ER quality control (ERAD) complex; depletion impairs degradation of misfolded ER proteins. Recruits the soluble E2 UBE2G2.
  [PMID:21857022 "Ancient ubiquitous protein 1 (AUP1) physically associates with the mammalian HRD1-SEL1L complex, and AUP1 depletion impairs degradation of misfolded ER proteins. One of the functions of AUP1 in ER quality control is to recruit the soluble E2 ubiquitin-conjugating enzyme UBE2G2."]
- Identified in the SEL1L-nucleated complex (SEL1L, AUP1, UBXD8/FAF2, UBC6e/UBE2J1, OS9) required for dislocation of misfolded glycoproteins.
  [PMID:18711132 "We identified AUP1, UBXD8, UBC6e, and OS9 as functionally important components of this degradation complex in mammalian cells"]
- CUE domain facilitates AUP1's interaction with the HRD1 complex and with dislocation substrates and regulates polyubiquitylation.
  [PMID:21857022 "the CUE domain of AUP1 regulates polyubiquitylation and facilitates the interaction of AUP1 with the HRD1 complex and with dislocation substrates"]
- Required for ERAD dislocation of NHK (null Hong Kong alpha-1-antitrypsin), confirming a role in retrograde ER-to-cytosol transport. [PMID:25660456]

## HMGCR / sterol-regulated ERAD on LD-associated ER membranes
- AUP1 recruits UBE2G2 (Ubc7) to lipid droplets and facilitates its binding to the E3s gp78/AMFR and Trc8/RNF139, driving sterol-induced ubiquitination of HMGCR and its ERAD. Also required for ERAD of INSIG1, SREBF1, SREBF2.
  [PMID:23223569 "Aup1 recruits the ubiquitin-conjugating enzyme Ubc7 to lipid droplets and facilitates its binding to both gp78 and Trc8."]
  [PMID:23223569 "RNAi-mediated knockdown of Aup1 blunts sterol-accelerated ubiquitination of reductase ... and subsequent ERAD of the enzyme. In addition, Aup1 knockdown inhibits ERAD of Insig-1 ... as well as that of membrane-bound precursor forms of sterol-regulatory, element-binding protein-1 and -2"]
- UBE2G2 interaction maps to the C-terminal G2BR (mutagenesis of L386, K390, L393, R400, R404 abolishes interaction). [file:human/AUP1/AUP1-uniprot.txt]

## Lipid droplet biology
- AUP1 expression level affects abundance of cellular LDs; first LD-regulatory protein linked to ER quality control.
  [PMID:21857022 "The AUP1 expression level affects the abundance of cellular lipid droplets and as such represents the first protein with lipid droplet regulatory activity to be linked to ER quality control."]
- Monoubiquitinated AUP1 (CUE-dependent) on the LD surface induces LD clustering; likely homophilic/heterophilic ubiquitin-mediated interaction.
  [PMID:24039768 "We show that the lipid droplet protein AUP1 induces cluster formation. A fraction of AUP1 is monoubiquitinated at various lysine residues. This process depends on its internal CUE domain"]
  [PMID:24039768 "The data indicate that monoubiquitinated AUP1 on the lipid droplet surface specifically induces clustering"]
- Hepatic VLDL assembly/secretion and APOB stability: AUP1 is a key determinant; interacts with APOB. [PMID:28183703]

## Other / contextual
- Integrin alpha cytoplasmic-tail binding (yeast two-hybrid; low affinity Kd ~90 uM), proposed inside-out signaling in platelets. Reported as cytoplasmic in that early study (before LD/ER role established). Contextual, not core.
  [PMID:12042322 "identified a protein, ancient ubiquitous protein 1 (Aup1) ... Binding study with an alpha(IIb) cytoplasmic tail peptide and glutathione S-transferase-Aup1 fusion protein revealed a low affinity (K(d) = 90 microm)."]
- Dengue/flavivirus (microbial infection): DENV NS4A binds AUP1, relocates it from LDs to autophagosomes, triggers lipophagy to drive virus production. Host-virus, non-core for normal physiology.
  [file:human/AUP1/AUP1-uniprot.txt "Following Dengue virus infection, required for induction of lipophagy which facilitates production of virus progeny particles."]
  [file:human/AUP1/AUP1-uniprot.txt "Upon Dengue virus infection, relocates from lipid droplets to autophagosomes."]
- Extracellular exosome / generic membrane: high-throughput proteomics localizations (HDA). Non-core.

## Assessment summary (core vs non-core)
- CORE: ER membrane location; LD location; ERAD pathway; ubiquitin-conjugating enzyme binding (UBE2G2 recruitment); ubiquitin protein ligase binding (gp78/AMFR, Trc8); ubiquitin binding (CUE); lipid droplet organization/formation; protein localization to LD; retrograde ER-to-cytosol transport.
- NON-CORE / contextual: autophagosome + lipophagy + response to virus (DENV-specific); VLDL/APOB (tissue-specific hepatic); integrin binding (early, low-affinity).
- OVER-ANNOTATED / uninformative: protein binding (GO:0005515) generic IPI; extracellular exosome; generic membrane.

## protein binding IPI references
- PMID:22119785 (ERAD network mapping), PMID:23840749 (MOR interactome Y2H), PMID:32296183 (binary interactome), PMID:29902443 (DENV NS4A). The 29902443 protein-binding maps to the specific NS4A interaction (host-virus); others are generic.
