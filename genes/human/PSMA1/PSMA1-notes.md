# PSMA1 notes

PSMA1 encodes proteasome subunit alpha type-1, a non-catalytic alpha-ring component
of the 20S core proteasome. The key curation distinction is that PSMA1 is a
structural constituent of the proteasome, not an executor of the beta-subunit
threonine protease chemistry.

Evidence summary:

- The eukaryotic 26S proteasome contains a 20S core particle of 28 subunits capped
  by 19S regulatory particles [PMID:23495936 "barrel-shaped proteolytic 20S core
  particle (CP) of 28 subunits"].
- The 20S core has alpha outer rings and beta inner rings; beta1, beta2, and beta5
  contain the proteolytic active sites [PMID:23495936 "The β1, β2, and β5 subunits
  contain the proteolytic active sites"].
- Human structural studies of the 20S proteasome support the assembled complex context
  for PSMA1 [PMID:27493187 "native human 20S proteasome was determined at an
  unprecedented resolution of 1.8 angstroms"].
- Proteasomes are found in cytoplasmic and nuclear contexts, including clastosomes
  enriched for 19S and 20S proteasomes [PMID:12181345 "proteolytically active 20S
  core and the 19S regulatory complexes"].
- AKIRIN2 binds fully assembled 20S proteasomes and mediates nuclear import, supporting
  nuclear active-location annotations for proteasome subunits [PMID:34711951 "directly
  bind to fully assembled 20S proteasomes to mediate their nuclear import"].

Curation decisions:

- Accept structural constituent of proteasome and specific 20S alpha/core complex
  membership as the core PSMA1 annotations.
- Keep cytosol, cytoplasm, nucleus, nucleoplasm, nuclear body, and other localization
  annotations as non-core context.
- Accept proteasome-mediated protein catabolism process annotations only when they
  stay at the proteasome-process level.
- Avoid annotating PSMA1 as independently enabling protease activity; the reviewed
  evidence supports a non-catalytic alpha-ring structural role, while proteolytic
  chemistry occurs at beta subunits.
- Mark generic protein binding as over-annotated. The interactions may be real, but
  the term does not distinguish PSMA1's proteasome-specific role.
- Mark immune, DNA repair, apoptosis, spermatogenesis, cell-cycle, and similar
  pathway-level process exports as over-annotated for the individual PSMA1 subunit.
- Remove the automated lipopolysaccharide binding annotation because it is not
  supported as a human PSMA1 function by the proteasome evidence reviewed here.
