# AKIRIN1 notes

Human AKIRIN1 encodes a small, conserved nuclear Akirin-family protein. The strongest direct evidence in the local cache is for nuclear localization and a role as a transcriptional cofactor in NF-kappaB-dependent gene expression [PMID:18066067, "strict nuclear localization"; PMID:18066067, "novel important nuclear cofactors regulating the transcriptional activities of main transactivators"].

The 2008 mouse paper also makes the paralog split explicit: Akirin2, not Akirin1, is the paralog required for the IL-1/TLR cytokine-response phenotype, while Akirin1 knockout mice were viable and showed no gross developmental abnormalities [PMID:18066067, "MmAkirin1-/- mice were born in a Mendelian ratio, grew healthily and did not show gross developmental abnormalities"; PMID:18066067, "the functional role of MmAkirin1, attested by its sequence conservation, is unknown thus far"].

The Proteostasis PN projection for AKIRIN1 points to `GO:0070628 proteasome binding` in the adaptor/shuttle bucket [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv]. In the local literature cache I do not see direct AKIRIN1-specific proteasome-binding evidence, so that projection should be treated conservatively rather than promoted automatically.

## 2026-09-20 full re-review

This entry supersedes the earlier NF-kappaB-centered and paralog-transfer cautions above. All 27 source assertions were reassessed. Actual PTHR13293 target descent and exact mouse Akirin1 Q99LF1 primaries support the previously downgraded motility and muscle roles. PMID:18066067 provides direct human nuclear localization, but its immune rescue uses HsAkirin2; the separate Akirin1 branch IRD is for positive innate immune response, not chemotaxis or general transcription.

Seventeen MARK_AS_OVER_ANNOTATED/KEEP_AS_NON_CORE decisions are restored to ACCEPT. Negative proliferation is state-dependent; the glucocorticoid rescue study is not a universal directional refutation. GO:1902725 refers to acquisition of satellite identity, and related primary reserve-cell experiments support its compatibility with positive myotube differentiation. The original journal paper remains abstract-only, recorded explicitly. No new adjudication is needed to manufacture a conflict that disappears on checking the term and source context.

The actual AKIRIN1-GOPC IntAct binary interaction is verified, but the old GO:0044877 replacement is unsupported. Generic protein binding is retained as KEEP_AS_NON_CORE; its limited mechanistic information is not evidence that the observed interaction is false. No NEW rows were introduced. The core/description now distinguish inherited human capacity, ortholog experiments and direct human nuclear localization. The complete Falcon report and artifact were incorporated with species and condition limits; association findings were not promoted to new functions.

See [primary and phylogeny scope](AKIRIN1-primary-and-phylogeny-scope.md), [actual lineage](AKIRIN1-Q9H9L7-paint-lineage.json), [source and term checks](AKIRIN1-source-and-term-check.json), and [exact interaction records](AKIRIN1-IntAct-PMID25416956.tsv). Existing generated PN notes are left intact; their earlier interpretation is superseded here.


## Recovery PR review: generic binding policy (2026-09-22)

Applied the repository policy to the re-reviewed GO:0005515 rows. Removal concerns
the uninformative function label and does not refute the source interaction.
Rows whose target-specific assays remain inaccessible are UNDECIDED. Source
assertions and supporting evidence are preserved.

- PMID:25416956: KEEP_AS_NON_CORE -> REMOVE
