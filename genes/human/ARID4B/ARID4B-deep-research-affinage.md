---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARID4B
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q4LE39
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

# Affinage mechanistic annotation for ARID4B (human)

## Current model (mechanistic narrative)

ARID4B is a chromatin-associated transcriptional regulator that operates within histone-modifying complexes to control developmental, reproductive, and oncogenic gene programs [PMID:17043311, PMID:33454011]. It physically partners with its paralog ARID4A and, together with that protein, functions in epigenetic complexes that maintain repressive histone trimethylation (H3K9, H4K20) and DNA methylation at imprinted loci such as the PWS/AS domain, where combined Arid4a/Arid4b deficiency shifts the maternal allele toward a paternal epigenotype [PMID:17043311]. Within the SIN3A complex, ARID4B interacts specifically with HDAC1 (and not HDAC2) and with the corepressor components mSIN3A/mSDS3, and its activity governs the balance of H3K27 acetylation versus H3K27 trimethylation at developmental gene loci, where it is required for embryonic stem cell differentiation toward mesoderm and endoderm [PMID:33454011, PMID:22693453]. ARID4A and ARID4B act as transcriptional coactivators for the androgen receptor (AR) and the retinoblastoma protein (RB); in Sertoli cells, ARID4B is required for AR-dependent activation of target genes including Rhox5, and its loss causes complete male infertility with spermatogenic arrest, blood-testis barrier defects, and failure of spermatogonial stem cell niche establishment through dysregulation of effectors such as GDNF, KIT ligand, and CYP26B1 [PMID:23487765, PMID:26258622, PMID:28207192]. In cancer, ARID4B binds directly to the promoters of PI3K pathway genes — PIK3CA, PIK3R2, and mTOR — where it competes with histone H1 to modulate chromatin condensation and deposits activating H3K27ac, thereby driving PI3K/AKT/mTOR signaling; this places ARID4B downstream of PTEN as a required factor for prostate tumorigenesis and as a context-dependent regulator of tumor growth and metastasis [PMID:31551414, PMID:34881695, PMID:22693453]. ARID4B expression is post-transcriptionally constrained by multiple microRNAs targeting its 3'UTR [PMID:23447578, PMID:29477868].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0003677 DNA binding, GO:0042393 histone binding
- **localization:** GO:0005634 nucleus, GO:0005694 chromosome
- **pathway (Reactome):** R-HSA-4839726 Chromatin organization, R-HSA-74160 Gene expression (Transcription), R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-1474165 Reproduction
- **partners:** ARID4A, HDAC1, BRMS1, SIN3A, SDS3, AR, RB1, H1
- **complexes:** SIN3A complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | Medium | RBP1L1/ARID4B encodes a 1226-amino acid protein sharing 37% amino acid identity with retinoblastoma-binding protein 1 (RBP1/ARID4A); the protein localizes to the cytoplasm of MCF-7 breast cancer cells, as determined by immunoperoxidase staining with purified RBP1L1-specific IgG. | PMID:11481388 | Journal of the National Cancer Institute |
| 2004 | Medium | BRCAA1/ARID4B protein contains a novel antigen epitope (SSKKQKRSHK) at residues 610–619 and localizes to the cytoplasm of MCF-7 cells; the protein shares 37% identity with RBP1 and 74% with a partial RBP1 sequence, and its expression is associated with ER/PR status in breast cancer. | PMID:15247124 | Cancer epidemiology, biomarkers & prevention |
| 2006 | High | ARID4B (Rbbp1l1/Arid4b) physically interacts with ARID4A (Rbbp1/Arid4a) and with the Snrpn promoter, forming part of an epigenetic complex. Combined homozygous deficiency of Arid4a and heterozygous deficiency of Arid4b in mice reduced trimethylation of histone H4K20 and H3K9 and reduced DNA methylation at the PWS-IC, shifting the maternal allele toward a paternal epigenotype. Mutations of Arid4b (or Arid4a, or Rb) suppressed an Angelman syndrome imprinting defect caused by a mutation at the AS-IC. | PMID:17043311 | Genes & development |
| 2008 | High | Arid4b haploinsufficiency combined with Arid4a deficiency in mice accelerates progression to acute myeloid leukemia (AML); Arid4a/Arid4b deficiency decreases expression of Hox genes (Hoxb3, Hoxb5, Hoxb6, Hoxb8) and FoxP3 in bone marrow, and increases histone trimethylation of H3K4, H3K9, and H4K20, identifying Arid4a and Arid4b as leukemia suppressor genes that regulate hematopoietic gene expression through histone modification. | PMID:18728284 | Journal of the National Cancer Institute |
| 2012 | High | ARID4B physically interacts with the breast cancer metastasis suppressor BRMS1, and also differentially binds to histone deacetylase complex members mSIN3A and mSDS3 depending on allelic variant. Ectopic expression of Arid4b promotes primary tumor growth and increases migration and invasion in vitro; shRNA knockdown reduces pulmonary metastases. Downregulation of the Tpx2 gene network (cell cycle and mitotic spindle regulators) accompanies loss of metastatic efficiency in Arid4b knockdown cells. | PMID:22693453 | PLoS genetics |
| 2013 | High | ARID4A and ARID4B physically interact with each other; ARID4A is an RB-binding protein. In Arid4a−/−Arid4b+/− mice, combined deficiency causes progressive loss of male fertility with hypogonadism, spermatogenic arrest, and impaired blood-testis barrier integrity — phenotypes that recapitulate Sertoli cell-specific AR knockout and RB knockout mice. ARID4A and ARID4B were identified as transcriptional coactivators for androgen receptor (AR) and RB, with several AR- and RB-responsive genes identified as downstream targets. | PMID:23487765 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | Medium | miR-290-3p directly targets the 3' UTR of Arid4b mRNA, as confirmed by luciferase reporter assay; miR-290 upregulation suppresses both primary breast tumor growth and metastasis, and this effect is mediated through repression of Arid4b. Pathway analysis identified estrogen receptor (ER) signaling as a top canonical pathway affected by miR-290 upregulation. | PMID:23447578 | Cancer research |
| 2015 | High | ARID4B is required in Sertoli cells for spermatogenesis; Sertoli cell-specific Arid4b knockout (Arid4bSCKO) mice are completely infertile, showing impaired testis development, loss of germ cells, Sertoli cell-only phenotype, and delayed Sertoli cell maturation with spermatogenic arrest at the round spermatid stage. ARID4B functions as a coactivator of the androgen receptor (AR) and is required for optimal transcriptional activation of reproductive homeobox 5 (Rhox5), an AR target gene in Sertoli cells. | PMID:26258622 | Molecular endocrinology |
| 2017 | High | In Sertoli cell-specific Arid4b knockout mice, ARID4B ablation causes abnormal detachment of Sertoli cells from the basement membrane during the gonocyte-to-SSC transition, preventing niche establishment for spermatogonial stem cell (SSC) formation. Gene expression profiling identified downstream effectors of ARID4B including gap junction protein alpha-1, KIT ligand, anti-Müllerian hormone, GDNF, inhibin alpha/beta, and CYP26B1 as genes governing SSC niche function. | PMID:28207192 | Stem cells |
| 2018 | Medium | miR-519b-3p directly binds the 3' UTR of ARID4B mRNA (validated by luciferase assay), and miR-519b-3p overexpression enhances responsiveness to chemoradiation in rectal cancer cells in an ARID4B-dependent manner. | PMID:29477868 | Gene |
| 2019 | High | PTEN suppresses ARID4B expression, while ARID4B acts as a transcriptional activator of PI3K subunit genes PIK3CA and PIK3R2, which are crucial for PI3K/AKT pathway activation. Reciprocal binding of ARID4B and histone H1 to the PIK3CA and PIK3R2 promoters modulates chromatin condensation. ARID4B is required for prostate tumorigenesis when PTEN is deficient, establishing a PTEN-ARID4B-PI3K axis. | PMID:31551414 | Nature communications |
| 2020 | High | ARID4B is critical for mouse embryonic stem cell (mESC) differentiation toward mesodermal and endodermal lineages; Arid4b-deficient mESCs have normal pluripotency but fail to upregulate meso/endodermal gene expression programs. ARID4B physically and functionally interacts with HDAC1 (but not HDAC2) within the SIN3A complex, suggesting functionally distinct SIN3A subcomplexes. ARID4B deficiency leads to increased H3K27me3 and reduced H3K27Ac at key developmental gene loci. | PMID:33454011 | The Journal of biological chemistry |
| 2020 | Low | Circ-SMARCA5 sponges miR-93-3p (also described as miR-39-3p in the abstract), and ARID4B is a direct target of this miRNA; circ-SMARCA5 upregulates ARID4B expression by sponging the miRNA, thereby inhibiting colorectal cancer cell proliferation, migration, and invasion. The miRNA–ARID4B interaction was validated by luciferase reporter assay. | PMID:32807692 | Digestive and liver disease |
| 2021 | Medium | ARID4B knockdown in human glioma cells suppresses PI3K/AKT signaling (decreased p-mTOR, p-PI3K, p-AKT), induces G1 phase arrest via downregulation of Cyclin D1, increases HDAC1 expression leading to elevated acetyl-p53 and acetyl-H3, and reduces cell migration and invasion. | PMID:33732001 | OncoTargets and therapy |
| 2021 | High | Taurine promotes ARID4B expression in a PI3K-dependent manner in C2C12 myoblasts. ARID4B directly binds the mTOR gene promoter (at the −4368 to −4591 bp site), and this binding is associated with H3K27ac (but not H3K27me3) at that site. ARID4B knockdown abolishes taurine-stimulated mTOR expression and phosphorylation, cell proliferation, and protein synthesis, whereas ARID4B gene activation (CRISPR/dCas9) has stimulatory effects, establishing a PI3K–ARID4B–mTOR pathway in muscle cells. | PMID:34881695 | The British journal of nutrition |
| 2018 | Low | ARID4B expression correlates with WHO grade in gliomas and meningiomas; in vitro ARID4B protein is elevated in some glioma cell lines relative to normal brain tissue (Western blot), establishing overexpression as a feature of malignant primary brain tumors. | PMID:27451434 | Journal of clinical pathology |

## Citations

- PMID:11481388
- PMID:15247124
- PMID:17043311
- PMID:18728284
- PMID:22693453
- PMID:23447578
- PMID:23487765
- PMID:26258622
- PMID:27451434
- PMID:28207192
- PMID:29477868
- PMID:31551414
- PMID:32807692
- PMID:33454011
- PMID:33732001
- PMID:34881695
