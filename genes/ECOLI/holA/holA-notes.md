# holA: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P28630 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **mechanical beta-clamp opening and recycling**. HolA is the delta subunit of the Escherichia coli DNA polymerase III clamp loader. It binds and opens the beta sliding clamp, while DnaX ATPase cycling and the other loader subunits coordinate loading onto primer-template DNA. Free delta can also unload beta clamps without ATP, allowing clamp recycling. HolA is a mechanical clamp-opening component rather than a DNA polymerase.

Primary anchor: [PMID:9927437](https://pubmed.ncbi.nlm.nih.gov/9927437/), “The function of ATP is to regulate the activity of one subunit, delta, which opens the clamp simply by binding to it.”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI holA` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 49; current rows: 49; inherited NEW: 0; added NEW: 0. Actions: {'ACCEPT': 10, 'REMOVE': 35, 'MODIFY': 4}.

PMID10924523 directly assays ATP-independent unloading by free delta. This supports the proposed ATP-independent clamp-unloader MF, distinct from its contribution to ATP-dependent clamp loading.

Current QuickGO GO0061860 requires ATP hydrolysis; it cannot describe free delta ATP-independent unloading. The draft GO0061860 proposal was discarded on checking that definition, and a supported proposed term is used instead. No seeded row was altered or removed.
