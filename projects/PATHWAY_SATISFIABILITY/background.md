---
title: "Pathway satisfiability — background: pathway hole filling"
maturity: IN_PROGRESS
tags: [PIPELINE]
autolink_gene_symbols: false
---

# Background: the pathway-hole-filling landscape

Companion to [Pathway satisfiability](../PATHWAY_SATISFIABILITY.md). This page situates the
project against ~20 years of prior art on *pathway holes* — the question "a pathway looks like
it should run, but a step has no gene assigned; what is going on, and which gene fills it?"
The short version: the field is mature for **microbial genomes**, where the discriminating
variable is gene *presence/absence*, and essentially silent on the **metazoan** version of the
question, where the genome is constant and the discriminating variable is *which isozyme is
expressed in which context*. That gap is what this project targets.

The term **"pathway hole"** itself comes from SRI's Pathway Tools (Karp lab): a hole is a
reaction in an inferred pathway for which no enzyme in the organism has been assigned.

## Three families of prior work

The literature clusters into three problems that are often conflated but are actually
distinct.

### 1. Step-finding: does the genome encode this pathway? (presence/absence)

Given a genome and a pathway written as a set of required steps (often with alternative
routes), decide whether every step has a plausible gene. This is the family closest to what
this project does — the difference is the *oracle*.

- **GapMind** (Price, Deutschbauer & Arkin, *GapMind: Automated Annotation of Amino Acid
  Biosynthesis*, mSystems 2020, PMID:32576650; carbon-catabolism and 2024 updates followed).
  A pathway is a set of **steps**, and each step can be satisfied by any of several
  **alternative rules / variant routes** (e.g. succinyl- vs acetyl-acylation, trans-sulfuration
  vs direct sulfhydrylation for methionine). Candidate genes for a step come from similarity to
  a curated set of **experimentally characterized** proteins, with explicit handling of fusion
  and split proteins, and links out to Curated BLAST to catch frameshifts, un-annotated ORFs,
  and highly diverged (<30% id) candidates a best-hit annotation would miss. GapMind reports,
  per genome, which route is encoded and which step is the **gap**. **This project is
  explicitly the eukaryotic analogue of GapMind** — same "module = steps with OR-branches,
  evaluate against an oracle, report the gate/gap" shape, but the oracle is tissue/zone
  expression rather than genome gene-content.

- **KEGG module completeness / KAAS / KEGG Mapper.** KEGG Modules encode pathways as boolean
  block expressions over KO (KEGG Orthology) groups; "module completeness" is exactly a
  satisfiability check over KO presence. Cheap and ubiquitous, but KO-granularity and no
  candidate-gene nomination for the missing block.

- **MinPath** (Ye & Doak, *A Parsimony Approach to Biological Pathway
  Reconstruction/Inference for Genomes and Metagenomes*, PLoS Comput Biol 2009). A parsimony
  layer on top of naïve family→pathway mapping: report the **minimum** set of pathways that
  explains the observed families, which suppresses the spurious "everything is present"
  over-calling that plagues metagenome pathway annotation. Relevant here as the canonical
  warning that **presence of a marker ≠ the pathway runs** — the same asymmetry this project
  encodes (absence excludes, presence only permits).

- **SEED subsystems / RAST** (Overbeek et al.). Human-curated "subsystem spreadsheets" with
  explicit **variant codes** capturing that a function can be realised by different gene sets in
  different clades — a curated ancestor of variant-aware step-finding.

### 2. Hole-filling proper: find the gene for a known-but-unassigned step

Here the pathway is believed to run (or the reaction is known to occur), one step lacks an
assigned enzyme, and the task is to **nominate the gene**. This is where the phrase "pathway
hole filler" originates.

- **Pathway Tools — PathoLogic Pathway Hole Filler** (Green & Karp, *A Bayesian method for
  identifying missing enzymes in predicted metabolic pathway databases*, BMC Bioinformatics
  2004, 5:76, PMID:15189570). For a hole reaction, it pulls all known sequences catalysing that
  reaction in other organisms (via UniProt), BLASTs them against the target proteome, and scores
  candidates with a **naïve Bayes classifier** that combines sequence evidence (best E-value,
  average rank) with **genome-context** evidence: is the candidate on the same *directon*/operon
  as other pathway genes ("pathway-directon"), and is it adjacent to genes for neighbouring
  reactions ("adjacent-rxns"). At a stringent cutoff it proposes fillers for ~45% of holes in a
  microbial genome. This is the intellectual root of the whole area.

- **IMG (Integrated Microbial Genomes, JGI) — "Find Candidate Genes for Missing Function."**
  IMG operationalised hole-filling at database scale: for a KO/enzyme absent from a genome's
  reconstruction, surface candidate genes (by homology/ortholog association) and hand the user
  **gene-neighbourhood, occurrence-profile, and alignment** tools to adjudicate them. This sits
  on the **comparative-genomics** tradition of missing-gene detection (Osterman & Overbeek,
  *Missing genes in metabolic pathways: a comparative genomics approach*, Curr Opin Chem Biol
  2003) — infer the filler from **chromosomal clustering, gene fusions, and phylogenetic
  co-occurrence (occurrence profiles)** rather than sequence similarity alone. IMG's
  contribution was less a new algorithm than making "which genes could fill this hole?" a
  first-class, tool-supported operation over thousands of genomes.

### 3. Network gap-filling: add reactions so the model balances

A different sense of "gap": in a genome-scale metabolic model, a **blocked metabolite** (a
dead-end that cannot be produced/consumed at steady state) is a gap, and the fix is to **add
reactions** — not necessarily assign genes — so the model can produce biomass on a defined
medium.

- **GapFind / GapFill** (Satish Kumar et al.) — MILP identification of blocked metabolites and
  minimal reaction additions to unblock them.
- **ModelSEED** (Henry et al., *High-throughput generation, optimization and analysis of
  genome-scale metabolic models*, Nat Biotechnol 2010) and **KBase / gapseq** — automated
  reconstruction with LP/MILP gap-filling that adds the fewest reactions needed for growth.

This family is **flux-driven and gene-agnostic**: it can restore a viable model by adding a
reaction nobody has a gene for. Useful, but it answers "what reaction must exist," not "which
gene, in which context."

## Where this project sits

| | granularity of the "hole" | discriminating variable | candidate output |
|---|---|---|---|
| GapMind / KEGG modules / MinPath | pathway **step** | gene **presence** in a genome | which step is missing |
| Pathway Hole Filler / IMG | reaction with **no gene** | genome context (operon, profiles) | the **gene** that fills it |
| GapFind / ModelSEED / gapseq | blocked **metabolite** | steady-state flux | the **reaction** to add |
| **this project** | pathway **step** | **expression/context** (tissue, cell zone) | the **context-localised gene hypothesis** |

Every tool above answers a **genome-level** question: given the gene content of *one* genome,
is the pathway present, and if a step is empty, which gene fills it? That is exactly the right
question for a microbe, where a genome roughly *is* an organism.

It is the wrong question for a metazoan. Every human cell carries the whole genome, so
"is gluconeogenesis present?" is trivially yes everywhere — yet glucose output is restricted to
a few tissues and, within the liver, to a few cell layers. The discriminating variable is not
presence but **which isozyme is expressed where**. None of the microbial hole-fillers can ask
this, because their oracle is gene-content, which does not vary across a metazoan's cells.

This project keeps the GapMind-style logic (a module as steps with OR-branches; find the gate;
report the gap) but swaps the oracle from **genome presence** to **context expression** (GTEx
tissue, liver zonation, substrate-entry route). A "hole" becomes not "this genome lacks the
gene" but "this pathway cannot be wired up *in this context* — and here is the gene and place
where it fails." Crossing that with an independent activity claim (a known tissue function, a
growth phenotype) is the **abduction** step, which turns a context-specific hole into a
reviewable, gene- and location-localised hypothesis — the metazoan analogue of the Bayesian
hole filler's candidate list.

## References

- Green ML, Karp PD. *A Bayesian method for identifying missing enzymes in predicted metabolic
  pathway databases.* BMC Bioinformatics 2004;5:76. PMID:15189570.
- Osterman A, Overbeek R. *Missing genes in metabolic pathways: a comparative genomics
  approach.* Curr Opin Chem Biol 2003;7(2):238–251.
- Price MN, Deutschbauer AM, Arkin AP. *GapMind: Automated Annotation of Amino Acid
  Biosynthesis.* mSystems 2020;5(3):e00291-20. PMID:32576650.
- Ye Y, Doak TG. *A Parsimony Approach to Biological Pathway Reconstruction/Inference for
  Genomes and Metagenomes.* PLoS Comput Biol 2009;5(8):e1000465.
- Henry CS, DeJongh M, Best AA, Frybarger PM, Linsay B, Stevens RL. *High-throughput
  generation, optimization and analysis of genome-scale metabolic models.* Nat Biotechnol
  2010;28(9):977–982.
- Karp PD et al. *Pathway Tools* (PathoLogic, Pathway Hole Filler); *Integrated Microbial
  Genomes (IMG)*, JGI — "Find Candidate Genes for Missing Function."
