# dnaE: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P10443 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **DNA-template-directed nucleotide incorporation**. DnaE is the catalytic alpha subunit of Escherichia coli DNA polymerase III. It extends a DNA primer on a DNA template and synthesizes both nascent chromosome strands as part of the replisome. The beta sliding clamp provides high processivity, while DnaX organizes the polymerase cores. E. coli alpha lacks intrinsic 3′ to 5′ proofreading exonuclease activity; the separate DnaQ epsilon subunit provides editing.

Primary anchor: [PMID:2997151](https://pubmed.ncbi.nlm.nih.gov/2997151/), “The isolated alpha subunit has DNA polymerase activity”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI dnaE` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 52; current rows: 52; inherited NEW: 0; added NEW: 0. Actions: {'MODIFY': 8, 'ACCEPT': 13, 'REMOVE': 31}.

The exonuclease row is `negated: true` and is ACCEPTed as a negative claim. PMID2997151 explicitly separates polymerase alpha from proofreading epsilon; this negative cannot be exported as positive capacity. No generalization is made to PHP-active DnaE enzymes in other bacterial lineages.
