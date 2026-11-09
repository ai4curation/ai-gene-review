# GYPA notes

Deep research providers unavailable in this environment; research from UniProt (P02724),
cached publications, and Reactome.

## Identity / topology
- Glycophorin A: major sialoglycoprotein of the erythrocyte membrane, single-pass type I
  membrane protein (signal peptide, extracellular glycosylated N-terminus bearing MN blood
  group antigens, GXXXG-containing transmembrane helix, short cytoplasmic tail).
- Carries MN blood group antigens on the N-terminal glycosylated segment that lies outside the
  erythrocyte membrane (UniProt FUNCTION).

## Localization (cell-surface benchmark)
- Plasma (cell) membrane; extracellular glycosylated domain exposed on the RBC surface.
  [PMID:19438409 "GPA was localized at the cell surface, but also localized to the Golgi."]
- UniProt SUBCELLULAR LOCATION: Cell membrane; Single-pass type I membrane protein.

## Function
- Component of the ankyrin-1 complex (ANK1, RHCE, RHAG, SLC4A1, EPB42, GYPA, GYPB, AQP1), which
  provides stability and shape to the erythrocyte membrane [PMID:35835865 "Component of the
  ankyrin-1 complex, a multiprotein complex involved in the stability and shape of the erythrocyte
  membrane"]. Cryo-EM: "a GPA monomer is bound at each end of the SLC4A1 dimer".
- Associates with band 3 / SLC4A1 (anion exchanger); important for SLC4A1 activity and may assist
  its surface trafficking, though GPA knockdown did not change AE1 surface level [PMID:19438409].
- Forms homodimers via the TM GXXXG motif (classic model membrane-helix dimer) [PMID:35835865
  homodimer; GXXXG TM dimerization is the textbook glycophorin A paradigm].
- Hijacked as a receptor by pathogens: P. falciparum EBA-175 (sialic-acid dependent) and
  Hepatitis A virus (UniProt FUNCTION, microbial infection). These are host-pathogen, non-core.

## Curation decisions
- Many GO:0005515 protein binding rows (large interactome screens, PMID:32296183 etc.): bare,
  uninformative -> REMOVE per protein-binding policy. Functional band 3 / ankyrin-1 relationship
  is captured by GO:0170014 ankyrin-1 complex.
- GO:0042802 identical protein binding = homodimer -> ACCEPT.
- GO:0016020 membrane -> TOO_GENERAL (plasma membrane asserted).
