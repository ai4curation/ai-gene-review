# ftz-f1 review notes

## Scope and exact product

Review target: [M9NFK2](https://www.uniprot.org/uniprotkb/M9NFK2/entry), 803 aa, taxon 7227, [FlyBase FBgn0001078](https://flybase.org/reports/FBgn0001078.htm). All 12 seeded GOA rows are electronic and have been reviewed without changing their source terms, qualifiers, or evidence fields. The free-text ProtNLM prediction is adjudicated separately in [ftz-f1-protnlm-function-review.md](ftz-f1-protnlm-function-review.md).

The current M9NFK2 sequence is exactly identical to [P33244-2](https://rest.uniprot.org/uniprotkb/P33244-2.fasta), reviewed isoform A: 803/803 aa, SHA256 `8e47b8779f9e0ee27c6b92a56b1170a84a3c05cd7eade1dd500c5d6d3c6082b7`. The entire common tail, target residues 175–803, matches P33244-1 residues 399–1027. Source files and a generic equality checker are in [ftz-f1-isoform-records](ftz-f1-isoform-records/README.md). M9NFK2 has the PROSITE-defined DNA-binding domain at 281–356 and regulatory LBD at 568–800. These domains lie wholly within the shared tail; the 2018 NMR construct (long-product residues 785–1027) therefore corresponds to the target's identical residues 561–803.

UniProt's isoform A sequence change cites Lavorgna et al. [PMID:8096644](https://pubmed.ncbi.nlm.nih.gov/8096644/), DOI [10.1073/pnas.90.7.3004](https://doi.org/10.1073/pnas.90.7.3004), who cloned the midprepupal developmental isoform. Together with its N-terminal sequence this supports betaFTZ-F1 identity, despite the potentially confusing A/B database labels. Historical papers report older protein lengths; the older labels and lengths should not substitute for current sequence matching. Ensembl also maps M9NFK2 to ftz-f1-RA/RC products. Current sequence equality does not prove the sequence originally supplied to ProtNLM.

## Primary evidence

- [PMID:2113881](https://pubmed.ncbi.nlm.nih.gov/2113881/): purification, recognition-site mutations, and embryo reporter expression support sequence-specific activation. Cached excerpt: “The results suggest that FTZ-F1 is a transcriptional activator necessary for the proper expression of the ftz gene.” The early-embryo context is not assumed to describe the beta product's expression pattern.
- [PMID:7954827](https://pubmed.ncbi.nlm.nih.gov/7954827/): developmental competence and feedback. Cached excerpt: “We show that beta FTZ-F1 represses its own transcription and is repressed by ecdysone”. This supports a negative regulatory effect, not an assertion that direct repression has been demonstrated at every locus.
- [PMID:11060234](https://pubmed.ncbi.nlm.nih.gov/11060234/): temporal expression, mutant rescue, and nuclear localization of betaFTZ-F1. Cached excerpt: “betaFTZ-F1, is expressed in the nuclei of almost all tissues slightly before the first and second larval ecdysis and before pupation.”
- [PMID:21775434](https://pubmed.ncbi.nlm.nih.gov/21775434/): crystal structure and mutational activity assays. Cached excerpt: “the ligand-binding pocket of the FTZ-F1 LBD is completely occupied by helix 6 (H6) of the receptor”. The structure is one conformation, not a demonstration that all small-molecule binding is impossible.
- [PMID:23340581](https://pubmed.ncbi.nlm.nih.gov/23340581/): functional rescue by NR5A orthologs supports conserved transcriptional activity and argues against a necessary specific activating ligand. Cached excerpt: “These NR5A family members bind DNA as monomers and strongly activate transcription.”
- [PMID:23737522](https://pubmed.ncbi.nlm.nih.gov/23737522/): biochemical and mass-spectrometric work reported absent phospholipid binding. The abstract states “FTZ-f1 is incapable of PL binding”. This cannot be treated as an uncontested universal statement given the later positive experiment.
- [PMID:29547262](https://pubmed.ncbi.nlm.nih.gov/29547262/): full text inspected. NMR detects a dynamic regulatory domain; a lipid-overlay experiment supports phospholipid binding. Cached excerpt: “Indeed, we show that the Ftz-F1 LBD can bind phospholipids, not unlike its orthologs.” The assay uses purified regulatory domain and a lipid strip, not a quantitative T3/T4 binding series or a physiological transcriptional response. The authors' proposed link from lipid binding to altered Ftz-cofactor affinity is a hypothesis.

The publication caches for these sources are present. PMID:29547262 has full text; the other listed records are abstract-only in the local cache. Decisive quoted claims occur in those abstracts. No missing full text is described as available, and no experimental curator assertion is removed on the basis of an abstract's silence.

## Annotation decisions

All source rows have a decision: five ACCEPT, six MODIFY, one KEEP_AS_NON_CORE. The core function is sequence-specific RNA polymerase II transcriptional regulation in the nucleus. Generic DNA binding and transcription annotations are made more informative using already-seeded specific terms. Zinc binding is retained as a structural, non-core property.

QuickGO definitions checked on 2026-09-08:

- [GO:0004879](https://www.ebi.ac.uk/QuickGO/term/GO:0004879) requires transcription factor activity regulated by ligand binding. MODIFY to the supported [GO:0000981](https://www.ebi.ac.uk/QuickGO/term/GO:0000981) does not deny the nuclear-receptor fold or the 2018 lipid-binding experiment. Physiological ligand-dependent transcription remains unestablished.
- [GO:0030522](https://www.ebi.ac.uk/QuickGO/term/GO:0030522) describes the series of signals initiated by binding to an intracellular receptor. BetaFTZ-F1 participates downstream in the ecdysone-response cascade even though direct hormone-receptor activity is unproven. This process annotation is therefore retained.

The ProtNLM thyroid specificity is PLI, with the raw record explicitly attributing the paragraph's phmmer hit to Japanese flounder THRB Q91279. Exact identity to a reviewed FTZ-F1 product, NR5A-specific structural/functional evidence, and the NR1 thyroid-receptor match provide a concrete subfamily-confusion explanation. This does not rest on ARBA, an AI review's prose, an assumed taxon exclusion, or an invented negative hormone-binding experiment.

## Remaining biological question

Can an endogenous phospholipid alter full-length betaFTZ-F1 cofactor recruitment and transcription in vivo? This question is distinct from the unsupported T3/T4 receptor specificity. A future assay should measure both binding and transcriptional regulation with appropriate NR5A and thyroid-receptor controls, while preserving the target's isoform identity.

## Provider research and validation

[Falcon/Edison research](ftz-f1-deep-research-falcon.md) completed successfully on 2026-09-08 (481 seconds), with its provider artifact preserved. It supports the overall nuclear transcription-factor and developmental-competence synthesis and offers additional steroidogenesis source leads. Its locus-wide discussion does not resolve the exact M9NFK2 isoform, and the ligand assessment needs the independently retrieved 2018 NMR/phospholipid-binding paper. The curated decisions therefore cite primary experiments and sequence records directly. The validator advisory suggesting a deep-research citation is intentionally left as an advisory; quoting the provider's summary would not add evidence to those primary-source-supported decisions.

`just validate DROME ftz-f1` passes with no errors and that single advisory. The scaffolded gene history record validates. The HTML review has been rendered. The generic FASTA equality checker gives the expected identical result for M9NFK2/P33244-2 and nonidentical results for the longer P33244-1 control and synthetic control sequences.
