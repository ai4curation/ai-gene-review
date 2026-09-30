# tlr5b (zebrafish, UniProt A0ACM8R384) — curation notes

No `tlr5b-deep-research-*.md` file was produced by the batch harness before this
review was written; these notes rest on the UniProt record, the GOA rows and the
cached publications.

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
