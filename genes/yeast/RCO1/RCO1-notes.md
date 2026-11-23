# RCO1 curation notes

## 2026 IBA re-review

Re-checked the two current RCO1 IBA annotations against GOA and the cached
`PTHR47636` PAINT table:

- `GO:0006357 regulation of transcription by RNA polymerase II` traces to
  `PANTHER:PTN001236278`, with budding-yeast RCO1 itself as the curated descendant
  evidence. The term is broad, but it is biologically sound for the Rpd3S subunit that
  helps suppress cryptic intragenic and antisense transcription during Pol II
  transcription, so the review now accepts it rather than proposing duplicate
  replacements to `chromatin organization` and `negative regulation of antisense RNA
  transcription`.
- `GO:0032221 Rpd3S complex` also traces to `PANTHER:PTN001236278`, supported by both
  the SGD Rco1 annotation and the two fission-yeast Rco1-family descendants in PomBase.

Both IBA rows are sound for RCO1, so the YAML now records the GOA `WITH/FROM` lists as
`supporting_entities` and adds PTN-level propagation reviews with the PTN ancestral node
as the source entity.

I also rechecked the cached high-throughput interaction publications behind the
`GO:0005515 protein binding` rows. They support physical associations, including Rpd3S
complex partners and chaperone/interactome hits, but not an evidence-backed replacement
molecular-function term. Those rows were changed from `KEEP_AS_NON_CORE` to `REMOVE`
under the current generic-protein-binding policy; that recommendation does not dispute
the reported interactions.

The newer-paper search found the 2023-2024 Rpd3S structural literature already discussed
in the Falcon deep-research report, but no later RCO1 paper that changes these IBA or
generic-protein-binding calls.

## PR follow-up

The 2026 Cell Reports Rpd3 nutrient-shift paper was already cached as PMID:42418323.
It is mainly an Rpd3L study, but its direct comparison with Rpd3S confirms that the
Rco1/Eaf3 complex safeguards active gene bodies rather than acting as the primary
canonical promoter regulator during nutrient transitions.

The broad `GO:0006357` IBA was left biologically sound but demoted to non-core so it
is not ranked above the more precise cryptic-initiation and chromatin-organization
rows. `GO:0006351` and `GO:0006334` were converted from contradictory
`KEEP_AS_NON_CORE` decisions to over-annotation calls because the first is a broad
keyword transfer for a chromatin subunit and the second describes assembly rather than
the maintenance/stabilization role supported by the Rpd3 core paper.

`core_functions` now separates Rco1's PHD histone-reader activity from its SID-MRG
Rpd3S scaffold role. GO has `GO:0140566 histone reader activity` for the PHD module;
the Rpd3S scaffold role is represented with `GO:0030674 protein-macromolecule
adaptor activity` rather than being folded into zinc binding.

## 2026-10-01 GOA / PAINT refresh

Refetched `Q04779` from GOA and UniProt and refreshed PTHR47636 from PAINT. The
PAINT export is unchanged: `PTN001236278` still carries the two RCO1 IBD rows,
`GO:0006357 regulation of transcription by RNA polymerase II` and
`GO:0032221 Rpd3S complex`, with budding-yeast Rco1 itself among the descendants
that seed both assertions. The existing IBA actions and PTN-level propagation
reviews remain appropriate.

The live GOA set has changed more on the non-IBA side. GOA now omits the older
UniProt keyword rows for `GO:0006325`, `GO:0006351`, `GO:0008270`, and
`GO:0046872`, and no longer carries the broad IntAct `GO:0005515 protein
binding` rows. Those rows are retained in the review file for provenance and
marked `retired: true`, rather than being deleted. Current GOA also adds a
ComplexPortal `part_of GO:0032221 Rpd3S complex` IPI row from PMID:17101441; this
was accepted as a redundant but correct confirmation of Rco1's core Rpd3S
membership.

During PR review, the retired UniProt-keyword `GO:0006325 chromatin organization`
row was replaced as live support by a `NEW` proposed row citing the Rpd3S primary
literature, so `GO:0006357`, `GO:0006351`, `GO:0006334`, and `core_functions`
no longer depend on an annotation absent from current GOA.

Searched the 2025-2026 public literature for `RCO1`/`YMR075W`/Rpd3S updates.
The newer hits were Rpd3S structural papers and reviews that refine Rco1 and
Eaf3 nucleosome engagement but do not change the reviewed GO surface.
