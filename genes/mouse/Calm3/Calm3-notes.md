# Calm3 (Mouse) — Research Notes

## Overview

Mouse Calm3 (UniProt: P0DP28) encodes calmodulin-3, one of three mouse calmodulin genes (Calm1, Calm2, Calm3) that all produce an **identical 149 aa, ~17 kDa protein** [Hussey et al. 2023, *Channels* PMID:36692125]. The proteins differ only at the locus level (noncoding regulatory regions, transcript isoforms, expression timing/location). This makes ISO transfers from human CALM1/CALM2/CALM3 biochemically valid at the protein level, but means Calm3-specific biology must be sought at the regulatory/post-transcriptional level.

## Core Protein Function (shared across all three CaM genes)

Calmodulin is a ubiquitous intracellular **Ca2+ sensor** that transduces cytosolic Ca2+ changes into altered target protein activity [Sobue 2024, *Proc Jpn Acad Ser B* https://doi.org/10.2183/pjab.100.025]. It has >300 target proteins.

- **Structure**: Two globular lobes (N and C), each with two EF-hand Ca2+-binding motifs (4 total). Connected by flexible linker.
- **Ca2+ affinities**: C-lobe KD ~2.4 µM (higher affinity), N-lobe KD ~16 µM — allows differential decoding of Ca2+ signals.
- **Target recognition**: Methionine-rich hydrophobic surfaces (Met51, Met71, Met72; C-lobe: Met124, Met144, Met145) engage target CaM-binding motifs with hydrophobic anchors spaced 10–17 residues apart (motif classes 1-10, 1-14, 1-16, 1-17) [Denesyuk et al. 2023, *J Biomol Struct Dyn* https://doi.org/10.1080/07391102.2022.2123391].

### Key downstream targets/pathways (all three CaM genes contribute):
- CaMKI/II/III/IV kinases (CaMKII especially abundant in forebrain postsynapses)
- Calcineurin → NFAT signaling
- CaV1.2 (L-type Ca2+ channels) — Ca2+-dependent inactivation (CDI)
- RyR2, IP3 receptors — intracellular Ca2+ release channels
- SK/IK channels — small conductance Ca2+-activated K+ channels
- Gap junction gating via connexins (Ca2+-CaM "cork" mechanism, connexin CL2 peptide KD ~0.7–1 µM) [Peracchia 2024, *Int J Mol Sci* https://doi.org/10.3390/ijms25189789]
- TRPM2, TRPM3, TRPM4, TRPM6 channels [Bousova et al. 2023, *Int J Mol Sci* https://doi.org/10.3390/ijms242015162]

## Calm3-Specific Biology: Dendritic mRNA Localization

The most important and well-established Calm3-specific finding is at the **RNA level**, not the protein level.

**Sharangdhar et al. 2017 EMBO Rep** [PMID:28765142, https://doi.org/10.15252/embr.201744334]:

- Performed Staufen2 (Stau2) iCLIP on E18 mouse brain. Stau2 is a dsRNA-binding protein that localizes mRNAs to neuronal dendrites.
- Identified 356 neuronal mRNAs with Stau2 binding in 3'-UTRs; 28 (7.9%) had binding in retained 3'-UTR introns.
- **Calm3 was the top Stau2 iCLIP target in this class**, accounting for **0.24% of all mRNA iCLIP tags** — a striking enrichment.
- The long Calm3 isoform (**Calm3L**) has a **retained intron in its 3'-UTR** with **six Stau2 crosslink clusters**, four of which are within the retained intron.
- **Calm1 and Calm2 lacked Stau2 crosslink clusters entirely** in this analysis — this is the key paralog-specific distinction.
- Functionally: Calm3L (with intron) localized to MAP2-positive dendrites; intron removal impaired dendritic localization.
- Stau2 knockdown reduced dendritic localization and increased nuclear retention WITHOUT changing total Calm3L abundance (regulation of localization, not stability).
- **NMDA receptor activation** specifically promoted Calm3L dendritic localization; synaptic silencing reduced it.

**Interpretation**: Calm3 may contribute to spatially restricted CaM availability in dendrites via local translation, tuning synaptic Ca2+ signaling in an activity-dependent manner.

## Calyx of Held / Presynaptic Endocytosis — Attribution Issue

PMID:31628181 (Jin et al. 2019, *J Neurosci*) is cited for IMP/NAS annotations on Calm3 for calyx of Held synaptic vesicle endocytosis. However, this paper explicitly used **Calm2 KO mice**, not Calm3 KO. The annotations on Calm3 (P0DP28) are made by protein identity (all three CaM proteins are identical), not by direct Calm3 genetic manipulation. This was flagged in the review — presynaptic annotations were kept as KEEP_AS_NON_CORE with explanation.

## ISO Transfer Context

Mouse Calm3 receives ISO annotations from two sources:
1. **GO_REF:0000119** (mouse-human ortholog pipeline) — transfers from human CALM1 (UniProtKB:P0DP25)
2. **GO_REF:0000096** (mouse-rat ortholog pipeline) — transfers from rat calmodulins (RGD:2257, 2258, 2259)

Since all calmodulin proteins are 100% identical across paralogs and orthologs, ISO transfers are biochemically valid. The review question shifts to whether they add paralog-specific signal. Most ISO terms on Calm3 represent legitimate calmodulin biology and were ACCEPTED or KEEP_AS_NON_CORE based on whether they represent core vs. peripheral functions.

## Therapeutic and Clinical Relevance

- CALM3 mutations (e.g., D130G, F142L) cause **calmodulinopathy** — severe LQT syndrome and catecholaminergic polymorphic ventricular tachycardia (CPVT) [Reed et al. 2015, *Heart Rhythm* https://doi.org/10.1016/j.hrthm.2014.10.035].
- **Gene-selective ASO therapy** (2024): CALM1-selective ASOs can reduce a mutant CALM1 allele without depleting total CaM protein (compensated by CALM2/CALM3), demonstrating that gene-selective knockdown is feasible while protein levels remain stable [Bortolin et al. 2024, *Circulation* https://doi.org/10.1161/circulationaha.123.068111].
  - Lead ASOs: IC50 < 500 nM; ~50% CALM1 depletion at 5 µM without changing total CaM protein.
  - Normalized prolonged repolarization in CALM1^F142L/+ iPSC-cardiomyocytes.
  - >85% in vitro reduction with top murine ASOs.

## Key Quantitative Data Points

| Measurement | Value | Source |
|---|---|---|
| Calm3 iCLIP fraction | 0.24% of all mRNA tags | Sharangdhar 2017 |
| Stau2 crosslink clusters in Calm3L 3'-UTR | 6 total, 4 in retained intron | Sharangdhar 2017 |
| CaM C-lobe Ca2+ affinity | KD ~2.4 µM | Hussey 2023 |
| CaM N-lobe Ca2+ affinity | KD ~16 µM | Hussey 2023 |
| Connexin peptide–CaM KD | ~0.7–1 µM | Peracchia 2024 |
| Gap junction conductance reduction (ionomycin) | 95% (blocked by CaM inhibitor) | Peracchia 2024 |
| ASO IC50 (CALM1-selective) | < 500 nM | Bortolin 2024 |

## Literature Gaps and Open Questions

1. No **Calm3-specific knockout** phenotype described in mouse — all functional data uses generic CaM depletion or Calm2 KO.
2. Is Calm3L dendritic localization functionally significant for synaptic plasticity? LTP/LTD experiments with Calm3L-specific disruption not yet done.
3. Does Calm3 preferentially localize to postsynaptic densities vs. presynaptic terminals compared to Calm1/Calm2?
4. What is the relative contribution of Calm3 vs. Calm1/Calm2 to total synaptic CaM pool?
5. Are there other brain regions or cell types where Calm3 mRNA regulation differs from paralogs?
