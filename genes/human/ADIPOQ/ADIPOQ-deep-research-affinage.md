---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADIPOQ
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q15848
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 19
citation_count: 19
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADIPOQ (human)

## Current model (mechanistic narrative)

ADIPOQ encodes adiponectin (GBP28/apM1/Acrp30), an adipocyte-secreted, collagen-domain protein that acts as a systemic regulator of glucose and lipid metabolism, insulin sensitivity, and organismal healthspan [PMID:8947845, PMID:33904399]. Originally purified from plasma as a gelatin-binding protein with a signal sequence, collagen-like repeats, and a globular C-terminal domain, it assembles into trimers, hexamers, and high-molecular-weight (HMW) oligomers, with interchain disulfide bonds through Cys-39/Cys-22 required for higher-order assembly [PMID:8947845, PMID:12496257, PMID:14522956]. Oligomerization state dictates signaling output: trimers preferentially activate AMPK (Thr172 phosphorylation) in muscle, while hexameric and HMW forms drive NF-κB signaling via IκB-α degradation, and only hexamer/HMW species bind the receptor T-cadherin in a manner dependent on eukaryotic post-translational modification [PMID:12496257, PMID:12087086, PMID:14522956, PMID:15210937]. Its principal metabolic action is suppression of hepatic glucose output — in vivo it reduces endogenous glucose production and downregulates the gluconeogenic enzymes PEPCK and G6Pase, sensitizing the liver to insulin [PMID:11479628, PMID:11748271]. In muscle, adiponectin signaling supports IRS-1-associated PI3-kinase activity, FATP-1 expression, free fatty acid clearance, and AMPK/SIRT1/PGC-1α-driven mitochondrial biogenesis, as established by adiponectin and muscle-specific AdipoR1 knockouts [PMID:12068289, PMID:22492282]. Intracellular signal transmission depends on the adaptor APPL1, which binds the AdipoR1 cytoplasmic domain, is recruited upon adiponectin stimulation, and links receptor engagement to lipid oxidation, glucose uptake, GLUT4 translocation (via Rab5), and cross-talk with insulin signaling [PMID:16622416]. Adiponectin expression is regulated transcriptionally — suppressed by TNF-α and induced through a GPRC6A→cAMP/PKA→ERK/CREB→PPARγ axis by uncarboxylated osteocalcin — and its actions extend to context-dependent modulation of macrophage inflammation and lifespan extension [PMID:11246823, PMID:25562427, PMID:25392268, PMID:33904399].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0048018 receptor ligand activity, GO:0098772 molecular function regulator activity, GO:0005198 structural molecule activity
- **localization:** GO:0005576 extracellular region, GO:0031012 extracellular matrix
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1430728 Metabolism, R-HSA-168256 Immune System
- **partners:** CDH13, APPL1, ADIPOR1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1996 | High | ADIPOQ (GBP28/apM1) was isolated from human plasma as a gelatin-binding protein. Structural analysis revealed it is encoded by the adipose-specific apM1 cDNA and contains a secretory signal sequence, collagen-like repeats, and a globular C-terminal domain, enabling homo-trimer formation and higher-order oligomeric complexes via its collagen-like domain. | PMID:8947845 | Journal of biochemistry |
| 2001 | High | A single injection of recombinant Acrp30 in mice transiently lowered basal glucose levels and abolished hyperglycemia in ob/ob, NOD, and streptozotocin-treated mice independent of changes in insulin levels. In isolated hepatocytes, Acrp30 enhanced the ability of sub-physiological insulin to suppress glucose production, identifying the liver as a primary target organ. | PMID:11479628 | Nature medicine |
| 2001 | High | Acrp30 infusion during a pancreatic euglycemic clamp in conscious mice caused a ~65% reduction in endogenous glucose production and reduced hepatic gluconeogenic enzyme mRNAs (PEPCK and G6Pase) by >50%, without affecting peripheral glucose uptake, glycolysis, or glycogen synthesis, establishing hepatic gluconeogenesis suppression as the primary mechanism of Acrp30-mediated glucose lowering. | PMID:11748271 | The Journal of clinical investigation |
| 2002 | High | Adiponectin/ACRP30 knockout mice showed delayed clearance of plasma free fatty acids, reduced FATP-1 mRNA in muscle, elevated adipose TNF-alpha mRNA and plasma TNF-alpha, and severe diet-induced insulin resistance with reduced IRS-1-associated PI3-kinase activity in muscle. Viral re-expression of adiponectin reversed these defects, placing adiponectin upstream of FATP-1 expression and IRS-1-mediated insulin signaling in muscle. | PMID:12068289 | Nature medicine |
| 2002 | High | Acrp30 circulates as trimeric and high-molecular-weight (HMW) oligomeric complexes whose distribution shows sexual dimorphism (females have more HMW). Disulfide bonds via Cys-39 are required for HMW complex formation. Mutation of Cys-39 (C39S) produces trimers that are more bioactive than HMW forms in reducing serum glucose and suppressing hepatic glucose output in primary hepatocytes, demonstrating that oligomerization state regulates bioactivity. | PMID:12496257 | The Journal of biological chemistry |
| 2002 | High | Hexameric and higher molecular weight (HMW) isoforms of Acrp30 activate NF-κB in C2C12 myocytes via phosphorylation and degradation of IκB-alpha, whereas trimeric Acrp30 and globular domain (gAcrp30) do not, establishing oligomerization-state-dependent NF-κB signaling. | PMID:12087086 | The Journal of biological chemistry |
| 2003 | High | Trimeric Acrp30 (but not hexameric or HMW forms) activates AMP-activated protein kinase alpha (phosphorylation at Thr172) in isolated rat muscle. Conversely, HMW and hexameric Acrp30 activate NF-κB but trimers do not. Cys-22 disulfide bonds are required for hexamer/HMW formation but not trimer stability, establishing that different oligomeric forms activate distinct signaling pathways. | PMID:14522956 | The Journal of biological chemistry |
| 2004 | High | T-cadherin was identified as a binding receptor for hexameric and HMW species of adiponectin, but not for trimeric or globular species. Binding requires eukaryotic post-translational modifications on adiponectin and the N-terminal cysteine required for hexamer/HMW formation; a C-terminal cysteine mutant that cannot form hexamers/HMW failed to bind T-cadherin in co-immunoprecipitation. | PMID:15210937 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | High | APPL1 (adaptor protein with PTB, PH and leucine zipper domains) was identified as a direct binding partner of AdipoR1 intracellular domain by yeast two-hybrid. APPL1 interaction with adiponectin receptors in mammalian cells is stimulated by adiponectin. APPL1 overexpression increases, and APPL1 knockdown reduces, adiponectin-stimulated lipid oxidation, glucose uptake, and GLUT4 membrane translocation. Adiponectin also stimulates APPL1–Rab5 interaction, promoting GLUT4 translocation. APPL1 mediates cross-talk between adiponectin and insulin signaling pathways. | PMID:16622416 | Nature cell biology |
| 1999 | Medium | The GBP28/ADIPOQ gene was mapped to human chromosome 3q27 by FISH and found to span 16 kb with 3 exons and 2 introns. The gene lacks a TATA box and its exon-intron organization resembles the leptin gene, providing structural basis for understanding its transcriptional regulation. | PMID:10095105 | Gene |
| 2001 | Medium | GBP28/adiponectin expression is normally absent in mouse liver, but after CCl4-induced hepatic injury, circulating GBP28 binds to hepatocyte extracellular matrix early (3–6 h), and GBP28 mRNA is subsequently markedly induced in damaged hepatocytes. IL-6 treatment of human HepG2 hepatoma cells also induced GBP28 expression, identifying liver as a secondary production site regulated by injury and inflammatory signals. | PMID:11444852 | Biochemical and biophysical research communications |
| 2001 | Medium | Mouse Acrp30 gene was mapped to the telomere of chromosome 16 (syntenic to human 3q27), and alternative polyadenylation produces two distinct mRNA species. Acrp30 expression is induced only at late stages of mouse embryonic development. The promoter was shown to drive strong adipocyte-specific expression in tissue culture cells. | PMID:11162643 | Biochemical and biophysical research communications |
| 2010 | High | AdipoR1 forms endogenous homodimers in multiple cell lines and human muscle tissue. A GxxxG motif in the fifth transmembrane domain is required for dimerization; mutation of both glycines (to Phe or Glu) disrupts dimerization. Adiponectin decreases AdipoR1 dimerization in a concentration-dependent manner, with this effect primarily mediated by the collagen-like domain of full-length adiponectin. | PMID:20332107 | Journal of cell science |
| 2000 | Medium | TNF-alpha reduces apM1 expression and secretion in differentiating primary human preadipocytes, while dibutyryl-cAMP also reduces expression. Ionomycin increases secretion of apM1. These findings establish transcriptional/secretory regulatory mechanisms for ADIPOQ in human adipocytes. | PMID:11246823 | Hormone and metabolic research |
| 2015 | Medium | Uncarboxylated osteocalcin (GluOC) induces adiponectin expression in adipocytes via GPRC6A receptor activation → cAMP accumulation → PKA activation → Src → Rap1 → ERK → CREB phosphorylation → PPARγ upregulation → adiponectin expression. ERK inhibition (U0126) blocked CREB phosphorylation. In vivo, oral GluOC in mice increased PPARγ and adiponectin expression in gonadal white adipocytes. | PMID:25562427 | Cellular signalling |
| 2012 | Medium | Adiponectin/AdipoR1 signaling in muscle regulates mitochondrial biogenesis via AMPK- and SIRT1-mediated PGC-1α activation and Ca2+-dependent upregulation of PGC-1α expression. Muscle-specific AdipoR1 knockout mice had impaired mitochondrial biogenesis and insulin resistance, revealing this as the mechanistic basis for adiponectin's insulin-sensitizing effect in muscle. | PMID:22492282 | Cold Spring Harbor symposia on quantitative biology |
| 2014 | Medium | Macrophage polarization state controls AdipoR1/R2 expression and adiponectin signaling outcome: classical M1 activation suppresses AdipoR expression (40–60% reduction) and causes adiponectin to induce pro-inflammatory cytokines (TNF-α, IL-6, IL-12 >10-fold), whereas M2 activation preserves AdipoR expression and adiponectin induces anti-inflammatory IL-10. Adiponectin upregulates AdipoR mRNA and protein in macrophages via LXRα. | PMID:25392268 | FASEB journal |
| 2012 | Medium | Acrp30 inhibits leptin-induced invasion of SPEC-2 endometrial cancer cells by activating AMPK and thereby reducing STAT3 phosphorylation and nuclear translocation, with downstream reduction of MMP-2 and MMP-9. JAK/STAT3 inhibitor and AMPK inhibitor experiments confirmed the pathway: Acrp30 acts via AMPK to suppress the JAK/STAT3 axis activated by leptin. | PMID:22327423 | Oncology reports |
| 2021 | High | Adiponectin null mice display exacerbated age-related glucose and lipid metabolism disorders and shortened lifespan on both chow and high-fat diet. Transgenic mice with elevated circulating adiponectin have improved systemic insulin sensitivity, reduced age-related tissue inflammation and fibrosis, and prolonged healthspan and median lifespan, establishing adiponectin as a direct regulator of aging and longevity. | PMID:33904399 | eLife |

## Citations

- PMID:10095105
- PMID:11162643
- PMID:11246823
- PMID:11444852
- PMID:11479628
- PMID:11748271
- PMID:12068289
- PMID:12087086
- PMID:12496257
- PMID:14522956
- PMID:15210937
- PMID:16622416
- PMID:20332107
- PMID:22327423
- PMID:22492282
- PMID:25392268
- PMID:25562427
- PMID:33904399
- PMID:8947845
