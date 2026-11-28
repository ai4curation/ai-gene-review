# SOCS6 notes

## 2026-11-28 review notes

Falcon/perplexity deep research could not run in this workspace: the configured providers reported only `claude_code`, which this lane is not using as an extra worker. I therefore reviewed the seeded GOA rows manually from the UniProt record, the cached GOA PMIDs, Reactome event summaries, and the PTHR10155 PAINT rows.

Key decisions:

- SOCS6 is a long-N-terminal SOCS-box protein with substrate-adaptor evidence for tyrosine-phosphorylated kinases. PMID:21030588 supports SH2-domain recognition of the phosphorylated KIT pY568 peptide and SOCS6 ubiquitin-ligase activity toward KIT.
- PMID:20007709 gives direct T-cell evidence that SOCS6 is recruited to the immunological synapse, binds active LCK, promotes LCK ubiquitination, and targets it to the proteasome. Those rows are kept, but T-cell activation itself remains a non-core specialization.
- PMID:9344848 cloned CIS4/SOCS6 but reports JAK2/JAK-STAT inhibition for CIS3 and JAB rather than CIS4; its cached abstract is not positive support for a SOCS6 JAK-STAT or defense-response function.
- The generic SOCS-box InterPro/UniPathway `protein ubiquitination` row is kept as non-core because direct KIT and LCK evidence support a ubiquitination role, but the exact core molecular function is substrate-adaptor activity.
- The bare `GO:0005515 protein binding` IPI rows are each removed as uninformative while leaving their distinct references and WITH/FROM entities intact.
