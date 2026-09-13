# cis4 (Q9HGQ3) — evidence and prediction assessment

Cis4 is a CDF-family zinc transporter that forms a heteromeric complex with Zrg17 in the cis-Golgi membrane. It transfers zinc from the cytosol into the secretory pathway, particularly under zinc-limiting conditions, and thereby supports intracellular zinc balance and Golgi-dependent protein trafficking. Its compartment and low-zinc role differ from the ER zinc transporter Zhf1.

## Evidence and family boundary

The [2008 target study](https://pubmed.ncbi.nlm.nih.gov/18199682/) identifies Cis4 localization at cis-Golgi and its interaction with Zrg17. The [2018 full-text study](https://pubmed.ncbi.nlm.nih.gov/29529046/) uses zinc-sensitive FRET sensors in defined cis4/zrg17/zhf1 mutants: Cis4/Zrg17 is important during zinc limitation; ER-localized Zhf1 is important when zinc is abundant. Thus zinc specificity is supported by target physiology rather than a generic CDF family label. The ER IEA assertion remains unresolved as a possible additional pool; no exclusion experiment establishes that Cis4 can never reside in ER.

These experiments do not establish exact transport coupling, affinity, stoichiometry or complete alternative-metal exclusion. Golgi trafficking and cell-wall phenotypes are downstream consequences of zinc partitioning, not evidence that Cis4 transports magnesium or directly assembles GPI anchors. Falcon agrees on these distinctions; its numerical phenotypes are not copied into curated fields without source verification.

## External ProtNLM statements

[Exact retained output](cis4-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | Zinc transporter | LSP | The correct broad name omits experimentally established cis-Golgi import with Zrg17 and its low-zinc role. Target zinc-sensor and localization experiments establish zinc specificity (PMID:18199682; PMID:29529046). |
| location | Membrane | LSP | A correct but broad compartment: the target is a cis-Golgi membrane transporter. This conclusion comes from target localization and zinc-transport physiology, not simply from a membrane-domain default (PMID:18199682; PMID:29529046). |

## Source quotations

[PMID:29529046](https://pubmed.ncbi.nlm.nih.gov/29529046/):

> Cis4 and Zrg17 form a heterodimeric complex that
> transports zinc into the cis-Golgi.

[PMID:29529046](https://pubmed.ncbi.nlm.nih.gov/29529046/):

> deletion of cis4 or
> zrg17 leads to higher levels of zinc accumulating in the cytosol under
> conditions of zinc deficiency

## Research provenance

The genuine [Falcon report](cis4-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.
