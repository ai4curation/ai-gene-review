# recC (P07648, E. coli K-12) curation notes

Author: Claude (AI-assisted), 2026-11-09.

Deep research was not run for this gene (no provider API keys were available in
this session). The summary below is drawn from the cached publications under
`publications/`, the UniProt record (`recC-uniprot.txt`) and a small sequence
motif scan (`recC-bioinformatics/RESULTS.md`). Almost all cached papers are
abstract-only (`full_text_available: false`); only PMID:21219465 has full text.

## Identity and complex

- RecC (exonuclease V gamma chain) is one of the three subunits of the RecBCD
  helicase-nuclease, which processes double-strand DNA ends [UniProtKB:P07648
  "Heterotrimer of RecB, RecC and RecD. All subunits contribute to DNA-binding"].
- The purified subunits reassemble into a holoenzyme indistinguishable from
  native RecBCD, but RecC alone has no detectable holoenzyme activity
  [PMID:1618858 "The RecB, RecC, and RecD subunits can associate in vitro to give
  nuclease, helicase, ATPase, and Chi-specific endonuclease activities which are
  indistinguishable from those of the RecBCD holoenzyme"; "none of the individual
  RecB, RecC, or RecD subunits have readily detectable activities of the
  holoenzyme, except RecB protein"].

## Role of RecC within RecBCD

- In the crystal structure the DNA duplex is split across RecC, and the 3' tail
  passes through a RecC tunnel, which provides the mechanism of Chi recognition
  [PMID:15538360 "the DNA duplex has been split across the RecC subunit to create
  a fork with the separated strands each heading towards different helicase motor
  subunits"; "Passage of the 3' tail through one of these tunnels provides a
  mechanism for the recognition of a Chi sequence by RecC within the context of
  double-stranded DNA"].
- RecBC and RecBCD bind duplex DNA ends and melt out about six base pairs in the
  absence of ATP [PMID:16126227 "both RecBC and RecBCD helicases can destabilize or
  "melt out" six base-pairs upon binding to a blunt DNA duplex end in the absence
  of ATP"].
- RecC is not a motor: RecB carries the slow 3'-5' helicase and nuclease, RecD the
  fast 5'-3' helicase, and RecC stimulates RecB and contributes to Chi recognition
  [UniProtKB:P07648 "RecC stimulates the ATPase and processivity of the RecB
  helicase and contributes to recognition of the Chi site"].
- Mutations in RecC change or abolish Chi recognition (UniProt MUTAGEN/VARIANT
  lines from PMID:22603794 and PMID:10884344, e.g. "Q->A: Acts at variant Chi
  sequences", "L->A: Does not act at Chi").
- Sequence scan: RecC has no Walker A motif, whereas RecB and RecD do
  (`recC-bioinformatics/RESULTS.md`). The helicase-like P-loop folds of RecC are
  therefore degenerate; there is no sequence basis for ATP binding by RecC.

## Biological processes

- RecBCD initiates DSB repair by homologous recombination and degrades linear
  foreign DNA; Chi switches it to recombination mode and RecA loading
  [PMID:19052323 "The RecBCD enzyme of Escherichia coli is a helicase-nuclease that
  initiates the repair of double-stranded DNA breaks by homologous recombination.
  It also degrades linear double-stranded DNA, protecting the bacteria from phages
  and extraneous chromosomal DNA."].
- recBC deletion mutants are viable but defective in repair and recombination
  [PMID:6389498 "exonuclease V, is not essential for the growth of E. coli but is
  important for DNA repair and recombination"].
- RecBCD unwinding feeds RecA/SSB homologous pairing in vitro [PMID:2014257
  "RecBCD enzyme initiates the process by unwinding the linear double-stranded DNA
  to produce single-stranded DNA, which is trapped by SSB and RecA"].
- In vivo recBC nuclease limits transfection by linear phage DNA [PMID:123277
  "the recBC nuclease can limit transfection at several stages during the
  production of an infective center"].
- Cas1 (YgbT) co-purifies with RecB and RecC [PMID:21219465 "Among the proteins
  co-purifying with YgbT (Suppl. Table 3) were RecB and RecC"].

## Curation decisions (summary)

- Molecular function: RecC's own activity is DNA (end) binding within RecBCD; it
  contributes to, but does not by itself enable, exodeoxyribonuclease V activity.
  The electronic and EcoCyc rows use `enables`; recorded as qualifier defects.
- `DNA helicase activity`, `catalytic activity, acting on DNA`: over-annotation of
  holoenzyme or motor-subunit activities on the non-motor subunit.
- `ATP binding`: removed (no Walker A, no binding site in the record; the ATPase
  is RecB's/RecD's).
- `DNA recombination` and `recombinational repair` are refined to
  `double-strand break repair via homologous recombination` (and, for the
  recombination rows, `homologous recombination`).
- Chi recognition is E. coli/enteric-specific; Pseudomonas RecBCD does not act at
  E. coli Chi (see genes/PSEPK/recC).
