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

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 12 GOA rows, the description and core functions. ProtNLM2 output was not consulted.

### Identity of the benchmark accession

- M9NFK2 (UniProtKB/TrEMBL, PE 3, 803 aa) is a duplicate unreviewed entry for the shorter FTZ-F1 product. It is identical to reviewed isoform P33244-2 (803/803 aa) and is **not a fragment**. Relative to canonical P33244-1 (1027 aa) it has a different, shorter isoform-specific N-terminus (M9NFK2 1-174 vs P33244-1 1-398) and shares the entire C-terminal 629 aa (M9NFK2 175-803 = P33244-1 399-1027). The DNA-binding domain (281-356), LBD-type domain (568-800) and AF-2 motif (789-800) are all in the shared segment; nothing functional is missing. See [RESULTS-rereview.md](ftz-f1-bioinformatics/RESULTS-rereview.md) and `compare_isoforms_rereview.py` (new files; the existing isoform-records were not modified).
- The canonical product P33244 (Swiss-Prot) carries all the FlyBase experimental and PAINT IBA annotations (QuickGO query on 2026-10-20); M9NFK2 carries only 12 IEA rows. This folder (`genes/DROME/ftz-f1`) is keyed to M9NFK2, and no review exists for P33244, so the next review should be `genes/DROME/ftz-f1__P33244`.
- Naming hazard: UniProt Q05192 ("Nuclear hormone receptor FTZ-F1 beta") is the separate paralog **Hr39** (PANTHER SF25), not the betaFTZ-F1 isoform of ftz-f1.

### Evolutionary grounding

- PANTHER PTHR24086:SF15 (NUCLEAR HORMONE RECEPTOR FTZ-F1) contains M9NFK2, canonical P33244, Bombyx FTZ-F1 P49867 and C. elegans nhr-25 Q19345. Mammalian NR5A1/SF-1 (SF24) and NR5A2/LRH-1 (SF18) are separate subfamilies; their steroidogenic and phospholipid-ligand-regulated properties are not transferred.
- PAINT node PTN000639680 (donors include FBgn0001078 and mouse Nr5a1/Nr5a2) gives canonical P33244 IBA rows for GO:0000978 RNA pol II cis-regulatory region sequence-specific DNA binding, GO:0006357, GO:0009755 hormone-mediated signaling pathway, GO:0009888 tissue development and GO:0090575 RNA pol II TF complex. GO:0004879 nuclear receptor activity is not among them; treated as a deliberate PAINT decision that supports the existing MODIFY of the InterPro2GO GO:0004879 row.
- Family review `interpro/panther/PTHR24086/PTHR24086-review.yaml` (SF15, representative M9NFK2) agrees with the UniProt subfamily placement; no disagreement.

### Changes in this re-review

- GO:0003677 DNA binding: MODIFY target changed from GO:0043565 to the more precise GO:0000978 (binding to the ftz upstream regulatory element, PMID:2113881; matches PAINT).
- GO:0043565 sequence-specific DNA binding: ACCEPT -> MODIFY to GO:0000978 (correct-but-general rule; GO:0000978 is_a descendant verified via QuickGO ancestors).
- GO:0004879: MODIFY retained; reason extended with subfamily placement and the PAINT omission.
- All other decisions re-examined and retained (GO:0000981 ACCEPT; GO:0003700, GO:0006351, GO:0006355 MODIFY; GO:0006357 ACCEPT; GO:0005634 ACCEPT; GO:0008270 KEEP_AS_NON_CORE; GO:0030522 ACCEPT as participation of a downstream competence TF in the ecdysone-initiated cascade; GO:0035556 MODIFY to GO:0030522).
- No NEW terms. FlyBase organismal IMP terms on P33244 (pupation, metamorphosis, salivary gland cell death, etc.) were deliberately not added: they are mutant phenotypes, and the isoform-level assignment to the beta product would need checking against each paper. The Ftz cofactor interaction (GO:0061629 IPI on P33244) is mainly an embryonic alphaFTZ-F1 context and was not proposed for this product.
- Validation: `just validate DROME ftz-f1` passes (only the deep-research-citation advisory).
