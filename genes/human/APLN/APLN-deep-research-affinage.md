---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APLN
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9ULZ1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 31
citation_count: 31
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for APLN (human)

## Current model (mechanistic narrative)

Apelin (APLN) is a secreted peptide hormone, processed from a precursor into multiple bioactive forms (apelin-13, apelin-17, apelin-36), that acts as an endogenous agonist of the G-protein-coupled apelin receptor APJ/APLNR to coordinate cardiovascular, angiogenic, metabolic, and tissue-protective programs [PMID:15907343]. Engagement of APJ activates Gαi2/Gαi3 by molecular rearrangement and Gαo/Gαq by classical dissociation [PMID:25193074], driving PI3K/Akt and MAPK/ERK signaling that underlies its cellular effects, including cardioprotection against ischemia-reperfusion injury via the RISK pathway and delay of mitochondrial permeability transition pore opening [PMID:17694254]. Receptor activation is followed by GRK2-mediated, β-arrestin1-independent, clathrin/dynamin-dependent internalization, and downstream signaling bias is encoded structurally: the I109^3.32 residue of TM3 controls the balance between G protein and β-arrestin/GRK recruitment [PMID:30409826, PMID:27492965], and structure-guided design of G-protein-biased agonists yields improved efficacy against cardiac hypertrophy [PMID:38428423]. Crystal and cryo-EM structures defined a curved two-site peptide binding mode and stoichiometry-dependent G protein coupling, and showed that the second endogenous ligand Elabela/Toddler engages APJ through a distinct binding mode from apelin [PMID:28528775, PMID:35817871, PMID:32301550]. APLN is transcriptionally induced by hypoxia through HIF-1α binding to an intronic hypoxia-responsive element [PMID:18617693], by β-catenin in hepatocellular carcinoma [PMID:31410213], and by muscle contraction as an exerkine [PMID:30061698]. Functionally, apelin marks and drives sprouting (tip) endothelial cells in angiogenesis [PMID:25597280], promotes lymphangiogenesis [PMID:24962866], directs cardiac precursor migration during gastrulation [PMID:17336905], enhances muscle mitochondriogenesis and autophagy [PMID:30061698], and protects vasculature against aneurysm and oxidative injury [PMID:31189595, PMID:32879139]; its peptides are inactivated by ACE2 and by neutral endopeptidase [PMID:15907343, PMID:31189595]. The APLN/APJ axis also regulates Sertoli-cell carnitine production and blood-testis barrier integrity [PMID:36443325] and cholangiocyte proliferation through Nox4/ROS/ERK signaling [PMID:32964473], and apelin inhibition reduces tumor angiogenesis and glioblastoma stem-like cell expansion [PMID:31267692, PMID:29053791].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0048018 receptor ligand activity, GO:0060089 molecular transducer activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-8953897 Cellular responses to stimuli, R-HSA-1643685 Disease
- **partners:** APLNR, ACE2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | High | Apelin peptides are derived from a single gene and activate the 7-transmembrane G-protein-coupled receptor APJ; apelin peptides also represent substrates for ACE2 carboxypeptidase, which cleaves and inactivates them. | PMID:15907343 | Pharmacology & therapeutics |
| 2008 | High | Hypoxia induces apelin expression in endothelial and vascular smooth muscle cells via HIF-1α binding to a hypoxia-responsive element (HRE) located within the first intron (+813/+826) of the human apelin gene; siRNA knockdown of HIF-1α abolished hypoxia-induced apelin expression; apelin or APJ receptor knockdown inhibited hypoxia-induced endothelial cell proliferation in vitro and vessel regeneration in zebrafish. | PMID:18617693 | Circulation research |
| 2007 | High | Apelin-13 and apelin-36 produce cardioprotection against ischemia-reperfusion injury by activating the PI3K-Akt and p44/42 MAPK (RISK pathway) and delaying mitochondrial permeability transition pore (MPTP) opening; pharmacological inhibition of PI3K (LY294002) or MEK (UO126/MEK inhibitor 1) abolished the protective effects. | PMID:17694254 | Basic research in cardiology |
| 2007 | High | Zebrafish apelin (ligand) and its receptor Agtrl1b (APJ homolog) control heart field formation during gastrulation by directing convergence of cardiac precursors from lateral plate mesoderm toward the midline; reduced or excess Apelin/Agtrl1b function caused deficiency of cardiac precursors and heart defects. | PMID:17336905 | Developmental cell |
| 2015 | Medium | Apelin-APJ signaling promotes brown adipocyte differentiation and browning of white adipocytes by increasing expression of brown adipogenic and thermogenic transcription factors via PI3K/Akt and AMPK signaling pathways; apelin also increases mitochondrial biogenesis, PGC1α and UCP1 expression, and oxygen consumption. | PMID:25931124 | The Journal of biological chemistry |
| 2015 | High | APLN is robustly expressed in sprouting (tip) endothelial cells during angiogenesis and is re-activated in adult endothelial cells after ischemia; genetic ablation using Apln-CreER specifically labels sprouting but not quiescent vasculature, and abolishment of VEGF-VEGFR2 signaling reduced APLN expression in sprouting endothelium. | PMID:25597280 | Nature communications |
| 2015 | High | Elabela (ELA)/Toddler activates the apelin receptor (APJ) in mammalian cells, causing receptor internalization, suppression of cAMP production (EC50 ~11 nM), ERK1/2 phosphorylation (EC50 ~14 nM), and weak intracellular calcium mobilization; ELA also induces angiogenesis in endothelial cells and relaxes mouse aortic blood vessels. | PMID:25639753 | Scientific reports |
| 2017 | High | Crystal structure of human apelin receptor (APJR) at 2.6 Å resolution in complex with a 17-amino acid apelin mimetic peptide revealed a lactam-constrained, curved two-site ligand binding mode; mutation analysis and molecular dynamics simulations with apelin-13 identified key binding residues for apelin recognition and specificity. | PMID:28528775 | Structure |
| 2016 | High | Apelin-induced internalization of APJ occurs via clathrin-coated vesicles (CCVs) in a GRK2-mediated phosphorylation-dependent, β-arrestin1-independent, EPS15- and dynamin-dependent manner; [Pyr1]apelin-13 stimulation also causes rapid desensitization of APJ-mediated ERK1/2 (ppERK1/2) signaling through upstream APJ-specific adaptive changes rather than internalization. | PMID:27492965 | Molecular and cellular endocrinology |
| 2014 | Medium | Apelin-13 stimulation of APJ activates Gαi2 and Gαi3 through molecular rearrangement (rather than classical dissociation), while Gαo and Gαq are activated through classical dissociation; Gαi1 showed little change after apelin-13 stimulation. | PMID:25193074 | Experimental cell research |
| 2006 | Medium | Apelin and APJ are expressed in human osteoblasts; apelin stimulates osteoblast proliferation via APJ-dependent activation of PI3K/Akt (but not JNK, p38, or ERK1/2); siRNA-mediated APJ knockdown and LY294002 (PI3K inhibitor) abolished apelin-induced proliferation. | PMID:16563531 | Regulatory peptides |
| 2018 | Medium | Apelin inhibition reduces tumor angiogenesis, remodels the tumor microenvironment by reducing polymorphonuclear myeloid-derived suppressor cell infiltration, and prevents resistance to anti-angiogenic RTK inhibitor therapy; apelin loss alone accelerated tumor cell invasion, but combined apelin/VEGFR2 blockade was synergistically effective. | PMID:31267692 | EMBO molecular medicine |
| 2019 | Medium | APLN is transcriptionally upregulated by active β-catenin, which binds to the APLN promoter to induce transcription in hepatocellular carcinoma; APLN activates PI3K/Akt via APLN receptor, leading to increased p-GSK3β and cyclin D1, promoting G1/S cell cycle progression and inhibiting apoptosis. | PMID:31410213 | Theranostics |
| 2019 | High | APLN protects against abdominal aortic aneurysm by preventing smooth muscle cell apoptosis and oxidative stress; APLN induces ACE2 expression in the vasculature; neutral endopeptidase (NEP) is a major enzyme that metabolizes and inactivates APLN-17 in human AAA tissue; a NEP-resistant APLN-17 analog (APLN-NMeLeu9-A2) ameliorated Ang II-mediated AAA in mice. | PMID:31189595 | Proceedings of the National Academy of Sciences of the United States of America |
| 2022 | High | Cryo-EM structures of fully active human apelin receptor (APJR) complexed with heterotrimeric G protein in both 2:1 (dimer:G protein) and 1:1 (monomer:G protein) stoichiometric ratios were determined; structural differences in G protein engagement between dimeric and monomeric APJR suggest a role for stoichiometry in GPCR-G protein coupling and downstream signaling; a small hydrophobic dimer interface was identified. | PMID:35817871 | Nature structural & molecular biology |
| 2018 | High | A single residue mutation I109A (I109^3.32) in transmembrane domain 3 of APJ converts a balanced receptor into a G protein-biased receptor: it retains full ligand binding and G protein activation but is defective in GRK recruitment, β-arrestin recruitment, and downstream receptor-mediated ERK activation; molecular dynamics simulations indicated that the Phe-13 residue of apelin rotates to form new hydrophobic interactions with TM3 residues (F110, M113), stabilizing the biased conformation. | PMID:30409826 | The Biochemical journal |
| 2024 | High | Cryo-EM structures of APLNR-Gi1 complexes bound to three agonists with divergent signaling profiles identified 'twin hotspots' in APLNR as key determinants for G protein vs. β-arrestin signaling bias; structure-guided design produced G protein-biased agonists WN353 and WN561, which showed superior therapeutic effects against cardiac hypertrophy with reduced adverse effects compared to established APLNR agonists. | PMID:38428423 | Cell |
| 2021 | High | APLN is produced by Sertoli cells in response to high glucose, and hyper-activated APLN/APJ signaling in diabetic testes suppresses carnitine production and represses cell adhesion gene expression in Sertoli cells, causing blood-testis barrier (BTB) structural dysfunction and impaired spermatogenesis; pharmacological blockade of APLN/APJ with ML221 ameliorated BTB damage and improved spermatogenesis in diabetic db/db mice and cultured human testes. | PMID:36443325 | Nature communications |
| 2021 | High | Apelin induces cholangiocyte proliferation through Nox4/ROS/ERK-dependent signaling and activates hepatic stellate cells (HSCs) through intracellular ROS; APLN knockout or APJ antagonism (ML221) reduced bile duct ligation-induced cholangiocyte proliferation, liver inflammation, fibrosis, and angiogenesis in mice. | PMID:32964473 | Hepatology |
| 2020 | High | Elabela/Toddler and apelin bind differently to the apelin receptor: alanine scanning of ELA showed the C-terminus carries the key pharmacophore; Asp282/Asp284 of rat/human apelin receptor are critical for apelin binding and activity but are NOT involved in Elabela/Toddler activity, demonstrating distinct binding modes for the two endogenous ligands. | PMID:32301550 | FASEB journal |
| 2021 | Medium | Apelin-13, pGlu1-apelin-13, apelin-17, apelin-36, Elabela-21, and Elabela-32 exhibit distinct signaling profiles at APJ: all activate both G protein-dependent (cAMP inhibition, Ca2+ mobilization, early-phase ERK activation) and β-arrestin-dependent (GRKs, β-arrestin 1/2, AP2) pathways in a dose-dependent manner, but with different bias ratios; Elabela-32 showed >1000-fold bias to β-arrestin-dependent signaling, and apelin-17 was biased toward β-arrestin-dependent signaling. | PMID:33746758 | Frontiers in pharmacology |
| 2017 | High | Protamine binds the apelin receptor (APJ) with 390 nM affinity and acts as a full antagonist of both G protein and β-arrestin-dependent intracellular signaling; ex vivo and in vivo, protamine abolishes apelin-mediated angiogenesis, glucose tolerance improvement, and vasodilatation; protamine's APJ antagonist activity is fully reversed by heparin both in vitro and in vivo. | PMID:28242772 | FASEB journal |
| 2016 | Medium | Apelin (APLN-13 and APLN-17) increases steroidogenesis (basal and IGF1-induced progesterone and estradiol) in human luteinized granulosa cells through activation of AKT and MAPK3/1 (ERK1/2) pathways and increased HSD3B protein expression; these effects are reversed by the APLNR antagonist ML221. | PMID:27683264 | Biology of reproduction |
| 2017 | Medium | In bovine granulosa cells, APLN-13 and APLN-17 increase progesterone production via MAPK ERK1/2 and increase cell proliferation via AKT signaling (blocked by ML221); conversely, APLN-13 and APLN-17 arrest bovine oocytes at germinal vesicle stage during in vitro maturation, associated with decreased progesterone, inhibited ERK1/2 phosphorylation, and increased PRKA phosphorylation. | PMID:28250234 | Reproduction |
| 2018 | Medium | Apelin promotes lymphangiogenesis: APJ is expressed in lymphatic endothelial cells (LECs) and activates apelinergic signaling; apelin treatment enhances LEC migration, protects against UV-induced apoptosis, increases spheroid formation, stimulates in vitro tube formation, and promotes in vivo lymphatic microvessel invasion; apelin overexpression in tumor cells increases intratumoral lymphangiogenesis and lymph node metastasis. | PMID:24962866 | Oncotarget |
| 2018 | High | Apelin deficiency in mice increases NADPH-stimulated superoxide levels in atria and slows atrial conduction velocities; apelin administration in mice with increased AF vulnerability reduced AF incidence/duration, prolonged atrial refractory periods, accelerated conduction velocity, and increased action potential duration; these electrophysiological effects were associated with increased atrial cardiomyocyte sodium currents. | PMID:32879139 | JCI insight |
| 2018 | High | The exerkine apelin is induced by muscle contraction; apelin or APLNR deficiency in mice causes age-dependent muscle dysfunction; restoration of apelin signaling enhances muscle function by triggering mitochondriogenesis, autophagy, and anti-inflammatory pathways in myofibers, and enhances regenerative capacity by targeting muscle stem cells. | PMID:30061698 | Nature medicine |
| 2015 | Medium | Apelin controls fetal glucose homeostasis: intravenous apelin injection in pregnant rats increases transplacental glucose transport; intraperitoneal apelin in neonates increases glucose uptake in lung and muscle; the apelinergic system is expressed at the fetoplacental interface and in multiple fetal tissues; placenta releases high amounts of apelin in late gestation ex vivo. | PMID:26631739 | Diabetes |
| 2017 | Medium | APJ is expressed at cellular junctions in human umbilical vein endothelial cells (HUVECs) and may associate with PECAM-1; siRNA-mediated silencing of APJ influences shear-induced cytoskeletal remodeling, cellular elasticity, motility, attachment, and distribution of adhesion complexes in endothelial cells. | PMID:29369349 | Journal of cellular physiology |
| 2021 | Medium | Apelin improves endothelial cell dysfunction in diabetes by decreasing apoptosis, reducing adhesion molecule expression, and increasing proliferation, angiogenesis, and expression of E-cadherin, VEGFR2, and Tie-2; these effects were dependent on APJ and downstream NF-κB pathways, as confirmed by endothelial cell-specific APJ knockout mice. | PMID:33504680 | The Journal of endocrinology |
| 2017 | Medium | Apelin is identified as a factor secreted by brain endothelial cells (by mass spectrometry proteomics) that maintains glioblastoma stem-like cell expansion; genetic and pharmacological targeting of the apelin receptor abrogates apelin- and endothelial-mediated expansion of glioblastoma stem-like cells in vitro and suppresses tumor growth in vivo. | PMID:29053791 | Brain |

## Citations

- PMID:15907343
- PMID:16563531
- PMID:17336905
- PMID:17694254
- PMID:18617693
- PMID:24962866
- PMID:25193074
- PMID:25597280
- PMID:25639753
- PMID:25931124
- PMID:26631739
- PMID:27492965
- PMID:27683264
- PMID:28242772
- PMID:28250234
- PMID:28528775
- PMID:29053791
- PMID:29369349
- PMID:30061698
- PMID:30409826
- PMID:31189595
- PMID:31267692
- PMID:31410213
- PMID:32301550
- PMID:32879139
- PMID:32964473
- PMID:33504680
- PMID:33746758
- PMID:35817871
- PMID:36443325
- PMID:38428423
