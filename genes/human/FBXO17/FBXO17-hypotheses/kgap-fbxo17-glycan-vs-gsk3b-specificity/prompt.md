# AIGR Gene Hypothesis Deep Research

Evaluate one focused AI Gene Review knowledge-gap hypothesis.

## Target Gene

- Organism code: human
- Taxon: Homo sapiens (NCBITaxon:9606)
- Gene symbol: FBXO17
- UniProt accession: Q96EF6

## Seed Hypothesis

FBXO17 recognizes complex or sulfated glycoprotein substrates through its FBA/G
lectin domain, while recognition of the validated GSK3B protein substrate uses a
mechanistically distinct protein-binding mode rather than high-mannose ERAD
substrate recognition.

## Context

- The gene review accepts FBXO17 carbohydrate binding and glycoprotein
  catabolism, but rejects broad high-mannose ERAD propagation from related FBA
  paralogs.
- PMID:18203720 reports that FBXO17 binds heparin strongly, chondroitin sulfate
  weakly, and lactoferrin through complex glycan moieties, while not binding
  high-mannose glycans on the glycan array.
- A separate mechanistic lead identifies GSK3B as a validated FBXO17 substrate
  and maps a putative FBXO17 GSK3B-binding region around amino acids 151-200.

## Research Objective

Determine whether the hypothesis is supported, partially supported, unresolved,
or refuted. Focus on evidence that separates:

1. FBXO17 from high-mannose-binding FBA paralogs such as FBXO2 and FBXO6.
2. Complex/sulfated glycan recognition from ERAD/high-mannose recognition.
3. GSK3B recognition from the FBXO17 FBA/G lectin pocket.

Use primary literature where possible, and do not rely on literature alone. If
useful, compare FBXO17 sequence/domain features with related FBA proteins and
check whether the mapped GSK3B-binding region overlaps or is separable from the
FBA/G glycan-binding domain. Keep computation compact: do not run broad BLAST,
large structural searches, or long exploratory workflows. A concise domain/region
comparison from UniProt, InterPro, AlphaFold/sequence coordinates, and primary
papers is sufficient. Report computational checks conservatively.

## Required Output

Include:

- Executive judgment.
- Evidence matrix with citations, evidence type, claim tested, finding, context,
  confidence, and limitations.
- GO curation implications for carbohydrate binding, glycoprotein catabolism,
  ERAD/high-mannose propagation, and SCF substrate-receptor activity.
- Remaining decisive experiments.
