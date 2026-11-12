# thiO (Q88Q83) notes, Pseudomonas putida KT2440

Completed in a session without deep-research providers; the existing falcon report and
PMID:26875494 (abstract-only) were used, with genes/BACSU/thiO as the comparator.

- Function [PMID:26875494 "Glycine oxidase, encoded by the thiO gene, participates in the biosynthesis of thiamin by providing glyoxyl imine to form the thiazole moiety of thiamin."]; glycine preferred; monomeric.
- Actions aligned with BACSU thiO: GO:0016491 MODIFY -> GO:0043799; GO:0050660 MODIFY -> GO:0071949;
  GO:0006520 MARK_AS_OVER_ANNOTATED; GO:0009228 ACCEPT (sibling of GO:0009229, not parent; earlier
  KEEP_AS_NON_CORE reason was wrong); cytoplasm ACCEPT; NEW GO:0052837 thiazole biosynthetic process.
- Conflict: this paper says B. subtilis ThiO prefers D-proline; B. subtilis kinetics (UniProt O31616,
  PMID:9827558) show Km ~46 mM for D-proline vs ~1 mM for glycine.
