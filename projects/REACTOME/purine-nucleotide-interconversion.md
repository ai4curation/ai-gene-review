---
title: "Reactome purine nucleotide interconversion pilot"
---

# Purine nucleotide interconversion Reactome/module pilot

[Back to Reactome-GO Alignment](../REACTOME.md)

**Bottom line:** this small soluble-metabolism pilot cleanly separates the
reaction layer from the pathway-container layer. The local
[`purine_nucleotide_interconversion`](../../modules/purine_nucleotide_interconversion.html)
module and the cached Reactome entries agree on one exact human reaction event,
GMP synthase. The adenylosuccinate synthetase, IMP dehydrogenase, and AMP
deaminase events have matching chemistry but Reactome represents each paralog
group as a `DefinedSet`, so they need family-level review before being counted
as exact executor assertions. The cached human GO-CAM production index has no
activity rows for the seven `UniProtKB` executors in this module, so this first
pilot is a Reactome-vs-local-module comparison rather than a three-way
reconciliation.

The generated comparator output is in
[`pathway-alignments/purine_nucleotide_interconversion.md`](pathway-alignments/purine_nucleotide_interconversion.md).

## Reaction-Level Match

| Reactome event | Module node | Local MF alignment | Executors in the module | Completed gene-review rows | GO-CAM status |
|----------------|-------------|--------------------|-------------------------|----------------------------|---------------|
| `R-HSA-111524` IMP + L-aspartate + GTP => adenylosuccinate + GDP + Pi | `adss_step` | `GO:0004019` adenylosuccinate synthase activity matches the reaction chemistry, but Reactome uses a `DefinedSet` rather than an exact accessioned executor | `UniProtKB:Q8N142` | `ADSS1` has an accepted Reactome-backed cytosol row for `R-HSA-111524` | no cached human GO-CAM row for the executor |
| `R-HSA-73794` IMP + H2O + NAD+ => XMP + NADH + H+ | `impdh_step` | `GO:0003938` IMP dehydrogenase activity matches the oxidoreductase reaction, but Reactome uses a `DefinedSet` rather than exact accessioned executors | `UniProtKB:P12268`, `UniProtKB:P20839` | `IMPDH1` and `IMPDH2` have accepted Reactome-backed cytosol rows for `R-HSA-73794` | no cached human GO-CAM rows for the executors |
| `R-HSA-73792` XMP + L-glutamine + ATP + H2O => GMP + L-glutamate + AMP + diphosphate | `gmps_step` | `GO:0003922` GMP synthase (glutamine-hydrolyzing) activity matches the ATP-dependent amination | `UniProtKB:P49915` | `GMPS` has an accepted Reactome-backed cytosol row for `R-HSA-73792` | no cached human GO-CAM row for the executor |
| `R-HSA-76590` AMP + H2O => IMP + NH4+ | `ampd_step` | `GO:0003876` AMP deaminase activity matches the family-level hydrolytic deamination, but Reactome uses a `DefinedSet` rather than an exact accessioned executor | `UniProtKB:P23109`, `UniProtKB:Q01432`, `UniProtKB:Q01433` | `AMPD1`, `AMPD2`, and `AMPD3` have accepted Reactome-backed cytosol rows for `R-HSA-76590` | no cached human GO-CAM rows for the executors |

All four reaction IDs are used in `modules/purine_nucleotide_interconversion.yaml`
as activity evidence, directly below the local GO molecular-function term. In
the completed human gene reviews, the same reaction IDs appear as accepted
Reactome-backed `GO:0005829` cytosol TAS rows rather than MF rows; the pilot
therefore aligns the individual MFs through the module layer, while the gene
reviews confirm that the same reactions are already being adjudicated at the
gene-annotation layer.

## Pathway Container

| Reactome stable ID | Local use | Gene-review rows | Alignment verdict |
|--------------------|-----------|------------------|-------------------|
| `R-HSA-73817` Purine ribonucleoside monophosphate biosynthesis | Module-level evidence only | `GART` and `PFAS` use it for `GO:0009168` purine ribonucleoside monophosphate biosynthetic process; `GMPS` keeps the same pathway-container row as non-core | Keep out of the reaction-to-MF table; it is a pathway container that mentions GMP and AMP synthesis from IMP, not a fifth catalyzed MF step |

This is the first reusable pattern from the pilot: pathway containers can be
valid Reactome evidence for a BP assertion but should be excluded from
individual MF matching. The `R-HSA-73817` row can be audited in a de novo purine
comparison that includes `GART` and `PFAS`; it should not be counted as an
additional GMPS reaction or as support for a second MF in the interconversion
module.

## Scope Boundary: ADSL

The local module describes the AMP branch as two reactions:

1. ADSS condenses IMP, L-aspartate, and GTP to make adenylosuccinate.
2. ADSL cleaves adenylosuccinate to AMP and fumarate.

Only the ADSS reaction is a part of this module's executable reaction list.
ADSL is intentionally treated as an adjacent de novo purine enzyme and reviewed
in `de_novo_purine_synthesis`. A full Reactome pathway comparison for the
purine nucleotide cycle should make one of two choices:

| Choice | Consequence |
|--------|-------------|
| Pull ADSL into this module | The AMP branch becomes chemically complete and can be compared to Reactome event-by-event from IMP to AMP |
| Leave ADSL external | The module remains focused on the IMP branch-point entry/exit reactions, and the ADSS row must be described as the committed step toward AMP rather than the whole AMP-producing branch |

The current module follows the second interpretation.

## Next Checks

- Check whether the ADSS family selector should list both human adenylosuccinate
  synthetase isozymes as representative members. The annoton says
  `ADSS1/ADSS2`, but the representative list currently has only
  `UniProtKB:Q8N142`.
- Inspect the ADSS, IMPDH, and AMPD `DefinedSet` events before treating those
  stable IDs as exact per-paralog evidence.
- Look for a production GO-CAM covering human de novo purine synthesis or purine
  nucleotide interconversion, then decide whether this pilot can be upgraded
  from a Reactome/module comparison to a Reactome/module/GO-CAM comparison.
