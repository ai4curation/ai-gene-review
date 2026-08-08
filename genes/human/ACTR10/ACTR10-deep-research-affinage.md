---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTR10
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: Q9NZ32
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 4
citation_count: 3
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACTR10 (human)

## Current model (mechanistic narrative)

ACTR10 (Arp11), the pointed-end subunit of the dynactin complex, mediates the physical attachment of dynactin-bound cargo to the dynein retrograde motor in neurons [PMID:28414272]. It is specifically required for coupling mitochondria to dynactin and thereby for dynein-driven retrograde mitochondrial transport in axons; an Actr10 construct lacking its dynactin-binding domain still binds mitochondria, indicating that Actr10 functions as the mitochondria-anchoring element rather than merely a structural dynactin subunit [PMID:28414272]. This retrograde transport activity is essential for homeostatic mitochondrial distribution: its loss causes aged organelles to accumulate at axon terminals while cell body mitochondria are depleted [PMID:33376159]. Beyond mitochondria, Actr10 is required for proper distribution of Mbp mRNA in oligodendrocytes, where Mbp mRNA granules associate with the dynein/dynactin motor complex, extending its role to motor-driven mRNA transport [PMID:29073112]. Genetic interaction places Actr10-dependent retrograde mitochondrial movement in a pathway with the fission GTPase Drp1 [PMID:28414272].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005856 cytoskeleton, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-9609507 Protein localization
- **partners:** DNM1L
- **complexes:** dynactin

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2017 | High | Actr10 (Arp11 subunit of dynactin) is required for dynactin-mitochondria interaction and mitochondrial retrograde transport in axons. Loss-of-function mutation in zebrafish actr10 causes failure of mitochondria to attach to the dynein retrograde motor. An Actr10 construct lacking the dynactin-binding domain retains mitochondria-binding ability, indicating Actr10 mediates dynactin-mitochondria interaction rather than simply serving as a structural dynactin subunit. | PMID:28414272 | eLife |
| 2017 | Medium | Genetic interaction studies implicated Drp1 as a partner in Actr10-dependent mitochondrial retrograde transport, placing Actr10 in a pathway with the mitochondrial fission GTPase Drp1 for retrograde axonal transport. | PMID:28414272 | eLife |
| 2017 | High | actr10 mutation in zebrafish causes failure to properly distribute mbp mRNA in oligodendrocytes, revealing a role for the Arp11/dynactin subunit in anterograde Mbp mRNA transport. Biochemical isolation of reporter-tagged Mbp mRNA granules from primary mammalian oligodendrocytes showed that they associate with the retrograde dynein/dynactin motor complex. | PMID:29073112 | Proceedings of the National Academy of Sciences of the United States of America |
| 2020 | Medium | Disruption of actr10-dependent retrograde mitochondrial transport in zebrafish neurons leads to accumulation of aged organelles in axon terminals and loss of cell body mitochondria, demonstrating that Actr10-mediated retrograde transport is essential for homeostatic mitochondrial distribution throughout the neuron. | PMID:33376159 | The Journal of neuroscience : the official journal of the Society for Neuroscience |

## Citations

- PMID:28414272
- PMID:29073112
- PMID:33376159
