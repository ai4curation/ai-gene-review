---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T14:16:14.724517'
end_time: '2026-05-12T14:35:14.133362'
duration_seconds: 1139.41
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

Concise GO annotation research for human POMC / UniProt P01189. Focus only on evidence relevant to GO curation: POMC as a secreted prohormone cleaved into ACTH, alpha-MSH, beta-MSH, gamma-MSH, beta-endorphin and met-enkephalin; melanocortin receptor binding versus generic GPCR binding; hormone activity; regulation of appetite, pigmentation, glucocorticoid secretion, adrenal cortex function, pain/opioid signaling and stress response; processing by PCSK1/PC1-3 and PCSK2; tissue-specific processing in pituitary and hypothalamic neurons; caveats for gene-level annotations that conflate distinct cleavage-product functions, generic protein binding, identical protein binding, and broad developmental/behavioral terms. Include PMID/DOI citations and keep under 1500 words.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

Concise GO annotation research for human POMC / UniProt P01189. Focus only on evidence relevant to GO curation: POMC as a secreted prohormone cleaved into ACTH, alpha-MSH, beta-MSH, gamma-MSH, beta-endorphin and met-enkephalin; melanocortin receptor binding versus generic GPCR binding; hormone activity; regulation of appetite, pigmentation, glucocorticoid secretion, adrenal cortex function, pain/opioid signaling and stress response; processing by PCSK1/PC1-3 and PCSK2; tissue-specific processing in pituitary and hypothalamic neurons; caveats for gene-level annotations that conflate distinct cleavage-product functions, generic protein binding, identical protein binding, and broad developmental/behavioral terms. Include PMID/DOI citations and keep under 1500 words.

## Concise GO-annotation research report: human **POMC** (UniProt **P01189**)

### Scope and GO-curation framing
**Pro-opiomelanocortin (POMC)** is best curated in GO as a **secreted prohormone precursor** that is sorted to regulated secretory granules and **proteolytically processed in a tissue-specific manner** to yield multiple bioactive peptides (ACTH, α/β/γ-MSH, β-endorphin; enkephalin motifs embedded in the β-LPH/β-endorphin region). Most experimentally demonstrated receptor binding and “hormone activity” properties belong to the **cleavage products** rather than the intact precursor, which is a central curation caveat. (cawley201660yearsof pages 15-16, harno2018pomcthephysiological pages 1-2)

### 1) Key concepts/definitions (GO-relevant)
**Processing enzymes / pathway concepts**
- Canonical regulated-secretory-pathway processing of POMC uses **PCSK1/PC1-3** and **PCSK2/PC2** endoproteolysis, followed by exopeptidase trimming (e.g., **CPE**) and additional modifications that can alter activity (e.g., acetylation affecting β-endorphin opioid activity). (cawley201660yearsof pages 10-11, lindberg2021obesitypomcand pages 2-3)
- **Tissue specificity:** anterior pituitary corticotrophs predominantly generate ACTH (less extensive processing), while tissues with additional convertase activities (e.g., pars intermedia/hypothalamic contexts) generate further products such as α-MSH and β-endorphin. (harno2018pomcthephysiological pages 2-3, cawley201660yearsof pages 15-16)
- **Human pituitary evidence for dual processing systems:** human pituitary contains components for both the classic PC pathway (**PC1/3, PC2, CPE**) and an alternative **cathepsin L + aminopeptidase B** processing pathway; western blots detect ACTH- and β-endorphin-immunoreactive products consistent with POMC processing. (Hook et al., 2009-04-03, https://doi.org/10.1007/s12020-009-9163-5) (hook2009humanpituitarycontains pages 1-2, hook2009humanpituitarycontains pages 4-5)

**Melanocortins and receptor specificity (avoid generic GPCR binding)**
- Melanocortins are POMC-derived peptides sharing a conserved HFRW pharmacophore and binding melanocortin receptors (MCRs). (fridmanis2017acthreceptor(mc2r) pages 1-2)
- **MC2R (ACTH receptor) is uniquely selective**: MC2R binds a **single endogenous ligand, ACTH**—important for GO term choice (**melanocortin receptor binding** rather than generic GPCR binding). (Fridmanis et al., 2017-02-06, https://doi.org/10.3389/fendo.2017.00013) (fridmanis2017acthreceptor(mc2r) pages 1-2)

**Opioid peptides / embedded enkephalins**
- Sequence/biochemistry literature documents that **Met-enkephalin and Leu-enkephalin motifs** are embedded within the **β-LPH/β-endorphin** region and can be liberated by proteolytic processing/digestion, supporting an evidential link from POMC processing to opioid peptide generation (but not necessarily implying high abundance of free enkephalin in every POMC tissue). (Smyth, 2016-05, https://doi.org/10.1530/jme-16-0033) (smyth201660yearsof pages 2-4)

### 2) Recent developments (prioritizing 2023–2024)
**Appetite regulation update (2023)**
- A 2023 review summarizes evidence that **α-MSH** (cleaved from POMC) is released from arcuate POMC neurons and acts on **MC3R/MC4R-expressing neurons** to suppress appetite and increase energy expenditure, integrating with AgRP antagonism and other appetite signals. (Wu et al., 2023-04-24, https://doi.org/10.1159/000530804) (wu2023alphamelanocytestimulatinghormonemediatedappetite pages 1-2)

**Tool-compounds/drug-discovery context (2024)**
- A 2024 pharmacology review highlights how synthetic α-MSH derivatives (e.g., NDP-α-MSH analog series) are widely used as **tool compounds** to interrogate melanocortin receptors and as scaffolds for therapeutics, reinforcing that the relevant molecular function is **melanocortin receptor binding**, not generic GPCR binding. (Weirath & Haskell-Luevano, 2024-08, https://doi.org/10.1021/acsptsci.4c00129) (weirath2024recommendedtoolcompounds pages 19-19)

### 3) Current applications / real-world implementations (GO-relevant)
- **Clinical melanocortin pharmacology** relies on receptor specificity: MC2R-selective antagonism has been pursued as a strategy to block **ACTH-driven steroidogenesis** (e.g., ACTH excess conditions), leveraging the “single endogenous ligand” specificity concept. (yuan2022ligandsformelanocortin pages 3-4)
- Central melanocortin pathways are a major translational axis for obesity therapeutics (e.g., pharmacologic modulation of MC4R circuits); this supports GO BP annotation around **regulation of feeding behavior/appetite/energy homeostasis** but should be attributed to **α/β-MSH → MC3R/MC4R signaling**, not to “POMC binds GPCRs” generically. (wu2023alphamelanocytestimulatinghormonemediatedappetite pages 1-2, lindberg2021obesitypomcand pages 2-3)

### 4) Authoritative expert synthesis and curation caveats
Key expert/authoritative sources emphasize that POMC biology depends on **which peptide(s)** are produced, in **which tissue**, and in what **modified state**, and that measurement of precursor vs fragments can confound interpretation—directly relevant to GO curation boundaries. (harno2018pomcthephysiological pages 1-2, cawley201660yearsof pages 10-11)

**Specific caveats requested for GO curation**
1. **Gene-level conflation:** Avoid annotating POMC (precursor) directly with all cleavage-product functions (e.g., both “melanocortin receptor binding” and “opioid receptor binding”) unless the annotation model explicitly supports product-level entities. (harno2018pomcthephysiological pages 44-45, cawley201660yearsof pages 15-16)
2. **Melanocortin receptor binding vs generic GPCR binding:** Prefer **melanocortin receptor binding** terms, with **MC2R specificity for ACTH** explicitly supported; do not use generic “GPCR binding” for POMC gene product as a catch-all. (fridmanis2017acthreceptor(mc2r) pages 1-2, yuan2022ligandsformelanocortin pages 3-4)
3. **Generic protein binding / identical protein binding:** Do not annotate generic binding (including “identical protein binding”) unless there is direct biochemical interaction evidence for the relevant molecular entity (precursor vs peptide). The reviewed literature instead supports **processing-dependent receptor binding**. (cawley201660yearsof pages 10-11, harno2018pomcthephysiological pages 1-2)
4. **Broad behavior/development terms:** Appetite and stress are supported mechanistically through defined endocrine/neuropeptide pathways (α-MSH → MC3R/MC4R; ACTH → MC2R). Prefer pathway-grounded BP terms (e.g., regulation of food intake; regulation of glucocorticoid secretion) over very broad behavior/development annotations. (wu2023alphamelanocytestimulatinghormonemediatedappetite pages 1-2, fridmanis2017acthreceptor(mc2r) pages 1-2)

### 5) Curation-relevant functions/processes and quantitative evidence
**Processing evidence and peptide quantitation (human pituitary)**
- Hook et al. report western blots detecting POMC-derived ACTH products (including a band co-migrating with standard ACTH) and β-endorphin products (including a band co-migrating with standard β-endorphin), alongside detection of processing enzymes (PC1/3, PC2, CPE) and cathepsin L pathway components in human pituitary. (hook2009humanpituitarycontains pages 4-5, hook2009humanpituitarycontains pages 1-2)
- Quantitation in this study reports (units as presented): **ACTH 4.94 ± 1.73 pmol/µg**, **α-MSH 0.138 pmol/µg**, **β-endorphin 0.382 fmol/µg** pituitary protein. (hook2009humanpituitarycontains pages 4-5)
- Visual evidence: the dual-pathway processing schematic and mapping of ACTH/α-MSH/β-endorphin within POMC are shown in Hook et al. figures. (hook2009humanpituitarycontains media 305ec3c4, hook2009humanpituitarycontains media e02b8ab2)

**Receptor-binding specificity and binding constants**
- MC2R specificity: MC2R binds only ACTH endogenously. (fridmanis2017acthreceptor(mc2r) pages 1-2, yuan2022ligandsformelanocortin pages 3-4)
- Quantitative receptor pharmacology compiled for melanocortin peptides includes example **Ki** values for α-MSH and ACTH across MCRs (illustrating higher affinity at MC1R and differing affinities across receptors) and notes the requirement of the N-terminal ACTH residues for MC2R activation. (yuan2022ligandsformelanocortin pages 3-4)

**Appetite/energy homeostasis statistics**
- Review synthesis indicates **~2–5% of morbidly obese humans have loss-of-function MC4R mutations**, contextualizing the importance of α/β-MSH→MC4R signaling for feeding regulation. (lindberg2021obesitypomcand pages 2-3)

**Opioid receptor binding evidence**
- β-endorphin is described as a POMC-derived peptide that binds opioid receptors (μ/δ/κ) with agonist activity for major forms. (lindberg2021obesitypomcand pages 2-3)
- Embedded enkephalin motifs within β-LPH/β-endorphin are supported by sequence/digestion evidence, consistent with opioid-signaling potential arising from POMC processing. (smyth201660yearsof pages 2-4, harno2018pomcthephysiological pages 1-2)

### Curation-focused mapping table
| Entity | Processing / evidence basis | Recommended GO MF | Recommended GO BP | Curation caveats / NOT guidance | Key citations |
|---|---|---|---|---|---|
| **POMC precursor (human P01189)** | Secreted prohormone sorted to dense-core granules; tissue-specific cleavage by **PCSK1/PC1-3** and **PCSK2/PC2** with trimming by **CPE**; human pituitary also contains **cathepsin L + aminopeptidase B** alternative processing components. Anterior pituitary mainly PC1/3→ACTH/β-LPH; hypothalamus/pars intermedia uses additional PC2 for more extensive processing. | **hormone activity** only if curator policy allows precursor-level annotation for secreted prohormone; otherwise reserve direct receptor-binding MF for mature peptides. | **peptide hormone processing**, **regulated secretory pathway**, broad precursor role in endocrine/neuropeptide secretion. | **Do NOT assign peptide-specific receptor binding to intact precursor**; avoid generic **GPCR binding**, **protein binding**, **identical protein binding** unless direct evidence exists for intact POMC; avoid collapsing all cleavage-product biology into one gene-level annotation. | (cawley201660yearsof pages 15-16, hook2009humanpituitarycontains pages 1-2) |
| **ACTH** | Generated from POMC primarily by **PC1/3**; further processing can occur in tissues with **PC2**. | **hormone activity**; **melanocortin receptor binding** with specific support for **MC2R/ACTH receptor** binding rather than generic GPCR binding. | **positive regulation of glucocorticoid secretion**; **adrenal cortex development/function/homeostasis**; **stress response / HPA axis**. | Prefer **melanocortin receptor binding** or ACTH-specific receptor statements over generic GPCR binding. ACTH is the **sole endogenous ligand for MC2R**; do not generalize this specificity to all POMC products. | (fridmanis2017acthreceptor(mc2r) pages 1-2, yuan2022ligandsformelanocortin pages 3-4) |
| **α-MSH** | Produced from ACTH region after additional cleavage in PC2-expressing tissues; acetylation/amidation influence bioactivity. | **hormone activity**; **melanocortin receptor binding** (especially **MC1R**, **MC3R**, **MC4R**; not MC2R). | **regulation of appetite/food intake**, **energy homeostasis**, **pigmentation**, also stress-linked melanocortin signaling. | Curate to peptide-level where possible. Do **not** annotate as generic GPCR binding. For appetite, prefer specific melanocortin-process terms over broad behavior terms. | (wu2023alphamelanocytestimulatinghormonemediatedappetite pages 1-2, lindberg2021obesitypomcand pages 2-3) |
| **β-MSH** | Human POMC product generated by processing of β-LPH region; absent in some rodents, so use **human-specific** evidence carefully. | **hormone activity**; **melanocortin receptor binding**. | **regulation of appetite / feeding / body weight**; possible pigmentation-related melanocortin signaling. | Strong caveat against inferring from mouse where β-MSH is not produced. Avoid assigning to intact precursor without human peptide evidence. | (lindberg2021obesitypomcand pages 2-3, yuan2022ligandsformelanocortin pages 4-5) |
| **γ-MSH** | Derived from N-terminal POMC domain with additional cleavage/amidation steps. | **hormone activity**; **melanocortin receptor binding**. | Melanocortin signaling; some appetite/energy-homeostasis relevance depending on subtype/context. | Evidence is weaker/more context-dependent than for ACTH or α-MSH; avoid over-annotation to broad systemic physiology without direct support. | (yuan2022ligandsformelanocortin pages 4-5, harno2018pomcthephysiological pages 44-45) |
| **β-endorphin** | Derived from β-LPH region via PC processing; human pituitary western blots detect β-endorphin products; acetylation/proteolysis modulate activity. | **hormone activity / neuropeptide hormone activity**; **opioid receptor binding** (μ/δ/κ, strongest emphasis often on μ). | **pain / antinociception**, **opioid signaling**, **stress response**, some **energy homeostasis** roles. | Use **opioid receptor binding**, not generic receptor binding or generic protein binding. Distinguish β-endorphin from melanocortin-mediated functions of other POMC peptides. | (lindberg2021obesitypomcand pages 2-3, hook2009humanpituitarycontains pages 4-5) |
| **Met-enkephalin sequence within POMC-derived β-endorphin / β-LPH** | Sequence evidence shows **Met-enkephalin motif embedded** in β-LPH/β-endorphin and can be liberated by proteolytic processing/digestion. | If annotated at all, use peptide-level **opioid receptor binding / hormone activity** only for the liberated opioid peptide, not for intact POMC. | **opioid signaling**, **antinociception/pain modulation**. | Major caveat: evidence often shows **embedded sequence / potential liberation**, not necessarily abundant standalone peptide production in every human POMC-expressing tissue. Avoid assigning met-enkephalin functions directly to intact precursor or without peptide-level evidence. | (smyth201660yearsof pages 2-4, harno2018pomcthephysiological pages 1-2) |
| **Gene-level summary annotation policy** | Aggregate only precursor-supported facts: secreted prohormone, regulated secretion, proteolytic processing by PCSK1/2 (and cathepsin L pathway components in human pituitary). | Conservative gene-level MF: precursor **hormone activity** may be acceptable; peptide-specific receptor binding should usually remain product-level. | Conservative BP: **peptide hormone processing**, **regulated secretion**, and only well-supported shared processes. | **Avoid** generic **GPCR binding**, **protein binding**, **identical protein binding**, broad **behavior**, **development**, or omnibus endocrine annotations that conflate ACTH, melanocortins, and opioid peptides. | (harno2018pomcthephysiological pages 44-45, harno2018pomcthephysiological pages 2-3) |


*Table: This table maps human POMC precursor and major cleavage products to GO-relevant molecular functions and biological processes, while highlighting the processing evidence and the main annotation pitfalls. It is useful for separating precursor-level annotations from mature peptide-specific functions during GO curation.*

### Recommended minimal GO annotation set (high-confidence, gene-level)
If constrained to gene-level annotations only (without peptide-level product entities), conservative high-confidence choices supported by direct evidence include:
- **Extracellular / secretory granule / regulated secretion context** and **peptide hormone processing** (processing by PCSK1/PCSK2; evidence of pituitary processing components). (cawley201660yearsof pages 15-16, hook2009humanpituitarycontains pages 1-2)
- **Precursor role in endocrine/neuropeptide hormone production** (avoid assigning specific receptor binding unless using peptide-level entities). (harno2018pomcthephysiological pages 1-2, cawley201660yearsof pages 15-16)

For peptide-level annotations (preferred), assign receptor-binding and downstream process terms to **ACTH, α/β/γ-MSH, β-endorphin** separately, per the table. (fridmanis2017acthreceptor(mc2r) pages 1-2, wu2023alphamelanocytestimulatinghormonemediatedappetite pages 1-2)



References

1. (cawley201660yearsof pages 15-16): Niamh X Cawley, Zhaojin Li, and Y Peng Loh. 60 years of pomc: biosynthesis, trafficking, and secretion of pro-opiomelanocortin-derived peptides. Journal of molecular endocrinology, 56 4:T77-97, May 2016. URL: https://doi.org/10.1530/jme-15-0323, doi:10.1530/jme-15-0323. This article has 210 citations and is from a peer-reviewed journal.

2. (harno2018pomcthephysiological pages 1-2): Erika Harno, Thanuja Gali Ramamoorthy, Anthony P. Coll, and Anne White. Pomc: the physiological power of hormone processing. Physiological reviews, 98 4:2381-2430, Oct 2018. URL: https://doi.org/10.1152/physrev.00024.2017, doi:10.1152/physrev.00024.2017. This article has 299 citations and is from a highest quality peer-reviewed journal.

3. (cawley201660yearsof pages 10-11): Niamh X Cawley, Zhaojin Li, and Y Peng Loh. 60 years of pomc: biosynthesis, trafficking, and secretion of pro-opiomelanocortin-derived peptides. Journal of molecular endocrinology, 56 4:T77-97, May 2016. URL: https://doi.org/10.1530/jme-15-0323, doi:10.1530/jme-15-0323. This article has 210 citations and is from a peer-reviewed journal.

4. (lindberg2021obesitypomcand pages 2-3): Iris Lindberg and Lloyd D Fricker. Obesity, pomc, and pomc-processing enzymes: surprising results from animal models. Endocrinology, Aug 2021. URL: https://doi.org/10.1210/endocr/bqab155, doi:10.1210/endocr/bqab155. This article has 50 citations and is from a domain leading peer-reviewed journal.

5. (harno2018pomcthephysiological pages 2-3): Erika Harno, Thanuja Gali Ramamoorthy, Anthony P. Coll, and Anne White. Pomc: the physiological power of hormone processing. Physiological reviews, 98 4:2381-2430, Oct 2018. URL: https://doi.org/10.1152/physrev.00024.2017, doi:10.1152/physrev.00024.2017. This article has 299 citations and is from a highest quality peer-reviewed journal.

6. (hook2009humanpituitarycontains pages 1-2): Vivian Hook, Lydiane Funkelstein, Thomas Toneff, Charles Mosier, and Shin-Rong Hwang. Human pituitary contains dual cathepsin l and prohormone convertase processing pathway components involved in converting pomc into the peptide hormones acth, α-msh, and β-endorphin. Endocrine, 35:429-437, Apr 2009. URL: https://doi.org/10.1007/s12020-009-9163-5, doi:10.1007/s12020-009-9163-5. This article has 39 citations and is from a peer-reviewed journal.

7. (hook2009humanpituitarycontains pages 4-5): Vivian Hook, Lydiane Funkelstein, Thomas Toneff, Charles Mosier, and Shin-Rong Hwang. Human pituitary contains dual cathepsin l and prohormone convertase processing pathway components involved in converting pomc into the peptide hormones acth, α-msh, and β-endorphin. Endocrine, 35:429-437, Apr 2009. URL: https://doi.org/10.1007/s12020-009-9163-5, doi:10.1007/s12020-009-9163-5. This article has 39 citations and is from a peer-reviewed journal.

8. (fridmanis2017acthreceptor(mc2r) pages 1-2): Davids Fridmanis, Ance Roga, and Janis Klovins. Acth receptor (mc2r) specificity: what do we know about underlying molecular mechanisms? Frontiers in Endocrinology, Feb 2017. URL: https://doi.org/10.3389/fendo.2017.00013, doi:10.3389/fendo.2017.00013. This article has 97 citations.

9. (smyth201660yearsof pages 2-4): Derek Smyth. 60 years of pomc: lipotropin and beta-endorphin: a perspective. Journal of molecular endocrinology, 56 4:T13-25, May 2016. URL: https://doi.org/10.1530/jme-16-0033, doi:10.1530/jme-16-0033. This article has 56 citations and is from a peer-reviewed journal.

10. (wu2023alphamelanocytestimulatinghormonemediatedappetite pages 1-2): Qiwen Wu, Jingmei Chen, Tingyu Hua, and Jinyan Cai. Alpha-melanocyte-stimulating hormone-mediated appetite regulation in the central nervous system. Neuroendocrinology, 113:885-904, Apr 2023. URL: https://doi.org/10.1159/000530804, doi:10.1159/000530804. This article has 49 citations and is from a peer-reviewed journal.

11. (weirath2024recommendedtoolcompounds pages 19-19): Nicholas A. Weirath and Carrie Haskell-Luevano. Recommended tool compounds for the melanocortin receptor (mcr) g protein-coupled receptors (gpcrs). ACS pharmacology & translational science, 7 9:2706-2724, Aug 2024. URL: https://doi.org/10.1021/acsptsci.4c00129, doi:10.1021/acsptsci.4c00129. This article has 5 citations and is from a peer-reviewed journal.

12. (yuan2022ligandsformelanocortin pages 3-4): Xiao-Chen Yuan and Ya-Xiong Tao. Ligands for melanocortin receptors: beyond melanocyte-stimulating hormones and adrenocorticotropin. Biomolecules, 12:1407, Oct 2022. URL: https://doi.org/10.3390/biom12101407, doi:10.3390/biom12101407. This article has 25 citations.

13. (harno2018pomcthephysiological pages 44-45): Erika Harno, Thanuja Gali Ramamoorthy, Anthony P. Coll, and Anne White. Pomc: the physiological power of hormone processing. Physiological reviews, 98 4:2381-2430, Oct 2018. URL: https://doi.org/10.1152/physrev.00024.2017, doi:10.1152/physrev.00024.2017. This article has 299 citations and is from a highest quality peer-reviewed journal.

14. (hook2009humanpituitarycontains media 305ec3c4): Vivian Hook, Lydiane Funkelstein, Thomas Toneff, Charles Mosier, and Shin-Rong Hwang. Human pituitary contains dual cathepsin l and prohormone convertase processing pathway components involved in converting pomc into the peptide hormones acth, α-msh, and β-endorphin. Endocrine, 35:429-437, Apr 2009. URL: https://doi.org/10.1007/s12020-009-9163-5, doi:10.1007/s12020-009-9163-5. This article has 39 citations and is from a peer-reviewed journal.

15. (hook2009humanpituitarycontains media e02b8ab2): Vivian Hook, Lydiane Funkelstein, Thomas Toneff, Charles Mosier, and Shin-Rong Hwang. Human pituitary contains dual cathepsin l and prohormone convertase processing pathway components involved in converting pomc into the peptide hormones acth, α-msh, and β-endorphin. Endocrine, 35:429-437, Apr 2009. URL: https://doi.org/10.1007/s12020-009-9163-5, doi:10.1007/s12020-009-9163-5. This article has 39 citations and is from a peer-reviewed journal.

16. (yuan2022ligandsformelanocortin pages 4-5): Xiao-Chen Yuan and Ya-Xiong Tao. Ligands for melanocortin receptors: beyond melanocyte-stimulating hormones and adrenocorticotropin. Biomolecules, 12:1407, Oct 2022. URL: https://doi.org/10.3390/biom12101407, doi:10.3390/biom12101407. This article has 25 citations.

## Citations

1. wu2023alphamelanocytestimulatinghormonemediatedappetite pages 1-2
2. weirath2024recommendedtoolcompounds pages 19-19
3. yuan2022ligandsformelanocortin pages 3-4
4. hook2009humanpituitarycontains pages 4-5
5. lindberg2021obesitypomcand pages 2-3
6. harno2018pomcthephysiological pages 1-2
7. harno2018pomcthephysiological pages 2-3
8. hook2009humanpituitarycontains pages 1-2
9. harno2018pomcthephysiological pages 44-45
10. yuan2022ligandsformelanocortin pages 4-5
11. https://doi.org/10.1007/s12020-009-9163-5
12. https://doi.org/10.3389/fendo.2017.00013
13. https://doi.org/10.1530/jme-16-0033
14. https://doi.org/10.1159/000530804
15. https://doi.org/10.1021/acsptsci.4c00129
16. https://doi.org/10.1530/jme-15-0323,
17. https://doi.org/10.1152/physrev.00024.2017,
18. https://doi.org/10.1210/endocr/bqab155,
19. https://doi.org/10.1007/s12020-009-9163-5,
20. https://doi.org/10.3389/fendo.2017.00013,
21. https://doi.org/10.1530/jme-16-0033,
22. https://doi.org/10.1159/000530804,
23. https://doi.org/10.1021/acsptsci.4c00129,
24. https://doi.org/10.3390/biom12101407,