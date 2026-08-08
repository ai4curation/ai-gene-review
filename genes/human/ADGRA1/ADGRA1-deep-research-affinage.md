---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADGRA1
affinage_run_date: 2026-06-09T22:02:41
uniprot_accession: Q86SQ6
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 9
citation_count: 11
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADGRA1 (human)

## Current model (mechanistic narrative)

ADGRA1 (GPR123) is an atypical adhesion G protein-coupled receptor that controls inhibitory synaptic function in the central nervous system and broader homeostatic signaling [PMID:41961591, PMID:33824276]. It is structurally distinguished from other adhesion GPCRs by the absence of the GPS/GAIN domain in its N-terminus while retaining the canonical seven-transmembrane architecture [PMID:12565841, PMID:25713288, PMID:27832482, PMID:25424900]. Its expression is largely CNS-restricted, with enrichment in thalamus, cortical layers 5/6, amygdala, hypothalamus, and hippocampus [PMID:17212699], and the protein localizes to postsynaptic compartments and a subset of synapses [PMID:28935861, PMID:41961591]. In the hippocampus, ADGRA1 is selectively enriched in parvalbumin (PV) interneurons, where it couples to downstream G proteins including Gα13 to sustain PV interneuron intrinsic excitability and inhibitory synaptic strength onto dentate gyrus granule cells, supporting learning and memory [PMID:41961591]. Beyond the synapse, ADGRA1 acts as a negative regulator of metabolic and behavioral homeostasis: its loss in mice elevates energy expenditure and thermogenesis via the sympathetic and hypothalamus-pituitary-thyroid axes [PMID:33824276] and increases anxiety-like behavior with altered amygdalar dendritic morphology [PMID:36115515], both phenotypes accompanied by aberrant activation of the PI3K/AKT/GSK3β and MEK/ERK pathways that ADGRA1 normally suppresses [PMID:33824276, PMID:36115515]. ADGRA1 is also required for maintenance of human pluripotent stem cell identity and for reprogramming to induced pluripotency [PMID:36672239].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060089 molecular transducer activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-112316 Neuronal System
- **partners:** GNA13
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | Medium | ADGRA1 (GPR123) was identified as a member of the adhesion GPCR family with a seven-transmembrane domain but notably LACKS a GPS (GPCR proteolytic site) domain in its N-terminus, unlike most other adhesion GPCRs in this family. | PMID:12565841, PMID:25713288, PMID:27832482, PMID:25424900 | Biochemical and biophysical research communications |
| 2006 | Medium | ADGRA1 (GPR123) mRNA is predominantly expressed in the CNS, with high expression in thalamic nuclei, cortex layers 5 and 6, subiculum, amygdala, hypothalamus, inferior olive, and spinal cord, as determined by in situ hybridization and real-time PCR in mouse and rat. | PMID:17212699 | Journal of neurochemistry |
| 2006 | Low | GPR123 protein sequence is well conserved within the vertebrate lineage, especially within transmembrane regions and in the distal cytoplasmic tail, which contains a potential PDZ binding domain. | PMID:17212699 | Journal of neurochemistry |
| 2017 | Medium | ADGRA1 protein localizes to postsynaptic compartments in mouse brain neurons, as confirmed by super-resolution microscopy on primary neuronal culture combined with biochemical sub-fractionation profiling. | PMID:28935861 | Scientific reports |
| 2021 | Medium | ADGRA1 negatively regulates energy expenditure and thermogenesis in male mice via the sympathetic nervous system and hypothalamus-pituitary-thyroid axis. Adgra1 knockout male mice show decreased body weight, increased lipolysis, elevated core temperature, cold resistance, activation of TH, β3-AR, UCP1, PGC1-α (in BAT), and HSL (in WAT), plus elevated serum T3/T4. The PI3K/AKT/GSK3β and MEK/ERK pathways in the hypothalamus are aberrantly activated in knockout mice, and ADGRA1 overexpression in Neuro2A cells suppresses these pathways. | PMID:33824276 | Cell death & disease |
| 2022 | Medium | ADGRA1 deficiency in male mice causes increased anxiety-like behavior accompanied by elevated neuron dendritic branching complexity and spine density in the amygdala, upregulated PSD95 and SYN expression, and aberrant activation of PI3K/AKT/GSK-3β and MEK/ERK pathways in amygdalae. | PMID:36115515 | Neuroscience |
| 2023 | Medium | GPR123 (ADGRA1) is required for maintenance of pluripotency in human pluripotent stem cells (hPSCs) and for reprogramming to hiPSCs. RNAi-mediated suppression of GPR123 in hPSCs leads to loss of pluripotency, altered colony morphology, G2-phase cell cycle accumulation, impaired scratch closure, reduced E-cadherin expression, decreased NANOG+ nuclei, and absence of actin cytoskeleton remodeling and alkaline-phosphatase-positive hiPSC colonies. | PMID:36672239 | Cells |
| 2025 | Medium | ADGRA1 is selectively enriched in hippocampal PV and SST interneurons, localizes to a subset of synapses, and is essential for hippocampal inhibitory synaptic function. Deletion of ADGRA1 in PV and SST interneurons impairs inhibitory synaptic inputs onto dentate gyrus granule cells and generates deficits in learning and memory. ADGRA1 engages several downstream G proteins, notably Gα13, a pathway important for establishing hippocampal PV interneuron synaptic networks. | PMID:40766348 | bioRxiv |
| 2026 | High | ADGRA1 is selectively enriched in hippocampal PV interneurons, localizes to a subset of synapses, and is required for PV interneuron intrinsic excitability and inhibitory synaptic strength onto dentate gyrus granule cells. ADGRA1 engages several downstream G proteins, notably Gα13, a pathway important for establishing hippocampal PV interneuron synaptic networks. | PMID:41961591 | Cell reports |

## Citations

- PMID:12565841
- PMID:17212699
- PMID:25424900
- PMID:25713288
- PMID:27832482
- PMID:28935861
- PMID:33824276
- PMID:36115515
- PMID:36672239
- PMID:40766348
- PMID:41961591
