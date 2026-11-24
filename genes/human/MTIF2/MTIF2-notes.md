# MTIF2 notes

## Deep research

`MTIF2-deep-research-claude-code.md` (claude_code provider) ran for about 39 s with 3 web
searches and 9 citations (Kummer 2018, the Ma & Spremulli 1995 cloning paper, PDB entries,
a 2025 bioRxiv preprint, two PMC links). It was used as a list of leads only; no claim
in the review rests on it.

## Function

- Human knockout: [PMID:36629253 "The results of the [35S]-methionine/cysteine metabolic labeling
  indicated a near complete loss of mitochondrial translation in KO clones (Figure 3A and B), which
  was restored upon expression of mtIF2."]
- In vitro: [PMID:36629253 "Omission of mtIF2 severely inhibited [3H]-fMet-tRNAfMet binding to
  monosomes, showing that mtIF2 is crucial for the formation of the mitochondrial initiation complex."]
- Leaderless mRNAs are initiated mostly on 55S monosomes, mtIF2-dependent and mtIF3-independent
  (PMID:36629253). The same paper notes no experiment has tested whether mtIF2 has a
  subunit-association effect.
- Insertion domain replaces IF1 and stabilises leaderless mRNA [PMID:30089917 "By closing the
  decoding centre, this insertion stabilizes the binding of leaderless mRNAs"].
- fMet-tRNA preference (bovine) [PMID:15477394 "bovine IF-2(mt) has a 25-fold greater affinity for
  mitochondrial fMet-tRNA than Met-tRNA"]; 28S binding (bovine) [PMID:15935986].
- GTP dependence [PMID:8621449, PMID:2380177].

## Judgement calls

- GO:0001731 formation of translation preinitiation complex (IDA, PMID:36629253) modified to
  mitochondrial translational initiation, because GO:0001731 is defined as part of cytoplasmic
  translational initiation.
- GO:0032790 ribosome disassembly (ISS from bovine P46198) removed. The bovine IDA it is
  transferred from cites PMID:12095986, an IF3mt paper whose abstract attributes subunit
  dissociation to IF3mt. IF-2 family factors do not dissociate ribosomes. The bovine
  P46198 annotations from that paper (small subunit binding, translation factor activity,
  mitochondrial translational initiation, mitochondrion) look as if they may belong to IF3mt
  and are worth a curator check.
- Cytoplasm IBA marked as over-annotation (comes from the broad IF2/eIF5B node).
- No disease association for MTIF2 is established in OMIM/UniProt.
