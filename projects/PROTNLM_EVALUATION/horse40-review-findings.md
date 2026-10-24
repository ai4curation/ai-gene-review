---
title: Horse40 paired review findings
species: [HORSE, human]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Horse40 paired review findings

**The cohort contains useful biological errors, supported predictions and consequential gene-model uncertainties.** Its value is the evidence needed to distinguish them. A conserved family can support a function in horse, but a high identity percentage over the aligned region does not establish that the selected protein has every required domain or targeting sequence.

[Paired review index and frozen predictions](horse40.md) · [Machine-readable review inventory](mammal-benchmark/review-inventory.json) · [Selected OpenScientist investigations](horse40-openscientist-selection.md)

## Illustrative cases

| Case | Finding | Benchmark value |
|---|---|---|
| <gene species="HORSE" symbol="GHSR">Horse GHSR</gene> | The ghrelin receptor must be distinguished from both the predicted oxytocin receptor and the growth hormone–releasing hormone receptor in an existing GO annotation. | Ligand specificity and an independently traceable electronic-propagation problem. |
| <gene species="HORSE" symbol="HSPD1">Horse HSPD1</gene> | Hsp60-family identity is distinct from the cytosolic TRiC/CCT complex invoked by the prediction and an electronic annotation. A deletion also leaves exact-model folding activity uncertain. | Agreement between two wrong assertions is not independent support; family identity and catalytic competence are separate questions. |
| <gene species="HORSE" symbol="DNMT3L">Horse DNMT3L</gene> and <gene species="HORSE" symbol="DNMT3A">horse DNMT3A</gene> | Broad nuclear gene regulation is compatible with both the noncatalytic cofactor and the active DNA methyltransferase. | Pseudoenzyme status does not refute participation in the corresponding process. |
| <gene species="HORSE" symbol="OLFML2A">Horse OLFML2A</gene> | The current protein lacks the segment corresponding to the human signal peptide despite strong olfactomedin-family conservation. | Extracellular family biology is convincing, but secretory entry of this exact model is unresolved. |
| <gene species="HORSE" symbol="DYNLT2B">Horse DYNLT2B</gene> | The missing C terminus corresponds to a strand in the experimentally solved light-chain structure. | Even 91.4% identity among paired residues can conceal a consequential structural deletion. |
| <gene species="HORSE" symbol="WDPCP">Horse WDPCP</gene> | The shorter N terminus resembles a known human–mouse difference; a separate tail deletion may affect lipid affinity. | Domain context distinguishes ordinary variation from a specific functional uncertainty; broad ciliary/cytoskeletal roles remain supportable. |
| <gene species="HORSE" symbol="SHLD2">Horse SHLD2</gene> | Human splice products distinguish recruitment/complex assembly from effective DNA-end protection. The horse distal OB region needs resolution. | Correct localization or complex identity cannot certify a full repair mechanism. |
| <gene species="HORSE" symbol="WEE1">Horse WEE1</gene> | A primary oocyte experiment separates WEE2-dependent pronucleus formation from WEE1; later knockout evidence cautions against universal claims of indispensability. | A likely paralog-transfer explanation does not by itself refute redundant participation; the horse oocyte claims remain uncertain. |
| <gene species="human" symbol="DNMT3A">Human DNMT3A</gene> | Catalytic-cysteine automethylation is a real, slow DNA-free biochemical reaction suppressed by natural DNA substrate. | A surprising protein-methylation annotation has a source, but should not be presented as a second established physiological core function. |

The gene pages contain primary citations, source excerpts, sequence analyses and the paired inference. Narrative outputs are preserved in each horse gene's **ProtNLM Function Review** research section; GO outputs have separate **External predictions** sections.

## Coverage

The initial pass covers all **40 horse–human pairs**, **89 GO predictions** and **17 original function paragraphs**. Every human target has deep research: 35 Edison reports and five substantive manual reports where external research was unavailable. Three horse-specific Edison reports returned; the SIRT5 request failed and its direct horse evidence is documented in notes.

The GO assessments are **33 COR, 8 CNN, 5 LSP, 42 UNC and 1 NPI**. Narrative claims include additional specificity and family-transfer errors and are scored separately. The main reviews assess 2,784 original human GOA rows and 309 horse rows, plus two proposed human annotations. Unresolved source details remain explicit, including numerous high-throughput interaction records.

## What the review establishes

The human reviews supply literature and mechanistic context. Horse reviews evaluate whether that mechanism transfers to the selected accession, considering family identity, domain conservation, targeting signals, paralog distinctions and relevant horse experiments. Horse-specific research was pursued where direct literature was identified, including GHSR, CXCR3, SIRT5 and DNMT3A. Provider-generated reports are preserved when returned; documented manual research fills unavailable reports.

The current UniProt sequences and their checksums are frozen. Their identity with the original prediction-time input sequences has **not** been established. A suspicious model is therefore a limitation on evaluating the exact target, not proof that ProtNLM received the wrong sequence. Resolve such cases before using them as definitive model-error examples.

Reviews retain **UNDECIDED** for original GOA rows whose relevant experimental details remain inaccessible or untraced. They retain **UNC** for predictions that cannot yet be supported or refuted. These decisions identify follow-up work; a populated review is not a claim that every high-throughput interaction was independently verified.

## Reading the categories

Biological correctness is assessed separately from annotation overlap. Following the [function-prediction review criteria](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/review-function-prediction/SKILL.md), **COR** denotes a supported claim absent from the frozen target annotations, **CNN** a supported equivalent already present, and **LSP** a supported claim less specific than an existing annotation. None of these overlap checks establishes membership in the model's training data. Unsupported agreement with an electronic label does not make a prediction correct.

**PLI** and **NPI** require contrary biological evidence; broad terms are not errors merely because they are uninformative. Molecular activity, regulation of that activity, and participation in a process are assessed separately. Narrative paragraphs receive atomic claim assessments rather than being forced into the GO/EC-only PredictionReview schema.

## Evidence and reproducibility

- [Frozen cohort and all original outputs](horse40.md)
- [Sequence-comparison methods](mammal-benchmark/paired-sequences/README.md)
- [Validation summary](mammal-benchmark/validation-summary.json), [gene-review advisories](mammal-benchmark/gene-review-validation.csv), and [prediction evidence report](mammal-benchmark/prediction-evidence-validation.json): all 80 gene reviews and 27 GO sidecars pass with no errors. Gene-review advisories remain for unresolved core functions, propagation/source follow-up and related curation checks.
- [Review inventory generator](mammal-benchmark/review_inventory.py): checks exact GO IDs/labels, original narrative text, research availability and unassessed annotation rows. It does not assign biological verdicts.
- Batch notes: [pairs 1–10](mammal-benchmark/reviews-01-10.md), [pairs 11–20](mammal-benchmark/reviews-11-20.md), [pairs 21–30](mammal-benchmark/reviews-21-30.md), [pairs 31–40](mammal-benchmark/reviews-31-40.md).

The cohort was selected retrospectively from available horse predictions to expose informative distinctions. Its category proportions are not an estimate of whole-proteome accuracy. Cases with unresolved protein models or experimental sources should remain outside a definitive binary accuracy score until resolved.
