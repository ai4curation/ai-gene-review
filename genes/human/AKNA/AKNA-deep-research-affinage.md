---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AKNA
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q7Z591
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AKNA (human)

## Current model (mechanistic narrative)

AKNA is a dual-function AT-hook protein acting both as a sequence-specific transcription factor and as a centrosomal microtubule organizer [PMID:11268217, PMID:30787442]. As a transcription factor it directly binds A/T-rich regulatory elements in target promoters, originally defined for the coordinate regulation of CD40 and CD40 ligand, and genome-wide it engages AT-rich response elements in over a thousand promoters in activated T cells where it induces IL-2 and CD80 [PMID:11268217, PMID:36835622]. Depending on context it acts as an activator or a repressor: AKNA loss in mice de-represses broad inflammatory gene networks (IL-1β, IFN-γ, MMP9, S100A8/9, neutrophil chemoattractants), producing neutrophil-driven alveolar destruction and neonatal lethality [PMID:21606955]. AKNA carries multiple PEST motifs and is subject to high-turnover proteolytic processing, undergoing PEST-dependent cleavage to p50 in mature B cells in a manner linked to CD40 upregulation [PMID:11268217, PMID:15869410]. Its abundance is set by upstream signaling and protein-interaction inputs: phospho-CREB and phospho-p65 bind the AKNA promoter to suppress its transcription downstream of PKA/CREB and NF-κB, while the HPV E6 oncoprotein binds AKNA and drives its proteasomal degradation and p53 binds AKNA and promotes its expression [PMID:29079362, PMID:30562965]. Independently of transcription, AKNA localizes to the subdistal appendages of the mother centriole in neural stem cells and basal progenitors, where it is necessary and sufficient to organize centrosomal microtubule nucleation and growth, a function required for epithelial delamination, progenitor movement, and epithelial-to-mesenchymal transition [PMID:30787442].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003677 DNA binding, GO:0140110 transcription regulator activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005634 nucleus, GO:0005815 microtubule organizing center, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-168256 Immune System, R-HSA-1266738 Developmental Biology
- **partners:** KDM6B, TP53, HPV E6
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | High | AKNA is an AT-hook transcription factor that directly binds A/T-rich regulatory elements in the promoters of CD40 and CD40 ligand (CD40L), coordinately regulating their expression. AKNA localizes to the nucleus and contains multiple PEST protein-cleavage motifs consistent with high turnover. | PMID:11268217 | Nature |
| 2005 | Medium | AKNA undergoes PEST-dependent cleavage into p50 polypeptides specifically in mature B cells, and this cleavage appears to be required for CD40 upregulation. AKNA is encoded by a single gene producing at least nine distinct transcripts via alternative splicing, differential polyadenylation, and promoter usage, yielding detectable protein isoforms p70 and p100. | PMID:15869410 | DNA and cell biology |
| 2011 | High | AKNA acts as a transcriptional repressor of inflammatory gene networks. In AKNA knockout mice, loss of AKNA activates broad inflammatory gene networks including IL-1β, IFN-γ, MMP9, S100A8/9, and neutrophil chemoattractants, leading to neutrophil-dominated alveolar destruction and neonatal death. Promoter/reporter experiments confirmed AKNA can act as a gene repressor. | PMID:21606955 | Cell research |
| 2019 | High | AKNA localizes specifically to the subdistal appendages of the mother centriole in neural stem cells and in basal progenitors. At this location, AKNA is necessary and sufficient to organize centrosomal microtubules, promoting their nucleation and growth. This centrosomal microtubule organization function is required for epithelial delamination (entry into the subventricular zone) and for exit from the subventricular zone, and also regulates epithelial-to-mesenchymal transition in other epithelial cell types. | PMID:30787442 | Nature |
| 2017 | Medium | AKNA expression is regulated downstream of PKA/CREB and NF-κB signaling pathways: T-2 toxin activates these pathways, causing phospho-CREB and phospho-p65 to directly bind the AKNA promoter and inhibit AKNA transcription. AKNA in turn regulates expression of GH and inflammatory cytokines (TNF-α, IL-1β, IL-6) in pituitary GH3 cells. | PMID:29079362 | Toxicology |
| 2018 | Medium | HPV E6 oncoprotein interacts with AKNA and downregulates AKNA protein in a proteasome-dependent manner, leading to reduced CD40 expression. Additionally, p53 physically interacts with AKNA and promotes AKNA expression, placing AKNA in the E6/p53/AKNA regulatory axis. | PMID:30562965 | Cancers |
| 2025 | Medium | AKNA localizes at the basal foot of ciliary basal bodies in human airway multiciliated cells, together with γ-TuRC, NEDD1, Augmin/HAUS, and ninein, as part of the microtubule-organizing center responsible for dense apical microtubule arrays. This localization was mapped using expansion microscopy volumetric averaging. | — | bioRxiv |
| 2025 | Medium | In neuroblastoma cells, AKNA is predominantly nuclear during induction of pluripotency where it promotes stemness; knockdown of AKNA reduces stemness even in presence of OCT4 and SOX2. During differentiation induction, AKNA relocalizes to the cytosol (driven by FAK signaling). In the nucleus, AKNA physically interacts with the demethylase KDM6B to promote H3K27me3 demethylation, and subsequently promotes CBP/p300-mediated H3K27ac deposition on promoters of target genes, activating their transcription. | — | bioRxiv |
| 2023 | Medium | ChIP-seq and microarray analysis identified five AT-rich motifs as potential AKNA response elements found in promoters of over a thousand genes in activated T-cells. Functional validation by RT-qPCR demonstrated that AKNA induces expression of IL-2 and CD80 in T-cell activation. | PMID:36835622 | International journal of molecular sciences |

## Citations

- PMID:11268217
- PMID:15869410
- PMID:21606955
- PMID:29079362
- PMID:30562965
- PMID:30787442
- PMID:36835622
