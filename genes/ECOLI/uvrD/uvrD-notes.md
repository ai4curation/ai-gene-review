# uvrD (P03018, E. coli K-12 DNA helicase II) curation notes

Reviewer: Claude (AI-assisted)

## Deep research

No provider deep-research file is available for this gene (no provider API
access in this session). These notes were compiled from the cached
publications in `publications/`, the UniProt record `uvrD-uniprot.txt`, and the
PTHR11070 PAINT table. Literature checked: every PMID cited in the GOA file
(PMID:10543970, 10632890, 12527299, 1530937, 15375374, 15690043, 16135232,
16606699, 17641684, 17765269, 18304323, 2170128, 23695672, 24402227, 24561554,
2536658, 25883359, 27718375, 2942537, 31757945, 6135974, 6308634, 6319401,
8419285, 9482750). Most are abstract-only in the cache; PMID:18304323,
23695672, 24402227, 24561554, 25883359 and 31757945 have full text.

## Molecular function

- UvrD is DNA helicase II, an SF1A helicase/ssDNA-dependent ATPase
  [PMID:6135974 "The purified protein has single stranded DNA-dependent ATPase
  activity and ATP-dependent DNA helicase activity"; PMID:6319401 "Thus, it is
  concluded that the uvrD protein is identical with DNA helicase II and
  DNA-dependent ATPase I."].
- Polarity is 3' to 5', both for ssDNA translocation [PMID:2942537 "The
  translocation of helicase II along single-stranded DNA is unidirectional and
  in the 3' to 5' direction with respect to the DNA strand on which the enzyme
  is bound."] and for duplex unwinding [PMID:2170128 "The results suggest that
  DNA helicase II unwinds with 3'-5' polarity relative to the single strand of
  the DNA partial duplex."].
- A monomer translocates on ssDNA, while processive unwinding in vitro needs a
  dimer or a partner [PMID:12527299 "two UvrD monomers must bind the DNA
  substrate in order to form a complex that is able to unwind short DNA
  substrates in vitro."; PMID:25883359 single-molecule strand switching].
- The Walker A mutant uvrD252 (G30D) loses ATPase and helicase activity and is UV
  sensitive [PMID:8419285].

## Biological processes

- Nucleotide excision repair: after UvrBC incision, UvrD releases the excised
  oligonucleotide and UvrC [PMID:1530937 "Helicase II releases the damaged
  oligomer and UvrC from this complex, making repair synthesis possible"]. A
  second, debated role is backtracking of lesion-stalled RNA polymerase
  [PMID:24402227].
- Methyl-directed mismatch repair: required in the reconstituted system
  [PMID:6308634, "uvrE" is a historical uvrD allele name], loaded and made
  processive by MutL [PMID:9482750; PMID:31757945].
- Replication fork processing / anti-RecA: UvrD removes RecA from blocked forks,
  allowing fork reversal [PMID:15375374; PMID:16135232; PMID:17641684].
- Rolling-circle plasmid replication: replicative helicase for several RC
  plasmids [PMID:10632890].
- Recombinational repair (IBA, PTN000116141): seeded by RecB, Srs2 and Fbh1;
  UvrD itself acts mainly as an anti-recombinase [PMID:16135232] and has "an
  undefined role in the RecF recombination pathway" [PMID:9482750]. Marked as
  over-annotated.
- SOS response (EXP, PMID:2536658): uvrD mutants constitutively induce SOS,
  which the authors attribute to defective replication; uvrD is itself
  SOS-inducible [PMID:6319401]. Neither makes UvrD a participant of the SOS
  response; marked as over-annotated.

## Decisions summary

Core: GO:0043138 3'-5' DNA helicase activity in NER (GO:0006289) and
mismatch repair (GO:0006298); second core activity GO:0015616 DNA translocase
activity in replication fork processing (GO:0031297). Generic helicase terms
modified to GO:0043138; bare protein-binding rows removed except the RNA
polymerase rows (modified to GO:0043175).
