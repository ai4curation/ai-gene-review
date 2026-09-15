# trm402 (O13935) — evidence and prediction assessment

Trm402 (Trm4b) is a SAM-dependent NSUN2/Trm4-family tRNA cytosine-C5 methyltransferase. In fission yeast it establishes m5C at tRNA C49 and selected C50 positions, complementing Trm4a, which modifies C48 and physiological wobble C34 sites. Trm4b can methylate C34 in vitro but does not supply this modification in vivo. The protein has been observed in the nucleus.

## Evidence and family boundary

The cohort path uses trm402; the current UniProt primary symbol is trm4b, locus SPAC23C4.17. The [2019 primary full text](https://pubmed.ncbi.nlm.nih.gov/30646830/) separates Trm4a/C34/C48 from Trm4b/C49/C50. Its precursor-RNA assay permits Trm4b C34 methylation in vitro while knockout methylome data exclude that physiological role. GO:0002127 was checked in QuickGO: it is specifically anticodon position34, not generic tRNA cytosine methylation.

The [2012 paper](https://pubmed.ncbi.nlm.nih.gov/23074192/) describes C48/C49 and additional tRNA-Asp positions as dependent on two Trm4 homologs. The 2019 full text states that the earlier purported trm4b deletion strain did not contain the deletion. The older extra-site assignment in UniProt therefore cannot establish Trm4b physiological specificity. This is a source-level experimental limitation, distinct from an inferred-function disagreement.

The rRNA methyltransferase, rRNA processing and mitochondrial-LSU IBA assertions are unresolved rather than categorically refuted by tRNA experiments. The mRNA ISS assertion is likewise an open substrate extension explicitly mentioned in the 2019 discussion. Neither the number of PAINT donors nor the target appearing among its own experimental descendant sources is a reason to reject an IBA.

## External ProtNLM statements

[Exact retained output](trm402-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | tRNA (cytosine(34)-C(5))-methyltransferase | PLI | Physiological site specificity is transferred from the wrong Trm4 paralog. Trm4b modifies C49/C50 in vivo; Trm4a supplies C34. C34 activity is real in vitro, so this is an IN_VITRO_NOT_IN_VIVO problem as well as paralog specificity, not proof that Trm4b cannot catalyze the reaction (PMID:30646830). |
| location | Nucleolus | UNC | Nuclear localization does not establish nucleolar enrichment. The emitted source cites similarity to budding-yeast P38205, whereas the target study and localization record resolve only nucleus (PMID:30646830; PMID:16823372). |

## Source quotations

[PMID:30646830](https://pubmed.ncbi.nlm.nih.gov/30646830/):

> Trm4b methylates both C34 and C49 in vitro, even though it does not methylate C34 in vivo.

[PMID:30646830](https://pubmed.ncbi.nlm.nih.gov/30646830/):

> Trm4b methylated all C49 sites on tRNAs.

[PMID:30646830](https://pubmed.ncbi.nlm.nih.gov/30646830/):

> However, both enzymes are localized to the nucleus

[PMID:30646830](https://pubmed.ncbi.nlm.nih.gov/30646830/):

> Conversely, Trm4b methylates C49 and C50,
> which both lie in the TΨC-stem.

[PMID:30646830](https://pubmed.ncbi.nlm.nih.gov/30646830/):

> It will also be interesting to see whether Trm4a and Trm4b methylate mRNAs or other small RNAs in S. pombe

## Research provenance

The genuine [Falcon report](trm402-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.
