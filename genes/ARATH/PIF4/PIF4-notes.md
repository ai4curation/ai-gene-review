# PIF4 (Arabidopsis thaliana) research notes

UniProt: Q8W2F3 (PIF4_ARATH); locus AT2G43010; synonyms BHLH9/AtbHLH9/bHLH009, EN102, SRL2 (short under red-light 2).
430 aa bHLH transcription factor; bHLH domain at residues 257-306; multiple disordered/low-complexity regions. Two isoforms (Long Q8W2F3-1 displayed; Short Q8W2F3-2 truncates the bHLH/C-terminus and is likely non-functional as a TF).

## Core identity / function
PIF4 (Phytochrome-Interacting Factor 4) is a nuclear basic helix-loop-helix (bHLH) transcription factor of the PIF subfamily (bHLH subgroup 15). It binds G-box (CACGTG) and E-box (CAYGTG) DNA motifs in light-regulated promoters and is a central integrator of light and temperature signals that drives cell-elongation growth (notably hypocotyl elongation).

- Discovered as SRL2 mutant; encodes a phyB-interacting bHLH that acts as a negative regulator of phyB signaling. [PMID:12006496 "The SRL2 gene encodes a bHLH factor, designated PIF4 (phytochrome-interacting factor 4), which binds selectively to the biologically active Pfr form of phyB, but has little affinity for phyA"]
- Nuclear localization and G-box DNA binding established in the same study. [PMID:12006496 "PIF4 localizes to the nucleus and can bind to a G-box DNA sequence motif found in various light-regulated promoters"]
- UniProt FUNCTION: "Transcription factor acting negatively in the phytochrome B signaling pathway. May regulate the expression of a subset of genes involved in cell expansion by binding to the G-box motif".

## Light signaling
- phyB (Pfr) binds PIF4 and promotes its degradation; PIF4 acts negatively/selectively in phyB signaling. [PMID:12006496]
- PIF7/PIF3/PIF4 modulate phyB levels under prolonged red light. [PMID:18252845]
- CRY1 and CRY2 (blue-light photoreceptors) directly interact with PIF4 (and PIF5) and activate PIF4 to drive growth in low blue light (LBL). [PMID:26724867 "CRY1 and CRY2 perceive this change and respond by directly contacting two bHLH transcription factors, PIF4 and PIF5"] PIF4/PIF5 are necessary for LBL-induced hypocotyl growth and act downstream of CRY1/CRY2; CRY-PIF complexes occupy overlapping promoter regions by ChIP-seq. [PMID:26724867 "the bHLH transcription factors (TFs) PIF4 and PIF5 are necessary for LBL-induced hypocotyl growth, and that they act downstream of CRY1 and CRY2"]
- Cryptochrome1 represses PIF4 expression; low blue light releases this to enhance phototropism. [PMID:32554507]

## Thermomorphogenesis (a major, well-established role)
- PIF4 is the central thermoregulator driving warm-temperature growth (thermomorphogenesis). [PMID:33824329 "Daytime warm temperature elicits thermomorphogenesis in Arabidopsis by stabilizing the central thermoregulator PHYTOCHROME INTERACTING transcription FACTOR 4 (PIF4), whose degradation is otherwise promoted by the photoreceptor and thermosensor phytochrome B"]
- PIF4 protein is stabilized in daytime by RCB/HMR; phyB otherwise promotes its degradation. [PMID:33824329]
- PIF4 + co-activator HEMERA (HMR) activate auxin biosynthesis/signaling genes to drive thermosensory hypocotyl elongation; requires Mediator subunit MED14. [PMID:36063057 "PIF4 and its co-activator HEMERA (HMR) promote plant thermosensory growth by activating genes involved in the biosynthesis and signaling of the phytohormone auxin"; "PIF4 plays a central role in regulating thermomorphogenetic hypocotyl elongation"]

## Auxin
- PIF4 (with PIF5) directly controls expression of auxin biosynthesis and auxin signaling genes to promote elongation growth under changing light. [PMID:22536829 "PIF4 and PIF5 regulate elongation growth by controlling directly the expression of genes that code for auxin biosynthesis and auxin signaling components"]
- PIF4 is required for cytokinin-induced upregulation of auxin biosynthesis genes (CKRC1/TAA1, CKRC2/YUC8); PIF4 transcription itself induced by cytokinin. [PMID:27827441 "the phytochrome-interacting factor 4 (PIF4) is required for this upregulation"]

## Protein-protein interactions (informative partners; the GO:0005515 "protein binding" IPI annotations point to these)
- phyB (Pfr-specific), CRY1, CRY2 [PMID:26724867]; PIF3, APRR1/TOC1 [UniProt SUBUNIT].
- DELLA proteins RGA and RGL2 [PMID:20093430]; gibberellin/light framework involving DELLAs [PMID:18216857].
- HFR1 (forms non-DNA-binding/non-functional heterodimers, inhibiting shade-avoidance/PIF4 activity) [PMID:19851283 "Inhibition of the shade avoidance response by formation of non-DNA binding bHLH heterodimers"].
- BZR1 (brassinosteroid; BZR1-PIF4 integrate brassinosteroid and environmental responses) [PMID:22820378].
- HEMERA/PTAC12/HMR/PAP5 (transcriptional co-activator; couples proteolysis and transcriptional activity) [PMID:25944101].
- 14-3-3 proteins (TAP-MS proteomics) [PMID:19452453].
- FYPP1/FYPP3 (PP6 phosphatase) dephosphorylate PIF proteins to repress photomorphogenesis [PMID:31527236].
- MED14 (Mediator) [PMID:36063057].
- SSN1 (salt-responsive condensate facilitating PIF4 degradation) [PMID:40726285].
- NO2/nitrogen dioxide suppresses PIF4 activity (DNA binding context) [PMID:38958765].

## Stress / expression regulation (IEP - regulation of expression, not necessarily PIF4 acting in pathway)
- PIF4 mRNA: down-regulated by ethylene (ACC) and auxin (IAA); up-regulated by salt (NaCl), cold, heat; circadian rhythm with higher daytime levels. [PMID:23708772; UniProt INDUCTION] These IEP annotations reflect that PIF4 *expression responds to* these stimuli (gene-to-stimulus correlation), which is weaker evidence than IMP/IDA for PIF4 being a causal effector in those response pathways. The heat/temperature response is independently and strongly supported as a genuine PIF4 function (thermomorphogenesis).

## Localization
- Nucleus. [PMID:12006496; PMID:26724867; UniProt SUBCELLULAR LOCATION: Nucleus]

## Summary of core molecular functions for the review
1. Sequence-specific DNA-binding transcription factor (G-box/E-box) regulating transcription (RNA Pol II) of growth/elongation genes — core MF GO:0003700 + GO:0003677; process GO:0006357/GO:0006355.
2. Negative component of phyB red-light signaling; node integrating red (phyB) and blue (CRY) light signals controlling de-etiolation/hypocotyl elongation — GO:0010017 / GO:0010161.
3. Central positive regulator of thermomorphogenesis (warm-temperature growth) via auxin pathway activation with HMR/MED14 — GO:0140922.
4. Regulator of auxin biosynthesis and auxin signaling — GO:0010600 / GO:0010928.
5. Protein dimerization (bHLH homo/heterodimers, incl. non-functional HFR1 heterodimers) — GO:0046983.

## Action rationale notes
- "protein binding" (GO:0005515, IPI): many separate entries, each anchored to a specific partner. Uninformative as a *core* MF per project guidelines; keep as non-core (they document real, curated interactions). Not removed because experimental IPI.
- IEP stress annotations (cold/heat/salt/ethylene/auxin from PMID:23708772): these are expression-correlation evidence; keep response-to-temperature/heat as relevant (corroborated by thermomorphogenesis), keep others as non-core. Not removing experimental-class IEP annotations.
- IEA/ISS/ISM electronic annotations for TF activity, nucleus, DNA-templated transcription regulation, dimerization, red/far-red signaling: all consistent with strong experimental evidence; accept core ones, keep generic ones.
