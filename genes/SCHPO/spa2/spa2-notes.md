# spa2 (S. pombe, SPAC3G9.05) notes

## 2026-10-10 Initial review (PTHR21601 family pass with S. cerevisiae SPA2/SPH1)

### Localization
- Tips and division site: [PMID:25428987 "The previously uncharacterized protein identified here
  as an SH3 interactor, Spa2, localizes to arc-like structures at cell tips during interphase
  and the cell division site during cytokinesis and septation."]
- Ring layer: [PMID:28914606 "Multiple binding partners of Cdc15's and Imp2’s SH3 domains
  including Pxl1, Fic1, Spa2, Rgf3, and Cyk3 ... concentrate in this intermediate zone."]
- Recruited via a PXXP motif (residues 188-194, P191) binding the Cdc15/Imp2 SH3 domains
  (PMID:25428987), and mainly by the exocyst [PMID:40931936 "we conclude that the exocyst
  complex plays a major role in targeting Spa2 to sites of polarized growth."].

### Function
- [PMID:40931936 "At cell tips, stable complexes of oligomerized Spa2 contribute to constraining
  the growth zone, in part by delivering the Rab GTPase-activating protein for the Sec4 homolog
  Ypt2."] The SHD binds Gyp3; CC2 binds Pos1. spa2 deletion cells are shorter and wider, with
  broader Exo70/Sec3 zones.
- spa2 deletion abolishes invasive growth (PMID:25428987). This was not added as NEW because
  PomBase did not annotate it from that paper.
- Actin: deletion cells have normal F-actin at 25-36 C (PMID:25428987), and Spa2 localization is
  largely LatA-insensitive (PMID:40931936). The 2008 ISO "actin cytoskeleton organization" from
  SGD is therefore marked over-annotated.
- MAPK: [PMID:25428987 "We did not detect physical or genetic interactions between Spa2 and the
  S. pombe homologues of Bni1, Bud6, or MAP kinases"]. Pek1 is not at tips and does not depend on
  Spa2; Spa2 localizes without Mkh1 (PMID:40931936). The GO:0005078 IBA (root node PTN004550576,
  seeded only by SGD SPA2) and its derived GO:0000165 IEA were therefore removed.
- GO:0120207 "endocytosis, site selection" (PomBase IMP, PMID:40931936) is marked UNDECIDED. The
  cached main text has no endocytosis assay (no occurrence of "endocyt"); the phenotype is about
  focusing exocytosis. This may be an exo/endo slip, but the supplement was not seen, so the
  question is raised for PomBase rather than removing the annotation.
- Protein binding (Cdc15) was changed with MODIFY to GO:0017124 SH3 domain binding.

### Deep research
- `spa2-deep-research-falcon.md` (Falcon) agrees with the above. It also flags Spa2 as a
  candidate Kin1 phosphosubstrate (not validated, so not used).
