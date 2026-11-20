# ssb: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P0AGE0 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **single-stranded DNA protection and recruitment of DNA-processing enzymes**. Escherichia coli SSB forms a homotetramer that binds exposed single-stranded DNA cooperatively, protects it and prevents inappropriate annealing during replication, repair and recombination. Its flexible C-terminal tails recruit genome-maintenance proteins and can stimulate their activities, including exonuclease I. SSB therefore combines DNA protection with organization of productive DNA-processing assemblies.

Primary anchor: [PMID:2087220](https://pubmed.ncbi.nlm.nih.gov/2087220/), “As it binds tightly and cooperatively to single-stranded DNA, it has become a prototypic model protein for studying protein-nucleic acid interactions.”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI ssb` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 45; current rows: 45; inherited NEW: 0; added NEW: 0. Actions: {'ACCEPT': 17, 'REMOVE': 23, 'KEEP_AS_NON_CORE': 5}.
