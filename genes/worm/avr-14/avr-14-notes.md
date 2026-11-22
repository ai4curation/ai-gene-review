# avr-14 curation notes

## 2026-11-22

`just fetch-gene worm avr-14` seeded 21 GOA rows for UniProtKB Q8IFY7. The
accession is the C. elegans `avr-14`/`B0207.12` record and is unreviewed in
UniProtKB/TrEMBL, so the review uses it for the identifier and Cys-loop domain
context rather than for curated channel function.

Reviewer follow-up showed that Q8IFY7 itself is a 239-aa partial protein model:
the record has a signal peptide and Cys-loop ligand-binding domain, but lacks
the four transmembrane helices expected for a full-length Cys-loop channel.
The channel, chloride-transport and plasma-membrane calls in the review
therefore describe the full-length AVR-14B splice form cloned and expressed by
Dent et al., not the truncated sequence on the seeded TrEMBL record.

Follow-on fetches:

- `just fetch-gene-pmids worm avr-14` found PMID:10716995, PMID:12750328 and
  PMID:16527366; all were already cached.
- `just mod-description-deep-research worm avr-14` fetched the WormBase curated
  description as `avr-14-deep-research-wormbase.md`.
- `just paint-losses worm avr-14` reported that Q8IFY7 is in PTHR18945 but not a
  leaf of the PAINT tree, and no IRD or IKR losses are available on this
  lineage.
- `just deep-research-falcon worm avr-14 --fallback perplexity-lite` could not
  run here because the deep-research client reported that only `claude_code` was
  available and `agentapi` was missing; no provider deep-research file was
  written.

Dent et al. is full text in the local cache and is the main evidence source. It
cloned `avr-14`, identified it with the previously cloned `gbr-2` GluCl gene,
showed that the AVR-14B splice form produces robust glutamate and ivermectin
responses in Xenopus oocytes, and placed `avr-14`, `avr-15` and `glc-1` in
parallel ivermectin-sensitivity pathways [PMID:10716995, "Oocytes expressing
transcript B gave a robust response to both ivermectin and glutamate";
PMID:10716995, "simultaneous mutation of three genes, avr-14, avr-15, and
glc-1"].

The same paper is enough for the generic transport and membrane rows. The
direct IDA `GO:0006811` and `GO:0016020` rows are refined to chloride
transmembrane transport and plasma membrane because the electrophysiological
assay required functional AVR-14B at the oocyte surface. The InterPro generic
transport and membrane rows are retained as true but imprecise ancestors of the
specific accepted claims.

PMID:12750328 is abstract-only in the local cache but supports the pharyngeal
pumping rows: adult tail tap inhibits pumping through `unc-7` and
glutamatergic pathway genes `avr-14` and `avr-15`. PMID:16527366 is also
abstract-only and supports the locomotion rows by reporting that four C.
elegans GluCl alpha subunits regulate locomotor pattern and that H. contortus
GluClalpha3 can restore normal motor movement in the C. elegans `avr-14` mutant
from the `avr-14` promoter.

The GO-CAM `GO:0060079` excitatory-postsynaptic-potential row repeats the same
GO parentage problem corrected in the `glc-1` and `glc-2` reviews:
`GO:0008068 extracellularly glutamate-gated chloride channel activity` is the
right molecular function for AVR-14, but GO currently places the GluCl term
under an excitatory glutamate-gated parent. I kept `GO:0008068`, removed the
sign-wrong excitatory row, and left the proposed ontology change on
`GO:0005234` in the review so the source of the propagation is explicit.
