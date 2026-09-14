# SPAC25B8.09 (Q9UTA9) — evidence and prediction assessment

SPAC25B8.09 is a soluble methyltransferase type-11 protein found in the nucleus and cytosol. PomBase assigns trans-aconitate methyltransferase activity through curated orthology to budding-yeast Tmt1. This supports a probable small-molecule methyltransferase, while the predominant endogenous substrate and physiological role in fission yeast remain untested. Budding-yeast Tmt1 also methylates 3-isopropylmalate, so trans-aconitate detoxification is not the only plausible metabolic context.

## Evidence and family boundary

The [PomBase target page](https://www.pombase.org/gene/SPAC25B8.09) explicitly labels biological role inferred and provides TMT1/SGD:S000000977 orthology. The downloaded [P32643 record](SPAC25B8.09-P32643-ortholog-uniprot.txt) verifies that identifier and its experimental sources. [PMID:11695919](https://pubmed.ncbi.nlm.nih.gov/11695919/) establishes Tmt1 trans-aconitate methyltransferase activity; [PMID:15147181](https://pubmed.ncbi.nlm.nih.gov/15147181/) identifies 3-isopropylmalate as its major endogenous substrate in yeast extracts. The two substrate observations are compatible; neither makes the other reaction false.

Curated orthology is reasonable support for target molecular capability. It does not settle the dominant physiological substrate, conservation of the starvation response, or a universal substrate for PTHR44942. Falcon misses both Tmt1 orthology and the target HDA nucleus/cytosol record. Its blanket “location unknown” is therefore not adopted; nor is absence of a target biochemical paper treated as grounds for erasing a curator-supported localization.

## External ProtNLM statements

[Exact retained output](SPAC25B8.09-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | Methyltransferase type 11 domain-containing protein | CNN | The claim specifies a domain class, not a methyl acceptor. IPR013216/PF08241 directly support that class. The curated Tmt1 orthology makes small-molecule methylation a reasonable additional inference but does not experimentally identify the target substrate. |

## Source quotations

[PMID:11695919](https://pubmed.ncbi.nlm.nih.gov/11695919/):

> We have identified the yeast open reading frame YER175c as the gene encoding the
> trans-aconitate methyltransferase of Saccharomyces cerevisiae.

[PMID:15147181](https://pubmed.ncbi.nlm.nih.gov/15147181/):

> the major
> methylated endogenous product of Tmt1 in yeast extracts

## Research provenance

The genuine [Falcon report](SPAC25B8.09-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.
