---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB11
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8WXH4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB11 (human)

## Current model (mechanistic narrative)

ASB11 is the substrate-recognition subunit of a Cullin-5/Elongin-BC E3 ubiquitin ligase complex (CRL5-ASB11) that controls cell fate, progenitor maintenance, and metabolic and survival programs by directing the polyubiquitination and turnover of specific substrates [PMID:24337577, PMID:21124961]. It assembles with Cullin 5 and Elongins B/C, and its Cul5-box domain is essential for complex formation and in vivo activity [PMID:24337577, PMID:21124961]. In developmental contexts, ASB11 maintains neural and myogenic progenitors in an undifferentiated, proliferating state and acts as an essential mediator of Delta-Notch lateral inhibition by directly ubiquitinating and degrading the Notch ligand DeltaA [PMID:16893969, PMID:22512762, PMID:18776899]. Beyond development, ASB11 governs several stress and metabolic pathways through dedicated substrates: during ER stress it is transcriptionally activated by the IRE1α-XBP1s arm of the unfolded protein response and ubiquitinates the pro-apoptotic protein BIK to promote survival [PMID:31387940]; it drives K6-linked polyubiquitination of the purine-synthesis enzyme PAICS to recruit UBAP2 and nucleate purinosome phase separation [PMID:37848033]; it ubiquitinates DIRAS2 within a UBE2F-neddylation-activated CRL5-ASB11 axis that sustains MAPK-c-Myc signaling in pancreatic cancer [PMID:38574733]; and it degrades the cholesterol-homeostasis regulator ERLIN1 [PMID:41668292]. ASB11 activity is post-translationally tuned by FIH-mediated hydroxylation of asparaginyl residues in its ankyrin repeat domain, a modification relieved under hypoxia to enhance substrate degradation [PMID:35537551, PMID:41668292]. Its localization to the endoplasmic reticulum is consistent with substrates spanning ER glycosylation and lipid-homeostasis machinery, including Ribophorin 1 of the OST complex [PMID:24337577].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016874 ligase activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005783 endoplasmic reticulum
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-1266738 Developmental Biology, R-HSA-8953897 Cellular responses to stimuli, R-HSA-1643685 Disease, R-HSA-162582 Signal Transduction
- **partners:** CUL5, ELOB, ELOC, UBE2F, FIH, DELTAA, BIK, PAICS
- **complexes:** CRL5-ASB11 (Cullin5-Elongin BC E3 ubiquitin ligase)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | High | d-Asb11 knockdown in zebrafish altered expression of neural precursor genes sox2 and sox3, caused expansion of neurogenin1-positive proneural cells followed by premature neuronal differentiation, while forced misexpression of d-asb11 ectopically induced sox2 and abolished neurogenesis. Overexpression in pluripotent and neural-committed progenitor cell lines inhibited terminal neuronal differentiation and enhanced proliferation, establishing d-Asb11 as a regulator of neural progenitor compartment size that maintains precursors in an undifferentiated proliferating state, possibly through control of SoxB1 transcription factors. | PMID:16893969 | The Journal of cell biology |
| 2008 | High | d-Asb11 is an essential mediator of canonical Delta-Notch lateral inhibition signaling in zebrafish. Morpholino knockdown repressed Delta-Notch elements and their transcriptional targets; misexpression activated Notch reporters cell-non-autonomously. d-Asb11 was shown to specifically ubiquitylate and degrade DeltaA both in vitro and in vivo, identifying DeltaA as a direct substrate for ASB11-mediated ubiquitination and degradation. | PMID:18776899 | Nature cell biology |
| 2010 | High | The Cul5 box domain of d-Asb11 is required in vivo for proper Notch signaling and neural cell fate. A zebrafish mutant lacking the Cul5 box (Asb11(Cul)) was defective in Notch signaling, unable to degrade DeltaA during embryogenesis, showed impaired neural cell fate specification, and Asb11(Cul) mRNA failed to transactivate a her4::gfp Notch reporter. This establishes that the Cul5 box domain is essential for d-Asb11 function in the ECS ubiquitin ligase complex. | PMID:21124961 | PloS one |
| 2012 | High | Asb11 localizes specifically to Pax7+ muscle satellite cells across vertebrates. Forced expression of d-asb11 impaired terminal differentiation and caused enhanced proliferation in myogenic progenitors in vivo and in vitro. A germline hypomorphic zebrafish d-asb11 mutation caused premature differentiation of muscle progenitors and delayed regenerative responses in adult injured muscle, establishing d-Asb11 as a principal regulator of embryonic and adult regenerative myogenesis. | PMID:22512762 | Stem cells and development |
| 2013 | High | ASB11 is a novel endoplasmic reticulum-resident ubiquitin ligase that interacts with and promotes ubiquitination of Ribophorin 1, an integral component of the oligosaccharyltransferase (OST) glycosylation complex. Expression of ASB11 increases Ribophorin 1 protein turnover in vivo. ASB11 was also found to form complexes with Cullin 5 and Elongins B/C, and Cullin 5 complexes can oligomerize. | PMID:24337577 | The Journal of biological chemistry |
| 2019 | High | Cul5-ASB11 is the E3 ligase that ubiquitinates the pro-apoptotic protein BIK, targeting it for degradation. ER stress activates ASB11 through the IRE1α-XBP1s arm of the unfolded protein response, stimulating BIK ubiquitination, interaction with p97/VCP, and proteolysis, thereby promoting cell survival during ER stress adaptation. Genotoxic agents down-regulate this IRE1α-XBP1s-ASB11 axis to stabilize BIK, contributing to apoptosis. XBP1s was identified as the transcriptional activator of ASB11 in response to ER stress. | PMID:31387940 | The Journal of cell biology |
| 2022 | High | The aspariginyl hydroxylase FIH (factor inhibiting HIF) catalyzes hydroxylation of asparaginyl residues in ankyrin repeat domain-containing proteins including ASB11. Biochemical and crystallographic evidence showed that FIH hydroxylates both asparaginyl residues in 'VNVN' motifs of ASB11's ankyrin repeat domain, representing a post-translational modification of ASB11. | PMID:35537551 | The Journal of biological chemistry |
| 2023 | High | The Cul5/ASB11-based ubiquitin ligase polyubiquitinates PAICS (a de novo purine synthesis enzyme) with K6-linked chains, driving purinosome assembly via phase separation. Polyubiquitinated PAICS recruits UBAP2, a ubiquitin-binding protein with intrinsically disordered regions, inducing phase separation for purinosome assembly and enhancing de novo purine synthesis flux. In melanoma, ASB11 is upregulated by relief of H3K9me3/HP1α-mediated transcriptional silencing, leading to constitutive purinosome formation required for melanoma cell proliferation and tumorigenesis. | PMID:37848033 | Molecular cell |
| 2024 | High | UBE2F neddylates CUL5 to activate CRL5-ASB11 E3 ligase, which ubiquitylates DIRAS2 for degradation. Ube2f deletion in a mouse KrasG12D PDAC model inactivates Mapk-c-Myc signaling by blocking DIRAS2 ubiquitylation, suppressing pancreatitis and pancreatic intraepithelial neoplasia. DIRAS2 deletion largely rescues Ube2f-deletion phenotypes, establishing UBE2F-CRL5ASB11-DIRAS2 as an oncogenic axis in pancreatic cancer. | PMID:38574733 | Developmental cell |
| 2026 | Medium | Under hypoxia, FIH-dependent hydroxylation of ASB11 at asparagine residues 90 and 92 is impaired, which enhances ASB11-mediated degradation of ERLIN1. ERLIN1 stabilizes the INSIG1-SCAP-SREBP2 axis to maintain cholesterol homeostasis in hepatocellular carcinoma. Pharmacological targeting using zoledronic acid weakens the ASB11-ERLIN1 interaction and restores cholesterol homeostasis, establishing ERLIN1 as a substrate of ASB11 regulated by FIH hydroxylation. | PMID:41668292 | Clinical and molecular hepatology |

## Citations

- PMID:16893969
- PMID:18776899
- PMID:21124961
- PMID:22512762
- PMID:24337577
- PMID:31387940
- PMID:35537551
- PMID:37848033
- PMID:38574733
- PMID:41668292
