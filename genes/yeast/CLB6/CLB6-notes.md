# CLB6 (YGR109C, P32943) — curation notes

*Saccharomyces cerevisiae* S288C. Reviewed for the
[Yeast Cell Cycle & Translation Control](../../../projects/YEAST_CELL_CYCLE.md)
project (issue #3960).

Automated deep research was unavailable in this run (no provider API keys were
configured, so `just deep-research yeast CLB6 --provider perplexity` failed with
`Provider 'perplexity' not available`). These notes are therefore hand-assembled
from the cached publications in `publications/` plus the UniProt record, and are
**not** a `-deep-research-<provider>.md` file.

## Identity and family

- 380 aa, single chain, no reported processing
  [file:yeast/CLB6/CLB6-uniprot.txt "SEQUENCE   380 AA;  44145 MW;"].
- B-type cyclin: Pfam `PF00134` Cyclin_N and `PF02984` Cyclin_C, PROSITE
  `PS00292` CYCLINS, PIRSF `PIRSF001771` Cyclin_A_B_D_E, and the budding-yeast
  Clb-specific CDD models
  [file:yeast/CLB6/CLB6-uniprot.txt "CDD; cd20568; CYCLIN_CLBs_yeast_rpt1; 1."].
  UniProt places it in the cyclin AB subfamily
  [file:yeast/CLB6/CLB6-uniprot.txt "Belongs to the cyclin family. Cyclin AB subfamily."].
- Only one disordered region is annotated (residues 63-91, MobiDB-lite), i.e.
  the tandem cyclin box is the structured core and the short N-terminal
  extension carries the instability determinants.
- The entry's own FUNCTION line is minimal
  [file:yeast/CLB6/CLB6-uniprot.txt "Involved in G1/S and or S phase progression. Interacts with CDC28."],
  and its only recorded interactor is the CDK catalytic subunit
  [file:yeast/CLB6/CLB6-uniprot.txt "P32943; P00546: CDC28; NbExp=3; IntAct=EBI-2049771, EBI-4253;"].
  The Clb6-Cdc28 holoenzyme has its own Complex Portal entry
  [file:yeast/CLB6/CLB6-uniprot.txt "ComplexPortal; CPX-339; CLB6-CDC28 kinase complex."].
- Expression is cell-cycle periodic and peaks at Start
  [file:yeast/CLB6/CLB6-uniprot.txt "Maximally expressed just before cell cycle start."].

## Discovery and genetics

- *CLB5* and *CLB6* were cloned together as a new, early-expressed pair of
  B-type cyclins, physically adjacent to the mitotic pair *CLB1*/*CLB2*
  [PMID:8253070 "Two new B-type cyclin genes from Saccharomyces cerevisiae, called CLB5 and CLB6,
  are located in a tail to tail arrangement adjacent to the G2/M phase promoting cyclins CLB2 and
  CLB1, respectively."], and both are periodically transcribed early in the cycle
  [PMID:8253070 "Both genes are periodically expressed, peaking early in the cell cycle."].
- Their transcripts belong to the Start (SBF/MBF) program
  [PMID:8319908 "We describe a new family of B-type cyclin genes, CLB5 and CLB6, whose transcripts
  appear in late G1 along with those of CLN1, CLN2, and many genes required for DNA replication."],
  and the kinase they generate, rather than Cln-Cdc28, is what drives S-phase
  entry [PMID:8319908 "Thus, the kinase activity associated with Clb5/6 and not with Cln cyclins
  may be responsible for S-phase entry."].
- Both cyclins associate with the CDK catalytic subunit in vivo
  [PMID:8253070 "Both cyclins have the potential to interact with the p34CDC28 kinase in vivo."].
- **The single-mutant phenotypes are asymmetric and this is the central fact
  about Clb6.** Kühne & Linder reported a late-G1/S delay for *clb6*
  [PMID:8253070 "Loss of function mutants are viable, but clb5- mutants exhibit a delay in S phase
  whereas clb6- mutants show a delay in late G1 and/or S phase."], whereas Schwob &
  Nasmyth found essentially nothing
  [PMID:8319908 "Deletion of CLB6 has little or no effect, but deletion of CLB5 greatly extends S
  phase, and deleting both genes prevents the timely initiation of DNA replication."].
  The double mutant is what exposes the shared function
  [PMID:8253070 "The clb5 mutant phenotype is somewhat more pronounced in a double null mutant."].
- Origin-firing analysis explains the asymmetry mechanistically: Clb6 can only
  fire the early origins
  [PMID:9734354 "Therefore, Clb5p promotes the timely activation of early and late origins, but
  Clb6p can activate only early origins."], and in the double mutant the late-origin
  defect is actually suppressed by Clb1-4
  [PMID:9734354 "In clb5 clb6 double mutant cells, the late origin firing defect is suppressed,
  accounting for the normal duration of the phase despite its delayed onset."].
- The reason Clb6 reaches only the early origins is its lifetime, not a
  different docking surface: it is destroyed while S phase is still running
  [PMID:29263158 "The Clb5 protein level remains elevated throughout the S phase, whereas Clb6 is
  rapidly degraded in early unperturbed S phase via an SCF Cdc4 - and anaphase promoter complex
  (APC)-dependent pathway during normal cell cycle progression ( 37 , 38 )."].
- Together the pair is the physiological S-phase CDK activator
  [PMID:29263158 "The Clb5/Clb6-dependent CDK activity peaks at the G 1 -to-S transition and is
  primarily responsible for cooperation with DDK to activate the firing of replication origins."],
  with overlapping but non-identical substrate ranges
  [PMID:29263158 "Although the clb6 Δ mutant shows no apparent S-phase defect, as opposed to the
  clb5 Δ mutant, the clb5Δ clb6 Δ double mutant exhibits a more severe S-phase delay and an
  increased HU sensitivity relative to those of each single mutant ( 39 , 40 ), suggesting
  overlapping albeit distinct roles of the two cyclins ( 39 )."].

## Meiosis: the one place where the pair is essential

- Stuart & Wittenberg showed that *CLB1-CLB4* cannot substitute in meiosis
  [PMID:9732268 "In contrast, CLB5 and CLB6 are essential."]; the double mutant simply
  does not replicate
  [PMID:9732268 "Diploid clb5/clb5 clb6/clb6 mutants are unable to perform premeiotic DNA
  replication."], and therefore cannot activate the Mec1 replication checkpoint
  [PMID:9732268 "We conclude that CLB5 and CLB6 are essential for premeiotic DNA replication and,
  consequently, for activation of a meiotic DNA replication checkpoint."].
- Clb6's own contribution is again redundant: no defect on its own
  [PMID:9732268 "No delay or defect in DNA replication could be detected in clb6/clb6 mutants
  (data not shown)."], but it adds to Clb5's
  [PMID:9732268 "Thus, unlike the modest defect caused by these mutations in S phase of the mitotic
  cell cycle, inactivation of both CLB5 and CLB6 appears to completely block progression into
  premeiotic S phase."].
- The activity acts through Cdc28
  [PMID:9732268 "We show that premeiotic S phase is inhibited by the Clb/Cdc28-specific CDK
  inhibitor, Sic1, suggesting that the essential role of Clb5 and Clb6 is executed in conjunction
  with Cdc28."], and the pair are described as the primary S-phase activators of
  Cdc28 [PMID:9732268 "The B-type cyclins Clb5 and Clb6 are the primary activators of the S phase
  function of the budding yeast CDK Cdc28."].

## Clb6-specific substrates: the two things only Clb6 does

This is where CLB6 stops being "the weaker paralog of CLB5" and acquires its own
molecular identity. Two independent studies, using opposite logic (in vitro
cyclin panel; in vivo deletion plus phospho-site mutant), converge on
Clb6-Cdc28 reducing the nuclear pool of a specific substrate.

### Swi6 (SBF/MBF subunit)

- Geymonat et al. purified all nine Cdc28 cyclins and found the Ser160 kinase
  activity to be Clb6-specific
  [PMID:14993267 "In addition, by purifying all nine cyclins of Cdc28, we show that the specific
  phosphorylation of serine 160 is directed largely by Clb6-Cdc28 and not by other G 1 or mitotic
  cyclin-Cdc28 kinase complexes."], confirmed by depletion
  [PMID:14993267 "Clb6 specificity was confirmed with Cdc28 purified from cells depleted for
  different cyclins."] and in vitro
  [PMID:14993267 "Furthermore, Cdc28 combined with the S-phase cyclin Clb6 specifically
  phosphorylates serine 160 of Swi6 in vitro."]. Clb6 also binds Swi6 directly
  [PMID:14993267 "A specific interaction was also detected between Clb6 and Swi6 in vitro."],
  notably **without** needing an RXL/Cy motif — unlike the Clb5 hydrophobic-patch
  paradigm.
- In vivo, *CLB6* is required for Swi6 to leave the nucleus
  [PMID:14993267 "We show that Clb6/Cdc28 kinase is required for this nuclear export."],
  [PMID:14993267 "we demonstrated that Clb6 and presumably its associated kinase, Cdc28, are
  required for nuclear export of Swi6"]. The paper is explicit that this was the first
  direct Clb6 substrate
  [PMID:14993267 "Thus, for the first time, we provide direct evidence for Clb6/Cdc28 substrate
  specificity."].
- The functional consequence is negative feedback on the Start transcriptional
  program
  [PMID:14993267 "In this context, Clb6 can be seen as a negative regulator that curtails G 1 by
  promoting nuclear export of Swi6 in addition to other mechanisms of antagonizing G 1 Cdc28
  activity ( 4 )."], with the sign established by both directions of perturbation
  [PMID:14993267 "This conclusion is supported by the inhibitory effects of Clb6 overexpression and
  the stimulatory effects of CLB6 deletion on SBF- and MBF-dependent gene expression ( 4 )."].
- **Caveat worth carrying into the review**: whether Ser160 phosphorylation
  drives export or blocks re-import is unsettled
  [PMID:14993267 "Clearly, the question of whether phosphorylation triggers nuclear export or
  prevents import requires further examination, but in either case Clb6 would play a determining
  role."]. The robust claim is therefore "reduces the nuclear pool of Swi6", which is
  what `GO:1900181` says and what `GO:0046827` would over-commit to.

### Rnr2 (ribonucleotide reductase small subunit)

- Wu et al. showed Clb6-dependent phosphorylation of a single consensus CDK site
  [PMID:29263158 "Rnr2 contains a consensus CDK site and exhibits Clb6-dependent phosphorylation
  in S phase."] with a loss-of-function phenotype in both nuclear retention and drug
  sensitivity
  [PMID:29263158 "Deletion of CLB6 or removal of the CDK site results in an increased association
  of Rnr2 with its nuclear anchor Wtm1, nuclear retention of Rnr2-Rnr4, and an enhanced sensitivity
  to the RNR inhibitor hydroxyurea."], and a mechanism
  [PMID:29263158 "Thus, we propose that Rnr2-Rnr4 redistribution in S phase is triggered by
  Clb6-Cdc28-mediated phosphorylation of Rnr2, which disrupts the Rnr2-Wtm1 interaction and
  promotes the release of Rnr2-Rnr4 from the nucleus."].
- They state the paralog specificity directly
  [PMID:29263158 "Intriguingly, our results demonstrate that the redistribution of R2 in S phase is
  specifically controlled by Clb6 but not its paralog Clb5, with which it shares 50% primary
  sequence identity ( 36 )."].
- Note the same mechanistic shape as Swi6: the outcome is loss of nuclear
  residency through disruption of an anchor, not necessarily stimulated export.

## Annotation judgements and why

- **`GO:0016538` (CDK regulator activity) is the core MF** and is unusually well
  grounded for a cyclin: IDA and IMP both from the Geymonat cyclin panel, plus
  the IBA where CLB6 (`SGD:S000003341`) is itself a donor of the deep cyclin node
  `PTN000019791`.
- **`GO:0005815` microtubule organizing center (IBA)** propagates from
  `PTN007424001`, a sub-node of mitotic B-type cyclins (*S. pombe* cdc13/crs1,
  human cyclin B1/B2, Clb2). CLB6 is not a donor. Clb6 has no reported spindle or
  SPB function at all — not even the redundant `clb3 clb4 clb5` spindle phenotype
  that Clb5 has — and it is degraded in early S phase, before SPB separation.
  Flagged as over-annotated (absence of evidence is not evidence of loss).
- **`GO:0007089` traversing start control point (IBA)** propagates from
  `PTN000808767`, seeded only by *S. pombe* cig2. Budding yeast splits the job
  cig2 does in fission yeast: Cln3/Cln1/Cln2 run the Start commitment loop, and
  the Clb5/Clb6 kinase executes S phase afterwards. For Clb6 the propagation is
  not merely imprecise but sign-inverted: its documented relationship to the
  Start transcriptional program is to *shut it off* by exporting Swi6. Flagged
  as over-annotated with a `propagation_review`.
- **The CC-aspect `ND` (`GO:0005575`, SGD, 2013)** is stale. It coexists on this
  same entry with an experimentally-evidenced CC annotation — the Complex Portal
  `GO:0000307` IPI row from PMID:8319908 — and Geymonat et al. purified the
  Clb6-Cdc28 holoenzyme in 2004. The ND was defensible if read narrowly as "no
  subcellular-localization microscopy of Clb6" (there still is none), but as an
  aspect-level claim it no longer holds. `REMOVE`, `nd_case: STALE`; the
  supported CC terms (`GO:0000307`, `GO:0005634`) are already in the review, so
  nothing needs adding.
- **`GO:0006355` regulation of DNA-templated transcription (IMP, PMID:8319908,
  Complex Portal)** is the one row the CLB5 review had to leave `UNDECIDED`
  because the Schwob & Nasmyth full text is not cached. For CLB6 the direction is
  independently established by Geymonat et al., so the row is refined to
  `GO:0045892` rather than parked.
- **`GO:0032880` regulation of protein localization (IMP, PMID:29263158)** is
  refined to `GO:1900181` negative regulation of protein localization to nucleus,
  which both the Rnr2 and Swi6 results support and which survives the
  export-versus-import ambiguity that `GO:0046827` would not.
- **`GO:0044772` mitotic cell cycle phase transition (IEA)** is true but entailed
  by `GO:0000082`, which the gene already carries with IMP/IGI/IBA support, so it
  is refined rather than accepted.
- `GO:0005515` rows: the PMID:20489023 high-throughput row is removed under the
  protein-binding policy; the PMID:8253070 row is refined to `GO:0016538`,
  because the paper's own conclusion is Cdc28 association, mirroring the CLB5
  review.

## Comparator check performed before proposing anything new

No `NEW` rows are proposed. Two were considered and rejected:

- `GO:0046827 positive regulation of protein export from nucleus` — rejected in
  favour of `GO:1900181` as the MODIFY target, because Geymonat et al. explicitly
  leave open whether Ser160 phosphorylation triggers export or prevents import,
  and the Rnr2 mechanism is anchor release rather than export.
- A `GO:0006260`/`GO:0006270` DNA-replication-initiation term — rejected on the
  comparator used in the CLB5 review: SGD places the cyclins and Cdc28 on
  `GO:0045740` positive regulation of DNA replication and on `GO:0000082`, and
  reserves the initiation terms for ORC/MCM/Sld/DDK components. Clb6 supplies the
  kinase activity; it is not part of the replisome.

## Open questions carried into the review

- Is the Clb6-versus-Clb5 substrate difference (Swi6 Ser160, Rnr2 Thr5) a
  property of the cyclin's own docking surface, or merely of the two proteins'
  different lifetimes? Geymonat et al. found the Swi6 interaction does not need
  an RXL motif, which argues for a genuinely different surface; the Clb6
  early-degradation data argue for timing.
- Does Clb6-Cdc28 phosphorylation of Swi6 Ser160 stimulate export or block
  import?
- Is there any direct localization data for Clb6 itself? Every CC annotation on
  the entry is either propagated (nucleus, cytoplasm, MTOC) or complex-based
  (`GO:0000307`).
