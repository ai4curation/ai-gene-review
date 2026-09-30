# Tlr12 (mouse, UniProt Q6QNU9, MGI:3045221) — curation notes

Deep research (falcon) was requested for this gene by the batch harness but no
`Tlr12-deep-research-*.md` file was produced before this review was written, so
these notes rest on the UniProt record, the GOA rows and the cached publications.

## Naming: this entry is the receptor the literature calls "TLR11"

Both UniProt entries of the pair carry the caution "There is some confusion
regarding the nomenclature of this gene. In the literature, Tlr12 is frequently
referred to as Tlr11 and vice-versa"
(`file:mouse/Tlr12/Tlr12-uniprot.txt`). The direction can be fixed from sequence
data in the cached full texts:

- Q6QNU9 (MGI **Tlr12**, this gene) starts `MGRYWLLPGL ...`, RefSeq NP_991392,
  signal peptide 1..21.
- Q6R5P0 (MGI **Tlr11**) starts `MPRMERHQFC ...`, RefSeq NP_991388, signal 1..30.

Cloning primers published for the receptors called TLR11 encode the Q6QNU9
N-terminus: [PMID:21097503 "GCTAGCATGGGCCGCTACTGGCTGCTGCCCG"] and
[PMID:24078692 "AAGTCGACGCCACCATGGGCCGCTACTGGCT"] (ATG GGC CGC TAC TGG = M-G-R-Y-W),
while the primer for the receptor called TLR12 encodes the Q6R5P0 N-terminus
[PMID:24078692 "AAGTCGACGCCACCATGCCCCGCATGGAGCG"]. Koblansky's "TLR12" open reading
frame is [PMID:23246311 "Analysis of the putative open reading frame of TLR12 (Gen-Bank accession number NP_991388.1)"],
again the other entry. MGI records the widely used knockout allele as
Tlr12<tm1Gho> (MGI:3045751) with the note that every reference identifies it as a
Tlr11 allele while all associated sequence information indicates an allele of
Tlr12 — consistent with the same inversion. UniProt likewise cites PMID:15001781
under this entry for FUNCTION, TISSUE SPECIFICITY and DISRUPTION PHENOTYPE.

So the literature on "TLR11" — uropathogenic bacteria (Zhang 2004), Toxoplasma
profilin (Yarovinsky 2005, Pifer 2011), flagellin (Mathur 2013) — is about this
gene product.

## Established biology of Q6QNU9

- Ligand-restricted innate receptor, not responsive to the standard TLR agonist
  panel: [PMID:15001781 "Cells expressing TLR11 fail to respond to known TLR ligands but instead respond"]
  specifically to uropathogenic bacteria; knockouts are
  [PMID:15001781 "susceptible to infection of the kidneys by uropathogenic bacteria"].
- The bacterial ligand was later identified as flagellin:
  [PMID:23101627 "Flagellin binds TLR11 and induces innate responses in mice independent of TLR5."]
  and [PMID:23101627 "Flagellin is also the TLR11 ligand from UPECs."].
- It is also the receptor for apicomplexan profilin:
  [PMID:15860593 "TLR11 is required in vivo for parasite-induced IL-12 production"];
  loss impairs the anti-Toxoplasma response
  [PMID:19050265 "TLR11-deficient mice developed dramatically reduced serum IL-12 levels"].
- It is an intracellular receptor that depends on UNC93B1:
  [PMID:21097503 "we show that TLR11, an innate sensor for the Toxoplasma protein profilin, is an"]
  intracellular receptor residing in the endoplasmic reticulum, and
  [PMID:23290966 "both TLR11 and TLR12 are endosomal TLRs and act as heterodimers in the recognition of Toxoplasma molecules"].
- Of the pair, this entry is the MyD88-recruiting member:
  [PMID:24078692 "only TLR11 is capable of recruiting MyD88 to the receptor complex"].

## Annotation decisions (summary)

- GO:0002224 (IBA) accepted; the numbered children GO:0034170/GO:0034174 are named
  after the literature receptors and cannot be assigned until GO and MGI settle the
  inversion (raised as a question, identically to the paralogue's review).
- GO:0038023 (IBA) modified to GO:0038187 pattern recognition receptor activity:
  two chemically defined PAMPs (flagellin, parasite profilin) are bound directly.
- GO:0005886 plasma membrane (IBA) modified to endosome — this is an
  ER/endolysosomal, UNC93B1-dependent receptor; the donor set of the PAINT node is
  surface TLRs.
- GO:0042832 defense response to protozoan (IMP, PMID:19050265, allele MGI:3045751)
  accepted: allele and paper both belong to this gene on the evidence above.
- NEW GO:0009617 response to bacterium proposed, the counterpart of the row sitting
  on the paralogue: the knockout of *this* allele is susceptible to uropathogenic
  bacteria and the receptor binds bacterial flagellin directly.
- Generic IEA rows (GO:0007165, GO:0016020, GO:0051707) kept as non-core.
