---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/TOP2B
affinage_run_date: 2026-06-10T10:51:55
uniprot_accession: Q02880
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

# Affinage mechanistic annotation for TOP2B (human)

## Current model (mechanistic narrative)

TOP2B is an ATP-dependent type II DNA topoisomerase that generates transient, controlled double-strand breaks (DSBs) to resolve transcription-associated DNA supercoiling and drive signal-induced transcriptional programs [PMID:20601956, PMID:21228215]. It is co-recruited with nuclear receptors and their cofactors to target promoters and enhancers: with androgen receptor at TMPRSS2-ERG breakpoints, where its recombinogenic DSBs generate fusion transcripts [PMID:20601956], and with PARP1 to glucocorticoid receptor target promoters via the BRG1/SWI/SNF complex and Ku70/86, where transient DSBs are required for efficient hormone-stimulated transcription [PMID:26055322]. Its catalytic engagement, not mere binding, determines transcriptional output: TOP2B activity at promoters, enhancers, and introns controls expression of oncogenes such as PDGFRA and MYC [PMID:34433651], drives ATRA-induced and long-gene transcriptional programs [PMID:35831557], and underlies activity-dependent early-response gene induction in neurons [PMID:30930055, PMID:bio_10.1101_2025.05.06.652469]. TOP2B catalytic activity is tightly regulated — directly inhibited by PARP1/PARP2 and PAR modification during spermiogenesis [PMID:21228215], suppressed at estrogen-responsive elements through an ERα/ZATT/non-catalytic TOP2A axis that builds negative supercoiling to enable regulatory chromatin contacts [PMID:41296866], and positively favored in gene bodies marked by H3K36me3 [PMID:38377005]. TOP2B also shapes 3D genome organization, cooperating with XPF in R-loop processing and with CTCF, cohesin (PDS5A, RAD21), and the nuclear lamina to maintain chromatin looping and LAD/iLAD partitioning [PMID:37939182, PMID:41959374]. Under genotoxic stress from TOP2 poisons, ATM and CK1 phosphorylate TOP2B within a degron to trigger SCFβ-TrCP-mediated proteasomal degradation [PMID:32015321], and TOP2B is the principal cellular target of the clinical agent CX-5461 [PMID:34753908]. TOP2B is further required for tissue-specific genome integrity and differentiation in ovarian granulosa cells and photoreceptors [PMID:24002654, PMID:28370415].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140097 catalytic activity, acting on DNA, GO:0140657 ATP-dependent activity, GO:0003677 DNA binding, GO:0140110 transcription regulator activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005635 nuclear envelope
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-73894 DNA Repair, R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** PARP1, XPF, CTCF, PDS5A, ATRX, ZATT, TOP2A, BRG1
- **complexes:** BRG1/SWI/SNF complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | Androgen receptor and TOP2B are co-recruited to TMPRSS2-ERG genomic breakpoints upon androgen stimulation, triggering recombinogenic TOP2B-mediated DNA double-strand breaks (DSBs) that generate TMPRSS2-ERG fusion transcripts; this process requires both TOP2B and components of the DSB repair machinery. | PMID:20601956 | Nature genetics |
| 2015 | High | TOP2B (topoisomerase IIβ), together with PARP1, is recruited to nuclear receptor target gene promoters through the BRG1/SWI/SNF complex via a direct interaction between Ku70/86 and the HSA/BRK domains of BRG1; transient TOP2B-mediated DSBs at these promoters are required for efficient glucocorticoid receptor (GR)-stimulated transcription. | PMID:26055322 | Molecular and cellular biology |
| 2011 | High | PARP1 and PARP2 directly inhibit TOP2B activity in vitro; poly(ADP-ribose) (PAR) modification suppresses TOP2B-mediated DNA strand breaks in elongating spermatids, and this inhibition is reversed by PAR glycohydrolase, establishing a regulatory cycle that coordinates TOP2B-dependent DNA relaxation with histone-to-protamine exchange during spermiogenesis. | PMID:21228215 | Biology of reproduction |
| 2020 | High | In response to TOP2 poison (teniposide/VM-26), ATM kinase and CK1 cooperatively phosphorylate TOP2B on Ser1134 and Ser1130 within a canonical degron motif, enabling β-TrCP binding and SCFβ-TrCP-mediated ubiquitin-proteasomal degradation of TOP2B; blocking this degradation impairs DNA damage repair and accelerates apoptosis. | PMID:32015321 | Oncogenesis |
| 2021 | High | CX-5461, previously classified as an RNA Pol I inhibitor, acts primarily as a TOP2B poison at pharmacologically relevant concentrations; comprehensive in vitro and in vivo assays demonstrated its primary target is TOP2B rather than RNA Pol I, with implications for therapy-induced leukemia and cardiotoxicity. | PMID:34753908 | Nature communications |
| 2013 | High | TOP2B is required for DNA integrity in granulosa cells (GCs) of growing ovarian follicles; GC-specific deletion of Top2b using Cyp19-Cre in mice causes DNA damage accumulation, follicle atresia, decreased ovulation, and hypersensitivity to genotoxic chemotherapeutic drugs. | PMID:24002654 | Molecular endocrinology |
| 2019 | High | Endogenous TOP2B-mediated DNA double-strand breaks (TOP2βcc intermediates) in neurons are required for NGF-dependent AKT-mTORC1 signaling and maintenance of HSV-1 latency; suppression of DNA repair pathways that remove TOP2βcc triggers HSV-1 reactivation, linking TOP2B catalytic activity to AKT signaling dynamics. | PMID:30930055 | Molecular cell |
| 2023 | High | XPF physically interacts with TOP2B and recruits it to active gene promoters; TOP2B is required for XPF-dependent R-loop processing, leading to DSB accumulation and DNA damage response activation at active promoters. Abrogation of TOP2B diminishes recruitment of XPF, CTCF, and cohesin subunits to promoters and impairs CTCF-mediated DNA looping. | PMID:37939182 | Science advances |
| 2024 | High | Genome-wide mapping of catalytically engaged TOP2B (trapped as covalent cleavage complexes) in cortical neurons shows that TOP2Bcc distribution is influenced by nucleosome organization and compartmental chromosome architecture; H3K36me3 positively regulates TOP2B catalytic engagement in gene bodies, while high RNA Pol II occupancy at active promoters correlates with reduced TOP2Bccs; poisoning or inhibiting TOP2B increases nascent transcription at most genes but reduces transcription within long genes via effects on intragenic enhancers. | PMID:38377005 | Cell reports |
| 2024 | High | Estrogen-mediated inhibition of TOP2B catalytic activity (but not binding) at estrogen-responsive enhancers and promoters depends on estrogen receptor α (ERα), a non-catalytic function of TOP2A, and the SUMO-ligase ZATT; this inhibition causes accumulation of negative DNA supercoiling and promotes formation of regulatory chromatin contacts required for the estrogen transcriptional response. | PMID:41296866 | Science advances |
| 2019 | Medium | NMDA receptor activation induces TOP2B-dependent DNA double-strand breaks in glioblastoma cells, and TOP2B activity is required downstream of NMDAR signaling for expression of the proto-oncogene cFos; siRNA knockdown of TOP2B reduced cFos expression and increased radiosensitivity. | PMID:30841565 | Cancers |
| 2017 | Medium | TOP2B cell-autonomously controls the expression of key photoreceptor transcription factors and retinopathy-related genes (e.g., Crx, Nr2e3, Opn1sw, Abca4, Bbs7, Pde6b) during late-stage photoreceptor differentiation, and its loss causes defective outer segment formation without immediate dramatic cell loss. | PMID:28370415 | Journal of neuroscience research |
| 2021 | Medium | TOP2B regulates transcription of multiple oncogenes in gliomas (including PDGFRA and MYC) specifically at genomic sites where it is catalytically active (in promoters, enhancers, and introns), not merely at all binding sites; TOP2B activity correlates with chromatin accessibility at these sites. | PMID:34433651 | Clinical cancer research |
| 2024 | Medium | DNA-PKcs directly binds the TOP2B promoter upstream region and acts as a transcriptional repressor of TOP2B expression in anthracycline-resistant AML cells; GCN5 (KAT2A) mediates transcriptional upregulation of DNA-PKcs in AML relapse, establishing a GCN5-DNA-PKcs-TOP2B transcriptional regulatory axis underlying anthracycline resistance. | PMID:38240344 | Journal of cell science |
| 2022 | Medium | TOP2B is required for ATRA-induced transcriptional activation of many rapidly induced genes in SH-SY5Y neuroblastoma cells (including BCL2, CYP26A1, CRABP2, NTRK2); long genes and highly expressed genes are disproportionately dependent on TOP2B; loss of TOP2B causes upregulation of mesenchymal markers and NOTCH signaling, shifting cells from adrenergic to mesenchymal transcriptional state. | PMID:35831557 | Molecular neurobiology |
| 2025 | Medium | TOP2B cooperates with ATRX to resolve G-quadruplex (G4) structures during DNA replication; CX-5461 acts as a TOP2B poison that selectively impairs TOP2B binding at G4 sites, leading to G4 accumulation, replication fork stalling, and MRE11-dependent degradation of stalled forks, with enhanced effects in ATRX-deficient glioma cells. | PMID:40990248 | Nucleic acids research |
| 2025 | Medium | During vaccinia virus infection, early viral protein synthesis induces cytoplasmic relocalization of TOP2B; TOP2B is recruited to cytoplasmic viral factories through interaction of its C-terminal domain with the viral ligase A50; in the cytoplasm, TOP2B suppresses viral replication by enhancing formation of double-stranded RNA and antiviral granules containing tRNA splicing ligase components. | PMID:bio_10.1101_2025.02.05.636656 | bioRxiv |
| 2025 | Medium | TOP2B-mediated DSBs within promoters of early response genes (Fos, Npas4) in neurons are sufficient to recapitulate enhancer-promoter contact profiles observed after neuronal stimulation; repeated DSB cycles progressively potentiate ERG induction (transcriptional memory effect) and are associated with loss of cis chromosome interactions and gain of trans interactions at ERG promoters. | PMID:bio_10.1101_2025.05.06.652469 | bioRxiv |
| 2024 | Medium | TOP2B binds predominantly to inter-LAD (iLAD) chromatin and its depletion results in partial loss of genome partitioning between LADs and iLADs; TOP2B depletion preferentially disrupts genome interactions with lamin B receptor (LBR) over lamins; co-depletion of TOP2B and LBR causes partial LAD/iLAD inversion resembling oncogene-induced senescence, supporting a coordinated TOP2B(iLAD)/LBR(LAD) axis for nuclear lamina organization. | PMID:bio_10.1101_2024.10.01.616012 | bioRxiv |
| 2002 | Medium | TOP2B promoter activity is constant throughout the cell cycle and requires direct binding of NF-Y transcription factor to two inverted CCAAT boxes (ICBs) in the region -533 to -481 upstream; an Sp1-binding GC box just upstream of the ICBs synergistically contributes to promoter activity; dominant-negative NF-Y subunit A ablates promoter activity. | PMID:12197834 | The Biochemical journal |
| 2025 | Medium | UTX (KDM6A) directly binds the TOP2β (Top2b) promoter and acts as a transcriptional repressor; UTX deletion in spinal cord microvascular endothelial cells upregulates Top2β, reduces cellular senescence, and promotes proliferation/angiogenesis after spinal cord injury; knockdown of Top2β reverses the anti-senescence effects of UTX deletion. | PMID:41385502 | PloS one |
| 2015 | Medium | TOP2B occupancy across the human genome (ChIP-seq in MCF7 cells) shows enrichment at gene promoters and within 5 kb of transcription start sites; TOP2B peaks coincide with binding motifs for SP1, KLF4, TFAP2A, CTCF, ESR1/ESR2, and REST; genes associated with TOP2B peaks are enriched for neuronal development and axon guidance ontology terms. | PMID:26459242 | Biology open |
| 2025 | Medium | PDS5A (a regulatory cohesin subunit) and TOP2B cooperate for their mutual recruitment to CTCF-bound chromatin; catalytically active TOP2B increases PDS5A occupancy genome-wide; a novel PDS5A-CTCF interaction region (CTCF N-terminal residues 95-116) is required for CTCF-PDS5A-TOP2B interaction in vitro and for TOP2B-mediated enrichment of PDS5A in vivo; loss of this interaction reduces chromatin loop number. | PMID:41959374 | bioRxiv |
| 2025 | Medium | PNU142586, a primary metabolite of linezolid, targets TOP2B (and TOP2A) by impeding DNA binding to TOP2B in a conformation favorable for cleavage and by inhibiting ATP hydrolysis; these biochemical effects cause disruption of transcription and antiproliferative/cytotoxic outcomes including mitochondrial dysfunction. | PMID:40435237 | Science advances |

## Citations

- PMID:12197834
- PMID:20601956
- PMID:21228215
- PMID:24002654
- PMID:26055322
- PMID:26459242
- PMID:28370415
- PMID:30841565
- PMID:30930055
- PMID:32015321
- PMID:34433651
- PMID:34753908
- PMID:35831557
- PMID:37939182
- PMID:38240344
- PMID:38377005
- PMID:40435237
- PMID:40990248
- PMID:41296866
- PMID:41385502
- PMID:41959374
- PMID:bio_10.1101_2024.10.01.616012
- PMID:bio_10.1101_2025.02.05.636656
- PMID:bio_10.1101_2025.05.06.652469
