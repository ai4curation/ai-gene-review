---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATXN7
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: O15265
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 25
citation_count: 25
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATXN7 (human)

## Current model (mechanistic narrative)

ATXN7 is a subunit of the SAGA/STAGA transcriptional coactivator complex that anchors the histone H2B deubiquitination module (DUBm), and through this role governs chromatin organization and photoreceptor/neuronal gene programs [PMID:19226466, PMID:25306109]. Its yeast ortholog Sgf73 is required to recruit the DUBm into the SAGA and SLIK HAT complexes, and an N-terminal zinc-finger domain maintains the active, ubiquitin-binding conformation of the catalytic deubiquitinase Ubp8 [PMID:19226466, PMID:25526805, PMID:20510875]. ATXN7 binds the cone-rod homeobox factor CRX and is required for normal photoreceptor gene expression, and its loss in vertebrates causes eye morphogenesis defects through elevated Hedgehog signaling and altered crx expression [PMID:11580893, PMID:30445451]. Distinct domains of Sgf73 mediate SAGA-independent functions including heterochromatin boundary activity and assembly of the RNAi/RITS silencing complex [PMID:23819448, PMID:26443059]. ATXN7 abundance is itself controlled by ubiquitin-proteasome degradation, which feeds back on transcription, and by a STAGA-dependent miR-124/lnc-SCA7 regulatory loop [PMID:30559154, PMID:37075097, PMID:25306109]. Polyglutamine expansion in ATXN7 produces both loss of these coactivator functions—reduced promoter occupancy with increased local H2B ubiquitination—and a gain of toxic function: caspase-7 cleavage at D266 is a critical in vivo driver of neurotoxicity, while SUMO2/3-RNF4-mediated clearance, autophagy impairment via a p53-FIP200-ULK1 axis, and NADPH oxidase-dependent oxidative and bioenergetic stress collectively produce selective degeneration of cerebellar Purkinje cells and retinal photoreceptors [PMID:25859008, PMID:30559154, PMID:23236151, PMID:23592174, PMID:22827889, PMID:25647692]. Mutations in ATXN7 cause spinocerebellar ataxia type 7 (SCA7) [PMID:25859008].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0060089 molecular transducer activity, GO:0003677 DNA binding
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-1643685 Disease, R-HSA-9612973 Autophagy, R-HSA-392499 Metabolism of proteins
- **partners:** CRX, USP22/UBP8, GCN5, RNF4, SUMO2, FIP200, TP53, APLP2
- **complexes:** SAGA/STAGA, histone deubiquitination module (DUBm), SLIK/SALSA HAT complex, RITS complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | High | Ataxin-7 physically interacts with the cone-rod homeobox protein CRX, as demonstrated by yeast two-hybrid assay and co-immunoprecipitation; polyglutamine-expanded ataxin-7 colocalizes with CRX and dramatically suppresses CRX transactivation activity, leading to reduced CRX DNA-binding activity and decreased expression of CRX-regulated photoreceptor genes in SCA7 transgenic mice. | PMID:11580893 | Neuron |
| 2009 | High | Yeast Sgf73 (ortholog of human ATXN7) is required to recruit the histone deubiquitination module (DUBm) into both the SAGA and Slik(SALSA) HAT complexes, and loss of Sgf73 impairs histone H2B deubiquitination and regulation of transcription at multiple genes. | PMID:19226466 | Epigenetics & chromatin |
| 2014 | High | Sgf73 point mutations (yeast ATXN7 ortholog) that disrupt DUBm deubiquitinating activity do so by impairing the ubiquitin-binding fingers region of Ubp8 and destabilizing overall DUBm folding, demonstrating that Sgf73 maintains the organization and ubiquitin-binding conformation of the catalytic subunit Ubp8. | PMID:25526805 | Journal of molecular biology |
| 2010 | Medium | The N-terminal zinc finger motif of yeast Sgf73 (residues 1-104) requires a zinc ion to maintain stable folding and conformation, as demonstrated by NMR backbone assignment, secondary structure analysis, and circular dichroism after zinc chelation with EDTA. | PMID:20510875 | Biochemical and biophysical research communications |
| 2013 | Medium | C-terminus of yeast Sgf73 (residues 373-402) is essential for heterochromatin boundary function, and this boundary function depends on the HAT module components Ada2, Ada3, and Gcn5 of the SAGA/SLIK complex, but is independent of the deubiquitinase-anchoring domain of Sgf73. | PMID:23819448 | Genes to cells |
| 2015 | Medium | In fission yeast, Sgf73 (ATXN7 ortholog) is physically associated with Ago1 and Chp1 subunits of the RITS complex and is required for RITS complex assembly, pericentromeric heterochromatin silencing, and siRNA generation; this function is independent of SAGA enzymatic activities or structural integrity. | PMID:26443059 | Scientific reports |
| 2015 | High | Proteolytic cleavage of ataxin-7 by caspase-7 at residue D266 is a critical mediator of SCA7 neurotoxicity in vivo; transgenic mice expressing caspase-7-resistant ataxin-7 (D266N mutation) show improved motor performance, reduced neurodegeneration, and substantial lifespan extension compared to SCA7 mice without the D266N mutation. | PMID:25859008 | Human molecular genetics |
| 2019 | High | Endogenous ATXN7 and polyQ-expanded ATXN7 are modified by SUMO2/3; RNF4 (a SUMO-targeted ubiquitin ligase) is recruited by SUMO2/3-modified polyQ-ATXN7, leading to its polyubiquitination and proteasomal degradation. Overexpression of RNF4 and/or SUMO2 significantly decreased levels of polyQ-ATXN7, and SUMO2/3 co-localizes with polyQ-ATXN7 inclusions in SCA7 knock-in mouse cerebellum and retina. | PMID:30559154 | Disease models & mechanisms |
| 2023 | Medium | Yeast Sgf73 (ATXN7 ortholog) undergoes ubiquitylation and proteasomal degradation; impaired Sgf73 degradation increases its abundance, enhances TBP recruitment to promoters but impairs transcription elongation, while decreased Sgf73 reduces PIC formation. Similarly, human ataxin-7 undergoes ubiquitylation and proteasomal degradation, alteration of which changes ataxin-7 abundance and is associated with altered transcription. | PMID:37075097 | Genetics |
| 2012 | Medium | Polyglutamine-expanded ATXN7 (mutant) decreases ATXN7 occupancy at the reelin promoter, which correlates with increased histone H2B monoubiquitination at that locus, reducing reelin transcription in human SCA7 astrocytes. TSA treatment partially restores reelin transcription. | PMID:23236151 | Proceedings of the National Academy of Sciences of the United States of America |
| 2011 | Medium | Reducing Gcn5 expression (the HAT catalytic subunit of SAGA) accelerates both cerebellar and retinal degeneration in SCA7 mice, demonstrating that Gcn5 HAT activity within the SAGA complex in which ATXN7 resides contributes to SCA7 disease onset and severity; however, Gcn5 depletion does not further alter known ATXN7 transcriptional targets, suggesting non-transcriptional SAGA functions are involved. | PMID:22002997 | Human molecular genetics |
| 2013 | Medium | STAGA complex (containing ATXN7) is required for transcription initiation of miR-124, which post-transcriptionally regulates ATXN7 mRNA via cross-talk with lnc-SCA7; polyQ expansion in ATXN7 disrupts this regulatory feedback, resulting in neuron-specific increases in ATXN7 expression most prominent in disease-relevant tissues (retina and cerebellum). | PMID:25306109 | Nature structural & molecular biology |
| 2001 | Medium | Mutant ataxin-7 undergoes cytoplasm-to-nucleus translocation and accumulates as N-terminal fragments in neuronal nuclei in SCA7 transgenic mice; mouse TAFII30 (a subunit of TFIID) is markedly sequestered into nuclear inclusions; mutant ataxin-7 is selectively stabilized at the protein level relative to wild-type, as evidenced by discrepancy between mRNA and protein levels in transgenic mice expressing mutant but not wild-type ataxin-7. | PMID:11487572 | Human molecular genetics |
| 2006 | Medium | Polyglutamine-expanded ataxin-7 in rod photoreceptors activates the JNK/c-Jun stress pathway; genetic prevention of c-Jun activation (JunAA knock-in) improves SCA7 retinopathy and partially restores expression of rod-specific genes including the transcription factor Nrl and its downstream phototransduction targets. c-Jun directly represses Nrl transcription. | PMID:17189700 | Neurobiology of disease |
| 2013 | Medium | Interferon-beta induces PML protein expression and PML nuclear body formation, which mediates clearance of mutant ataxin-7 from neuronal intranuclear inclusions in SCA7 knock-in mice; this is accompanied by improved motor function on behavioral tests and improved Purkinje cell survival in cell culture. | PMID:23518714 | Brain : a journal of neurology |
| 2013 | Medium | Mutant ATXN7 inhibits autophagy via a p53-mediated mechanism: increased p53-FIP200 interaction and co-aggregation of p53 and FIP200 into ATXN7 aggregates decreases soluble FIP200, destabilizing ULK1 and reducing capacity for autophagy induction through the ULK1-FIP200-Atg13-Atg101 complex. p53 inhibitor treatment or blocking ATXN7 aggregation restores FIP200/ULK1 levels and increases autophagic activity. | PMID:23592174 | Journal of molecular neuroscience : MN |
| 2012 | Medium | Polyglutamine-expanded ATXN7 induces reactive oxygen species (ROS) production from NADPH oxidase (NOX) complexes; NOX inhibition completely prevents the ROS increase, and both antioxidant treatment and NOX inhibition reduce ATXN7 aggregation and toxicity. Mutant ATXN7 also decreases catalase levels, contributing to oxidative stress. | PMID:22827889 | BMC neuroscience |
| 2015 | Medium | Mutant ATXN7 causes bioenergetic defects through disruption of p53 and NOX1 activity: p53 co-aggregates with mutant ATXN7 reducing its transcriptional activity (50% decrease in AIF and TIGAR), while NOX1 expression increases ~2-fold, collectively resulting in decreased respiratory capacity, increased glycolytic reliance, and 20% reduction in ATP. Restoring p53 function or suppressing NOX1 activity reverses metabolic dysfunction. | PMID:25647692 | Biochimica et biophysica acta |
| 2010 | Low | Ataxin-7 physically interacts with APLP2 (amyloid precursor-like protein 2); caspase-3-mediated cleavage of APLP2 generates intracellular C-terminal domains that translocate to the nucleus, and abnormal nuclear relocation of APLP2 N-terminal fragments is detected in SCA7 neuronal intranuclear inclusions. Co-expression of APLP2 ICDs with mutant ataxin-7 causes cumulative cytotoxicity. | PMID:20732423 | Neurobiology of disease |
| 2011 | Medium | In SCA7 rod photoreceptor nuclei, the amount of linker histone H1c is strongly reduced and its distribution in facultative heterochromatin is altered, accompanied by fragmentation and decondensation of the most external heterochromatin ring. Acetylated histones H3 and H4 are unchanged in nuclear extracts. | PMID:21970987 | Nucleus (Austin, Tex.) |
| 2019 | Medium | Loss-of-function of ATXN7 in zebrafish causes ocular coloboma by elevating Hedgehog signaling in the forebrain, altering proximo-distal patterning of the optic vesicle; at later stages, photoreceptor outer segment formation is incomplete, correlating with altered expression of crx. This demonstrates ATXN7 plays an essential role in vertebrate eye morphogenesis and photoreceptor differentiation. | PMID:30445451 | Human molecular genetics |
| 2012 | Medium | In a stable inducible SCA7 cell model, the ubiquitin-proteasome system (UPS) is essential for degradation of full-length ATXN7 (both normal and expanded), whereas cleaved ATXN7 fragments are degraded by both UPS and autophagy. Inhibition of either pathway worsens mutant ATXN7 toxicity; pharmacological autophagy activation ameliorates toxicity. | PMID:22367614 | Journal of molecular neuroscience : MN |
| 2002 | Low | Ataxin-7 expression is primarily nuclear in most brain regions studied; in cerebellar Purkinje cells, differences in subcellular distribution were observed between SCA7 patients and controls of different ages, suggesting disease-related redistribution. | PMID:12070661 | Acta neuropathologica |
| 2005 | Low | An alternative ataxin-7 isoform (ataxin-7b), generated by inclusion of exon 12b causing a frameshift and novel 58-amino acid C-terminus, localizes to a more cytoplasmic location compared to the canonical nuclear ataxin-7a isoform. | PMID:16297465 | Biochimica et biophysica acta |
| 2022 | Low | TDP-43 and TIA1 are sequestered into aggregates formed by polyQ-expanded ATXN7 in SCA7 cells; mutant ATXN7 also localizes to stress granules induced by arsenite and alters their shape; mutant ATXN7 expression increases speckling of stress granule-nucleating protein G3BP1. The dynamics of stress granule assembly and disassembly are not significantly impaired in SCA7 cells. | PMID:35689166 | Molecular neurobiology |

## Citations

- PMID:11487572
- PMID:11580893
- PMID:12070661
- PMID:16297465
- PMID:17189700
- PMID:19226466
- PMID:20510875
- PMID:20732423
- PMID:21970987
- PMID:22002997
- PMID:22367614
- PMID:22827889
- PMID:23236151
- PMID:23518714
- PMID:23592174
- PMID:23819448
- PMID:25306109
- PMID:25526805
- PMID:25647692
- PMID:25859008
- PMID:26443059
- PMID:30445451
- PMID:30559154
- PMID:35689166
- PMID:37075097
