# queA review notes (E. coli K-12, P0A7F9)

Created for the bacterial preQ1 incorporation and queuosine maturation module,
which needed reviewed exemplars outside *Pseudomonas*.

## Provenance of this review

- No deep-research provider was available in this environment (no provider API
  keys), so no `-deep-research-<provider>.md` file exists or was fabricated.
  The review was built from the reviewed UniProt record and the cached
  publications below.
- Literature checked, all abstract-only in the cache except the proteome paper:
  PMID:8347586 (oQ synthesis from preQ1-tRNA, the IDA and IMP rows),
  PMID:12731872 (steady-state kinetics, the second IDA row), PMID:1706703 (the
  queA gene identified by complementation), PMID:27718375 (radiation-survival
  screen), PMID:18304323 (cytosol proteome, full text cached; QueA is not named
  in the parsed text).

## Function

- QueA transfers and isomerizes the AdoMet ribosyl moiety onto preQ1 at
  position 34, giving epoxyqueuosine. [file:ECOLI/queA/queA-uniprot.txt
  "Transfers and isomerizes the ribose moiety from AdoMet to the
  7-aminomethyl group of 7-deazaguanine (preQ1-tRNA) to give epoxyqueuosine
  (oQ-tRNA)."]
- One AdoMet-dependent step does the whole job. [PMID:8347586 "The enzyme QueA
  synthesizes oQ from preQ1 in a single S-adenosylmethionine- (AdoMet-)
  requiring step"] [PMID:8347586 "We propose that QueA is an
  S-adenosylmethionine:tRNA ribosyltransferase-isomerase."]
- Ordered sequential bi-ter mechanism, preQ1-tRNA first. [PMID:12731872 "fully
  ordered sequential bi-ter kinetic mechanism in which preQ(1)-tRNA(Tyr) binds
  first followed by AdoMet"]
- The gene was found by complementing a queuosine mutation downstream of Tgt.
  [PMID:1706703 "This gene was designated queA."]
- Monomer. [file:ECOLI/queA/queA-uniprot.txt "SUBUNIT: Monomer."]

## Curation decisions

- `GO:0009314` response to radiation is `KEEP_AS_NON_CORE`. The queA knockout
  is a hit in a genome-wide radiation-sensitivity screen with no mechanism
  given; this most likely reflects the general fitness cost of lacking tRNA
  queuosine under stress rather than a dedicated QueA role, and the row's
  `acts_upstream_of_or_within` qualifier already keeps it loose. A
  `suggested_experiments` entry proposes comparing queA, tgt and queG
  deletions to settle it.
- `GO:0016740` and `GO:0016853` were both refined to `GO:0051075`, which
  records the coupled transfer-and-isomerization chemistry. `GO:0051075` is a
  direct `is_a` child of `GO:0016853` in the current ontology (its OBO stanza
  asserts `is_a: GO:0016853 ! isomerase activity`, alongside `GO:0016757` and
  `GO:0140101`), so this is refinement, not a lateral move.
- `GO:0006400` was refined to `GO:0008616` and `GO:0005737` to `GO:0005829`.
- QueA seeds the PTHR30307 PAINT node, so it is also the reference protein of
  `interpro/panther/PTHR30307/PTHR30307-review.yaml`.
