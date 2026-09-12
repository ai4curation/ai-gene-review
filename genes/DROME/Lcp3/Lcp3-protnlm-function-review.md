# Lcp3 ProtNLM function-description review

Target: **Drosophila melanogaster A0A0B4KEF3 (Lcp3)**. Source: the frozen ProtNLM2 response in `projects/PROTNLM_EVALUATION/fly-benchmark/predictions.jsonl.gz`, retrieved 2026-09-08. The exact response is also retained as [Lcp3-protnlm-source.json](Lcp3-protnlm-source.json). This is an external prediction, separate from GOA. The scope here is the function paragraph, with ancillary checks of its predicted name and location; this is not a review of every field in the API record.

## Original prediction

> Component of the rigid cuticle of the spider

## Claim assessment

| Claim | Assessment | Evidence and limitation |
|---|---|---|
| Component of cuticle | LSP, score 2 | Correct, but less specific than the experimentally grounded larval-cuticle function on reviewed Lcp3 P07188. The selected target and P07188 are identical current 112-residue sequences at the same FlyBase locus. This support is independent of ARBA. |
| Rigid cuticle | UNC, score 1 | The retrieved target evidence establishes larval cuticle structure, not the stated mechanical specialization. The adjective occurs in a spider donor description; it is not a demonstrated Lcp3 property. |
| Of the spider | NPI, score 0; taxon-context error | The target is D. melanogaster, an insect. The literal claim places its function in the wrong organism. This is a narrative taxon mismatch, not a formal GO taxon-constraint assessment. |

The literal full sentence is **NPI** because of its explicit spider attribution; the useful cuticle claim remains correct. Do not score the entire biological core as wrong or translate the paragraph into an invented GO prediction. Novelty here is assessed against existing annotations, including the equivalent reviewed record, not presumed knowledge of training data.

## Source trace

The function prediction's evidence names **P80519** as `tmalign_accession` (model score 0.61; reported TMalign scores 0.54948 and 0.40119). [P80519](https://www.uniprot.org/uniprotkb/P80519/entry) is adult-specific rigid cuticular protein ACP15.7 from the spider *Araneus diadematus*. Its curated function sentence matches the prediction apart from a terminal period. The donor's primary study purified and sequenced cuticle proteins from mature spiders: [Norup et al., PMID:9014336](https://pubmed.ncbi.nlm.nih.gov/9014336/), DOI [10.1016/S0965-1748(96)00052-5](https://doi.org/10.1016/S0965-1748(96)00052-5).

The metadata plus wording support an inference of donor-context leakage into the description. They do not reveal ProtNLM's internal generation steps, and the TMalign values are reported metadata, not an independently reproduced structural analysis. Shared arthropod cuticle structure can justify the broad function while failing to justify the donor's species or mechanical specialization.

## Ancillary outputs

- **Name:** the response recommends “Larval cuticle protein 4”, with phmmer donor P07189. This is an incorrect paralog name for the exact current target, which matches Lcp3 P07188 identically. P07189 is the distinct Lcp4 protein (98/112 ungapped positional matches). The name has a paralog-confusion pattern; it does not establish that the function paragraph arose from that same donor.
- **Location:** “Secreted” is supported by the characterized extracellular cuticular role and the identical reviewed precursor's residues 1–16 signal peptide. It is biologically consistent but not a novel localization finding. The response separately names P24490 as its location TMalign donor; that donor's provenance was not investigated here.

## Evidence

The [current-sequence comparison](Lcp3-bioinformatics/RESULTS.md) establishes identity with P07188 without substituting the target accession. [Snyder et al., PMID:6817923](https://pubmed.ncbi.nlm.nih.gov/6817923/), DOI [10.1016/0092-8674(82)90466-4](https://doi.org/10.1016/0092-8674(82)90466-4), linked protein sequences of major third-instar cuticle components to their genes. [FlyBase FBgn0002534](https://flybase.org/reports/FBgn0002534.html) supplies the Lcp3-specific curated interpretation and reports two transcripts encoding one unique polypeptide. The primary-paper caches are abstract-only; the gene-specific assignment also rests on reviewed sequence provenance and FlyBase curation, not an assertion that the full historical experiments were independently re-read.
