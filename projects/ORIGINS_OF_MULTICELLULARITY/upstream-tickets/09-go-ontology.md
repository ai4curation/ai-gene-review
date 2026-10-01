# GO ontology: organ-level terms on unicellular lineages; rosette colony development

**Destination:** GO ontology tracker (`geneontology/go-ontology`).

**1. Taxon constraints for organ-level growth terms.** GO:0035265 organ growth
and GO:0046620 regulation of organ growth carry `never_in_taxon` only for
Bacteria, Archaea, *S. pombe* and *S. cerevisiae* (QuickGO, 2026-10-01).
IBA and TreeGrafter rows therefore put "regulation of organ growth" on
unicellular choanoflagellate proteins (Ticket 1) with no constraint
violation.

Requested: consider constraints that keep organ-level terms off clearly
unicellular lineages, such as Choanoflagellata (NCBITaxon:28009),
Filasterea (NCBITaxon:2687318) and Ichthyosporea (NCBITaxon:127916). Plants
and animals have organs, so a simple only-in-Metazoa rule would be wrong.

**2. New term request: rosette colony development.**
- Proposed definition: "The developmental process in a unicellular colonial
  organism by which a single founding cell undergoes repeated incomplete
  cytokinesis, with daughter cells remaining attached, to form a spherical
  rosette colony held together by intercellular bridges and a shared basal
  extracellular matrix."
- Example: *Salpingoeca rosetta*, where rosetteless, jumble, couscous and
  warts affect rosette formation (PMID:25299189, PMID:30556809,
  DOI:10.1101/2024.07.13.603360). Rosettes form clonally, not by aggregation
  (PMID:23066504, PMID:30556809).
- Proposed parent: GO:0048856 anatomical structure development.
  - GO places *Dictyostelium* sorocarp development outside GO:0007275
    multicellular organism development, so we suggest the same placement
    here.
- Full draft: `genes/SALRS/rosetteless/rosetteless-ai-review.yaml`
  (proposed_new_terms).
