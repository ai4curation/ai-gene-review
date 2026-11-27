# PLK4 manual review notes

PLK4 is the divergent PLK-family kinase dedicated to centriole biogenesis. Its
best-supported molecular function is protein serine/threonine kinase activity
at parental centrioles and procentrioles, where CEP192, CEP152, STIL and other
scaffolds position it to initiate daughter-centriole assembly.

Key evidence reviewed:

- PMID:16244668 identifies PLK4 as a required regulator of centriole
  duplication in human cells.
- PMID:17681131 shows that PLK4 overexpression induces centrosome amplification
  by generating multiple procentrioles adjacent to each parental centriole and
  places PLK4 upstream of hSAS-6, CPAP, CEP135, gamma-tubulin and CP110 during
  centriole assembly.
- PMID:21725316 shows that PLK4 phosphorylates FBXW5 at Ser151, thereby
  suppressing SCF-FBXW5-mediated ubiquitylation of HsSAS-6 during centrosome
  duplication.
- PMID:22020124 supports PLK4-induced centriole amplification requiring STIL.
- PMID:24997597 supports the procentriole scaffold-switching model in which
  human PLK4 moves from a CEP192-associated inner ring to a CEP152-associated
  outer ring during centriole biogenesis.
- PMID:27796307 shows that KAT2A/2B-dependent PLK4 acetylation restrains PLK4
  kinase activity and centrosome amplification.
- PMID:30804208 identifies CEP131 Ser78 as a direct PLK4 substrate required to
  maintain centriolar-satellite integrity.

Rows reviewed conservatively:

- The long block of generic `GO:0005515` interaction rows mostly comes from
  structural, scaffold or high-throughput interaction papers. These rows were
  left distinct and removed as uninformative unless the same evidence identified
  a phosphorylated PLK4 substrate; only the FBXW5 row was modified to
  `GO:0106310`.
- Many Reactome `GO:0005829` cytosol rows are PLK1, AURKA, ciliogenesis or
  basal-body events rather than PLK4 events. They were removed row by row
  instead of treating Reactome as a uniform PLK4 source.
- Mouse-derived XY-body localization was left `UNDECIDED`; mouse-derived
  nucleolus, cleavage-furrow, trophoblast and deuterosome rows were kept only as
  non-core similarity transfers.
