---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AGT
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: P01019
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 11
citation_count: 11
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AGT (human)

## Current model (mechanistic narrative)

Angiotensinogen (AGT) is a liver-secreted precursor that serves as the obligate source of angiotensin peptides and, in this capacity, is functionally required for maintenance of circulating angiotensin II and systemic blood pressure: hepatic RNAi knockdown reduces circulating AGT and Ang II and lowers systolic blood pressure in vivo [PMID:22977667]. Its expression is tightly controlled at the transcriptional and epigenetic level — IFN-γ drives AGT transcription via STAT1 binding to a defined promoter element distinct from IL-6/STAT3 input [PMID:16949687], DNA methylation at promoter CEBP sites represses AGT with salt- and aldosterone-driven demethylation activating expression in adipose and cardiac tissue [PMID:33925539], and a common M235T coding polymorphism functionally raises AGT secretion levels [PMID:11095476]. In non-vascular and disease contexts, AGT acts upstream of inflammatory and pro-fibrotic signaling cascades, driving JAK2/STAT3 activation in osteoarthritic chondrocytes where it is repressed by miR-149-5p [PMID:32141427] and the TGFβ1/Smad2 axis in diabetic nephropathy [PMID:33571918]. AGT also functions as a driver in cancer, promoting epithelial-mesenchymal transition through PI3K/AKT in gastric cancer [PMID:36986671] and, in colorectal cancer where it is upregulated by KDM4A-mediated H3K9me3 demethylation, disrupting PHB1-mediated mitophagy to activate cGAS-STING1 signaling and the senescence-associated secretory phenotype [PMID:40923240]. Independently of its angiotensin-precursor role, AGT possesses peroxisomal alanine:glyoxylate aminotransferase enzymatic activity required for glyoxylate-to-glycine metabolism, as restoration of this activity normalizes urinary oxalate in a primary hyperoxaluria type 1 model [PMID:40203111].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016740 transferase activity, GO:0048018 receptor ligand activity
- **localization:** GO:0005777 peroxisome, GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1430728 Metabolism, R-HSA-74160 Gene expression (Transcription)
- **partners:** REN, PHB1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | High | IFN-γ upregulates angiotensinogen (AGT) gene transcription in hepatocytes through STAT1 binding to a specific element between -271 and -279 in the AGT promoter, as confirmed by EMSA and chromatin immunoprecipitation (ChIP) assays; mutation of this STAT1 element reduced IFN-γ responsiveness. This pathway is distinct from IL-6/STAT3-mediated AGT upregulation. | PMID:16949687 | Biochimica et biophysica acta |
| 2021 | Medium | AGT knockdown in IL-6-stimulated human chondrocytes inhibited increases in IL-1β, MMP-13, and nitrite, placing AGT upstream of inflammatory mediators via the renin-angiotensin system. miR-149-5p directly binds AGT mRNA (validated by luciferase reporter with mutant 3′UTR), negatively regulating AGT protein levels and downstream JAK2/STAT3 pathway activation in osteoarthritic chondrocytes. | PMID:32141427 | Clinical and experimental rheumatology |
| 2021 | Medium | DNA methylation at CEBP-binding sites in the AGT promoter negatively regulates AGT expression in adipose tissue and heart; high salt intake and excess aldosterone cause DNA demethylation at these CEBP sites, converting AGT expression from an inactive to an active state in visceral adipose tissue. Salt-dependent hypertension is partially mediated by increased cardiac AGT expression associated with CEBP site demethylation. | PMID:33925539 | International journal of molecular sciences |
| 2021 | Medium | AGT knockdown by siRNA in high-glucose-induced glomerular mesangial cells significantly attenuated the beneficial effects of epiberberine (EPI), demonstrating that AGT acts upstream of the TGFβ1/Smad2 signaling pathway in diabetic nephropathy; EPI reduced AGT, TGFβ1, and Smad2 expression both in vitro and in vivo in db/db mice. | PMID:33571918 | Phytomedicine |
| 2017 | Low | AGT overexpression in A549 cells under hyperoxic conditions promoted inflammation and suppressed cell proliferation via activation of the JAK/STAT signaling pathway; the AGT inhibitor Valsartan blocked these effects, placing AGT upstream of JAK/STAT-mediated inflammatory signaling in bronchopulmonary dysplasia. | PMID:29221188 | Oncotarget |
| 2012 | Medium | RNAi-mediated knockdown of AGT in rat liver using nanoparticle-delivered shRNA markedly reduced hepatic AGT mRNA and protein expression, decreased circulating AGT and Ang II levels, and lowered systolic blood pressure by ~27 mmHg within 3 days, demonstrating that hepatic AGT is functionally required for maintenance of blood pressure and angiotensin II production in vivo. | PMID:22977667 | International journal of clinical and experimental pathology |
| 2000 | Medium | In normotensive men, the T235 allele of AGT is associated with greater stimulation of AGT secretion in plasma after ethinylestradiol (EE) administration; in a 7-day study, TT subjects had higher peak plasma AGT concentrations than MM subjects, resulting in compensatory suppression of renin release and readjustment of angiotensin production, establishing that the M235T polymorphism functionally affects AGT secretion levels. | PMID:11095476 | The Journal of clinical endocrinology and metabolism |
| 2025 | Medium | Sequence-optimized human AGT mRNA encapsulated in lipopolyplex (LPP) produced functional AGT enzyme localized to peroxisomes in vitro; in AgxtQ84-/- rats (a primary hyperoxaluria type 1 model), a single 2 mg/kg dose achieved 70% reduction in urinary oxalate, confirming that restored peroxisomal AGT enzymatic activity normalizes glyoxylate-to-glycine metabolism. | PMID:40203111 | Science advances |
| 2025 | Medium | In colorectal cancer, KDM4A upregulates AGT expression through H3K9me3 demethylation at the AGT locus. AGT then disrupts PHB1 (prohibitin 1)-mediated basal mitophagy, leading to cytoplasmic mitochondrial DNA accumulation that activates cGAS-STING1 signaling and enhances senescence-associated secretory phenotype (SASP) secretion, promoting CD8+ T-cell infiltration. | PMID:40923240 | Autophagy |
| 2021 | Low | AGT promotes progression of colorectal carcinoma cells; in vitro knockdown of AGT inhibited proliferation, migration, and invasion of CRC cells and reduced angiogenesis of HUVECs induced by CRC-conditioned medium, placing AGT as a functional driver of CRC progression. | PMID:34655849 | International immunopharmacology |
| 2023 | Medium | AGT knockdown in gastric cancer cells reduced epithelial-mesenchymal transition (EMT) and enhanced chemotherapy (5-fluorouracil) sensitivity both in vitro and in vivo; mechanistically, AGT induced EMT through the PI3K/AKT pathway, as the PI3K/AKT agonist 740Y-P restored EMT impaired by AGT knockdown. | PMID:36986671 | Pharmaceutics |

## Citations

- PMID:11095476
- PMID:16949687
- PMID:22977667
- PMID:29221188
- PMID:32141427
- PMID:33571918
- PMID:33925539
- PMID:34655849
- PMID:36986671
- PMID:40203111
- PMID:40923240
