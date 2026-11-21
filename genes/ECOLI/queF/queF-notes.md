# queF review notes (E. coli K-12, Q46920)

Created for the bacterial preQ1 incorporation and queuosine maturation module,
which needed reviewed exemplars outside *Pseudomonas*.

## Provenance of this review

- No deep-research provider was available in this environment (no provider API
  keys), so no `-deep-research-<provider>.md` file exists or was fabricated.
  The review was built from the reviewed UniProt record and the cached
  publications below.
- Literature checked: PMID:15767583 (abstract only in the cache; the GOA IDA
  and IMP rows for this protein) and PMID:18304323 (cytosol proteome, full text
  cached; QueF is not named in the parsed text, so the curator's IDA row is
  deferred to).

## Function

- QueF reduces the nitrile of preQ0 to the primary amine of preQ1, consuming
  two NADPH. [file:ECOLI/queF/queF-uniprot.txt "Catalyzes the NADPH-dependent
  reduction of 7-cyano-7-deazaguanine (preQ0) to 7-aminomethyl-7-deazaguanine
  (preQ1), a late step in the queuosine pathway."]
- The recombinant E. coli and B. subtilis enzymes were cloned and assayed,
  which is how the activity was discovered. [PMID:15767583 "We have cloned the
  queF genes from B. subtilis and Escherichia coli and characterized the
  recombinant enzymes."]
- Specificity is high: a panel of aliphatic, aromatic, benzylic and
  heterocyclic nitriles is not used. [file:ECOLI/queF/queF-uniprot.txt "Is
  highly specific for its natural substrate preQ0, since it cannot use various
  aliphatic, aromatic, benzylic and heterocyclic nitriles"]
- Type 2 (unimodular) QueF subfamily, by HAMAP.
  [file:ECOLI/queF/queF-uniprot.txt "HAMAP; MF_00817; QueF_type2; 1."]

## Curation decisions

- `GO:0008616` is kept rather than refined to the de novo child `GO:0160253`:
  preQ1 made here also serves queuosine formation from salvaged preQ0, so the
  general term is the correct one. The same call was made on the sibling
  reviews (tgt, queA, queG).
- `GO:0005737` cytoplasm was refined to `GO:0005829` cytosol, which this
  protein already carries by IDA and by the PAINT node PTN002154489.
- The broad InterPro2GO parent `GO:0046857` was refined to `GO:0033739`, which
  the same entry carries with direct evidence.
- QueF seeds the PTHR34354 PAINT node, so it is also the reference protein of
  `interpro/panther/PTHR34354/PTHR34354-review.yaml`.
