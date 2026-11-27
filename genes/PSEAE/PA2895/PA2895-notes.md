# PA2895 / sbrR (Q9HZV2) review notes

## The paper names the locus, which settles attribution

[PMID:26620262 "Here, we provide evidence that sbrR (PA2895), a gene previously identified as
required during chronic P. aeruginosa respiratory infection, encodes an anti-σ factor that
inhibits the activity of its cognate extracytoplasmic-function σ factor, SbrI (PA2896)."] Both
loci are given, so neither annotation depends on inferring which gene was studied — the case that
goes wrong most often in this project.

The mechanism is established at two levels:

- **Direct interaction, and the part that does it.** [PMID:26620262 "Bacterial two-hybrid analysis
  identified an N-terminal region of SbrR that interacts directly with SbrI and that was
  sufficient for inhibition of SbrI-dependent gene expression."]
- **The target is the transcription machinery.** [PMID:26620262 "We show that SbrI associates with
  RNA polymerase in vivo and identify the SbrIR regulon."] An anti-σ factor that sequesters a σ
  which associates with RNA polymerase is acting before initiation, which is what makes
  `GO:2000143` the right process term rather than a generic repression term.

## The record and the paper agree on architecture

The UniProt entry is thin — `PE 4: Predicted`, no `CC` lines, and its only name,
`RecName: Full=Anti-sigma factor SbrR`, carries `{ECO:0008006|Google:ProtNLM}`, a
machine-generated name that this project does not accept as support. So nothing in the record is
used to support an annotation here.

One record feature is worth reading against the paper rather than as support for it. Phobius
places a single transmembrane helix at **65..87** (`ECO:0000256|SAM:Phobius`), in a 254-residue
protein. That is the canonical architecture of a membrane-anchored extracytoplasmic-function
anti-σ factor: a cytoplasmic N-terminal anti-σ domain, a single membrane anchor, and a
periplasmic C-terminal sensor. The paper's finding that an **N-terminal** region is both
sufficient for interaction with SbrI and sufficient for inhibition fits that layout exactly,
since residues before 65 are the ones on the cytoplasmic side where a σ factor can be reached.

This is a consistency observation, not an annotation. No location row is proposed: the helix is a
single prediction, and the architectural argument restates the same inference rather than adding
an independent line. It is recorded as a question and an experiment instead.

## What is downstream, and why it is not annotated

The phenotypes the paper reports for *sbrR* — swarming motility and biofilm formation — are
mediated by *muiA*, a gene whose expression SbrI drives: [PMID:26620262 "In cells lacking SbrR, the
SbrI-dependent expression of muiA was found to inhibit swarming motility and promote biofilm
formation."] SbrR therefore affects those behaviours by not letting SbrI transcribe *muiA*. That
is two regulatory steps and one effector away from anything SbrR itself does, so no motility or
biofilm process term is proposed. The gene product's own work is sequestering a σ factor.
