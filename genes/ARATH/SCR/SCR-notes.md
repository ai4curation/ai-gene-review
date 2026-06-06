# SCR (SCARECROW) curation notes — Arabidopsis thaliana, UniProt Q9M384, AT3G54220

## Overview
SCR is a plant-specific GRAS-family transcriptional regulator. Core role: with the mobile
GRAS factor SHORT-ROOT (SHR), it controls the asymmetric (formative) cell division that
generates the cortex and endodermis, and it specifies/maintains the root quiescent centre (QC)
and surrounding stem-cell niche. It acts in a nuclear SHR–SCR heterodimer that recruits
BIRD/IDD zinc-finger transcription factors (JKD, MGP, NUC) to control ground-tissue patterning.

## Molecular function — DNA binding vs coregulator
Key point for MF curation: GRAS proteins including SHR–SCR are best characterised as transcription
cofactors that act through DNA-binding partners (BIRD/IDD zinc fingers), not as direct
sequence-specific DNA binders.

- [PMID:28211915 "Although GRAS proteins function in transcriptional regulation, only two GRAS proteins, OsSCL7 and Nodulation Signaling Pathway1 (NSP1) in Medicago truncatula, have been reported to bind DNA directly by EMSA analysis. In contrast, there is no evidence for direct binding of SHR-SCR or other GRAS proteins to DNA. We did not find any DNA-binding motifs in our structure of the SHR-SCR complex, which comprises an overall negatively-charged surface potentials ... unfavorable for binding to highly negatively-charged DNA."]
- [PMID:28211915 "These results suggest that SHR-SCR are transcriptional cofactors that regulate target gene transcription via binding of SHR to BIRD transcription factors."]
- The crystal structures (PDB 5B3G binary SHR-SCR; 5B3H ternary JKD-SHR-SCR) show JKD ZF3-ZF4 docks into a groove on SHR; SCR makes no direct contact with JKD. [PMID:28211915 "The JKD ZFs bind SHR, whereas no contacts were found with SCR"]
- SCR has its own groove corresponding to the SHR ZF-binding groove, suggesting SCR also binds partner proteins via this groove. [PMID:28211915 "SCR also possesses a deep groove corresponding to the JKD ZF-binding groove of SHR ... We speculate that SCR and probably other GRAS domain proteins interact with their partner proteins via their grooves."]

Implication: The MF annotations GO:0003700 (DNA-binding transcription factor activity, ISS/IMP)
and GO:0043565 (sequence-specific DNA binding, IDA from PMID:17446396) likely over-state a direct
DNA-binding activity for SCR. SCR/SHR bind target promoters (e.g. MGP, NUC, CYCD6;1) but the
structural and biochemical evidence (PMID:28211915) argues this is indirect, via BIRD/IDD partners.
The IDA "sequence-specific DNA binding" from PMID:17446396 (the SHR-sequestration paper, abstract
does not describe an EMSA/DNA-binding assay for SCR itself) is questionable; best treated as
over-annotation rather than core direct activity. The ISS GO:0003700 calls (PMID:11118137 genome-wide
TF survey; PMID:8756724 original cloning) derive from family/sequence classification of GRAS as
"putative transcription factors," appropriate as a broad classification but better expressed as
transcription regulator / coregulator given current evidence.

## Asymmetric cell division and radial patterning (core BP)
- Original cloning: scr mutant roots miss one cell layer due to disruption of the asymmetric
  division generating cortex and endodermis. [PMID:8756724 "The scarecrow mutation results in roots that are missing one cell layer owing to the disruption of an asymmetric division that normally generates cortex and endodermis."] SCR deduced as a putative TF, expressed in cortex/endodermal initial and endodermal lineage. [PMID:8756724 "The deduced amino acid sequence of SCARECROW (SCR) suggests that it is a member of a novel family of putative transcription factors."]
- SCR acts cell-autonomously in the ACD; autoregulates its own expression; limits SHR movement.
  [PMID:15314023 "we show that SCR acts cell-autonomously to control asymmetric cell division within the ground tissue. We provide evidence that SCR gene expression is under autoregulatory control, that SCR limits SHR movement"]
- Radial patterning common to root and shoot: scr loses ground-tissue layer in root, and starch
  sheath in hypocotyl/stem. [PMID:10631180 "both hypocotyl and shoot inflorescence also have a radial pattern defect, loss of a normal starch sheath layer, and consequently are unable to sense gravity in the shoot."]
- SHR/SCR/JKD/BIRDs throughout root growth control lineage identity, divisions and patterning.
  [PMID:26494755 "the BIRDs and SCARECROW regulate lineage identity, positional signals, patterning, and formative divisions throughout Arabidopsis root growth. These transcription factors are postembryonic determinants of the ground tissue stem cells and their lineage."]

## QC / stem-cell niche
- SCR required for QC specification and maintenance of surrounding stem cells (UniProt FUNCTION,
  PMID:12569126). QC and stem cells specified by parallel PLT and SHR/SCR routes.
  [PMID:29352064 "The QC and adjacent stem cells are specified by two parallel routes directed by the transcription factors PLETHORA (PLT) and SHORTROOT (SHR)/SCARECROW (SCR)"]

## Protein interactions (replace bare "protein binding")
- SHR (Q9SZF7 / AT4G37650): direct heterodimer partner; central to function.
  [PMID:17446396 "SCARECROW (SCR) blocks SHR movement by sequestering it into the nucleus through protein-protein interaction"]; structure [PMID:28211915 "the crystal structures of the SHR-SCR binary and JACKDAW (JKD)/IDD10-SHR-SCR ternary complexes ... form a head-to-head 1:1 heterodimer"]. Also Y2H confirmation [PMID:18500650 "we confirmed the protein-protein interaction between SHORT-ROOT (SHR) and SCARECROW (SCR)"].
- JKD (JACKDAW, Q700D2 / AT5G03150) and MGP (MAGPIE, Q9ZWA6 / AT1G03840): BIRD/IDD zinc-finger TFs;
  in the ternary complex JKD binds SHR (not SCR directly), but SHR-SCR-BIRD is the functional unit.
  [PMID:17785527 "JACKDAW and MAGPIE ... act in a SHR-dependent feed-forward loop to regulate the range of action of SHORT-ROOT and SCARECROW"]
- RBR1 (RETINOBLASTOMA-RELATED, Q9LKZ3): binds SCR directly via SCR's LxCxE motif (residues 295-299);
  this represses SHR-SCR target activation and constrains ACD to the niche.
  [PMID:22921914 "Spatial restriction of these divisions requires physical binding of the stem cell regulator SCARECROW (SCR) by the RETINOBLASTOMA-RELATED (RBR) protein."]; [PMID:22921914 "this interaction depends on the LxCxE motif in SCR."] Mutation LQCAE->AQCAA abolishes RBR1 interaction (UniProt MUTAGEN 295-299).
- AN3/GIF1 (AT5G26840): AN3/GIF coregulator complexes bind the SCR promoter region (SCR is a target,
  not necessarily a direct physical SCR partner). [PMID:29352064 "AN3 complexes bind directly to the promoter regions of PLT1 as well as SCARECROW"] — the GOA "protein binding" with AN3 (PMID:29352064) reflects this regulatory relationship; treat cautiously.
- GA2OX7 (Q9C6I4): a binary Y2H/interactome hit in the phytohormone protein network.
  [PMID:32612234 "a systems-level map of the Arabidopsis phytohormone signalling network, consisting of more than 2,000 binary protein-protein interactions."] Large-scale interactome; biological significance for SCR unestablished — keep but non-core/over-annotated.
- SCL23 (AT5G41920): redundant paralog with SCR in bundle-sheath fate; IGI partner.
  [PMID:24517883 "SCR and SCL23 are expressed specifically in the BS cells and act redundantly in BS cell-fate specification"]
- Cell-type-specific complexes confirmed in vivo by FRET-FLIM (SHR, SCR, JKD higher-order complexes).
  [PMID:28746306 "three fully functional fluorescently tagged cell fate regulators establish cell-type-specific interactions at endogenous expression levels and can form higher order complexes."]

## Maintenance of protein location in nucleus (SHR sequestration)
- SCR sequesters SHR in the endodermal nucleus, restricting SHR's intercellular movement to a single
  cell layer. [PMID:17446396 "SCR ... sequestering it into the nucleus through protein-protein interaction and a safeguard mechanism that relies on a SHR/SCR-dependent positive feedback loop for SCR transcription."] This supports GO:0051457 (maintenance of protein location in nucleus) for the SHR target. Note: the GOA NOT|protein homodimerization (GO:0042803, PMID:17446396) records that SCR does NOT homodimerize (it heterodimerizes with SHR).

## Gravitropism (shoot)
- SCR = SGR1; endodermis/starch sheath is the site of gravity perception in shoots; scr/sgr1 lacks
  shoot gravitropism. [PMID:10322541 "shoot gravitropism 1 (sgrl), which is allelic to scarecrow (scr) ... indicate that the endodermis is the site of gravity perception in shoots."] This is a downstream consequence of SCR's radial-patterning role (starch-sheath formation), not a distinct molecular function → non-core developmental/physiological output.

## Leaf bundle sheath / redox
- SCR + SCL23 + SHR control bundle-sheath cell fate; SCR involved in sugar transport in BS cells.
  [PMID:24517883 "mutations in three GRAS family transcription factors, SHORT-ROOT (SHR), SCARECROW (SCR) and SCARECROW-LIKE 23 (SCL23), affect BS cell fate"] → bundle sheath cell fate specification, leaf development = non-core (tissue-specific developmental outputs).
- SCR coordinates root elongation, endodermal differentiation, redox homeostasis and oxidative
  stress; scr accumulates ROS in the elongation zone (decreased Peroxidase 3). [PMID:34056773 "the scr mutant accumulated a higher level of reactive oxygen species (ROS) in the elongation zone, which is probably due to decreased expression of peroxidase gene 3"] → GO:0045454 cell redox homeostasis is acts_upstream_of_or_within (indirect, downstream physiological output), non-core.

## Localization
- Nucleus. UniProt SUBCELLULAR LOCATION: Nucleus. IDA nuclear localization in PMID:26494755 and
  PMID:15314023; SHR sequestration into the SCR-expressing nucleus (PMID:17446396). Accept nucleus.

## Domain architecture (UniProt)
- 653 aa; single C-terminal GRAS domain (281-650) with LHRI, VHIID, LHRII, PFYRE, SAW subdomains;
  N-terminal disordered region (1-69, 193-265); LxCxE motif at 295-299 (RBR1 binding).

## Action summary rationale
- Core MF: transcription coregulator/cofactor function via SHR heterodimer + BIRD/IDD recruitment.
  The existing set lacks a clean coregulator MF term and over-relies on direct DNA-binding terms.
- Core BP: asymmetric cell division / radial pattern formation / root development (QC + ground tissue).
- Non-core: gravitropism, bundle-sheath/leaf development, redox homeostasis, GA2OX7 interactome hit.
- protein binding (GO:0005515) IPI entries: uninformative; recommend replacing with specific partner
  capture (SHR especially) — per curation guidance, avoid bare protein binding.
