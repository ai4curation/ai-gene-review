---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AFF4
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q9UHB7
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 27
citation_count: 26
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for AFF4 (human)

## Current model (mechanistic narrative)

AFF4 is the central intrinsically disordered scaffold of the Super Elongation Complex (SEC), an assembly that releases promoter-proximally paused RNA Polymerase II to drive productive transcriptional elongation [PMID:20159561, PMID:37609817]. Along its disordered axis, AFF4 uses distinct short interaction motifs to directly recruit P-TEFb (through CycT1), ELL2, and ENL/AF9, integrating these elongation factors into a single complex acting on the same polymerase [PMID:20471948, PMID:23251033]. Crystallographic analysis shows AFF4 meanders over the CycT1 surface without contacting CDK9, binding through a surface distinct from the CDK9 and Hexim1 sites [PMID:23471103, PMID:24985467], while its C-terminal homology domain (CHD) and a dimerization domain (THD) mediate AFF4 homodimerization and AFF1–AFF4 heterodimerization, with dimerization being essential for HIV-1 proviral transactivation but dispensable for binding other SEC subunits [PMID:31147444, PMID:32128251]. AFF4 is a key cofactor for HIV-1 Tat: it bridges P-TEFb and ELL2 into a bifunctional elongation complex and, by partially ordering the CycT1 Tat-TAR recognition motif, increases the affinity of Tat-P-TEFb for TAR RNA, acting as a selectivity filter that favors SEC assembly over P-TEFb alone [PMID:20471948, PMID:24843025, PMID:27731797]. Its activity is tuned by phosphorylation—CDK9 modifies a CHD surface loop to trigger pause release and phosphorylates S388 for PAX2-directed recruitment, while P70S6K phosphorylates S831 in an insulin-dependent manner to enhance ENL/AF9 recruitment to crotonylated histones [PMID:31147444, PMID:41476161, PMID:37063434]. Through these activities AFF4 controls discrete transcriptional programs and physically engages cohesin and RNAP2; gain-of-function missense mutations in AFF4 cause CHOPS syndrome [PMID:25730767]. Functionally, AFF4 is essential for spermatogenesis via Sertoli-cell transcriptional control [PMID:16024815] and for osteogenic and adipogenic differentiation, the latter through direct transcriptional activation of autophagy genes ATG5 and ATG16L1 [PMID:28955517, PMID:36149892], and it sustains oncogenic transcription of MYC, SOX2 and nucleotide-metabolism genes in bladder and pancreatic cancers [PMID:30659266, PMID:32676121, PMID:37063434]. AFF4 acts antagonistically with its paralog AFF1 across the transcription start site to set elongation rate and termination [PMID:37528066].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0060090 molecular adaptor activity, GO:0003723 RNA binding, GO:0003677 DNA binding, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus, GO:0005694 chromosome
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-1643685 Disease, R-HSA-1266738 Developmental Biology
- **partners:** CCNT1, ELL2, MLLT3, MLLT1, AFF1, FUS, MECP2, ATG5
- **complexes:** Super Elongation Complex (SEC), P-TEFb, Tat-AFF4-P-TEFb-TAR complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | AFF4 is a core component of the Super Elongation Complex (SEC), which includes ELL, P-TEFb, and other factors. AFF4 is required for SEC stability and proper transcription by poised RNA polymerase II in metazoans. Knockdown of AFF4 in leukemic cells reduces MLL chimera target gene expression. | PMID:20159561 | Molecular cell |
| 2010 | High | AFF4 bridges P-TEFb and ELL2 into a bifunctional elongation complex that greatly activates HIV-1 transcription. Through scaffolding functions of both Tat and AFF4, P-TEFb and ELL2 cooperate on the same RNA polymerase II. Without Tat, AFF4 can mediate the ELL2-P-TEFb interaction inefficiently; Tat overcomes this by bringing more ELL2 to P-TEFb and stabilizing ELL2 in a process requiring active P-TEFb. | PMID:20471948 | Molecular cell |
| 2002 | Medium | MCEF (AFF4) was identified as a binding partner of P-TEFb (CDK9/CyclinT1) by affinity purification from stably transfected cells expressing epitope-tagged CDK9; antisera against recombinant MCEF specifically immunoprecipitated P-TEFb. | PMID:12065898 | Journal of biomedical science |
| 2012 | High | AFF4 acts as the central scaffold of the HIV-1 Tat elongation complex, recruiting ELL2, ENL/AF9, and P-TEFb through direct interactions with short hydrophobic regions along its structurally disordered axis. CycT1, ELL2, and ENL/AF9 act as bridging components linking the complex to P-TEFb and the PAF complex. Binding sites were mapped both in vitro and in vivo. | PMID:23251033 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | High | Crystal structure of AFF4 in complex with P-TEFb (CDK9/CycT1) revealed that AFF4 meanders over the surface of CycT1 but makes no stable contacts with CDK9. AFF4 is positioned to make direct contacts with HIV Tat, and Tat enhances P-TEFb affinity for AFF4. Interface mutations in AFF4 reduced CycT1 binding and AFF4-dependent transcription. | PMID:23471103 | eLife |
| 2014 | High | Crystal structure of quaternary Tat-P-TEFb-AFF4 complex showed Tat and AFF4 fold on the CycT1 surface and interact directly. AFF4 binding partially orders the CycT1 Tat-TAR recognition motif (TRM) and increases the affinity of Tat-P-TEFb for TAR RNA 30-fold. Interface mutations in AFF1 reduced Tat-AFF1 affinity in vivo and Tat-dependent transcription from the HIV promoter. AFF4 acts as a two-step filter to increase selectivity of Tat and TAR for SECs over P-TEFb alone. | PMID:24843025 | eLife |
| 2014 | High | Crystal structure of Tat·AFF4·P-TEFb complex revealed that Tat binding to AFF4·P-TEFb causes concerted structural changes in AFF4 via a shift of helix H5' of CycT1 and the α-3(10) helix of AFF4. The Tat-TAR recognition motif (TRM) in CycT1 interacts with both Tat and AFF4, exposing arginine side chains for TAR RNA binding. Structural modeling suggests AFF1 and AFF4 are preferred over AFF2/3 for interaction with Tat·P-TEFb. | PMID:24727379 | Cell cycle (Georgetown, Tex.) |
| 2015 | High | Gain-of-function missense mutations in AFF4 cause CHOPS syndrome. Transcriptome and ChIP-seq analyses demonstrated altered genome-wide binding of AFF4, cohesin, and RNAP2 in CHOPS and Cornelia de Lange syndrome (CdLS). Direct molecular interaction between the SEC, cohesin, and RNAP2 was demonstrated, functionally linking the super elongation complex and cohesin. | PMID:25730767 | Nature genetics |
| 2016 | High | Cryo-EM/integrative structure of the HIV-1 TAR-Tat-AFF4-CDK9-CycT1 complex at 5.9 Å resolution showed TAR central loop contacts the CycT1 TRM and the second Tat Zn2+-binding loop. HDX showed AFF4 helix 2 is stabilized in the TAR complex despite not touching RNA, explaining how AFF4 enhances TAR binding to the SEC 50-fold. The Tat ARM enters the TAR major groove between the bulge and central loop. | PMID:27731797 | eLife |
| 2017 | High | Crystal structure (2.0 Å) of ELL2 C-terminal domain bound to its 50-residue binding site on AFF4 (ELLBow) revealed ELL2 has an arch-shaped fold similar to tight junction protein occludin. The ELLBow consists of an N-terminal helix followed by an extended hairpin (elbow joint) occupying the concave surface of ELL2. The AFF4-ELL2 interface surface is important for ELL2 promotion of HIV-1 Tat-mediated proviral transcription. | PMID:28134250 | Nature communications |
| 2017 | Medium | AFF4 depletion in MSCs inhibits osteogenic differentiation (decreased ALP activity, mineralization, osteogenic gene expression), while AFF4 overexpression enhances it. AFF4 is enriched at the promoter region of ID1, and AFF4 knockdown blunts BMP2-induced BRE luciferase activity and SP7/ALP expression. | PMID:28955517 | Bone research |
| 2019 | High | X-ray crystal structure of AFF4 C-terminal homology domain (CHD) at 2.2 Å revealed a novel eight-helix domain distantly related to tetratricopeptide repeat motifs. AFF4-CHD mediates AFF4 homodimerization and AFF1-AFF4 heterodimerization. Fluorescence anisotropy experiments showed AFF4-CHD interacts with both RNA and DNA in vitro. A surface loop in AFF4-CHD was identified as a substrate for CDK9, which triggers release of Pol II from promoter-proximal pausing. | PMID:31147444 | The Journal of biological chemistry |
| 2020 | High | Crystal structure of AFF4-THD (TPRL with Handle Region Dimerization Domain) at 2.4 Å revealed the α4, α5, and α6 helices of one AFF4-THD mediate dimer formation packing against equivalent regions of the second molecule. Single mutations F1014A or Y1096A of AFF4 impair dimer formation. AFF4 dimerization is essential for transactivation of HIV-1 provirus but mutations of AFF1/4 dimerization residues have no effect on interaction with other SEC subunits. | PMID:32128251 | Cell discovery |
| 2007 | Medium | MCEF (AFF4) localizes exclusively to the nucleus. Three distinct protein sequences encoded by three separate exons mediate nuclear localization. Ectopic expression of MCEF represses HIV-1 LTR-directed RNA Pol II transcription at the level of Tat-transactivation. | PMID:17389929 | International journal of biological sciences |
| 2005 | High | AF5q31 (AFF4) knockout mice show male infertility with azoospermia due to arrest of spermiogenesis. AFF4 is preferentially expressed in Sertoli cells. Knockout mice display severely impaired expression of protamine 1, protamine 2, and transition protein 2 and increased apoptosis in seminiferous tubules, indicating AFF4 functions as a transcriptional regulator in testicular somatic cells essential for male germ cell differentiation. | PMID:16024815 | Molecular and cellular biology |
| 2012 | Medium | AFF4 expression in hypothalamic neurons is induced by ghrelin and fasting. AFF4 overexpression specifically induces AMPKα2 subunit expression and increases AMPKα2 promoter activity. AFF4 also increases phosphorylation of acetyl-CoA carboxylase α (ACCα) downstream of AMPK. Ghrelin-induced AMPKα2 expression and ACCα phosphorylation in the late phase of activation were attenuated by AFF4 siRNA knockdown. | PMID:22528490 | The Journal of biological chemistry |
| 2019 | Medium | FUS (fused in sarcoma) physically interacts with AFF4 in cells and forms nuclear punctuated condensates with AFF4, which are disrupted by aliphatic alcohol treatment. FUS inhibits activation of HIV transcription by AFF4 and ELL2. FUS depletion elevates occupancy of AFF4 and Cdk9 on the viral promoter, genome-wide FUS knockdown leads to increased AFF4 and Cdk9 occupancy on gene promoters, and FUS knockout delays HIV entry into latency. | PMID:31238957 | Retrovirology |
| 2019 | Medium | METTL3-mediated m6A modification directly targets AFF4 mRNA in bladder cancer cells. AFF4 binds to the MYC promoter and promotes MYC expression, operating as part of an AFF4/NF-κB/MYC signaling network downstream of METTL3-mediated m6A modification. | PMID:30659266 | Oncogene |
| 2020 | Medium | AFF4 regulates m6A-dependent expression and promotes SOX2 and MYC transcription in bladder cancer stem cells. AFF4 binds to promoter regions of SOX2 and MYC to sustain their transcription; AFF4 knockdown phenocopies METTL3 ablation and diminishes tumor-initiating capability in vivo. | PMID:32676121 | Stem cells international |
| 2022 | High | AFF4 regulates autophagy during adipogenesis by directly binding to autophagy-related proteins ATG5 and ATG16L1 and promoting their transcription. Adipose-specific Aff4 knockout mice have impaired adipocyte development and white fat depot formation. Depleting ATG5 or ATG16L1 abrogates adipogenesis in AFF4-overexpressing cells, while overexpression of ATG5/ATG16L1 rescues impaired adipogenesis in Aff4-knockout cells. | PMID:36149892 | PLoS genetics |
| 2024 | High | AFF4 and AFF1 function antagonistically at transcription start sites: AFF4 is enriched downstream of the TSS while AFF1 binds upstream. AFF4 disruption causes slow elongation and early termination in a subset of AFF4-bound active genes; AFF1 deletion leads to fast elongation and transcriptional readthrough in the same gene subset. AFF1 knockdown increases AFF4 levels at chromatin and vice versa. | PMID:37528066 | Journal of molecular cell biology |
| 2023 | Medium | AFF4 knockdown in HEL cells decreases cellular levels and global chromatin occupancy of CTD serine 2 phosphorylated Pol II. AFF4 promotes pause release likely by facilitating P-TEFb binding to Pol II. AFF4 loss increases promoter-proximal pause of Pol II on heat shock and thousands of non-heat shock genes. | PMID:37609817 | Yi chuan = Hereditas |
| 2025 | High | P70S6K phosphorylates AFF4 at S831 in an insulin-dependent manner, and this phosphorylation is attenuated in aged, insulin-resistant bone. Phosphorylation of S831 in AFF4 increases recruitment of chromatin remodelers ENL/AF9 to crotonylated histone via the YEATS domain, promoting gene-specific transcriptional elongation activation. In insulin-resistant osteoblasts, AFF4 S831 phosphorylation is defective and associated with reduced transcriptional elongation at discrete genomic locations. | PMID:41476161 | Nature communications |
| 2024 | Medium | MeCP2 directly binds AFF4 (the SEC scaffold) via the MeCP2 transcriptional repression domain. Loss of MeCP2 in mouse cortex reduces AFF4 binding at a subset of genes involved in synaptic function, which also show the strongest decrease in RNA Pol II genebody binding. MeCP2 physically interacts with the SEC in human cells and mouse brain. | — | bioRxiv |
| 2027 | Medium | AFF4 regulates NFIC transcription during odontogenic differentiation in dental pulp cells. AFF4 depletion decreases ALP activity and odontogenic gene expression; overexpression of NFIC rescues restricted differentiation in AFF4-depleted cells. | PMID:32139123 | Biochemical and biophysical research communications |
| 2014 | Medium | A cyclin T1 mutant (V107E) that cannot bind Hexim1 or CDK9 and cannot assemble on HIV TAR or 7SK snRNA retains strong binding to AFF4, demonstrating that AFF4 binding to CycT1 is mediated by a distinct surface from CDK9 and Hexim1 binding sites. This mutant enforces HIV transcription repression, demonstrating the functional importance of the AFF4-CycT1 interaction for transcription activation. | PMID:24985467 | Retrovirology |
| 2023 | Medium | AFF4 promotes expression of HPRT1 and IMPDH2 (nucleotide metabolism enzymes) in pancreatic ductal carcinoma cells. CDK9 mediates AFF4 phosphorylation at S388, which is required for PAX2-mediated recruitment of AFF4 to drive HPRT1 and IMPDH2 expression. Xenograft studies confirmed HPRT1 and IMPDH2 function genetically downstream of AFF4. | PMID:37063434 | International journal of biological sciences |

## Citations

- PMID:12065898
- PMID:16024815
- PMID:17389929
- PMID:20159561
- PMID:20471948
- PMID:22528490
- PMID:23251033
- PMID:23471103
- PMID:24727379
- PMID:24843025
- PMID:24985467
- PMID:25730767
- PMID:27731797
- PMID:28134250
- PMID:28955517
- PMID:30659266
- PMID:31147444
- PMID:31238957
- PMID:32128251
- PMID:32139123
- PMID:32676121
- PMID:36149892
- PMID:37063434
- PMID:37528066
- PMID:37609817
- PMID:41476161
