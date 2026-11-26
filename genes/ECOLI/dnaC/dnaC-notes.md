# dnaC: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P0AEF0 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **DnaB ring opening and helicase loading**. DnaC is the AAA+ helicase loader of Escherichia coli. It binds DnaB, opens its hexameric ring and permits single-stranded DNA to enter during origin initiation and replication restart. DnaB and DNA stimulate DnaC ATP hydrolysis, coordinating remodeling and release of the loader as the helicase becomes active. DnaC is not the Bacillus DnaC helicase and is not a continuously required elongating-replisome motor.

Primary anchor: [PMID:30797687](https://pubmed.ncbi.nlm.nih.gov/30797687/), “six DnaC protomers latch onto and crack open a DnaB hexamer using an extended N-terminal domain”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI dnaC` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 25; current rows: 25; inherited NEW: 0; added NEW: 0. Actions: {'UNDECIDED': 1, 'REMOVE': 6, 'ACCEPT': 15, 'MARK_AS_OVER_ANNOTATED': 2, 'MODIFY': 1}.

Unresolved claims remain explicit despite COMPLETE review status:

- GO:0003688 (GO_REF:0000033): The IBA carries a phylogenetic origin-binding judgment, and no PAINT loss was found. DnaC is recruited at oriC, but direct structural evidence establishes ssDNA contact during helicase loading and does not by itself resolve origin-selective binding. Do not equate recruitment to oriC with DnaA-like origin recognition or reject the IBA solely from the familiar loader role. PAINT lineage-loss inspection found no applicable IRD/IKR; the IBA is evaluated as an ancestral-function judgment, not by counting listed donors.

The broad PTHR30050 family also contains DnaA. DnaC is SF9, DnaA SF2; the origin-binding IBA uses the same PTN001574578 ancestral node. Direct DnaC structures show ssDNA contacts, not DnaA-like origin-sequence recognition. The loader MF is proposed without guessing a GO id; the current QuickGO search returned MCM loader activity, whose eukaryotic complex is not appropriate. PMID6277866 supports fork reconstitution rather than a continuous elongation requirement.
