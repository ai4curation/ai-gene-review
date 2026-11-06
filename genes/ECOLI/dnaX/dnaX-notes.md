# dnaX: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P06710 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **ATP-driven clamp-loader assembly and tau-mediated replisome organization**. The Escherichia coli dnaX gene produces full-length tau and a shorter gamma protein through programmed ribosomal frameshifting. Their shared N-terminal ATPase and oligomerization domains form the motor of the clamp-loading complex, which opens and deposits beta sliding clamps on primed DNA. Tau-specific C-terminal domains additionally connect polymerase cores and DnaB helicase, organizing coupled chromosome replication. Neither product is the DNA-polymerizing subunit.

Primary anchor: [PMID:9927437](https://pubmed.ncbi.nlm.nih.gov/9927437/), “The gamma complex uses ATP to open the beta clamp and assemble it onto DNA.”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI dnaX` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 67; current rows: 68; inherited NEW: 0; added NEW: 1. Actions: {'ACCEPT': 9, 'REMOVE': 52, 'MODIFY': 3, 'KEEP_AS_NON_CORE': 3, 'NEW': 1}.

Tau and gamma are products of programmed ribosomal frameshifting (PMID11463787). The shared clamp-loader role is qualified as a complex contribution; tau-specific C-terminal organization must not be assigned to gamma.
