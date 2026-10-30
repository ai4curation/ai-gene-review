# SERCA (Ca-P60A, CG3725; UniProt P22700) - manual literature synthesis

No deep-research API was available for this session. This file is a manual synthesis written by
the reviewer from the cached publications in `publications/` and the UniProt record
(`SERCA-uniprot.txt`). Every assertion carries provenance.

## Identity and family

- Drosophila SERCA (FlyBase FBgn0263006, GeneID 49297; synonyms Ca-P60A, CaP60A, CG3725) is the
  single sarco/endoplasmic reticulum Ca2+-ATPase of the fly. Cloned by Magyar and Varadi:
  [PMID:2148477 "It consists of 1002 amino acids with all the characteristic features of the P-type ATPases. It shows 67-71% amino acid identity and an apparently identical hydropathy profile with the mammalian sarco/endoplasmic reticulum-type Ca2(+)-ATPases."]
- It is the only SERCA expressed in flies: [PMID:23434461 "knockdown of Ca-P60A, the only SERCA expressed in Drosophila"].
- UniProt: [UniProt P22700 "Belongs to the cation transport ATPase (P-type) (TC 3.A.3)"];
  NCBIfam TIGR01116 (ATPase-IIA1_Ca, the SERCA-type P2A calcium ATPase family); 10 TM helices
  (UniProt TRANSMEM features), catalytic phospho-Asp at residue 351 (FT ACT_SITE 351), Ca2+ site
  residues in TM4-TM8 (FT BINDING).
- Reaction: [UniProt P22700 "Reaction=Ca(2+)(in) + ATP + H2O = Ca(2+)(out) + ADP + phosphate + H(+);"] (EC 7.2.2.10).

## Molecular function: P-type Ca2+ pump into the ER/SR

- [PMID:15520268 "SERCA, a sarco-endoplasmic reticulum calcium ATPase, being the main agent for calcium uptake into the ER, plays a central role in this process."]
- [PMID:24807223 "SERCA, an endoplasmic reticulum (ER) calcium pump, is solely responsible for transporting cytosolic calcium into the ER lumen."]
- Activity assays in flies: Ca2+-dependent, thapsigargin-sensitive ATP hydrolysis
  [PMID:28399403 "An SERCA activity assay that quantifies Ca2+-dependent ATP hydrolysis (Gehrig et al., 2012) revealed that loss of THADA leads to significantly elevated calcium-dependent SERCA activity both in flies"];
  reduced SERCA activity in DJ-1beta PD-model flies [PMID:33892078 "Our results showed that SERCA enzymatic activity is significantly reduced in DJ-1β mutant flies"].
- Thapsigargin binding site conserved [PMID:22952921 "The Drosophila serca gen has about 70% identity with the mammalian serca1, with which it shares identical binding sites for its inhibitor thapsigargin (Thg) [28]."].

## Regulators / partners

- Sarcolamban peptides SclA/SclB (smORF peptides; phospholamban/sarcolipin-like) regulate cardiac
  Ca2+ uptake [PMID:23970561 "Here, we describe two peptides of less than 30 amino acids regulating calcium transport, and hence influencing regular muscle contraction, in the Drosophila heart."];
  UniProt [UniProt P22700 "Interacts with SclA and SclB."].
- Seipin binds and promotes SERCA activity in fat body [PMID:24807223 "Seipin physically interacts with the sarco/endoplasmic reticulum Ca(2+)-ATPase (SERCA) in both Drosophila and man."].
- THADA binds SERCA and acts as an uncoupler [PMID:28399403 "THADA binds the sarco/ER Ca2+ ATPase (SERCA) and acts on it as an uncoupler."].

## Localization

- ER membrane and SR membrane [UniProt P22700 "Endoplasmic reticulum membrane"; "Sarcoplasmic reticulum membrane"], colocalizing with SclA/SclB at diads (PMID:23970561 via UniProt).
- Used as an ER marker in fat body and salivary gland [PMID:28399403 "SERCA, which is widely used as an ER marker, co-localizes with THADA in all tissues tested such as the fat body and salivary gland (Figure 2D)."].
- LOPIT organelle proteomics of embryos (PMID:19317464).

## Physiological roles (downstream of ER/SR Ca2+ uptake)

- Neuromuscular: conditional (kum) paralytic alleles [PMID:15520268 "At motor nerve terminals, SERCA inhibition retards calcium sequestration and reduces the amplitude of evoked excitatory junctional currents."]; muscle relaxation [PMID:15520268 "Conditional paralysis of SERCA mutants is also marked by prolonged neural activity-driven muscle contraction, thus reflecting the phylogenetically conserved role of SERCA in terminating contraction."].
- Photoreceptor synaptic exocytosis in the lamina depends partly on ER Ca2+ stores filled by SERCA [PMID:22952921 "These results strongly implicate ER Ca2+ release in photoreceptors exocytosis."].
- Heart: [PMID:24098595 "In contrast to prior work, we show that disruption of CaP60A in a cardiac specific manner results in cardiac dilation and dysfunction rather than alteration in heart rate."]; RyR mutation rescues kum170 cardiac phenotype [PMID:24098595 "the co-expression of a calcium release channel mutation with CaP60A (kum170) is sufficient to rescue the cardiac phenotype but not paralysis."].
- Flight circuit: InsP3R deficits compensated by reduced SERCA [PMID:16899722 "Decreased Ca2+ release in aminergic neurons during development of the flight circuit can be compensated by reducing Ca2+ uptake from the cytosol to intracellular stores."].
- Lipid storage in fat body [PMID:24807223 "Like dSeipin, dSERCA cell-autonomously promotes lipid storage in Drosophila fat cells."].
- Thermogenesis: in mammals uncoupled SERCA ATP hydrolysis generates heat; fly evidence is via THADA
  mutants [PMID:28399403 "SERCA uses the energy derived from ATP hydrolysis in part to translocate calcium from the cytosol into the ER, and in part to produce heat via a futile cycle (Reis et al., 2001)."].
- Notch signalling: SERCA loss impairs Notch receptor maturation/trafficking, affecting midgut stem
  cell differentiation and follicle cell programmes [PMID:23434461 "Of note, loss-of-function mutations in a Drosophila SERCA homolog, Ca-P60A, have been reported to produce Notch loss-of-function phenotypes in this model organism by altering Notch trafficking (Periz and Fortini, 1999)."];
  [PMID:26205122 "Ca-P60A positively regulates calcium-transporting ATPase activity for proper intracellular trafficking of the Notch receptor47."].
