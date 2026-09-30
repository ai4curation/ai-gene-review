# Tlr11 (mouse, UniProt Q6R5P0, MGI:3045226) — curation notes

Deep research (falcon) was requested for this gene by the batch harness but no
`Tlr11-deep-research-*.md` file was produced before this review was written, so
these notes are built from the UniProt record, the cached GOA rows and the cached
publications listed below.

## The Tlr11 / Tlr12 naming inversion (critical for every annotation here)

UniProt records the problem explicitly for both paralogues: "There is some
confusion regarding the nomenclature of this gene. In the literature, Tlr11 is
frequently referred to as Tlr12 and vice-versa"
(`file:mouse/Tlr11/Tlr11-uniprot.txt`). MGI records the same for the knockout
allele used in most of the literature (Tlr12<tm1Gho>, MGI:3045751): "Confusion
exists regarding the identity of Tlr11 and Tlr12. All of the references listed
below identify this allele as an allele of Tlr11. However, all of the associated
sequence information indicates that this is, in fact, an allele of Tlr12."

The direction of the inversion can be settled from sequence data in the cached
full texts, independently of what the papers call the proteins:

- Q6R5P0 (MGI **Tlr11**) begins `MPRMERHQFC SVLLILILLT ...`, has RefSeq
  NP_991388, and a 1..30 signal peptide.
- Q6QNU9 (MGI **Tlr12**) begins `MGRYWLLPGL LLSLPLVTGW ...`, RefSeq NP_991392,
  signal 1..21.

Koblansky et al. cloned the receptor they call TLR12 as
[PMID:23246311 "Analysis of the putative open reading frame of TLR12 (Gen-Bank accession number NP_991388.1)"]
— i.e. the entry MGI calls **Tlr11** — and note its construct "included the
signal sequence found in the first 30 amino acids", matching Q6R5P0's 1..30
signal. Raetz et al. give both cloning primers:
[PMID:24078692 "AAGTCGACGCCACCATGGGCCGCTACTGGCT"] for their "TLR11" (reading frame
ATG GGC CGC TAC TGG CT = M-G-R-Y-W, the Q6QNU9 N-terminus) and
[PMID:24078692 "AAGTCGACGCCACCATGCCCCGCATGGAGCG"] for their "TLR12"
(ATG CCC CGC ATG GAG CG = M-P-R-M-E, the Q6R5P0 N-terminus). Pifer et al. cloned
their "Tlr11" with [PMID:21097503 "GCTAGCATGGGCCGCTACTGGCTGCTGCCCG"], again the
Q6QNU9 N-terminus.

**Conclusion:** literature "TLR12" (Koblansky 2013, Raetz 2013) = Q6R5P0 = MGI
Tlr11 = *this gene*; literature "TLR11" (Zhang 2004, Yarovinsky 2005, Pifer 2011,
Mathur 2013) = Q6QNU9 = MGI Tlr12. UniProt's own reference sets agree: PMID:15001781
(uropathogenic bacteria) is cited under Q6QNU9 with FUNCTION and DISRUPTION
PHENOTYPE, not under Q6R5P0.

## What is established for the protein encoded by Q6R5P0

- It is an intracellular (endosomal/endolysosomal) TLR, not a surface receptor:
  [PMID:23246311 "suggesting that TLR12 also is guided to the endolysosomal system by Unc-93B1"];
  [PMID:23290966 "both TLR11 and TLR12 are endosomal TLRs and act as heterodimers in the recognition of Toxoplasma molecules"].
- It binds the *Toxoplasma gondii* profilin PAMP directly and forms homodimers and
  heterodimers with its paralogue:
  [PMID:24078692 "we observed strong interactions between TLR11 and TLR12, suggesting that these receptors can form a heterodimeric complex"].
  Raetz reports that both receptors interacted with profilin in a pH-dependent
  manner, but that of the pair
  [PMID:24078692 "only TLR11 is capable of recruiting MyD88 to the receptor complex"]
  — i.e. the MyD88-recruiting partner is Q6QNU9, and Q6R5P0 contributes
  recognition/dimerisation rather than adaptor recruitment.
- Loss of it impairs host resistance to *T. gondii*: that is the substance of
  [PMID:23246311 "TLR11 and TLR12 act as obligate heterodimers to activate NF-κB and produce IL-12 in response to TgPRF"]
  whose title states recognition of profilin by "TLR12" is critical for host
  resistance to *Toxoplasma gondii*.
- The receptor is rodent-restricted:
  [PMID:23246311 "TLR12 sequences are present in the genomes of rodents, horses, and lemurs, but could not be detected in humans"].

## Annotation decisions (summary)

- GO:0002224 (IBA) accepted. The numbered children GO:0034170 (TLR11 pathway) and
  GO:0034174 (TLR12 pathway) are *named after the literature receptors*, so which
  child belongs on which UniProt entry cannot be settled without a GO/MGI decision
  on the nomenclature; left as the unnumbered parent and raised as a question.
- GO:0038023 (IBA) modified to GO:0038187 pattern recognition receptor activity —
  the profilin PAMP is bound directly by both paralogues (Raetz), and GO:0038187 is
  the established MF for characterised TLRs (human TLR2, TLR5 and TLR9 all carry it
  by IDA).
- GO:0005886 plasma membrane (IBA from surface-TLR donors) modified to endosome:
  the phylogenetic transfer carried the donor clade's location, which is wrong for
  this UNC93B1-dependent intracellular receptor.
- GO:0009617 response to bacterium (IMP, PMID:15001781, WITH the *Tlr12* allele
  MGI:3045751) left UNDECIDED: the cited paper and allele belong to the paralogue on
  the sequence evidence above, but per repository policy an experimental annotation
  is not removed on paralog-attribution grounds by a reviewer who cannot see the
  curator's full reasoning. Flagged for MGI/GO resolution.
- GO:0005515 (IPI with *Salmonella* FliC, PMID:23101627) left UNDECIDED for the same
  reason: bare protein binding is uninformative, and the flagellin-binding receptor
  in that paper is the one named TLR11 (= Q6QNU9 on the primer/sequence evidence),
  while IntAct placed the interaction on Q6R5P0.
- NEW GO:0042832 defense response to protozoan proposed: Q6R5P0 is the receptor
  Koblansky calls TLR12, whose loss impairs IL-12 production and resistance to
  *T. gondii*; the paralogue already carries this term from the mirror-image paper.
