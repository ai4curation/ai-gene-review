# Tlr11 (mouse, UniProt Q6R5P0, MGI:3045226) — curation notes

These notes are built from the UniProt record, the cached GOA rows and the cached
publications listed below; the Falcon deep-research report arrived after the review
was written and is cross-checked at the end of this file.

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


## Deep-research cross-check (2026-09-30)

Compared `Tlr11-deep-research-falcon.md` against the finished review. **The report
is written around the literature name, not the database symbol.** Its subject is the
receptor the literature calls TLR11, i.e. Q6QNU9 / MGI Tlr12, so most of its content
(Hatai's flagellin and profilin binding assays, the MIC3 candidate ligand, the testis
expression survey) belongs to the paralogue's review and was cross-filed there. The
report never states the inversion; it only remarks that the gene "was historically
also referred to as" the other name.

Agreement, for the parts that are about this entry (the report's "TLR12" statements
and the family-level material): intracellular endosomal/endolysosomal rather than
surface localisation; UNC93B1 dependence; direct profilin binding by the ectodomain
at endolysosomal pH; obligate heterodimer with the paralogue in conventional
dendritic cells and macrophages; MyD88-dependent signalling with the paralogue
supplying MyD88 recruitment; IL-12 as the defining output; absence of a functional
human counterpart. These all match decisions already in the review.

Additions taken up, each verified in a primary paper:

- **The pair is not rodent-restricted.** The report's phylogenetic section (citing a
  2024 equid comparative-genomics paper) contradicted the review's "rodent-restricted"
  wording. Verified directly in the cached primary sources:
  [PMID:23246311 "TLR12 sequences are present in the genomes of rodents, horses, and lemurs, but could not be detected in humans."]
  and [PMID:37874499 "equine TLR11 and TLR12 are transcribed genes and confirmed their expression in equine white blood cells"].
  `description` corrected; the human absence, which is the point that matters for the
  annotations, is unchanged.
- **The transcriptional route is not simply NF-kappa-B.** The report's Tlr12 counterpart
  flagged an IRF8-dependent, largely NF-kappa-B-independent IL-12 pathway. Verified in
  the cached full text:
  [PMID:24078692 "our study uncovered a MyD88 and IRF8-dependent but NF-κB independent pathway in DCs for the induction of IL-12"]
  and [PMID:24078692 "neither NF-κB1 nor NF-κB2 were required for DC IL-12 production"],
  against [PMID:23246311 "TLR11 and TLR12 act as obligate heterodimers to activate NF-κB and produce IL-12 in response to TgPRF"].
  The `description`, the GO:0002224 summary and the core-function description no longer
  assert NF-kappa-B activation as the route; a suggested question records the cell-type
  dependence. No GO annotation changed, since no NF-kappa-B regulation term was
  annotated or proposed.

Not taken up: the report's claims about plasmacytoid-dendritic-cell homodimer function
and about this receptor being more essential than its paralogue are Koblansky findings
stated under the inverted name, and the review already records the homodimer capability;
no annotation turns on them. The MIC3 candidate ligand and the testis expression are
paralogue-side and in any case too preliminary for a GO annotation.

Actions: unchanged for every existing annotation and for the proposed GO:0042832. Changes
were confined to `description`, two narrative fields and one new suggested question. The
Falcon file is deliberately **not** cited as `supported_by` on any annotation, because its
gene-name mapping is inverted and a reader following the citation would be misled; the
validator warning about unused deep research is accepted for that reason.
