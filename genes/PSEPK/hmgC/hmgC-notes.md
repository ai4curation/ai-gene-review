# hmgC curation notes

Q88E49/PP_4619 is annotated as maleylacetoacetate isomerase (EC 5.2.1.2) and
belongs to the GST zeta family
[UniProtKB:Q88E49, "SubName: Full=Maleylacetoacetate isomerase";
"Belongs to the GST superfamily. Zeta family."].

The organism-specific pathway paper identifies HmgC as the middle enzyme of the
three-step homogentisate pathway
[PMID:15262943, "Homogentisate is then catabolized by a central catabolic
pathway that involves three enzymes, homogentisate dioxygenase (HmgA),
fumarylacetoacetate hydrolase (HmgB), and maleylacetoacetate isomerase (HmgC),
finally yielding fumarate and acetoacetate."].

The GST-family molecular-function annotation is retained as non-core, but its
propagated `glutathione metabolic process` annotation is over-annotated:
catalytic use of glutathione does not establish a role in glutathione
homeostasis or turnover.

## 2026-10-24 re-review (status COMPLETE)

- Replaced the UniProt quotes of the submitter-imported protein name and the
  ARBA-only SIMILARITY line with signature evidence: NCBIfam TIGR01262 (maiA) and
  InterPro IPR005955 (GST_Zeta).
- Catalytic activity and aromatic amino acid metabolic process are now TOO_GENERAL
  (both true, both entailed by GO:0016034 / GO:1902000 / GO:0006559).
- GST activity and glutathione metabolic process stay MARK_AS_OVER_ANNOTATED. They
  descend from the family-root IBD PTN001344486. The NagL structure paper says that in
  these bacterial isomerases glutathione is a regenerated cofactor
  [PMID:18824004, "glutathione is a true cofactor rather than a substrate in the reaction"].
  Family-level reasoning is in interpro/panther/PTHR42673/PTHR42673-review.yaml.
