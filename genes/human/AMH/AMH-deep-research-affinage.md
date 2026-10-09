---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AMH
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: P03971
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 22
citation_count: 22
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AMH (human)

## Current model (mechanistic narrative)

AMH is a TGF-β superfamily glycoprotein that governs sexual differentiation and gonadal function by signaling through its dedicated type II receptor AMHR2 together with shared type I receptors [PMID:15878900, PMID:35813657]. It is secreted as a noncovalent complex of an unusually large N-terminal prodomain and a smaller C-terminal mature signaling domain; the mature domain assembles a receptor complex of two type I and two type II receptors to drive intracellular SMAD signaling [PMID:35813657]. In the developing testis, AMH expression is initiated by SOX9 and modulated by SF1, GATA factors, WT1, DAX1, and FSH, then suppressed at puberty by androgens and meiotic germ cells [PMID:14656472]. Loss-of-function mutations in AMH or AMHR2 cause persistent Müllerian duct syndrome, establishing the ligand–receptor axis as the effector of Müllerian duct regression in males [PMID:15878900]. In the ovary, AMH acts as a brake on folliculogenesis: superphysiological AMH arrests follicle development while preserving the primordial reserve and protects against chemotherapy-induced follicle depletion [PMID:28137855], imposing a quiescent, anti-proliferative transcriptional state across granulosa, epithelial, and stromal cells [PMID:33980714]. AMH also restrains steroidogenesis, inhibiting aromatase (CYP19A1) expression in granulosa cells [PMID:27268296, PMID:30403655] and suppressing androgen synthesis via reduced CYP17A1 in theca cells through ALK2/ALK5 acting with AMHR2 [PMID:36856855]. Its own expression is reciprocally controlled by oocyte-derived GDF9+BMP15 acting via SMAD2/3, PI3K/Akt, and p300-mediated H3K27 acetylation, antagonized by FSH through a GIOT1/HDAC2 repressive route [PMID:30060157, PMID:28874516, PMID:29885643], and by estrogen acting through ERα binding to the AMH promoter [PMID:32934281, PMID:33658225]. Beyond the gonad, AMH is expressed in migratory GnRH neurons and acts as a pro-motility factor, with AMHR2 deficiency causing defective GnRH neuron migration and reduced fertility, linking the pathway to central reproductive control [PMID:31291191]; AMHR2 is itself transcriptionally activated by GnRH via Egr1 in pituitary gonadotropes [PMID:30368511]. Comparative genetics in zebrafish and tilapia confirm a conserved role for Amh/Amhr2 in suppressing early germ cell proliferation and enabling follicular transition [PMID:32745576, PMID:31560938].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0048018 receptor ligand activity, GO:0060089 molecular transducer activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-1474165 Reproduction
- **partners:** AMHR2, ALK2, ALK5
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | High | AMH expression in Sertoli cells is triggered by SOX9 at the onset of testicular differentiation, and is regulated by transcription factors SF1, GATA factors, WT1, DAX1, and by FSH. In males, AMH is downregulated at puberty by androgens and meiotic germ cells, and its directional secretion switches from the basal compartment to the seminiferous tubule lumen. | PMID:14656472 | Molecular and cellular endocrinology |
| 2005 | High | AMH signals through two transmembrane receptors: a specific type II receptor (AMHR2) and type I receptors shared with the BMP family. Mutations in AMH or AMHR2 lead to persistent Müllerian duct syndrome (PMDS) in males. Mutations in the extracellular domain of AMHR2 prevent translocation to the surface membrane, explaining receptor inactivity. | PMID:15878900 | Human reproduction update |
| 2003 | Medium | AMH (MIS) acts as a member of the TGF-β superfamily and signals through type II and type I receptors. A candidate AMH-target gene involved in Müllerian duct regression was identified downstream of AMH signaling. | PMID:14656478 | Molecular and cellular endocrinology |
| 2003 | Medium | Recombinant AMH induces mesonephric cell migration into XX gonads in culture, promotes increased vascular development and altered morphology of the coelomic epithelium consistent with testis differentiation, but does not induce markers of Sertoli or Leydig cell differentiation. AMH-deficient mice show no early testis development abnormalities, suggesting functional redundancy in vivo. | PMID:14656469 | Molecular and cellular endocrinology |
| 2017 | High | Long-term administration of superphysiological doses of MIS/AMH (via AAV9 gene therapy or recombinant protein) causes complete arrest of folliculogenesis in mice while retaining the primordial follicle reserve. This effect is reversible upon cessation of treatment or orthotopic transplantation of treated ovaries. MIS co-treatment significantly preserved primordial follicles against chemotherapy-induced depletion (carboplatin, doxorubicin, cyclophosphamide), suggesting AMH acts as a negative regulator of primordial follicle activation. | PMID:28137855 | Proceedings of the National Academy of Sciences of the United States of America |
| 2021 | Medium | Single-cell RNA sequencing of neonatal ovaries treated with MIS/AMH revealed that MIS inhibits follicle development by inhibiting proliferation in granulosa, surface epithelial, and stromal cells, imposing a quiescent transcriptional state in granulosa cells, and uncoupling germ cell and granulosa cell maturation. | PMID:33980714 | Proceedings of the National Academy of Sciences of the United States of America |
| 2018 | High | GDF9 and BMP15 together (but not individually) induce AMH expression in granulosa cells via PI3K/Akt and Smad2/3 pathways, recruiting coactivator p300 to the AMH promoter, resulting in H3K27 acetylation. FSH inhibits this effect through PKA/SF1-mediated expression of GIOT1, a transcriptional repressor that recruits HDAC2 to deacetylate H3K27ac and suppress AMH expression. Fshβ-null mice have elevated ovarian Amh mRNA, restored by hFSHβ transgene. | PMID:30060157 | Endocrinology |
| 2017 | Medium | GDF9 and BMP15 together (but not individually) stimulate AMH expression in primary human cumulus cells in a dose-dependent manner; the effect is inhibited by SMAD2/3 pathway inhibitors and by FSH co-treatment. | PMID:28874516 | Reproduction (Cambridge, England) |
| 2019 | High | AMH is expressed in migratory GnRH neurons during embryonic development in both mouse and human fetuses, and acts as a pro-motility factor for GnRH neurons. Amhr2-deficient mice show abnormal peripheral olfactory system development and defective embryonic GnRH cell migration to the basal forebrain, resulting in reduced adult fertility. | PMID:31291191 | eLife |
| 2022 | Medium | AMH exists as a noncovalent complex of a large N-terminal prodomain and a smaller C-terminal mature signaling domain. The mature domain binds to extracellular domains of two type I and two type II receptors (with AMHR2 as its dedicated type II receptor), resulting in intracellular SMAD signal transduction. The prodomain is the largest within the TGF-β family and remains largely uncharacterized. | PMID:35813657 | Frontiers in endocrinology |
| 2017 | Medium | AMH treatment of primary Sertoli cells promotes proliferation at low concentrations (10 ng/mL) via activation of the non-canonical ERK signaling pathway, while inducing apoptosis at high concentrations (50–800 ng/mL) via increased Caspase-3 and Bax and decreased Bcl-2. Low concentrations of AMH also increase stem cell factor (SCF) expression in Sertoli cells. | PMID:28851672 | The Journal of steroid biochemistry and molecular biology |
| 2019 | High | In zebrafish, Amh deficiency causes severe gonadal dysgenesis with accumulation of early germ cells (spermatogonia in testis, primary growth oocytes in ovary). Amh suppresses proliferation of early germ cells and promotes their progression to advanced stages. Elevated Fshb in juvenile amh mutant males contributes to gonadal hypergrowth; compound fshb and amh mutants confirm FSH involvement in ovarian hypertrophy in females. | PMID:32745576 | Molecular and cellular endocrinology |
| 2019 | High | In Nile tilapia, Amh regulates female folliculogenesis in a dose-dependent manner through Amhr2. Heterozygous and homozygous amh or amhr2 mutations cause increased primary growth follicles, failed follicular transition, decreased gnrh3/fsh/lh expression, reduced serum estradiol, and increased follicle cell apoptosis. Exogenous E2 administration does not rescue folliculogenesis defects in mutants. | PMID:31560938 | Molecular and cellular endocrinology |
| 2020 | High | Estradiol (E2) upregulates AMH expression in prepubertal Sertoli cells by activating estrogen receptor 1 (ERα), which binds to a specific ERE sequence in the hAMH promoter. A modest action is also mediated through the membrane estrogen receptor GPER. ERα expression in Sertoli cells was confirmed by immunohistochemistry in patients with complete androgen insensitivity syndrome (CAIS). | PMID:32934281 | Scientific reports |
| 2018 | High | GnRH transactivates the human AMHR2 promoter in pituitary gonadotrope cells via Egr1 binding to a proximal promoter element (-53/-37 bp). SF1 and β-catenin are required for basal and GnRH-stimulated AMHR2 promoter activity. FOXO1 acts as a negative regulator of basal and GnRH-dependent AMHR2 expression in gonadotrope cells. Amhr2 expression is differentially regulated by GnRH pulse frequency. | PMID:30368511 | Neuroendocrinology |
| 2022 | Medium | AMH suppresses androgen synthesis in human theca cells by reducing CYP17A1 expression and decreasing androstenedione and testosterone production. This effect is mediated through ALK2 and ALK5 (BMP and TGFβ type I receptors), which interact with AMHR2 in the presence of AMH. However, AMH did not activate canonical TGFβR-Smad2/3 or BMPR-Smad1/5/8 signaling in these cells. | PMID:36856855 | The Journal of steroid biochemistry and molecular biology |
| 2018 | Medium | BMP15 upregulates AMH transcription in goat granulosa cells via the p38 MAPK signaling pathway. Inhibition of p38 MAPK decreases BMP15-induced AMH and SOX9 expression, implicating SOX9 as a downstream transcription factor in this regulatory axis. | PMID:29885643 | Theriogenology |
| 2021 | Medium | AMH acts as an autocrine pro-survival and pro-proliferation factor in ovarian cancer cells at physiological concentrations. AMH depletion by siRNA reduces cell viability by 20–50% across four ovarian cancer cell lines. An anti-AMH antibody (B10) at physiological AMH concentrations reduces clonogenic survival, decreases AKT phosphorylation, and increases PARP and caspase 3 cleavage. In vivo, B10 reduces tumor growth and extends median survival. | PMID:33500516 | Scientific reports |
| 2016 | Medium | AMH treatment inhibits CYP19A1 (aromatase) expression in a dose-dependent manner and reduces granulosa cell proliferation in bovine cells from small follicles. AMHR2 expression is greater in smaller (5–8 mm) follicles than in larger follicles. BMP6 and BMP15, but not BMP2, significantly increase AMHR2 mRNA expression in bovine granulosa cells. | PMID:27268296 | Theriogenology |
| 2021 | Medium | Estrogen receptor 1 (ESR1/ERα), activated by estrogen, binds to the 5' region of the Amh gene and upregulates its transcription in pregranulosa cells before follicle formation. Ectopic AMH expression inhibits normal follicle formation. Alpha-fetoprotein (AFP) blocks estrogen action and thereby prevents ectopic AMH induction, enabling successful follicle assembly in vitro. | PMID:33658225 | Development (Cambridge, England) |
| 2019 | High | In infantile mice, high FSH concentrations specifically lower Amh expression in preantral/early antral follicles. AMH in turn decreases FSH-mediated Cyp19a1 (aromatase) expression in organotypic ovarian culture, without altering cyclin D2-mediated granulosa cell proliferation. Fshβ-null mice show elevated ovarian Amh levels, consistent with FSH suppressing AMH expression in vivo. | PMID:30403655 | The Journal of endocrinology |
| 1996 | Medium | In Amh-deficient mice, the timing of Sry downregulation is unaffected, excluding a role for AMH as a negative regulator of Sry expression. Fra1 is not expressed at the critical period of sex determination when Sry transcripts are present, excluding Fra1 from the Sry regulatory pathway. | PMID:9115712 | Molecular reproduction and development |

## Citations

- PMID:14656469
- PMID:14656472
- PMID:14656478
- PMID:15878900
- PMID:27268296
- PMID:28137855
- PMID:28851672
- PMID:28874516
- PMID:29885643
- PMID:30060157
- PMID:30368511
- PMID:30403655
- PMID:31291191
- PMID:31560938
- PMID:32745576
- PMID:32934281
- PMID:33500516
- PMID:33658225
- PMID:33980714
- PMID:35813657
- PMID:36856855
- PMID:9115712
