# CLB6 (S-phase entry cyclin-6, P32943, YGR109C) — curation notes

Provider deep research was not available for this gene (no API keys in the run
environment, `just deep-research-falcon yeast CLB6` exited with
"No research providers available"), so these notes are hand-assembled from the
cached publications and the UniProt record. They are **not** a generated
`-deep-research-*.md` file.

## Summary

Clb6 is one of the two budding-yeast S-phase (B-type) cyclins. With its paralog
Clb5 it is the regulatory subunit of the S-phase form of the Cdc28 (Cdk1)
kinase: it has no catalytic activity itself, binds Cdc28, and determines when
and toward which substrates that kinase acts. `CLB6` is transcribed in late G1
together with `CLN1`, `CLN2` and the DNA-replication genes
[PMID:8319908 "We describe a new family of B-type cyclin genes, CLB5 and CLB6, whose transcripts appear in late G1 along with those of CLN1, CLN2, and many genes required for DNA replication."],
peaking early in the cycle
[PMID:8253070 "Both genes are periodically expressed, peaking early in the cell cycle."],
and UniProt records the same timing (`CC DEVELOPMENTAL STAGE`: "Maximally
expressed just before cell cycle start.").

The two S-phase cyclins are *not* interchangeable, and the differences are what
make Clb6 interesting:

- **Phenotypic asymmetry.** `clb6` deletion on its own has little or no effect
  on S phase, whereas `clb5` deletion greatly extends it; only the double
  deletion prevents timely initiation of replication
  [PMID:8319908 "Deletion of CLB6 has little or no effect, but deletion of CLB5 greatly extends S phase, and deleting both genes prevents the timely initiation of DNA replication."].
  The original cloning paper nevertheless scored a `clb6` delay in late G1
  and/or S
  [PMID:8253070 "Loss of function mutants are viable, but clb5- mutants exhibit a delay in S phase whereas clb6- mutants show a delay in late G1 and/or S phase."],
  and later work confirmed replication is slowed in `clb5Δ` but not `clb6Δ`
  [PMID:16508019 "DNA replication is significantly slowed in clb5Delta mutants but not in clb6Delta mutants."].
- **Origin usage.** Clb6 fires only early origins; late origins need Clb5
  [PMID:9734354 "Therefore, Clb5p promotes the timely activation of early and late origins, but Clb6p can activate only early origins."].
  In the double mutant the remaining mitotic cyclins Clb1-4 drive a late S phase
  in which both early and late origins fire
  [PMID:9734354 "In clb5 clb6 mutants, the other B-type cyclins (Clb1-4p) promote an S phase during which both early and late replication origins fire."].
- **Stability, not intrinsic activity, explains much of the asymmetry.** Clb6
  lacks the destruction box through which APC/C destroys Clb5, carries Cdc4
  degrons in its N terminus, and is destroyed at the G1/S border
  [PMID:16508019 "We have examined the basis for the differential functions of Clb5 and Clb6 and determined that unlike Clb5, which is stable until mitosis, Clb6 is degraded rapidly at the G1/S border.";
  PMID:16508019 "Clb6 lacks the destruction box motif responsible for the anaphase promoting complex-mediated destruction of Clb5 but contains putative Cdc4 degron motifs in the N terminus."].
  Hyperstabilized Clb6 expressed from its own promoter rescues the `clb5Δ` slow
  S phase
  [PMID:16508019 "Finally, hyperstabilized Clb6 expressed from the CLB6 promoter rescued the slow S-phase defect exhibited by clb5Delta cells."],
  so Clb6-Cdc28 *can* do Clb5's job if it survives long enough
  [PMID:16508019 "Taken together, these findings suggest that the SCF(Cdc4) ubiquitin ligase complex regulates Clb6 turnover and that the functional differences exhibited by Clb5 and Clb6 arise from the distinct mechanisms controlling their stability."].
  APC/C-Cdh1 contributes to Clb6 proteolysis in G1 through a KEN box and a
  destruction box in the N terminus
  [PMID:26994663 "In this study, we found that the APC(Cdh1) form of the Anaphase-Promoting Complex (APC) was required for Clb6 proteolysis in both early and late G1.";
  PMID:26994663 "A KEN box and a destruction box in the Clb6N-terminus were identified."].

## Clb6-specific Cdc28 substrates

Two substrates have been shown to be phosphorylated by Clb6-Cdc28 specifically,
and in both cases the consequence is release of the substrate from the nucleus.

1. **Swi6 (Ser160).** Clb6/Cdc28 is required for Swi6 nuclear export and
   phosphorylates Ser160 directly; the specificity was established by purifying
   all nine Cdc28 cyclins
   [PMID:14993267 "We show that Clb6/Cdc28 kinase is required for this nuclear export.";
   PMID:14993267 "Furthermore, Cdc28 combined with the S-phase cyclin Clb6 specifically phosphorylates serine 160 of Swi6 in vitro.";
   PMID:14993267 "the specific phosphorylation of serine 160 is directed largely by Clb6-Cdc28 and not by other G 1 or mitotic cyclin-Cdc28 kinase complexes"].
   Clb6 also binds Swi6 directly in vitro
   [PMID:14993267 "A specific interaction was also detected between Clb6 and Swi6 in vitro."].
   Because Swi6 is the shared subunit of SBF and MBF, its export alters G1/S
   transcription — the clearest statement of that consequence is in the later
   RNR paper
   [PMID:29263158 "A previous study has shown that Clb6-Cdc28 but not Clb5-Cdc28 triggers nuclear export of transcription factor Swi6 in early S phase by specifically phosphorylating Swi6 at serine-160"].
   The *direction* of the transcriptional effect is not resolved by the primary
   data (Swi6 export should relieve MBF repression and remove SBF activation),
   so a sign-specific GO term is not warranted.
2. **Rnr2 (TPSK motif).** Clb6-Cdc28 phosphorylates Rnr2, weakening the
   Rnr2-Wtm1 interaction and releasing Rnr2-Rnr4 from the nucleus so the
   ribonucleotide reductase holoenzyme can assemble in the cytoplasm in S phase
   [PMID:29263158 "Here, we report that the S-phase cyclin-cyclin-dependent kinase (CDK) complex Clb6-Cdc28 controls Rnr2-Rnr4 relocalization in S phase.";
   PMID:29263158 "Thus, we propose that Rnr2-Rnr4 redistribution in S phase is triggered by Clb6-Cdc28-mediated phosphorylation of Rnr2, which disrupts the Rnr2-Wtm1 interaction and promotes the release of Rnr2-Rnr4 from the nucleus."].
   `clb6Δ` or CDK-site removal retains Rnr2-Rnr4 in the nucleus and sensitizes
   cells to hydroxyurea
   [PMID:29263158 "Deletion of CLB6 or removal of the CDK site results in an increased association of Rnr2 with its nuclear anchor Wtm1, nuclear retention of Rnr2-Rnr4, and an enhanced sensitivity to the RNR inhibitor hydroxyurea."].
   This redistribution is Clb6-specific and not shared with Clb5
   [PMID:29263158 "Intriguingly, our results demonstrate that the redistribution of R2 in S phase is specifically controlled by Clb6 but not its paralog Clb5, with which it shares 50% primary sequence identity"].

Both outputs are **positive regulation of protein export from the nucleus**
(GO:0046827), which is why the SGD `regulation of protein localization`
(GO:0032880) row is proposed for refinement in the review rather than simply
accepted: two independent substrates, two independent papers, same direction.

## Meiosis

Clb5 and Clb6 are the only B-type cyclins able to support premeiotic DNA
replication; `clb5/clb5 clb6/clb6` diploids cannot replicate and fail to
activate the meiotic replication checkpoint
[PMID:9732268 "Diploid clb5/clb5 clb6/clb6 mutants are unable to perform premeiotic DNA replication.";
PMID:9732268 "We conclude that CLB5 and CLB6 are essential for premeiotic DNA replication and, consequently, for activation of a meiotic DNA replication checkpoint."].
This contrasts with mitosis, where Clb1-Clb4 can substitute
[PMID:9732268 "However, in mitotically growing cells this role can be fulfilled by the other B-type cyclins Clb1-Clb4."],
so meiotic S phase is the one setting in which the two S-phase cyclins are not
redundant with the mitotic ones.

A further S-phase-stress role: cells lacking both S-phase cyclins lose sister
chromatid cohesion under replication stress
[PMID:21518961 "cells lacking the S-phase cyclins Clb5 and Clb6 have a cohesion defect under conditions of replication stress"].
This is a `clb5 clb6` double-mutant phenotype with no CLB6 GOA row, and because
the paper does not separate the contributions of the two cyclins it is recorded
here rather than proposed as a new annotation.

## Localization — what is and is not known

No experimental localization of Clb6 could be found; SGD's root
`cellular_component` ND row records exactly that. GOA's compartment rows for
CLB6 are all IBA from the cyclin tree (nucleus, cytoplasm, microtubule
organizing center). The functional argument for the nucleus is indirect but
solid: both demonstrated Clb6-Cdc28 substrates are nuclear when phosphorylated
(Swi6 in the nucleus, Rnr2 held there by Wtm1), and in both cases
Clb6-dependent phosphorylation is what releases them. The microtubule
organizing center row is the weakest: that PANTHER sub-node is seeded by mitotic
B-type cyclins (cdc13, cyclin B1/B2, Clb2), Clb6 is destroyed at the G1/S border
before spindle assembly, and no spindle or SPB phenotype has been reported for
`clb6Δ`.

## Relationship to the project

Reviewed as part of [projects/YEAST_CELL_CYCLE.md](../../../projects/YEAST_CELL_CYCLE.md)
(issue #3960), alongside the already-reviewed CLB5, CLB2, CDC28, SIC1 and the
Cln cyclins. Actions were kept consistent with the CLB5 review where the same
propagated rows appear (microtubule organizing center, traversing Start), and
differ from it where CLB6-specific evidence exists: the
`regulation of DNA-templated transcription` row that had to be left UNDECIDED
for CLB5 is supportable for CLB6 through the Swi6 mechanism, and the
`regulation of protein localization` row is refinable to nuclear export.

Paralog context not used in the review itself: Loog & Morgan's comparison of
cyclin specificity [PMID:15744308] is about Clb5 versus Clb2 and does not assay
Clb6, so the hydrophobic-patch/RXL docking mechanism is assumed rather than
demonstrated for Clb6. Ccr4-dependent control of `CLB6` mRNA
[PMID:35522675] regulates Clb6 levels and is not a function of the protein.
