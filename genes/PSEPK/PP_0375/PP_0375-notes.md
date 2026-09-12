# PP_0375 curation notes

## 2026-07-20 pathway hole filling

- UniProt Q88QV9 has no accepted gene symbol and describes PP_0375 as a
  prolyl-oligopeptidase-family protein. InterPro IPR001375 and PANTHER
  PTHR43056:SF5 support an S9 serine-peptidase catalytic domain.
- PP_0375 was absent from UniPathway UPA00539 and therefore landed in the
  domain-only orphan bucket. The KT2440 operon paper nevertheless identifies
  PP_0375 as putative `pqqG` by conserved locus and sequence and places it
  downstream of `pqqE` on the `pqqCDEG` transcript [PMID:27287323, "The pqq
  gene cluster (pqqFABCDEG) encodes at least two independent transcripts"].
- The Pseudomonas fluorescens B16 homolog is named PqqG/PqqM. The primary full
  text says that Tn3-gusA insertions in every named ORF, including `pqqM`,
  abolished PQQ production [PMID:18055583, "the Tn3-gusA insertions in each ORF
  abolished PQQ production"]. The study assayed culture filtrate, so it cannot
  distinguish failed formation from failed export and does not support a
  PQQ-biosynthetic-process annotation by itself.
- A reproducible MMseqs2 comparison in `PP_0375-bioinformatics/` found 66.0%
  identity over a 606-residue alignment to B16 PqqG/PqqM AAX10035.1, with
  nearly complete coverage of both proteins.
- OpenScientist surfaced the Pseudomonas aeruginosa PA1990/PqqH comparison. A
  reproduced MMseqs2 alignment found 52.2% identity over 597 residues with
  nearly complete coverage. The PA1990 mutant lost extracellular PQQ, while a
  separate `pqqF` mutant could not produce PQQ [PMID:19902179, "Gene PA1990 of
  Pseudomonas aeruginosa, located downstream of pqqE and encoding a putative
  peptidase, was shown to be involved in excretion of PQQ into the culture
  supernatant."].
- The OpenScientist report further described PA1990 disruption as not blocking
  synthesis. The cached primary abstract only establishes loss of PQQ excretion
  and does not report intracellular PQQ, so that stronger inference was not
  adopted in the review.
- The same report gives exact AlphaFold confidence/active-site distances,
  STRING scores, and an unsaved global-alignment identity. Its artifacts contain
  only the final report, so those calculations are not reproducible. The
  independently scripted MMseqs2 comparisons in `PP_0375-bioinformatics/` are
  used instead. The OpenScientist source is marked `MISCITED` for combining
  these unretained calculations with the unsupported excretion-versus-synthesis
  conclusion.

## Curation boundary

The sequence and locus evidence support PP_0375 as a PqqG/PqqM candidate linked
to PQQ-related biology and support the existing broad serine-peptidase
annotations. They do not establish a biosynthetic-process role or the native
substrate. In particular, PP_0375 must not be treated as equivalent to the
unrelated M16B PqqG partner characterized in the Methylorubrum PqqF/PqqG
complex. Direct PqqA-derived peptide cleavage and a role in PQQ excretion are
distinct, unresolved hypotheses.
