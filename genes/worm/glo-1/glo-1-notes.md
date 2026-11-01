# glo-1 review notes

- 2026-10-28: fetch-gene resolved G5EBF0 (WormBase WBGene00011083, GeneID 3565633); GOA has 17 rows.
- PMID:15843430 and PMID:17202409 are abstract-only in the cache (PMC refused full text);
  PMID:22916203, 23705068, 30419011, 24501423, 39078368, 31848222, 37704756 have full text.
- PMID:23705068 (Zhu et al. 2013, sphingolipid-TORC1) uses ges-1p::glo-1::GFP only as a lysosome
  marker: [PMID:23705068 "Both LMP-1::GFP (A–D) and GLO-1::GFP are lysosomal markers in C. elegans."]
  It does not test GLO-1 function.
- Decisions:
  - GTPase activity: ACCEPT (Rab family; Q71 catalytic Gln present; Q71L/T25N genetics [PMID:30419011]).
  - GTP binding: ACCEPT (GEF-driven nucleotide exchange in vitro [PMID:39078368]).
  - Lysosome organization (IMP): MODIFY to gut granule assembly GO:1902900; GO places gut granule
    assembly under vesicle/organelle assembly, not lysosome organization, and glo-1 does not affect
    conventional endolysosomes [PMID:30419011].
  - Lipid storage (IMP, abstract only): MARK_AS_OVER_ANNOTATED; downstream of organelle loss.
  - Mitochondrion/Golgi/TGN: MARK_AS_OVER_ANNOTATED (mammalian paralog localizations).
  - Generic CC (cytoplasm, membrane, vesicle, endomembrane system): MODIFY to gut granule (membrane).
- Comparator check not needed: no NEW process terms proposed.
