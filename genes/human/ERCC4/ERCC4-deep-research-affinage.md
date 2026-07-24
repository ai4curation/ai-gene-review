---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ERCC4
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q92889
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 40
citation_count: 41
gates_passed: False
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ERCC4 (human)

> ⚠️ **CAUTION — trust gate(s) tripped; review before using:**
>
> - Affinage's own head-to-head self-evaluation scored this record `pairwise = tie` (not `win`) vs the curated UniProt reference — treat the narrative with extra scepticism.

## Current model (mechanistic narrative)

ERCC4 (XPF) is the catalytic subunit of a structure-specific endonuclease that operates as an obligate heterodimer with ERCC1 to incise DNA at single-strand/double-strand junctions across multiple genome-maintenance pathways [PMID:8253090, PMID:8253091, PMID:7559382, PMID:9525876]. The purified heterodimer cleaves bubble, splayed-arm, and flap substrates on the 5' side of ss/ds junctions, requiring divalent cations and a minimal stretch of unpaired nucleotides [PMID:9525876], with the nuclease active site mapping to XPF residues 670–740 where point mutations abolish catalysis without affecting DNA binding [PMID:11953324]. Structural work resolves the basis for substrate engagement: ERCC1 and XPF contribute non-equivalent (HhH)₂ and central domains that bind ssDNA and dsDNA asymmetrically [PMID:16076955, PMID:22483113], and cryo-EM shows the DNA-free complex adopts an auto-inhibited conformation that masks the active site until junction engagement couples the ERCC1 (HhH)₂ to the nuclease domains [PMID:32111838]. In nucleotide excision repair, the complex is recruited through direct ERCC1–XPA interaction to execute the 5' incision [PMID:8197175, PMID:17948053], and its participation is distributive, with damage-induced transient immobilization at lesions [PMID:10320375]. Beyond NER, XPF-ERCC1 carries out interstrand crosslink unhooking downstream of FANCD2 ubiquitylation and SLX4 recruitment, with RPA activating incision at replication-fork ICL structures and SNM1A loading from the resulting nicks [PMID:19805513, PMID:24726325, PMID:28607004, PMID:28292785], and it functions in double-strand break end-joining and single-strand annealing [PMID:18541667, PMID:17962301]. The complex additionally maintains telomeres [PMID:18812185], processes R-loops in association with XAB2 [PMID:34039990], drives ALT telomere synthesis via TERRA R-loops [PMID:36184605], and supports CTCF/cohesin-dependent chromatin looping for transcriptional regulation and imprinted-gene silencing independent of repair, a role requiring its catalytic activity [PMID:22771116, PMID:28368372]. Heterodimerization governs the complex's integrity and compartmentalization: XPF stability requires ERCC1 [PMID:20418188], nuclear import of ERCC1 requires XPF [PMID:28130555], and USP45-mediated deubiquitylation of ERCC1 promotes recruitment to damage sites [PMID:25538220]. Biallelic ERCC4 mutations cause Fanconi anemia, and the spectrum of XP, XFE progeroid, and FA phenotypes reflects mutations that separably impair NER, ICL repair, or proper localization [PMID:20221251, PMID:23623386, PMID:30165384].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140097 catalytic activity, acting on DNA, GO:0016787 hydrolase activity, GO:0003677 DNA binding, GO:0003723 RNA binding
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-4839726 Chromatin organization, R-HSA-1643685 Disease
- **partners:** ERCC1, XPA, SLX4, RPA, USP45, SLX4IP, RAD52, XAB2
- **complexes:** ERCC1-XPF heterodimer, SLX4-XPF-ERCC1 complex, XAB2-ERCC1-XPF-XPG complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1994 | High | XPA forms a ternary complex with the ERCC1/XPF (ERCC4) heterodimer; XPA affinity column retained ERCC1 and ERCC4(XPF) correcting activities from HeLa cell-free extract, establishing a direct protein-protein interaction between XPA and the ERCC1-XPF complex. | PMID:8197175 | Proceedings of the National Academy of Sciences of the United States of America |
| 1993 | High | ERCC1 co-purifies with XPF/ERCC4 as a ~100 kDa complex; extracts from ERCC1, ERCC4 (group 4), and XP-F cells all fail to complement each other in vitro, and depletion of ERCC1 simultaneously removes correcting activities for groups 4, 11, and XP-F, indicating ERCC1 and XPF form a functional repair complex. | PMID:8253090, PMID:8253091 | The EMBO journal |
| 1995 | High | Purified XPF-ERCC1 heterodimer (ERCC1 38 kDa + XPF 112 kDa) from HeLa cells possesses endonuclease activity with preference for single-stranded DNA and bubble-structured duplex DNA; this activity is stimulated by RPA in the presence of UV-damaged DNA. XPF and ERCC4 are biochemically confirmed to be identical proteins. | PMID:7559382 | The Journal of biological chemistry |
| 1998 | High | Recombinant ERCC1-XPF purified from insect cells cleaves at single-strand/double-strand DNA junctions (5' side of junction) in the absence of other NER factors, requiring divalent cations (optimal at 0.2 mM Mn²⁺). A minimum of 4–8 unpaired nucleotides is required; the complex cuts splayed arm and flap substrates to remove 3' single-stranded arms, 2–8 nt from the junction. | PMID:9525876 | The Journal of biological chemistry |
| 1999 | High | In living CHO cells, GFP-tagged ERCC1/XPF moves freely through the nucleus (diffusion coefficient ~15 µm²/s) consistent with free complex rather than preassembled holocomplexes. UV-induced DNA damage causes transient, dose-dependent immobilization of ERCC1/XPF for ~4 minutes per repair event, consistent with distributive (not processive) participation in NER. | PMID:10320375 | Science |
| 2002 | High | The nuclease active site of the XPF-ERCC1 heterodimer resides within residues 670–740 of XPF. Point mutations of acidic and basic residues in this region abolish nuclease activity but not DNA binding, separating catalysis from substrate recognition. Seven residues are absolutely conserved with Mus81 and archaeal RNA helicase families, defining a shared nuclease motif. | PMID:11953324 | The EMBO journal |
| 2004 | High | XPF-ERCC1 is required for repair of DNA double-strand breaks (DSBs) in mammals via a Ku86-independent end-joining mechanism. XPF-deficient fibroblasts are hypersensitive to γ-irradiation and accumulate persistent γH2AX foci; Ercc1−/− Ku86−/− cells show additive hypersensitivity and chromosomal aberrations; in vitro repair of DSBs with 3' overhangs produces large deletions in absence of ERCC1-XPF. | PMID:18541667 | Molecular and cellular biology |
| 2004 | Medium | XPF physically interacts with hRad52 via the N-terminal domain of hRad52 and the XPF protein. This interaction is stable in human cell-free extracts and stimulates XPF-ERCC1 endonuclease activity while attenuating hRad52 strand annealing activity, placing XPF-ERCC1 in a ternary complex that processes recombination intermediates. | PMID:14734547 | The Journal of biological chemistry |
| 2005 | High | Crystal structure of ERCC1 central domain reveals it adopts a fold similar to archaeal Mus81/XPF nuclease domains despite low sequence identity; ERCC1 central domain and C-terminal HhH₂ domain both bind ssDNA. Crystal structure of the XPF-ERCC1 HhH₂ heterodimer reveals two independent ssDNA-binding surfaces. ERCC1 central domain preferentially binds 5' single-stranded overhangs at ssDNA/dsDNA junctions. A model is proposed in which XPF-ERCC1 recognizes branched DNA using HhH₂ domains of both subunits plus the ERCC1 central domain. | PMID:16076955 | Proceedings of the National Academy of Sciences of the United States of America |
| 2005 | High | Crystal structure of an archaeal XPF homodimer alone and bound to dsDNA reveals large domain movement upon DNA binding, coupling the (HhH)₂ domain and nuclease domain for recognition of ds/ssDNA junctions; two non-equivalent DNA-binding sites are identified, and a model is proposed in which XPF distorts a 3' flap substrate to engage both sites for cleavage. | PMID:15719018 | The EMBO journal |
| 2007 | High | ERCC1 directly binds XPA via a small region (peptide) of XPA with submicromolar affinity; crystal structure of ERCC1 in complex with an XPA peptide reveals the binding interface. This XPA peptide potently inhibits NER in cell-free assay, blocking excision of a cisplatin adduct, establishing that XPA-ERCC1 interaction is essential for ERCC1-XPF recruitment to NER complexes. | PMID:17948053 | The EMBO journal |
| 2007 | Medium | ERCC1-XPF endonuclease is required for single-strand annealing (SSA) and also gene conversion in mammalian cells, supporting a role in synthesis-dependent strand annealing during DSB repair. | PMID:17962301 | Nucleic acids research |
| 2008 | Medium | ERCC1/XPF limits LINE-1 retrotransposition: XPF knockdown in human cells increases retrotransposition frequency, and ERCC1 complementation in ERCC1-deficient hamster cells reduces it, revealing that ERCC1-XPF processes flap intermediates generated during retrotransposon insertion. | PMID:18396111 | DNA repair |
| 2008 | Medium | XPF controls TRF2 association with telomeric DNA and telomere length maintenance through two distinct mechanisms: (1) nuclease-activity-dependent control of TRF2 binding to telomeres; (2) nuclease-activity-independent regulation of telomere length. Overexpression of XPF induces telomere shortening in XPF-proficient cells; XPF complementation suppresses telomere lengthening in XPF-deficient cells. | PMID:18812185 | Mechanisms of ageing and development |
| 2009 | High | XPF-ERCC1 unhooking of ICLs is required for stable chromatin loading and FANCD2 foci formation at ICLs: in XPF-ERCC1-deficient cells, FANCD2 is monoubiquitinated but chromatin-bound FANCD2 levels are dramatically reduced and ICL-induced foci are significantly lower, establishing that ICL unhooking by XPF-ERCC1 is required for downstream FA pathway activation and homologous recombination. | PMID:19805513 | Molecular and cellular biology |
| 2010 | Medium | XPF protein stability depends on ERCC1: siRNA knockdown of ERCC1 significantly reduces XPF protein levels (but not mRNA), while ERCC1 knockdown by XPF does not reciprocally destabilize ERCC1, indicating XPF protein stability requires its heterodimer partner. | PMID:20418188 | DNA repair |
| 2010 | High | Missense mutations in XPF can cause cytoplasmic mislocalization of XPF-ERCC1: cells from XFE progeroid patients show XPF-ERCC1 accumulation in the cytoplasm. Microinjection of XPF(R153P)-ERCC1 into the nucleus of XPF-deficient human cells restores NER of UV damage, demonstrating that mislocalization (not catalytic inactivity) accounts for part of the DNA repair defect in XFE syndrome. | PMID:20221251 | PLoS genetics |
| 2011 | High | SNM1A (hSNM1A) collaborates with XPF-ERCC1 to initiate ICL repair in replicating human cells: SNM1A 5'-3' exonuclease loads from XPF-ERCC1-induced nicks and digests past the ICL. Depletion of hSNM1A or ERCC1 each causes ICL sensitivity and accumulation of Mus81-dependent replication-associated DSBs. | PMID:21896658 | Genes & development |
| 2012 | High | XPF (and XPG) endonuclease activity is required for CTCF-dependent chromatin looping between promoter and terminator of the RARβ2 gene: siRNA silencing or catalytic-site mutations in XPF prevent CTCF recruitment, chromatin loop formation, and optimal transcription, establishing a non-repair transcriptional role for XPF. | PMID:22771116 | Molecular cell |
| 2012 | High | Multiple DNA-binding domains of ERCC1-XPF cooperate for NER function: mutations in the HhH domain of ERCC1 or the nuclease domain of XPF abolish cleavage of model substrates. Mutations in multiple DNA-binding domains are required to significantly diminish NER activity in vitro and in vivo, and ICL repair requires tighter substrate binding than NER. | PMID:22547097 | The Journal of biological chemistry |
| 2012 | High | The XPF C-terminal HhH domain directly contacts ssDNA phosphate backbone (NMR structure); a guanine base is flipped into a pocket contacting residues from both HhH motifs; a one-residue deletion in XPF's second HhH motif permits ssDNA interactions distinct from ERCC1's dsDNA binding, establishing asymmetric DNA recognition by the XPF-ERCC1 heterodimer at ss/ds junctions. | PMID:22483113 | Structure |
| 2013 | High | Biallelic germline mutations in ERCC4 (XPF) cause Fanconi anemia (FA-Q subtype). FA-causing ERCC4 mutations strongly disrupt ICL repair function without severely compromising NER, demonstrating that ERCC4/XPF has separable NER and ICL repair activities, and that the type of mutation determines which disease (XP, XFE progeroid, or FA) manifests. | PMID:23623386 | American journal of human genetics |
| 2014 | High | XPF-ERCC1 cooperates with SLX4/FANCP to carry out ICL unhooking incisions in replication-coupled ICL repair. Efficient recruitment of XPF-ERCC1 and SLX4 to the ICL requires FANCD2 and its ubiquitylation, establishing the pathway order: FANCD2 ubiquitylation → SLX4/XPF-ERCC1 recruitment → unhooking. | PMID:24726325 | Molecular cell |
| 2014 | High | USP45 deubiquitylase directly binds ERCC1 (via an acidic motif outside the USP45 catalytic domain), deubiquitylates ERCC1 in vitro, and promotes ERCC1-XPF translocation to UV-induced DNA damage foci. Loss of USP45 causes elevated ubiquitylated ERCC1, impaired ERCC1-XPF foci formation, and hypersensitivity to UV and ICL agents similar to ERCC1-deficient cells. | PMID:25538220 | The EMBO journal |
| 2017 | High | RPA activates XPF-ERCC1 endonuclease activity at ICL-containing replication fork structures: a nascent leading strand inhibits XPF-ERCC1 incision on model fork substrates, but addition of RPA selectively restores activity. SNM1A can load from XPF-ERCC1-RPA-induced incisions and digest past the crosslink to complete unhooking. | PMID:28607004 | The EMBO journal |
| 2017 | High | The helicase-like domain of XPF mediates binding to SLX4 for ICL-specific recruitment; a mutation in this domain disrupts SLX4 binding and recruitment to ICL but not to NER substrates. A second transient XPF-SLX4 interaction is required for positioning/unhooking. Nuclease domain mutations prevent incisions without affecting ICL localization, defining three separable steps: recruitment, positioning, and catalysis. | PMID:28292785 | The EMBO journal |
| 2017 | High | ERCC1-XPF cooperates with the insulator protein CTCF and cohesin (SMC1A, SMC3) to facilitate developmental silencing of imprinted genes. In vivo biotinylation tagging shows ERCC1-XPF co-localizes with CTCF, cohesin, MBD2, and ATRX at imprinted gene promoters and ICRs during postnatal hepatic development. Loss of Ercc1 dissociates CTCF-cohesin from promoters and alters histone marks without changing DNA methylation. | PMID:28368372 | Nature cell biology |
| 2019 | Medium | SLX4IP binds both SLX4 and XPF-ERCC1 simultaneously, stabilizing the SLX4-XPF-ERCC1 complex; disruption of one interaction destabilizes both. SLX4IP depletion sensitizes cells to ICL agents and causes G2/M accumulation, promoting the interaction between SLX4 and XPF-ERCC1 particularly after DNA damage. | PMID:31495888 | Nucleic acids research |
| 2019 | Medium | ERCC1/XPF is required for repair of DSBs containing DNA secondary structures (AT-rich sequences from common fragile sites and G-quadruplexes). XPF inactivation is synthetically lethal with FANCM deficiency (which removes DNA secondary structures), and XPF sensitizes FANCM-deficient cells to G4-interacting compounds. | PMID:31153042 | iScience |
| 2020 | High | Cryo-EM structures of human XPF-ERCC1 reveal that the DNA-free form adopts an auto-inhibited conformation in which the XPF helical domain masks the ERCC1 (HhH)₂ domain and restricts access to the XPF catalytic site. DNA junction engagement releases this auto-inhibition, coupling ERCC1 (HhH)₂ with the nuclease domains. FA patient mutations in XPF are resistant to activation by the ICLR recruitment factor SLX4 despite retaining in vitro activity. | PMID:32111838 | Nature communications |
| 2017 | High | XPF protein requires heterodimerization with ERCC1 for nuclear import: in CRISPR/Cas9 XPF knockout cells, ERCC1 is retained in the cytoplasm and not detectable in the nucleus; overexpression of wild-type XPF restores ERCC1 nuclear localization, showing that XPF is required for nuclear entry of ERCC1. | PMID:28130555 | Cellular and molecular life sciences |
| 2021 | Medium | The splicing factor XAB2 interacts with ERCC1-XPF (and XPG) outside of canonical NER; the trimeric XAB2-ERCC1-XPF-XPG complex binds RNA:DNA hybrids (R-loops). XAB2 depletion causes aberrant intron retention, R-loop formation, and DNA damage, linking spliceosomal function to R-loop processing by ERCC1-XPF. | PMID:34039990 | Nature communications |
| 2021 | Medium | In C. elegans, tissue-specific NER activity differs: in oocytes XPF-1 functions in global genome NER for rapid genome-wide lesion removal, whereas in post-mitotic neurons and muscles XPF-1 participates only in transcription-coupled NER of transcribed genes, establishing that XPF-1 NER subpathway usage is determined by cell type. | PMID:33440146 | Cell reports |
| 2022 | Medium | XPF is recruited to ALT telomeres by telomeric RNA:DNA R-loops (TERRA R-loops) and induces DNA damage response (DDR) independently of CSB and SLX4, triggering break-induced telomere synthesis (ALT). XPF recruitment requires BRCA1 and RAD51 in FANCM-deficient cells that accumulate telomeric R-loops. | PMID:36184605 | Nature communications |
| 2001 | Medium | Functional ERCC1-XPF heterodimer can be reconstituted from separately produced subunits (expressed in E. coli). ERCC1 alone can confer partial NER activity to ERCC1-deficient extracts only when endogenous XPF is present; adding ERCC1 to XPF-deficient extracts requires co-addition of XPF. Sequence comparison reveals similarity between ERCC1 and the C-terminal region of XPF, suggesting ancient gene duplication gave rise to both subunits. | PMID:11160918 | Nucleic acids research |
| 2015 | Medium | ERCC1-XPF participates in repair of Topoisomerase 1-attached nick DNA lesions (Tyr-nick DNA): ERCC1-XPF shows nuclease activity on Tyr-nick substrates in the presence of RPA in vitro; ERCC1-XPF and RPA co-localize in CPT-treated cells in vivo; repair synthesis of Tyr-nick DNA requires ERCC1-XPF, RPA, DNA polymerase delta, FEN1, and DNA ligase 1. | PMID:26025908 | Carcinogenesis |
| 2018 | High | XP-causing XPF mutations (e.g. R799W) diminish XPF recruitment to DNA damage and mildly affect GG-NER, whereas an XPCS-complex-specific mutation causes persistent recruitment of XPF and upstream NER machinery to DNA damage, severely impairing both GG-NER and TC-NER. Persistent NER factor engagement at DNA damage is identified as a hallmark of XPCS-complex cells. | PMID:30165384 | Nucleic acids research |
| 2018 | Medium | XPF-ERCC1 mediates large deletions at DSBs associated with DNA:RNA hybrids (R-loops): XPF-dependent kilobase deletions are increased by Senataxin knockdown and reduced by RNaseH1 overexpression, and DNA:RNA hybrids are detected at DSB sites, establishing XPF as a mediator of mis-repair deletions at transcribed loci. | PMID:29497062 | Scientific reports |
| 2018 | Medium | XPF and ARTEMIS independently cleave stalled DNA replication forks through non-epistatic pathways during S and G2 phases. Both nucleases are recruited to chromatin to promote replication fork restart; their rapid fork cleavage activity prevents mitotic segregation defects. | PMID:30059501 | PLoS genetics |
| 2019 | Medium | TGFβ signaling enhances NER by increasing ERCC1-XPF and ERCC1-XPA protein interactions and promoting their nuclear co-localization; the effect requires intact TGFβ/Smad4 signaling and ERCC1, and is cell-cycle independent. | PMID:30418489 | Carcinogenesis |

## Citations

- PMID:10320375
- PMID:11160918
- PMID:11953324
- PMID:14734547
- PMID:15719018
- PMID:16076955
- PMID:17948053
- PMID:17962301
- PMID:18396111
- PMID:18541667
- PMID:18812185
- PMID:19805513
- PMID:20221251
- PMID:20418188
- PMID:21896658
- PMID:22483113
- PMID:22547097
- PMID:22771116
- PMID:23623386
- PMID:24726325
- PMID:25538220
- PMID:26025908
- PMID:28130555
- PMID:28292785
- PMID:28368372
- PMID:28607004
- PMID:29497062
- PMID:30059501
- PMID:30165384
- PMID:30418489
- PMID:31153042
- PMID:31495888
- PMID:32111838
- PMID:33440146
- PMID:34039990
- PMID:36184605
- PMID:7559382
- PMID:8197175
- PMID:8253090
- PMID:8253091
- PMID:9525876
