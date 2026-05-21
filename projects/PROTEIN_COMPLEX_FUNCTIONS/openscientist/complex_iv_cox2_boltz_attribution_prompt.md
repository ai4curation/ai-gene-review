# Structure-Informed Complex Function Attribution: Human Complex IV COX2 Copper-Maturation Module

## Project Context

This task supports the AI Gene Review `PROTEIN_COMPLEX_FUNCTIONS` project. The goal is to decide when
a gene product should be annotated as the executor of a molecular function, as a direct contributor
to a complex function, or instead as an accessory, structural, regulatory, assembly, or maturation
factor.

Do not treat complex membership alone as evidence for molecular function. The point of this task is
to test whether Boltz2-like structure prediction can help distinguish direct functional contributors
from accessory or indirect complex members.

## Target Module

Evaluate the human Complex IV COX2 copper-maturation module:

- MT-CO2 / COX2, UniProt P00403
- SCO1, UniProt O75880
- SCO2, UniProt O43819
- COA6, UniProt Q5JTJ3
- COX20, UniProt Q5RI15
- Optionally COX16 if it is needed to interpret COX2 metallation interfaces

Project artifacts already exist and can be treated as context, not final evidence:

- `analysis/complex_iv_boltz/README.md`
- `analysis/complex_iv_boltz/domain_manifest.csv`
- `analysis/complex_iv_boltz/RESULTS_MODEL_C_DOMAINS_CU_BIOLM.md`
- `analysis/complex_iv_boltz/RESULTS_MODEL_A_COX2_SCO1_DOMAINS_CU_BIOLM.md`
- `projects/PROTEIN_COMPLEX_FUNCTIONS.md`
- `projects/OXPHOS.md`

## Core Question

For COX2 CuA-site maturation and mitochondrial respiratory chain complex IV assembly, classify each
component as one of:

1. sole executor,
2. direct active contributor,
3. mechanical or structural presenter,
4. redox/copper-state modulator,
5. accessory or stabilizing member,
6. assembly factor whose loss indirectly affects the function.

Use this classification to decide which GO annotations would be justified for each gene product:

- copper chaperone activity
- copper ion binding
- mitochondrial respiratory chain complex IV assembly
- respiratory chain complex IV assembly
- cytochrome c oxidase activity / contributes_to cytochrome c oxidase activity
- COX2 maturation or copper-center maturation, if appropriate
- accessory/stabilization/presentation roles where no direct molecular function is supported

## Required Structure-Prediction Component

Do not only summarize literature. Use Boltz2 or an equivalent protein-complex structure prediction
method as a first-class evidence layer. Equivalent methods may include AlphaFold-Multimer,
ColabFold, RoseTTAFold-All-Atom, AlphaFold 3-like complex prediction, or existing experimentally
determined structures plus AlphaFold monomer models if direct prediction is unavailable.

If you cannot directly run Boltz2 or an equivalent model in this OpenScientist environment, state
that limitation explicitly and do the next-best rigorous thing:

- identify available experimental structures, AlphaFold models, and domain annotations;
- define exact Boltz2/AF-Multimer input sets that should be run;
- specify domain boundaries, cofactors, metals, membranes, and mature-vs-precursor sequence choices;
- explain what interface confidence scores, PAE/ipTM/pLDDT, residue distances, and orientation
  checks would count as support or non-support for functional attribution;
- distinguish "usable curation evidence" from "hypothesis-generating structure prediction".

## Model Comparisons To Run Or Specify

Run or specify at least these model comparisons:

A. MT-CO2 + SCO1
B. MT-CO2 + SCO2
C. MT-CO2 + SCO1 + SCO2
D. MT-CO2 + SCO1 + SCO2 + COA6
E. MT-CO2 + COX20 + SCO1/SCO2/COA6
F. Optional: MT-CO2 + COX16 + SCO1/SCO2/COA6

For each model, evaluate:

- whether SCO1 or SCO2 is predicted near the MT-CO2 CuA region;
- whether COA6 contacts SCO1/SCO2 in a way consistent with redox modulation;
- whether COX20 appears to present or stabilize MT-CO2 rather than execute copper transfer;
- whether interfaces are high-confidence enough to use as curation support, or only as hypothesis
  generation;
- whether any predicted model distinguishes direct executor from accessory assembly factor.

## Required Output

### Executive Verdict

Give a concise verdict on whether Boltz2-like structure prediction can meaningfully improve GO
function attribution for this module.

### Structure-Prediction Plan And Findings

Create a table with one row per model comparison. Include:

- model/input composition;
- whether the model was actually run or only specified;
- sequence/domain boundaries;
- cofactors/metals/membrane assumptions;
- confidence metrics to inspect;
- key predicted or expected interfaces;
- attribution interpretation;
- limitations.

### Attribution Matrix

Create a matrix for MT-CO2, SCO1, SCO2, COA6, COX20, and optional COX16. Include:

- proposed attribution class;
- direct molecular role;
- evidence type supporting the class;
- what structure prediction could support;
- what structure prediction cannot prove;
- GO curation implication.

### GO Curation Implications

State which gene products should, should not, or may receive each relevant GO term. Be explicit
about when `contributes_to` molecular-function export would be appropriate and when complex
membership should not export a molecular function.

### Decisive Readouts

List the structural readouts that would change the curation decision, including residue-level or
distance-level checks around the MT-CO2 CuA region, SCO1/SCO2 CxxxC motifs, COA6 Cx9C region, and
COX20/COX16 presentation interfaces.

### Recommended Next Prediction

Pick the single best next Boltz2 or equivalent prediction to run for this project, and justify it.
Specify exact input chains, domain boundaries, and what result would be considered decisive.

### References And Provenance

Prefer primary literature with PMID citations. Separate direct experimental evidence from database
statements, reviews, and prediction-only evidence.
