---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APELA
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: P0DMC3
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

# Affinage mechanistic annotation for APELA (human)

## Current model (mechanistic narrative)

APELA (Elabela/Toddler/ELA) is a secreted peptide hormone that serves as a high-affinity endogenous ligand for the APJ (APLNR) receptor, where it competes with apelin for the same site, activates inhibitory Gi signaling to suppress forskolin-stimulated cAMP, and drives ERK1/2 phosphorylation [PMID:25995451]. Through this APJ axis it regulates cardiovascular physiology — increasing cardiac contractility and inducing coronary vasodilation in an ERK1/2-dependent manner [PMID:26611206] — and genetic ablation in mice produces cardiovascular and vascular remodeling defects together with aberrant erythroid/myeloid marker expression, with epistasis showing APELA acts on early Aplnr-expressing mesoderm independently of apelin [PMID:28854362]. The APELA precursor (proELA) is processed by furin into mature isoforms, and disrupting the furin cleavage site alters its biological activity [PMID:32516140, PMID:34455010], with distinct fragments such as ELA-11 signaling through APJ to activate PI3K/AKT and ERK/MAPK and to protect against oxidative and inflammatory stress [PMID:36160397, PMID:32687618]. Beyond its receptor-mediated peptide role, the APELA RNA acts independently as a non-coding regulatory transcript in embryonic stem cells, binding hnRNPL to block mitochondrial p53 localization and thereby restrain DNA-damage-induced apoptosis in a manner that does not require its coding capacity [PMID:25936916]. APELA also exerts APLNR-independent, p53-linked effects on tumor cell proliferation [PMID:29079036].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0048018 receptor ligand activity, GO:0060089 molecular transducer activity, GO:0003723 RNA binding
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-5357801 Programmed Cell Death
- **partners:** APLNR, HNRNPL, FURIN, GPR25
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2015 | High | APELA (Elabela/Toddler) binds directly to the APJ receptor with high affinity (Kd = 0.51 nM), competes with apelin for the same binding site, and activates the inhibitory G protein (Gi) pathway by inhibiting forskolin-stimulated cAMP production and inducing ERK1/2 phosphorylation. | PMID:25995451 | The Journal of biological chemistry |
| 2015 | High | APELA binds to apelin receptors in the adult rodent heart (non-cardiomyocyte fraction), increases cardiac contractility and induces coronary vasodilation, and this inotropic effect is accompanied by ERK1/2 phosphorylation; pharmacological inhibition of ERK1/2 markedly attenuates apela-induced inotropy. | PMID:26611206 | Basic research in cardiology |
| 2017 | High | Loss of Apela in mice (CRISPR/Cas9 null allele) causes low-penetrance cardiovascular defects, vascular remodeling defects, and aberrant upregulation of erythroid and myeloid markers. Double-mutant analysis showed that Apela signaling impacts early Aplnr-expressing mesodermal populations independently of the alternative ligand Apelin, and combined loss causes lethal cardiac defects. | PMID:28854362 | Cell reports |
| 2015 | High | The Apela RNA functions as a regulatory (non-coding) RNA in mouse embryonic stem cells that interacts with hnRNPL protein, thereby preventing mitochondrial localization and activation of p53. This forms a tri-element negative feedback loop (p53 → represses Apela → Apela/hnRNPL suppresses p53 mitochondrial activation) regulating p53-mediated DNA damage-induced apoptosis. The coding ability of Apela is dispensable for this function. | PMID:25936916 | Cell stem cell |
| 2017 | Medium | APELA promotes tumor cell growth and migration in ovarian clear cell carcinoma (OCCC) through an APLNR-independent pathway in cells lacking APLNR expression, and affects cell-cycle progression in a p53-dependent manner; APELA knockdown induced p53 expression. | PMID:29079036 | Gynecologic oncology |
| 2020 | High | The APELA precursor (proELA) is cleaved by furin to generate mature ELA; site-directed mutagenesis of the furin cleavage site improves ELA antitumorigenic activity. Mature ELA suppresses kidney tumor cell growth, migration, and survival through mTORC1 signaling activation. | PMID:32516140 | JCI insight |
| 2017 | Medium | Apela isoforms (apela-54, -32, and -11) exhibit distinct membrane-binding behaviors: apela-32 interacts with DPC, SDS, and LPPG micelles (inducing α-helical character), while apela-11 interacts preferentially with SDS and LPPG micelles (inducing β-turn character), indicating isoform- and headgroup-dependent membrane interactions that may influence apelin receptor recognition. | PMID:28132903 | Biochimica et biophysica acta. Biomembranes |
| 2021 | Medium | Apela inhibits angiotensin II-induced inflammatory responses in renal glomerular endothelial cells (including MCP-1, TNF-α, ICAM-1, VCAM-1 expression and THP-1 cell adhesion) by inhibiting the NFκB signaling pathway; blockade of the APJ receptor abolishes these inhibitory effects, confirming APJ-dependence. | PMID:34516679 | FASEB journal |
| 2022 | Medium | ELA-11 (the furin-cleaved 11-residue fragment of APELA) protects cardiomyocytes against oxidative stress-induced apoptosis through PI3K/AKT and ERK/MAPK signaling pathways, and its protective effect is mediated through the APJ receptor (blocked by ML221, an APJ antagonist). | PMID:36160397 | Frontiers in pharmacology |
| 2020 | Medium | ELABELA improves endothelial cell function (viability, migration, tube formation) via the ELA–APJ axis by activating PI3K/Akt signaling; the PI3K inhibitor wortmannin blocks ELA-induced effects and also blocks ELA-induced APJ receptor upregulation. | PMID:32687618 | Clinical and experimental pharmacology & physiology |
| 2018 | Medium | In non-mammalian vertebrates (zebrafish, spotted gar, pigeon), APELA peptides activate GPR25 (an orphan GPCR) to inhibit cAMP production and induce receptor internalization; human GPR25 was NOT activated by Apela under the same conditions. | PMID:29727602 | Biochemical and biophysical research communications |
| 2021 | Medium | ELA-32 (Apela) in human plasma has a half-life of ~47 min and in kidney homogenates ~44 s. The primary metabolic fragments generated include ELA-11, ELA-16, ELA-19, and ELA-20; ELA-16 was identified as a potentially more stable fragment. | PMID:34455010 | Peptides |
| 2022 | Medium | Apela gene therapy (AAV-ELA32) in monocrotaline-induced pulmonary arterial hypertension rats upregulates KLF2/eNOS and BMPRII/SMAD4 signaling in pulmonary arterioles, inhibits endothelial-to-mesenchymal transition, and reduces pulmonary arteriolar muscularization. | PMID:35747913 | FASEB journal |
| 2019 | Low | Two rare variants in the 5'-UTR of the APELA gene (c.-306A>G and c.-145A>G) impair transcriptional activity of APELA by altering promoter function, as demonstrated by luciferase reporter assays in HEK293 and HTR-8/SVneo cells. | PMID:30719741 | Prenatal diagnosis |
| 2024 | Medium | In zebrafish fin regeneration, Apela selectively accumulates in newly formed fin tissue and vessels; morpholino-mediated knockdown of Apela prevents vessel remodeling, while exogenous Apela peptide mediates plexus repression and promotes arterial development in regenerated fins. Apela also regulates expression of vascular remodeling genes including VWF, IGFBP3, ESM1, VEGFR2, Apln, and Aplnr. | PMID:38355946 | Scientific reports |
| 2025 | Medium | ELA-11 suppresses macrophage foam cell formation, M1 polarization, and apoptosis via inhibition of the AKT–endoplasmic reticulum (ER) stress pathway; mPEG@ELA-11 (a pH-responsive conjugate) reduces atherosclerotic plaque area more effectively than free ELA-11 in ApoE-/- mice. | PMID:41306397 | BME frontiers |

## Citations

- PMID:25936916
- PMID:25995451
- PMID:26611206
- PMID:28132903
- PMID:28854362
- PMID:29079036
- PMID:29727602
- PMID:30719741
- PMID:32516140
- PMID:32687618
- PMID:34455010
- PMID:34516679
- PMID:35747913
- PMID:36160397
- PMID:38355946
- PMID:41306397
