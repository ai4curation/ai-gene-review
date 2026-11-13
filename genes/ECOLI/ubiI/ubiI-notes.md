# ubiI review notes (E. coli K-12, P25535)

Reviewed for the ubiquinone_biosynthesis module (UbiH/VisC-family
2-polyprenylphenol 6-hydroxylase annoton).

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Built from the
  reviewed UniProt record, the cached abstract of PMID:23709220 and
  PMID:30686758, and the PTHR43876 PAINT table.

## Which hydroxylation

- UbiI is the C5 hydroxylase, the first of the three ring hydroxylations
  (2-octaprenylphenol to 2-octaprenyl-6-hydroxyphenol; GO:0019168).
  [PMID:23709220 "Based on genetic and biochemical experiments, we establish
  that the UbiI protein functions in the C5-hydroxylation reaction."]
- UbiH is the C1 hydroxylase (2-octaprenyl-6-methoxyphenol to the
  1,4-benzoquinol; GO:0008681) and UbiF the C6 hydroxylase
  (2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinol to 3-demethylubiquinol;
  GO:0008682). The module's assignments agree.
- UbiI acts only aerobically. [PMID:23709220 "We also demonstrate that UbiI is
  only implicated in aerobic Q biosynthesis and that an alternative enzyme
  catalyzes the C5-hydroxylation reaction in the absence of oxygen."]

## Decisions

- Generic monooxygenase / paired-donor oxygenase terms: MODIFY to GO:0019168.
- Flavin adenine dinucleotide binding: MODIFY to FAD binding (GO:0071949),
  which is kept as non-core.
- These choices follow the "correct but general is MODIFY" rule; the P. putida
  VisC draft instead used MARK_AS_OVER_ANNOTATED for the same rows.
