---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATXN3
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P54252
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 24
citation_count: 24
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ATXN3 (human)

## Current model (mechanistic narrative)

ATXN3 is a Josephin-family deubiquitinating enzyme that maintains protein homeostasis through the ubiquitin-proteasome system, with knockout animals accumulating ubiquitinated proteins in vivo [PMID:17764659]. It removes ubiquitin from a broad range of substrates to control their stability, including HDAC3 during antiviral interferon-I signaling [PMID:29802126], the transcription factors KLF4 [PMID:31563563], YAP via Josephin-domain engagement of the YAP WW domain with K48-linkage specificity [PMID:37349820], and JunB/IRF1/STAT3/HIF-2α to drive PD-L1 expression in tumor cells [PMID:38038129]. Beyond catalysis, ATXN3 operates in genome maintenance as a component of a transcription-coupled DNA repair complex with RNA polymerase II, PNKP and CBP, where its activity protects CBP from ubiquitin-mediated degradation and supports global transcription and error-free double-strand break repair [PMID:30994454, PMID:32205441]. It also functions through a catalytic-independent activity to organize chromatin, controlling HDAC3 subcellular localization and chromatin recruitment, with loss producing abnormal nuclear morphology, altered replication timing and epigenetic marks [PMID:36971114, PMID:30231063]. Nuclear entry of ATXN3 is gated by CK2/GSK3 phosphorylation of serine 29 within the Josephin domain [PMID:20347968], and the protein is processed by calpains and caspases to generate C-terminal fragments [PMID:23100324, PMID:19783548]. ATXN3 also participates in ER-associated retrotranslocation, deubiquitinating type II iodothyronine deiodinase as it is extracted via the p97 ATPase [PMID:24196352]. Polyglutamine expansion causes the SCA3/MJD spinocerebellar ataxia through multiple toxic mechanisms: nuclear inclusion formation that sequesters the proteasome [PMID:10072437], physical inactivation of PNKP leading to persistent DNA damage and ATM-mediated apoptotic signaling [PMID:25590633], cell-autonomous impairment of oligodendrocyte maturation [PMID:35042771], potassium channel dysfunction [PMID:16765348], and toxicity arising from -1 ribosomal frameshifting at the expanded CAG repeat rather than the polyQ tract alone [PMID:16087686, PMID:22337953].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016787 hydrolase activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol, GO:0005730 nucleolus
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-73894 DNA Repair, R-HSA-4839726 Chromatin organization, R-HSA-74160 Gene expression (Transcription), R-HSA-168256 Immune System, R-HSA-1643685 Disease
- **partners:** PNKP, HDAC3, POLR2A, CBP, YAP, KLF4, JUNB, P97/VCP
- **complexes:** transcription-coupled DNA repair complex (RNAP II / PNKP / CBP)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | Medium | The 26S proteasome complex redistributes into polyglutamine aggregates in SCA3/MJD; in neurons from SCA3/MJD brain, the proteasome localizes to intranuclear inclusions containing mutant ataxin-3. Proteasome inhibitors caused a repeat length-dependent increase in aggregate formation, implying the proteasome directly suppresses polyglutamine aggregation. Inclusion formation by full-length mutant ataxin-3 required nuclear localization of the protein and occurred within PML oncogenic domains. | PMID:10072437 | Human molecular genetics |
| 2007 | High | Loss of Atxn3 in knockout mice increased levels of ubiquitinated proteins in vivo, providing direct evidence for ATXN3's deubiquitinating activity in a physiological context. Atxn3 ko mice showed no overt neurological abnormality on rotarod but displayed reduced exploratory behavior. | PMID:17764659 | Biochemical and biophysical research communications |
| 2010 | High | CK2 and GSK3 phosphorylate ATXN3 on serine 29 within the Josephin domain, and this phosphorylation promotes nuclear uptake of ATXN3. Site-directed mutagenesis of S29 to alanine strongly reduced nuclear localization, while phospho-mimic S29D restored wild-type nuclear localization. Treatment with CK2 and GSK3 inhibitors prevented S29 phosphorylation and inhibited nuclear uptake. | PMID:20347968 | Biochimica et biophysica acta |
| 2012 | High | Calpain-2 cleaves ataxin-3 in vitro and in mouse brain homogenates, and polyglutamine-expanded ataxin-3 is more sensitive to calpain-mediated degradation than wild-type. In vivo, enhancing calpain activity (via calpastatin knockout in SCA3 transgenic mice) aggravated neurological phenotype, increased nuclear aggregate number, and accelerated cerebellar neurodegeneration. | PMID:23100324 | Human molecular genetics |
| 2009 | Medium | Ataxin-3 protein cleavage (likely caspase-dependent) is conserved in Drosophila models of SCA3, and preventing cleavage by mutating caspase cleavage sites reduces neuronal loss in vivo, demonstrating that ataxin-3 cleavage enhances neurotoxicity. | PMID:19783548 | Human molecular genetics |
| 2015 | High | Mutant ATXN3 (polyQ-expanded) physically interacts with and inactivates the DNA repair enzyme PNKP, resulting in inefficient DNA strand break repair, persistent DNA damage accumulation, and chronic ATM activation leading to p53 and PKC-δ pro-apoptotic signaling and neuronal death in SCA3. PNKP overexpression or ATM inhibition blocked mutant ATXN3-mediated cell death. | PMID:25590633 | PLoS genetics |
| 2019 | High | Mutant HTT impairs a transcription-coupled DNA repair (TCR) complex that includes ATXN3, POLR2A, PNKP, and CBP. Within this complex, ATXN3 activity prevents CBP ubiquitination and degradation; loss of ATXN3 function in HD leads to CBP degradation, impairing transcription and DNA repair. Wild-type ATXN3 thus protects CBP from ubiquitin-mediated degradation as part of the TCR complex. | PMID:30994454 | eLife |
| 2020 | High | ATXN3 associates with RNA polymerase II (RNAP II) and classical non-homologous end-joining (C-NHEJ) proteins including PNKP along with nascent RNAs under physiological conditions. ATXN3 depletion significantly decreases global transcription, repair of transcribed genes, and error-free double-strand break repair. Brain extracts from SCA3 patients show lower PNKP activity, elevated 53BP1, more DNA strand breaks in transcribed genes, and degradation of RNAP II. PNKP complementation completely rescues SCA3 phenotype in Drosophila. | PMID:32205441 | Proceedings of the National Academy of Sciences of the United States of America |
| 2018 | Medium | ATXN3 physically interacts with HDAC3, deubiquitinates HDAC3, and thereby stabilizes HDAC3 protein. This ATXN3/HDAC3 interaction increases during viral infection and promotes IFN-I-mediated signaling pathway (not IFN-I production itself) to enhance antiviral response in murine primary lung cells and human cell lines. | PMID:29802126 | Journal of immunology |
| 2019 | Medium | ATXN3 binds to KLF4 via immunoprecipitation and acts as a deubiquitinating enzyme for KLF4, mediating its deubiquitination and stabilization, thereby promoting breast cancer cell metastasis in vitro and in vivo. | PMID:31563563 | Cancer letters |
| 2023 | Medium | CRISPR screen identified ATXN3 as a positive regulator of PD-L1 transcription. ATXN3 deubiquitinates the AP-1 transcription factor JunB and also stabilizes IRF1, STAT3, and HIF-2α, transcription factors that drive PD-L1 expression in response to IFN-γ and hypoxia. ATXN3 deletion abolished IFN-γ- and hypoxia-induced PD-L1 expression. | PMID:38038129 | The Journal of clinical investigation |
| 2023 | Medium | ATXN3 acts as a deubiquitinase for YAP in prostate cancer: the Josephin domain of ATXN3 interacts with the WW domain of YAP, deubiquitylates YAP (specifically inhibiting K48-linked polyubiquitination), and stabilizes YAP protein, thereby promoting YAP/TEAD target gene expression (CTGF, ANKRD1, CYR61) and prostate cancer cell proliferation and invasion. | PMID:37349820 | Cell communication and signaling |
| 2021 | Low | ATXN3 promotes anaplastic thyroid carcinoma progression by directly binding to EIF5A2 and reducing its K48-linked ubiquitination and proteasomal degradation, thereby stabilizing EIF5A2 expression. | PMID:34428509 | Molecular and cellular endocrinology |
| 2013 | Medium | The type II iodothyronine deiodinase (D2) undergoes retrotranslocation from the ER to the cytoplasm via a p97-ATPase complex, and during this process, Ataxin-3 (Atx3) deubiquitinates ubiquitinated D2 (UbD2). Inhibiting Atx3 with eeyarestatin-I did not affect D2:p97 binding but decreased UbD2 retrotranslocation and caused ER accumulation of high-molecular-weight UbD2. | PMID:24196352 | Molecular endocrinology |
| 2018 | Medium | Loss of ATXN3 in null mouse embryonic fibroblasts altered transcription of multiple signal transduction pathways, including depressed Wnt and BMP4 and elevated Prolactin, TGF-β, and Ephrin pathways. The most upregulated gene was Efna3 (Ephrin receptor A3), associated with hyperacetylation of histones H3 and H4 at the Efna3 promoter and decreased HDAC3 and NCoR levels in ATXN3-null cells. Overexpression of normal or expanded ATXN3 suppressed Efna3 expression. | PMID:30231063 | PloS one |
| 2023 | High | ATXN3 regulates chromatin organization in a catalytic-independent (deubiquitinase-independent) manner. Loss of ATXN3 leads to abnormal nuclear and nucleolar morphology, altered DNA replication timing, increased global transcription, increased histone H1 mobility, changes in epigenetic marks, and higher chromatin sensitivity to MNase digestion. ATXN3 controls the subcellular localization of HDAC3 (its interaction partner), and absence of ATXN3 decreases HDAC3 chromatin recruitment. PolyQ-expanded ATXN3 behaves as a null mutant in these assays, altering DNA replication parameters, epigenetic marks, and HDAC3 subcellular distribution. | PMID:36971114 | Nucleic acids research |
| 2004 | Medium | The misfolding propensity and ubiquitination of ataxin-3 are directly proportional to the length of the polyglutamine repeat and inversely dependent on the size of the protein. Normal-repeat ataxin-3 (full-length and truncated) is not ubiquitinated, whereas expanded-polyQ ataxin-3 is ubiquitinated in proportion to its misfolding propensity. | PMID:15639784 | Neurotoxicity research |
| 2013 | Medium | In Drosophila SCA3 models, Hsp104 suppressed toxicity of a C-terminal ataxin-3 fragment containing the expanded polyQ tract but unexpectedly enhanced aggregation and toxicity of full-length pathogenic ataxin-3. Hsp104 suppressed toxicity of MJD variants lacking part of the N-terminal deubiquitylase domain and variants unable to engage polyubiquitin, indicating that MJD-ubiquitin interactions hinder protective Hsp104 function. This demonstrates that the ubiquitin-binding capacity of ataxin-3 is functionally important for its behavior in protein disaggregation contexts. | PMID:24039611 | PLoS genetics |
| 2017 | Medium | The truncated C-terminal fragment of mutant ATXN3 causes more mitochondrial fission, decreases expression of mitochondrial fusion markers Mfn-1 and Mfn-2, reduces mitochondrial membrane potential, increases reactive oxygen species, and leads to higher cell death than full-length mutant ATXN3 in neuroblastoma cells and transgenic mice. | PMID:28676741 | Frontiers in molecular neuroscience |
| 2006 | Medium | Neuronally differentiated PC12 cells expressing expanded ataxin-3 showed significantly reduced resting membrane potential and a hyperpolarizing shift of the delayed rectifier potassium current activation curve, prior to neuronal cell death, indicating that mutant ataxin-3 causes potassium channel dysfunction. | PMID:16765348 | Experimental neurology |
| 2022 | High | Oligodendrocyte maturation is impaired early in SCA3 disease in selectively vulnerable brain regions (cerebellum and brainstem) of SCA3 transgenic mice. This impairment is a cell-autonomous toxic gain-of-function of mutant ATXN3, as ATXN3 KO mice show no oligodendrocyte maturation defects. Ultrastructural microscopy confirmed abnormalities in axonal myelination in SCA3 mice. | PMID:35042771 | The Journal of neuroscience |
| 2005 | Medium | Ribosomal frameshifting occurs at the expanded CAG repeat in ATXN3 mRNA, specifically by -1 slippage, generating polyalanine-containing proteins. This frameshifting is dependent on long CAG tract length. PolyQ-encoding CAA repeats (which cannot frameshift) were not toxic, while expanded CAG ATXN3 was toxic, indicating that frameshifting (not the polyQ per se) contributes to toxicity. Anisomycin reduced -1 frameshifting and also reduced toxicity. | PMID:16087686 | Human molecular genetics |
| 2012 | Medium | Frameshifting events occurring at the expanded CAG repeat in ATXN3 are toxic in Drosophila and mammalian neurons. Transgenic expression of expanded CAG ATXN3 led to -1 frameshifting, whereas expression of polyglutamine-encoding expanded CAA ATXN3 (which cannot frameshift) was not toxic, demonstrating that expanded CAG-derived frameshifting (not polyQ per se) is necessary for toxicity in these models. | PMID:22337953 | Human molecular genetics |
| 2015 | Medium | ATXN3 does not interact with the ubiquitin-binding protein UBQLN2 (tested by Co-IP via UBA domain), in contrast to mutant HTT which does interact with UBQLN2. Consequently, UBQLN2 is not recruited to inclusions in SCA3 (neither in mouse models nor human SCA3 brain), distinguishing SCA3 inclusions from HD inclusions. | PMID:26141599 | Neurobiology of disease |

## Citations

- PMID:10072437
- PMID:15639784
- PMID:16087686
- PMID:16765348
- PMID:17764659
- PMID:19783548
- PMID:20347968
- PMID:22337953
- PMID:23100324
- PMID:24039611
- PMID:24196352
- PMID:25590633
- PMID:26141599
- PMID:28676741
- PMID:29802126
- PMID:30231063
- PMID:30994454
- PMID:31563563
- PMID:32205441
- PMID:34428509
- PMID:35042771
- PMID:36971114
- PMID:37349820
- PMID:38038129
