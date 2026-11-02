# PP_4704 (Q88DW4) curation notes

Reached from KBase gene-annotate dashboard protein
[NZ_BCBP01000038.1_47](https://gene-annotate-dashboard.kbase.us/review/NZ_BCBP01000038.1_47)
(P. putida, tier B). The query is 99.1% identical over 978/978 residues to KT2440 PP_4704.
The exact-match UniParc entries were deleted ("Not part of a reference proteome"), so the review is
filed on the reference-proteome entry Q88DW4, with the dashboard ID as an alias.

## Conclusion

PP_4704 is the P. putida orthologue of P. aeruginosa **PA4735 / EpaF** ("essential Pseudomonas
AsmA-like protein four"). It is an inner-membrane-anchored AsmA-like (bridge-like, repeating
beta-groove) protein. By orthology it contributes, redundantly with TamB and YhdP, to outer-membrane
biogenesis, probably by moving glycerophospholipids to the outer membrane. This is an inference
from the orthologue. Nothing has been measured for the P. putida protein.

- **Orthology.** The reciprocal best hit between the KT2440 and PAO1 AsmA-like sets is PA4735: 64.9%
  identity over 977 aligned residues, spanning both full sequences (BERIL run
  `20261030T213714Z-pp4704-homology`; `PP_4704-bioinformatics/homology_results.json`). The dashboard's
  "58.1%" PAO1 homolog is the same protein, measured with a different method.
- **Not an orthologue of any E. coli AsmA-like protein.** Local alignments to AsmA, TamB, YhdP, YdbH,
  YicH and YhjG cover only 6-27% of PP_4704 (SW scores 49-68, against 3157 for PA4735). It shares
  the AsmA-like/DUF748 family and PANTHER PTHR30441:SF8 with YicH, but it is not a YicH orthologue.
  Sposato et al. state that PA4735 is absent from E. coli. The deep-research report guessed "YicH
  subfamily, probably non-essential". That guess is wrong.
- **KT2440 AsmA-like set** (reciprocal best hits with PAO1):
  - PP_2893 = TamB (PA2542)
  - PP_0938 = YhdP (PA4476)
  - PP_4857 = YhjG (PA4879)
  - PP_0287 = AsmA (PA5146)
  - PP_4704 = EpaF (PA4735)
  - PP_4572 = PA2708, the short DUF748 protein reviewed by another agent
  - KT2440 has **no YdbH orthologue**: the best KT2440 hit to PA5307 is TamB, with a score of 136.
- **Genetics in the orthologue (PMID:38305166).**
  - PA4735 deletion worsens the defects of tamB yhdP mutants.
  - A tamB yhdP ydbH PA4735 quadruple mutant could not be made.
  - Overexpressed PA4735 restores growth and vancomycin resistance to the triple mutant.
  - This is genetic evidence for outer-membrane biogenesis and integrity. Phospholipid transport is
    inferred from the family (PMID:34781743, PMID:38748582) and from the LPS-balance suppression,
    not from an assay.

## KT2440 fitness

The Fitness Browser returns 403 and `just fetch-fitness` failed. The data were read from the BERDL
lakehouse copy (`kescience.fitnessbrowser`) using a curl User-Agent and pagination (runs
`20261030T213451Z-pp4704-fitness` and `20261030T213749Z-pp4704-asma-paralog-fitness`).

- **PP_4704.** It was measured in 300 experiments and has no phenotype. Fitness ranges from -0.72
  (D-galacturonate, t -5.2) to +0.31, and the mean is 0.00. Under polymyxin B the values are
  +0.07 to +0.31. It has no specific-phenotype entries.
- **Cofitness.** The top cofitness is only 0.47, with glucarate/galacturonate catabolism genes
  (PP_1165-PP_1171 and PP_3599-PP_3601). Together with the weak galacturonate value, this is most
  likely noise and is not informative about function.
- **Paralogs.**
  - YhdP (PP_0938) has 14 phenotypes at fit ≤ -1 and t ≤ -4.
  - TamB (PP_2893) has 1.
  - AsmA, YhjG and PP_4572 have none.
- **Interpretation.** A flat single-mutant profile is what redundancy predicts. It neither supports
  nor refutes the process claim. No KT2440 fitness or genetic data bear directly on "outer membrane
  biogenesis".

## Dashboard verdict

**Recommended verdict: supported.** The supporting evidence is orthology to a genetically
characterized protein, not data on this gene.

Corrected annotation: "AsmA-like inner-membrane-anchored protein, orthologue of P. aeruginosa
EpaF (PA4735); by orthology contributes redundantly (with TamB/YhdP) to outer-membrane biogenesis,
probably intermembrane phospholipid transport; untested in P. putida."

| GO term | Assessment |
|---|---|
| GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly | **COR** (2). Novel; supported by orthology to EpaF. |
| GO:0005886 plasma membrane | **CNN** (2). Correct, but already in GOA as a TreeGrafter IEA. |

The call got the right answer from family labels and snippets of Sposato et al. It never identified
its homolog as EpaF, and it did not say that the genetic data belong to the orthologue. The call's
"OmpA-like C-terminal domain" is a weak Gene3D/SUPERFAMILY superfamily hit (0.8% HMM coverage), not
an OmpA peptidoglycan-binding domain.

## GOA review

- GO:0005886 plasma membrane (IEA): **ACCEPT**.
- GO:0090313 regulation of protein targeting to membrane (IEA, TreeGrafter): **REMOVE**. It is a
  family-wide propagation from the historical E. coli AsmA/OmpF phenotype.
- NEW, ISS from PMID:38305166:
  - GO:0043165
- GO:0120010 intermembrane phospholipid transfer was proposed as NEW (ISS) in the first
  version and **dropped** after PR #5755 review. Comparator check (QuickGO, 2026-10-31,
  `PP_4704-bioinformatics/ecoli_asma_comparator_goa.tsv`): none of E. coli TamB, YhdP or
  YdbH carries GO:0120010. YhdP has GO:0015914 phospholipid transport (EXP PMID:33046656,
  IBA), YdbH has it at IGI (PMID:34781743), TamB has none. The chain to PP_4704
  (proposed transporters -> EpaF sufficient when overexpressed -> orthology) shows
  sufficiency, not lipid movement, so the mechanism is now a suggested question and
  GO:0043165 carries the claim.

## Caveats

- No experiment on any P. putida AsmA-like protein.
- Lipid transfer has not been shown biochemically for EpaF.
- In P. aeruginosa, EpaF supports growth without the other three only when overexpressed.
- KT2440 lacks YdbH, so the redundancy network differs from that of P. aeruginosa.

## Tooling

- **`just fetch-gene`.** It failed on EBI OLS read timeouts at the taxon-label step. I seeded the
  review by calling `fetch_gene_data` with `ncbitaxon_label` patched to use `ubergraph:`. That
  first wrote to `genes/genes/...` because I passed the wrong base path; I moved the file and
  deleted the stray directory.
- **`just fetch-fitness`.** It failed (403, no local FEBA). The BERDL workaround is described above.
- **`fetch-gene-pmids`.** It found no PMIDs. I fetched PMID:38305166, PMID:34781743 and
  PMID:38748582 manually.
- **Deep research.** I used the `claude-code` provider, because no API keys are set.
- **`validate-predictions`.** It writes an untracked `reports/prediction-evidence.json` at the
  repo root.
