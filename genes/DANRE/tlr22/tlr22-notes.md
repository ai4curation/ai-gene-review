# tlr22 (zebrafish, UniProt A0A2R8RTN4) — curation notes

No `tlr22-deep-research-*.md` file was produced by the batch harness before this
review was written; these notes rest on the UniProt record, the GOA rows and the
cached publications. This is the thinnest evidence base of the eight genes reviewed
in this batch, and the review is correspondingly conservative.

## Entry identity (TrEMBL, unreviewed)

`A0A2R8RTN4_DANRE`, 955 aa, submitter name "Toll-like receptor 22 precursor", gene
name tlr22 (synonym TLR21.2), cross-referenced to RefSeq NP_001122147, GeneID 403135
and ZFIN ZDB-GENE-040220-5. NCBI gene 403135 is "tlr22 toll-like receptor 22" on
chromosome 21, so this is the right gene. Features: signal peptide 1..30,
transmembrane 749..774, TIR domain 801..942, leucine-rich repeats with a
cysteine-rich flanking region. Its PANTHER subfamily assignment is
PTHR24365:SF522 "LOW QUALITY PROTEIN: TOLL-LIKE RECEPTOR 13-RELATED", which is
consistent with the phylogenetic placement of tlr22 in the TLR21/TLR22/TLR13 branch
and is a family name, not a statement about this protein's quality.

GOA holds only four rows: two electronic, and two IDA rows from ZFIN citing
expression studies.

## Established biology

For zebrafish tlr22 specifically, almost everything available is transcript-level:

- [PMID:22729906 "Immunostimulation experiments revealed that expression of zebrafish tlr22 is"]
  [PMID:22729906 "modulated by several unrelated PAMPs"], with
  [PMID:22729906 "Up to a 3-fold increase in tlr21 and tlr22"]
  [PMID:22729906 "expression was detected in larvae exposed to immunostimulants such as"]
  lipopolysaccharide, peptidoglycan or poly I:C; expression is mainly in spleen and
  kidney. The same study found
  [PMID:22729906 "Evidence of positive selection was detected at three sites within the"]
  [PMID:22729906 "leucine-rich repeat regions of Tlr22"], which the authors read as
  functional diversification of ligand recognition.
- [PMID:17804254 "the expression of genes related to the immune"]
  [PMID:17804254 "response (il1b, cebpb, tfa, mpx, tnfa, nitr9, tlr22, hsc70, cp, mrlp1, c3b and"]
  [PMID:17804254 "lyz) in each fish was monitored by means of real-time RT-PCR"] after
  *Listonella anguillarum* inoculation. The cached record is abstract-only and the
  abstract does not state what tlr22 did; the genes it names as changing are others.
- In another teleost the function is known:
  [PMID:18714020 "fgTLR22 recognizes long-sized dsRNA on the cell surface"] and
  signals through the TICAM-1 (TRIF) adaptor to induce interferon, protecting cells
  from aquatic dsRNA viruses; the authors propose it as a functional substitute for
  cell-surface TLR3 in fish. That is fugu, not zebrafish, so it informs expectations
  without supporting an annotation here.
- The zebrafish TLR21 study notes in passing that zebTLR21 is most closely related to
  zebTLR22, zebTLR5b and zebTLR3, and that poly(I:C), described there as
  "the TLR3 and TLR22 ligand", did not activate TLR21 — an indirect indication that
  dsRNA recognition is attributed to tlr22 in this species too, though it was not
  tested on tlr22 in that work.

## The project's question: which pathway term fits TLR22?

GO has numbered pathway terms for TLR1-13, 15 and 21 but none for TLR22. The answer
this review reaches is that **GO:0002224 toll-like receptor signaling pathway is
sufficient and no new numbered term should be requested yet.** The reasoning:

1. The numbered terms exist where a receptor's ligand and signalling route are
   established, which is what makes the term more informative than its parent. For
   zebrafish tlr22 neither is established: the ligand is inferred from fugu, and no
   signalling assay has been reported for the zebrafish protein.
2. If a term were created now it would be defined by receptor name alone, and the
   name is unstable: this gene's own synonym is TLR21.2, the teleost tlr21/tlr22/tlr23
   genes have been renamed and re-partitioned between species, and the PANTHER
   subfamily groups it with TLR13.
3. A term would be worth requesting once the zebrafish receptor's ligand and adaptor
   are demonstrated — and at that point the useful shape would be a term modelled on
   GO:0035682, with the fugu route (TICAM-1-dependent interferon induction in response
   to long dsRNA) as the template if it proves conserved.

Recorded in `suggested_questions` rather than in `proposed_new_terms`, deliberately:
proposing a term now would assert a receptor-specific pathway that nobody has
demonstrated for this species.

## Annotation decisions (summary)

- GO:0002221 pattern recognition receptor signaling pathway (IDA, PMID:22729906)
  modified to GO:0002224 toll-like receptor signaling pathway. The gene is an
  unambiguous member of the family by domain architecture and phylogeny, so the
  TLR-specific child of the annotated term is the right level; this is also the
  concrete answer to the project's "which pathway term" question.
- GO:0009617 response to bacterium (IDA, PMID:17804254) left UNDECIDED. The cached
  record is abstract-only; the abstract lists tlr22 among genes measured but does not
  report how it behaved, and the genes it singles out as induced are others. The
  ZFIN curator may well have read a figure showing induction, so the row is not
  removed; but the assertion cannot be verified from what is available, which is the
  circumstance the UNDECIDED action exists for.
- GO:0007165 and GO:0016020 kept as non-core.
- No `NEW` annotations. In particular no dsRNA-binding, interferon-pathway or
  cell-surface annotation: all three would rest on the fugu orthologue, and
  cross-species transfer of a ligand specificity is exactly what this project set out
  to scrutinise. They appear instead as the leading suggested experiments.
