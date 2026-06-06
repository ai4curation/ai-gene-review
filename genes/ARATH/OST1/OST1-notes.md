# OST1 / SRK2E / SnRK2.6 (Arabidopsis thaliana, AT4G33950, UniProt Q940H6) — review notes

## Identity and family
- Serine/threonine-protein kinase SRK2E; aka OPEN STOMATA 1 (OST1), SNF1-related kinase 2.6 (SnRK2.6). 362 aa, MW ~41 kDa. EC 2.7.11.1.
- Subclass III SnRK2 (with SnRK2.2/SRK2D and SnRK2.3/SRK2I); these three are the key positive regulators of ABA signaling [PMID:22090030 "Subclass III consists of SnRK2.6 (SnRK2E), SnRK2.3 (SnRK2I), and SnRK2.2 (SnRK2D), which play a redundant role as positive regulators of ABA signaling."].
- Protein kinase domain 21–277; ATP binding 27–35 and 50; active-site (proton acceptor) Asp-140; activation loop 160–186 (Ser-175 phospho crucial). C-terminal regulatory domain split into Domain I (osmotic, 283–318) and Domain II (ABA / ABI1 binding, 319–362) [PMID:16365038].

## Core molecular function — ABA-activated Ser/Thr protein kinase
- ABA-activated protein kinase; ost1 mutants impaired in ABA-induced stomatal closure [PMID:12468729 "OST1 is an ABA-activated protein kinase related to the Vicia faba ABA-activated protein kinase (AAPK)"].
- p44 (= SRK2E) activated by ABA and low humidity; srk2e mutant wilty due to loss of stomatal closure [PMID:12514244 "the p44 is encoded by a SnRK2-type protein kinase gene, SRK2E. The srk2e mutation resulted in a wilty phenotype mainly due to loss of stomatal closure in response to a rapid humidity decrease."].
- Phosphorylates and activates the S-type anion channel SLAC1 [PMID:19955427 "the OST1 kinase interacts with the SLAC1 anion channel, leading to its activation via phosphorylation."].
- Activation requires autophosphorylation; inhibited by group A PP2Cs [PMID:22090030 "Activation of SnRK2s requires autophosphorylation ... inhibited by group A PP2Cs"]. Ser-175 autophosphorylation crucial for kinase activity (UniProt PTM).
- Substrates: SLAC1 anion channel, KAT1 K+ channel, AtrbohF NADPH oxidase, AREB/ABF bZIP TFs, AKS1 bHLH TFs, MAPKKK18.
  - AtrbohF: [PMID:19716822 "OST1 phosphorylates Ser13 and Ser174 on AtrbohF ... OST1 physically interacts with AtrbohF"].
  - AREB1/ABFs phosphorylated in vitro; co-localize/interact in nuclei [PMID:19880399 "The AREB1 protein is phosphorylated in vitro by ABA-activated ... SRK2E/SnRK2.6 ... SRK2D/E/I and AREB1 co-localize and interact in nuclei in planta"].

## Biological processes
- Positive regulator of ABA-activated signaling pathway / stomatal closure in response to drought, darkness, high CO2, pathogens, low humidity [UniProt FUNCTION; PMID:30361234].
- Response to water deprivation / drought: srk2e wilty; SRK2D/E/I triple mutant drought-hypersensitive [PMID:12514244; PMID:19880399 "srk2d srk2e srk2i (srk2d/e/i) triple mutants exhibit greatly reduced tolerance to drought stress and highly enhanced insensitivity to ABA"].
- Osmotic stress / salt stress: SnRK2s activated by hyperosmotic/saline stress [PMID:15292193]; SnRK2 decuple mutant shows in-vivo osmotic-stress importance [PMID:21220313].
- Acts upstream of ROS production in guard cells [PMID:12468729 "OST1 acts in the interval between ABA perception and ROS production"; PMID:15064385].
- Stomatal innate immunity (PAMP-triggered stomatal closure against bacteria) requires guard-cell OST1 [PMID:16959575 "Stomatal guard cells of Arabidopsis perceive bacterial surface molecules, which requires the FLS2 receptor, production of nitric oxide, and the guard-cell-specific OST1 kinase"].
- CO2 / darkness-induced stomatal closure delayed in ost1 [PMID:30361234 "Delayed CO(2)-mediated and darkness-induced and reduced abscisic acid (ABA)-triggered stomatal closure"].
- Sucrose metabolism / fatty-acid desaturation / triglyceride (seed oil) / leaf growth: SnRK2.6 overexpression increases Suc synthesis and fatty acid desaturation; knockout reduces seed oil [PMID:20200070 "Inactivation of this gene reduced oil synthesis in Arabidopsis ... seeds, whereas its overexpression increased Suc synthesis and fatty acid desaturation in the leaves"]. These are pleiotropic/non-core metabolic effects of a broadly expressed kinase.

## Regulators / interactors (mostly upstream regulation, not OST1 MF)
- Negatively regulated by group A PP2Cs: ABI1, ABI2, PP2CA/AHG3, HAB1 — physical interaction and dephosphorylation [PMID:16365038 (ABI1, Domain II); PMID:19955427 (PP2CA); PMID:22090030 (ABI1 structure); UniProt SUBUNIT].
- ABA receptors PYR/PYL/RCAR inhibit PP2Cs to de-repress OST1 (core ABA signalosome).
- TOPP1/PP1 + Inhibitor-2 negatively regulate [PMID:26943172]; PIA1 phosphatase [PMID:37514328].
- RAF15 (B3-Raf MAP3K) acts upstream in guard cells [PMID:37226855 "RAF15-SnRK2.6/OST1 kinase cascade in guard cells"].
- SnRK2-interacting calcium sensors (SCS) negatively regulate [PMID:31699848].
- GHR1 receptor-like pseudokinase required for stomatal closure / SLAC1 activation context [PMID:30361234].
- MAP4K1/MAP4K2 upstream in ABA/Ca2+ stomatal closure; OST1 cytosolic localization shown [PMID:41417897].

## Subcellular location
- Nucleus (IDA) [PMID:26852793 associates with MAPKKK18 in nucleus; PMID:19880399 nuclei interaction with AREB1]. UniProt: Nucleus.
- Cytoplasm / cytosol (IDA) [PMID:19880399; PMID:41417897 cytosol IDA]. Functions in guard cell cytoplasm/at plasma membrane microdomains where SLAC1 acts.
- Plasma membrane (HDA proteomics, PMID:28887381) — consistent with action on plasma-membrane anion channel SLAC1.
- NOT cytosol (RCA, PMID:21166475): a computational/proteomic-prediction negation from a cytosolic-proteome study. This is contradicted by experimental IDA cytosol/cytoplasm evidence (19880399, 41417897). The RCA "NOT" should be treated with low confidence / removed; OST1 is genuinely cytoplasmic.

## Notes on specific annotation issues
- Many GO:0005515 "protein binding" IPI annotations come from IntAct/TAIR for individual interactors (ABI1, ABI2, PP2CA, HAB1, SLAC1, RBOHF, SAG113, ABF2, HT1, EDL2, AKS1/bHLH, MAPKKK18, RAF15, SCS, PIA1, MAP4K). Bare "protein binding" is uninformative; replace with the kinase MF and, where warranted, more specific MF (protein phosphatase binding GO:0019903 is already present for PP2CA; ion channel regulator activity GO:0099106 present for SLAC1).
- GO:0009931 "calcium-dependent protein serine/threonine kinase activity" (ISS, PMID:12468729) is INCORRECT: OST1/SnRK2.6 is calcium-INDEPENDENT. SnRK2s were explicitly characterized as calcium-independent kinases [PMID:15292193 "Several calcium-independent protein kinases were activated by hyperosmotic and saline stresses"]. The ISS to a calcium-dependent kinase class (CDPK) is a misannotation.
- GO:0042802 "identical protein binding" — OST1 homodimer in IntAct (self Q940H6) and ABI2-associated; weak/uninformative; OST1 functions as a monomeric kinase, no established functional homodimer. Mark as over-annotated.
- GO:0099106 "ion channel regulator activity" (IDA, PMID:19955427) — supported: OST1 activates SLAC1; informative non-kinase-catalysis MF describing its regulation of the anion channel. Accept (KEEP as non-core relative to kinase activity, but it is a real, specific MF — accept).
- Metabolic-process terms (sucrose, triglyceride, unsaturated fatty acid, leaf development) from PMID:20200070 are pleiotropic over-expression/knockout phenotypes of a broadly expressed kinase; keep as non-core.

## Core function summary
1. ABA-activated Ser/Thr protein kinase (protein serine/threonine kinase activity; EC 2.7.11.1; ATP binding) — autophosphorylates and phosphorylates downstream targets. Core.
2. Positive regulator of the ABA-activated signaling pathway -> regulation of stomatal closure / response to water deprivation / drought tolerance. Core biological role.
3. Activation of the guard-cell S-type anion channel SLAC1 (ion channel regulator activity) driving stomatal closure. Core.

## Deep research synthesis (Falcon / Edison Scientific report, 2026-06-06)

Source: `OST1-deep-research-falcon.md` (provider: falcon). Used to corroborate and strengthen existing annotation decisions; no decisions were reversed. Key additional findings and provenance:

- Catalytic mechanism restated explicitly: OST1 transfers phosphate from ATP to Ser/Thr residues of downstream effectors, antagonized by PP2C dephosphorylation [falcon "OST1/SRK2E/SnRK2.6 is an ABA-activated Ser/Thr protein kinase that transfers phosphate from ATP to serine/threonine residues on downstream effectors in ABA, osmotic-stress, and guard-cell signaling pathways; PP2C phosphatases antagonize this by dephosphorylation"]. Added as supporting_text to GO:0004674, GO:0005524 (ATP binding), and core function 1.
- Canonical PYR/PYL-PP2C-SnRK2 module reaffirmed: "In the absence of ABA, PP2Cs inhibit SnRK2s; ABA perception relieves this inhibition, enabling kinase activation and phosphorylation of downstream targets." Added to GO:0009738 (ABA-activated signaling pathway).
- SLAC1 activation: "OST1 interacts with SLAC1 and activates it via phosphorylation, linking ABA signaling to anion efflux and stomatal closure" (Lee 2009, Geiger 2009). Brandt 2012 functional-site evidence: SLAC1 S120A prevents activation by OST1. Added to GO:0099106 and core function 3.
- PP2CA acts at multiple nodes: "PP2CA inhibits SLAC1 and also physically interacts with OST1 to inhibit the kinase" — supports GO:0019903 protein phosphatase binding.
- RBOHF/RBOHD substrate residues compiled: OST1 phosphorylates RBOHF (Ser13, Ser174) and RBOHD (Ser343, Ser347; also Ser163); "These phosphorylation events are linked to ROS production in guard cells and stomatal closure." Added to GO:2000377 (regulation of ROS metabolic process).
- Dual activation modes reaffirmed: "Yoshida et al. showed SRK2E/OST1 is activated in vivo by both ABA and osmotic stress" with osmotic activation being ABA-independent. Added to GO:0006970 (response to osmotic stress).
- Localization: functional/interaction evidence places OST1 at plasma-membrane-proximal complexes with SLAC1 ("OST1 forms complexes with plasma membrane-localized SLAC1...") and in nuclear-proximal functions ("OST1 is also implicated in nuclear-proximal functions through phosphorylation of transcriptional regulators and chromatin-associated proteins"). Added to GO:0005634 (nucleus).
- Physiological synthesis: "OST1 is a core positive regulator of ABA-induced stomatal closure, drought and osmotic-stress responses, ROS production in guard cells, and broader stress signaling." Added to GO:0009414 (water deprivation) and GO:0090333 (stomatal closure).

New/expanded biology in the report not yet annotatable as core OST1 GO terms (no verified GO ID; kept as context only, NOT added):
- Compartmentalized SnRK2 signaling: prolonged ABA drives N-glycosylation-dependent nucleus-to-peroxisome relocalization of SnRK2.2/2.3 (Lu 2024), but this is explicitly NOT yet assigned to OST1/SnRK2.6 — not annotated.
- Additional reported direct targets (review-synthesized, not primary-extracted): CNGC5/6/9/12, KAT1, QUAC1, PIP2;1, BRM, ICE1, PUB25/26, AtANN1. These remain candidate substrates; no new GO term added.
- PTM regulation of OST1: S-nitrosylation by NO negatively regulates OST1 (Yastreb 2024 review). Candidate suggested_question/experiment, not annotated.

No UNDECIDED actions were present; none required resolution. No NEW annotation added (no clearly missing function with a verifiable GO ID from existing GOA/UniProt). Status kept DRAFT.
