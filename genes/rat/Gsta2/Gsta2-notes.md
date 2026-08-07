# Gsta2 review notes

## Evidence summary
- [UniProtKB:P04903] UniProt summarizes Gsta2 as catalyzing conjugation of glutathione to diverse electrophilic compounds.
- [PMID:17112229] The fetched GOA file uses this publication for glutathione transferase activity, cytosolic localization, glutathione binding, and xenobiotic catabolism.

## Bromobenzene evidence direction (PMID:17112229)
This paper is often read as evidence that Gsta2 detoxifies bromobenzene metabolites. It shows the
opposite direction of causality: GSTA1/GSTA2 are *targets* of arylation, not catalysts acting on
bromobenzene metabolites. The GST here was simply an abundant hepatic protein recovered on a
GSH-agarose column.
- [PMID:17112229 "Here we report that treatment of rats with bromobenzene results in the site-specific
  modification of Cys-111 in cytosolic glutathione transferase subunits A1 and A2 by bromobenzoquinone."]
- [PMID:17112229 "although the effect of Cys-111 alkylation on the activity of GSTA1 and A2 is not known,
  the distance from this residue to the active site suggests that its modification would not be likely to
  affect catalysis adversely"]

Neither UniProtKB:P04903 nor this paper establishes GSTA2-catalysed conjugation of bromobenzene-derived
epoxides or quinones, so `description` and `core_functions[0]` state the adduction finding rather than a
substrate claim.

## Provenance for the ISO propagation reviews
The five `propagation_review` blocks argue that RGD's mouse-to-rat ISO transfers here are **cluster-level
rather than 1:1**. That claim is verifiable from files in this repo, without relying on MGI subunit
nomenclature (Ya/Yc naming for the mouse donors is *not* sourced in-repo and is deliberately not used as
evidence):
- `genes/rat/Gsta2/Gsta2-goa.tsv` — rat Gsta2 receives ISO from mouse `MGI:MGI:1095417` and `MGI:MGI:95863`.
- `genes/rat/Gsta1/Gsta1-goa.tsv` — rat *Gsta1* receives ISO from nearly the same mouse donor set
  (`MGI:95856`, `95861`, `95862`, `95863`, `95864`, `95865`, `1095417`).

Two different rat alpha-class genes drawing on the same mouse donors is direct evidence of cluster-level
transfer. This matters asymmetrically by term type, which is why the file's actions differ on the *same*
donors: the class-defining catalytic term `GO:0004364` transfers safely (every alpha-class member has that
activity, and the target additionally has IDA support), whereas compartment (`GO:0005739`) and
stimulus-response (`GO:0009617`, `GO:0035634`, `GO:0061771`) terms are member-specific and do not.

## Curation decisions
- Core function: glutathione S-transferase alpha-2 (glutathione transferase activity, GO:0004364).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.
