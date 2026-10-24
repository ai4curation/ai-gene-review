# EMENI cysD notes

## 2026-10-24

Fetched `EMENI/cysD`, read the cached GOA and UniProt records, and reviewed all
15 GOA rows. The direct local evidence is a small, older A. nidulans literature
set:

- PMID:6381643, "Mutations affecting the sulphur assimilation pathway in
  Aspergillus nidulans: their effect on sulphur amino acid metabolism" -
  abstract-only in the cache; supports homocysteine synthase as "the enzyme
  which constitutes an alternative pathway for homocysteine synthesis".
- PMID:8249501, "Comparative studies on O-acetylhomoserine sulfhydrylase:
  physiological role and characterization of the Aspergillus nidulans enzyme" -
  abstract-only; characterizes A. nidulans OAH sulfhydrylase as an "oligomeric
  protein with a broad substrate specificity with regard to sulfhydryl
  compounds" and says its major physiological role "seems to be recycling of
  the thiomethyl group of methylthio-adenosine".
- PMID:9506902, "Structure and regulation of cysD, the homocysteine synthase
  gene of Aspergillus nidulans" - abstract-only; cysD was isolated by
  "functional complementation of a cysD11 mutation" and its cDNA complemented
  a S. cerevisiae homocysteine-synthase mutant.
- PMID:17482430, "Multiple fungal enzymes possess cysteine synthase activity in
  vitro" - abstract-only; cysD has in-vitro cysteine synthase activity, but the
  authors report that "the cysB-encoded enzyme is the only CS of physiological
  importance in the studied fungus".

The current PTHR43797 PAINT snapshot places only three assertions at
`PTN002887184`: cytoplasm, O-acetylhomoserine sulfhydrylase activity, and
L-homocysteine biosynthetic process. The GOA IBA row for `GO:0004124` cysteine
synthase activity is therefore stale relative to the local 2026 PAINT export;
it is still biologically defensible as a non-core in-vitro activity because
PMID:17482430 explicitly names homocysteine synthase encoded by cysD among the
A. nidulans enzymes that catalyze O-acetylserine plus sulfide to form cysteine
in vitro.

I searched the web for newer `cysD`, homocysteine synthase, and
O-acetylhomoserine sulfhydrylase papers. The newer hits were background papers,
database pages, conference PDFs, and thesis citations; I did not find a newer
primary paper that changes the cysD functional picture after PMID:17482430.
