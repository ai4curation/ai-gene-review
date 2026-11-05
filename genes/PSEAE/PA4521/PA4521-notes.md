# PA4521 (G3XD69, AmpE) notes

## Identity

- UniProt G3XD69, unreviewed, 278 aa; locus PA4521, no gene name in the entry
  (name "AmpE protein" is ProtNLM-generated). Five TM helices (Phobius),
  Pfam PF17113 AmpE, InterPro IPR031347 AmpE, IPR052966
  Beta-lactamase_Reg; PANTHER PTHR38684 (PROTEIN AMPE). Second gene of the
  ampDE operon (ampD = PA4522).

## Literature

- Langaee et al. 1998 (PMID:9835532; abstract only, PMC full text not
  retrievable): cloned and characterised P. aeruginosa ampD and ampE as an
  operon; the only functional result in the abstract is for ampD
  [PMID:9835532 "These genes are transcribed in the same orientation and form an
  operon."; "The ampD product transcomplemented Escherichia coli ampD mutants to
  wild-type beta-lactamase expression."]. No ampE mutant or ampE-specific
  phenotype is mentioned in the abstract.
- P. aeruginosa clinical isolates (Juan et al. 2005; abstract): some ampD
  mutants were complemented only by ampDE, and the authors infer an indirect
  role for AmpE [PMID:16251318 "our findings suggest that for certain types of
  mutations, AmpE plays an indirect role in resistance"].
- E. coli/Enterobacter AmpE: the two 1989 papers disagree. Honoré et al.:
  AmpE is a cytoplasmic membrane protein needed for induction
  [PMID:2607970 "loss of AmpE results in a total block in induction, despite
  the presence of the activator, AmpR."]; they also note E. coli lacks ampR
  [PMID:2607970 "although Escherichia coli has lost its ampR gene it has
  retained the second regulatory locus and that this comprises the
  bicistronic ampDE operon"]. Lindquist et al.: AmpE is an integral membrane
  protein but not needed for induction [PMID:2691840 "Since neither AmpD nor
  AmpE are needed for beta-lactam induction and since these proteins could not
  be covalently labelled by benzylpenicillin, they are not thought to act as
  beta-lactam-binding sensory transducers."].

## Participation test

If AmpE relays a peptidoglycan-recycling signal to AmpR it would take part in
the beta-lactam induction response, but whether it does is contested in the
enterobacteria and only indirectly supported in P. aeruginosa. The cited
paper's abstract shows no ampE phenotype, so the PseudoCAP IMP cannot be
checked. "Response to antibiotic" is a broad phenotype-level term; for AmpE it
would hold only where an inducible AmpC/AmpR system exists, and E. coli (a
leaf) has no ampR. The membrane location is solid (5 TM helices; E. coli
AmpE a cytoplasmic membrane protein).

Clade check: PTN002214697 leaves are E. coli AmpE (P0AE14), Salmonella,
Yersinia, Coxiella, Shewanella and Xanthomonas AmpE homologues and PA4521.
None of the leaves has experimental support for a response-to-antibiotic role
of AmpE itself in this record set.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002214697 | GO:0046677 response to antibiotic | 1 (sole) | 7 (7 taxa) | GO:0046677, IMP, PMID:9835532 (PseudoCAP) | UNVERIFIABLE | Abstract only; it reports ampD complementation, not an ampE mutant. AmpE's role in beta-lactamase induction is contested (PMID:2607970 vs PMID:2691840) and only indirect in P. aeruginosa (PMID:16251318). A broad antibiotic-response phenotype is a poor clade term, and E. coli, a leaf, has no AmpR-inducible AmpC. |

## Decisions summary

- ACCEPT: plasma membrane (IBA).
- UNDECIDED: response to antibiotic (IMP, paper not readable; and the IBA,
  kept consistent), with a GO_CENTRAL CHECK defect on PTN002214697 arguing the
  phenotype term is a poor clade term.
