# dnaB: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P0ACB0 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **parental-duplex unwinding and coordination of primase**. DnaB is the hexameric replicative DNA helicase of Escherichia coli. Nucleoside-triphosphate hydrolysis powers movement along single-stranded DNA in the 5′ to 3′ direction, separating parental strands ahead of the replication machinery. DnaC loads DnaB at initiation and during replication restart. DnaB also organizes and stimulates DnaG primase, coupling template unwinding to RNA-primer synthesis.

Primary anchor: [PMID:3007474](https://pubmed.ncbi.nlm.nih.gov/3007474/), “It was determined that the dnaB protein moves 5' to 3' along single-stranded DNA, apparently in a processive fashion.”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI dnaB` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 57; current rows: 57; inherited NEW: 0; added NEW: 0. Actions: {'MODIFY': 4, 'REMOVE': 14, 'ACCEPT': 33, 'KEEP_AS_NON_CORE': 6}.
