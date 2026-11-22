# GALNT1 (GalNAc-T1) — curation notes

## 2026-09-17 — de novo review

No `-deep-research-PROVIDER.md`: tooling unavailable (OpenAI key rejected);
nothing self-authored was named as provider output. Grounded in the cached
publications plus two papers fetched during review.

### Core activity and the paralogue problem

Four independent IDAs support `GO:0004653`. The specificity study is the one that
matters for how far the term may be pushed: [PMID:9295285 "The enzymes have
distinct but partly overlapping specificities with short peptide acceptor
substrates"] and [PMID:9295285 "GalNAc-T1 and -T3 showed strict donor substrate
specificities for UDP-GalNAc"].

The family-level IBA is well placed (36 WITH/FROM entries spanning fly, worm,
mouse, rat, Xenopus and fourteen human paralogues) but it asserts the *shared*
activity. What distinguishes the twenty human GALNTs is **which peptide sites
each prefers**, and GO does not currently express that. This is the axis on which
paralogue over-annotation in this family would occur; raised in
`suggested_questions`.

### Golgi localisation — prefer the GALNT1-specific reference

Originally the Golgi rows leaned on PMID:12506059, an isoform-antibody survey of
ocular surface epithelia (rated `relevance: MEDIUM` here). UniProt's own
`RP SUBCELLULAR LOCATION` reference for the entry is better and is now cited:

- [PMID:9394011 "In this study, we have localized endogenous and epitope-tagged
  human GalNAc-T1, -T2 and -T3 to the Golgi apparatus in HeLa cells by
  subcellular fractionation, immunofluorescence and immunoelectron microscopy."]
- [PMID:9394011 "We show that all three GalNAc-transferases are concentrated
  about tenfold in Golgi stacks over Golgi associated tubular-vesicular membrane
  structures."]

Three independent methods, GALNT1-specific. The "throughout the Golgi stack"
finding also supports `GO:0032580 Golgi cisterna membrane`.

Note `GO:0000139 Golgi membrane` and `GO:0032580 Golgi cisterna membrane` are
**not** parent/child: `GO:0000139` is not among `GO:0032580`'s ancestors under
`is_a` or `is_a,part_of` (checked via QuickGO). Both are kept.

### Extracellular region — downgraded, and why

`GO:0005576` was initially ACCEPTed on the reasoning that UniProt models the
soluble form as its own curated chain (`41..559`, PRO_0000012257) rather than as
an alternative location for the intact enzyme, making it a deliberate curatorial
act. That treated an assertion as evidence. Three checks changed the call:

1. The UniProt `Secreted` line carries **no ECO code**. (So does the competing
   Golgi location line, so the absence of a code is not by itself the
   discriminator — the difference is that the Golgi location has independent
   experimental support and the secreted one has none.)
2. No GALNT1-specific secretion or extracellular-localisation study was found.
3. The shedding mechanism that would justify the term is characterised, and
   GALNT1 is not among the enzymes it was shown for:
   [PMID:35279766 "secretion of select novel substrates such as the key
   mucin-type O-glycosylation enzyme GALNT2 is dependent on endogenous SPPL3
   protease activity"].

**GALNT1 has zero word-boundary mentions in PMID:35279766** — apparent hits are
substrings of *B4GALNT1*. Worth recording because the substring trap is easy to
fall into when grepping a family name.

Marked `MARK_AS_OVER_ANNOTATED` rather than removed: the mechanism is real
([PMID:35279766 "Secretion of soluble Golgi enzymes that are released from their
membrane anchor by endoprotease activity is a wide-spread yet largely unexplored
phenomenon"]), so a shed GALNT1 species remains plausible, just unshown.

### Viral protein processing

`GO:0019082` comes from Reactome's SARS-CoV-2 model (GALNT1 glycosylating ORF3a).
Marked over-annotated: the enzyme's activity does not change with the provenance
of its acceptor, and the same reasoning would give every constitutively expressed
Golgi enzyme a virus-specific annotation. The ERGIC location row from the same
model is kept as non-core, since a location claim is a different kind of thing
from a process claim.

### Abstract-only caution exercised

PMID:16638743 is a GalNAc-T3/FGF23 paper cited as an IDA on GALNT1,
abstract-only in the cache. Marked `UNVERIFIED` rather than MISCITED and the
annotation ACCEPTed: a selectivity claim of that kind is normally established
against a panel of isoforms, so a GalNAc-T1 comparator assay is very likely in
the full text the curator read, and the asserted activity is independently
certain for this gene.
