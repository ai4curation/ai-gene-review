---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARL6IP5
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: O75915
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 32
citation_count: 33
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARL6IP5 (human)

## Current model (mechanistic narrative)

ARL6IP5 (GTRAP3-18/JWA/PRAF3) is a four-transmembrane PRA1-domain endoplasmic reticulum protein that governs the ER residence and surface delivery of membrane transporters and acts more broadly as an ER membrane-shaping factor [PMID:18167356, PMID:40209949]. Its founding function is to bind the C-terminal intracellular domain of the neuronal glutamate/cysteine transporter EAAC1, retaining it in the ER and lowering its substrate affinity, thereby restricting EAAC1-mediated cysteine uptake and dominantly suppressing intracellular glutathione synthesis [PMID:11242046, PMID:18167356, PMID:17646425, PMID:18799673, PMID:21373771]; loss of ARL6IP5 in mice raises plasma-membrane EAAC1, elevates neuronal GSH, and confers neuroprotection against oxidative stress [PMID:18799673, PMID:22210510]. This trafficking control reflects a general role as a negative regulator of Rab1-dependent ER-to-Golgi transport, an activity rescued by Rab1 co-expression [PMID:18363836, PMID:29872729]. Through its PRA1 domain ARL6IP5 constricts ER tubules and shapes the tubular ER network, and is required for FAM134B-mediated ER-phagy [PMID:40209949]; consistent with a reticulophagy role, it promotes autophagy/ER-phagy via Ca2+/AMPK signaling and interaction with CALCOCO1 to clear pathological aggregates [PMID:39394963]. The protein also retains other secretory cargos in the ER, including POMC—limiting α-MSH secretion to influence food intake [PMID:28904020]—and RANKL, decreasing soluble RANKL and inhibiting osteoclastogenesis [PMID:26220341], while controlling ER calcium and CHOP-dependent ER stress in osteoblasts [PMID:25321471]. In a distinct nuclear/cytoplasmic role, ARL6IP5 (as JWA) functions in DNA single-strand-break base excision repair by interacting with XRCC1, being shuttled to the nucleus by XRCC1, transcriptionally upregulating XRCC1 via MAPK/E2F1, and protecting it from ubiquitin-proteasomal degradation [PMID:19208635]. ARL6IP5 protein levels are themselves controlled by RNF185-mediated ubiquitination at K158 [PMID:29481911]. Acting through MAPK cascades (ERK/FAK/COX-2) and integrin αVβ3/Sp1 signaling, it restrains cancer cell migration, adhesion, and invasion [PMID:19946336, PMID:17336041], and modulates the abundance of multiple receptors and death-pathway components by directing E3-ligase–dependent ubiquitination—promoting HER2 degradation via c-Cbl and SMURF1, and DR4 degradation via MARCH8 to suppress TRAIL-induced apoptosis [PMID:28671676, PMID:27708243, PMID:33875644]. It additionally protects dopaminergic neurons by occupying the ferritin-binding site of NCOA4 to inhibit ferritinophagy and ferroptosis [PMID:38744191].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0005198 structural molecule activity
- **localization:** GO:0005783 endoplasmic reticulum, GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9612973 Autophagy, R-HSA-73894 DNA Repair, R-HSA-162582 Signal Transduction, R-HSA-392499 Metabolism of proteins
- **partners:** EAAC1, XRCC1, RAB1, POMC, RANKL, NCOA4, RNF185, CALCOCO1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | High | GTRAP3-18 (ARL6IP5) specifically interacts with the carboxy-terminal intracellular domain of EAAC1 (neuronal glutamate transporter), localizes to the cell membrane and cytoplasm, and increasing GTRAP3-18 expression reduces EAAC1-mediated glutamate transport by lowering substrate affinity. | PMID:11242046 | Nature |
| 2007 | High | GTRAP3-18 is a resident endoplasmic reticulum protein that delays ER exit of EAAC1 and other excitatory amino acid transporter family members; it self-associates via hydrophobic domain interactions in the ER membrane and uses cytoplasmic C-terminal interactions to regulate trafficking. | PMID:18167356 | The Journal of biological chemistry |
| 2007 | High | GTRAP3-18 at the plasma membrane negatively and dominantly regulates intracellular glutathione content by controlling EAAC1-mediated cysteine uptake; increasing cell-surface GTRAP3-18 (via methyl-β-cyclodextrin) decreases GSH, while decreasing it (via antisense oligonucleotides) increases GSH. | PMID:17646425, PMID:18799673, PMID:21373771 | Molecular pharmacology |
| 2008 | High | GTRAP3-18 acts as a negative regulator of Rab1, inhibiting ER-to-Golgi trafficking; overexpression reduces VSVG transport rate, slows cargo concentration of EAAC1 into transport complexes, and inhibits neurite outgrowth in CAD cells—effects rescued by Rab1 co-expression. | PMID:18363836 | Journal of cellular and molecular medicine |
| 2008 | High | GTRAP3-18 interacts with EAAC1 at the plasma membrane and dominantly determines intracellular neuronal glutathione levels; genetic reduction of GTRAP3-18 in mouse brain increases plasma membrane EAAC1 and raises brain GSH, while overexpression suppresses GSH. | PMID:18799673 | The Journal of neuroscience |
| 2009 | High | JWA interacts with XRCC1 and functions as a base excision repair protein for oxidative-stress-induced DNA single-strand breaks: JWA is translocated to the nucleus by XRCC1, co-localizes with XRCC1 foci after DNA damage, regulates XRCC1 transcriptionally via MAPK/E2F1, and protects XRCC1 from ubiquitination and proteasomal degradation. | PMID:19208635 | Nucleic acids research |
| 2009 | Medium | JWA knockdown increases melanoma cell adhesion and invasion and promotes metastatic colony formation in vivo by intensifying integrin αVβ3 signaling through regulation of nuclear factor Sp1. | PMID:19946336 | Oncogene |
| 2007 | Medium | JWA is required for rearrangement of F-actin cytoskeleton and activation of MAPK cascades (ERK, downstream FAK and COX-2) induced by As2O3 and PMA; JWA overexpression alone inhibits cancer cell migration, while JWA deficiency accelerates migration. SDR-SLR motifs of JWA are critical for MAPK cascade activation and cell migration. | PMID:17336041 | Cellular signalling |
| 2011 | High | GTRAP3-18-deficient mice show increased EAAC1 expression at the plasma membrane, increased neuronal GSH content, and neuroprotection against oxidative stress, as well as improved motor/spatial learning and memory. | PMID:22210510 | Neurobiology of disease |
| 2014 | Medium | JWA regulates cisplatin-induced DNA damage and apoptosis through the CK2-phospho-XRCC1-XRCC1 pathway: in normal cells JWA upregulates XRCC1, but in cisplatin-resistant gastric cancer cells JWA promotes XRCC1 degradation; mutation of CK2-targeted 518S/519T/523T residues of XRCC1 blocks this negative regulation. | PMID:25476899 | Cell death & disease |
| 2018 | Medium | E3 ubiquitin ligase RNF185 directly interacts with JWA and promotes its ubiquitination at K158, leading to proteasomal degradation; RNF185 expression is negatively correlated with JWA in gastric cancer tissues. | PMID:29481911 | Biochimica et biophysica acta. Molecular basis of disease |
| 2017 | Medium | JWA suppresses TRAIL-induced apoptosis in cisplatin-resistant gastric cancer cells by promoting ubiquitination of death receptor 4 (DR4) at K273 via upregulation of the E3 ubiquitin ligase MARCH8; JWA and DR4 protein levels are negatively correlated in gastric cancer tissues. | PMID:28671676 | Oncogenesis |
| 2014 | Medium | Arl6ip5 is expressed in osteoblasts and functions as an ER calcium regulator controlling calmodulin signaling for osteoblast proliferation; Arl6ip5 deficiency induces ER stress and ER stress-mediated apoptosis (via CHOP), impairs osteoblast differentiation, and increases RANKL expression to enhance osteoclastogenesis. | PMID:25321471 | Cell death & disease |
| 2015 | Medium | Overexpression of Arl6ip5 in osteoblasts retains RANKL in the ER, decreases soluble RANKL secretion, and inhibits osteoclastogenesis; Arl6ip5 physically binds RANKL and disrupts the RANKL-OPG complex. Deletion of the NH2-terminal 1–36 amino acids of Arl6ip5 abolishes its interaction with RANKL and restores RANKL secretion. | PMID:26220341 | Biochemical and biophysical research communications |
| 2017 | Medium | GTRAP3-18 interacts with pro-opiomelanocortin (POMC) in the ER, retaining it and reducing α-MSH secretion; GTRAP3-18-deficient mice show hypophagia, lean bodies, elevated α-MSH levels, and AMPK inhibition, effects reversed by melanocortin 4 receptor antagonist. | PMID:28904020 | FASEB journal |
| 2018 | Medium | Astrocytic JWA deficiency reduces expression of the glutamate transporter GLT-1 and glutamate uptake in vivo and in vitro; this occurs via suppression of MAPK and PI3K/CREB signaling. JWA-increased GLT-1 expression is abolished by MEK and PI3K inhibitors and by CREB silencing. | PMID:29500411 | Cell death & disease |
| 2011 | Medium | JWA is required for chronic morphine-induced maintenance of delta opioid receptor (DOR) stability via the ubiquitin-proteasome pathway; JWA knockdown in rats reduces morphine withdrawal response and suppresses DOR expression as well as DARPP-32 and MAP kinase activation. | PMID:21600884 | Biochemical and biophysical research communications |
| 2024 | Medium | JWA physically occupies the ferritin binding site of NCOA4 (nuclear receptor coactivator 4), thereby inhibiting NCOA4-mediated ferritinophagy and reducing iron-dependent ferroptosis in dopaminergic neurons; molecular docking, co-immunoprecipitation, and immunofluorescence confirm direct JWA-NCOA4 interaction. | PMID:38744191 | Redox biology |
| 2025 | High | ARL6IP5 is an ER membrane-shaping protein containing the PRA1 domain; upon overexpression it induces extensive ER tubular networks and constricts the ER membrane (excluding luminal ER enzymes from tubules). ARL6IP5 knockdown impairs ER morphology and reduces FAM134B-mediated ER-phagy flux. Disruption of putative short hairpin structures in the PRA1 domain abolishes membrane constriction. ARL6IP5 and ARL6IP1 (an RHD-containing protein) can functionally substitute for each other in ER shaping. | PMID:40209949 | The Journal of biological chemistry |
| 2023 | Medium | ARL6IP5 induces autophagy and reduces α-synuclein aggregate burden by stabilizing free ATG12 (preventing its ubiquitination and degradation) and enhancing Rab1-dependent autophagosome initiation and elongation. | PMID:37445677 | International journal of molecular sciences |
| 2024 | Medium | ARL6IP5 induces reticulophagy to reduce PrPSc burden and alleviate ER stress; ARL6IP5-induced reticulophagy depends on Ca2+-mediated AMPK activation and involves physical interaction with reticulophagy receptor CALCOCO1 and lysosomal marker LAMP1 for lysosomal degradation. | PMID:39394963 | Autophagy |
| 2018 | Low | Rab1a can rescue the cytotoxicity caused by PRAF3 (ARL6IP5) overexpression, presumably by positively regulating ER-to-Golgi trafficking and counteracting the negative modulation by PRAF3. | PMID:29872729 | Biochemistry and biophysics reports |
| 2016 | Medium | JWA suppresses EGF-induced cell migration and actin cytoskeletal rearrangement in HER2-overexpressing gastric cancer cells by downregulating HER2 expression through ERK activation and consequent PEA3 upregulation; modulation of HER2 by JWA is ERK/PEA3-dependent. | PMID:27167206 | Oncotarget |
| 2016 | Medium | JWA promotes HER2 degradation via the E3 ubiquitin ligase c-Cbl, representing a mechanism for JWA-induced HER2 downregulation that confers lapatinib resistance while reversing cisplatin resistance in gastric cancer cells. | PMID:27708243 | Oncotarget |
| 2021 | Medium | JWA suppresses HER2 ubiquitination and proliferation of HER2-positive breast cancer through the E3 ubiquitin ligase SMURF1 (increased by JAC1-mediated decrease of NEDD4, the E3 ligase for SMURF1); JWA promotes HER2 ubiquitination at K716 via SMURF1. | PMID:33875644 | Cell death discovery |
| 2018 | Medium | JWA suppresses breast cancer cell invasion by negatively regulating cell-surface CXCR4 expression via proteasome-mediated degradation (not transcriptional inhibition); normalizing CXCR4 reverses JWA's inhibitory effect on invasion. | PMID:29658570 | Molecular medicine reports |
| 2022 | Medium | JWA deficiency promotes NOTCH1 degradation via the ERK/FBXW7-mediated ubiquitin-proteasome pathway, thus disturbing the PPARγ/STAT5 axis and reducing intestinal stem cell function and epithelial cell lineage distribution. | PMID:36147468 | International journal of biological sciences |
| 2023 | Medium | JWA negatively regulates CD44 expression in lung cancer by inhibiting ubiquitination-mediated degradation of SP1 (Specificity Protein 1); nicotine downregulates JWA via the CHRNA5-mediated AKT pathway, leading to elevated SP1 and CD44. | PMID:37224781 | Ecotoxicology and environmental safety |
| 2023 | Medium | JAC4 promotes NEDD4L stability via AMPK-mediated phosphorylation at Thr367; the WW domain of NEDD4L (E3 ubiquitin ligase) interacts with EGFR and promotes its ubiquitination at K716, leading to EGFR degradation; this cascade is initiated by JAC4 directly binding CTBP1 and blocking its nuclear translocation, thereby de-repressing JWA gene transcription. | PMID:37240137 | International journal of molecular sciences |
| 2022 | Medium | JAC1 specifically binds YY1 and eliminates its transcriptional repression of the JWA gene; JAC1 also promotes ubiquitination and degradation of YY1, and disrupts the YY1-HSF1 interaction. | PMID:35383155 | Cell death discovery |
| 2008 | Medium | JWA knockdown attenuates arsenic trioxide (As2O3)-induced apoptosis in HeLa and MCF-7 cells; JWA is required for As2O3-induced mitochondrial transmembrane potential loss, caspase-9 activation, and MEK1/2, ERK1/2, and JNK phosphorylations. JWA expression is induced by intracellular ROS generated by As2O3. | PMID:18387645 | Toxicology and applied pharmacology |
| 2014 | Medium | JWA deficiency in neurons (JWA-nKO mice) enhances neurogenesis (survival/migration of newborn neurons and neurite growth) and lowers the LTP threshold in hippocampal dentate gyrus via the FAK-PI3K-Akt-mTOR pathway; PI3K or FAK inhibition abolishes enhanced neurogenesis and LTP; telomerase inhibition suppresses both neurogenesis and LTP enhancement. | PMID:25432888 | Molecular neurobiology |

## Citations

- PMID:11242046
- PMID:17336041
- PMID:17646425
- PMID:18167356
- PMID:18363836
- PMID:18387645
- PMID:18799673
- PMID:19208635
- PMID:19946336
- PMID:21373771
- PMID:21600884
- PMID:22210510
- PMID:25321471
- PMID:25432888
- PMID:25476899
- PMID:26220341
- PMID:27167206
- PMID:27708243
- PMID:28671676
- PMID:28904020
- PMID:29481911
- PMID:29500411
- PMID:29658570
- PMID:29872729
- PMID:33875644
- PMID:35383155
- PMID:36147468
- PMID:37224781
- PMID:37240137
- PMID:37445677
- PMID:38744191
- PMID:39394963
- PMID:40209949
