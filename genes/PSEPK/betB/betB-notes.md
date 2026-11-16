# betB review notes

## Identity and scope

- Target: `betB`, PP_5063, UniProt Q88CW7, *Pseudomonas putida* KT2440.
- Reviewed files: `betB-ai-review.yaml`, `betB-goa.tsv`, and `betB-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### Reviewed UniProt record

Source: `file:PSEPK/betB/betB-uniprot.txt`.

- `"DE   RecName: Full=Betaine aldehyde dehydrogenase"`
- `"DE            EC=1.2.1.8"`
- `"CC   -!- FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine"`
- `"CC       betaine. Catalyzes the irreversible oxidation of betaine aldehyde to"`
- `"CC       the corresponding acid."`
- `"CC       Reaction=betaine aldehyde + NAD(+) + H2O = glycine betaine + NADH + 2"`
- `"CC       Note=Binds 2 potassium ions per subunit."`
- `"CC   -!- SUBUNIT: Dimer of dimers."`
- `"DR   GO; GO:0008802; F:betaine-aldehyde dehydrogenase (NAD+) activity; IEA:UniProtKB-UniRule."`

### KT2440 pathway assignment

Source: Belda et al., 2016, PMID:26913973, DOI:10.1111/1462-2920.13230.

- The cached record is abstract-only and does not contain a checkable betIBA
  reaction passage. The inaccessible sentence retained in an earlier working
  note is no longer used as annotation support.
- PMID:17116241 provides checkable KT2440 evidence that `"the betBA genes were
  required for choline"` transformation and osmoprotection.

Source: Zhang et al., 2024, PMCID:PMC11200750. Full text accessed through PMC/web search.

- The abstract reports that `"betB-encoding betaine-aldehyde dehydrogenase was identified"` in KT2440 salt-stress transcriptomics and that overexpression of `betB` improved growth under high salinity.

The overexpression phenotype supports an osmoprotection role but does not replace the reaction-specific UniProt/HAMAP evidence.

## Curation conclusions

- Accept GO:0008802 as BetB's core molecular function and glycine-betaine biosynthesis from choline as its pathway.
- Keep metal ion binding as non-core mechanistic support.
- Mark generic oxidoreductase activity as over-annotated.

## 2026-09-27 retired process term

- GO:0019285 was retired in GO release 2026-05-19, so the NEW proposal and the
  authored core process now use GO:0031456 (glycine betaine biosynthetic process), the
  term the bacterial_choline_to_glycine_betaine_biosynthesis module grounds the same
  step on. The evidence and reasoning are unchanged.

## 2026-11-03 completion pass
- GO:0016491 MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0008802; GO:0046872 KEEP_AS_NON_CORE -> MODIFY to GO:0030955 potassium ion binding (HAMAP MF_00804: "Binds 2 potassium ions per subunit"). Both match E. coli BetB (P17445).
- Q88CW7 has only a family-level PANTHER cross-reference (PTHR11699); E. coli and P. aeruginosa BetB are in PTHR11699:SF228, but KT2440 BetB is not asserted there.
- Status set to COMPLETE.


## 2026-11-06 comparative choline/betaine module audit

Retained specific NAD-dependent BADH activity and inherited glycine-betaine process proposal using family-rule and KT2440 pathway evidence. Description explicitly marks tetramer and potassium-binding features as inference. Potassium-binding refinement is not inferred from salt tolerance. Expanded the truncated pathway quotation to state actual choline-to-glycine-betaine conversion. No target isolated-enzyme kinetics were invented.

No provider report was present. The normal Falcon command was attempted and failed with HTTP403 authentication/access error. No provider-named report was fabricated; this section is manual audit documentation.

All original machine row fields and raw UniProt/GOA files were preserved, with inherited NEW assertions tracked separately from this audit (zero added rows). The six-target baseline has 55 rows, three inherited NEW, twelve raw-file hashes and four provider-report hashes. Reusable check: `.cache/module-audit-logs/choline-betaine-20261106/check-original-six.py`; report `original-six-preservation.json`. Focused gene validation passed with no curation warnings. Ecoli BetT/BetA/BetB PAINT loss checks found no IRD/IKR. Status remains COMPLETE because review decisions are complete; unresolved biological/source claims are explicitly qualified.

Normal force-fetches of PMIDs39510372,34431198,3512525,3512526,2194570,17322201,27718375,26913973 did not recover full text; the first fetch of PMID18156257 also remained abstract-only. PMID34431198 full publisher text was read externally (https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.15741), including assay methods and preparation purity. Source distinctions: A. baumannii ATCC19606 HMPREF0010_01460 with a recombinant His tag; PMS serves as primary acceptor and oxygen measures its reoxidation. These data are comparative, not assays of either original BetA target. No publication cache was manually edited.
