---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AMIGO1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q86WK6
self_evaluation_pairwise: win
faith_pct: 83.33333333333333
n_discoveries: 12
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AMIGO1 (human)

## Current model (mechanistic narrative)

AMIGO1 is a type I transmembrane leucine-rich-repeat/immunoglobulin-domain cell adhesion molecule that serves dual roles in neural circuit assembly and in shaping neuronal electrical excitability [PMID:12629050, PMID:22056818]. Its ectodomain comprises six leucine-rich repeats with cysteine-rich N- and C-terminal caps followed by a C2-type Ig domain, and crystallographic and biophysical analysis shows it dimerizes through an LRR-LRR interface that is required for stable ER folding and cell-surface expression [PMID:21983541]. Through homophilic LRR-mediated adhesion AMIGO1 promotes neurite extension, fasciculation, and tract formation: the substrate-bound ectodomain drives outgrowth while the soluble ectodomain acts as a dominant-negative that disrupts fasciculation in hippocampal neurons and in zebrafish fiber scaffolds [PMID:12629050, PMID:24904058], and genetic deletion in mice reveals a compartment-specific requirement for AMIGO1 in scaling retinal horizontal cell axon arbors [PMID:35169021]. In parallel, AMIGO1 is an auxiliary subunit of Kv2.1/Kv2.2 voltage-gated potassium channels: it co-immunoprecipitates and colocalizes with Kv2.1, and loss of AMIGO suppresses the neuronal delayed rectifier current and reduces brain Kv2.1 protein in vivo [PMID:22056818, PMID:26240432]. Assembly with Kv2 channels hyperpolarizes the activation midpoint by roughly -10 mV, and mechanistically AMIGO1 destabilizes the earliest resting conformation of the Kv2.1 voltage sensors, speeding early sensor movements and shifting the gating charge-voltage relationship to more negative voltages [PMID:34137443, PMID:35314141]. The relationship is reciprocal: Kv2 α subunits are obligatory for AMIGO1 clustering, plasma-membrane trafficking, and expression, localizing it to ER-PM junctions, a dependency that extends to motor neurons where Kv2-mediated junction formation is required for AMIGO1 localization [PMID:29403353, PMID:bio_10.1101_2025.06.04.657913].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098631 cell adhesion mediator activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005886 plasma membrane, GO:0005783 endoplasmic reticulum
- **pathway (Reactome):** R-HSA-112316 Neuronal System, R-HSA-1266738 Developmental Biology
- **partners:** KCNB1, KCNB2, AMIGO1
- **complexes:** Kv2.1 channel complex, Kv2.2 channel complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | Medium | AMIGO1 (AMIGO) is a type I transmembrane protein with six leucine-rich repeats flanked by cysteine-rich LRR N- and C-terminal domains and one immunoglobulin domain; substrate-bound recombinant AMIGO ectodomain promoted neurite extension in hippocampal neurons, while soluble AMIGO ectodomain inhibited neurite fasciculation; AMIGO family members engage in homophilic and heterophilic binding with each other. | PMID:12629050 | The Journal of cell biology |
| 2011 | High | AMIGO1 is an auxiliary subunit of the Kv2.1 potassium channel complex: it shows extensive spatial and temporal colocalization and co-immunoprecipitation with Kv2.1 in mouse brain, increases Kv2.1 conductance in a voltage-dependent manner in HEK cells, and siRNA-mediated inhibition of endogenous AMIGO suppresses neuronal delayed rectifier current (IK) at negative membrane voltages. | PMID:22056818 | EMBO reports |
| 2011 | High | Crystal structure of AMIGO-1 ectodomain determined at 2.0 Å resolution, revealing a typical LRR domain with N- and C-terminal capping domains containing disulfide bridges followed by a C2-type Ig domain; AMIGO-1 forms a dimer through its LRR-LRR interface, and mutagenesis studies showed that dimerization is necessary for proper cell surface expression, suggesting a role in stable folding in the ER and cell-cell adhesion. | PMID:21983541 | Journal of molecular biology |
| 2012 | Medium | AMIGO1 localizes predominantly to dendrites in mature primary neurons (while LRR-deleted AMIGO is axonal), and siRNA-mediated silencing of AMIGO reduces dendritic growth of cortical neurons in culture; overexpression of AMIGO in SH-SY5Y cells confers resistance to staurosporine- and H2O2-induced apoptosis. | PMID:21938721 | Journal of cellular physiology |
| 2014 | Medium | In zebrafish, amigo1 is the predominant family member expressed during nervous system development; morpholino knockdown of amigo1 impairs fasciculated tract formation in early fiber scaffolds, and mRNA-mediated overexpression of the Amigo1 ectodomain (which inhibits adhesion by the full-length protein) produces a similar defect, confirming that homophilic interactions underlie fiber tract development; Amigo1 also regulates Kv2.1 potassium channel function to form functional neural circuitry controlling locomotion. | PMID:24904058 | The Journal of biological chemistry |
| 2015 | Medium | Genetic deletion of AMIGO in mice reduces the amount of Kv2.1 channel protein in brain and alters electrophysiological properties of neurons, demonstrating that AMIGO is required for normal Kv2.1 expression levels and neuronal electrical activity in vivo. | PMID:26240432 | Schizophrenia bulletin |
| 2018 | High | In adult brain neurons, AMIGO-1 is exclusively colocalized with Kv2.1 and Kv2.2 at plasma membrane sites associated with neuronal ER:PM junctions (hypolemmal subsurface cisternae); Kv2 α subunits are obligatory for AMIGO-1 clustering, PM trafficking, and expression level—coexpression of either Kv2.1 or Kv2.2 is sufficient to drive AMIGO-1 clustering in heterologous cells, and AMIGO-1 expression/localization is lost in Kv2.1 or Kv2.2 knockout mice. | PMID:29403353 | Frontiers in molecular neuroscience |
| 2021 | Medium | All three AMIGO family proteins (AMIGO1, 2, 3) are controlled in surface trafficking and localization by assembly with either Kv2.1 or Kv2.2; AMIGO1 assembly with either Kv2 channel hyperpolarizes the channel activation midpoint by approximately −10 mV; AMIGO1 does not significantly slow inactivation or deactivation (unlike AMIGO2), indicating isoform-specific modulation. | PMID:34137443 | Journal of cell science |
| 2022 | High | AMIGO1 modulates the Kv2.1 conductance activation pathway by destabilizing the earliest resting state of Kv2.1 voltage sensors: AMIGO1 speeds early voltage-sensor movements, shifts the gating charge-voltage (Q-V) relationship to more negative voltages, and when voltage sensors are detained at rest by toxins, AMIGO1 exerts a greater effect on the conductance-voltage relationship; fluorescence measurements from voltage-sensor toxins confirm that AMIGO1 makes the earliest resting conformation less stable upon voltage stimulation. | PMID:35314141 | Biophysical journal |
| 2022 | High | AMIGO1 selectively promotes axon arbor growth of retinal horizontal cells; genetic deletion of Amigo1 in mice reduces horizontal cell axon arbor size without affecting horizontal cell dendrite size or synapse formation, demonstrating a compartment-specific role for AMIGO1 in axon scaling; reduction of horizontal cell axons causes territory matching-mediated shrinkage of rod bipolar cell dendrites, preserving rod bipolar pathway function. | PMID:35169021 | The Journal of neuroscience |
| 2025 | Medium | AMIGO-1 clustering and expression in spinal motor neurons is dependent on Kv2 subunits: AMIGO-1 clustering at ER-PM junctions is severely reduced in Kv2.1 knockout mice and moderately reduced in Kv2.2 knockout mice, and is also severely reduced in Kv2.1 S590A mutant mice that cannot bind ER VAP proteins, indicating that Kv2-mediated ER-PM junction formation is required for AMIGO-1 localization in motor neurons. | PMID:bio_10.1101_2025.06.04.657913 | bioRxiv |
| 2024 | Medium | Chemogenetic activation of Amigo1-expressing GABAergic neurons within the interpeduncular nucleus (IPN) is critical for anxiety-like behaviors in both naïve mice and those undergoing nicotine withdrawal; stimulation of Amigo1 neurons in nicotine-naïve mice elicits opposite effects on affective versus somatic signs of withdrawal, demonstrating that Amigo1-expressing IPN neurons specifically mediate the affective component of nicotine withdrawal. | PMID:bio_10.1101_2024.07.05.602259 | bioRxiv |

## Citations

- PMID:12629050
- PMID:21938721
- PMID:21983541
- PMID:22056818
- PMID:24904058
- PMID:26240432
- PMID:29403353
- PMID:34137443
- PMID:35169021
- PMID:35314141
- PMID:bio_10.1101_2024.07.05.602259
- PMID:bio_10.1101_2025.06.04.657913
