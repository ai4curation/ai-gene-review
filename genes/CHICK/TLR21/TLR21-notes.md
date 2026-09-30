# TLR21 (chicken, UniProt A0A8V0ZKW5) — curation notes

No `TLR21-deep-research-*.md` file was produced by the batch harness before this
review was written; these notes rest on the UniProt record, the GOA rows and the
cached publications.

## Entry identity (TrEMBL, unreviewed)

`A0A8V0ZKW5_CHICK` is an unreviewed, Ensembl-derived entry of 1083 aa, submitter
name "Toll like receptor 21", gene name TLR21, whose only cross-reference is
Ensembl ENSGALG00010023066 / ENSGALP00010034014. Ensembl gives that gene as
"TLR21 toll like receptor 21 [Source:NCBI gene; Acc:415623]" on chromosome 11, so
the entry is the right gene even though it carries no RefSeq or GeneID link of its
own. (The project's candidate table listed another accession, A0A8V0ZYL3; both are
Ensembl models of chicken TLR21.) The entry has a TIR domain (915..1055), five
LRR_8 repeats and one predicted transmembrane segment; its PANTHER subfamily is
PTHR24365:SF545, the same subfamily as zebrafish tlr21, which is consistent with
the TLR21/TLR22/TLR13 branch rather than with any mammalian TLR9 orthology.

Caveat worth recording: this Ensembl model is longer than the cDNAs used in the
functional literature, and the functional work was done on cloned chicken TLR21
rather than on this accession; the review therefore treats the published work as
evidence about the chicken TLR21 gene, which is what GO annotations are made to.

## Established biology

- Chicken TLR21 is a receptor for unmethylated CpG DNA and the functional
  counterpart of mammalian TLR9, which birds lack:
  [PMID:20498358 "Expression of chTLR21 in HEK293 cells resulted in activation of"]
  [PMID:20498358 "NF-kappaB in response to unmethylated CpG DNA"], and it also
  responded to bacterial genomic DNA. Independently,
  [PMID:19573927 "expression of TLR21 but"]
  [PMID:19573927 "not TLR7 or 15 resulted in marked NF-kappaB activation upon stimulation with"]
  [PMID:19573927 "exogenous ODN"], with the response reduced by RNA interference
  against TLR21 in chicken macrophages.
- It acts intracellularly, in the same compartments as human TLR9:
  [PMID:20498358 "Inhibition of the chTLR21 response by"]
  [PMID:20498358 "the endosomal maturation inhibitor chloroquine suggested that the receptor is"]
  [PMID:20498358 "functional in endolysosomes"]; and in resting cells
  [PMID:19573927 "confocal microscopy and digestion with endoglycosidase H suggest TLR21 localizes"]
  [PMID:19573927 "to the endoplasmic reticulum (ER) of resting cells"].
- Keestra notes that chTLR21 is absent from human, has homologues in fish and frog,
  and "displays similarity with mouse TLR13" — so its relationship to TLR9 is
  functional analogy, not orthology. The zebrafish TLR21 study reaches the same
  conclusion for the fish receptor (PMID:24282308).

## Annotation decisions (summary)

GOA has only five electronic rows for this entry; none is experimental, and none
mentions the CpG-DNA function.

- GO:0002224 (IBA) modified to GO:0035682 toll-like receptor 21 signaling pathway:
  the receptor-specific term exists and two independent studies show
  NF-kappa-B-dependent signalling initiated at this receptor by CpG DNA.
- GO:0038023 (IBA) modified to GO:0038187 pattern recognition receptor activity.
  Unmethylated CpG DNA is a pathogen-associated pattern; heterologous expression of
  the receptor confers responsiveness to it and knockdown removes it in chicken
  cells. GO:0045322 unmethylated CpG binding was considered and *not* proposed: no
  direct binding assay exists for the chicken receptor, and human TLR9 itself holds
  that term only by ISS/IEA, so proposing it here would be less well supported than
  the existing annotation on the mammalian receptor.
- GO:0005886 plasma membrane (IBA) modified to endosome: the ancestral node's donors
  are surface TLRs, whereas this receptor is ER-resident when resting and functions
  in endolysosomes, its activation being blocked by inhibitors of endosomal
  maturation.
- GO:0007165 and GO:0016020 kept as non-core.

Ligand-specificity question for the project: the transfer that would have been wrong
here — a TLR9 pathway or ligand term — is absent from GOA, and the correct
receptor-specific term (GO:0035682) exists and is now proposed. The general pattern
across the batch is that the numbered pathway terms are safe to use where the
receptor identity is unambiguous, whereas donor-specific *ligand* terms
(triacyl lipopeptide binding on chicken TLR15) are not.
