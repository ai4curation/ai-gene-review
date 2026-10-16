---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARFGEF2
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9Y6D5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 24
citation_count: 24
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARFGEF2 (human)

## Current model (mechanistic narrative)

ARFGEF2 (BIG2) is a brefeldin A-sensitive guanine nucleotide exchange factor that activates class I ARFs (ARF1 and ARF3) to drive membrane trafficking at the trans-Golgi network (TGN) and recycling endosomes, and through this activity it controls cargo delivery, organelle integrity, and several downstream signaling outputs [PMID:14647276, PMID:15385626]. By activating ARFs at the TGN, BIG2 recruits the clathrin adaptors AP-1 and GGA — but not the COPI coat — placing it specifically in the TGN-to-endosome arm of membrane traffic, and it acts redundantly with its homolog BIG1 in AP-1-dependent retrograde transport while retaining a non-redundant role in maintaining recycling endosome integrity [PMID:11777925, PMID:12051703, PMID:18417613, PMID:20360857]. Its catalytic activity is required for recycling of cargoes including the transferrin receptor and integrin beta1, and for release of TNFR1 exosome-like vesicles, and BIG2 transports E-cadherin, beta-catenin, and Filamin A from the Golgi to the cell surface [PMID:14647276, PMID:15385626, PMID:16477018, PMID:16320251, PMID:17276987, PMID:22908276]. BIG2 is recruited to the TGN by the small G protein Arl1 acting downstream of a GBF1→ARF4/ARF5 cascade, and it homodimerizes through an intramolecular DCB/HUS interaction [PMID:22291037, PMID:23386609, PMID:17640864]. Beyond catalysis, BIG2 functions as an A-kinase-anchoring protein (AKAP) with three N-terminal domains that bind PKA regulatory subunits; PKA phosphorylation lowers its GEF activity and is reversed by PP1gamma, and this AKAP/cAMP module — also engaging PDE3A — couples BIG2 to TNFR1 vesicle release and beta-catenin S675 phosphorylation and transcriptional coactivation [PMID:12571360, PMID:17360629, PMID:18625701, PMID:19332778, PMID:27162341]. BIG2 additionally scaffolds a myosin phosphatase complex (myosin IIA, PP1delta, MYPT1) independently of its GEF activity to control myosin light-chain phosphorylation, F-actin content, and cell migration, and drives a BIG2-ARF1-RhoA-mDia1 axis governing dendritic Golgi polarization in neurons [PMID:23918382, PMID:29455446]. BIG2 is also required for VEGF expression and angiogenesis [PMID:31199673].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005768 endosome, GO:0005815 microtubule organizing center, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-162582 Signal Transduction, R-HSA-9609507 Protein localization
- **partners:** ARF1, ARF3, ARL1, EXO70, MYH9 (NONMUSCLE MYOSIN IIA), PPP1CC (PP1GAMMA), PDE3A, CTNNB1 (BETA-CATENIN)
- **complexes:** myosin phosphatase complex (myosin IIA / PP1delta / MYPT1), BIG2 AKAP-PKA complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | High | ARFGEF2/BIG2 is required for vesicle and membrane trafficking from the trans-Golgi network (TGN); inhibition by brefeldin A or dominant-negative ARFGEF2 cDNA decreases neural progenitor cell proliferation in vitro and disrupts intracellular localization of E-cadherin and beta-catenin by preventing their transport from the Golgi apparatus to the cell surface. | PMID:14647276 | Nature genetics |
| 2002 | Medium | BIG2 overexpression blocks BFA-induced redistribution of ARF1 and the AP-1 complex from TGN membranes but not the COPI complex, indicating BIG2 specifically regulates membrane association of AP-1 (but not COPI) through ARF activation at the TGN. | PMID:11777925 | The Journal of biological chemistry |
| 2002 | Medium | A dominant-negative BIG2 mutant induces redistribution of AP-1 and GGA1 coat proteins and membrane tubulation of the TGN, but does not affect COPI redistribution or Golgi tubulation, placing BIG2 specifically in the TGN-to-endosome trafficking pathway via AP-1 and GGA regulation. | PMID:12051703 | Biochemical and biophysical research communications |
| 2004 | High | BIG2 localizes to both the TGN and recycling endosomes; expression of a catalytically inactive BIG2 mutant (E738K) selectively induces membrane tubules from the recycling endosome compartment. BIG2 has exchange activity toward class I ARFs (ARF1 and ARF3) in vivo, and inactivation of either ARF exaggerates tubulation induced by BIG2(E738K), indicating BIG2 maintains recycling endosome integrity via class I ARF activation. | PMID:15385626 | Molecular biology of the cell |
| 2003 | High | BIG2 contains three A kinase-anchoring protein (AKAP) domains in its N-terminal region: domain A (residues 27–48) interacts with RI-alpha and RI-beta; domain B (284–301) interacts with RII-alpha and RII-beta; domain C (517–538) interacts with RI-alpha, RII-alpha, and RII-beta. BIG2 physically interacts with the PKA regulatory subunit RI-alpha, confirmed by coimmunoprecipitation of in vitro translated proteins and endogenous proteins. Elevation of cAMP (8-Br-cAMP or forskolin) induces translocation of BIG2 from cytosol to Golgi and other membranes. | PMID:12571360 | Proceedings of the National Academy of Sciences of the United States of America |
| 2005 | Medium | BIG2 physically interacts with exocyst protein Exo70 via its N-terminal region (amino acids 1–643); both BIG2 and Exo70 co-localize at trans-Golgi network membranes and at the microtubule-organizing center (MTOC)/centrosomes in HepG2 cells, suggesting functional association in vesicular trafficking from TGN to plasma membrane. | PMID:15705715 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | High | BIG2 localizes specifically (not BIG1) to recycling endosome structures during transferrin uptake and transferrin receptor (TfnR) recycling in COS7 cells. BIG2 siRNA knockdown causes perinuclear accumulation of TfnR and significantly slows transferrin release, demonstrating a functional role for BIG2 in TfnR recycling. BIG2 interacts with Exo70 in recycling endosome fractions. | PMID:16477018 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | Medium | BIG2 (but not BIG1) is required for trafficking of Filamin A (FLNA) from the Golgi apparatus to the cell membrane in neuroblastoma cells; transfection of dominant-negative ARFGEF2 partially blocks FLNA transport. BIG2 and FLNA are co-expressed in neural progenitors along the neuroependyma. | PMID:16320251 | The Journal of comparative neurology |
| 2007 | High | BIG2 (not BIG1) regulates constitutive release of TNFR1 exosome-like vesicles from human vascular endothelial cells via an ARF1- and ARF3-dependent mechanism. BIG2 co-localizes with TNFR1 in cytoplasmic vesicles, and this association is disrupted by BFA. ARF1 and ARF3 act nonredundantly and additively in TNFR1 exosome-like vesicle release. | PMID:17276987 | The Journal of biological chemistry |
| 2007 | High | PKA phosphorylates BIG2 in vitro, decreasing its GEP activity; this phosphorylation is reversed by protein phosphatase 1gamma (PP1gamma) but not PP1alpha or PP1beta. Endogenous PP1gamma (not PP1alpha or PP1beta) co-immunoprecipitates with BIG2 from microsomal fractions, establishing PP1gamma as a regulator of BIG2 activity. | PMID:17360629 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | Medium | AMY-1 (associate of Myc-1) co-immunoprecipitates with both BIG2 and BIG1 in vitro, but localizes to the TGN specifically through interaction with BIG2 (not BIG1) as demonstrated by RNAi: depletion of BIG2 (not BIG1) disperses AMY-1 from the TGN. | PMID:16866877 | Genes to cells : devoted to molecular & cellular mechanisms |
| 2007 | Medium | BIG2 (and BIG1) form homodimers through interactions between their conserved DCB domains; within each homodimer, the DCB domain also interacts with the HUS domain. The HUS box is the most conserved motif in large ArfGEFs after the Sec7 domain and mediates the DCB/HUS interaction. | PMID:17640864 | The Journal of biological chemistry |
| 2008 | Medium | Simultaneous knockdown of both BIG2 and BIG1 causes mislocalization of TGN/recycling endosome-associated proteins and blocks retrograde transport of furin from late endosomes to the TGN, a phenotype similar to depletion of AP-1, establishing BIG2 and BIG1 as redundant regulators of AP-1-dependent trafficking between TGN and endosomes. | PMID:18417613 | Molecular biology of the cell |
| 2008 | Medium | cAMP-induced release of TNFR1 exosome-like vesicles requires PKA activity and is mediated through BIG2's AKAP function: PKA regulatory subunit RIIbeta binds specifically to BIG2 AKAP domains B and C, and this interaction is required for both constitutive and cAMP-induced TNFR1 exosome-like vesicle release. | PMID:18625701 | The Journal of biological chemistry |
| 2009 | Medium | Phosphodiesterase 3A (PDE3A) physically associates with BIG2 (and BIG1) complexes; specific depletion of PDE3A by siRNA or its inhibition by cilostamide significantly decreases membrane-associated BIG2 and BIG1 and reduces activated ARF1-GTP, linking PDE3A-dependent cAMP regulation within BIG2 AKAP complexes to ARF1 activation. | PMID:19332778 | Proceedings of the National Academy of Sciences of the United States of America |
| 2010 | Medium | Depletion of BIG2 (but not BIG1) by siRNA induces tubulation of the recycling endosomal compartment, while BIG1 depletion causes Golgi fragmentation into mini-stacks; this demonstrates non-redundant and distinct functions for BIG2 (recycling endosome integrity) vs. BIG1 (Golgi morphology). | PMID:20360857 | PloS one |
| 2012 | High | The small G protein Arl1 is necessary and sufficient for Golgi recruitment of BIG2 (and BIG1) but not GBF1. Arl1 binds directly to the N-terminal region of Sec71 (the Drosophila ortholog of BIG1/BIG2), establishing Arl1 as the upstream recruiter that directs BIG2 specifically to the trans-Golgi. | PMID:22291037 | The Journal of cell biology |
| 2012 | Medium | BIG2 siRNA depletion causes perinuclear accumulation of integrin beta1 and delayed return to the cell surface, decreased cell motility, and reduced actin-based membrane protrusions; cytosolic levels of Arp2, Arp3, cofilin-1, phosphocofilin, vinculin, and Grb2 are increased, establishing BIG2 as a regulator of integrin beta1 recycling and actin dynamics in cell migration. | PMID:22908276 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | Medium | GBF1-activated ARFs (ARF4 and ARF5, but not ARF3) facilitate BIG2 and BIG1 recruitment to the TGN, establishing a functional GEF cascade: GBF1 (pre-Golgi/Golgi/TGN) → ARF4/ARF5 activation → BIG1/BIG2 TGN recruitment → ARF activation for AP-1/GGA clathrin adaptor recruitment. | PMID:23386609 | The Journal of biological chemistry |
| 2013 | High | BIG2 physically associates (reciprocal Co-IP) with nonmuscle myosin IIA in HeLa cells independently of its ARF-GEF activity; depletion of BIG2 (or BIG1) enhances phosphorylation of myosin regulatory light chain (T18/S19) and increases F-actin content, impairing cell migration. BIG2 anchors a myosin phosphatase complex containing myosin IIA, protein phosphatase 1delta, and myosin phosphatase-targeting subunit 1 (MYPT1). | PMID:23918382 | Proceedings of the National Academy of Sciences of the United States of America |
| 2016 | Medium | BIG2 (and BIG1) physically interact with beta-catenin; depletion of BIG1/BIG2 or expression of GEF-inactive mutants causes perinuclear Golgi accumulation of beta-catenin and reduces PKA-phosphorylated beta-catenin (S675). BIG2 AKAP-C sequence is required for PKA-dependent S675 phosphorylation and beta-catenin transcription coactivator function, requiring both ARF-GEF activity and phospholipase D-dependent vesicular trafficking. | PMID:27162341 | Proceedings of the National Academy of Sciences of the United States of America |
| 2018 | Medium | BIG2 co-localizes with the Golgi apparatus in hippocampal neurons and is required for Golgi deployment into major dendrites. BIG2 acts through ARF1 to activate RhoA and its downstream effector mDia1, forming a BIG2-ARF1-RhoA-mDia1 signaling axis that regulates dendritic Golgi polarization and dendrite growth/maintenance. In vivo, ARFGEF2 shRNA delivered by in utero electroporation impairs Golgi deployment into the apical dendrite. | PMID:29455446 | Molecular neurobiology |
| 2019 | Medium | BIG2 (and BIG1) knockdown significantly decreases VEGF mRNA and protein levels in glioblastoma U251 cells and HUVECs, and inhibits HUVEC angiogenesis by diminishing cell migration. Knockdown of the BIG2 homolog arfgef2 in zebrafish impairs angioblast migration and intersegmental vessel sprouting, and CRISPR/Cas9 deletion of arfgef2 causes vascular development defects, establishing a role for BIG2 in VEGF expression and angiogenesis beyond vesicular trafficking. | PMID:31199673 | FASEB journal |
| 2025 | Medium | In Drosophila neuroblasts, Arf1 and its GEF ARFGEF2/Sec71 control asymmetric division by facilitating cortical localization of nonmuscle myosin II regulatory light chain (Sqh). Arf1 physically associates with Sqh and with Vibrator (a type I PITP), and Arf1/Sec71 facilitate PI(4)P localization to the neuroblast cortex, linking PI(4)P production to myosin II cortical anchoring during asymmetric division. | PMID:40208939 | Proceedings of the National Academy of Sciences of the United States of America |

## Citations

- PMID:11777925
- PMID:12051703
- PMID:12571360
- PMID:14647276
- PMID:15385626
- PMID:15705715
- PMID:16320251
- PMID:16477018
- PMID:16866877
- PMID:17276987
- PMID:17360629
- PMID:17640864
- PMID:18417613
- PMID:18625701
- PMID:19332778
- PMID:20360857
- PMID:22291037
- PMID:22908276
- PMID:23386609
- PMID:23918382
- PMID:27162341
- PMID:29455446
- PMID:31199673
- PMID:40208939
