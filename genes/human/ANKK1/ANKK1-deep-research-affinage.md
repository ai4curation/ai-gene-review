---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKK1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8NFD2
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKK1 (human)

## Current model (mechanistic narrative)

ANKK1 encodes a RIP-family serine/threonine kinase bearing a single kinase domain and 11 ankyrin repeats, located immediately downstream of DRD2, where it functions in striatal dopaminergic circuitry to govern learning, impulsivity, and metabolic homeostasis [PMID:15146457, PMID:36805080]. In the adult brain it is expressed in astrocytes and, prominently, in striatal D2R-expressing neurons, with its transcription oppositely controlled by dopamine receptor activation — upregulated by D1R-like agonists and downregulated by D2R-like agonists — functionally coupling the kinase to dopaminergic tone [PMID:19853839, PMID:26194616, PMID:36805080]. Cell-type-specific loss of Ankk1 in dorsal and ventral striatum produces deficits in learning, impulsivity, and cognitive flexibility that mirror the endophenotypes of TaqIA A1 allele carriers, and ventral striatal loss disrupts energy homeostasis [PMID:36805080]. The kinase localizes to both nucleus and cytoplasm, and its abundance oscillates across the cell cycle, peaking in mitosis, where it regulates G1 and M phase progression in neural precursors [PMID:20845092, PMID:27166167]. Beyond neural tissue, ANKK1 is expressed in proliferative myoblasts, satellite cells, and fast-twitch glycolytic muscle fibers, and is induced by glycolytic and hypoxic stimuli, linking it to metabolic state [PMID:29758057]. The TaqIA-linked Ala239Thr variant alters basal protein levels and reverses the protein-level response to dopaminergic stimulation [PMID:20845092]. Direct enzymatic substrates of the kinase have not been identified in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016740 transferase activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | Medium | ANKK1 was identified as a novel gene containing a single serine/threonine kinase domain and 11 ankyrin repeats, located 10 kb downstream of DRD2 on chromosome 11q23.1. The DRD2 Taq1A RFLP (rs1800497) was shown to cause an amino acid substitution (Glu713Lys) within the 11th ankyrin repeat of ANKK1, which may affect substrate-binding specificity of the kinase. | PMID:15146457 | Human mutation |
| 2008 | Medium | A non-synonymous variant in ANKK1 (rs2734849, Arg→His in the C-terminal ankyrin repeat domain) was shown by luciferase reporter assay to alter expression levels of NF-κB-regulated genes, suggesting ANKK1 modulates NF-κB transcriptional activity. | PMID:18354387 | Neuropsychopharmacology |
| 2010 | High | ANKK1 mRNA and protein are expressed in the adult central nervous system exclusively in astrocytes in both humans and rodents; during embryonic development (peak ~E15 in mice), ANKK1 protein is ubiquitously expressed in radial glia. Ankk1 mRNA in mouse astrocyte cultures is upregulated by apomorphine, indicating a link to the dopaminergic system. | PMID:19853839 | Biological psychiatry |
| 2010 | Medium | ANKK1 kinase protein shows nucleocytoplasmic localization when expressed in HEK293T cells, suggesting nucleocytoplasmic shuttling. The Ala239Thr polymorphism (linked to TaqIA) produces differential basal protein expression levels (Thr239 variant ~1.56-fold higher than Ala239) and opposite responses to the dopamine agonist apomorphine: Ala239 variant shows ~2.4-fold increase in protein levels after apomorphine, while Thr239 variant shows ~0.67-fold reduction. | PMID:20845092 | Neurotoxicity research |
| 2011 | Low | ANKK1 belongs to the RIP (Receptor-Interacting Protein) serine/threonine kinase family, involved in cell proliferation, differentiation, and activation of transcription factors. DRD2 expression is proposed to be regulated by ANKK1 through NF-κB. | PMID:22232965 | Psychiatria polska |
| 2015 | Medium | Ankk1 mRNA was upregulated in mouse brain following activation of D1R-like dopamine receptors (SKF38393, apomorphine), whereas D2R-like agonists (7-OH-DPAT, aripiprazole) caused significant Ankk1 mRNA downregulation. At the protein level, D2R-like agonist 7-OH-DPAT caused a significant increase in Ankk1 protein specifically in the striatum compared to prefrontal cortex. Thus D1R-like and D2R-like receptor activation oppositely regulates Ankk1 transcription. | PMID:26194616 | Neurotoxicity research |
| 2017 | High | ANKK1 protein expression varies during the cell cycle in neural precursors: cell synchronization experiments showed a significant increase of ANKK1-kinase in mitotic cells. Overexpression of ANKK1-kinase affects G1 and M phase cell cycle progression, and these effects were modulated by ANKK1 alleles (Ala239 vs. Thr239) and apomorphine treatment. ANKK1 is expressed in slow-dividing neuroblasts and rapidly dividing precursors in embryonic neurogenesis, and is also found in astrocytes and nuclei of postmitotic neurons in adult brain. | PMID:27166167 | Cerebral cortex |
| 2018 | Medium | ANKK1 is expressed in myogenic precursors (migrating myotubes with polarized cytoplasmic distribution), proliferative myoblasts, and satellite cells. Nuclear ANKK1-kinase declines progressively during myogenic differentiation, being excluded from myotube nuclei. In adult mice, ANKK1 is expressed exclusively in fast-twitch (glycolytic) muscle fiber subtypes. Induction of glycolytic metabolism in C2C12 cells (high glucose or berberine) or hypoxia increases ANKK1 mRNA/nuclear ANKK1, respectively. ANKK1 is also found in regenerative fibers of dystrophic patient muscles. | PMID:29758057 | PloS one |
| 2023 | High | Ankk1 is preferentially enriched in striatal D2R-expressing neurons. Loss of Ankk1 function (transgenic and viral-mediated knockdown) in the dorsal and ventral striatum leads to alterations in learning, impulsivity, and cognitive flexibility resembling endophenotypes of A1 allele carriers. Ankk1 loss of function in ventral striatal D2R-expressing neurons also disrupts energy homeostasis/metabolism. In humans, differential nutrient partitioning was observed between A1 allele carriers and non-carriers. | PMID:36805080 | Biological psychiatry |
| 2009 | Low | ANKK1 mRNA transcript was detected by PCR in multiple human cortical regions (inferior temporal, occipital, superior frontal, and primary motor cortex) of control subjects. The TaqIA polymorphism selectively modulated NMDA receptor subunit (NR1, NR2A, NR2B) mRNA expression in superior frontal cortex of cirrhotic-alcoholic subjects, suggesting ANKK1 may mediate effects of TaqIA on NMDA receptor expression. | PMID:19283474 | Neurochemical research |

## Citations

- PMID:15146457
- PMID:18354387
- PMID:19283474
- PMID:19853839
- PMID:20845092
- PMID:22232965
- PMID:26194616
- PMID:27166167
- PMID:29758057
- PMID:36805080
