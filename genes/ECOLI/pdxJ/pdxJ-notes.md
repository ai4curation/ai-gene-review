# pdxJ review notes (E. coli K-12, P0A794)

Step 5 of the DXP-dependent de novo PLP module and seed of PAINT node
PTN000765245 (PTHR30456, Bacteria level: cytosol, GO:0033856, GO:0008615).

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Sources: the
  reviewed UniProt record and cached publications PMID:10225425,
  PMID:1537799, PMID:10944349, PMID:16858726 (all abstract-only) and
  PMID:18304323 (cytosol proteome; PdxJ only in supplementary lists).
- Structural papers cited by UniProt (PMID:11286891, PMID:12269807,
  PMID:12206776) and the PdxH-bypass G194S paper (PMID:8636054) are not cached.

## Function

- [file:ECOLI/pdxJ/pdxJ-uniprot.txt "Catalyzes the complicated ring closure
  reaction between the two acyclic compounds 1-deoxy-D-xylulose-5-phosphate
  (DXP) and 3-amino-2-oxopropyl phosphate (1-amino-acetone-3-phosphate or AAP)
  to form pyridoxine 5'-phosphate (PNP) and inorganic phosphate."]
- [PMID:10225425 "These results clarify the previously unknown role of PdxJ in
  the de novo PLP biosynthetic pathway."]
- Octamer: [PMID:10944349 "indicate the quaternary assembly of PdxJ into
  octamers with 422 symmetry."]
- Genetics: [PMID:1537799 "The pdxJ gene encodes a protein required in the
  biosynthesis of pyridoxine (vitamin B6)."]

## Curation decisions

- Cytosol rows (HDA, IBA, IDA) KEEP_AS_NON_CORE, matching the re-reviewed
  P. putida cytosol row; cytoplasm -> MODIFY to cytosol.
- `GO:0008615` ACCEPT (same rationale as pdxA: GO's term for the PNP-forming
  branch; PNP, not pyridoxine, is the product).
- `GO:0016769` -> MODIFY to `GO:0033856`.
- `GO:0042802` identical protein binding (IDA, octamer) KEEP_AS_NON_CORE;
  homodimerization would be wrong for an octamer.
- NEW `GO:0036001` (IDA, PMID:10225425): GOA has no PLP-pathway row.
- `just paint-losses ECOLI pdxJ`: no IRD/IKR.
