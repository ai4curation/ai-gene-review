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
