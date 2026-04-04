# MicroRNA Degradation Project Sources

This file tracks the seed papers that define project scope. It is intentionally smaller than a full
literature review. New papers from Chris should be appended here first, and only then used to widen
the review queue.

## P0: Anchor Mechanism

| Source | Why it matters now | Current effect on scope |
|--------|--------------------|-------------------------|
| [Farnung et al. 2026, "The E3 ubiquitin ligase mechanism specifying targeted microRNA degradation" (Nature)](https://www.nature.com/articles/s41586-026-10232-0) | Direct biochemical and cryo-EM mechanism for trigger-dependent AGO recognition by the ZSWIM8-CUL3 ligase with ELOB, ELOC, and ARIH1 | Defines the phase-1 queue as a TDMD machinery project, not a generic miRNA turnover project |
| [Shi et al. 2020, "The ZSWIM8 ubiquitin ligase mediates target-directed microRNA degradation" (Science)](https://pubmed.ncbi.nlm.nih.gov/33184237/) | Establishes ZSWIM8 ligase requirement for TDMD and expands the biological relevance across mammals, flies, and nematodes | Justifies ZSWIM8 as the central project anchor |
| [Han et al. 2020, "A ubiquitin ligase mediates target-directed microRNA decay independently of tailing and trimming" (Science)](https://pubmed.ncbi.nlm.nih.gov/33184234/) | Independent TDMD mechanism paper showing that ZSWIM8-dependent decay does not require tailing and trimming to be the core explanation | Keeps TUT and trimming pathways out of phase-1 core scope |

## P1: Endogenous Trigger Biology

| Source | Why it matters now | Current effect on scope |
|--------|--------------------|-------------------------|
| [Kleaveland et al. 2018, "A Network of Noncoding Regulatory RNAs Acts in the Mammalian Brain" (Cell)](https://pubmed.ncbi.nlm.nih.gov/29887379/) | Canonical endogenous CYRANO-miR-7 example linking TDMD to mammalian brain biology | Track CYRANO as context, but do not add ncRNA jobs to the phase-1 queue |
| [Bitetti et al. 2018, "MicroRNA degradation by a conserved target RNA regulates animal behavior" (Nature Structural & Molecular Biology)](https://pubmed.ncbi.nlm.nih.gov/29483647/) | NREP example with in vivo phenotype; useful for distinguishing validated endogenous trigger biology from speculative trigger predictions | Track NREP as context and later regulator-focused expansion |
| [Ghini et al. 2018, "Endogenous transcripts control miRNA levels and activity in mammalian cells by target-directed miRNA degradation" (Nature Communications)](https://www.nature.com/articles/s41467-018-05182-9) | SERPINE1 establishes an endogenous protein-coding trigger transcript in mammalian cells | Supports a separate "trigger-bearing transcript" context list without turning those genes into phase-1 review jobs |
| [Li et al. 2023, "Screening of Drosophila microRNA-degradation sequences reveals Argonaute1 mRNA's role in regulating miR-999" (Nature Communications)](https://www.nature.com/articles/s41467-023-37819-9) | Useful comparative Drosophila example and a reminder that trigger-bearing transcripts can be physiologically important | Comparative layer, not part of the initial human queue |
| [Lin et al. 2026, "mRNA 3' UTRs direct microRNA degradation to participate in imprinted gene networks and regulate growth" (Genes & Development)](https://pubmed.ncbi.nlm.nih.gov/41871909/) | Expands the validated mouse trigger list to ATP6V1G1, LPAR4, PLAGL1, and LRRC58 | Track these genes as regulators/context only unless a later subproject is explicitly about trigger-bearing transcripts |

## P2: Deferred Expansion

| Source | Why it matters now | Current effect on scope |
|--------|--------------------|-------------------------|
| [Yang et al. 2020, "AGO-bound mature miRNAs are oligouridylated by TUTs and subsequently degraded by DIS3L2" (Nature Communications)](https://www.nature.com/articles/s41467-020-16533-w) | Strong evidence for a miRNA turnover branch involving tailing and DIS3L2 | Keep this branch as phase-2 expansion rather than mixing it into the phase-1 TDMD machinery queue |

## Intake Rule

- If a new paper directly changes the identity of the dedicated TDMD machinery, update `genes.csv` and `fetch_queue.csv`.
- If a new paper adds trigger RNAs or trigger-bearing transcripts, update this file and the context-regulator section of `MIRNA_DEGRADATION.md` first.
- Do not widen the review queue just because a gene's transcript contains a TDMD trigger site.
