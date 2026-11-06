# dnaQ: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P03007 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **3′ to 5′ proofreading exonucleolysis**. DnaQ is the epsilon proofreading subunit of Escherichia coli DNA polymerase III. Its 3′ to 5′ exonuclease removes incorrectly incorporated terminal nucleotides and promotes replication fidelity. Epsilon associates with the DnaE alpha polymerase and HolE theta subunit in the polymerase core and also improves productive DNA synthesis. Polymerization and proofreading are catalyzed by different subunits.

Primary anchor: [PMID:6393125](https://pubmed.ncbi.nlm.nih.gov/6393125/), “We find that epsilon has 3'----5' exonuclease activity indistinguishable from that of polIII core”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI dnaQ` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 42; current rows: 42; inherited NEW: 0; added NEW: 0. Actions: {'MODIFY': 4, 'ACCEPT': 13, 'REMOVE': 25}.
