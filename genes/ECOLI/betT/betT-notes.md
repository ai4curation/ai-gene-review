# betT (E. coli K-12, P0ABC9) notes

## Sources read (2026-11-03)
- Cached abstracts: PMID:1956285, PMID:17322201 (fetched), PMID:3512526, PMID:15919996, PMID:11967071.
- Deep research: falcon failed (403); `just deep-research-openscientist ECOLI P0ABC9 --alias betT` produced `betT-deep-research-openscientist.md`, consistent with the review (proton-driven, high-affinity, osmo-activated choline carrier); cited on the MF row.

## Findings
- "betT encoding a proton-motive-force-driven, high-affinity transport system for choline" [PMID:1956285]
- 12 TM segments, cytoplasmic termini; osmotic upshock raises activity tenfold; the C-terminal domain is needed for activation [PMID:17322201].

## Decisions
- Core: GO:0015220 choline transmembrane transporter activity, GO:0015871 choline transport, plasma membrane.
- BCCT-family generic rows (GO:0022857, GO:0055085, GO:0016020) are MODIFIED to the specific terms. GO:0055085 -> GO:0015871 is lateral, because GO has no choline transmembrane transport term.
- The DNA damage response IEP (mitomycin microarray) is over-annotated.
- PANTHER PTHR30047:SF7 is not choline-specific (it also holds BetP, OpuD, BetL, EctP, TmaT), so neither the family nor that subfamily can define a choline-uptake selector.
