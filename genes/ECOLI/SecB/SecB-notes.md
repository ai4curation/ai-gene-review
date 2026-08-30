# SecB review notes

## 2026-08-29: identity and core mechanism

SecB (UniProt P0AG86; *E. coli* K-12) is the cytosolic, tetrameric export chaperone
for a subset of Sec-dependent preproteins. Its core activity combines ATP-independent
antifolding/holdase behavior with delivery of the bound client to the defined acceptor
SecA at membrane export sites.

- Structural work directly shows that SecB is a cytosolic multitasking chaperone with
  unusually strong antifolding activity and that it maintains secretory proteins in an
  unfolded, secretion-competent state while targeting them to SecA
  [PMID:27501151, "SecB is a multitasking molecular chaperone in the cytosol that exhibits an unusually strong antifolding activity"]
  [PMID:27501151, "SecB is responsible for maintaining secretory proteins in an unfolded, secretion-competent state, as well as for their targeted delivery to the SecA ATPase"].
- NMR structures establish the physical basis: non-native proteins engage extended
  hydrophobic grooves and wrap around the SecB tetramer
  [PMID:27501151, "The most remarkable feature is that PhoA wraps around SecB in an overall arrangement that maximizes the interacting surface between the client protein, which is held in an unfolded conformation, and the chaperone."].
- Classic biochemical work directly describes the two coupled roles of stabilization
  and handoff to membrane-bound SecA
  [PMID:2170023, "SecB has a dual function in stabilizing the precursor and in passing it on to membrane-bound SecA, the next step in the pathway."].
- Purified SecB retards precursor-MBP folding and prolongs translocation competence
  [PMID:2848249, "The purified protein also quantitatively retarded folding of precursor MBP into a stable, protease-resistant conformation in the absence of membranes."].

These findings support GO:0140309, whose current official label is "unfolded protein
holdase activity" but whose definition remains carrier-specific: SecB binds an unfolded
client and escorts it to a defined acceptor/location. A general holdase NTR is therefore
not needed for SecB.

## 2026-08-29: qualifier-aware annotation audit

The GOA file contains 28 physical rows but 27 qualifier-aware signatures because the
PMID:15690043 protein-binding signature is repeated for two partners (CpxR/P0AE88 and
SecA/P10408). The review now contains all 27 signatures and records both partners on the
grouped row. Qualifiers are complete: 12 `enables`, 7 `involved_in`, 4
`acts_upstream_of_or_within`, 3 `located_in`, and 1 `is_active_in`.

Final action tally: 11 ACCEPT, 8 MODIFY, 7 KEEP_AS_NON_CORE, 1 REMOVE.

- Four obsolete GO:0051082 signatures are MODIFY to GO:0140309.
- Broad cytoplasm, protein transport, and intracellular localization annotations are
  narrowed to GO:0005829, GO:0043952, and GO:0006605 respectively; each replacement
  already exists as a separate GOA annotation.
- The electronic GO:0006457 protein-folding mapping is REMOVE because SecB prevents or
  retards folding rather than promoting it.
- GO:0051262 tetramerization and six generic GO:0005515 interaction signatures are
  retained as non-core. The interaction observations are not contradicted; generic
  protein binding is simply uninformative. The high-throughput CpxR observations are
  retained conservatively because the cited method-level text does not independently
  establish their functional significance.

## 2026-08-29: PAINT provenance

All five IBAs cite PANTHER node PTN002199630 with SecB itself as descendant evidence.
Current `interpro/panther/PTHR36918/PTHR36918-paint.tsv` retains GO:0005829,
GO:0070678, and GO:0043952 at that node. It no longer serializes GO:0036506 or obsolete
GO:0051082. The three current assertions are recorded as `NO_FAILURE_CORE`; the two
historical assertions are `SOURCE_STALE_OR_MISSING`. SecB's appearance in its own
WITH/FROM is expected descendant evidence, not circularity. Direct IMP/IDA studies
independently establish maintenance of unfolded protein, while the obsolete binding
claim is replaced by GO:0140309.

## 2026-08-29: evidence limitations

Only PMID:18304323, PMID:19402753, and PMID:27501151 have cached full text. The classic
mechanistic abstracts directly support the principal SecB claims, so curator deference
does not require UNDECIDED actions. Method-level quotations from PMID:15690043 and
PMID:19402753 do not independently verify the exact interaction pairs; those pairs are
therefore tracked from the qualifier-aware GOA provenance rather than overstated as
verified from the quotation alone.
