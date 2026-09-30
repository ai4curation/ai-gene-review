# cao1 (Q9P7F2) — evidence and prediction assessment

Cao1 is a copper-dependent, quinone-containing primary amine oxidase that catalyzes oxidative deamination of primary amines. The enzyme supports utilization of ethylamine as a nitrogen source in heterologous yeast assays and obtains copper in part through the Atx1 metallochaperone. Cao1 is cytosolic in vegetative cells and concentrates within forespores during meiosis, where its activity depends on copper supplied through Mfc1.

## Evidence and family boundary

The [2006 primary study](https://pubmed.ncbi.nlm.nih.gov/16946276/) expresses pombe spao1/cao1 in budding yeast and establishes active primary-amine oxidation and ethylamine-dependent growth. The [2008 full text](https://pubmed.ncbi.nlm.nih.gov/18723604/) directly assays native pombe Cao1, copper loading and activity-retaining Cao1-GFP. Its statements about cao1-deletion ethylamine growth are labeled unpublished observations within that paper; they are not treated as a separately displayed quantitative experiment.

The [2011 Mfc1 paper](https://pubmed.ncbi.nlm.nih.gov/21828039/) directly images Cao1-GFP within forespores in figure6C and measures its activity. The focus on Mfc1 does not make the Cao1 annotation a misattribution. Falcon underestimates this direct localization evidence. GO:0008131 was checked against [QuickGO](https://www.ebi.ac.uk/QuickGO/term/GO:0008131); its RHEA reaction and synonyms encompass primary-amine oxidation, despite the potentially confusing current label “primary methylamine oxidase activity.”

Copper is experimentally required. TPQ is supported by conserved cofactor chemistry and the curated ortholog-attributed record; target-specific TPQ spectroscopy is not claimed. The Cu-loading phenotype is retained as non-core homeostasis, and TAS detoxification remains unresolved because the cited germination paper is abstract-only in the cache.

## External ProtNLM statements

[Exact retained output](cao1-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | Amine oxidase | LSP | The broad reaction class is correct; target assays establish a copper-dependent primary-amine oxidase with ethylamine catabolism, and the sequence belongs to the copper/TPQ oxidase family (PMID:16946276; PMID:18723604). |

## Source quotations

[PMID:18723604](https://pubmed.ncbi.nlm.nih.gov/18723604/):

> the Atx1 metallochaperone represents an important source of copper for Cao1.

[PMID:16946276](https://pubmed.ncbi.nlm.nih.gov/16946276/):

> Expression of
> spao1(+) resulted in the production of an active enzyme capable of catalysing
> the oxidative deamination of primary amines.

[PMID:18723604](https://pubmed.ncbi.nlm.nih.gov/18723604/):

> Cao1-GFP was localized
> in the cytosol

[PMID:21828039](https://pubmed.ncbi.nlm.nih.gov/21828039/):

> Cao1-GFP displayed fluorescent staining that was mainly observed within the forespores

## Research provenance

The genuine [Falcon report](cao1-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.
