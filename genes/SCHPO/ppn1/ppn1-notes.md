# ppn1 notes

## 2026-11-06

- Fetched the S. pombe `ppn1` seed with `just fetch-gene SCHPO ppn1 --uniprot-id Q9C1W8`, using the Q9C1W8 accession from the audited PTHR10340 family member table.
- Falcon deep research could not run in this sparse checkout because `templates/gene_research_go_focused.md` was not materialized. I therefore used the seeded GOA rows, the Q9C1W8 UniProt record, the PTHR10340 PAINT and family review files, the completed S. cerevisiae PPN1 review, the drafted C. glabrata PPN1 review, cached PMID:16823372, and manual PubMed/web searches.
- Manual PubMed and web searches on 2026-11-06 for SPBC713.07c, Q9C1W8, `"Schizosaccharomyces pombe" ppn1 endopolyphosphatase`, and `"Schizosaccharomyces pombe" polyphosphate endopolyphosphatase` found no direct S. pombe Ppn1 biochemical characterization.
- A same-name fission-yeast CPF/DPS subunit Ppn1 appears in the 2021 cleavage and polyadenylation literature; that Ppn1 is not Q9C1W8/SPBC713.07c and was not used as support here.
- Current PAINT supports the same four fungal Ppn1 conclusions used in the S. cerevisiae and C. glabrata reviews: `GO:0000298 endopolyphosphatase activity`, `GO:0004309 exopolyphosphatase activity`, `GO:0000324 fungal-type vacuole`, and `GO:0006798 polyphosphate catabolic process`.
- The Q9C1W8 UniProt record infers the EC 3.6.1.10 endopolyphosphatase reaction, the single-pass type-II vacuolar membrane topology, and the proteolytic activation model by similarity to S. cerevisiae Q04119. The GOA table has no stale TreeGrafter `GO:0008081 phosphoric diester hydrolase activity` row to remove for S. pombe.
