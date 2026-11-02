# GPX4 notes

## 2026-10-20 ORGANELLES batch 1 (mitochondrion rows)

- Three mitochondrion rows, all kept ACCEPT:
  - IBA (PTN002613015, PTHR11592): GPX4-orthologue node (Euteleostomi) seeded by mouse and rat Gpx4;
    human GPX4 is inside the clade, no paralog transfer. propagation_review NO_FAILURE_CORE added.
  - IEA GO_REF:0000120: mouse orthologue O70325 + SL-0173; human UniProt line is by similarity
    (ECO:0000250), and the human mitochondrial isoform has the N-terminal transit peptide
    (cytoplasmic isoform lacks 1-27).
  - HTP MitoCoP (PMID:34800366): organelle-level.
- NEW GO:0005743 mitochondrial inner membrane (IC, isoform P36969-1). Lines of evidence:
  1. Sub-mitochondrial fractionation, mouse liver [PMID:19447173 "Like cyt. c, Gpx4 was found in the membrane fractions and it was particularly enriched in the inner membrane."]
  2. Rat testis mitochondrial PHGPx [PMID:7524677 "suggesting an electrostatic binding of the protein to the inner surfaces of the organelle."]
     and [PMID:8155669 "The results indicate that PHGPx is largely localized in the contact sites fraction."]
  3. Leader-dependent, membrane-potential-dependent import with processing [PMID:8878533 "23-kDa PHGPx was imported into mitochondria in a time-dependent manner and was processed to yield the 20-kDa form of PHGPx."]
  4. Substrate is cardiolipin, an inner-membrane lipid [PMID:19447173 "Gpx4 differentially regulates apoptogenic protein release owing to its inner membrane location in mitochondria and its ability to repair cardiolipin peroxidation."]
  Disagreement on binding mode only (carbonate-resistant in mouse liver vs electrostatic in rat
  testis), not on the membrane. Side of the membrane unknown. Rodent data, so IC.
- core_functions.locations left as cytosol + mitochondrion: the inner-membrane location and the
  cardiolipin effect are suggestive, but the PLOOH-reducing activity has not been measured in a
  resolved inner-membrane fraction.
- Cached PMIDs 19447173, 7524677, 8155669, 8878533.
