# tlr5b (zebrafish, UniProt A0ACM8R384) — curation notes

These notes rest on the UniProt record, the GOA rows and the cached publications;
the Falcon deep-research report arrived after the review was written and is
cross-checked at the end of this file.

## Entry identity (TrEMBL, unreviewed)

`A0ACM8R384_DANRE`, 881 aa, submitter name "Toll-like receptor 5b precursor", gene
name tlr5b (synonym tlr5), cross-referenced to RefSeq NP_001124067 and GeneID
403139. NCBI gives gene 403139 as "tlr5b toll-like receptor 5b" on chromosome 20,
so this is the right gene. (The project candidate table listed F8W3J5, another
TrEMBL entry for the same gene.) Features: signal peptide 1..27, transmembrane
659..681, TIR domain 710..855, InterPro IPR017241 Toll-like_receptor, PANTHER
PTHR24365:SF525 TOLL-LIKE RECEPTOR 5. The entry carries the caution "Lacks
conserved residue(s) required for the propagation of feature annotation", which
concerns automatic feature transfer and not receptor function.

All five GOA rows are electronic (InterPro2GO and subcellular-location mapping);
there is no experimental annotation on this entry at all.

## Established biology

- Zebrafish has duplicated tlr5, and the two products work as an obligate
  heterodimer rather than as independent homodimeric receptors:
  [PMID:29555749 "zebrafish ( Danio rerio ) TLR5 unexpectedly signals as a heterodimer composed of the duplicated gene products drTLR5b and drTLR5a"].
  Flagellin is the ligand, and signalling is improved by the trafficking chaperone:
  [PMID:29555749 "Flagellin-induced signaling by the zebrafish TLR5 heterodimer increased in the"]
  [PMID:29555749 "presence of the TLR trafficking chaperone UNC93B1"]. Neither
  paralogue worked alone:
  [PMID:29555749 "Even after expression of drUNC93B1, which led to redistribution and more robust NF-κB activation by the heterodimeric receptor, individual drTLR5a and drTLR5b did not operate as homodimers"].
- Direct flagellin binding by this gene product is established structurally: the
  reference crystal structure of a TLR5-flagellin complex is of the zebrafish
  protein — [PMID:22344444 "we determined the crystal structure"]
  [PMID:22344444 "of zebrafish TLR5 (as a variable lymphocyte receptor hybrid protein) in complex"]
  [PMID:22344444 "with the D1/D2/D3 fragment of Salmonella flagellin, FliC, at 2.47 angstrom"]
  resolution, and [PMID:22344444 "TLR5 interacts primarily with the three helices of the FliC D1"]
  domain. The construct used was the TLR5b ectodomain (drTLR5-ECD), as the 2018
  paper notes when it says the crystallised fragment of zebrafish TLR5b "serves as a
  model structure for the homodimeric TLR5–flagellin interaction".
- Species specificity of the interaction is real: substituting the presumed principal
  flagellin-binding site of human TLR5 with the corresponding zebrafish residues
  abolished human TLR5 activation (PMID:29555749), so flagellin recognition is
  conserved as a function while the contact details are not interchangeable.
- A commentary on grass carp work reports that teleost TLR5b homodimers can respond
  to double-stranded RNA and signal to interferon-stimulated response elements
  [PMID:35762506 "However, TLR5b homodimers are able to respond to dsRNA to trigger antiviral transcriptional programs."],
  a capacity absent from mammalian TLR5. This is a secondary source about
  *Ctenopharyngodon idella*, so it is recorded as a question and an experiment to
  do in zebrafish, not as an annotation.

## Annotation decisions (summary)

The project question for this gene is whether the mammalian TLR5 ligand terms
transfer. They do — flagellin recognition is the conserved function, and the
structural evidence is on the zebrafish protein itself — but the *receptor
configuration* does not: zebrafish TLR5 is a heterodimer, so this gene product
contributes the activity rather than possessing it alone.

- GO:0002224 (IEA, InterPro) modified to GO:0034146 toll-like receptor 5 signaling
  pathway. The receptor-specific term exists, the gene is a genuine tlr5 paralogue
  by sequence and by function, and flagellin-induced signalling through it is
  demonstrated.
- GO:0004888 transmembrane signaling receptor activity (IEA) modified to GO:0038187
  pattern recognition receptor activity, with the caveat above; in `core_functions`
  the activity is recorded under `contributes_to_molecular_function`, since neither
  paralogue signals as a homodimer.
- GO:0006955 immune response and GO:0007165 signal transduction kept as non-core
  (true, generic).
- GO:0016020 membrane accepted: a signal peptide plus a single predicted
  transmembrane segment, consistent with the family.
- No `NEW` annotations. A dsRNA-binding or interferon-pathway annotation would rest
  on a commentary about another species; a plasma-membrane annotation would go beyond
  what was observed, since both paralogues were found in vesicle-like compartments
  rather than at a defined surface location.


## Deep-research cross-check (2026-09-30)

Compared `tlr5b-deep-research-falcon.md` against the finished review. Right gene, right
accession, and it agrees with every decision: flagellin as the ligand, obligate
heterodimerisation with the paralogue as the distinguishing feature, UNC93B1-dependent
trafficking, MyD88-dependent signalling to NF-kappa-B, teleost tandem duplication with
subfunctionalisation, and explicit caution that the grass carp dsRNA result has not been
shown for zebrafish —
[file:DANRE/tlr5b/tlr5b-deep-research-falcon.md "However, this dual-ligand capability has not been directly demonstrated for zebrafish TLR5b"],
which is exactly why the review made no dsRNA or interferon annotation.

Additions taken up, verified in primary papers:

- **In vivo loss-of-function evidence, which the review lacked entirely**
  (`publications/PMID_26208853.md`, full text). Morpholino knockdown in zebrafish embryos:
  [PMID:26208853 "Our results revealed that abrogation of both tlr5a and tlr5b effectively prevented the il1b up-regulation observed in control embryos upon flagellin stimulation"],
  with the informative asymmetry that there was
  [PMID:26208853 "a complete block of induction of il1b by injection with flagellin and a partial effect of the tlr5b morpholino"].
  A partial single-paralogue effect is what an obligate heterodimer predicts. Added to the
  GO:0034146 row and to `core_functions.supported_by`; until now every line of evidence for
  this gene came from heterologous expression or crystallography.
- **The vesicular compartment is identifiable, if not annotatable.** The primary paper's marker
  data were more specific than the review's wording allowed: the paralogues associated more with
  LAMP-1 than with EEA-1 positive vesicles, and
  [PMID:29555749 "drUNC93B1 enhanced relocalization of both receptors toward LAMP-1–specific compartments"]
  coinciding with increased flagellin responsiveness. Recorded in the GO:0016020 reason. The
  location annotation is deliberately still the generic `membrane`, because this is
  overexpression in a heterologous line; the existing suggested question and localisation
  experiment cover the gap.

Not taken up: the transcriptome-level downstream gene lists (il1b, il8, mmp9, cxcl-C1c, irak3,
tnfa) are outputs of the pathway rather than activities of this gene product, so they support the
pathway term and nothing further; the Stockhammer knockdowns used a combined tlr5a+tlr5b
morpholino, which cannot apportion the effect between paralogues; and the aquaculture-adjuvant
material is application rather than function. The report's claim of MyD88 dependence for this
receptor is drawn from reviews rather than from a zebrafish experiment, and no adaptor annotation
is made.

Actions: every existing annotation unchanged, no new annotations. Changes are to two `reason`
fields, three new `supported_by` quotes on annotations plus one in `core_functions`, and two new
references (PMID:26208853 and the Falcon file).
