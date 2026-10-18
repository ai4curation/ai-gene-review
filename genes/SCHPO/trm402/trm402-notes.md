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


## Full-gene re-review, 2026-09-20

All19 rows reviewed, preserving trm402 folder and current trm4b symbol. Restored RNA binding, methyltransferase, RNA methyltransferase and cytoplasm to ACCEPT. Physiological wobbleC34 IBA/ISO remain REMOVE on direct paralog-resolved evidence, explicitly preserving real in-vitro C34 catalysis. RNA-substrate and mitochondrial-assembly extensions remain UNDECIDED pending root-managed clade/substrate adjudication. The complete Falcon report is now referenced and used substantively; its physiological-site distinction and non-exclusion of cytoplasmic residence agree with the primary full text. No NEW rows added.

## OpenScientist rRNA/mRNA follow-up, 2026-10-10

Reviewed `trm402-hypotheses/trm4b-rrna-mrna-and-mitochondrial-ribosome-functions/openscientist.md` against the local GOA rows and the checked PTHR22808 family artifacts. The focused run answered the previous PAINT-boundary question: MGI:1919431 is mouse Nsun4, NSUN4 is a short mitochondrial rRNA methyltransferase branch inside heterogeneous PTHR22808, and the repo's PTHR22808 review independently treats the family as substrate-divergent. The GO:0006364 rRNA processing, GO:0009383 rRNA C5 methyltransferase and GO:1902775 mitochondrial large ribosomal subunit assembly IBA rows should therefore be removed as NSUN4 branch carry-over, not left UNDECIDED. GO:0062152 mRNA C5 methyltransferase remains UNDECIDED because the ISS from human NSUN2 is plausible but non-conservative and still untested in S. pombe.

Reviewed the PR follow-up comments. Human NSUN2 carries the same three NSUN4-donor IBAs from `PANTHER:PTN000516076`, so the OpenScientist run resolved donor identity rather than the exact PAINT node boundary. GO:0006364 and GO:0009383 are now marked over-annotated, consistent with NSUN2: MGI:1919431 names an NSUN4 donor that supports rRNA claims for NSUN4 but not for the Trm4/NSUN2 branch, while the family-wide PTN remains unaudited. GO:1902775 remains REMOVE because Trm4b is nuclear and lacks the direct mitochondrial targeting needed for a mitochondrial large ribosomal subunit assembly claim.
