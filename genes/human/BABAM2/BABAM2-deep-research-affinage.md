---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BABAM2
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NXR7
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 16
citation_count: 16
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for BABAM2 (human)

## Current model (mechanistic narrative)

BABAM2 (BRE/BRCC45) is a scaffold/adaptor protein that integrates two broad cellular programs: DNA-damage response and the control of receptor-triggered apoptosis [PMID:9737713, PMID:21282113]. In the nucleus it is a shared component of two BRCC36-containing deubiquitinase complexes—the BRCA1-A and BRISC/ABRO1 complexes—where its C-terminal UEV domain binds NBA1/MERIT40, an interaction required for complex integrity, cellular resistance to ionizing radiation, and recruitment of BRCA1 to DNA damage sites for homologous-recombination repair [PMID:21282113, PMID:27001068]. Through this DNA-damage axis BABAM2 also stabilizes the CDC25A phosphatase by recruiting the deubiquitylase USP7, opposing CDC25A degradation and permitting cell-cycle progression after damage; loss of BABAM2 causes G1 retention, CDC25A/CDK2 loss, and prolonged p53 activation [PMID:29416040, PMID:33050379]. At the cell surface, BABAM2 was first identified as a binding partner of the TNFR1 juxtamembrane domain that dampens TNF-induced NF-κB signaling, and it additionally binds Fas to inhibit the mitochondrial apoptotic pathway downstream of death receptors, an antiapoptotic role confirmed in vivo by resistance of liver-specific transgenic mice to Fas-mediated hepatic apoptosis [PMID:9737713, PMID:15465831, PMID:17704801]. BABAM2 further restrains apoptosis by maintaining XIAP protein and mRNA levels [PMID:24395041]. The protein also participates in developmental and lineage programs: it promotes Mdm2-mediated p53 ubiquitination and degradation to favor osteoblast differentiation, suppresses osteoclastogenesis by interacting with Hey1 to inhibit Nfatc1 transcription, and supports satellite-cell migration during muscle regeneration by protecting CXCR4 from SDF-1α-induced degradation [PMID:28436570, PMID:35864959, PMID:26740569].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-5357801 Programmed Cell Death, R-HSA-1640170 Cell Cycle
- **partners:** NBA1/MERIT40, TNFR1, FAS, USP7, TP53, HEY1, CXCR4
- **complexes:** BRCA1-A complex, BRISC complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | High | BRE was identified as a binding partner of the juxtamembrane domain of the p55 TNF receptor (TNFR1) via yeast two-hybrid screen, confirmed by in vitro biochemical assay using recombinant fusion proteins and co-immunoprecipitation in transfected mammalian cells. Overexpression of BRE inhibited TNF-induced NF-κB activation, indicating BRE modulates TNF-α signal transduction. | PMID:9737713 | FASEB journal |
| 2004 | High | BRE binds to Fas (in addition to TNFR1) and inhibits the mitochondrial apoptotic pathway downstream of death receptor activation. BRE dissociates rapidly from TNFR1 (but not Fas) upon receptor ligation, and associates with phosphorylated, sumoylated, and ubiquitinated proteins after death receptor stimulation. Knockdown of BRE by siRNA increased apoptosis specifically to death receptor-mediated (TNF-α) stimuli, but not etoposide, establishing a specific physiological role in death receptor-mediated apoptosis. | PMID:15465831 | The Journal of biological chemistry |
| 2011 | High | BRE is a common component of two distinct BRCC36-containing deubiquitinase complexes: the nuclear Abraxas-BRCA1 complex and the cytoplasmic ABRO1 complex. BRE interacts with NBA1/MERIT40 through a C-terminal UEV domain of BRE and a C-terminal conserved motif of NBA1; this NBA1-BRE interaction is critical for maintaining the integrity of both complexes. Knockdown of BRE leads to decreased levels of components of both BRCC36-containing complexes, and the NBA1-BRE interaction is required for cellular resistance to ionizing radiation and for BRCA1 recruitment to DNA damage sites. | PMID:21282113 | The Journal of biological chemistry |
| 2018 | High | BRE (BRCC45) promotes survival of BRCA2-deficient cells by stabilizing CDC25A phosphatase through recruitment of deubiquitylase USP7. In the presence of DNA damage, BRE facilitates USP7-mediated deubiquitylation of CDC25A, preventing its degradation and enabling cell cycle progression. | PMID:29416040 | Nature communications |
| 2014 | Medium | BRE maintains cellular XIAP protein levels (the most potent endogenous caspase inhibitor) through a mechanism that involves transcriptional and post-transcriptional regulation of XIAP. shRNA-mediated depletion of BRE reduced XIAP protein and mRNA levels and sensitized cells to apoptosis from both death receptor (TNF-α) and genotoxic (etoposide) stimuli; reconstitution of BRE restored XIAP levels and apoptotic resistance. | PMID:24395041 | Apoptosis |
| 2005 | Medium | Blocking BRE expression in mouse Leydig tumor cells (using antisense probes) impaired steroidogenesis specifically at the pregnenolone-to-progesterone conversion step, accompanied by reduced 3β-hydroxysteroid dehydrogenase type I (3β-HSDI) mRNA expression, without affecting StAR or P450scc expression or cAMP production. This establishes a role for BRE in steroidogenesis through regulation of 3β-HSD transcription. | PMID:15930177 | The Journal of endocrinology |
| 2016 | Medium | BRE is required for the BRCA1-A complex recruitment and homologous recombination (HR)-dependent DNA repair. BRE-/- fibroblasts showed persistent γ-H2AX foci after gamma irradiation, impaired BRCA1-A complex recruitment to DNA damage sites, and earlier replicative senescence compared to wild-type cells. | PMID:27001068 | Scientific reports |
| 2017 | Medium | BRE promotes Mdm2-mediated p53 ubiquitination and degradation by physically interacting with p53, thereby promoting osteoblast differentiation. Knockdown of BRE in bone marrow mesenchymal cells led to p53 pathway activation (increased p53, p21, Mdm2); inhibition of p53 by siRNA or pifithrin-α rescued the impaired osteogenesis caused by BRE knockdown. | PMID:28436570 | Stem cells |
| 2022 | Medium | Babam2 (BRE) negatively regulates osteoclastogenesis by interacting with Hey1 to inhibit Nfatc1 transcription. Babam2 knockdown accelerated osteoclast formation; Babam2 overexpression blocked it. Transgenic Babam2 mice had increased bone mass and reduced bone resorption. Silencing Hey1 diminished the inhibitory effects of Babam2 on osteoclastogenesis, placing Hey1 downstream of Babam2 in this pathway. | PMID:35864959 | International journal of biological sciences |
| 2020 | Medium | Loss of Babam2 (BRE) in mouse embryonic stem cells causes abnormal G1 phase retention in response to DNA damage (gamma irradiation or doxorubicin), with degradation of CDC25A and CDK2, prolonged p53 activation, and p53-mediated suppression of Nanog expression, reducing developmental pluripotency. | PMID:33050379 | Biomedicines |
| 2016 | Medium | BRE facilitates skeletal muscle satellite cell migration and differentiation during muscle regeneration. BRE-KO mice showed impaired muscle regeneration with fewer Pax7+ satellite cells. BRE normally protects CXCR4 from SDF-1α-induced degradation, thereby maintaining responsiveness to the chemoattractant SDF-1α. BRE-KO satellite cells showed significantly reduced velocity of movement and diminished chemotactic response to SDF-1α. | PMID:26740569 | Biology open |
| 2017 | Medium | BRE overexpression in the chick neural tube increased HNK-1+ neural crest cell migration and TuJ-1+ neurite outgrowth, and was associated with changes in BMP4 and Shh expression in the neural tube. Silencing BRE produced inverse effects. BRE effects on somitogenesis were indirect, mediated through altered BMP4/Shh signaling. | PMID:25568339 | Molecular biology of the cell |
| 2006 | Medium | BRE knockdown by siRNA in C2C12 cells resulted in increased cell proliferation and reduced p53 and prohibitin expression; overexpression of BRE in D122 cells decreased proliferation and upregulated p53 and prohibitin. Proteomic analysis showed BRE regulates prohibitin, 26S proteasome regulatory subunit S14, Akt-3, and carbonic anhydrase III. | PMID:16518872 | Proteomics |
| 2007 | Medium | Liver-specific BRE transgenic mice were significantly resistant to Fas-mediated lethal hepatic apoptosis in vivo, confirming BRE's antiapoptotic role in vivo. The study also revealed post-transcriptional regulation of BRE in normal liver (absent in HCC cells). | PMID:17704801 | Oncogene |
| 2020 | Low | BRE overexpression activates AKT phosphorylation and promotes esophageal squamous cell carcinoma (ESCC) cell growth and apoptotic resistance. Pharmacological inhibition of AKT (MK2206) abrogated BRE-induced cell growth, placing AKT signaling downstream of BRE in ESCC cells. | PMID:32850455 | Frontiers in oncology |
| 2001 | Low | Human BRE is expressed as at least six alternative mRNA isoforms generated by alternative splicing predominantly at either end of the gene. Isoform alpha(a), carrying a C-terminal peroxisomal targeting sequence, is the most abundant. LPS treatment of peripheral blood monocytes downregulates all BRE isoforms. | PMID:11676476 | Biochemical and biophysical research communications |

## Citations

- PMID:11676476
- PMID:15465831
- PMID:15930177
- PMID:16518872
- PMID:17704801
- PMID:21282113
- PMID:24395041
- PMID:25568339
- PMID:26740569
- PMID:27001068
- PMID:28436570
- PMID:29416040
- PMID:32850455
- PMID:33050379
- PMID:35864959
- PMID:9737713
