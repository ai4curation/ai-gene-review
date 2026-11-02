# Eb1 (A1Z6P3, FBgn0027066) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Eb1 is reviewed as the closest experimentally characterised SF6 relative of the ProtNLM2
benchmark gene Mst27D (Q8IPI4). No ProtNLM2 output was consulted.

### Deep research
`just deep-research-falcon DROME Eb1 --fallback perplexity-lite` failed. Falcon failed authentication,
and perplexity-lite returned HTTP 401 (quota exceeded). No deep-research file exists. The review is
based on the 17 cached GOA publications (11 full text, 6 abstract-only).

### Evolutionary grounding
- PANTHER v19 (`.cache/panther/PTHR19.0_fruit_fly`) places Eb1 in PTHR10623:SF6 ("EB1, ISOFORM
  F-RELATED"), together with Mst27D, CG18190 (EB-SUN), CG32371, CG2955 and CG15306. Human MAPRE1,
  MAPRE2 and MAPRE3 are in SF20, SF7 and SF10. SF6 is a fly-lineage expansion, and Eb1 has no
  one-to-one human ortholog at subfamily level.
- All IBAs come from the eukaryote-wide node PTN000065701 (taxon 2759;
  `interpro/panther/PTHR10623/PTHR10623-paint.tsv`). Eb1 (FB:FBgn0027066) is itself an
  experimental seed for GO:0051010 microtubule plus-end binding and GO:0051225 spindle assembly.
- The functions treated as core are all shown experimentally in Drosophila: plus-end comets
  [PMID:12213835 "Dm EB1 staining clearly coincided with individual microtubules and exhibited a
  comet-like gradient of staining"], loss of dynamics after RNAi [PMID:12213835], recruitment of
  Sentin [PMID:21646401], Shot [PMID:15699215] and CLIP-190 [PMID:16105886], and spindle
  defects [PMID:12213835].
- Not established in flies: the cargo-binding crystal structure and mutagenesis in PMID:15699215
  are of human EB1. Homodimerization is inferred from that work and from the conserved coiled coil;
  it was not annotated.

### Decisions (summary)
- Core: microtubule plus-end binding; microtubule plus-end location; regulation of microtubule
  polymerization or depolymerization; protein localization to microtubule plus-end (refined from
  the IBA protein localization to microtubule); spindle assembly and mitotic spindle elongation.
- MODIFY (general terms refined): microtubule and cytoskeleton to microtubule plus-end; microtubule
  binding to plus-end binding; microtubule cytoskeleton organization and regulation of microtubule
  cytoskeleton organization to GO:0031110.
- MARK_AS_OVER_ANNOTATED (organismal or indirect phenotypes): sensory perception of sound,
  locomotory behavior, flight behavior, wound healing, melanotic encapsulation, and pseudocleavage.
  For pseudocleavage, the authors themselves argue that the defects are secondary to spindle
  disruption [PMID:19279137 "these caps were associated with, and might be the result of, severe
  spindle disruptions"].
- REMOVE: the three GO:0005515 protein binding rows (Shot, DIA, CG32371), under the protein-binding
  policy.

### Notes for transfer to Mst27D and other SF6 paralogs
Only the deep, node-level EB1 functions (plus-end binding and plus-end-dependent regulation of
dynamics) have phylogenetic support across SF6. Cargo recruitment via the C-terminal EBH domain and
EEY tail depends on conserved C-terminal residues, which should be checked in each paralog before
transfer. EB-SUN partially substitutes for EB1 in oogenesis but not in embryogenesis [PMID:39475714].
