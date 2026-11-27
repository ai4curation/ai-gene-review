---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AKT1S1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q96B36
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 26
citation_count: 26
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AKT1S1 (human)

## Current model (mechanistic narrative)

AKT1S1 (PRAS40) is a raptor-binding inhibitory subunit of mTORC1 that couples growth-factor and nutrient signaling to control of protein synthesis, cell growth, and survival [PMID:17386266, PMID:17510057]. PRAS40 binds raptor through a TOS motif (FVMDE) and acts as a substrate-competitive inhibitor, blocking access of mTORC1 substrates such as 4E-BP1; high-resolution structures show it occupies both substrate-recruitment sites of mTORC1, the raptor TOS-binding site and the FRB domain [PMID:17510057, PMID:29236692]. Inhibition is relieved upon phosphorylation: insulin/growth-factor-activated Akt phosphorylates PRAS40 at Thr246, after which mTORC1 itself phosphorylates additional sites (Ser183/Ser221) in a hierarchical manner, driving PRAS40 dissociation from raptor and association with the cytosolic anchor 14-3-3, thereby activating mTORC1 toward S6K1 and 4E-BP1 [PMID:17386266, PMID:17277771, PMID:17604271, PMID:20138985]. Beyond Akt, multiple kinases — PIM1, PKM2, MELK, and PGK1 — directly phosphorylate PRAS40 at Thr246 or adjacent sites to release it from raptor and activate mTORC1 independently of canonical hormone/Akt input, frequently in cancer contexts [PMID:19276681, PMID:26876154, PMID:31813279, PMID:35058442]. PRAS40 also exerts mTORC1-independent functions: nuclear phospho-PRAS40 binds RPL11 to suppress the RPL11–HDM2–p53 nucleolar stress response [PMID:24704832], it couples protein synthesis to immunoproteasome β-subunit assembly [PMID:26876939], and Akt-Thr246 phosphorylation of PRAS40 is necessary and sufficient to drive exosome-mediated secretion [PMID:28674187]. Genetic ablation studies establish PRAS40 as a brake on basal mTORC1 activity that modulates insulin sensitivity, glucose homeostasis, tissue hypertrophy, vascular inflammation, and survival in ischemic injury [PMID:25931147, PMID:20629086, PMID:31728028, PMID:24583056].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0140313 molecular sequestering activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-392499 Metabolism of proteins, R-HSA-5357801 Programmed Cell Death
- **partners:** RPTOR, MTOR, AKT1, YWHAE, PIM1, PKM2, RPL11, PGK1
- **complexes:** mTORC1

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | High | PRAS40 binds to raptor (a component of mTORC1) in insulin-deprived cells, and this interaction inhibits mTORC1 kinase activity. In vitro, PRAS40 prevents the increase in mTORC1 kinase activity induced by Rheb1-GTP. Insulin stimulates Akt/PKB-mediated phosphorylation of PRAS40, which disrupts its inhibition of mTORC1 both in cells and in vitro. | PMID:17386266 | Molecular cell |
| 2007 | High | PRAS40 binds the mTOR kinase domain and its interaction with mTOR is induced under conditions that inhibit mTOR signaling (nutrient/serum deprivation, mitochondrial metabolic inhibition). PRAS40 phosphorylation by Akt and association with the cytosolic anchor 14-3-3 are required for insulin to stimulate mTOR. PRAS40 silencing inactivates IRS-1 and Akt and uncouples mTOR response to Akt signals. | PMID:17277771 | Nature cell biology |
| 2007 | High | PRAS40 contains a TOS (TOR signaling) motif (FVMDE) required for interaction with raptor. PRAS40 inhibits mTORC1 kinase activity in vivo and in vitro by functioning as a direct competitive inhibitor of substrate (4E-BP1) binding to raptor. Insulin stimulation markedly decreases PRAS40 bound to mTORC1. | PMID:17510057 | The Journal of biological chemistry |
| 2007 | High | PRAS40 is a substrate for phosphorylation by mTORC1 itself (in addition to Akt). PRAS40 interacts with raptor via its TOS motif, and requires amino acids and insulin for 14-3-3 binding. Binding of PRAS40 to 14-3-3 is inhibited by TSC1/2 and stimulated by Rheb in a rapamycin-sensitive manner. PRAS40 knockdown impairs amino acid- and insulin-stimulated phosphorylation of 4E-BP1 and S6, placing PRAS40 downstream of mTORC1 but upstream of S6K1 and 4E-BP1. | PMID:17604271 | The Journal of biological chemistry |
| 2007 | High | PRAS40 binds mTORC1 via raptor, is an mTOR phosphorylation substrate, and inhibits mTORC1 autophosphorylation and mTORC1 kinase activity toward 4E-BP1. PRAS40 knockdown in HeLa cells protects against TNFα/cycloheximide-induced apoptosis, and this protection is not mimicked by rapamycin, indicating PRAS40 mediates apoptosis independently of its mTORC1 inhibitory function. | PMID:18030348 | PloS one |
| 2017 | High | Cryo-EM structure of mTORC1 and crystal structure of a truncated mTOR–PRAS40 complex reveal that PRAS40 inhibits both substrate-recruitment sites on mTORC1 (the RAPTOR-TOS motif binding site and the FRB domain site), explaining its substrate-competitive mechanism of mTORC1 inhibition. | PMID:29236692 | Nature |
| 2009 | High | PIM1 protein kinase directly phosphorylates PRAS40 at Thr246 in vitro (an Akt phosphorylation site), independently of Akt activation. PIM1 overexpression reduces PRAS40 association with mTOR and increases mTOR-directed phosphorylation of 4EBP1 and p70S6K. | PMID:19276681 | Cancer biology & therapy |
| 2016 | High | Pyruvate kinase M2 (PKM2) phosphorylates PRAS40 at Ser202/203, releasing PRAS40 from raptor and facilitating its binding to 14-3-3, resulting in hormone- and nutrient-signal-independent activation of mTORC1 in cancer cells. | PMID:26876154 | Scientific reports |
| 2010 | High | Efficient phosphorylation of PRAS40 at Ser183 by mTORC1 requires prior phosphorylation of PRAS40 at Thr246 by PKB/Akt. Substitution of Thr246 with Ala alone is sufficient to abolish 14-3-3 binding under intact mTORC1 signaling conditions, indicating a hierarchical phosphorylation mechanism. | PMID:20138985 | Cellular signalling |
| 2014 | High | Akt- and mTORC1-mediated phosphorylation of PRAS40 at T246 and S221 respectively promotes nuclear-specific association of PRAS40 with ribosomal protein L11 (RPL11). PRAS40 negatively regulates the RPL11-HDM2-p53 nucleolar stress response pathway; PRAS40 silencing induces p53 upregulation dependent on RPL11, and a T246A mutant incapable of RPL11 binding cannot rescue this effect. | PMID:24704832 | Oncogene |
| 2016 | High | mTORC1 sequesters precursors of immunoproteasome β subunits via PRAS40. When mTORC1 is activated, it phosphorylates PRAS40 to simultaneously enhance protein synthesis and facilitate assembly of immunoproteasome β subunits, coupling elevated protein synthesis with immunoproteasome biogenesis to clear aberrant proteins. | PMID:26876939 | Molecular cell |
| 2017 | High | PRAS40 is a unique downstream effector of TGF-α (but not EGF) signaling via Thr308-phosphorylated Akt. Akt-mediated phosphorylation of PRAS40 at Thr246 is both necessary and sufficient to trigger exosome-mediated secretion. PRAS40 knockdown or dominant-negative mutant blocks TGF-α-, hypoxia-, and H2O2-induced exosome secretion without affecting the ER/Golgi pathway. | PMID:28674187 | Molecular and cellular biology |
| 2007 | Medium | Phosphorylated PRAS40 binds the cytosolic docking protein 14-3-3, and this interaction is regulated by the PI3K/Akt pathway. In spinal cord injury models, increased pPRAS40 via PRAS40 transfection promotes motor neuron survival; co-immunoprecipitation shows that pPRAS40–14-3-3 binding increases after injury and is dependent on the PI3K/Akt pathway. | PMID:17457363 | Journal of cerebral blood flow and metabolism |
| 2007 | Medium | PRAS40 is an Akt3 substrate in melanoma. Phospho-PRAS40 levels parallel Akt3 activity during melanoma tumor progression. Targeting PRAS40 (via siRNA) or upstream Akt3 similarly reduces anchorage-independent growth and tumor development, and decreasing pPRAS40 increases tumor cell apoptosis and chemosensitivity. | PMID:17440074 | Cancer research |
| 2011 | Medium | In radioresistant NSCLC cells, nuclear PIM1 phosphorylates PRAS40, and phospho-PRAS40 forms a trimeric complex with 14-3-3 and Akt-activated phospho-FOXO3a, driving cytoplasmic retention of FOXO3a, downregulation of proapoptotic genes, and radioresistance. Protein phosphatases PP2A and PP5 negatively regulate this pathway. | PMID:21910584 | Radiation research |
| 2010 | Medium | In response to leucine (but not insulin), PDK1 is required for PRAS40 phosphorylation and subsequent mTOR/p70S6K activation in the heart. A PDK1 L155E mutation that preserves insulin/Akt-dependent mTOR signaling abolishes leucine-induced PRAS40 phosphorylation, indicating a distinct PDK1-dependent, Akt-independent mechanism for leucine to activate mTORC1 via PRAS40. | PMID:20051528 | American journal of physiology. Endocrinology and metabolism |
| 2010 | Medium | High glucose increases PRAS40 phosphorylation at Thr246 via PI3K/Akt, dissociating PRAS40 from the raptor-PRAS40 complex, thereby activating mTORC1 and promoting mesangial cell hypertrophy. A phosphorylation-deficient PRAS40 mutant (in contrast to PRAS40 knockdown) inhibits 4EBP-1 and S6K phosphorylation and reduces hypertrophy, identifying PRAS40 phosphorylation as the mechanistic node. | PMID:20629086 | Journal of cellular physiology |
| 2012 | Medium | EWS (Ewing sarcoma protein) negatively regulates PRAS40 expression by binding the 3' UTR of PRAS40 mRNA. Loss of EWS leads to elevated PRAS40, which promotes Ewing sarcoma cell proliferation and metastatic growth; PRAS40 knockdown reverses the proliferative effect of EWS knockdown. | PMID:22241085 | Cancer research |
| 2019 | Medium | PRAS40 negatively regulates endothelial mTORC1 and pro-inflammatory signaling. PRAS40 knockdown in endothelial cells promotes TNFα-induced mTORC1 signaling and inflammatory marker upregulation, while PRAS40 overexpression blocks these. In vivo, endothelium-specific PRAS40 deficiency enhances neointimal hyperplasia and atherosclerotic lesion formation. | PMID:31728028 | Scientific reports |
| 2022 | Medium | Phosphoglycerate kinase 1 (PGK1) binds PRAS40 and phosphorylates it at Thr246 under normoxia, suppressing autophagy-mediated cell death and promoting liver cancer cell proliferation. Under hypoxia, PGK1 binding switches from PRAS40 to Beclin1, increasing Beclin1 phosphorylation and autophagy induction. | PMID:35058442 | Cell death & disease |
| 2019 | Medium | MELK kinase phosphorylates PRAS40, disrupting the interaction between PRAS40 and raptor and thereby over-activating mTORC1 signaling to promote clear cell renal cell carcinoma progression. | PMID:31813279 | Cell transplantation |
| 2014 | Medium | PRAS40 gene transfer in rats reduces cerebral infarction size by promoting phosphorylation of Akt, FOXO1, PRAS40, and mTOR. PRAS40 knockout increases infarction size and reduces p-S6K and p-S6 in the mTOR pathway after stroke; co-immunoprecipitation shows less Akt-mTOR interaction in PRAS40 KO, identifying PRAS40 as a physical bridge linking Akt and mTOR signaling in the context of ischemia. | PMID:24583056 | Neurobiology of disease |
| 2015 | Medium | Genetic ablation of PRAS40 in mice results in increased hepatic Akt (T308) and mTORC1 (p-p70S6K) signaling, altered hepatic GLUT4 levels, and improved glucose homeostasis, demonstrating that PRAS40 limits basal mTORC1 activity and insulin sensitivity in vivo. | PMID:25931147 | Biochemical pharmacology |
| 2014 | Medium | Over-expression of wild-type PRAS40 (but not AAA-PRAS40 mutant with mutated phosphorylation and mTORC1-binding sites) impairs insulin-mediated mTORC1 pathway activation but increases Akt phosphorylation and insulin sensitivity in skeletal muscle cells, identifying a role for PRAS40 in regulating insulin sensitivity through IRS1 stabilization and proteasome inhibition, independent of its mTORC1-binding function. | PMID:24576065 | Archives of physiology and biochemistry |
| 2005 | Low | PRAS40 is phosphorylated via the PI3K/Akt pathway (inhibited by wortmannin and LY294002 but not rapamycin); 14-3-3 is identified as a PRAS40 binding protein. PRAS40 constitutive phosphorylation activity is higher in pre-malignant and malignant cancer cell lines compared to normal cells. | PMID:16174443 | Acta pharmacologica Sinica |
| 2019 | Low | AKT3 (but not AKT1 or AKT2) is the specific Akt isoform mediating M2-tumor-associated macrophage-induced phosphorylation of PRAS40 (Thr246) in intrahepatic cholangiocarcinoma cells, leading to EMT activation. AKT3 silencing specifically inhibits p-AKT and p-PRAS40 under M2-TAM co-culture conditions. | PMID:31692069 | Journal of cellular biochemistry |

## Citations

- PMID:16174443
- PMID:17277771
- PMID:17386266
- PMID:17440074
- PMID:17457363
- PMID:17510057
- PMID:17604271
- PMID:18030348
- PMID:19276681
- PMID:20051528
- PMID:20138985
- PMID:20629086
- PMID:21910584
- PMID:22241085
- PMID:24576065
- PMID:24583056
- PMID:24704832
- PMID:25931147
- PMID:26876154
- PMID:26876939
- PMID:28674187
- PMID:29236692
- PMID:31692069
- PMID:31728028
- PMID:31813279
- PMID:35058442
