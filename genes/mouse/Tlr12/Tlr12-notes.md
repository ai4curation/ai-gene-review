# Tlr12 (mouse, UniProt Q6QNU9, MGI:3045221) — curation notes

These notes rest on the UniProt record, the GOA rows and the cached publications;
the Falcon deep-research report arrived after the review was written and is
cross-checked at the end of this file.

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


## Deep-research cross-check (2026-09-30)

Compared `Tlr12-deep-research-falcon.md` against the finished review, and also read the
paralogue's report, because **both reports are written around the literature names and are
therefore inverted relative to the database symbols.** The `Tlr12` report is about
literature "TLR12" = Q6R5P0 = MGI Tlr11, and the `Tlr11` report is about literature
"TLR11" = Q6QNU9 = *this* entry. Material was mapped accordingly before comparison.

Agreement (from the `Tlr11` report, which is this gene): pattern-recognition receptor with
two protein ligands, Toxoplasma profilin and bacterial flagellin from uropathogenic
*E. coli* and *Salmonella*; intracellular endosomal/endolysosomal rather than surface
receptor; UNC93B1-dependent trafficking; MyD88-dependent signalling with this receptor as
the MyD88-recruiting member of the pair; IL-12 as the principal output; protection against
uropathogenic bacteria and against *Salmonella* entry into Peyer's patches; epithelial
expression in intestine, lung and skin; no functional human counterpart.

Additions taken up, each verified in a primary paper:

- **A fourth, independent identity check on the naming inversion, plus direct
  two-ligand binding data.** The report cites a 2016 paper that the review had not used;
  fetched as `publications/PMID_26859749.md`. It is unambiguously about this entry:
  [PMID:26859749 "amino acids M1 to S21 correspond to the signal sequence and amino acids T22 to S709 comprise the extracellular domain of the receptor consisting of 26 LRRs"],
  matching Q6QNU9's UniProt features (SIGNAL 1..21, TOPO_DOM 22..709) and not Q6R5P0's
  1..30 signal. It shows one receptor binding both PAMPs through different ectodomain
  regions: [PMID:26859749 "Thus only full-length TLR11-Flag interacts with His-TPRF, while both cleaved and full-length TLR11-Flag binds to His-FliC."]
  Added as `supported_by` on the GO:0038023 -> GO:0038187 MODIFY row.
- **Compartment nuance for the location call.** Flagellin recognition is placed in an
  acidic endolysosomal compartment
  [PMID:26859749 "Cathepsin-derived C-terminal region of TLR11 interacts with FliC within an acidic endolysosomal compartment."],
  which supports the proposed GO:0005768 endosome; but profilin binding needs the uncleaved
  receptor and is seen at neutral pH, so that event may occur before cleavage, possibly at
  the surface or in early endosomes. Recorded in the GO:0005886 MODIFY reason; the proposed
  replacement term is unchanged, and the existing suggested question about compartments
  already covers it.
- **The pair is not rodent-restricted.** Verified with
  [PMID:37874499 "equine TLR11 and TLR12 are transcribed genes and confirmed their expression in equine white blood cells"]
  and [PMID:23246311 "TLR12 sequences are present in the genomes of rodents, horses, and lemurs, but could not be detected in humans."].
  `description` corrected; human absence unchanged.
- **The transcriptional route is not simply NF-kappa-B.**
  [PMID:24078692 "neither NF-κB1 nor NF-κB2 were required for DC IL-12 production"]
  and [PMID:24078692 "our study uncovered a MyD88 and IRF8-dependent but NF-κB independent pathway in DCs for the induction of IL-12"].
  The `description`, the GO:0002224 summary and the core-function description no longer
  assert NF-kappa-B activation; a suggested question records the cell-type dependence.

Not taken up: the microneme protein MIC3 as a second *Toxoplasma* ligand (single 2023
report, no IL-12 induction, candidate only) and expression in testicular germ cells
(descriptive immunohistochemistry with no function), neither sufficient for a GO
annotation.

Actions: unchanged for every existing annotation and for the proposed GO:0009617. Changes
were confined to `description`, two `reason`/`summary` fields, three new `supported_by`
quotes, two new references and one new suggested question. The Falcon file itself is not
cited as annotation support, because its gene-name mapping is inverted; the validator
warning about unused deep research is accepted for that reason.
