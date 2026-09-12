---
title: Focused OpenScientist investigations of fly function hypotheses
species: [DROME]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Focused OpenScientist investigations of fly function hypotheses

**Four unresolved predictions have a concrete route to further mechanistic investigation:** mitochondrial-carrier substrate specificity, crotonase-family reaction assignment, catalytic competence of a short glycosyltransferase isoform, and cross-species ligand recognition. These cases were selected from the 41-gene fly cohort because comparative or structural analysis could add decisive evidence beyond the completed literature reviews.

[Fly cohort and reviews](fly.md) · [Selection manifest](fly-benchmark/openscientist-selection/selection.json) · [Job status snapshot](fly-benchmark/openscientist-selection/run-status.json) · [OpenScientist jobs](https://www.openscientist.io/jobs)

## Selected hypotheses

| Target | Exact claim being investigated | Why a further investigation is useful |
|---|---|---|
| <gene species="DROME" symbol="Dic4">Dic4</gene>, Q9VVS1 | Uptake of thiamine pyrophosphate into mitochondria | Mitochondrial-carrier architecture does not establish substrate specificity. Compare experimentally characterized carrier subfamilies, specificity residues and the actual substrate panel in Dic4 transport studies. A negative assay with one substrate does not exclude another. |
| <gene species="DROME" symbol="CG5611">CG5611</gene>, Q9VB17 | An enzymatic contribution to fatty-acid oxidation | The crotonase superfamily supports many different reactions. Subfamily placement, catalytic geometry and characterized homologs could identify the reaction and distinguish a fatty-acid pathway role from competing metabolic functions. The original tentative wording is preserved. |
| <gene species="DROME" symbol="ttv">ttv</gene>, D5SHU8 | Glycosyltransferase activity of the 299-residue ttv-PC product | The short native product retains a catalytic region. Domain folding, substrate recognition and partner requirements matter more than length alone. The investigation separates intrinsic catalytic competence from targeting and participation in glycan synthesis in vivo. |
| <gene species="DROME" symbol="TyrRS">TyrRS</gene>, Q9VV60 | Resveratrol binding | A mammalian ligand-bound structure provides a testable pocket-level comparison. Conserved tyrosyl-tRNA synthesis does not establish the additional ligand interaction. Biochemical binding, downstream signaling and suitability as a GO annotation are separate questions. |

All four current prediction assessments are UNC. That status is curator context and is withheld from the submitted prompts. For TyrRS, the emitted GO:1905594 is obsolete; the investigation tests its biochemical content without treating binding evidence as a reason to restore an obsolete term.

## Investigation briefs

- [Dic4: thiamine-pyrophosphate transport](fly-benchmark/openscientist-selection/01-Dic4-thiamine-pyrophosphate-transport-prompt.md)
- [CG5611: fatty-acid oxidation mechanism](fly-benchmark/openscientist-selection/02-CG5611-fatty-acid-oxidation-mechanism-prompt.md)
- [ttv-PC: glycosyltransferase competence](fly-benchmark/openscientist-selection/03-ttv-short-isoform-glycosyltransferase-prompt.md)
- [TyrRS: resveratrol recognition](fly-benchmark/openscientist-selection/04-TyrRS-resveratrol-recognition-prompt.md)

Each brief supplies the exact frozen sequence, its SHA-256 checksum, accession and FlyBase identity lead. The current sequence is not asserted to be the original prediction-time input. The provider receives a neutral hypothesis and bounded questions, with the existing review verdict and local analyses held back. Primary papers are leads to inspect, not preassigned conclusions.

## Selection boundaries

The resolved protease/pseudoenzyme cases, explicit spider context in Lcp3, and routine conserved functions do not receive another investigation. Their decisive evidence is already available. Ank2's residual exocytosis claim is deferred because isoform-specific perturbation or interaction evidence may remain limiting. CG5565's proposed weak in-vitro side activity is also deferred: a different preferred physiological substrate cannot refute such activity, and a controlled assay is more likely to settle it than another fold comparison.

## Interpreting the reports

The requested outputs include executed methods, actual results, sequence identities, primary citations and explicit limitations. Docking scores alone do not establish binding, a shared fold does not establish substrate specificity, and a conserved catalytic residue does not establish an active isolated domain. Conversely, absence of a target-specific experiment does not invalidate a well-supported conserved-family inference.

Returned reports will be compared with the held-out analyses and inspected source by source. Conclusions about other isoforms remain separate from conclusions about the submitted protein. The reports can support, refute, narrow or leave the hypotheses unresolved; the existing reviews are not changed merely because a job was submitted.

## Execution and provenance

The four prepared commands passed dry-run checks. Each uses three OpenScientist iterations, a 7,200-second provider limit and an 8,100-second wrapper limit. The [collector](fly-benchmark/openscientist-selection/run.py) records accepted job IDs, upstream status and downloaded report paths. It refuses an existing local run-status file or matching remote hypothesis to prevent duplicate submissions. The static job-status link is a saved snapshot; the collector updates its repository source while jobs run.

## Accepted jobs

All four investigations were accepted on 9 September 2026 UTC. Reports are pending; submission does not change the biological assessments. [Submission verification](fly-benchmark/openscientist-selection/submission-verification.json) confirms that each upstream job contains the prepared prompt and exact frozen sequence.

| Target | OpenScientist job ID |
|---|---|
| Dic4 | `cc51f444-45ab-4933-b480-688ac83406d5` |
| CG5611 | `5f3a68b0-8473-4aca-b934-362c89e625b0` |
| ttv | `939966e3-12ee-4a0a-8311-48cd73058c14` |
| TyrRS | `30831c8b-4d81-4e64-a72f-8a3a97a9605d` |
