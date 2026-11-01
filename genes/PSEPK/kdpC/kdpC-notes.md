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
