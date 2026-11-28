# SOCS7 notes

## 2026-11-28 review notes

Falcon/perplexity deep research could not run in this workspace: the configured providers reported only `claude_code`, which this lane is not using as an extra worker. I therefore reviewed the seeded GOA rows manually from the UniProt record, the cached GOA PMIDs, Reactome event summaries, and the PTHR10155 PAINT rows.

Key decisions:

- SOCS7 combines SOCS-box adaptor biology with a long N-terminal region that mediates NCK/septin and cytoskeletal signaling. Human evidence supports cytoplasm, nucleus, and cell-membrane/cytoplasmic-side localization.
- PMID:9344857 cloned NAP4/SOCS7 as a protein containing proline-rich NCK-binding motifs, an SH2 domain, and predicted nuclear signaling motifs; it is enough to keep `SH3 domain binding` as a non-core direct activity.
- PMID:15677474 supports SOCS7 inhibition of prolactin, growth hormone, and leptin signaling through phospho-STAT3/5 binding, but there is no specific GOA row for those cytokine outputs in the current seed.
- PMID:16127460 supports regulation of insulin signaling through SOCS7 association with INSR and IRS1, and mouse orthology supports the DAB1/Reelin cortical-layer rows as non-core conserved outputs.
- The bare `GO:0005515 protein binding` IPI rows are each removed as uninformative while leaving their distinct references and WITH/FROM entities intact.
