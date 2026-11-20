# EMENI cysD notes

## 2026-11-01

Rechecked the `PTHR43797` paint rows against the current local cache. The
`PANTHER:PTN002887184` node still carries `GO:0005737` cytoplasm,
`GO:0051009` O-acetylhomoserine sulfhydrylase activity, and `GO:0071269`
L-homocysteine biosynthetic process, and the stale `GO:0004124` IBA remains
absent from the 2026 PAINT export. That matches the existing review: the
current PAINT rows are retained as core, while the old cysteine synthase IBA is
kept only as a non-core in-vitro side activity.

Searched for newer primary `cysD`, homocysteine synthase, and
O-acetylhomoserine sulfhydrylase literature in A. nidulans/Emericella. The
search did not find a newer cysD-specific paper that changes the interpretation
from the cached 1984, 1993, 1998, and 2007 primary literature.

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
  compounds", says OAH SHLase-negative mutants were "completely
  prototrophic", and says its major physiological role "seems to be recycling
  of the thiomethyl group of methylthio-adenosine".
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
in vitro. The IEA `GO:0071266` de novo methionine-biosynthesis row is retained
only through the homocysteine-producing hydrogen-sulfide/OAH branch; the
methanethiol reaction fits salvage of methylthioadenosine-derived sulfur and is
tracked separately with generic `GO:0071267` L-methionine salvage while the
precise fungal pathway term remains unresolved.

I searched the web for newer `cysD`, homocysteine synthase, and
O-acetylhomoserine sulfhydrylase papers. The newer hits were background papers,
database pages, conference PDFs, and thesis citations; I did not find a newer
primary paper that changes the cysD functional picture after PMID:17482430.
