# ligA: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P15042 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **NAD-dependent DNA nick sealing**. LigA is the essential NAD-dependent DNA ligase of Escherichia coli. It seals adjacent 3′ hydroxyl and 5′ phosphate DNA ends through an enzyme-adenylate intermediate, using NAD+ as the adenylate donor. LigA joins nicks after Okazaki-fragment maturation and during DNA repair, acting in the cytoplasm on chromosomal DNA. Its BRCT domain assists DNA binding but is not indispensable for nick sealing.

Primary anchor: [PMID:15848142](https://pubmed.ncbi.nlm.nih.gov/15848142/), “NAD(+)-dependent DNA ligases are essential enzymes in bacteria, with the most widely studied of this class of enzymes being LigA from Escherichia coli.”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI ligA` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 17; current rows: 17; inherited NEW: 0; added NEW: 0. Actions: {'ACCEPT': 14, 'REMOVE': 2, 'MODIFY': 1}.
