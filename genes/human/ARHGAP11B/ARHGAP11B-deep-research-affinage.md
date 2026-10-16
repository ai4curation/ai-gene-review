---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGAP11B
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q3KRB8
self_evaluation_pairwise: win
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

# Affinage mechanistic annotation for ARHGAP11B (human)

## Current model (mechanistic narrative)

ARHGAP11B is a human-specific gene that drives evolutionary expansion of the neocortex by amplifying basal progenitor populations during corticogenesis [PMID:25721503]. It arose from a partial duplication of ARHGAP11A on the human lineage, and a single C→G substitution created a novel splice donor site that truncates the RhoGAP domain—abolishing GTPase-activating activity—and appends a unique human-specific C-terminus; both the loss of RhoGAP activity and the gain of the novel C-terminal sequence are required for its progenitor-amplifying function [PMID:27957544]. Mechanistically, ARHGAP11B is imported into mitochondria, where it binds the adenine nucleotide translocase (ANT) and inhibits the mitochondrial permeability transition pore (mPTP), establishing a glutaminolysis-dependent metabolic state required for basal progenitor expansion; pharmacological inhibition of ANT or mPTP phenocopies its effect [PMID:31883789]. Expression of ARHGAP11B increases proliferative basal radial glia, extends neurogenesis, and produces supernumerary upper-layer neurons with neocortical enlargement and folding across mouse, ferret, marmoset, and primate organoid systems [PMID:30484771, PMID:32554627, PMID:36098218], and at physiological levels it enlarges the neocortex with persistent cognitive-behavioural consequences [PMID:33938018]. ARHGAP11B is both necessary and sufficient for the elevated basal progenitor levels that distinguish human from chimpanzee cortex, a role its ancestral paralog ARHGAP11A cannot fulfill [PMID:36098218].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1266738 Developmental Biology, R-HSA-1430728 Metabolism
- **partners:** SLC25A4
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2015 | High | ARHGAP11B arose from partial duplication of ARHGAP11A on the human lineage after separation from the chimpanzee lineage. Expression of ARHGAP11B in embryonic mouse neocortex promotes basal progenitor (BP) generation and self-renewal, increasing cortical plate area and inducing gyrification, establishing a direct role in basal progenitor amplification. | PMID:25721503 | Science |
| 2016 | High | A single C→G nucleotide substitution in ARHGAP11B creates a novel splice donor site that deletes 55 nucleotides from the mRNA, causing GAP domain truncation and loss of RhoGAP activity while adding a human-specific C-terminal amino acid sequence. Ancestral ARHGAP11B (without this substitution) retains RhoGAP activity but cannot increase basal progenitors. Thus, loss of RhoGAP activity and gain of the human-specific C-terminus are required for ARHGAP11B's neocortex-expansion function. | PMID:27957544 | Science Advances |
| 2019 | High | ARHGAP11B is imported into mitochondria where it interacts with the adenine nucleotide translocase (ANT) and inhibits the mitochondrial permeability transition pore (mPTP). Mitochondrial localization is required for BP expansion. Pharmacological inhibition of ANT function or mPTP opening phenocopies ARHGAP11B-induced BP expansion. BP expansion by ARHGAP11B additionally requires glutaminolysis (conversion of glutamine to glutamate for the TCA cycle). | PMID:31883789 | Neuron |
| 2018 | High | Expression of ARHGAP11B in developing ferret neocortex markedly increases proliferative basal radial glia (bRG), extends the neurogenic period, increases upper-layer neurons, and expands the neocortex in both radial and tangential dimensions, establishing that ARHGAP11B elicits hallmarks of neocortical expansion in a gyrencephalic mammal. | PMID:30484771 | eLife |
| 2020 | High | Expression of ARHGAP11B in fetal marmoset neocortex under its own human promoter increases basal radial glia in the outer subventricular zone, increases upper-layer neurons, enlarges the neocortex, and induces cortical folding, providing functional evidence that ARHGAP11B causes neocortical expansion in a non-human primate. | PMID:32554627 | Science |
| 2021 | High | Transgenic mice expressing ARHGAP11B at physiological levels exhibit increased neocortical size and upper-layer neuron numbers persisting into adulthood, and show altered neurobehaviour including increased memory flexibility and reduced anxiety, linking ARHGAP11B-driven neocortex expansion to cognitive phenotypes. | PMID:33938018 | The EMBO Journal |
| 2022 | High | ARHGAP11B is necessary and sufficient for the elevated basal progenitor levels characteristic of the fetal human neocortex: expression in chimpanzee cerebral organoids doubles basal progenitor levels, while interference with ARHGAP11B function in human cerebral organoids reduces basal progenitors to chimpanzee levels. ARHGAP11A cannot substitute for ARHGAP11B in this role. | PMID:36098218 | EMBO Reports |

## Citations

- PMID:25721503
- PMID:27957544
- PMID:30484771
- PMID:31883789
- PMID:32554627
- PMID:33938018
- PMID:36098218
