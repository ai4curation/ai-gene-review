---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABCB10
affinage_run_date: 2026-06-09T22:02:36
uniprot_accession: Q9NRK6
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

# Affinage mechanistic annotation for ABCB10 (human)

## Current model (mechanistic narrative)

ABCB10 is a homodimeric ABC transporter of the inner mitochondrial membrane that exports the tetrapyrrole biliverdin from the matrix to the cytosol, coupling mitochondrial redox and iron metabolism to cellular fate decisions in erythroid, hepatic, cardiac, immune, and stem cell lineages [PMID:34011630, PMID:22240895]. Structurally it adopts an exporter fold with matrix-facing nucleotide-binding domains, captured crystallographically in an open-inwards conformation both in the apo and nucleotide-bound states, with a transmembrane portal assisting substrate entry [PMID:23716676]; it is delivered to the inner membrane by an unusually long 105-residue presequence and assembles into homodimers and higher oligomers [PMID:15215243]. Its ATPase cycle is the functional core: catalytic Walker A/B and C-loop residues are required for ATP binding and hydrolysis [PMID:26053025], conserved transmembrane arginines R232/R295 mediate biliverdin-induced ATPase stimulation and conformational switching [PMID:41229075], and activity is tuned by cardiolipin, which binds preferentially and cooperatively [PMID:37807693], and by glutathione redox status acting partly through glutathionylation at Cys547 [PMID:26053025]. Functionally, ABCB10 ATPase activity is essential for hemoglobinization independent of any block at the ferrochelatase or ALA-export steps, and it shapes the heme biosynthetic transcriptional program via Bach1 [PMID:28808058]; biliverdin/bilirubin export rather than direct ALA or dALA transport is the established substrate axis [PMID:34011630, PMID:28808058, PMID:33253225]. ABCB10 physically organizes mitochondrial iron-heme machinery, stabilizing mitoferrin-1 to enhance iron import [PMID:19805291] and forming a complex with ferrochelatase bridged to ABCB7 near the nucleotide-binding domains [PMID:20427704, PMID:30765471]. Loss of ABCB10 causes mitochondrial and lysosomal iron accumulation, elevated ROS, and lethal failure of erythropoiesis [PMID:22240895, PMID:38655715, PMID:38493949], while its bilirubin product acts as the maladaptive effector limiting hepatic glucose handling and beta-cell insulin secretion through PTP1B and H2O2 signaling [PMID:34011630, PMID:34823065]; it additionally supports CD4+ T cell metabolic reprogramming and memory formation [PMID:34893527] and the mitochondrial unfolded protein response [PMID:28315685, PMID:30802639].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140657 ATP-dependent activity, GO:0005215 transporter activity, GO:0008289 lipid binding, GO:0140313 molecular sequestering activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-8953897 Cellular responses to stimuli, R-HSA-1266738 Developmental Biology
- **partners:** SLC25A37, FECH, ABCB7
- **complexes:** ABCB10 homodimer, ABCB10-mitoferrin-1-ferrochelatase complex, ferrochelatase-bridged ABCB7-ABCB10 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | High | Crystal structures of ABCB10 in apo- and nucleotide-bound states reveal a classic exporter-fold ABC transporter adopting an open-inwards conformation both without and with non-hydrolysable ATP analogs, in contrast to other ABC transporters that adopt open-outwards conformations with ATP. A portal between two transmembrane helices assists substrate entry into the binding cavity, and varying degrees of opening in the ATP-bound complexes indicate plasticity between the two halves of the protein. | PMID:23716676 | Proceedings of the National Academy of Sciences of the United States of America |
| 2009 | High | ABCB10 physically interacts with mitoferrin-1 (Mfrn1/Slc25a37) in the mitochondrial inner membrane of erythroid cells, stabilizing Mfrn1 protein and enhancing Mfrn1-dependent mitochondrial iron import. The binding domain maps to the N-terminus of Mfrn1. This interaction was identified by in vivo epitope-tagging affinity purification and mass spectrometry and confirmed in MEL and heterologous COS7 cells. | PMID:19805291 | Proceedings of the National Academy of Sciences of the United States of America |
| 2010 | High | Ferrochelatase (Fech), the terminal heme synthesis enzyme, forms an oligomeric complex with both Mfrn1 and ABCB10. Fech protein levels are induced in parallel with Mfrn1 and ABCB10 during erythroid differentiation, and the interactions were confirmed by affinity purification/MS and immunoprecipitation/Western blot with both endogenous and heterologous proteins. | PMID:20427704 | Blood |
| 2004 | High | ABCB10 contains an unusually long 105-amino acid mitochondrial targeting presequence (mTP). The central subdomain (aa 36–70) is sufficient for mitochondrial import of EGFP. The N-terminal subdomain (aa 1–35) is required for proper inner-membrane insertion. Hydrophobic character of the mTP (disrupted by L46Q/I47Q mutation) is required for efficient targeting; arginine residues and alpha-helical structure are not required. ABCB10 homodimerizes and homo-oligomerizes in the inner mitochondrial membrane, as shown by mass spectrometry of cross-linked immunoprecipitated protein. A mTP-deletion mutant targets to the ER with similar quaternary assembly. | PMID:15215243 | The Journal of biological chemistry |
| 2019 | High | Dimeric ferrochelatase bridges ABCB7 and ABCB10 homodimers in an architecturally defined multiprotein complex. Chemical cross-linking, tandem mass spectrometry, and mutational analyses mapped the interaction interfaces: ferrochelatase binds near the nucleotide-binding domains of each ABC transporter homodimer. | PMID:30765471 | Haematologica |
| 2021 | High | ABCB10 is a mitochondrial biliverdin exporter. Purified ABCB10 reconstituted into liposomes transported biliverdin. ABCB10 deletion caused intramitochondrial biliverdin accumulation. In obesity, hepatic ABCB10 deletion reduced cytosolic bilirubin, protected against steatosis and hyperglycemia, enhanced mitochondrial function, and increased inactivation of PTP1B. Restoration of bilirubin in ABCB10 KO hepatocytes reversed these improvements, demonstrating bilirubin as the maladaptive effector. | PMID:34011630 | Science translational medicine |
| 2012 | High | ABCB10 (ABC-me) is essential for erythropoiesis in vivo. ABC-me−/− mice die at embryonic day 12.5 with near-complete eradication of primitive erythropoiesis. Deletion causes increased mitochondrial superoxide production and protein carbonylation in erythroid precursors. Treatment with the mitochondrial antioxidant MnTBAP (SOD2 mimetic) supports survival, ex vivo differentiation, and hemoglobin production in ABC-me−/− progenitors, placing ABCB10 upstream of mitochondrial ROS control in erythropoiesis. | PMID:22240895 | Cell death and differentiation |
| 2015 | High | Gly497 and Lys498 (Walker A), Glu624 (Walker B), and Gly602 (C-loop) of ABCB10 are required for proper ATP binding and hydrolysis. Oxidized glutathione (GSSG) stimulates ATP hydrolysis without affecting ATP binding; reduced glutathione (GSH) inhibits both ATP binding and hydrolysis. ABCB10 is glutathionylated at Cys547. Delta-aminolevulinic acid (dALA) does not alter ABCB10 ATPase activity, providing evidence against dALA as a direct substrate. | PMID:26053025 | PloS one |
| 2017 | High | Reductions in Abcb10 do not cause protoporphyrin IX accumulation in zebrafish morphants or in differentiated shRNA-silenced MEL cells, ruling out a block at the ferrochelatase step. ATPase activity of Abcb10 is necessary for hemoglobinization in MEL cells. Abcb10 silencing does not affect ALA export from mitochondria (confirmed by succinylacetone treatment), ruling out ALA as a transported substrate. Abcb10 loss alters the heme biosynthesis transcriptional profile via Bach1 repression, which is partially rescued by Alas2 or Gata1 overexpression. | PMID:28808058 | The Journal of biological chemistry |
| 2020 | High | Zinc-mesoporphyrin (ZnMP) specifically activates purified ABCB10 ATPase activity by ~70% when reconstituted in lipid nanodiscs. This activation is present in cysteine-less ABCB10, indicating it does not require heme regulatory motif cysteines. Neither delta-aminolevulinic acid nor glutathione directly activated ABCB10 under these conditions, reducing their candidacy as transported substrates. | PMID:33253225 | PloS one |
| 2023 | High | Cardiolipin binds ABCB10 with higher affinity than other phospholipids, displaying positive cooperativity for the first three binding events (suggestive of specific binding sites). Cardiolipin regulates ABCB10 ATPase activity in a dose-dependent fashion, more strongly than other lipids tested. Phosphatidic acid is the second-best binder; phosphatidylcholine and phosphatidylethanolamine show the weakest affinity. | PMID:37807693 | Biochemistry |
| 2025 | High | Conserved transmembrane arginine residues R232 and R295 are required for biliverdin-induced stimulation of ABCB10 ATPase activity. Mutation of these residues decreases biliverdin stimulation and alters the conformational equilibrium of the transporter (detected by LRET). Biliverdin dimethyl ester does not effectively stimulate ABCB10, while mesobiliverdin inhibits rather than stimulates, indicating specific complementarity between biliverdin functional groups and the binding pocket. The detergent GDN abolishes biliverdin stimulation, suggesting it affects substrate binding in cryo-EM models. | PMID:41229075 | Protein science : a publication of the Protein Society |
| 2014 | Medium | E2F2, E2F3, and E2F4 transcription factors activate transcription from the ABCB10 promoter. E2F4 directly binds ABCB10 promoter sites as shown by EMSA and ChIP. Silencing E2F factors reduces basal ABCB10 expression, demonstrating they are required for ABCB10 transcriptional maintenance. E2F4 acts as a transcriptional activator (rather than its typical repressor role) at the ABCB10 promoter. | PMID:25220178 | Genomics |
| 2017 | Medium | Nrf2 transcriptionally regulates ABCB10 expression in blood-brain barrier endothelial cells: Nrf2 gene silencing markedly suppresses ABCB10 protein, while Nrf2 activation by sulforaphane up-regulates ABCB10. Conversely, ABCB10 knockdown induces Nrf2-driven antioxidant responses (increased Nrf2 and downstream targets) and elevates endothelial-monocyte adhesion, indicating a regulatory feedback relationship. | PMID:28572033 | Neuroscience letters |
| 2017 | Medium | ABCB10 depletion in HepG2 cells reduces expression of mitochondrial unfolded protein response (UPRmt) markers (mitochondrial chaperones HSPD1/HSP60 and DNAJA3, and mitochondrial protease LONP1), upregulates ROS and ROS-detoxifying enzymes (SOD2, GSTA1, GSTA2, SESN3), placing ABCB10 in the UPRmt signaling pathway analogous to C. elegans HAF-1. | PMID:28315685 | Biochemical and biophysical research communications |
| 2019 | Medium | Mutant huntingtin (mtHtt) suppresses the mitochondrial unfolded protein response (UPRmt) by impairing ABCB10 mRNA stability. ABCB10 loss in HD models increases mitochondrial ROS production and cell death; ABCB10 overexpression reduces these effects. ABCB10 regulates CHOP, a transcription factor controlling HSP60 and Clpp (UPRmt markers), in HD mouse striatal cells. | PMID:30802639 | Biochimica et biophysica acta. Molecular basis of disease |
| 2023 | Medium | Loss of Abcb10 in erythroid cell lines (MEL and K562) results in decreased arginine levels, increased transcripts for cationic and neutral amino acid transporters, reduced citrulline-to-arginine converting enzymes (argininosuccinate synthetase and argininosuccinate lyase), increased eIF2α phosphorylation, and upregulation of nutrient-sensing transcription factor ATF4 and downstream targets (CHOP, CHAC1, RARS). Arginine supplementation improved Abcb10-null proliferation and hemoglobinization, linking ABCB10 substrate trapping to nutrient stress signaling. | PMID:37269954 | The Journal of biological chemistry |
| 2024 | Medium | Cardiomyocyte-specific deletion of Abcb10 causes progressive cardiac fibrosis, mitochondrial structural abnormalities, decreased NAD+ levels, lysosomal dysfunction, and ferroptosis. ABCB10 knockdown HeLa cells accumulate Fe2+ and lipid peroxides in lysosomes; iron chelator treatment suppresses lipid peroxidation, implicating lysosomal iron accumulation in ferroptosis downstream of ABCB10 loss. | PMID:38655715 | Bioscience reports |
| 2021 | Medium | In beta-cells, ABCB10 activity limits glucose-stimulated insulin secretion (GSIS) and H2O2-mediated signaling. Beta-cell-specific Abcb10 KO mice are protected from high-fat diet-induced hyperinsulinemia and insulin resistance by limiting HFD-induced beta-cell mass expansion. Increasing ABCB10 expression was sufficient to limit GSIS capacity. Ex vivo deletion in islets increased H2O2 and GSIS, effects reversed by bilirubin treatment, confirming bilirubin as the mechanistic effector. | PMID:34823065 | Molecular metabolism |
| 2021 | Medium | ABCB10 loss selectively impairs CD4+ (but not CD8+) T cell cytokine expression upon activation and disrupts the ability of Jurkat T cells to switch to aerobic glycolysis upon activation. In vivo, CD4+ T cells lacking ABCB10 show reduced number and impaired antigen-specific memory formation and recall responses. CRISPR-mediated ABCB10 disruption in Jurkat cells recapitulates the cytokine expression defect. | PMID:34893527 | Journal of immunology |
| 2024 | Medium | ABCB10 gain-of-function in hepatocytes of alcoholic hepatitis mice decreases MPO gene expression and histone H3 citrullination (NET formation marker), reduces hepatic 4-HNE protein adducts, and increases the mitochondrial GSH/GSSG ratio, demonstrating that ABCB10-mediated ROS reduction in surviving hepatocytes mitigates maladaptive neutrophil activation. | PMID:38290384 | Redox biology |
| 2024 | Medium | Induced deletion of Abcb10 in adult mice causes excess mitochondrial iron accumulation and oxidative stress in hematopoietic stem cells (HSCs), reducing HSC numbers and stem cell potential while skewing differentiation toward the erythroid lineage. These hematopoietic defects could not be rescued by in vivo administration of a mitochondrial iron chelator or antioxidant, suggesting additional mechanisms beyond iron/ROS. | PMID:38493949 | Experimental hematology |

## Citations

- PMID:15215243
- PMID:19805291
- PMID:20427704
- PMID:22240895
- PMID:23716676
- PMID:25220178
- PMID:26053025
- PMID:28315685
- PMID:28572033
- PMID:28808058
- PMID:30765471
- PMID:30802639
- PMID:33253225
- PMID:34011630
- PMID:34823065
- PMID:34893527
- PMID:37269954
- PMID:37807693
- PMID:38290384
- PMID:38493949
- PMID:38655715
- PMID:41229075
