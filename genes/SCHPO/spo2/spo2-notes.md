# spo2 (C6Y4C2) — evidence and prediction assessment

Spo2 is a meiosis-induced spindle pole body protein that connects Spo15 with Spo13 on the cytoplasmic face of the meiotic spindle pole body. Its ordered recruitment is required for remodeling the spindle pole body and initiating forespore membrane formation during sporulation. It is not required for the meiotic nuclear divisions themselves.

## Evidence and family boundary

The [primary paper](https://pubmed.ncbi.nlm.nih.gov/18367542/) directly supports the Spo15→Spo2→Spo13 recruitment hierarchy and an adaptor interpretation. PubMed figure8 describes two-hybrid, GST pulldown and co-immunoprecipitation experiments; figure6 describes reciprocal localization dependencies. The cache is abstract-only; PMC and EuropePMC full-text retrieval attempts were unsuccessful. No experimental annotation is removed on that basis.

The exact 133-aa C6Y4C2 sequence matches the terminal segment of the large Vps1302 sequence, but the [reproducible identity analysis](../../../projects/PROTNLM_EVALUATION/family-curation/unassigned-results.json) finds distinct PomBase locus identifiers. Falcon identifies primary full-cDNA evidence for an independent small spo2 transcript; that is a source lead requiring inspection of the full primary text before claiming a gene-model error. Neither shared sequence nor the UniProt VPS13-family sentence establishes that Spo2 has the long lipid-transfer channel of full-length Vps13. Do not conflate family ancestry with retained lipid-transfer activity.

## External ProtNLM statements

[Exact retained output](spo2-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | Uncharacterized protein | UNSCORED | The returned uncharacterized name has no ECO:0008006 evidence object and is an API default, not an attributable ProtNLM hypothesis. Spo2 is experimentally characterized. |
| location | Membrane | UNC | The target is at the cytoplasmic face of the meiotic SPB beside the nascent forespore membrane. Participation in membrane assembly does not establish membrane residence. The retained source shows a string match to a function comment about membrane formation, not a membrane-localization assay (PMID:18367542). |

## Source quotations

[PMID:18367542](https://pubmed.ncbi.nlm.nih.gov/18367542/):

> Spo2 physically
> associated with both Spo15 and Spo13, but Spo13 and Spo15 did not interact
> directly.

[PMID:18367542](https://pubmed.ncbi.nlm.nih.gov/18367542/):

> Spo13 and Spo2 localized on the cytoplasmic side of
> the SPB in close contact with the nascent FSM.

[PMID:18367542](https://pubmed.ncbi.nlm.nih.gov/18367542/):

> The
> respective deletion mutants are viable, but defective in SPB modification and in
> the onset of FSM formation.

## Research provenance

The genuine [Falcon report](spo2-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.
