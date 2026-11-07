# dnaG: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P0ABS5 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **RNA-primer synthesis**. DnaG is the zinc-containing replicative primase of Escherichia coli. It synthesizes short RNA primers on single-stranded DNA templates, providing the 3′ hydroxyl ends needed by DNA polymerase III. Interactions with DnaB helicase and SSB coordinate primer synthesis with fork progression, primer handoff and replication restart. DnaG is a DNA-directed RNA polymerase specialized for priming, rather than the multisubunit transcription RNA polymerase.

Primary anchor: [PMID:1511009](https://pubmed.ncbi.nlm.nih.gov/1511009/), “Primase, the product of the Escherichia coli dnaG gene, is the enzyme responsible for RNA primer synthesis on both template strands at replication forks during chromosomal DNA synthesis.”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI dnaG` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 28; current rows: 28; inherited NEW: 0; added NEW: 0. Actions: {'MODIFY': 4, 'ACCEPT': 20, 'REMOVE': 4}.
