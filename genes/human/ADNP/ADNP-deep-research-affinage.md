---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADNP
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q9H2P0
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 28
citation_count: 28
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADNP (human)

## Current model (mechanistic narrative)

ADNP is a dual-compartment regulator of chromatin and the cytoskeleton that coordinates gene-expression programs underlying embryogenesis, neurogenesis, and immune cell differentiation [PMID:17222401, PMID:39808658, PMID:37285842]. In the nucleus, ADNP is a core subunit of a chromatin-remodeling complex, binding BRG1 and other SWI/SNF core subunits through its C-terminus [PMID:25169753] and recruiting the CHD4 helicase together with BRG1 (the ChAHP complex) to specific loci, where it converts pioneer-factor binding into active histone modification and DNA accessibility [PMID:37285842, PMID:39808658]. ADNP occupies defined promoters and chromatin regions—repressing endoderm genes while enhancing neurogenesis and organogenesis programs [PMID:17222401], binding the β-globin locus control region to drive erythroid maturation [PMID:23071114], and counteracting stable CTCF occupancy at SINE B2 elements to enforce H3K9me3 deposition and transcriptional silencing during preimplantation development [PMID:38479840]. ADNP also stabilizes β-catenin by binding its armadillo domain and blocking assembly of the Axin/APC degradation complex, thereby sustaining Wnt/neuroectoderm signaling [PMID:32533114], and it acts as a Wnt repressor whose loss promotes colorectal cancer cell migration, invasion, and tumor growth [PMID:27903678]. In the cytoplasm, ADNP is positioned by phosphorylation-dependent 14-3-3 binding [PMID:36631597] and engages microtubule end-binding proteins EB1 and EB3 through an SxIP motif in its NAP region, promoting EB3 homodimerization, EB-Tau recruitment to microtubules, and microtubule dynamics that support dendritic spine and PSD-95 maintenance [PMID:25178163, PMID:28115743]. ADNP loss-of-function disrupts neurite formation, synaptic transmission, hippocampal neurogenesis, and synaptic plasticity through dysregulated CaMKIIα activity, with several phenotypes corrected by the ADNP-derived NAP peptide [PMID:36631597, PMID:37365244, PMID:39715923]. Pathogenic ADNP truncating mutations, identified in autism spectrum disorder patients [PMID:25169753], disrupt nuclear localization and route the protein to cytoplasmic proteasomal degradation, producing mutation-specific neuronal phenotypes [PMID:29911927, PMID:36230962].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0003677 DNA binding, GO:0008092 cytoskeletal protein binding, GO:0140313 molecular sequestering activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol, GO:0005856 cytoskeleton, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-4839726 Chromatin organization, R-HSA-74160 Gene expression (Transcription), R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-112316 Neuronal System, R-HSA-168256 Immune System
- **partners:** BRG1, CHD4, EB1, EB3, CTNNB1, 14-3-3, SIRT1, EIF4E
- **complexes:** ChAHP complex (ADNP-CHD4-BRG1), SWI/SNF (BAF) complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | Medium | ADNP is a member of the SWI/SNF chromatin remodeling complex; its C-terminus directly and experimentally binds three core components of the BAF/SWI/SNF complex (BRG1 and two other core subunits), linking it to transcriptional regulation. | PMID:25169753 | American journal of medical genetics. Part C, Seminars in medical genetics |
| 2006 | Medium | ADNP directly interacts with chromatin at specific gene promoters (including apolipoproteins, cathepsins, neurogenesis markers such as Ngfr/neurogenin1/neurod1, and heart development markers like Myl2), acting to repress potential endoderm genes while enhancing organogenesis/neurogenesis genes; interaction with chromatin is increased in neuro-differentiated versus non-differentiated P19 cells. | PMID:17222401 | Developmental biology |
| 2008 | Medium | ADNP localizes differentially to the nucleus versus cytoplasm/neurites in neuronal-differentiated P19 cells compared to cardiovascular or non-differentiated cells; ADNP knockdown (~80% reduction) substantially reduces embryoid body formation and neurite numbers (~50%), placing ADNP in direct association with neuronal differentiation and maturation. | PMID:18286385 | Journal of molecular neuroscience : MN |
| 2014 | High | The NAP motif of ADNP contains an SxIP (SIP) microtubule end-binding protein (EB) interaction motif that binds EB1 and EB3 (but not EB2); NAP/ADNP-EB3 interaction increases PSD-95 expression in dendritic spines; EB1 or EB3 (but not EB2) silencing abolishes NAP-mediated cell protection; ADNP shows similar EB interactions enhanced by NAP treatment. | PMID:25178163 | Molecular psychiatry |
| 2017 | High | ADNP/NAP dramatically increases EB3 homodimer formation while decreasing EB1-EB3 heterodimer content; drives EB1- and EB3-Tau interactions (20-fold increases); recruits EB1/EB3 and Tau to microtubules under zinc intoxication. NAP protection against zinc intoxication requires Tau (or other MAPs), as NAP did not protect NIH3T3 fibroblasts unless transfected with Tau. | PMID:28115743 | Molecular psychiatry |
| 2012 | Medium | NAP (ADNP-derived peptide) significantly affects the alpha-tubulin tyrosination/detyrosination cycle in neuronal differentiation models (PC12 cells and rat cortical astrocytes), increases microtubule network area, increases tubulin beta3 (marker for neurite outgrowth), doubles dynamic microtubule invasion area in neuronal growth cones, and reverses zinc-decreased tau-tubulin-MT interaction. | PMID:23272107 | PloS one |
| 2012 | High | ADNP directly associates with (binds to) the mouse β-globin locus control region (by ChIP), and is required for erythroid maturation; knockdown of ADNP in zebrafish embryos or mouse erythroleukemia (MEL) cells inhibits erythroid maturation and hemoglobin production. ADNP also interacts with Brg1 (SWI/SNF component) in the context of erythropoiesis. | PMID:23071114 | The Journal of biological chemistry |
| 2015 | Medium | ADNP haploinsufficiency in mice exhibits co-immunoprecipitation with eIF4E (eukaryotic translation initiation factor 4E), with hippocampal eIF4E expression specifically increased in young ADNP+/- male mice; ADNP expression is a master regulator of key ASD and AD risk genes in a sex- and age-dependent manner. | PMID:25646590 | Translational psychiatry |
| 2014 | Low | ADNP interacts with Brahma (Brm), a SWI/SNF chromatin remodeling component that regulates alternative splicing, and with polypyrimidine tract-binding protein-associated splicing factor (PSF), a direct regulator of tau transcript splicing; immunoprecipitations in mouse brain tissue showed Brm-ADNP interaction coupled to ADNP-PSF binding. | PMID:24489906 | PloS one |
| 2020 | High | ADNP stabilizes β-catenin by binding to its armadillo domain, preventing association of β-catenin with key components of the degradation complex (Axin and APC); loss of ADNP promotes formation of the degradation complex and β-catenin degradation via the ubiquitin-proteasome pathway, resulting in downregulation of key neuroectoderm developmental genes. | PMID:32533114 | Nature communications |
| 2017 | Medium | FMDV leader protease (Lpro) interacts with ADNP (identified by mass spectrometry and confirmed in vitro and in cell culture); ADNP RNAi leads to reduced FMDV replication and increased IFN/ISG expression; FMDV infection recruits ADNP to IFN-α promoter sites; ADNP, Lpro, and Brg-1 (SWI/SNF) form a protein complex, and ADNP has a transcription repressive function on IFN expression. | PMID:28219017 | Virology |
| 2018 | Medium | ADNP mutations affect subcellular localization: mutations within the bipartite nuclear localization signal (NLS) stall the mutant protein in the cytoplasm; wild-type ADNP co-localizes with heterochromatin; certain mutant proteins show partially lost enrichment at pericentromeric heterochromatin; N-terminal truncated ADNP mutants are routed towards cytosolic proteasomal degradation (rescued by MG132). | PMID:29911927 | Cell cycle (Georgetown, Tex.) |
| 2021 | Medium | ADNP interacts with SIRT1 at two sites: (1) at the microtubule end-binding protein (EB1/EB3)-Tau level, with EB1/EB3 amplifying microtubule dynamics; and (2) on the DNA/chromatin site, sharing a DNA binding motif with YY1 and HDAC2, and regulating SIRT1, ADNP, and EB1 (MAPRE1). This ADNP-SIRT1 complex is associated with sex- and age-dependent altered histone modification via WD repeat-containing protein 5 (WDR5). | PMID:33967268 | Molecular psychiatry |
| 2016 | Medium | ADNP acts as a repressor of WNT signaling in colorectal cancer; silencing ADNP expression increases migration, invasion, and proliferation of colon cancer cells and accelerates tumor growth in xenografts in vivo. | PMID:27903678 | Clinical cancer research |
| 2022 | Medium | ADNP contains SH3 domain-ligand association sites (NAPVSIP motif) responsible for controlling cytoskeletal signaling; ADNP mutations differentially affect microtubule dynamics and Tau interactions; ADNP interacts with actin (co-immunoprecipitation from mouse brain), and NAP treatment normalizes Shank3-Adnp-actin interactions; NAP also contains an actin-binding site identified by ELM analysis. | PMID:35538192 | Molecular psychiatry |
| 2023 | High | ADNP forms a critical bridge in the transition from pioneer transcription factors to chromatin remodeling during Th2 cell differentiation: ADNP recruits CHD4 helicase and BRG1 ATPase (the ChAHP complex) following GATA3 and AP-1 binding; without ADNP, these pioneer TFs bind the type 2 cytokine locus but cannot initiate histone acetylation or DNA accessibility, resulting in impaired type 2 cytokine expression. | PMID:37285842 | Immunity |
| 2023 | High | ADNP is localized to the cytoplasm during neurite formation through interaction with 14-3-3 proteins (phosphorylation-dependent binding); inhibition of 14-3-3 with difopein blocks Adnp cytoplasmic localization; Adnp knockdown in cortical layer 2/3 pyramidal neurons via in utero electroporation alters neurite formation (increased basal dendrite number, increased axon length) and causes greater spontaneous calcium influx (especially in females) and increased interhemispheric connectivity. | PMID:36631597 | Molecular psychiatry |
| 2024 | High | ADNP counteracts stable association of CTCF at SINE B2-derived CTCF-binding sites during preimplantation development; Adnp knockout leads to impaired CTCF binding signal recovery, failed deposition of H3K9me3, and transcriptional derepression of SINE B2 elements during morula-to-blastocyst transition, resulting in unfaithful cell differentiation around implantation. | PMID:38479840 | Genes & development |
| 2025 | High | ADNP, as a core subunit of the ChAHP complex, recruits CHD4 to genes associated with progenitor proliferation during neocortical neurogenesis; in postmitotic neurons, ADNP and CHD4 co-regulate a network of neurodevelopmental disorder risk genes; conditional Adnp knockout during neocortical development impairs production of late-born upper-layer neurons. | PMID:39808658 | Proceedings of the National Academy of Sciences of the United States of America |
| 2022 | Medium | Different ADNP mutations (p.Pro403*/p.Ser404* and p.Tyr718*/p.Tyr719*) produce distinct neuronal phenotypes: p.Pro403* increases neurite numbers and lengths upon differentiation; p.Tyr718* decreases cell numbers; both mutations increase mutant protein in the cytoplasm and reduce nuclear/cytoplasmic boundary integrity (aberrant nuclear-cytoplasmic crosstalk), which is corrected by the NAP fragment. | PMID:36230962 | Cells |
| 2025 | Medium | In microglia, ADNP loss (CRISPRi knockdown) leads to altered endocytic trafficking, remodeled proteomes, and increased motility; ADNP functions as a modifier of microglial synaptic pruning. | PMID:40188316 | Molecular psychiatry |
| 2023 | Medium | NAP (ADNP-derived peptide) rapidly distributes in both cytoplasm and nucleus; disrupting microtubules by zinc or nocodazole intoxication mimics ADNP mutation phenotypes (aberrant nuclear-cytoplasmic boundaries) and NAP rapidly corrects this; NAP and ketamine both exhibit direct interactions with ADNP by in silico docking, but ketamine is ineffective at correcting mutant ADNP phenotypes while NAP is effective. | PMID:37759476 | Cells |
| 2023 | Medium | ADNP knockdown in mouse prefrontal cortex (via viral-based gene transfer) causes cognitive impairment, prominent upregulation of neuroinflammation genes (overlapping with POGZ deficiency), pro-phagocytic microglial activation, and significant decrease in glutamatergic transmission and postsynaptic protein expression. | PMID:35775424 | Brain : a journal of neurology |
| 2023 | Medium | Adnp haploinsufficiency in mice leads to hyperphosphorylated CaMKIIα and its substrates (including SynGAP1) in the adult hippocampus, and to excessive long-term potentiation (LTP); CaMKIIα inhibition normalizes the excessive LTP, linking ADNP to regulation of synaptic plasticity through CaMKIIα activity. | PMID:37365244 | Molecular psychiatry |
| 2025 | Medium | ADNP is a transcriptional target of POU3F2 in human neural progenitor cells, and mediates POU3F2's effects on canonical Wnt signaling; POU3F2 disruption reduces baseline Wnt signaling and decreases NPC proliferation, with ADNP identified as a downstream effector through unbiased analyses. | PMID:40498903 | Brain : a journal of neurology |
| 2006 | Medium | PACAP38 stimulates ADNP mRNA expression in mouse neuron-glia co-cultures via multiple receptor subtypes (PAC1-R at both sub-picomolar and nanomolar concentrations; VPAC1-R at nanomolar concentrations only); signaling is mediated through IP3/PLC pathway at both concentrations, and PKA pathway at nanomolar concentration only; MAPK inhibition has no effect. | PMID:16564114 | Peptides |
| 2024 | Medium | ADNP is essential for sex-dependent hippocampal neurogenesis: male Adnp+/- mice show dramatic reductions in BrdU incorporation in hippocampal sub-ventricular zone; mechanistically, male-specific downregulation of endoplasmic reticulum unfolded protein response genes and female-specific downregulation of mitochondrial ATP6 are observed; mitochondrial accessibility of ADNP is inhibited by the p.Tyr718* mutation. | PMID:39715923 | Molecular psychiatry |
| 2025 | Medium | Adnp heterozygous mutation (C-terminus) in mice causes significantly reduced glutamatergic and GABAergic synaptic transmission in PFC pyramidal neurons; treatment with an LSD1 inhibitor rescues synaptic transmission (particularly in females), associated with increased H3K4me2 and decreased H3K9me2/3 and elevated expression of synaptic genes; this links ADNP chromatin regulation (via LSD1/ADNP complex association) to synaptic gene expression. | PMID:40536108 | Autism research |

## Citations

- PMID:16564114
- PMID:17222401
- PMID:18286385
- PMID:23071114
- PMID:23272107
- PMID:24489906
- PMID:25169753
- PMID:25178163
- PMID:25646590
- PMID:27903678
- PMID:28115743
- PMID:28219017
- PMID:29911927
- PMID:32533114
- PMID:33967268
- PMID:35538192
- PMID:35775424
- PMID:36230962
- PMID:36631597
- PMID:37285842
- PMID:37365244
- PMID:37759476
- PMID:38479840
- PMID:39715923
- PMID:39808658
- PMID:40188316
- PMID:40498903
- PMID:40536108
