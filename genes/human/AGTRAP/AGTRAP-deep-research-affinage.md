---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AGTRAP
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q6RW13
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 21
citation_count: 21
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AGTRAP (human)

## Current model (mechanistic narrative)

AGTRAP (ATRAP) is a multi-pass transmembrane protein that functions as a negative regulator of angiotensin II type 1 receptor (AT1R) signaling, binding specifically to the carboxyl-terminal cytoplasmic tail of the AT1a receptor and not to other G-protein-coupled receptors [PMID:10358057, PMID:12960423]. It localizes to the plasma membrane and to intracellular trafficking vesicles (ER, Golgi, endocytic vesicles), with constitutive translocation toward the plasma membrane; its cytoplasmic C-terminal domain is required for AT1R binding [PMID:12960423]. Through this interaction ATRAP promotes AT1R internalization and surface downregulation, thereby suppressing downstream AT1R-mediated signaling including phospholipase C activation, p38 MAPK, STAT3, and Akt, and attenuating angiotensin II-induced proliferative and hypertrophic responses in vascular smooth muscle cells and cardiomyocytes [PMID:10358057, PMID:11162453, PMID:15757644]. Genetic deletion in mice establishes ATRAP as a physiological negative regulator: Atrap-deficient animals show elevated blood pressure, increased plasma volume, and enhanced renal AT1R surface expression [PMID:20093357], and additionally develop high-fat-diet-driven metabolic dysfunction that is rescued by transplantation of ATRAP-overexpressing adipose tissue [PMID:23902639]. Beyond AT1R, ATRAP interacts with the cardiac sarcoplasmic reticulum Ca2+-ATPase SERCA2a and enhances SERCA-dependent Ca2+ uptake to facilitate ventricular relaxation [PMID:27015675]. ATRAP abundance is tightly controlled post-translationally by proteasomal and immunoproteasomal degradation—notably via the immunoproteasome subunit β5i (PSMB8), whose action de-represses AT1R-driven NF-κB, NADPH oxidase, and TGF-β1/Smad signaling [PMID:25526681, PMID:30571551]—and post-transcriptionally by miR-125a/b-5p and miR-34a [PMID:37981211, PMID:41291382]. In cancer, ATRAP operates independently of AT1R, driving a USP14/PBX3/AKT-mTOR axis in breast cancer [PMID:35414770] and an IL-6/JAK2/STAT3 pathway in glioma [PMID:41689202].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005886 plasma membrane, GO:0005783 endoplasmic reticulum, GO:0005794 Golgi apparatus, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-9609507 Protein localization, R-HSA-392499 Metabolism of proteins
- **partners:** AGTR1, RACK1, PITPNC1, ATP2A2, USP14, PBX3, PSMB8, PSMB10
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | High | ATRAP (AGTRAP) was identified as a novel protein that specifically interacts with the carboxyl-terminal cytoplasmic domain of the AT1a receptor but not with AT2, m3 muscarinic, bradykinin B2, endothelin B, or beta2-adrenergic receptors. Overexpression of ATRAP in COS-7 cells markedly inhibited AT1a receptor-mediated activation of phospholipase C without affecting m3 receptor-mediated activation. | PMID:10358057 | The Journal of biological chemistry |
| 2000 | Medium | Overexpression of ATRAP potentiated AT1 receptor internalization upon angiotensin II stimulation in vascular smooth muscle cells (VSMCs) and inhibited AT1 receptor-induced DNA synthesis, associated with inhibition of STAT3 and Akt phosphorylation. | PMID:11162453 | Biochemical and biophysical research communications |
| 2002 | High | Human AGTRAP protein interacts with RACK1 (Receptor of Activated Protein C Kinase), as identified by yeast two-hybrid screening and confirmed by GST pull-down, co-immunoprecipitation, and surface plasmon resonance. | PMID:11733189 | The international journal of biochemistry & cell biology |
| 2003 | High | ATRAP is a transmembrane protein with three N-terminal hydrophobic domains (residues 14-36, 55-77, 88-108) and a hydrophilic C-terminal cytoplasmic tail (residues 109-161). Its N-terminus faces extracellularly, it localizes to intracellular trafficking vesicles (ER, Golgi, endocytic vesicles) and plasma membrane with constitutive translocation toward the plasma membrane. Deletion of the C-terminal domain abolishes AT1 receptor binding and causes perinuclear vesicle clustering. ATRAP overexpression decreases inositol lipid generation, suppresses angiotensin II-stimulated c-fos promoter activity, and decreases cell proliferation. | PMID:12960423 | Molecular biology of the cell |
| 2005 | Medium | Overexpression of ATRAP significantly decreases the number of AT1 receptors on the surface of cardiomyocytes, decreases p38 MAPK phosphorylation, reduces c-fos promoter activity, and decreases protein synthesis upon angiotensin II treatment, indicating ATRAP promotes AT1R downregulation and attenuates hypertrophic responses. | PMID:15757644 | FEBS letters |
| 2006 | Medium | ATRAP protein colocalizes with AT1 receptor in renal tubular cells in vivo, distributed along nephron segments from Bowman's capsules to inner medullary collecting ducts. Dietary salt depletion significantly decreased renal expression of both ATRAP and AT1 receptor. | PMID:16514431 | Kidney international |
| 2008 | Medium | ATRAP is expressed in differentiated brown and white adipocytes; beta3-adrenergic stimulation suppresses ATRAP expression through JAK2/STAT signaling, as inhibition of PKA and JAK2 reversed the beta3-adrenergic suppression of ATRAP expression. | PMID:18236361 | Hormone and metabolic research |
| 2010 | High | Atrap-deficient (Atrap-/-) mice show increased arterial blood pressure, increased plasma volume, lower plasma renin concentration, and enhanced surface expression of AT1 receptors in the renal cortex with increased carboanhydrase-sensitive proximal tubular function, demonstrating that Atrap acts as a negative regulator of AT1 receptors in renal tubules in vivo. | PMID:20093357 | Journal of the American Society of Nephrology |
| 2011 | Medium | The PITP domain of RdgBβ (PITPNC1) interacts with ATRAP (AGTRAP), an integral membrane protein. Upon PMA treatment, RdgBβ is recruited to membranes via its PITP domain through interaction with ATRAP. | PMID:21728994 | The Biochemical journal |
| 2013 | High | Agtrap-/- mice under high-fat dietary loading develop systemic metabolic dysfunction including increased fat accumulation, hypertension, dyslipidemia, insulin resistance, and adipose tissue inflammation. Subcutaneous transplantation of fat pads overexpressing ATRAP (from transgenic mice) to Agtrap-/- mice improved the systemic metabolic dysfunction, demonstrating a protective role of adipose ATRAP against insulin resistance. | PMID:23902639 | Journal of the American Heart Association |
| 2014 | Medium | Proteasomal degradation of ATRAP occurs during angiotensin II-induced cardiac hypertrophy; proteasome inhibitor bortezomib blocked ATRAP degradation and attenuated AT1R-mediated p38 MAPK and STAT3 signaling pathways, thereby reducing cardiac hypertrophy, fibrosis, and inflammation. | PMID:25526681 | Journal of molecular and cellular cardiology |
| 2016 | High | ATRAP interacts with the cardiac Ca2+-ATPase SERCA2a, confirmed by pull-down (MALDI-MS), co-immunoprecipitation, and surface plasmon resonance. ATRAP enhances SERCA-dependent Ca2+ uptake in isolated SR membrane vesicles. Atrap-/- myocytes show prolonged Ca2+ transient decay and sarcomere re-lengthening, and Atrap-/- mice have decreased maximum ventricular filling rate, indicating ATRAP facilitates ventricular relaxation via SERCA2a stimulation. | PMID:27015675 | Cardiovascular research |
| 2019 | High | Immunoproteasome subunit β5i (PSMB8) directly targets ATRAP for degradation. β5i knockout attenuated Ang II-induced atrial fibrillation, fibrosis, and oxidative stress, while restoring ATRAP levels. Overexpression of ATRAP abrogated Ang II-induced atrial remodeling and AF in β5i-overexpressing mice. Mechanistically, β5i-mediated ATRAP degradation leads to activation of AT1R-mediated NF-κB signaling, increased NADPH oxidase activity, and TGF-β1/Smad signaling. | PMID:30571551 | Hypertension |
| 2019 | Medium | Proximal tubule-specific ATRAP knockout (PT-KO) mice showed no significant difference in blood pressure at baseline or in pressor response to angiotensin II infusion compared to wild-type mice, indicating that ATRAP in renal proximal tubules has a minor role in angiotensin-dependent hypertension in vivo. | PMID:30977419 | Journal of the American Heart Association |
| 2021 | Medium | SAM (S-adenosylmethionine) upregulates ATRAP protein expression in NAFLD by methylating HuR protein, which controls HuR subcellular localization; HuR directly binds ATRAP mRNA and controls its nucleocytoplasmic shuttling for export from the nucleus, thereby regulating ATRAP translation. | PMID:33753727 | Cell death & disease |
| 2022 | Medium | In breast cancer cells, ATRAP directs USP14 (Ubiquitin-specific protease 14)-mediated deubiquitination and stabilization of PBX3 (Pre-B cell leukemia homeobox 3), and promotes AKT/mTOR signaling pathway activation; ATRAP is itself a transcriptional target of USF1 (Upstream stimulatory factor 1). | PMID:35414770 | International journal of biological sciences |
| 2022 | Medium | DJ-1 (PARK7) in hypoxia-conditioned MSC-derived extracellular vesicles suppresses cardiac hypertrophy by directly physically interacting with and inhibiting proteasome subunit PSMB10 activity, which in turn reduces ubiquitination-mediated degradation of ATRAP, thereby preserving AT1R-mediated signaling inhibition. | PMID:36509316 | Pharmacological research |
| 2022 | Medium | Tubular ATRAP-mediated modulation of AT1R signaling regulates the accumulation of tubulointerstitial M2-polarized macrophages (marked by CD206), thereby affecting glomerular injury in diabetic nephropathy via tubule-glomerular crosstalk. Adoptive transfer of M2 macrophages into diabetic ATRAP-knockout mice ameliorated glomerular injury. | PMID:35240129 | Kidney international |
| 2023 | Medium | miR-125a-5p and miR-125b-5p directly repress ATRAP/Atrap mRNA expression. Inhibition of miR-125a-5p/miR-125b-5p suppresses Ang II-AT1R signaling in mouse distal convoluted tubule cells by increasing ATRAP levels. | PMID:37981211 | The Journal of biological chemistry |
| 2025 | Medium | miR-34a directly targets AGTRAP mRNA in human aortic smooth muscle cells (HASMC); Ang II upregulates miR-34a, which suppresses AGTRAP and SIRT1 expression; forced AGTRAP expression rescues miR-34a-induced pro-inflammatory gene upregulation (IL-6, COX2, MCP-1, MFGE8), establishing a negative feedback loop where AGTRAP downmodulation further enhances miR-34a expression. | PMID:41291382 | GeroScience |
| 2026 | Medium | AGTRAP knockdown in glioma cells suppressed proliferation, increased apoptosis, reduced IL-6 mRNA and protein levels, and attenuated JAK2/STAT3 activation; recombinant IL-6 partially restored JAK2/STAT3 signaling and mitigated growth inhibition caused by AGTRAP silencing, placing AGTRAP upstream of IL-6/JAK2/STAT3 in glioma. | PMID:41689202 | CNS neuroscience & therapeutics |

## Citations

- PMID:10358057
- PMID:11162453
- PMID:11733189
- PMID:12960423
- PMID:15757644
- PMID:16514431
- PMID:18236361
- PMID:20093357
- PMID:21728994
- PMID:23902639
- PMID:25526681
- PMID:27015675
- PMID:30571551
- PMID:30977419
- PMID:33753727
- PMID:35240129
- PMID:35414770
- PMID:36509316
- PMID:37981211
- PMID:41291382
- PMID:41689202
