# ASPFU Q4WDG6 / mitA notes

## 2026-11-06

- Fetched `ASPFU/Q4WDG6`, the Af293 `AFUA_6G04680` protein that Kotz et al.
  call `mitA`.
- A local cache search for `mitA`, `AFUA_6G04680`, `Afu6g04680`, `MIPC
  transferase`, and `inositol-phosphorylceramide` found only Kotz et al. 2010
  [PMID:19822220] for direct A. fumigatus MitA literature.
- A PubMed ESearch query for newer direct MitA papers using `"Aspergillus
  fumigatus"` with `MitA`, `AFUA_6G04680`, `Afu6g04680`, `"mannosylation of
  inositol-phosphorylceramide"`, or `"MIPC transferase"` also returned only
  PMID:19822220. Web search found PubMed/ScienceDirect records, a PDF copy of
  the same Kotz et al. paper, CAZy GT32, Aspertome, and later reviews that cite
  Kotz et al.; it did not identify a newer primary reassignment of MitA's
  direct function.
- The cached Kotz et al. paper is abstract-only. The abstract is still enough to
  support the core call: deleting `mitA` eliminates MIPC and MIPC-derived
  glycosphingolipids and accumulates the precursor IPC, so GOA's older
  `GO:0000030` and `GO:0016740` IMP rows should be replaced by the exact
  `GO:0103064 inositol phosphorylceramide mannosyltransferase activity`.
- Both PTHR32385 PAINT rows from `PANTHER:PTN001285482` are sound for Q4WDG6.
  The GO:0000030 MF row is too broad because GO:0103064 now exists; the
  GO:0051999 MIPC biosynthesis row is exact.
- The UniProt ARBA process rows to `GO:0006673` and `GO:0006688` are ancestors
  of the exact MIPC-biosynthesis process. No M(IP)2C row appears here, which is
  appropriate because the Aspergillus acidic GIPC pathway is not the budding
  yeast Ipt1 route.
- The membrane row is kept as non-core. Q4WDG6 has two Phobius transmembrane
  helices in the UniProt record and MitA must act at a membrane on a lipid
  acceptor, but I did not find a direct A. fumigatus Golgi-localization assay.
