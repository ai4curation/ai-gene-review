# A0A8B6BFL6 (Mytilus galloprovincialis) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not open or use the ProtNLM2 predictions file. The earlier review cited it
as support for DNA integration and DNA recombination. Those claims are dropped below.

### Identity

- A0A8B6BFL6 is the ORF MGAL_10B073878, 612 aa, from an unassembled WGS entry (PE 4, predicted).
  Pfam RVT_1 covers 174-349; CDD cd09275 is RNase_HI_RT_DIRS1. [file:MYTGA/A0A8B6BFL6/A0A8B6BFL6-uniprot.txt]
- This is a repeat-derived coding sequence, not a conventional host gene. It has no gene
  symbol, so there is no "canonical product" to compare against and no isoform question.
  The protein starts with Met and its RT-RNase H region is intact (see below). Even so, it
  probably represents only one protein of a multi-ORF DIRS element, the way DIRS-1 ORF2 does.
  So it is complete as an RT-RNase H unit but not as a whole element.
- The deep-research report (falcon) assumes a LINE/non-LTR element with target-primed reverse
  transcription. That contradicts the domain evidence. cd09275 and the PANTHER subfamily point
  to the DIRS (tyrosine recombinase retrotransposon) order, so the TPRT and LINE claims are not
  carried into the review.

### Phylogenetic placement

- PANTHER PTHR33050 (official name "REVERSE TRANSCRIPTASE DOMAIN-CONTAINING PROTEIN"),
  subfamily SF7 ("RIBONUCLEASE H"). The earlier description called PTHR33050 "Hepadnavirus
  polymerase/reverse transcriptase". That is the name of InterPro IPR052055, not of the
  PANTHER family, and has been corrected.
- SF7 holds both the hepadnavirus P proteins and the Dictyostelium DIRS-1 ORF2 product
  (O96849/Q23898, 608 aa, cd03714 RT_DIRS1 + cd09275), as confirmed in the UniProt REST
  PANTHER cross-references. The DIRS-1 ORF3 tyrosine recombinase (O96848) is in a different
  family, PTHR31660.
- Alignment (bioinformatics/RESULTS-rereview.md): against DIRS-1 ORF2 the score is 283
  (z=51.7 vs shuffled controls), 26.4% identity over 397 columns, spanning both RT and RNase H.
  Against DHBV P the score is 65 (z=6.8) and covers the RT core only. Against the DIRS-1 YR
  there is no similarity (z=-0.7). The target lacks the C-terminal Dam-like MTase region that
  DIRS-1 ORF2 carries.
- No PAINT/IBA annotations exist, and GOA has no rows for this accession.

### What can be transferred

- RNA-directed DNA polymerase activity (GO:0003964). The RT domain retains motif C `YLDD`
  (300-303). Within the DIRS order, the DIRS-1 RT is genetically required and acts in trans
  [PMID:32170321 "indicated that the endogenous DIRS-1 reverse transcriptase can act in trans"].
- RNA-DNA hybrid ribonuclease activity (GO:0004523). This rests on the cd09275 RNase H
  assignment and the alignment to the DIRS-1 RNase H, with a candidate SDA-context first
  carboxylate at 463. It is weaker than the RT claim.
- Retrotransposition (GO:0032197). The RT does the cDNA-synthesis step, so it participates
  in the process. This is not just a necessity argument.
- NOT transferred: DNA integration and DNA recombination. In DIRS elements these steps
  belong to the separately encoded tyrosine recombinase [PMID:32170321 "As this name
  suggests, the group is characterized by the presence of tyrosine recombinases instead of an
  integrase (INT) or endonuclease"], and this protein has no YR domain.
- NOT transferred: nucleus and cytoplasm. No evidence supports them. The earlier review
  inferred them by analogy to LINE-1, which is the wrong element order. Hepadnavirus-specific
  biology (protein priming, capsid-internal replication, DNA-dependent DNA polymerase,
  cccDNA) is also not transferred. The target sits in a different branch of SF7 from the
  hepadnaviruses (DIRS-like; it aligns weakly to DHBV P).

### Relative to review next

- The closest relative with any experimental data is the DIRS-1 ORF2 RT-RNase H of
  Dictyostelium discoideum (O96849; identical-length copy Q23898). It is in the same PANTHER
  subfamily and the same element order, and it aligns across the whole RT-RNase H unit. The
  experimental data come from element-level genetics (PMID:32170321), not biochemistry of
  the purified protein. The repo has no review of it (grep for O96849/Q23898 under genes/
  returned nothing).
- The PANTHER family review (interpro/panther/PTHR33050/PTHR33050-review.yaml) agrees with the
  SF7 placement and the conclusion that integration and recombination cannot be inferred. Its
  summary leans on hepadnaviral polymerases. These notes add that DIRS-1 ORF2 is also an SF7
  member and is the closer comparator.
- Modules: none relevant (grep of modules/ for retrotransposon terms found only host
  defence/piRNA modules).
