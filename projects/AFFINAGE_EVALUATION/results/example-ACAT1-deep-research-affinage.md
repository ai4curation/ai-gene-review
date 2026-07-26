---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACAT1
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: P35610
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 37
citation_count: 38
gates_passed: False
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACAT1 (human)

> ⚠️ **CAUTION — trust gate(s) tripped; review before using:**
>
> - Accession mismatch: local review uses `P24752` but the Affinage record's prefetch UniProt accession is `P35610`.

## Current model (mechanistic narrative)

ACAT1 is a cholesterol-esterifying enzyme that maintains intracellular cholesterol homeostasis and, through this lipid-handling role, governs membrane sterol pools in macrophages, neurons, and adipocytes [PMID:32433614, PMID:9857049, PMID:39481851]. In the ER membrane it assembles as a dimer-of-dimers tetramer in which each protomer presents converging cytosolic and transmembrane tunnels that admit acyl-CoA and cholesterol, respectively, to a shared catalytic site; long-chain unsaturated acyl-CoA (preferentially oleoyl-CoA) is conjugated to free cholesterol, and the enzyme behaves allosterically with sigmoidal kinetics toward its cholesterol substrate [PMID:32433614, PMID:32433613, PMID:9857049]. Catalysis depends on a cytosolic-facing active-site serine (Ser269) and on histidines H386 and H460, and substrate recognition is stereospecific for the 3β-hydroxyl steroid configuration [PMID:11071899, PMID:16647063, PMID:20964445]. ACAT1 accounts for the dominant fraction of cholesterol-esterifying activity in human liver, adrenal, macrophage, and kidney tissue, and is enriched at mitochondria-associated ER membranes, where its inhibition raises local cholesterol and strengthens ER–mitochondria contacts [PMID:9717734, PMID:36982602]. In macrophages, ACAT1 controls the balance between cholesterol esterification and efflux and is transcriptionally driven by TNF-α through an NF-κB element in its promoter; myeloid ACAT1 ablation attenuates atherosclerotic lesion formation, adipose inflammation, and TLR4-dependent inflammatory signaling [PMID:15499044, PMID:19189937, PMID:31495784, PMID:36982689]. In neurons, ACAT1 activity controls plasma-membrane and ER free-cholesterol pools and thereby modulates APP processing and amyloid-β generation, placing cholesterol esterification upstream of amyloidogenesis [PMID:20133765, PMID:26474739]. Beyond its esterase function, mitochondrial ACAT1 acts as a protein acetyltransferase that acetylates PDHA1 (K321) and PDP1 (K202) to inhibit the pyruvate dehydrogenase complex and promote the Warburg effect, opposed by the deacetylase SIRT3 [PMID:24486017]. The human enzyme is unusual in arising from a chimeric mRNA assembled by interchromosomal trans-splicing, which additionally yields a 56-kDa ER-localized isoform via IRES-dependent translation from a GGC start codon [PMID:10196189, PMID:15319423].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016740 transferase activity, GO:0140096 catalytic activity, acting on a protein, GO:0008289 lipid binding, GO:0098772 molecular function regulator activity
- **localization:** GO:0005783 endoplasmic reticulum, GO:0005739 mitochondrion, GO:0005764 lysosome, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-168256 Immune System, R-HSA-392499 Metabolism of proteins
- **partners:** PDHA1, PDP1, SIRT3, ME2, METTL3, UBE3A, SIRT5
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2020 | High | Cryo-EM structure of human ACAT1 revealed it forms a dimer-of-dimers tetramer; each protomer has nine transmembrane segments enclosing a cytosolic tunnel and a transmembrane tunnel that converge at the predicted catalytic site. Structure-guided mutagenesis showed acyl-CoA enters through the cytosolic tunnel and cholesterol likely enters from the side through the transmembrane tunnel, rationalizing ACAT1's preference for unsaturated acyl chains. | PMID:32433614 | Nature |
| 2020 | High | Cryo-EM structure of human ACAT1 in complex with the clinical-stage inhibitor nevanimibe confirmed a tetrameric (dimer-of-dimers) holoenzyme; each monomer has nine transmembrane helices with TM4–TM9 forming a cavity that accommodates nevanimibe and an endogenous acyl-CoA; this cavity contains the catalytically essential histidine residue. The structure provides a physical model for cholesterol esterification and inhibitor binding. | PMID:32433613 | Nature |
| 1998 | High | Recombinant human ACAT1 purified to homogeneity exhibits allosteric (sigmoidal) kinetics with respect to cholesterol substrate whether assayed in mixed micelles or reconstituted vesicles, while the oleoyl-CoA saturation curves are hyperbolic, supporting the hypothesis that ACAT1 is an allosteric enzyme regulated by cholesterol. | PMID:9857049 | The Journal of biological chemistry |
| 2000 | High | ACAT1 topology study using glycosylation reporters and FLAG epitope tags showed ACAT1 spans the ER membrane five times with its N-terminus in the cytosol and C-terminus in the ER lumen. The putative active-site serine (Ser269 in ACAT1) is positioned on the cytosolic face; mutation of Ser269 inactivated ACAT1, demonstrating its catalytic essentiality. | PMID:11071899 | Molecular biology of the cell |
| 2006 | High | Histidine residues H386 and H460 in ACAT1 are essential for catalytic activity; H386A and H460A substitutions abolished enzymatic activity without altering substrate-binding affinity, indicating these residues are catalytic rather than structural. Partial restoration of H386A activity with 25-hydroxycholesterol (but not cholesterol) as substrate further defined the catalytic role. | PMID:16647063 | FEBS letters |
| 2010 | High | Purified human ACAT1 binds oleoyl-CoA with Kd ~1.9 μM, inducing significant intrinsic fluorescence changes indicating structural rearrangement; cholesterol binding produces larger fluorescence changes than its diastereomer epicholesterol, demonstrating stereospecificity (3β-OH on steroid ring A) in substrate recognition by ACAT1. | PMID:20964445 | Biochemistry |
| 2014 | High | Mitochondrial ACAT1 was identified as an acetyltransferase for PDHA1 (K321) and PDP1 (K202) in the pyruvate dehydrogenase complex; K321 acetylation of PDHA1 recruits PDK1 to inhibit PDC activity, and K202 acetylation of PDP1 dissociates its substrate PDHA1, both promoting the Warburg effect. SIRT3 acts as the opposing deacetylase. Y381 phosphorylation of PDP1 dissociates SIRT3 and recruits ACAT1 to the PDC. | PMID:24486017 | Molecular cell |
| 2000 | High | In human macrophages, ACAT1 localizes to the tubular rough ER under normal conditions; upon cholesterol loading, ~30–40% of total ACAT1 immunoreactivity shifts into small ER-derived vesicles that are also enriched in the ER marker GRP78, suggesting cholesterol overload activates an ER vesiculation process. | PMID:10623671 | The American journal of pathology |
| 2010 | High | Cholesterol loading of macrophages causes ACAT1 to redistribute from high-density ER membranes to lower-density ER-derived vesicles positive for both ER and trans-Golgi network markers; these vesicles exhibit ~3-fold higher ACAT1-specific enzymatic activity than ER membranes, and reconstitution assays showed this is not due to increased cholesterol content in the vesicles. | PMID:20460577 | Journal of lipid research |
| 1999 | High | The human ACAT1 4.3-kb mRNA is produced from sequences on two different chromosomes (exons 1–16 and P1 promoter on chromosome 1; exon Xa and P7 promoter on chromosome 7), requiring a novel interchromosomal trans-splicing mechanism of two discontinuous precursor RNAs. | PMID:10196189 | The Journal of biological chemistry |
| 2004 | High | The chimeric 4.3-kb human ACAT1 mRNA (derived from chromosomes 1 and 7 via trans-splicing) produces a 56-kDa ACAT1 isoform using a GGC (glycine) start codon upstream of the normal AUG; this 56-kDa isoform localizes to the ER and is enzymatically active. Both chromosomal sequences are required for its production. | PMID:15319423 | The Journal of biological chemistry |
| 2008 | Medium | Production of the 56-kDa ACAT1 isoform from the chimeric mRNA requires two specific RNA secondary structures (stem-loops at nt 1255–1268 from chromosome 7 and nt 1286–1342 from chromosome 1) flanking the GGC start codon; translation initiation from GGC is mediated by an IRES mechanism requiring an upstream AU-constituted structure and downstream GC-rich structure. | PMID:18542101 | Cell research |
| 1998 | High | Immunodepletion experiments demonstrated that ACAT1 protein accounts for ~90% of ACAT activity in adult human liver, ~98% in adrenal gland, ~91% in macrophages, and ~80% in kidney, but only ~19% in intestines, establishing tissue-specific catalytic roles. | PMID:9717734 | Journal of lipid research |
| 2000 | High | In adult human liver, ACAT1 (not ACAT2) accounts for 85–90% of total ACAT activity as measured by immunodepletion. ACAT1 and ACAT2 do not form hetero-oligomeric complexes. In intestinal enterocytes, ACAT2 (not ACAT1) is the dominant isoenzyme, concentrated at villus apices. | PMID:10846185 | The Journal of biological chemistry |
| 2003 | Medium | Purified ACAT1 expressed in insect cells exists preferentially as oligomers (dimer to tetramer); ACAT1 esterifies cholesterol more rapidly than ACAT2, which more efficiently esterifies cholic acid derivatives, demonstrating distinct substrate specificities. Pyripyropene A selectively inhibits ACAT2 (IC50 = 0.64 μM) but not ACAT1. | PMID:13679053 | Biochemical and biophysical research communications |
| 2003 | Medium | ACAT1 selectively esterifies oleic acid over polyunsaturated fatty acids in intact cells and microsomes (THP-1 macrophages), while ACAT2-expressing cells show broader unsaturated fatty acid utilization; K-604 competitively inhibits ACAT1 with respect to oleoyl-CoA (Ki = 0.378 μM), establishing the oleoyl-CoA binding site as part of the active site. | PMID:14617738, PMID:16820149 | Journal of lipid research |
| 2014 | High | Pharmacological blockade (K604) or genetic knockout of ACAT1 in microglia stimulates autophagosome formation and TFEB-mediated lysosomal proteolysis in an mTOR-independent manner, increasing phagocytic uptake and lysosomal degradation of oligomeric Aβ1-42. The effect can be modulated by agents that disrupt cholesterol biosynthesis. | PMID:25339759 | The Journal of neuroscience |
| 2023 | Medium | Acute ACAT1/SOAT1 blockade increases cholesterol content at the mitochondria-associated ER membrane (MAM), where ACAT1 is enriched; this increases the number of ER-mitochondria contact sites and shortens the distance between these organelles, strengthening ER-mitochondria connectivity. | PMID:36982602 | International journal of molecular sciences |
| 2023 | High | ACAT1/SOAT1 blockade in microglia alters the intracellular fate of TLR4 by increasing TLR4 endocytosis and enhancing its trafficking to lysosomes for degradation, thereby suppressing LPS-induced pro-inflammatory signaling. Myeloid-specific Acat1 KO mice showed markedly attenuated LPS-induced neuroinflammation in hippocampus and cortex. | PMID:36982689 | International journal of molecular sciences |
| 2018 | High | Myeloid-specific Acat1 knockout reduces Ly6Chi monocyte integrin-β1 expression, impairing monocyte adhesion to inflamed endothelium and infiltration into adipose tissue; this attenuates Western diet-induced obesity and adipose tissue inflammation. ACAT1 inhibition in RAW264.7 macrophages also reduces LPS-induced inflammatory responses. | PMID:29533741 | American journal of physiology. Endocrinology and metabolism |
| 2010 | Medium | In cholesterol-loaded macrophages, approximately 20% of total ACAT1 co-localizes with the late endosome/lysosome marker LAMP2, and ACAT1-positive membranes isolated by immunoadsorption contain LAMP2; cholesterol-loaded macrophages can re-esterify LDL-derived cholesterol even when cholesterol egress from late endosomes is blocked by U18666A, suggesting ACAT1-positive LE/LS facilitate direct esterification of lipoprotein-derived free cholesterol. | PMID:20523008 | Journal of atherosclerosis and thrombosis |
| 2005 | Medium | ACAT1 deficiency in peritoneal macrophages increases de novo cholesterol synthesis by 134% and upregulates SREBP1a mRNA 6-fold, indicating that ACAT1 normally suppresses the SREBP-driven cholesterol/fatty acid synthesis program; total cellular cholesterol efflux increases proportionally but esterification of new cholesterol is reduced by 93%. | PMID:16144700 | Atherosclerosis |
| 2004 | Medium | ACAT1 deficiency in macrophages reduces overall cellular cholesterol efflux by 25% despite upregulated ABCA1 expression, while efflux of lipoprotein-derived (acLDL) cholesterol is increased by 32%; ACAT1-deficient macrophages accumulate 26% more free cholesterol from acLDL and show a 75% increase in intracellular vesicles. | PMID:15499044 | Arteriosclerosis, thrombosis, and vascular biology |
| 2023 | Medium | ACAT1 acetylates ME2 (malate enzyme 2) at lysine 156, potentiating ME2 enzyme activity and promoting conversion of glutamine-derived malate to pyruvate and subsequently lactate; this ME2-derived lactate facilitates lactylation of homologous recombination repair proteins, contributing to chemoresistance in ovarian cancer. Glucose deprivation triggers this ACAT1-ME2 axis. | PMID:39951294 | Advanced science |
| 2023 | Low | ACAT1 acetylates METTL3, and this interaction (demonstrated by Co-IP and GST pulldown) stabilizes METTL3 protein by inhibiting ubiquitin-proteasome-mediated degradation; ACAT1-mediated METTL3 stabilization suppresses TNBC cell migration and invasion. NR2F6 transcriptionally activates ACAT1 to regulate this axis. | PMID:36890220 | Genes and immunity |
| 2023 | Medium | ACAT1 loss in lung tumor cells leads to mitochondrial protein hypersuccinylation and enhanced mitochondrial oxidative metabolism; this increases ROS, which impedes tertiary lymphoid structure (TLS) formation. ACAT1 knockdown reduced ROS and promoted B-cell aggregation and TLS construction, sensitizing tumors to anti-PD1 therapy. | PMID:40166933 | The Journal of clinical investigation |
| 2024 | Low | SIRT5 acts as a desuccinylase of ACAT1, removing succinyl groups from ACAT1 and enhancing its enzymatic activity; SIRT5-mediated ACAT1 activation then activates the NRF2 pathway and inhibits secretion of CCL5 and CXCL10 chemokines that recruit CD8+ T cells, contributing to an immunosuppressive tumor microenvironment in EGFR-mutant LUAD. | PMID:39524872 | Heliyon |
| 2023 | Low | ACAT1 inhibition suppresses fatty acid oxidation and acetyl-CoA production while increasing free fatty acids in glioblastoma cells; this restores mitochondrial function and negatively regulates the choline metabolic pathway, which is required for GBM cell differentiation into astrocytes. Chlorogenic acid inhibits ACAT1 phosphorylation to achieve this effect. | PMID:39494339 | International journal of biological sciences |
| 2023 | Medium | UBE3A ubiquitin ligase ubiquitinates ACAT1 (identified by orthogonal ubiquitin transfer), promoting its degradation; on a high-fat diet, reduced hepatic UBE3A expression is associated with increased ACAT1 protein and ketone body accumulation; forced UBE3A expression in mouse liver decreases ACAT1 protein content. | PMID:36920305 | Biochemistry |
| 2024 | Medium | ACAT1-deficient preadipocytes show inhibited SREBP2-mediated cholesterol uptake, reduced intracellular and plasma membrane cholesterol, and impaired PPARγ transcription and adipogenesis; rescue with catalytically functional but not catalytic-dead ACAT1 restores cholesterol levels and PPARγ transcription, demonstrating that ACAT1 enzymatic activity is required for normal adipogenesis. | PMID:39481851 | Journal of lipid research |
| 2019 | High | Myeloid-specific Acat1 KO in the ApoE-KO mouse model for advanced atherosclerosis significantly reduced lesion cholesterol crystal content, lesion size, and macrophage content without increasing apoptotic cell death; cell culture studies showed that ACAT1 inhibition in macrophages reduces pro-inflammatory responses to cholesterol loading by acetyl-LDL. | PMID:31495784 | The Journal of biological chemistry |
| 2013 | Medium | Global Acat1 knockout causes a higher proportion of Lin−Sca-1+c-Kit+ hematopoietic stem/progenitor cells to proliferate, resulting in increased myeloid progenitor cell numbers and leukocytosis in normal mice and elevated monocytosis in Apoe−/− mice during atherosclerosis, demonstrating that ACAT1 plays a role in regulating hematopoiesis. | PMID:23846496 | Arteriosclerosis, thrombosis, and vascular biology |
| 2010 | High | ACAT1 gene ablation in a 3xTg-AD mouse model increases 24(S)-hydroxycholesterol content by 32% in the brain at 4 months, decreases HMG-CoA reductase protein by 65%, reduces sterol synthesis rate by 28%, and decreases full-length hAPP and its proteolytic fragments by >60%; treating hippocampal neurons with 24(S)-hydroxycholesterol recapitulates reductions in hAPP and HMGR, placing cholesterol esterification upstream of APP processing. | PMID:20133765 | Proceedings of the National Academy of Sciences |
| 2007 | Medium | ACAT1 RNAi (~50% protein reduction) decreases cholesteryl ester levels by 22%, causes slight increase in ER free cholesterol, and reduces Aβ secretion by 40%, demonstrating that ACAT1 activity influences amyloidogenic APP processing. | PMID:17412327 | FEBS letters |
| 2015 | Medium | ACAT1 inhibition in SK-N-SH neuronal cells increases free cholesterol at the plasma membrane (PM-FC), and this increased PM-FC reduces APP α-processing; the effect on PM-FC and α-processing is independent of total cellular cholesterol and persists even when the NPC-dependent cholesterol trafficking pathway is blocked, identifying an ACAT1-dependent pathway for shuttling PM-FC to the intracellular pool. | PMID:26474739 | Acta biochimica et biophysica Sinica |
| 2009 | Medium | Leptin increases ACAT1 protein expression (~1.9-fold) and ACAT activity (~1.8-fold) in human monocyte-derived macrophages via JAK2 and PI3K signaling pathways, promoting cholesteryl ester accumulation and suppressing HDL-mediated cholesterol efflux; the efflux suppression is reversed by the ACAT1 inhibitor K604. | PMID:19625677 | American journal of physiology. Endocrinology and metabolism |
| 2009 | Medium | TNF-α, through NF-κB, specifically enhances ACAT1 (but not ACAT2) gene expression in differentiating human monocytes; a functional NF-κB element in the human ACAT1 proximal promoter is required for this effect; increased ACAT1 promotes cholesteryl ester accumulation and lipid-laden cell formation. | PMID:19189937 | Journal of lipid research |

## Citations

- PMID:10196189
- PMID:10623671
- PMID:10846185
- PMID:11071899
- PMID:13679053
- PMID:14617738
- PMID:15319423
- PMID:15499044
- PMID:16144700
- PMID:16647063
- PMID:16820149
- PMID:17412327
- PMID:18542101
- PMID:19189937
- PMID:19625677
- PMID:20133765
- PMID:20460577
- PMID:20523008
- PMID:20964445
- PMID:23846496
- PMID:24486017
- PMID:25339759
- PMID:26474739
- PMID:29533741
- PMID:31495784
- PMID:32433613
- PMID:32433614
- PMID:36890220
- PMID:36920305
- PMID:36982602
- PMID:36982689
- PMID:39481851
- PMID:39494339
- PMID:39524872
- PMID:39951294
- PMID:40166933
- PMID:9717734
- PMID:9857049
