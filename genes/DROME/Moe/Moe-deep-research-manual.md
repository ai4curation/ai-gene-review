# Moe (Moesin, P46150) - manual literature synthesis

No deep-research API was available for this session. This file is a manual synthesis
written by the reviewer from the cached publications in `publications/` (abstracts,
plus full text where `full_text_available: true`) and the UniProt record
(`Moe-uniprot.txt`). Every assertion carries its source.

## Identity and family

- Moe encodes the single ERM (ezrin/radixin/moesin) protein of *Drosophila melanogaster*
  (578 aa canonical isoform J; several splice isoforms). [PMID:12511959 "the sole Drosophila
  ERM protein Moesin"]
- Domain architecture: N-terminal FERM domain (1-296), alpha-helical linker, and C-terminal
  ERM_C (C-ERMAD) actin-binding domain; the conserved activating phospho-site is Thr559.
  [UniProt FT DOMAIN 1..296 FERM; Pfam PF00769 ERM_C; CC PTM "Phosphorylated on Thr-559"]
- PANTHER family PTHR23281 (MERLIN/MOESIN/EZRIN/RADIXIN); Merlin (Mer) is the only other
  family member in fly. [UniProt DR PANTHER]

## Molecular activities

- **Actin binding / membrane-actin linkage.** ERM proteins "are thought to constitute a
  bridge between the actin cytoskeleton and the plasma membrane (PM)", and Dmoesin "is
  required during oogenesis for anchoring microfilaments to the oocyte cortex"
  [PMID:12360288]. Moe "has the ability to bind to and organize cortical F-actin"
  [PMID:23468526].
- **PI(4,5)P2 binding.** "PtdIns(4,5)P(2) binding is essential for moesin recruitment to
  the membrane and for its subsequent phosphorylation" [PMID:20519583].
- **Activation by phosphorylation.** Slik phosphorylates/activates Moe at mitosis
  [PMID:18283112 "Mitosis onset is characterized by a burst of moesin activation mediated by
  a Slik kinase-dependent phosphorylation"]; Rho-kinase can phosphorylate T559 in vitro
  [PMID:16887114]; PP1beta/Flapwing dephosphorylates Moe [PMID:22133918]. Slik and the FGFR
  Breathless activate Moe at the luminal membrane of tracheal terminal cells [PMID:25061859].
- **Microtubule binding.** "Moesin directly binds to microtubules in vitro and stabilizes
  microtubules at the cell cortex in vivo", via two conserved FERM-domain lysines (K212,213)
  [PMID:23857773].
- **Partner recruitment (adaptor).** Moe binds the RhoGAP Conundrum through its FERM domain
  and "recruits it to the cell cortex to negatively regulate RhoA activity" [PMID:23468526];
  binds the TNFR Wengen juxtamembrane domain [PMID:23544124]; binds TRP/TRPL channels in the
  dark [PMID:16216927]; binds PCID2 in the nucleus [PMID:28554770].

## Cellular roles

- Cortical actin organization and epithelial apical-basal polarity; Moe acts by
  antagonizing Rho1 rather than purely structurally [PMID:12511959 "Moesin facilitates
  epithelial morphology not by providing an essential structural function, but rather by
  antagonizing activity of the small GTPase Rho"].
- Mitotic cortex: Moe is required for cortical rigidity, rounding and spindle morphogenesis
  [PMID:18207738; PMID:18283112].
- Photoreceptors: structural role in rhabdomere (apical microvillar membrane) morphogenesis
  [PMID:14724125 "Our results show an essential structural role for Moesin in photoreceptor
  morphology"]; light-regulated association with TRP/TRPL needed for photoreceptor
  maintenance [PMID:16216927].
- Oocyte: anchoring microfilaments to the oocyte cortex, needed for oskar/germ plasm
  anchoring and A/P polarity [PMID:12360288; PMID:12498700].
- Tracheal terminal cells: Btsz recruits activated Moe to luminal membrane for luminal
  actin integrity [PMID:24413568]; endocytosis limits apical p-Moe to constrain seamless tube
  shape [PMID:25065756].
- Nucleus: Moe is recruited to active transcription sites and participates in mRNA export
  with PCID2 [PMID:28554770]; it is also dynamically nuclear in mitosis [PMID:19592131].
- R8 photoreceptor axon targeting with Wengen [PMID:23544124].

## Caveats noted

- PMID:8666669 (McCartney & Fehon 1996) is mostly a localization paper; in the full text
  (PMC2120840) the Moe-Armadillo/Merlin relationship is colocalization ("data not shown"),
  and F-actin binding is inferred from colocalization and sequence homology.
- PMID:25065756 shows endocytosis acting upstream of p-Moe ("heterozygosity for Moe did not
  appear to bypass the requirement for Syx7 in early endocytosis"), not Moe promoting
  endocytosis.
- PMID:16216927 contains no electrophysiological measurement of photoreceptor membrane
  potential in Moe mutants; it reports co-IP, light-dependent translocation and
  light-induced degeneration.
