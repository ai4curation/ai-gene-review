---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BAZ2A
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9UIF9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 13
citation_count: 13
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for BAZ2A (human)

## Current model (mechanistic narrative)

BAZ2A (TIP5) is a multi-domain chromatin reader-scaffold that recruits the nucleolar remodeling machinery to genomic loci to enforce transcriptional repression and heterochromatin organization [PMID:25533489, PMID:33433018]. It engages chromatin through distinct modules: a PHD finger that reads unmodified H3 tails and a bromodomain that recognizes acetylated histones via a KacXXR motif, with both modules cooperating in trans-histone recognition required for recruitment and rDNA repression [PMID:25533489]. The bromodomain specifically binds H3K14ac (deposited by EP300) at inactive enhancers, and disrupting this interaction by point mutation or small-molecule inhibition impairs prostate cancer stem cell features and Pten-loss-driven transformation [PMID:34403195]. Its TAM domain adopts an MBD-like fold that binds double-stranded DNA and RNA in a sequence-nonspecific, backbone-dependent manner, and also serves as the nucleolar localization and nuclear matrix targeting module that drives large-scale rDNA chromatin compaction [PMID:25916849, PMID:34715126, PMID:23580549]. Through these interactions BAZ2A partners with SNF2H, TOP2A, cohesin and KDM1A to constrain chromatin accessibility at repressive (B) compartments and to silence enhancer-controlled genes via an RNA-dependent mechanism distinct from rDNA silencing [PMID:33433018, PMID:37184661]. BAZ2A additionally maintains repressive epigenetic states with EZH2 in metastasis-related genes and is required for the initiation of Pten-loss prostate oncogenesis [PMID:25485837, PMID:32024754].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0042393 histone binding, GO:0003677 DNA binding, GO:0003723 RNA binding, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005730 nucleolus, GO:0005694 chromosome, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-4839726 Chromatin organization, R-HSA-74160 Gene expression (Transcription), R-HSA-1643685 Disease
- **partners:** EZH2, SNF2H, TOP2A, KDM1A, TCF7L2, EP300
- **complexes:** NoRC

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | Medium | BAZ2A (TIP5) directly interacts with EZH2 to maintain epigenetic silencing at genes repressed in metastasis in prostate cancer cells. | PMID:25485837 | Nature genetics |
| 2014 | High | The PHD zinc finger domain of TIP5 recognizes unmodified H3 histone tails as an independent structural module, while the bromodomain preferentially binds H3 and H4 acetylation marks followed by a key basic residue (KacXXR motif); together these modules mediate trans-histone tail recognition required for NoRC recruitment to chromatin and transcriptional repression of rDNA. | PMID:25533489 | Structure (London, England : 1993) |
| 2015 | High | The TAM domain of TIP5 adopts an extended MBD-like fold with unique C-terminal extensions that form a novel RNA-binding surface; mutation of critical residues on this surface abolishes RNA binding both in vitro and in vivo, explaining how NoRC is targeted to specific genomic loci via noncoding RNA. | PMID:25916849 | Nucleic acids research |
| 2015 | High | GSK2801 acts as an acetyl-lysine competitive inhibitor of the BAZ2A bromodomain (KD ~257 nM for BAZ2A), binding in a canonical acetyl-lysine competitive mode as confirmed by crystal structure; cellular activity was demonstrated by FRAP showing displacement of GFP-BAZ2A from acetylated chromatin. | PMID:25799074 | Journal of medicinal chemistry |
| 2015 | High | BAZ2-ICR occupies the BAZ2A bromodomain acetyl-lysine pocket through an intramolecular aromatic stacking interaction that efficiently fills the shallow binding site, as revealed by structure-based design. | PMID:25719566 | Journal of medicinal chemistry |
| 2013 | Medium | The TAM domain of Tip5 functions as the nucleolar localization and nuclear matrix targeting module, while AT-hooks are required for nucleolar targeting but do not mediate nuclear matrix association; Tip5 overexpression facilitates rDNA association with the nuclear matrix and increases DNase I inaccessibility, regulating large-scale rDNA chromatin organization. | PMID:23580549 | Nucleic acids research |
| 2013 | Medium | NuRD complex directly binds to the TIP5 promoter and negatively regulates TIP5 expression, thereby limiting TIP5-mediated recruitment of DNA methyltransferase to rDNA promoters and maintaining their unmethylated state. | PMID:23796711 | Biochemical and biophysical research communications |
| 2018 | Medium | TIP5 physically interacts with TCF7L2 (identified by co-immunoprecipitation and GST pull-down) and enhances the interaction between β-catenin and TCF7L2, thereby activating Wnt/β-catenin signaling in hepatocellular carcinoma cells. | PMID:29620186 | Molecular medicine reports |
| 2020 | High | In ground-state embryonic stem cells, BAZ2A interacts with SNF2H, DNA topoisomerase 2A (TOP2A), and cohesin on chromatin; BAZ2A depletion increases chromatin accessibility at B compartments and dysregulates H3K27me3 genome occupancy in a TOP2A-dependent manner, demonstrating that BAZ2A limits invasion of active chromatin domains into repressive compartments. | PMID:33433018 | The EMBO journal |
| 2021 | High | BAZ2A bromodomain specifically binds H3K14ac-marked chromatin at inactive enhancers; BAZ2A-BRD mutations or pharmacological inhibition of the BAZ2A-BRD/H3K14ac interaction impairs prostate cancer stem cell features and Pten-loss-driven oncogenic transformation in organoids. BAZ2A-mediated repression at these enhancers is linked to EP300, which acetylates H3K14. | PMID:34403195 | EMBO reports |
| 2021 | High | The BAZ2A TAM domain binds double-stranded DNA and double-stranded RNA in a sequence-nonspecific, backbone-dependent manner (distinct from canonical MBD methyl-CpG recognition), as established by EMSA, ITC, mutagenesis, and X-ray crystallography. | PMID:34715126 | The Journal of biological chemistry |
| 2023 | Medium | In prostate cancer, the BAZ2A TAM domain mediates interaction with TOP2A and KDM1A through an RNA-dependent mechanism; pharmacological inhibition of TOP2A or KDM1A upregulates BAZ2A-repressed genes controlled by inactive enhancers, whereas rRNA gene silencing is unaffected, revealing a distinct RNA-based gene repression mechanism separate from rDNA silencing. | PMID:37184661 | Life science alliance |
| 2020 | Medium | TIP5 is required for the initiation of prostate cancer transformation of luminal cells driven by Pten-loss in organoids, but is dispensable once transformation is established, placing TIP5 upstream of Pten-loss-mediated oncogenesis in a defined cellular context. | PMID:32024754 | Proceedings of the National Academy of Sciences of the United States of America |

## Citations

- PMID:23580549
- PMID:23796711
- PMID:25485837
- PMID:25533489
- PMID:25719566
- PMID:25799074
- PMID:25916849
- PMID:29620186
- PMID:32024754
- PMID:33433018
- PMID:34403195
- PMID:34715126
- PMID:37184661
