# betT-I review notes

## Identity and scope

- Target: `betT-I`, PP_5061, UniProt Q88CW9, *Pseudomonas putida* KT2440.
- Reviewed files: `betT-I-ai-review.yaml`, `betT-I-goa.tsv`, and `betT-I-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/betT-I/betT-I-uniprot.txt`.

- `"DE   SubName: Full=Choline transporter"`
- `"GN   OrderedLocusNames=PP_5061"`
- `"CC   -!- SUBCELLULAR LOCATION: Cell membrane"`
- `"CC       Multi-pass membrane protein"`
- `"DR   GO; GO:0022857; F:transmembrane transporter activity; IEA:InterPro."`
- Twelve transmembrane segments are predicted between residues 20 and 506.

The protein name is submission-derived and the GO rows are electronic; the record contains no substrate assay.

### KT2440 locus and paralog specificity

Source: Belda et al., 2016, PMID:26913973, DOI:10.1111/1462-2920.13230.

- The cached publication record is abstract-only and does not contain a
  BetT-I-specific substrate statement.
- Earlier working notes attributed choline transport to BetT-I and BetT-III
  and glycine-betaine transport to BetT-II, but no directly checkable passage
  or target-specific transport assay is currently available.
- The adjacency and divergent orientation of betT-I relative to betIBA make
  choline uptake a useful hypothesis, not sufficient evidence for a
  choline-specific GO annotation.

## Curation conclusions

- Accept plasma-membrane localization.
- Accept generic transmembrane transporter activity and transmembrane transport.
- Do not promote choline specificity into the reviewed annotations or core
  function until a directly checkable source or substrate assay is available.
- Keep choline uptake as the leading locus-based hypothesis.

## 2026-11-03 completion pass
- Every row now cites vetted support (Phobius TM helices, InterPro/NCBIfam BCCT signatures). Membrane changed MARK_AS_OVER_ANNOTATED -> MODIFY to plasma membrane.
- Substrate stays neutral. PTHR30047:SF7, where BetT-I is classified, mixes choline (E. coli BetT, Acinetobacter BetT1/BetT2), glycine betaine (BetP, OpuD, BetL), ectoine (EctP, EctT) and trimethylamine (TmaT) carriers, so family or subfamily membership does not predict choline.
- Status set to COMPLETE. The module keeps BetT-I out of its choline-specific selector.


## 2026-11-06 comparative choline/betaine module audit

Retained generic BCCT transmembrane transport and inferred inner-membrane location. Replaced an overbroad family/subfamily cargo statement with target-specific uncertainty. Genomic adjacency and the choline product name do not establish cargo or coupling. The 2016 reannotation and 2008 Pseudomonas transport comparison were investigated without finding a directly attributable Q88CW9 transport assay in accessible source text; the 2008 paper must not be assumed to assay PP5061 merely because it discusses KT2440 paralogs.

No provider report was present. The normal Falcon command was attempted and failed with HTTP403 authentication/access error. No provider-named report was fabricated; this section is manual audit documentation.

All original machine row fields and raw UniProt/GOA files were preserved, with inherited NEW assertions tracked separately from this audit (zero added rows). The six-target baseline has 55 rows, three inherited NEW, twelve raw-file hashes and four provider-report hashes. Reusable check: `.cache/module-audit-logs/choline-betaine-20261106/check-original-six.py`; report `original-six-preservation.json`. Focused gene validation passed with no curation warnings. Ecoli BetT/BetA/BetB PAINT loss checks found no IRD/IKR. Status remains COMPLETE because review decisions are complete; unresolved biological/source claims are explicitly qualified.

Normal force-fetches of PMIDs39510372,34431198,3512525,3512526,2194570,17322201,27718375,26913973 did not recover full text; the first fetch of PMID18156257 also remained abstract-only. PMID34431198 full publisher text was read externally (https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.15741), including assay methods and preparation purity. Source distinctions: A. baumannii ATCC19606 HMPREF0010_01460 with a recombinant His tag; PMS serves as primary acceptor and oxygen measures its reoxidation. These data are comparative, not assays of either original BetA target. No publication cache was manually edited.
