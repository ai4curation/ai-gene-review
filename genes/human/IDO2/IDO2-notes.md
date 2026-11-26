# IDO2 manual notes

## Research provenance

`just deep-research-falcon human IDO2 --fallback perplexity-lite` failed because
the configured wrapper only exposed the `claude_code` provider and neither the
Falcon nor Perplexity provider was available. No provider-authored
`IDO2-deep-research-*.md` file was written; this note records the manual
literature synthesis instead.

## Evidence summary

- IDO2 is the vertebrate PTHR28657:SF4 paralog of IDO1. The local
  PTHR28657-entries inventory places human IDO2 Q6ZQW0, mouse Ido2 Q8R0V5 and
  rat Ido2 F1LV46 in SF4, with human IDO1 in the sister SF2 branch.
- Ball et al. discovered the INDOL1/IDO2 paralog adjacent to IDO1 in mammalian
  genomes and showed that INDOL1/IDO2 converts tryptophan to kynurenine
  [PMID:17499941, "We demonstrate that INDOL1 catalyses the conversion of
  tryptophan to kynurenine"].
- Metz et al. directly assayed human IDO2 and reported IDO-like tryptophan
  catabolism plus common human R248W/Y359X alleles that reduce or abolish
  activity [PMID:17671174, "Like IDO, IDO2 catabolizes tryptophan"].
- UniProt records the same chemistry as `Reaction=L-tryptophan + O2 =
  N-formyl-L-kynurenine;` and annotates a heme cofactor and conserved proximal
  heme iron ligand by similarity to IDO1.
- The human IDO2 enzyme is weak compared with IDO1. Yuasa et al. interpreted
  IDO2 as a conserved low-efficiency vertebrate branch
  [PMID:25950090, "low efficiency IDO2 enzymes have been conserved throughout
  vertebrate evolution"], and Loeb et al. found in human tumor samples that IDO1
  supplied the detectable tryptophan degradation
  [PMID:18418598, "tryptophan degradation is entirely provided by IDO1"].
- Lee et al. reported that overexpressed human IDO2 can suppress co-expressed
  IDO1 through a heme-binding-site-dependent effect
  [PMID:25394548, "hIDO2 plays a novel role as a negative regulator of hIDO1 by
  competing for heme-binding with hIDO1"]. This supports the heme site but is an
  artificial HEK293 co-expression system, so it was not promoted to a new GO
  biological-process annotation.

## Curation decisions

- `GO:0033754` and `GO:0006569`: accept. Human IDO2 directly catalyzes the
  L-tryptophan to N-formylkynurenine entry reaction even though the enzyme is
  weak and often disabled by coding variants.
- `GO:0004833`: modify to `GO:0033754`, matching the IDO1 review. The Rhea and
  PAINT rows have the correct reaction chemistry but use the TDO-labelled term
  instead of the IDO-specific term.
- `GO:0034354`: mark over-annotated. The row is propagated from yeast BNA2 at
  the PTHR28657 root and is too strong for human IDO2, which is not an
  established committed contributor to de novo NAD biosynthesis.
- The existing `kynurenine_nad_de_novo` module already includes the established
  human first-step enzymes TDO2 and IDO1. IDO2 is deliberately left out because
  its low, polymorphic activity and unresolved physiological substrate do not
  make it a substantive pathway part for that module.
- `gocams/index.tsv` has no production human IDO2 annoton, and the family does
  not require a GO-CAM review in this content PR.
