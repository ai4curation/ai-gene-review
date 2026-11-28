# SOCS2 notes

## 2026-11-28 review notes

Falcon/perplexity deep research could not run in this workspace: the configured providers reported only `claude_code`, which this lane is not using as an extra worker. I therefore reviewed the seeded GOA rows manually from the UniProt record, the cached GOA PMIDs, Reactome event summaries, and the PTHR10155 PAINT rows.

Key decisions:

- SOCS2 is the well-characterized CRL5/ECS substrate receptor for phosphotyrosine-containing cytokine receptors, especially GHR and EPOR. PMID:21980433, PMID:25505247, PMID:31182716, PMID:34857742, and PMID:37816714 directly support the Cul5-RING complex, phosphorylation-dependent binding, GHR substrate recognition, and ubiquitin-like ligase-substrate adaptor roles.
- PMID:12135564 directly assayed recombinant human CIS2/SOCS2 binding to a tyrosine-phosphorylated human GHR cytosolic fragment and supports `growth hormone receptor binding`.
- PMID:9727029 supports IGF1R binding by human SOCS2 and shows a broad cytoplasmic distribution, but its cell-growth and generic signal-transduction rows are over-broad relative to the direct binding result.
- PMID:12552091 shows SOCS2-dependent estrogen attenuation of growth hormone/JAK2/STAT reporter signaling. The response-to-estradiol and cellular-response-to-hormone rows are kept as non-core pathway context; the core mechanism is GHR/JAK-STAT attenuation by the CRL5-SOCS2 adaptor.
- The bare `GO:0005515 protein binding` IPI rows are each removed as uninformative while leaving their distinct references and WITH/FROM entities intact.
