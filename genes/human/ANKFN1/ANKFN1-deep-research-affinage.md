---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKFN1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8N957
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKFN1 (human)

## Current model (mechanistic narrative)

ANKFN1 (mWAKE) is a clock-output molecule that acts as a brake on neuronal excitability across distributed brain regions, coupling circadian timing to arousal, sensory perception, anxiety, and fear memory [PMID:37821426, PMID:39303704]. In the dorsomedial hypothalamus, mWAKE protein peaks at night under clock control and dampens DMH neuronal excitability, such that its loss produces hyperarousal and elevated night-time excitability of these GABAergic neurons [PMID:37821426]. The same rhythmic, clock-dependent mechanism operates in the anterior/dorsal lateral amygdala, where mWAKE rises at night to promote rhythmic excitability by upregulating Ca2+-activated K+ channel activity and is required to sustain PER2 rhythms and rhythmic sensory and anxiety behavior [PMID:39303704]. In the central amygdala, mWAKE is expressed without rhythmicity yet still restrains intrinsic neuronal excitability, and its loss or chemogenetic perturbation of mWAKE neurons impairs fear learning and memory, with mWAKE levels falling after fear conditioning [PMID:40835437]. Outside the nervous system, ANKFN1 drives hepatocellular carcinoma proliferation, migration, and invasion by activating MEK1/2-ERK1/2 signaling and the cyclin D1/Cdk4/Cdk6 axis to promote G1/S transition [PMID:35725908], and vertebrate Ankfn1 is required for vestibular function, with zebrafish paralogs acting partially redundantly [PMID:35100349]. The molecular biochemistry of the ANKFN1 protein itself — how it regulates ion channels or engages the MEK-ERK cascade — has not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005634 nucleus, GO:0005929 cilium
- **pathway (Reactome):** R-HSA-9909396 Circadian clock, R-HSA-112316 Neuronal System
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2024 | High | mWAKE/ANKFN1 is expressed in the anterior/dorsal lateral amygdala (adLA) and defines an extra-SCN oscillator. mWAKE levels rise at night under clock control and promote rhythmic excitability of adLAmWAKE neurons by upregulating Ca2+-activated K+ channel activity specifically at night. Selective disruption of clock function or excitatory signaling in adLAmWAKE neurons abolishes PER2 rhythms throughout the lateral amygdala, and these neurons coordinate rhythmic sensory perception and anxiety in a clock-dependent and WAKE-dependent manner. | PMID:39303704 | Neuron |
| 2023 | High | mWAKE/ANKFN1 labels a subpopulation of dorsomedial hypothalamus (DMH) neurons involved in rhythmic arousal and acts as a clock-dependent brake on arousal at night. mWAKE levels peak at night under clock control; loss of mWAKE leads to hyperarousal and greater DMHmWAKE neuronal excitability specifically at night. DMHmWAKE neurons (shown to be GABAergic) are necessary and sufficient for arousal by chemogenetic manipulation. | PMID:37821426 | Nature communications |
| 2025 | High | mWAKE/ANKFN1 is expressed in multiple neuronal subclusters in the lateral central amygdala (CeA) but does not exhibit rhythmic expression there (and core clock genes PER2/BMAL also do not cycle in CeA). Loss of mWAKE increases intrinsic excitability of CeA neurons. Conditional knockout of mWAKE and chemogenetic activation of CeAmWAKE neurons each impair fear learning and memory. mWAKE levels in a subset of CeA neurons are reduced following fear conditioning. | PMID:40835437 | The Journal of neuroscience |
| 2020 | Medium | mWAKE/ANKFN1 protein is expressed in neurons in a restricted but distributed manner across multiple hypothalamic regions (SCN, DMH, tuberomammillary nucleus), limbic system, sensory processing nuclei, brainstem, and cortex in adult mouse brain, as well as in non-neuronal ependymal cells. Single-cell RNA-seq of hypothalamus identifies distinct molecular identities of mWake+ cell clusters. | PMID:33140455 | The Journal of comparative neurology |
| 2022 | Medium | ANKFN1 promotes hepatocellular carcinoma (HCC) cell proliferation, migration, and invasion by activating the MEK1/2-ERK1/2 signaling pathway, leading to induction of G1/S transition via the cyclin D1/Cdk4/Cdk6 pathway. ERK1/2 inhibitors partially reversed ANKFN1-induced proliferation, migration, and invasion. ANKFN1 silencing suppressed subcutaneous tumorigenesis in vivo. | PMID:35725908 | Oncogene |
| 2022 | Medium | Simultaneous disruption of both zebrafish Ankfn1 paralogs (ancestral and derived) causes vestibular defects and early lethality from swim bladder inflation failure, while retention of one intact copy at either locus prevents major phenotypes, demonstrating partial redundancy between paralogs and a required role of vertebrate Ankfn1 in vestibular function. | PMID:35100349 | G3 (Bethesda, Md.) |
| 2022 | Low | CRISPR/Cas9-induced disruption of ankfn1 in zebrafish F0 crispants recapitulates ciliary phenotypes consistent with a cilia-associated function, grouping ANKFN1 among genes required for cilia function. | PMID:36533556 | Disease models & mechanisms |

## Citations

- PMID:33140455
- PMID:35100349
- PMID:35725908
- PMID:36533556
- PMID:37821426
- PMID:39303704
- PMID:40835437
