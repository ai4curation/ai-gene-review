---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/HYAL2
affinage_run_date: 2026-06-10T01:55:22
uniprot_accession: Q12891
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 21
citation_count: 21
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for HYAL2 (human)

## Current model (mechanistic narrative)

HYAL2 is a GPI-anchored, lipid raft-associated cell-surface hyaluronidase that initiates extracellular catabolism of high-molecular-weight hyaluronan (HA), cleaving it preferentially at acidic pH to ~20 kDa intermediates rather than to smaller fragments [PMID:9712871, PMID:21740893, PMID:26515055]. Unlike the lysosomal isoenzyme HYAL1, cell-associated HYAL2 displays only weak intrinsic hyaluronidase activity and depends on local acidification — for example through Na+/H+ exchanger-1 — for efficient pericellular HA degradation [PMID:11296287, PMID:19783662]. By trimming the HA-rich glycocalyx, HYAL2 controls CD44 retention and its coupling to ezrin-radixin-moesin proteins, thereby regulating cell motility and cytoskeletal organization [PMID:19783662, PMID:38490466]. The size-defined HA fragments it generates are themselves signaling molecules: low-molecular-weight HA acts through CD44 to modulate AKT/PI3K signaling, driving outcomes ranging from odontoblastic differentiation to cellular senescence, inflammation, and tumor-cell migration [PMID:38490466, PMID:41806573]. In vivo, HYAL2 is essential for plasma HA clearance, craniovertebral skeletal development, and erythrocyte/platelet homeostasis, and biallelic loss-of-function mutations that destabilize the protein and abolish its cell-surface localization cause syndromic orofacial clefting with cor triatriatum sinister in humans [PMID:18772348, PMID:28081210, PMID:34906488]. HYAL2 also serves as the high-affinity cell-surface entry receptor for jaagsiekte sheep retrovirus, binding the viral Env surface protein with picomolar affinity through a surface patch distinct from its catalytic site [PMID:11296287, PMID:12584308, PMID:15596803, PMID:16191204]. Independently, cell-surface HYAL2 binds TGF-β1 and recruits the proapoptotic adaptor WWOX/WOX1, forming a complex that translocates to the nucleus and amplifies Smad-driven transcription [PMID:19366691].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140098 catalytic activity, acting on RNA, GO:0016787 hydrolase activity, GO:0001618 virus receptor activity, GO:0060089 molecular transducer activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005886 plasma membrane, GO:0005576 extracellular region, GO:0005764 lysosome, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-1643685 Disease, R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** WWOX, CD44, TGFB1, NCF1, JSRV ENV (SU)
- **complexes:** HYAL2-WWOX/WOX1 complex, HYAL2-CD44-ERM complex, HYAL2-p47phox complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | High | HYAL2 encodes a lysosomal hyaluronidase with acidic pH optimum that cleaves high molecular mass hyaluronan (from umbilical cord, rooster comb, Streptococcus) only down to ~20 kDa intermediates, not smaller fragments; smaller (~20 kDa) hyaluronan from vitreous humor is resistant to HYAL2 cleavage, implying structural domains in hyaluronan. | PMID:9712871 | The Journal of biological chemistry |
| 2001 | High | HYAL2 is a glycosylphosphatidylinositol (GPI)-anchored cell-surface protein, not primarily a lysosomal enzyme; cells expressing HYAL2 did not exhibit detectable hyaluronidase activity, whereas cells expressing HYAL1 did. HYAL2 functions as the cell-surface receptor for jaagsiekte sheep retrovirus (JSRV), identified by phenotypic screening of radiation hybrid cell lines. | PMID:11296287 | Proceedings of the National Academy of Sciences of the United States of America |
| 2002 | Medium | Xenopus Hyal2 (Xhyal2) exists both as a GPI-anchored cell-surface protein and as a soluble extracellular protein; it degrades hyaluronan at acidic pH and more slowly at physiological pH. Ectopic overexpression of Xhyal2 in frog embryos causes loss of pericellular hyaluronan and severe defects in vitelline vessel plexus assembly from prevascular endothelial cells. | PMID:11804776 | Mechanisms of development |
| 2002 | Medium | Hyal-2 overexpression in L929 fibroblasts increases sensitivity to TNF cytotoxicity (~60–110% increase) and upregulates constitutive WOX1 (WWOX) expression; Hyal-2 translocates from lysosomes to mitochondria during staurosporine-induced apoptosis. TGF-β1 inhibits Hyal-2-mediated TNF cytotoxicity by 30–50%. | PMID:11960552 | BMC cell biology |
| 2003 | High | Human Hyal2 directly binds the surface (SU) region of JSRV Env protein, as demonstrated by direct binding assays; Hyal2 orthologs that mediate virus entry suppress transformation by JSRV/ENTV Env proteins. Human Hyal2 expressed in mouse cells suppresses Env-mediated transformation by increasing Env protein degradation, not by a general Env-independent tumor suppressor mechanism. | PMID:12584308 | Journal of virology |
| 2005 | High | Soluble human Hyal2 (sHyal2) purified from baculoviral expression is a 54-kDa monomer with weak hyaluronidase activity active over a broad pH range (not only acidic), capable of further degrading 20 kDa hyaluronan fragments. sHyal2 binds JSRV envelope glycoprotein with a remarkably tight KD of 32 ± 1 pM as measured by surface plasmon resonance, and inhibits viral transduction at 28 nM with >90% efficiency. | PMID:15596803 | Journal of virology |
| 2005 | Medium | Amino acid differences in the central third of Hyal2 account for the ~1000-fold difference in JSRV receptor activity between human and mouse Hyal2; the critical residues map to a small surface patch near but not overlapping the enzyme active site (based on bee venom hyaluronidase structural homology), suggesting this region is the Env binding site. | PMID:16191204 | Retrovirology |
| 2008 | High | HYAL2-deficient mice are viable and fertile but display craniovertebral bone formation defects, mild thrombocytopenia, chronic hemolysis, and 10-fold elevated plasma HA levels, demonstrating that HYAL2 has physiological hyaluronidase activity in vivo relevant for skeletal development, plasma HA clearance, and erythrocyte/platelet homeostasis. Liver sinusoidal cells accumulate undigested HA in Hyal2−/− mice. | PMID:18772348 | FASEB journal |
| 2009 | High | TGF-β1 binds cell-surface Hyal-2 on microvilli in TGF-β receptor II-deficient cells; this binding recruits proapoptotic WOX1/WWOX, with TGF-β1 strengthening the interaction between the catalytic domain of Hyal-2 and the N-terminal Tyr-33-phosphorylated WW domain of WOX1. The Hyal-2/WOX1 complex translocates to the nucleus and dramatically enhances Smad-driven promoter activity (8–9-fold), leading to cell death. | PMID:19366691 | The Journal of biological chemistry |
| 2009 | High | Hyal2 co-immunoprecipitates with CD44 and ezrin-radixin-moesin (ERM) proteins. Hyal2 overexpression in rat fibroblasts causes loss of the HA-rich pericellular glycocalyx, shedding of CD44, separation of CD44 from ERM, reduced baseline ERM activation, and ~50% decreased cell motility. These effects are inhibited by Na+/H+ exchanger-1 (NHE-1) inhibitor, suggesting Hyal2 requires local acidification for pericellular hyaluronidase activity. | PMID:19783662 | The Journal of biological chemistry |
| 2011 | High | Hyal2 is strongly associated with the plasma membrane through a functional GPI anchor in MDA-MB231 cancer cells and COS-7 transfected cells, demonstrated by phosphatidylinositol-specific phospholipase C (PI-PLC) release into aqueous phase and Triton X-114 hydrophobic phase extraction. Hyal2 is specifically associated with detergent-resistant, cholesterol-rich lipid raft membrane fractions. | PMID:21740893 | Biochemical and biophysical research communications |
| 2015 | Medium | HYAL2 is localized to the surface and cytoplasm of endothelial cells and specialized epithelial cells in multiple mouse tissues, including brain (contrary to earlier reports of brain silencing). In Hyal2−/− mice, accumulated higher-molecular-mass HA is detected near sites of normal HYAL2 expression, confirming HYAL2 initiates extracellular HA catabolism; highest HYAL2 levels were found in tissues that clear circulating HA (liver, lymph node, spleen). | PMID:26515055 | Histochemistry and cell biology |
| 2016 | Medium | Low shear stress (LSS) activates HYAL2 to degrade HA in the endothelial glycocalyx; HYAL2 knockdown in HUVECs prevents LSS-induced HA degradation, dephosphorylation of eNOS-Ser-633, and decrease in NO production. LSS-induced eNOS-Ser-633 dephosphorylation is mediated via PKA dephosphorylation downstream of HYAL2 activation, reversible by PKA activator 8-Br-cAMP. | PMID:27798230 | Molecular biology of the cell |
| 2017 | High | Biallelic loss-of-function mutations in HYAL2 cause syndromic orofacial clefting and cor triatriatum sinister in humans. Transfection assays showed that HYAL2 disease mutations destabilize the protein, dramatically reducing HYAL2 protein levels. Hyal2−/− mice recapitulate craniofacial abnormalities including submucosal cleft palate, cor triatriatum sinister, and hearing loss. | PMID:28081210 | PLoS genetics |
| 2017 | Low | Rare HYAL2 variants, including a missense variant (N357S) at a known N-glycosylation site and a nonsense variant (Q406*) that removes the GPI anchor, are associated with increased ADP-induced platelet aggregation, suggesting that proper N-glycosylation and membrane-anchoring via GPI are required for normal HYAL2 function in platelet reactivity. | PMID:28300864 | Thrombosis and haemostasis |
| 2018 | Medium | Hyal2 interacts with p47phox in a complex (co-immunoprecipitation), and LSS induces dissociation of the p47phox/Hyal2 complex, activating Hyal2 and NADPH oxidase; LKB1 overexpression prevents complex dissociation. LSS activates Hyal2 via LKB1/AMPK/NADPH oxidase (p47phox) signaling, and Hyal2 knockdown provides positive feedback on LKB1 activity. | PMID:30078213 | Journal of cellular physiology |
| 2020 | Medium | Hyal2-expressing CD11b+CD33+ monocytic myeloid-derived suppressor cells degrade extracellular HA to produce LMW-HA (<20 kDa) in bladder cancer tissue. CD44 receptor engagement by specific mAb triggers translocation of Hyal2 to the cell surface and stimulates IL-1β secretion in these myeloid cells; IL-1β in turn enhances Hyal2 HA-degrading activity. | PMID:33239427 | Cancer research |
| 2021 | Medium | HYAL2 missense variants identified in patients with syndromic cleft lip/palate cause protein instability and result in absence of HYAL2 from the cell surface, as demonstrated by immunoblotting and immunofluorescence of mutant vs. wild-type HYAL2 expressed in mouse fibroblasts. In silico modeling confirmed deleterious effects on protein folding. | PMID:34906488 | Genetics in medicine |
| 2024 | Medium | HYAL2 promotes odontoblastic differentiation of mouse dental papilla cells (mDPCs) by degrading extracellular HA; HYAL1 had negligible effect on differentiation. Hyal2 silencing causes HA accumulation in the extracellular environment, attenuating F-actin and filopodium formation and inhibiting cell migration. PI3K/Akt signaling activation rescues differentiation defects caused by HA accumulation. | PMID:38490466 | Matrix biology |
| 2024 | Low | In vitro, lower molecular weight HA (produced by HYAL2 degradation) increases sphere-forming ability and migration of MCF-7 and MDA-MB-231 breast cancer cells, while higher molecular weight HA inhibits these processes, establishing HYAL2-mediated HA fragmentation as a pro-tumorigenic mechanism via product size. | PMID:38991455 | Pathology, research and practice |
| 2026 | Medium | HYAL2-generated LMW-HA promotes nucleus pulposus cell senescence, inflammatory activation, and ECM degradation via CD44-mediated suppression of AKT phosphorylation. Genetic ablation of HYAL2 in a mouse IVDD model attenuates disease progression. CD44 knockdown abolishes LMW-HA-induced AKT inactivation; AKT reactivation reverses the degenerative phenotype. | PMID:41806573 | Biochemical and biophysical research communications |

## Citations

- PMID:11296287
- PMID:11804776
- PMID:11960552
- PMID:12584308
- PMID:15596803
- PMID:16191204
- PMID:18772348
- PMID:19366691
- PMID:19783662
- PMID:21740893
- PMID:26515055
- PMID:27798230
- PMID:28081210
- PMID:28300864
- PMID:30078213
- PMID:33239427
- PMID:34906488
- PMID:38490466
- PMID:38991455
- PMID:41806573
- PMID:9712871
