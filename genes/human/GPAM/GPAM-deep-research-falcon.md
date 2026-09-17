---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T13:54:17.859117'
end_time: '2026-09-08T14:03:07.178643'
duration_seconds: 529.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GPAM
  gene_symbol: GPAM
  uniprot_accession: Q9HCL2
  protein_description: 'RecName: Full=Glycerol-3-phosphate acyltransferase 1, mitochondrial
    {ECO:0000305}; Short=GPAT-1; EC=2.3.1.15 {ECO:0000269|PubMed:18238778, ECO:0000269|PubMed:36522428};'
  gene_info: Name=GPAM {ECO:0000312|HGNC:HGNC:24865}; Synonyms=GPAT1 {ECO:0000303|PubMed:36522428},
    KIAA1560;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the GPAT/DAPAT family. .
  protein_domains: GPAT/DHAPAT. (IPR022284); GPAT/DHAPAT_C. (IPR045520); GPAT/DHAPAT_LPLAT.
    (IPR041728); GPAT_PlsB. (IPR028354); Plipid/glycerol_acylTrfase. (IPR002123)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 10
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: GPAM-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9HCL2
- **Protein Description:** RecName: Full=Glycerol-3-phosphate acyltransferase 1, mitochondrial {ECO:0000305}; Short=GPAT-1; EC=2.3.1.15 {ECO:0000269|PubMed:18238778, ECO:0000269|PubMed:36522428};
- **Gene Information:** Name=GPAM {ECO:0000312|HGNC:HGNC:24865}; Synonyms=GPAT1 {ECO:0000303|PubMed:36522428}, KIAA1560;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the GPAT/DAPAT family. .
- **Key Domains:** GPAT/DHAPAT. (IPR022284); GPAT/DHAPAT_C. (IPR045520); GPAT/DHAPAT_LPLAT. (IPR041728); GPAT_PlsB. (IPR028354); Plipid/glycerol_acylTrfase. (IPR002123)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GPAM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GPAM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GPAM** (gene ID: GPAM, UniProt: Q9HCL2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

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

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9HCL2
- **Protein Description:** RecName: Full=Glycerol-3-phosphate acyltransferase 1, mitochondrial {ECO:0000305}; Short=GPAT-1; EC=2.3.1.15 {ECO:0000269|PubMed:18238778, ECO:0000269|PubMed:36522428};
- **Gene Information:** Name=GPAM {ECO:0000312|HGNC:HGNC:24865}; Synonyms=GPAT1 {ECO:0000303|PubMed:36522428}, KIAA1560;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the GPAT/DAPAT family. .
- **Key Domains:** GPAT/DHAPAT. (IPR022284); GPAT/DHAPAT_C. (IPR045520); GPAT/DHAPAT_LPLAT. (IPR041728); GPAT_PlsB. (IPR028354); Plipid/glycerol_acylTrfase. (IPR002123)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GPAM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GPAM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GPAM** (gene ID: GPAM, UniProt: Q9HCL2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human **GPAM / GPAT1** Functional-Annotation Report

## Executive conclusion

The requested identity is coherent and unambiguous: **human GPAM** (HGNC:24865; UniProt **Q9HCL2**; synonyms **GPAT1**, *KIAA1560*) encodes **mitochondrial glycerol-3-phosphate acyltransferase 1**, EC **2.3.1.15**. It is an integral **outer mitochondrial membrane** enzyme of the GPAT/DHAPAT, PlsB-like glycerolipid acyltransferase family. Its primary function is to transfer a long-chain fatty acyl group—preferentially a saturated chain, especially palmitoyl—from acyl-CoA to the **sn-1 position of glycerol-3-phosphate**, generating lysophosphatidic acid (LPA). This is the first committed and commonly rate-limiting reaction of de novo glycerolipid synthesis. No evidence reviewed here concerned a different gene sharing the GPAM symbol. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24, yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7, zhang2024gpat1activityand pages 1-2)

| Feature | Validated annotation | Strongest evidence or qualification |
|---|---|---|
| Identity | **Human GPAM**; UniProt **Q9HCL2**; also called **GPAT1** or mitochondrial glycerol-3-phosphate acyltransferase 1 | The accession and organism derive from the specified UniProt record. Literature independently identifies GPAT1 as a mitochondrial GPAT distinct from GPAT2, GPAT3, and GPAT4. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24) |
| Catalytic reaction | **sn-Glycerol-3-phosphate + long-chain fatty acyl-CoA → 1-acyl-sn-glycerol-3-phosphate (LPA) + CoA**; **EC 2.3.1.15** | Acylation occurs at the sn-1 position and constitutes the first committed, commonly rate-limiting step of de novo glycerolipid synthesis. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7, zhang2024gpat1activityand pages 1-2) |
| Family and catalytic architecture | Member of the **GPAT/DHAPAT, PlsB-like glycerolipid acyltransferase family**, consistent with the supplied InterPro domains; the conserved **HXXXXD** motif participates in catalysis | The family and domains are human database annotations. Motif functions are mechanistic inferences supported by biochemical and comparative analyses of GPAT-family enzymes. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7) |
| Cellular location and topology | Integral **outer mitochondrial membrane** protein with **two transmembrane helices**, cytosolic N- and C-termini, an intermembrane-space loop, and a **cytosol-facing active site** | This topology gives the catalytic site access to cytosolic glycerol-3-phosphate and acyl-CoA. Detailed topology comes mainly from mammalian models rather than a high-resolution human GPAM structure. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24, daniel2015physiologicalconsequencesof pages 25-29) |
| Acyl-donor specificity | Accepts long-chain acyl-CoAs but favors **saturated substrates**, especially **palmitoyl-CoA (16:0-CoA)**; activity with 16:0-CoA is approximately **2–3-fold** higher than with 18:0- or 18:1-CoA | The preference is established mainly through mammalian and rodent enzyme assays and is consistent with enrichment of saturated downstream lipid species. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, daniel2015physiologicalconsequencesof pages 25-29) |
| Biochemical discriminator | GPAT1 activity is **resistant to N-ethylmaleimide (NEM)** | This distinguishes GPAT1 from mitochondrial **GPAT2** and ER-localized **GPAT3 and GPAT4**, which are NEM-sensitive. NEM-resistant GPAT activity is commonly used as an operational measure of GPAT1. (zhang2024gpat1activityand pages 1-2, zhang2024gpat1activityand pages 3-5) |
| Pathway role | GPAM-generated LPA is converted successively to **phosphatidic acid (PA)** and **diacylglycerol (DAG)**, then routed into **triacylglycerol (TAG)** or glycerophospholipid synthesis | GPAM influences glycerolipid flux and the fatty-acyl composition of downstream LPA, PA, DAG, TAG, and membrane phospholipids. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, heras2026targetingthemitochondrial pages 24-28) |
| Metabolic partitioning | In hepatocytes, GPAT1 channels newly synthesized fatty acids into TAG and **away from mitochondrial beta-oxidation** | Mouse Gpat1-null hepatocytes oxidized approximately **2-fold** more exogenous fatty acid; knockout liver contained **3-fold** more long-chain acylcarnitines after fasting and **3.5-fold** more after fasting and refeeding. These are rodent mechanistic data, not human effect estimates. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9) |
| Regulation | Lipogenic conditions induce GPAT1 through **SREBP1c** and **ChREBP**; insulin- and LXR-associated signaling promote expression or activity, whereas glucagon, cAMP, and **AMPK** oppose it | This model integrates promoter, nutritional, and rodent or cell evidence. Transcriptional regulation is better established than some proposed acute phosphorylation mechanisms. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35, zhang2024gpat1activityand pages 8-9) |
| 2024 mechanistic findings | In primary mouse hepatocytes, 25 mM glucose raised **GPAT1 mRNA 5.7-fold**, total GPAT activity **1.9-fold**, and NEM-resistant activity **1.8-fold**; GPAT1 overexpression raised NEM-resistant activity **4.0-fold** and di-16:0 PA approximately **4.4-fold**, or **5.3-fold** with 200 μM palmitate | High glucose reduced insulin suppression of glucose production from **58.1% to 31.3%**, while added palmitate abolished suppression. High glucose inhibited insulin-stimulated Akt Ser473 phosphorylation by **51%**, increasing to **98%** with palmitate. These cultured-mouse-hepatocyte results support a GPAT1–di-16:0-PA–mTORC2/Akt mechanism but are not human clinical evidence. (zhang2024gpat1activityand pages 6-8, zhang2024gpat1activityand pages 8-9, zhang2024gpat1activityand pages 5-6, zhang2024gpat1activityand pages 3-5) |


*Table: Core annotation of human GPAM/Q9HCL2 with supporting biochemical and mechanistic evidence. Human annotations are distinguished from findings in rodent and cultured-cell systems.*

## 1. Identity verification and isoform disambiguation

The literature’s biochemical description matches the supplied UniProt annotation: mitochondrial **GPAT1** is encoded by **GPAM**, acts as an acyl-CoA:glycerol-3-phosphate acyltransferase, resides in the mitochondrial outer membrane, favors palmitoyl-CoA, and is resistant to N-ethylmaleimide (NEM). These combined features distinguish it from every other mammalian GPAT isoform. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24, zhang2024gpat1activityand pages 1-2)

* **GPAT2** is also mitochondrial but is NEM-sensitive, lacks GPAT1’s strong palmitoyl-CoA preference, and is particularly associated with germ-cell lipid metabolism.
* **GPAT3 and GPAT4** are NEM-sensitive enzymes located principally in the endoplasmic reticulum rather than mitochondria.
* In the 2024 direct comparison, GPAT1 overexpression increased NEM-resistant activity and di-16:0 phosphatidic acid, whereas GPAT3 increased NEM-sensitive activity without reproducing the di-16:0-PA phenotype. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35, zhang2024gpat1activityand pages 1-2, zhang2024gpat1activityand pages 6-8, zhang2024gpat1activityand pages 5-6)

The supplied InterPro assignments—GPAT/DHAPAT, GPAT/DHAPAT_C, GPAT/DHAPAT_LPLAT, GPAT_PlsB, and phospholipid/glycerol acyltransferase—are therefore consistent with the established enzymology and evolutionary family. No contradictory family or organism assignment was found.

## 2. Primary molecular function

### Catalyzed reaction

**sn-Glycerol-3-phosphate + long-chain fatty acyl-CoA → 1-acyl-sn-glycerol-3-phosphate (LPA) + CoA**

GPAM acylates the glycerol backbone at **sn-1**. The product is therefore 1-acyl-LPA rather than phosphatidic acid or triacylglycerol itself. LPA is subsequently acylated by AGPAT enzymes to phosphatidic acid (PA), dephosphorylated by lipins/phosphatidate phosphatases to diacylglycerol (DAG), and either acylated by DGAT to triacylglycerol (TAG) or routed into glycerophospholipid synthesis. (heras2026targetingthemitochondrial pages 24-28, nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24, yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7, zhang2024gpat1activityand pages 1-2)

The reaction is considered the first committed—and often rate-limiting—step in de novo glycerolipid synthesis because it commits glycerol-3-phosphate and activated fatty acid to an LPA-centered biosynthetic pathway. Nevertheless, “rate-limiting” is physiological and context-dependent rather than an invariant property in every tissue. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, zhang2024gpat1activityand pages 1-2)

### Substrate specificity

GPAT1 uses multiple long-chain acyl-CoAs but favors **saturated acyl donors**, particularly **palmitoyl-CoA (16:0-CoA)**. Mammalian assays report approximately **two- to threefold greater activity with 16:0-CoA** than with stearoyl- or oleoyl-CoA. This preference helps explain the enrichment of saturated species such as di-16:0 PA downstream when GPAT1 activity and palmitate availability are high. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, daniel2015physiologicalconsequencesof pages 25-29, zhang2024gpat1activityand pages 6-8)

NEM resistance is a useful operational biochemical marker. In membrane preparations, 1 mM NEM inhibits GPAT2–4 but not GPAT1; consequently, activity remaining after NEM treatment is commonly interpreted as GPAT1 activity. The 2024 assay directly measured incorporation of radiolabeled glycerol-3-phosphate into 16:0-LPA using 82.5 μM palmitoyl-CoA. (zhang2024gpat1activityand pages 1-2, zhang2024gpat1activityand pages 3-5)

## 3. Structure, domains, and catalytic mechanism

GPAM belongs to the GPAT/DHAPAT class of membrane-associated glycerolipid acyltransferases. The conserved **HXXXXD** motif is central to catalysis: histidine is proposed to act as a general base, activating the glycerol-3-phosphate hydroxyl, while aspartate contributes to charge relay. Conserved motifs II and III are implicated in glycerol-3-phosphate recognition, and motif IV may contribute to acyl-CoA binding. These assignments derive mainly from comparative sequence analysis and family-wide mutagenesis rather than an atomic-resolution structure of full-length human Q9HCL2. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7)

Topology studies support **two transmembrane segments**, with both termini and the catalytic site exposed to the cytosol and the connecting loop facing the mitochondrial intermembrane space. This arrangement is chemically sensible because both glycerol-3-phosphate and long-chain acyl-CoA are supplied from the cytosolic side. The resulting LPA must subsequently reach downstream enzymes, many of which reside in the ER; liver fatty-acid-binding protein can mediate mitochondrial-to-ER LPA transfer in vitro, although the complete trafficking mechanism in intact human cells remains incompletely resolved. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24, daniel2015physiologicalconsequencesof pages 25-29)

## 4. Cellular localization and biochemical compartmentation

The functional site is the **cytosolic face of the mitochondrial outer membrane**, not the matrix or inner membrane. GPAT1 and mitochondrial CPT1 therefore occupy a strategically important interface where long-chain acyl-CoAs can be partitioned between esterification and mitochondrial β-oxidation. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24, nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35)

GPAT1 is especially important in lipogenic tissues. Older mammalian estimates attribute approximately **40–50% of total hepatic GPAT activity** to GPAT1, compared with roughly **10–20% in most other tissues**. Expression and activity are high in liver and adipose tissue, with additional expression in muscle, kidney, brain, and epidermal cells. These percentages are biochemical estimates from mammalian tissues rather than modern quantitative human proteomic fractions. (daniel2015physiologicalconsequencesof pages 25-29, nagle2007glycerol3phosphateacyltransferaseisoforms pages 24-25)

## 5. Pathway role and metabolic consequences

### Glycerolipid synthesis

GPAM supplies LPA for synthesis of PA, DAG, TAG, and membrane glycerophospholipids. Because GPAT1 favors palmitoyl-CoA, it influences not only pathway flux but also downstream lipid molecular species. In GPAT1-overexpressing CHO cells, DAG and TAG labeling rose approximately twofold, TAG mass rose **two- to threefold**, and phospholipid labeling fell by about **30%**, illustrating that increased GPAT1 can redistribute glycerolipid intermediates toward storage lipid under suitable substrate conditions. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 24-25)

### Competition with fatty-acid oxidation

GPAT1 channels newly synthesized fatty acids—particularly de novo synthesized palmitate—toward esterification and away from oxidation. In mouse Gpat1-null hepatocytes, oxidation of exogenous fatty acid was approximately **twofold higher**; long-chain hepatic acylcarnitines were approximately **threefold higher after fasting** and **3.5-fold higher after fasting/high-sucrose refeeding**. These experiments demonstrate metabolic partitioning, although they should not be interpreted as human effect sizes. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9)

AMPK reinforces the opposite metabolic state: it inhibits GPAT1 while lowering malonyl-CoA through ACC inhibition, relieving CPT1 restraint and favoring β-oxidation. Thus, GPAM is best understood as a mitochondrial-surface branch-point enzyme coupling nutritional state to the choice between lipid storage/membrane synthesis and fatty-acid catabolism. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35)

### Lipid signaling

GPAT1-generated products are not merely biosynthetic intermediates. LPA, PA, and DAG can participate in signaling. Evidence also associates GPAT1-dependent LPA with mitochondrial fusion, although this remains less comprehensively defined than its glycerolipid-synthetic function. Overexpressing GPAT1 in CHO cells increased LPA, PPARγ activity, and expression of the PPARγ target CD36. These results indicate potential intracellular signaling functions but do not establish a universal GPAM–PPARγ pathway in human tissues. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, heras2026targetingthemitochondrial pages 24-28)

## 6. Physiological regulation

GPAM is strongly nutritionally regulated:

* **Insulin/SREBP-1c and LXR** promote its expression in lipogenic states.
* **Glucose-responsive ChREBP** cooperates with SREBP-1c under carbohydrate abundance.
* **Glucagon/cAMP, fasting, exercise, and AMPK** oppose GPAT1 expression or activity.
* Fasting lowered liver/adipose GPAT1 protein or activity by approximately **30–50%**, whereas high-sucrose refeeding raised it **30–60% above the fed-state level** in rodent experiments. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, daniel2015physiologicalconsequencesof pages 25-29, nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35)

Acute regulation by phosphorylation has been proposed. Insulin may increase activity, AMPK may inhibit it, and CK2 treatment of isolated rat mitochondria increased activity approximately twofold. The transcriptional response to carbohydrate is better established than the physiological importance and exact sites of every proposed phosphorylation event. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35)

## 7. Recent research: 2024 mechanistic advance

Zhang and colleagues, published online **13 February 2024** in *The Journal of Nutrition*, tested GPAT1 directly in primary hepatocytes from male C57BL/6J mice. Cells were exposed to 5.5 or 25 mM glucose, adenovirally overexpressed GPAT1 or GPAT3, and in some conditions received 200 μM palmitate or linoleate. This is a mechanistically precise study, but it is an ex vivo mouse experiment—not a human clinical study. DOI/URL: https://doi.org/10.1016/j.tjnut.2024.02.004. (zhang2024gpat1activityand pages 1-2, zhang2024gpat1activityand pages 2-3, zhang2024gpat1activityand pages 3-5)

Key quantitative observations were:

* High glucose increased **SREBP1c, ChREBP, and GPAT1 mRNA approximately 2-, 5-, and 5.7-fold**, respectively.
* High glucose increased total and NEM-resistant GPAT activity **1.9- and 1.8-fold**; approximately **60%** of the total activity increase was attributable to GPAT1.
* GPAT1 overexpression raised total and NEM-resistant GPAT activity **4.1- and 4.0-fold**, respectively.
* GPAT1 overexpression increased di-16:0 PA approximately **4.4-fold**, or **5.3-fold with palmitate**; GPAT3 did not reproduce this effect.
* Insulin suppressed glucose production by **58.1% at 5.5 mM glucose** but only **31.3% at 25 mM glucose**; high glucose plus palmitate abolished suppression.
* High glucose inhibited insulin-stimulated Akt Ser473 phosphorylation by **51%**, rising to **98% inhibition with palmitate**. Most comparisons were supported by three independent experiments; PA measurements used six independent experiments in duplicate, with Bonferroni-adjusted *P*<0.05. (zhang2024gpat1activityand pages 6-8, zhang2024gpat1activityand pages 8-9, zhang2024gpat1activityand pages 5-6, zhang2024gpat1activityand pages 3-5)

The authors’ mechanistic interpretation is that carbohydrate-responsive induction of GPAT1, together with abundant palmitate, increases di-16:0 PA. This lipid species disrupts mTOR–rictor/mTORC2 assembly, reduces Akt activation, and weakens insulin suppression of hepatic glucose production. This is strong pathway-level evidence but remains a model requiring confirmation in human liver in vivo. (zhang2024gpat1activityand pages 2-3, zhang2024gpat1activityand pages 8-9)

## 8. Human disease relevance and applications

### MASLD, dyslipidemia, and insulin resistance

GPAM is biologically plausible in metabolic dysfunction-associated steatotic liver disease because it promotes hepatic glycerolipid synthesis and determines whether newly synthesized saturated fatty acids enter TAG or oxidation. Human genetics and recent functional-genomic studies have nominated **GPAM as a regulator of hepatocyte lipid accumulation**, but the evidence retrieved here did not provide sufficiently detailed human effect estimates to report responsibly. The strongest causal mechanistic evidence remains cellular and rodent work.

Importantly, TAG storage and insulin resistance are not identical phenotypes. GPAT1 deficiency can reduce hepatic steatosis without necessarily restoring insulin sensitivity in every mouse model, and different GPAT isoforms generate spatially distinct lipid pools. Expert interpretation therefore emphasizes **compartmentalized LPA/PA/DAG signaling**, rather than assuming total hepatic TAG alone drives insulin resistance. (daniel2015physiologicalconsequencesof pages 25-29, nagle2007glycerol3phosphateacyltransferaseisoforms pages 24-25, nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35)

### Therapeutic and research applications

GPAM is being investigated as a metabolic target for reducing hepatic lipid synthesis, saturated PA signaling, and possibly tumor-associated lipid metabolism. Current practical implementations are preclinical: genetic knockdown/knockout, adenoviral manipulation, NEM-resistant activity assays, lipidomics, and experimental GPAT inhibitors. No approved GPAM-selective medicine, validated companion diagnostic, or established GPAM-directed clinical treatment was identified in the reviewed evidence. Broad GPAT inhibition also presents a selectivity problem because GPAT1–4 occupy different organelles and produce functionally distinct lipid pools.

A rational translational strategy would require GPAT1-selective compounds, confirmation of target engagement through NEM-resistant activity or isotope tracing, and lipidomic monitoring of LPA/PA species—especially di-16:0 PA—rather than relying solely on total TAG. Potential liabilities include altered membrane-phospholipid composition, excessive fatty-acid oxidation, mitochondrial effects, and tissue-specific responses.

## 9. Evidence assessment and unresolved questions

**High-confidence annotation:** identity as human mitochondrial GPAT1; EC 2.3.1.15 reaction; outer-mitochondrial-membrane localization; NEM resistance; preference for saturated acyl-CoA/palmitoyl-CoA; role in initiating LPA-dependent glycerolipid synthesis. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24, yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7, zhang2024gpat1activityand pages 1-2)

**Strong mechanistic but largely nonhuman evidence:** metabolic competition with β-oxidation; carbohydrate/SREBP1c/ChREBP regulation; saturated PA–mTORC2–Akt signaling; effects on hepatic glucose production. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35, zhang2024gpat1activityand pages 6-8, zhang2024gpat1activityand pages 8-9, zhang2024gpat1activityand pages 5-6)

**Still incomplete:** an experimentally resolved full-length human GPAM structure; exact human tissue-specific flux contribution; mechanisms transferring mitochondrial LPA to ER pathways; consequences of common human GPAM variants; and clinical safety or efficacy of selective GPAM inhibition.

## Key sources

1. Zhang C. et al. **“GPAT1 Activity and Abundant Palmitic Acid Impair Insulin Suppression of Hepatic Glucose Production in Primary Mouse Hepatocytes.”** *The Journal of Nutrition* 154, 1109–1118. Published online **13 February 2024**. https://doi.org/10.1016/j.tjnut.2024.02.004. (zhang2024gpat1activityand pages 1-2, zhang2024gpat1activityand pages 6-8, zhang2024gpat1activityand pages 8-9)
2. Yamashita A. et al. **“Glycerophosphate/Acylglycerophosphate Acyltransferases.”** *Biology* 3, 801–830. Published **November 2014**. https://doi.org/10.3390/biology3040801. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9, yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7)
3. Gonzalez-Baró M.R., Lewin T.M., Coleman R.A. **“Function of mitochondrial GPAT1 in the regulation of triacylglycerol biosynthesis and insulin action.”** *American Journal of Physiology—Gastrointestinal and Liver Physiology* 292, G1195–G1199. Published **May 2007**. https://doi.org/10.1152/ajpgi.00553.2006. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9)
4. Wendel A.A. et al. **“GPAT1, but Not GPAT4, Incorporates Newly Synthesized Fatty Acids into Triacylglycerol and Diminishes Fatty Acid Oxidation.”** *Journal of Biological Chemistry* 288, 27299–27306. Published **September 2013**. https://doi.org/10.1074/jbc.M113.485219. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9)

Overall, the most defensible functional annotation is that **GPAM/GPAT1 is a cytosol-facing mitochondrial outer-membrane gatekeeper that preferentially commits newly synthesized saturated fatty acyl-CoA—especially palmitoyl-CoA—to LPA and downstream glycerolipid synthesis, thereby influencing both lipid storage and lipid-mediated signaling at the interface with fatty-acid oxidation**.

References

1. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9): Atsushi Yamashita, Yasuhiro Hayashi, Naoki Matsumoto, Yoko Nemoto-Sasaki, Saori Oka, Takashi Tanikawa, and Takayuki Sugiura. Glycerophosphate/acylglycerophosphate acyltransferases. Biology, 3:801-830, Nov 2014. URL: https://doi.org/10.3390/biology3040801, doi:10.3390/biology3040801. This article has 191 citations.

2. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 21-24): CA Nagle. Glycerol-3-phosphate acyltransferase isoforms: hepatic triacylglycerol synthesis and the development of insulin resistance. Unknown journal, 2007.

3. (yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7): Atsushi Yamashita, Yasuhiro Hayashi, Naoki Matsumoto, Yoko Nemoto-Sasaki, Saori Oka, Takashi Tanikawa, and Takayuki Sugiura. Glycerophosphate/acylglycerophosphate acyltransferases. Biology, 3:801-830, Nov 2014. URL: https://doi.org/10.3390/biology3040801, doi:10.3390/biology3040801. This article has 191 citations.

4. (zhang2024gpat1activityand pages 1-2): Chongben Zhang, Mathew Steadman, Hudson P Santos, Saame R Shaikh, and Rose Mary Xavier. Gpat1 activity and abundant palmitic acid impair insulin suppression of hepatic glucose production in primary mouse hepatocytes. Apr 2024. URL: https://doi.org/10.1016/j.tjnut.2024.02.004, doi:10.1016/j.tjnut.2024.02.004. This article has 5 citations.

5. (daniel2015physiologicalconsequencesof pages 25-29): Physiological Consequences of Compartmentalized Glycerolipid Synthesis This article has 0 citations and is from a peer-reviewed journal.

6. (zhang2024gpat1activityand pages 3-5): Chongben Zhang, Mathew Steadman, Hudson P Santos, Saame R Shaikh, and Rose Mary Xavier. Gpat1 activity and abundant palmitic acid impair insulin suppression of hepatic glucose production in primary mouse hepatocytes. Apr 2024. URL: https://doi.org/10.1016/j.tjnut.2024.02.004, doi:10.1016/j.tjnut.2024.02.004. This article has 5 citations.

7. (heras2026targetingthemitochondrial pages 24-28): M Alvarez de las Heras. Targeting the mitochondrial lysophosphatidic acid-producing enzyme glycerol-3-phosphate acyltransferase 1 in ovarian cancer using a stable knockdown …. Unknown journal, 2026.

8. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 30-35): CA Nagle. Glycerol-3-phosphate acyltransferase isoforms: hepatic triacylglycerol synthesis and the development of insulin resistance. Unknown journal, 2007.

9. (zhang2024gpat1activityand pages 8-9): Chongben Zhang, Mathew Steadman, Hudson P Santos, Saame R Shaikh, and Rose Mary Xavier. Gpat1 activity and abundant palmitic acid impair insulin suppression of hepatic glucose production in primary mouse hepatocytes. Apr 2024. URL: https://doi.org/10.1016/j.tjnut.2024.02.004, doi:10.1016/j.tjnut.2024.02.004. This article has 5 citations.

10. (zhang2024gpat1activityand pages 6-8): Chongben Zhang, Mathew Steadman, Hudson P Santos, Saame R Shaikh, and Rose Mary Xavier. Gpat1 activity and abundant palmitic acid impair insulin suppression of hepatic glucose production in primary mouse hepatocytes. Apr 2024. URL: https://doi.org/10.1016/j.tjnut.2024.02.004, doi:10.1016/j.tjnut.2024.02.004. This article has 5 citations.

11. (zhang2024gpat1activityand pages 5-6): Chongben Zhang, Mathew Steadman, Hudson P Santos, Saame R Shaikh, and Rose Mary Xavier. Gpat1 activity and abundant palmitic acid impair insulin suppression of hepatic glucose production in primary mouse hepatocytes. Apr 2024. URL: https://doi.org/10.1016/j.tjnut.2024.02.004, doi:10.1016/j.tjnut.2024.02.004. This article has 5 citations.

12. (nagle2007glycerol3phosphateacyltransferaseisoforms pages 24-25): CA Nagle. Glycerol-3-phosphate acyltransferase isoforms: hepatic triacylglycerol synthesis and the development of insulin resistance. Unknown journal, 2007.

13. (zhang2024gpat1activityand pages 2-3): Chongben Zhang, Mathew Steadman, Hudson P Santos, Saame R Shaikh, and Rose Mary Xavier. Gpat1 activity and abundant palmitic acid impair insulin suppression of hepatic glucose production in primary mouse hepatocytes. Apr 2024. URL: https://doi.org/10.1016/j.tjnut.2024.02.004, doi:10.1016/j.tjnut.2024.02.004. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](GPAM-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 4-7
2. yamashita2014glycerophosphateacylglycerophosphateacyltransferases pages 7-9
3. daniel2015physiologicalconsequencesof pages 25-29
4. heras2026targetingthemitochondrial pages 24-28
5. https://doi.org/10.1016/j.tjnut.2024.02.004.
6. https://doi.org/10.3390/biology3040801.
7. https://doi.org/10.1152/ajpgi.00553.2006.
8. https://doi.org/10.1074/jbc.M113.485219.
9. https://doi.org/10.3390/biology3040801,
10. https://doi.org/10.1016/j.tjnut.2024.02.004,