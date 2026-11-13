# STXBP1 (Munc18-1, P61764) review notes

## Conclusions

- Core MF is syntaxin-1 binding, in two modes: closed syntaxin-1 and the N-peptide/SNARE complex
  [PMID:17989281 "Munc18-1 interacts with neuronal SNARE proteins in two distinct modes"].
  The mechanism that matters is templating SNARE assembly with Munc13
  [PMID:23258414 "Munc13 opens syntaxin-1 and, together with Munc18-1, forms a template to bring the three SNAREs together"].
  I added a NEW GO:0030674 protein-macromolecule adaptor activity row for this. The rat Stxbp1 review uses the same term.
- It is essential for release [PMID:10657302 "Deletion of a single protein, Munc18-1, in mice leads to a complete loss of neurotransmitter secretion from synaptic vesicles throughout development."],
  and the brain still wires normally without it. That is why axon target recognition is marked over-annotated
  [PMID:10657302 "this does not prevent normal brain assembly, including formation of layered structures, fiber pathways, and morphologically defined synapses"].
- It is required for dense-core vesicle docking [PMID:11545717 "mutant cells displayed a 10-fold reduction in morphologically docked LDCVs"],
  so vesicle docking activity (GO:0160321) is accepted.
- The "regulation of SV priming/fusion" rows are MODIFIED to the processes themselves (GO:0016082, GO:0031629),
  because Munc18-1 is part of the machinery rather than a modulator of it.
- Negative regulation of protein-containing complex assembly is MODIFIED to GO:0035544 negative regulation of SNARE complex assembly
  [PMID:23258414 "Munc18-1 could displace SNAP-25 from syntaxin-1"].
- The platelet rows (PMID:12773094, abstract only) rest on Munc18-derived peptides. Degranulation is kept as non-core.
  Aggregation is marked over-annotated because it is a downstream consequence of secretion.
- All high-throughput bare protein-binding rows are REMOVED as uninformative. Row 17 (STX1A, PMID:26635000) is MODIFIED to syntaxin-1 binding
  [PMID:26635000 "there was no change in binding to Munc18a"].
- Identical protein binding is UNDECIDED: wild-type self-association could not be checked.

## Differences from the comparators

- Intracellular protein transport (IBA): KEEP_AS_NON_CORE here, MARK_AS_OVER_ANNOTATED in rat. The basis is syntaxin-1 delivery
  [PMID:17543282 "important role in stabilizing membrane delivery of Stx1A"]. The worm review also kept it as non-core.
- Response to estradiol: the human row is an IEA transfer of the rat expression response. MARK_AS_OVER_ANNOTATED here, KEEP_AS_NON_CORE for the rat IEP row.
