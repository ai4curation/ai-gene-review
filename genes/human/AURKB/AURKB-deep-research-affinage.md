---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AURKB
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q96GD4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 47
citation_count: 48
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AURKB (human)

## Current model (mechanistic narrative)

AURKB (Aurora B kinase, the IPL1/AIR-2/AIM-1 ortholog) is the catalytic engine of high-fidelity chromosome segregation, functioning as the kinase subunit of the chromosomal passenger complex (CPC) together with INCENP/Sli15, Survivin/Bir1, and Borealin/Nbl1, which together control CPC localization, stability, and activity [PMID:8007975, PMID:7874197, PMID:10385519, PMID:19158380]. Its kinase activity is stimulated by direct association with INCENP/Sli15, which also targets it to the mitotic spindle [PMID:10385519, PMID:11724818]. AURKB enforces chromosome bi-orientation by phosphorylating outer-kinetochore and microtubule-binding substrates — Ndc10, the Dam1/DASH complex, and Ndc80 — to weaken improper kinetochore-microtubule attachments and promote their turnover until tension is established, at which point substrate dephosphorylation by the opposing PP1/Glc7 phosphatase stabilizes correct attachments [PMID:10072382, PMID:11724818, PMID:19923271, PMID:19822728, PMID:28928489, PMID:16537909]. By converting tension defects into unattached-kinetochore signals it activates the spindle assembly checkpoint specifically in response to loss of tension [PMID:11731476, PMID:16327780]. AURKB also phosphorylates histone H3 on serine 10 during mitosis [PMID:10975519, PMID:19704020], and drives cytokinesis, spindle midzone organization, and spindle disassembly through phosphorylation of midzone regulators such as Ase1 and through CPC relocalization to the central spindle [PMID:9809983, PMID:9852156, PMID:12566427, PMID:17765685]. Its spatiotemporal control is layered: Cdk1 phosphorylates AURKB and INCENP/Sli15 to restrain premature spindle binding until anaphase [PMID:21727193, PMID:22521784], haspin-generated H3T3ph and Shugoshin recruit it to centromeres [PMID:35694956, PMID:24945276], USP29-mediated deubiquitination stabilizes it [PMID:38233848], and VRK1 cross-inhibition modulates its H3 phosphorylation [PMID:29340707]. In specialized and disease contexts AURKB remodels meiotic kinetochores and protects meiotic cohesion [PMID:17371833, PMID:23371552, PMID:26157162], resets Oct4-driven pluripotency transcription in stem cells [PMID:26880562], and acts in interphase as a transcriptional regulator by depositing promoter H3S10ph at genes including CCND1, CCNE1, and TERT [PMID:31982864, PMID:38713155, PMID:37079315].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016740 transferase activity, GO:0042393 histone binding, GO:0140110 transcription regulator activity, GO:0008092 cytoskeletal protein binding, GO:0003723 RNA binding
- **localization:** GO:0005634 nucleus, GO:0005694 chromosome, GO:0005856 cytoskeleton, GO:0005815 microtubule organizing center, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-1474165 Reproduction, R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-1643685 Disease
- **partners:** INCENP, BIRC5, BOREALIN/NBL1, DAM1, NDC80, VRK1, USP29, MAD2L2
- **complexes:** Chromosomal passenger complex (CPC)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1994 | High | IPL1 encodes a protein kinase required for high-fidelity chromosome segregation in budding yeast. Type 1 protein phosphatase (PP1/GLC7) acts in opposition to Ipl1 kinase to ensure proper chromosome segregation: overexpression of GLC7 causes chromosome missegregation in wild-type cells, and glc7-1 mutation can partially suppress ipl1-1, establishing these two enzymes as opposing regulators of chromosome segregation. | PMID:8007975, PMID:7874197 | Molecular and cellular biology |
| 1999 | High | Ipl1p (Aurora B ortholog) regulates microtubule binding to kinetochores; kinetochores assembled from ipl1 mutant extracts show altered microtubule binding, and Ipl1p phosphorylates the kinetochore component Ndc10p in vitro. Ipl1p localizes to the mitotic spindle with cell-cycle-regulated levels. | PMID:10072382 | Genes & development |
| 2000 | High | Ipl1/Aurora kinase and its genetically interacting phosphatase Glc7/PP1 are responsible for the balance of histone H3 serine 10 phosphorylation during mitosis in S. cerevisiae and C. elegans. Both enzymes are required for H3 phosphorylation and chromosome segregation. | PMID:10975519 | Cell |
| 1998 | Medium | AIM-1 (rat Aurora B ortholog) controls entry into cytokinesis during M phase; kinase-negative AIM-1 inhibits cleavage furrow formation without affecting nuclear division. Overexpression of wild-type AIM-1 produces multinuclearity and increased ploidy. | PMID:9809983 | Cancer research |
| 1998 | High | AIR-2 (C. elegans Aurora B ortholog) is required for polar body extrusion and cytokinesis; RNAi-mediated depletion of AIR-2 results in failed cytokinesis with transient cleavage furrow initiation followed by regression, and mislocalization of midbody microtubule components. AIR-2 localizes to chromosomes during meiosis, moves to midbody microtubules at anaphase, and persists at the cytokinesis remnant. | PMID:9852156 | The Journal of cell biology |
| 1999 | High | Sli15 (INCENP ortholog) associates directly with the Ipl1 protein kinase in vivo; both proteins co-localize to the mitotic spindle. sli15 mutant phenotype is very similar to ipl1 mutants and is partially suppressed by reduced PP1 activity, establishing Sli15 as a key functional partner of Ipl1 in chromosome segregation. | PMID:10385519 | The Journal of cell biology |
| 2001 | High | Ipl1p (Aurora B) is required to maintain spindle checkpoint arrest induced by lack of tension at kinetochores but is not required for arrest induced by spindle depolymerization. Ipl1p localizes at or near kinetochores during mitosis, distinguishing two mechanistically distinct spindle checkpoint signals. | PMID:11731476 | Genes & development |
| 2001 | High | The Ipl1-Sli15 complex promotes chromosome bi-orientation by altering kinetochore-spindle pole connections. In ipl1 mutants, kinetochores remain attached to old spindle pole bodies and fail to turn over attachments, suggesting Ipl1-Sli15 facilitates bi-orientation by promoting turnover of kinetochore-microtubule connections until tension is established. | PMID:11853667 | Cell |
| 2001 | High | Sli15 stimulates the in vitro kinase activity of Ipl1 and facilitates Ipl1's association with the mitotic spindle. Both Ipl1 and Sli15 bind Dam1 (a microtubule-binding kinetochore protein) directly, and Ipl1 phosphorylates both Sli15 and Dam1 in vitro with reduced in vivo phosphorylation in ipl1 mutants. Sli15 and Ipl1 also bind microtubules directly in vitro and are associated with yeast centromeric DNA in vivo. | PMID:11724818 | The Journal of cell biology |
| 2003 | Medium | Ipl1p has a role in mitotic spindle disassembly separable from its chromosome segregation functions. Ipl1-GFP transfers from kinetochores to the spindle after metaphase and accumulates at the spindle midzone late in anaphase; Ipl1p kinase activity increases at anaphase, and ipl1 mutants can stabilize fragile spindles. | PMID:12566427 | The Journal of cell biology |
| 2005 | High | Ipl1/Aurora activates the spindle checkpoint in response to tension defects by creating unattached kinetochores. When Ipl1 function was impaired in kinetochore mutants that appear to have unattached kinetochores, microtubule attachments were restored and the checkpoint was turned off, demonstrating that Ipl1 converts tension defects into unattached kinetochore signals. | PMID:16327780 | Nature cell biology |
| 2005 | High | The Set1 methyltransferase modulates the Ipl1/Glc7 balance. Set1 methylates conserved lysines in the kinetochore protein Dam1, and Dam1 methylation inhibits Ipl1-mediated phosphorylation of flanking serines, demonstrating antagonism between lysine methylation and serine phosphorylation as a mechanism controlling Ipl1 substrate activity. | PMID:16143104 | Cell |
| 2006 | High | Glc7/PP1 ensures accurate chromosome segregation by dephosphorylating Ipl1 targets (particularly Dam1) rather than by regulating Ipl1 kinase levels or activity. Regulatory subunits Gip3 and Gip4 suppress ipl1-321 by redistributing Glc7 away from Ipl1 targets, restoring the balance of Dam1 phosphorylation. | PMID:16537909 | Molecular and cellular biology |
| 2007 | Medium | Aurora B kinase (Ipl1) in yeast is essential for protection of meiotic centromeric cohesion. Sgo1 recruits Ipl1 to centromeric regions, and in the absence of Ipl1, the PP2A regulatory subunit Rts1 cannot be maintained at centromeres after anaphase I onset, leading to loss of cohesion protection. | PMID:17371833 | The Journal of cell biology |
| 2007 | High | Ipl1/Aurora kinase is required for centrosome-mediated spindle assembly in the absence of BimC motor Cin8. Ipl1 regulates Ase1 (spindle midzone protein) by phosphorylating it; an Ase1 mutant lacking Ipl1 consensus phosphorylation sites cannot assemble spindles in the absence of Cin8, and Ase1 phosphorylation and localization are altered in ipl1 mutants. | PMID:17765685 | Developmental cell |
| 2009 | Medium | AURKB phosphorylates H3 at prophase, and RNAi knockdown of AURKB causes mitotic retention of XIST RNA on the inactive X chromosome, demonstrating that AURKB-mediated H3 phosphorylation regulates RNA binding to heterochromatin during mitosis. H3S10 phosphorylation (but not H3S28ph) is excluded from the inactive X and potentially linked to ubiquitination. | PMID:19704020 | The Journal of cell biology |
| 2009 | High | Ipl1-dependent phosphorylation of the kinetochore protein Dam1 is maximal during S phase and minimal during metaphase; when tension at kinetochores is reduced by failure to establish sister chromatid cohesion, Dam1 phosphorylation persists in metaphase, indicating that tension leads to dephosphorylation of Ipl1 substrates, stabilizing bi-orientation. | PMID:19923271 | Journal of cell science |
| 2009 | Medium | Phosphorylation of the Ndc80 kinetochore protein by Ipl1/Aurora B reduces its microtubule binding activity in vitro, and kinetochore-bound Ndc80 is phosphorylated on Ipl1 sites in vivo; however, this phosphorylation is not essential alone, indicating additional Ipl1 targets contribute to segregation and checkpoint signaling. | PMID:19822728 | Genetics |
| 2009 | High | Nbl1p is a new core component of the chromosomal passenger complex (CPC) in budding yeast, related to Borealin/Dasra. Nbl1p colocalizes and co-purifies with the CPC (Ipl1/Aurora B, Sli15/INCENP, Bir1/Survivin), is essential for CPC localization, stability, integrity, and function. Structure modeling revealed structural conservation of the CPC architecture from Fungi to Animalia. | PMID:19158380 | Molecular biology of the cell |
| 2009 | Medium | Ipl1/Aurora B coordinates synaptonemal complex (SC) disassembly with cell cycle progression in budding yeast meiosis. Ipl1 mutants fail to dissociate the central element Zip1 and its binding partner Smt3/SUMO from chromosomes in a timely fashion, and SC disassembly delay occurs even in cdc5 or NDT80-regulated backgrounds. | PMID:19759266 | Genes & development |
| 2011 | High | Ipl1/Aurora B-dependent phosphorylation of Sli15/INCENP modulates microtubule dynamics by preventing CPC binding to the preanaphase spindle and to the central spindle until late anaphase. Decreased Ipl1-dependent Sli15 phosphorylation drives direct CPC-microtubule binding, revealing how CPC influences microtubule dynamics. Cdk1 and Ipl1/Aurora cooperatively modulate microtubule dynamics. | PMID:21727193 | The Journal of cell biology |
| 2011 | Medium | Aurora kinase Ipl1 is necessary for maintenance of tight association (cohesion) between duplicated spindle pole bodies (SPBs) during meiosis. Loss of Ipl1 leads to premature SPB separation, overduplication, and multipolar spindles. The Polo-like kinase Cdc5 interacts antagonistically with Ipl1 at the meiotic SPB. | PMID:21878496 | Journal of cell science |
| 2012 | High | Cdk1 directly phosphorylates Ipl1/Aurora B on two serine residues in the N-terminal domain, suppressing its association with the microtubule plus-end tracking protein Bim1 until anaphase onset. Failure to phosphorylate Ipl1 leads to premature targeting to the metaphase spindle and constitutive Bim1 phosphorylation, and the non-phosphorylatable Ipl1-Sli15 complex causes severe growth defects. | PMID:22521784 | Current biology : CB |
| 2013 | High | Ipl1/Aurora B releases kinetochore-microtubule associations after meiotic entry, liberating chromosomes for homologous pairing in meiosis I. Ipl1 also releases improper kMT connections established early in meiosis, while Mps1 triggers formation of new force-generating attachments, establishing a sequential kinase mechanism for correct chromosome orientation. | PMID:23371552 | Science |
| 2014 | High | Ipl1/Aurora B-dependent phosphorylation of Sli15 on microtubule-binding domain sites inhibits Sli15-microtubule interaction in vitro; mimicking constitutive phosphorylation delocalizes the CPC in metaphase, while blocking phosphorylation drives excessive spindle localization. These Ipl1-phosphorylation events also regulate the tension checkpoint mechanism. | PMID:24558497 | PloS one |
| 2014 | Medium | Shugoshin (Sgo1) in budding yeast maintains Aurora B/Ipl1 localization on kinetochores during metaphase and also recruits condensin to centromeric chromatin via PP2A-Rts1, demonstrating a dual function of shugoshin in promoting biorientation. | PMID:24945276 | PLoS genetics |
| 2015 | High | Ipl1/Aurora B is necessary for kinetochore restructuring in meiosis I. Upon meiotic entry, the Ndc80 outer kinetochore complex (but not other subcomplexes) is shed from kinetochores in an Ipl1-dependent manner, promoting assembly of a meiosis-specific kinetochore that confers correct segregation patterns. | PMID:26157162 | Molecular biology of the cell |
| 2016 | High | Aurora B (Aurkb) phosphorylates Oct4 at serine 229 during G2/M, leading to dissociation of Oct4 from chromatin in embryonic stem cells (ESCs). PP1 then binds Oct4 and dephosphorylates S229 during M/G1 transition, resetting Oct4-driven transcription for pluripotency and cell cycle genes. Phospho-mimetic and PP1-binding-deficient Oct4 mutations alter the cell cycle and cause loss of pluripotency. | PMID:26880562 | eLife |
| 2017 | Medium | Rad52 is a substrate of Ipl1/Aurora B kinase in yeast and humans (confirmed by in vitro kinase assay). Ipl1-dependent phosphorylation of Rad52 facilitates kinetochore accumulation of Mps1, linking Aurora B activity to spindle assembly checkpoint regulation via Rad52. | PMID:29078282 | Proceedings of the National Academy of Sciences of the United States of America |
| 2017 | Medium | Phosphorylation of Dam1 by Ipl1/Aurora B kinase at three key serine residues in vivo promotes chromosome bipolar attachment. Phospho-deficient dam1-3A mutants show stabilized kinetochore-microtubule attachment, delay establishment of bipolar attachment after nocodazole washout, and exhibit dramatic chromosome missegregation. | PMID:28928489 | Scientific reports |
| 2018 | Medium | AURKB (Aurora B) phosphorylates survivin, and PLK1 also phosphorylates survivin at different sites to affect cell proliferation. AURKB and PLK1 are required for growth of African American but not European American triple-negative breast cancer (TNBC) xenografts, establishing a context-specific requirement for this phosphorylation axis. | PMID:36627281 | Cell death & disease |
| 2018 | Medium | VRK1 and AURKB form a stable protein complex; each kinase inhibits the kinase activity of the other and inhibits their respective histone H3 phosphorylations (Thr3 by VRK1, Ser10 by AURKB). Depletion of VRK1 downregulates survivin (BIRC5), preventing AURKB recruitment and localization to centromeres. | PMID:29340707 | Cellular and molecular life sciences : CMLS |
| 2018 | High | In mouse oocyte meiosis, AURKC is the predominant CPC kinase. In the absence of AURKC, AURKA localizes to chromosomes in a CPC-dependent manner, suggesting AURKC prevents AURKA from competing for CPC binding. AURKB negatively regulates AURKC to prevent aneuploidy, revealing inter-kinase regulation critical for meiosis. | PMID:30415701 | Current biology : CB |
| 2019 | Medium | AURKB phosphorylates histone H3 at serine 10 (H3S10ph), and this activity activates CCND1 expression through H3S10ph at the CCND1 gene promoter in gastric cancer cells. AZD1152 (AURKB inhibitor) suppresses CCND1 expression and inhibits cell proliferation in vitro and in vivo. | PMID:31982864 | Aging |
| 2019 | Medium | AURKB restrains glucocorticoid (GC) signaling in B-ALL by phosphorylating the histone methyltransferases EHMT1/EHMT2, which are required for GC-induced cell death gene expression. AURKB inhibition enhances GC-induced expression of cell death genes and potentiates GC cytotoxicity in relapsed B-ALL cells. | PMID:30733284 | Proceedings of the National Academy of Sciences of the United States of America |
| 2019 | Medium | In NSCLC cells with acquired resistance to EGFR TKIs, AURKB is activated (measured as increased phospho-histone H3), and AURKB inhibition reduces pH3 levels, triggering G1/S arrest and polyploidy followed by cell death or senescence depending on mutation status. | PMID:31000705 | Nature communications |
| 2019 | Medium | In KSHV-infected tumor cells, the viral latent antigen LANA cleaves AURKB at Asp76 in a serine protease-dependent manner, generating an N'-AURKB isoform that relocalizes to the spindle pole and promotes metaphase-to-telophase transition, enhancing colony formation and malignant growth. | PMID:30917319 | Cell reports |
| 2019 | High | COMA complex (Ctf19/Ame1/Okp1/Mcm21) recruits the Sli15/Ipl1 (INCENP/Aurora B) CPC to the inner kinetochore in budding yeast. The Ctf19 C-terminus interacts with the CPC in vitro, and tethering Sli15 to Ame1/Okp1 rescues lethality from Ctf19 depletion in a Sli15 centromere-targeting deficient mutant. Ame1/Okp1 selectively binds Cse4/CENP-A nucleosomes through the Cse4 N-terminus. | PMID:31112132 | eLife |
| 2020 | Medium | CCAT2 lncRNA interacts directly with and stabilizes BOP1, and BOP1 overexpression promotes chromosomal instability by increasing the active form of Aurora kinase B (AURKB), which regulates chromosomal segregation. | PMID:32805281 | Gastroenterology |
| 2021 | Medium | BRAF(V600E) induces mitotic arrest in human melanocytes through microRNA-mediated suppression of AURKB. MIR211-5p and MIR328-3p target AURKB mRNA and their overexpression induces mitotic failure, genome duplication, and proliferation arrest. AURKB expression rescues arrested nevus cells from this arrest. | PMID:34812139 | eLife |
| 2022 | Medium | Haspin kinase activity is required for recruitment of Aurora B (AURKB) and kinesin MCAK to meiotic centromeres during male meiosis in mice. Haspin inhibition or genetic ablation reduces H3T3 phosphorylation, impairs AURKB centromere localization, and causes chromosome congression defects. | PMID:35694956 | Journal of cell science |
| 2022 | Medium | USP29 deubiquitinase stabilizes AURKB by suppressing K48-linked polyubiquitination. FUBP1 transcription factor directly activates USP29 gene transcription, constituting a FUBP1-USP29-AURKB regulatory axis promoting gastric cancer. Systemic knockout of Usp29 in mice reduces AURKB levels in forestomach tissues. | PMID:38233848 | Cancer cell international |
| 2023 | Medium | AURKB inhibition (hesperadin) in uveal melanoma reduces H3S10 phosphorylation at the TERT (telomerase reverse transcriptase) promoter, leading to H3K9 methylation and chromatin condensation that silences TERT transcription, demonstrating an epigenetic mechanism by which AURKB controls telomerase expression. | PMID:37079315 | Investigative ophthalmology & visual science |
| 2024 | Medium | AURKB interacts with and modulates the expression of MAD2L2 in bladder cancer cells. AURKB activates MAD2L2 expression to downregulate the p53 DNA damage response pathway, promoting cancer cell proliferation and cell cycle progression. MAD2L2 overexpression rescues AURKB knockdown phenotypes in vitro and in vivo. | PMID:38515112 | Journal of translational medicine |
| 2024 | Medium | AURKB activates CCNE1 (cyclin E1) expression by phosphorylating histone H3 at serine 10 (H3S10ph) at the CCNE1 promoter in colorectal cancer cells, promoting cell proliferation and tumor growth. | PMID:38713155 | Aging |
| 2024 | Low | AURKB interacts with and phosphorylates DHX9 (DExH-Box helicase 9), targeting its expression in hepatocellular carcinoma cells, and this AURKB-DHX9 interaction promotes HCC progression through the PI3K/AKT/mTOR pathway. | PMID:38874176 | Molecular carcinogenesis |
| 2025 | Medium | AURKB exerts a kinase-independent oncogenic function in colorectal cancer by binding HNRNPM and interfering with its interaction with PSAT1 mRNA, thereby suppressing HNRNPM-mediated mRNA degradation and increasing PSAT1 protein levels. AURKB transcription in CRC is driven by H3K18 lactylation at its promoter. | PMID:40784984 | Journal of experimental & clinical cancer research : CR |

## Citations

- PMID:10072382
- PMID:10385519
- PMID:10975519
- PMID:11724818
- PMID:11731476
- PMID:11853667
- PMID:12566427
- PMID:16143104
- PMID:16327780
- PMID:16537909
- PMID:17371833
- PMID:17765685
- PMID:19158380
- PMID:19704020
- PMID:19759266
- PMID:19822728
- PMID:19923271
- PMID:21727193
- PMID:21878496
- PMID:22521784
- PMID:23371552
- PMID:24558497
- PMID:24945276
- PMID:26157162
- PMID:26880562
- PMID:28928489
- PMID:29078282
- PMID:29340707
- PMID:30415701
- PMID:30733284
- PMID:30917319
- PMID:31000705
- PMID:31112132
- PMID:31982864
- PMID:32805281
- PMID:34812139
- PMID:35694956
- PMID:36627281
- PMID:37079315
- PMID:38233848
- PMID:38515112
- PMID:38713155
- PMID:38874176
- PMID:40784984
- PMID:7874197
- PMID:8007975
- PMID:9809983
- PMID:9852156
