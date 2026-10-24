# ASP3-4 notes

## Identity
- ASP3-4 is one of four identical copies (ASP3-1..ASP3-4) encoding asparaginase II, EC 3.5.1.1 [file:yeast/ASP3-4/ASP3-4-uniprot.txt "The 4 identical copies ASP3-1, ASP3-2, ASP3-3 and ASP3-4 are arranged in"]. Sequence identical to the other copy reviewed in this batch (ASP3-3/ASP3-4 SQ blocks identical).
- Reaction: [file:yeast/ASP3-4/ASP3-4-uniprot.txt "Reaction=L-asparagine + H2O = L-aspartate + NH4(+);"]
- Signal peptide 1-25, secreted / periplasm [file:yeast/ASP3-4/ASP3-4-uniprot.txt "SUBCELLULAR LOCATION: Secreted. Periplasm."]

## Evidence
- External, nitrogen-starvation-induced asparaginase distinct from an internal constitutive one [PMID:238936 "these strains of S. cerevisiae have an externally active asparaginase as well as an internally active one"; "The appearance of the external asparaginase is stimulated by nitrogen starvation, requires an available energy source, and is prevented by cycloheximide."]
- ASP3 is the structural gene; NCR acts at mRNA level [PMID:3042786 "nitrogen catabolite repression of asparaginase II is achieved by alteration in mRNA levels"]

## Curation decisions
- Core: asparaginase activity / L-asparagine catabolic process / cell wall-bounded periplasmic space.
- REMOVE RCA cytosol (YeastPathways pathway default; fits ASP1, not secreted ASP3).
- amino acid metabolic process IEA: over-annotation (parent of the specific process).
- cellular response to nitrogen starvation IDA: kept as non-core (regulated expression / N scavenging).

## Module notes
- ASP1 (cytoplasmic asparaginase I) vs ASP3 (periplasmic asparaginase II): both catalyse the same YeastPathways reaction in different compartments; ASP3 acts on external asparagine. ASP3 cluster is copy-number variable (4 copies in S288C).
