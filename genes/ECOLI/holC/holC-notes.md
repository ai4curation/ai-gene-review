# holC: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P28905 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **SSB-to-loader bridging and replisome stabilization**. HolC is the chi accessory subunit of the Escherichia coli DNA polymerase III clamp loader. Together with psi, it links the loader to SSB-coated DNA and stabilizes productive replisome organization. Chi–SSB binding affects coupled strand synthesis and replisome stability, although it is not an obligatory step for every primer-utilization event. HolC also associates with the YoaA helicase in DNA-damage tolerance. It has no established intrinsic DNA-polymerizing activity.

Primary anchor: [PMID:21857649](https://pubmed.ncbi.nlm.nih.gov/21857649/), “sequence changes in χ that block complex formation with SSB lead to salt-dependent uncoupling of leading- and lagging-strand DNA synthesis”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI holC` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 40; current rows: 40; inherited NEW: 0; added NEW: 0. Actions: {'UNDECIDED': 2, 'REMOVE': 27, 'MODIFY': 3, 'ACCEPT': 6, 'MARK_AS_OVER_ANNOTATED': 2}.

Unresolved claims remain explicit despite COMPLETE review status:

- GO:0003677 (GO_REF:0000002): Chi binds SSB and psi in the clamp-loader accessory module; association with SSB-coated DNA does not establish direct DNA binding by isolated chi. The available target evidence is insufficient to resolve the broad electronic DNA-binding claim.
- GO:0009314 (PMID:27718375): The cited Keio-screen abstract describes radiation-survival phenotypes but does not enumerate HolC among the individually characterized results. The target-specific full table was not accessible; retain uncertainty rather than reject the curator or infer a radiation-specific function from replication accessory activity alone.

PMID9989506 reports a primase-handoff mechanism. PMID21857649 explicitly does not support an essential chi–SSB role in lagging-strand primer utilization and instead shows context-dependent replisome stability. The full 2023 YoaA–chi study (PMID36509145) establishes a stable active helicase complex and chi-dependent solubility; its Discussion leaves direct activation versus structural stabilization unresolved. No independent helicase/ATPase activity or universal chi requirement is inferred.
