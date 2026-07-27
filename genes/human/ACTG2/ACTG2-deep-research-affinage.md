---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTG2
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: P63267
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 13
citation_count: 13
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACTG2 (human)

## Current model (mechanistic narrative)

ACTG2 encodes γ2 enteric smooth muscle actin, a structural protein whose polymerization into thin filaments is required for contractility of visceral smooth muscle [PMID:24337657, PMID:26647307]. Heterozygous missense variants—clustered at conserved arginine residues (R178, R257, R40, R63, R211) located in CpG dinucleotide hotspots—impair actin polymerization, shifting the equilibrium toward monomeric G-actin and reducing smooth muscle cell contractility [PMID:24337657, PMID:26647307, PMID:31769566]. These variants cause a spectrum of visceral myopathy, with ACTG2 established as the first gene clearly associated with megacystis-microcolon-intestinal hypoperistalsis syndrome (MMIHS), and arginine substitutions stratify disease severity (R178 > R257 > R40) [PMID:24676022, PMID:31769566]. CRISPR/Cas9 knock-in mouse models carrying the R257C or D245G variants reproduce the molecular defect (elevated G-actin/F-actin ratio), reduced collagen gel contraction, prolonged gastrointestinal transit, and impaired voluntary urination, directly linking the polymerization defect to the gastrointestinal and bladder dysfunction of human disease [PMID:36264152, PMID:40617346]. Beyond visceral muscle, ACTG2 expression is post-transcriptionally controlled by microRNAs and long noncoding RNA sponges across vascular and cancer contexts, where it modulates vascular smooth muscle phenotypic switching and tumor cell proliferation, migration, and invasion [PMID:33910387, PMID:35652208, PMID:28385530].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-397014 Muscle contraction, R-HSA-1643685 Disease
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | Medium | ACTG2 missense mutations p.R178L and p.R178C interfere with proper polymerization of ACTG2 into thin filaments, leading to impaired contractility of smooth muscle. Structural analysis and functional experiments confirmed this polymerization defect. | PMID:24337657 | Human genetics |
| 2014 | High | Heterozygous missense variants in ACTG2 (encoding γ2 enteric actin) cause megacystis-microcolon-intestinal hypoperistalsis syndrome (MMIHS) and a spectrum of smooth muscle disease, with a mutational hotspot at arginine residues in CpG dinucleotides. ACTG2 is established as the first gene clearly associated with MMIHS. | PMID:24676022 | PLoS genetics |
| 2015 | High | ACTG2 missense variants impair actin polymerization and reduce cell contractility in vitro, as demonstrated by molecular dynamics simulations and in vitro contractility assays in MMIHS patients. ACTG2 is expressed in smooth muscle cells across intestinal layers during human development. | PMID:26647307 | Human molecular genetics |
| 2015 | Medium | ACTG2 mutations (p.Arg257His, p.Arg257Cys, p.Arg178His) cause altered muscularis propria with markedly thinned longitudinal muscle layer and reduced/abnormal distribution of ACTG2 protein in intestinal tissue, as shown by immunostaining. | PMID:25998219 | Fetal diagnosis and therapy |
| 1995 | Medium | The human smooth muscle actin gene (enteric type, ACTG2/ACTA3/ACTSG) was chromosomally mapped to chromosome 2p13.1 by fluorescence in situ hybridization, and a HindIII RFLP in the first intron was characterized at the molecular level. | PMID:7759108 | Genomics |
| 2017 | Medium | ACTG2 overexpression promotes hepatocellular carcinoma (HCC) cell migration and metastasis, while ACTG2 knockdown (shRNA) impairs migration and invasion in vitro and inhibits metastasis in vivo. The metastasis-promoting effect operates in a Notch1-dependent manner. | PMID:28385530 | Biochemical and biophysical research communications |
| 2016 | Medium | ACTG2 overexpression inhibits neuroendocrine tumor cell (CNDT2.5) growth in vitro, and ACTG2 expression can be induced more than 10-fold by miR-145 transfection or by the histone methyltransferase inhibitor DZNep (but not by the selective EZH2 inhibitor EPZ-6438 or DNA hypomethylating agent 5-aza-2'-deoxycytidine). | PMID:27107594 | BMC endocrine disorders |
| 2019 | Medium | Recurrent arginine missense mutations (at residues R178, R257, R40, R63, R211) in ACTG2 are the primary drivers of visceral myopathy severity, with a severity spectrum of p.Arg178 > p.Arg257 > p.Arg40. Poor outcomes (TPN dependence, death, transplantation) were invariably caused by one of these arginine alleles. | PMID:31769566 | Human mutation |
| 2022 | High | The Actg2R257C heterozygous variant in mice impairs smooth muscle cell contraction by interfering with actin polymerization (increased G-actin/F-actin ratio), resulting in prolonged gastrointestinal transit time and decreased voluntary urination, thus mimicking the MMIHS phenotype. | PMID:36264152 | Neurogastroenterology and motility |
| 2025 | High | The Actg2D245G mutation impairs actin polymerization (increased G-actin/F-actin ratio), reduces smooth muscle cell contractility in collagen gel contraction assays, and disrupts hydrogen bonds within the mutant protein (by 3D structural simulation), causing intestinal and bladder dysfunction that is milder than that caused by the Actg2R257C mutation. | PMID:40617346 | Journal of pediatric surgery |
| 2021 | Medium | miR-500b-5p directly targets ACTG2 in vascular smooth muscle cells (VSMCs), and linc01278 sponges miR-500b-5p to regulate ACTG2 expression, thereby controlling VSMC phenotypic switching. Dual-luciferase reporter assays confirmed the miR-500b-5p/ACTG2 interaction. | PMID:33910387 | Journal of the American Heart Association |
| 2022 | Medium | ACTG2 overexpression suppresses colorectal cancer (CRC) cell proliferation, migration, and invasion. miR-3918 directly targets ACTG2, and MIR497HG acts as a competing endogenous RNA (ceRNA) to sponge miR-3918 and upregulate ACTG2. RNA pulldown, luciferase reporter, and RIP assays confirmed these interactions. | PMID:35652208 | Journal of genetics |
| 2023 | Medium | ACTG2 knockdown in bladder cancer cells (T24 and J82) enhances proliferation and invasion and reduces apoptosis, shortening G0-G1 phase and prolonging S phase. Conversely, ACTG2 overexpression decreases cell activity, enhances apoptosis, and prolongs G0-G1 phase. | PMID:37213144 | Cellular and molecular biology |

## Citations

- PMID:24337657
- PMID:24676022
- PMID:25998219
- PMID:26647307
- PMID:27107594
- PMID:28385530
- PMID:31769566
- PMID:33910387
- PMID:35652208
- PMID:36264152
- PMID:37213144
- PMID:40617346
- PMID:7759108
