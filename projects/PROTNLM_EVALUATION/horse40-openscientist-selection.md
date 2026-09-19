---
title: Horse40 function hypotheses selected for OpenScientist
species: [HORSE, human]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Horse40 function hypotheses selected for OpenScientist

**Eight focused investigations: seven unresolved hypotheses and one supported comparison.** The first four are the strongest starting set for structure/sequence-driven investigation. The remaining four test mechanisms, process specificity and whether the review applies uncertainty proportionately.

**All eight investigations have been submitted to OpenScientist; reports are pending.** Each investigation has one central claim. A result may support, refute, narrow or leave the claim unresolved.

[Horse40 reviews](horse40.md) · [Review findings](horse40-review-findings.md) · [Selection manifest and invocation arguments](mammal-benchmark/openscientist-selection/selection.json)

## Ranked selection

| Priority | Horse target | Function hypothesis | Why investigate |
|---|---|---|---|
| 1 | <gene species="HORSE" symbol="CTDSP2">CTDSP2</gene> (F7A4N8) | The horse protein F7A4N8 enables kinase activity. | Highest priority: the short model is not simply an intact phosphatase mislabeled as a kinase. Structural/family assignment could turn an unresolved claim into a defensible conclusion. |
| 2 | <gene species="HORSE" symbol="SIRT5">SIRT5</gene> (F6S899) | The horse protein F6S899 catalyzes NAD-dependent lysine desuccinylation. | Highest priority: unusual cofactor-site and C-terminal sequence features make an independent structure-aware assessment valuable. Focus on one reaction rather than all sirtuin chemistry. |
| 3 | <gene species="HORSE" symbol="OLFML2A">OLFML2A</gene> (A0A9L0SKW1) | The horse protein A0A9L0SKW1 localizes to the extracellular matrix. | Highest priority: extracellular family biology is strong, but the selected sequence raises a targeting question. This can test whether our caution about the exact model is warranted. |
| 4 | <gene species="HORSE" symbol="SHLD2">SHLD2</gene> (A0A9L0RGD6) | The horse protein A0A9L0RGD6 positively regulates double-strand break repair via nonhomologous end joining. | Highest priority: human isoforms separate recruitment from end protection. An independent assessment of the horse protein could resolve several related repair claims without treating localization as proof. |
| 5 | <gene species="HORSE" symbol="PTPRN2">PTPRN2</gene> (A0A9L0T4W6) | The horse protein A0A9L0T4W6 participates in protein dephosphorylation. | Priority 2: an informative pseudoenzyme/process distinction. A mechanistic synthesis could resolve a claim that neither domain classification nor generic catalytic inactivity settles. |
| 6 | <gene species="HORSE" symbol="MTMR9">MTMR9</gene> (A0A9L0T3C1) | The horse protein A0A9L0T3C1 negatively regulates autophagy. | Priority 2: the broad regulator role is supported, but transfer of the particular downstream phenotype remains uncertain. This checks whether a domain-junction difference really warrants withholding the process. |
| 7 | <gene species="HORSE" symbol="WDPCP">WDPCP</gene> (A0A3Q2KRK8) | The horse protein A0A3Q2KRK8 participates in cell projection organization. | Supported comparison case: the current review accepts the broad role despite sequence differences. Including it tests both excessive caution and overly permissive transfer; it is not presumed gold truth. |
| 8 | <gene species="HORSE" symbol="WEE1">WEE1</gene> (F6TY09) | The horse protein F6TY09 participates in female pronucleus assembly. | Lower priority: an important paralog-versus-redundancy question, but literature synthesis may still leave horse participation unresolved. Include one such biological-process case to test the limits of sequence-based adjudication. |

## Investigation briefs

The provider receives the neutral hypothesis, exact frozen horse sequence and checksum, a human comparison accession, and the bounded question. It does not receive the current verdict, suspected sequence defect, or local alignment/structure conclusions. Selection reasons on this page and in the manifest are curator-only context; send only the prepared prompt and neutral invocation arguments.

- **CTDSP2** — [neutral prompt](mammal-benchmark/openscientist-selection/01-CTDSP2-kinase-activity-prompt.md). Decision sought: A supported kinase mechanism, a well-supported incompatible fold, or an explicit failure to identify the protein.
- **SIRT5** — [neutral prompt](mammal-benchmark/openscientist-selection/02-SIRT5-nad-dependent-desuccinylation-prompt.md). Decision sought: Whether the submitted sequence plausibly retains a functional desuccinylase apparatus, or whether only a different transcript/model supports it.
- **OLFML2A** — [neutral prompt](mammal-benchmark/openscientist-selection/03-OLFML2A-extracellular-matrix-localization-prompt.md). Decision sought: Independent targeting and transcript evidence supporting or limiting ECM localization of this accession; not a general claim about the gene family.
- **SHLD2** — [neutral prompt](mammal-benchmark/openscientist-selection/04-SHLD2-nhej-promotion-prompt.md). Decision sought: Whether repair competence follows from the exact architecture, and which conclusions concern a different isoform or require an experiment.
- **PTPRN2** — [neutral prompt](mammal-benchmark/openscientist-selection/05-PTPRN2-protein-dephosphorylation-prompt.md). Decision sought: Evidence for a specific protein-dephosphorylation mechanism, or a clear account of why only lipid chemistry/other processes are supported.
- **MTMR9** — [neutral prompt](mammal-benchmark/openscientist-selection/06-MTMR9-negative-autophagy-regulation-prompt.md). Decision sought: Whether a conserved productive partner interaction supports the negative autophagy effect, rather than merely demonstrating binding or altered autophagy markers.
- **WDPCP** — [neutral prompt](mammal-benchmark/openscientist-selection/07-WDPCP-cell-projection-organization-prompt.md). Decision sought: Independent support, narrowing or refutation of the broad process, with the consequences of sequence variation evaluated proportionately.
- **WEE1** — [neutral prompt](mammal-benchmark/openscientist-selection/08-WEE1-female-pronucleus-assembly-prompt.md). Decision sought: A species- and paralog-specific mechanistic conclusion; persistence of uncertainty is acceptable if the missing evidence is experimental.

## Why this subset

CTDSP2, SIRT5, OLFML2A and SHLD2 give OpenScientist a plausible computational route to resolving uncertainty about a specific protein, rather than asking for another general literature summary. PTPRN2 and MTMR9 test the distinction between catalysis, partner regulation and biological-process participation. WDPCP deliberately tests a supported transfer; the investigation should be able to challenge our acceptance as well as our uncertainty. WEE1 is a lower-priority case because lack of horse perturbation data may remain decisive even after a good investigation.

Defer the well-grounded venom/sperm-crawling and ligand-mismatch examples for this round: another investigation is less likely to change the judgment. Also defer DYNLT2B's broad collection of localization/function claims, where the initial analysis already links the missing region to an experimental structural strand, and avoid sending every related SHLD2 or SIRT5 prediction as a separate job. GEMIN5 and EFR3A are useful reserves if the first four demonstrate that transcript/structure analysis resolves the exact-model questions.

## Comparing the results

For each returned report, establish which sequence was actually analyzed. Keep its conclusion about the supplied horse protein separate from a conclusion about an intact ortholog or an alternative transcript. Compare the decisive evidence with the held-out local analysis, inspect important computations and sources, then update the specific claim and any genuinely affected related claims. A report that integrates independent analyses can carry substantial weight; a verdict alone is not the evidence. Do not count the report and its underlying primary source as independent replications.

The default project invocation uses at least three OpenScientist iterations and the configured job timeout. All eight jobs were accepted on 2026-09-08 with three iterations each. Their submitted prompts match the prepared briefs, including the exact frozen sequences. Outputs will go under the corresponding horse gene's hypothesis directory.

## Submitted investigations

[OpenScientist jobs](https://www.openscientist.io/jobs) · [Collector status and output paths](mammal-benchmark/openscientist-selection/run-status.json)

| Gene | OpenScientist job ID |
|---|---|
| CTDSP2 | `afc0ec57-89dc-46a6-96c5-4cf6b718a414` |
| SIRT5 | `fa33ef4a-c7eb-4095-8ef4-b52b64beb163` |
| OLFML2A | `b1705385-7aa1-4aae-8a1d-05d642bf8045` |
| SHLD2 | `1af435bf-ce24-49b9-933b-8fd164d53de3` |
| PTPRN2 | `01e2100b-655d-4f8a-8893-9aa9ca0f0c68` |
| MTMR9 | `d5e0df06-43d8-4578-91fd-2c6c739db7a4` |
| WDPCP | `ac0cfe8c-36e5-4c9e-b265-29144d66ec45` |
| WEE1 | `980d6e10-73fe-4604-b8e5-63ddd111f8eb` |
