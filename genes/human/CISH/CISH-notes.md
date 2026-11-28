# CISH notes

## 2026-11-28 review notes

Falcon/perplexity deep research could not run in this workspace: the configured providers reported only `claude_code`, which this lane is not using as an extra worker. I therefore reviewed the seeded GOA rows manually from the UniProt record, the cached GOA PMIDs, Reactome event summaries, and the PTHR10155 PAINT rows.

Key decisions:

- CISH is a cytokine-inducible SH2/SOCS-box protein in the CISH/SOCS1/SOCS2/SOCS3 branch. UniProt describes negative regulation of cytokines that signal through JAK-STAT5 and phosphorylated EPOR / IL3 receptor binding, and PAINT places cytokine receptor binding plus cytokine/JAK-STAT negative regulation on this branch.
- The PMID:9465889 `regulation of cell growth` NAS row is not retained: the cached abstract only says mouse Cish had been shown to have a growth-inhibitory function and then reports human CISH cloning, expression, and mapping.
- PMID:10902923 cloned the alternative human CISH1b isoform and contains only background prose on JAK-STAT modulation by some CIS/SOCS/SSI-family proteins, so the NAS `intracellular signal transduction` row is marked over-annotated rather than converted into a direct CISH signaling claim.
- Reactome cytosol rows are kept when they sit in cytosolic CRL5 regulation events; the STAT5-upregulated expression event is retained as non-core localization context because CISH is separately placed in the cytosolic CRL5 module.
- The bare `GO:0005515 protein binding` IPI rows are each removed as uninformative while leaving their distinct references and WITH/FROM entities intact.
