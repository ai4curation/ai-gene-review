# alg-3 notes

## 2026-11-06 annotation review

Falcon deep research was not available because `agentapi` was unavailable, so no
`alg-3-deep-research-falcon.md` file was created.

I reviewed the seeded Neurospora annotations against:

- `alg-3-uniprot.txt` for the curated Q9C1K8 by-similarity function, Rhea/EC mapping, and
  endoplasmic-reticulum membrane localization.
- `interpro/panther/PTHR12646/`, especially the completed PTHR12646 family review, the
  2026-05-28 PAINT IBD rows at `PANTHER:PTN000291297`, and the entries table placing Q9C1K8
  in `PTHR12646:SF0`.
- The reviewed S. cerevisiae `ALG3` and S. pombe `alg3` YAML files from `origin/main`, as
  anchors for the experimental fungal biology behind the family review.

No same-species experimental characterization of Neurospora crassa `alg-3` was found in
the local publication cache. A 2026-11-06 web search for `NCU06552`, `Q9C1K8`, and
`Neurospora alg-3` likewise only turned up product/catalogue pages or comparative genome
mentions that reuse the UniProt/PANTHER assignment rather than new alg-3 biochemistry or a
Neurospora knockout phenotype.

Conservative curation decisions:

- Accept the specific `GO:0052925` transferase activity, ER/ER-membrane localization, and
  direct `GO:0006488` dolichol-linked oligosaccharide biosynthetic process.
- Modify generic `mannosyltransferase activity` and `glycosyltransferase activity` to
  `GO:0052925`.
- Keep `protein N-linked glycosylation` and `glycoprotein biosynthetic process` as broad,
  non-core pathway context, because alg-3 builds the LLO donor used for N-glycoproteins but
  its direct step is the first Dol-P-Man-dependent lumenal mannose addition.
