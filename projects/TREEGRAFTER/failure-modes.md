---
title: "TreeGrafter Failure Modes & Tree Placement"
autolink_gene_symbols: false
---
# TreeGrafter Failure Modes & Tree Placement

[← back to TreeGrafter Inference Evaluation](../TREEGRAFTER.md)

This sub-page drills into the **159 down-graded** TreeGrafter annotations
(`REMOVE` / `MARK_AS_OVER_ANNOTATED` / `MODIFY` from the
[main evaluation](../TREEGRAFTER.md)) and asks the question directly: **does it
make sense where TreeGrafter placed the protein on the PANTHER tree?**

We answer it *without* re-running TreeGrafter, because the placement is already
recorded for every protein:

- the **graft node** (`PTN…`) the term was propagated from — in the gene's GOA `WITH/FROM`;
- the **PANTHER family** (`PTHRxxxxx`) and **subfamily** (`PTHRxxxxx:SFn`) the
  protein was assigned to — in the UniProt record (`DR PANTHER` lines), produced
  by the same PANTHER classification TreeGrafter uses.

The join (graft node + family + subfamily + propagated term + reviewer action)
is computed by [`analyze_placement.py`](analyze_placement.py) into
[`treegrafter_placement.tsv`](treegrafter_placement.tsv). All 159 cases recover
a subfamily; 156 recover a graft node.

## Headline: placement is usually fine — the *term* is the problem

Reading the propagated GO term against the PANTHER **subfamily name** shows that
TreeGrafter rarely puts a protein in a grossly wrong part of the tree. The
fold/family assignment is almost always reasonable. What fails is the GO term
that rides along with the graft. Four failure modes account for nearly all the
down-grades:

### 1. Family-level over-generalisation (term granularity)

The protein is placed in the right **family**, but the propagated term is the
broad *family* function while the **subfamily** already knows something more
specific (or divergent).

| Gene | Propagated term (down-graded) | PANTHER subfamily (where it landed) |
|---|---|---|
| eryAI / eryAII / eryAIII | `fatty acid synthase activity` (MODIFY) | *INACTIVE PHENOLPHTHIOCEROL SYNTHESIS **POLYKETIDE SYNTHASE*** |
| mcr-1 / mcr2 / mcr-3 / mcr-4 | `LPS core region biosynthetic process` (OVER), `phosphotransferase activity, phosphate group as acceptor` (MODIFY) | **PHOSPHOETHANOLAMINE TRANSFERASE EptA** |
| ahpC | `thioredoxin peroxidase activity` (MODIFY) | ALKYL HYDROPEROXIDE REDUCTASE C |

The erythromycin PKS modules are the clearest case: the **family** is named
"fatty acid synthase" (PTHR43775) and the family-level GO term `fatty acid
synthase activity` was propagated — but the **subfamily** correctly identifies a
polyketide synthase. The mcr colistin-resistance enzymes are placed in *exactly*
the right subfamily (phosphoethanolamine transferase / EptA) yet inherited a
generic `phosphotransferase` MF and a lipid-A-vs-LPS-core process error. **The
graft point is right; the inherited term is too coarse.**

### 2. Pseudo-enzyme / loss of activity

Correct fold family, but the protein has lost catalytic activity or been
co-opted to a non-enzymatic role — something a tree graft cannot detect.

| Gene | Propagated term | Subfamily | Reality |
|---|---|---|---|
| OCTS1 | `glutathione transferase activity` (OVER) | GLUTATHIONE S-TRANSFERASE | Octopus **S-crystallin**: GST fold, ~1/700–1/6000 of authentic GST activity; a structural eye-lens protein (PMID:7639695, PMID:27499004, PMID:8587103) |
| TFP | `enzyme regulator activity` (MODIFY) | EPITHIOSPECIFIER PROTEIN | — |
| IRE1 (T. reesei) | `unfolded protein binding` (OVER) | NON-SPECIFIC SER/THR KINASE | UPR sensor kinase/RNase, not a general chaperone |

### 3. Generic / out-of-context localization and process

Low-information CC terms (`cytoplasm`, `cytosol`, `plasma membrane`, `nucleus`)
or organism-context BP terms inherited from a distant ancestor, correct-ish but
non-core or absent from the host. Examples: `relA` → `plasma membrane`, `dinB`
→ `cytosol`, `zwf` → `pentose-phosphate shunt`, several *Pseudomonas putida*
genes, and the `mcr` LPS-core process call above.

### 4. **True within-superfamily mis-placement** (the cases a re-run would change)

A minority *are* placement errors: the protein lands in a structurally related
but functionally distinct subfamily of a shared fold superfamily. These are the
only down-grades where re-examining the actual graft point (or an independent
bioinformatic/structural check) would change the call.

| Gene | Propagated term (down-graded) | Landed in subfamily | Should be |
|---|---|---|---|
| **aprA** (*Desulfovibrio*) | `succinate dehydrogenase activity` (REMOVE), `electron transfer activity`, `anaerobic respiration` | SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN (PTHR11632:SF51) | **Adenylylsulfate (APS) reductase** α-subunit — shares the FAD fumarate-reductase/SDH flavoprotein fold but reduces APS, not succinate |
| **fcs** (*P. putida*) | `medium-chain fatty acid-CoA ligase activity` (MODIFY), `fatty acid metabolic process` | 2-SUCCINYLBENZOATE–CoA LIGASE | **Feruloyl-CoA synthetase** — adjacent ANL adenylating-enzyme superfamily, wrong specific subfamily |

## Lightweight graft check (PANTHER vs InterPro, no re-run)

Rather than re-install InterProScan, we read the **two classifications UniProt
already stores** for each exemplar: the PANTHER family/subfamily (the TreeGrafter
graft point that propagated the term) and the InterPro signature entries (an
independent, signature-based opinion). Computed live by
[`graft_check.py`](graft_check.py) →
[`treegrafter_graft_check.tsv`](treegrafter_graft_check.tsv).

| Gene | Propagated term (down-graded) | PANTHER subfamily (graft) | InterPro's specific call | Diagnosis |
|---|---|---|---|---|
| **aprA** | succinate dehydrogenase activity | SDH flavoprotein, *mitochondrial* | **IPR011803 AprA** | PANTHER **subfamily-resolution gap**: no AprA subfamily exists, so it grafted onto the nearest (mito SDH) — but InterPro *does* identify AprA. An InterPro2GO call would beat TreeGrafter here. |
| **OCTS1** | glutathione transferase activity | GLUTATHIONE S-TRANSFERASE | **IPR003083 S-crystallin** | InterPro names the lens **crystallin**; PANTHER subfamily stays "GST". Pseudo-enzyme invisible to the graft. |
| **mcr-1** | phosphotransferase, phosphate acceptor | PHOSPHOETHANOLAMINE TRANSFERASE EptA | **IPR058128 Mcr1; IPR040423 PEA_transferase** | Placement is **right** (both methods); the propagated *GO term* is just a poor ancestral-node mapping. |
| **eryAIII** | fatty acid synthase activity | *INACTIVE…POLYKETIDE SYNTHASE* | PKS ketoacyl-synthase / acyltransferase domains | Placement is **right** (both methods say PKS); the propagated term is the **family-level** FAS term. |
| **fcs** | medium-chain fatty acid-CoA ligase | 2-succinylbenzoate–CoA ligase | only generic AMP-dependent ligase domain | Correct **superfamily**; *no* database has a feruloyl-CoA-synthetase-specific entry. Substrate unresolved by either method. |

**Two conclusions from the graft check:**

1. **In 4 of 5 cases the placement is sound — the error is the GO term bound to
   the graft node**, not the tree position. Re-running TreeGrafter would
   reproduce the same (reasonable) subfamily. The fix belongs upstream in
   PAINT/PANTHER's node-to-GO mapping (propagate the subfamily-specific term;
   don't attach a catalytic MF to a pseudo-enzyme subfamily).
2. **InterPro frequently has resolution PANTHER lacks** (`AprA`, `S-crystallin`,
   `Mcr1`). For these proteins a signature/InterPro2GO annotation would have been
   *more* specific or correct than the phylogenetic graft — a concrete argument
   for cross-checking TreeGrafter against InterPro2GO (see next steps).

> **Independent verification (in progress):** blinded OpenScientist
> function-assignment runs for all five exemplars (using the dedicated
> [`treegrafter_function_hypothesis.md`](../../templates/treegrafter_function_hypothesis.md)
> prompt) are running to see whether an independent agent, given only "GENE has
> *<propagated term>*", recovers the correct specific function. Verdicts will be
> folded in here on completion.

## What this means for the "re-run TreeGrafter" question

For the **bulk** of failures (modes 1–3, ~90% of the down-grades), re-running
TreeGrafter would reproduce the *same, sensible* placement — the fix belongs at
the **annotation** level (propagate the subfamily-specific term, gate
catalysis-implying MF behind active-site checks, suppress generic CC), not at
the placement level. For the **handful** in mode 4 (`aprA`, `fcs`, candidate
`tyrB`), the placement itself is the suspect, and an independent check — a
TreeGrafter re-run inspecting the graft branch, or a structural/active-site
analysis via OpenScientist — would be decisive.

## Suggested follow-ups

- **OpenScientist deep-dives** on the mode-4 candidates (`aprA`, `fcs`) as
  blinded function-assignment hypotheses, comparing the verdict to the recorded
  PANTHER subfamily.
- **Active-site / pseudo-enzyme check** on mode-2 candidates (catalytic-residue
  conservation) — the single most valuable upstream signal TreeGrafter lacks.
- Feed the family-vs-subfamily granularity cases (mode 1) back as candidate
  PAINT subfamily-annotation refinements (e.g. PTHR43775 PKS vs FAS).
