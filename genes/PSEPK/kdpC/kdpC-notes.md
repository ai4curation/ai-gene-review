# kdpC curation notes

## Evidence assessment

The initial removal of ATP binding was too strong. Primary work on E. coli KdpC
reports ATP interaction by KdpC, dependence on its conserved glutamine, and a
transient KdpB/KdpC/ATP complex that raises pump ATP-binding affinity
[PMID:21711450, "both ATP binding to KdpC and ATP hydrolysis activity of
KdpFABC were sensitive"]. The PSEPK protein is assigned to the conserved KdpC
family, but no PSEPK-specific binding assay was identified
[file:PSEPK/kdpC/kdpC-uniprot.txt].

## Curation decision

GO:0005524 is retained as non-core rather than removed: direct ortholog evidence
supports ATP binding, while its broad wording does not convey the transient
complex context and must not be confused with KdpB ATP hydrolysis. GO:0008556 is
accepted in substance with `contributes_to_molecular_function` carrying the
preferred complex-level relation.

## 2026-11-01 completion pass

- No provider deep-research file exists for this gene; provider deep research was
  not run for this pass.
- Revised GO:0005524 ATP binding from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED:
  the E. coli catalytic-chaperone evidence is contested by structures that place the
  KdpC soluble domain in the periplasm [PMID:28636601, "This topology puts the soluble
  domain, which appears to have a novel fold, on the periplasmic side of the
  membrane."].
- GO:0008556 changed to MARK_AS_OVER_ANNOTATED (accessory subunit; contributes_to in
  core_functions); GO:0006813 and GO:0016020 changed to MODIFY (correct but general).
  Added NEW part_of GO:0031004 by orthology.


## Scoped Kdp module consultation — 2026-11-07

GO0008556 is ACCEPT for structural contribution to the pump; the core already uses contributes_to. The inert inherited relationship string is not a reason to reject genuine function. ATP binding is UNDECIDED: the full E. coli21711450 paper reports low-specificity photoaffinity observations, no isolated-KdpC ATP ITC signal up to2.8mM, and ATP-dependent isolated-domain interaction. The later periplasmic structure challenges physiological contact with the KdpB ATP pocket, not all possible nucleotide binding. Original positive data remain represented.

Every original annotation row and its source payload/order was reviewed and preserved. No additional annotation rows were proposed. Full provenance and assay boundaries: `analysis/module_audits/bacterial_kdp_potassium_homeostasis/psepk-consultation/primary-scope.md`; sequence checks are adjacent. No IBA rows occur in these six reviews, so no IBA loss judgment is being made. Family membership and original historical ISO donors are retained independently of donor counts.

A genuine `just deep-research PSEPK kdpC --provider falcon` request failed HTTP403 authentication. Logs remain in `.cache/module-audit-logs/kdp-20261107/psepk-consultation/`; no provider report was manufactured.
