# CLB6 (YGR109C, P32943) — curation notes

*Saccharomyces cerevisiae* S288C. Reviewed for the
[Yeast Cell Cycle & Translation Control](../../../projects/YEAST_CELL_CYCLE.md)
project (issue #3960), as the partner of the already-reviewed S-phase cyclin
[CLB5](../CLB5/CLB5-ai-review.yaml).

Automated deep research was unavailable in this run (no provider API keys were
configured, so `just deep-research yeast CLB6 --provider perplexity` failed).
These notes are hand-assembled from the cached publications in `publications/`
plus the UniProt record, and are **not** a `-deep-research-<provider>.md` file.

## Identity and family

- 380 aa, single chain, no reported processing
  [file:yeast/CLB6/CLB6-uniprot.txt "SEQUENCE   380 AA;  44145 MW;"].
- Cyclin-box protein of the B-type (cyclin A/B) subfamily: Pfam `PF00134`
  Cyclin_N plus `PF02984` Cyclin_C, PROSITE `PS00292` CYCLINS, PIRSF
  `PIRSF001771` Cyclin_A_B_D_E, InterPro `IPR046965` Cyclin_A/B-like, and the
  two yeast-Clb-specific CDD models
  [file:yeast/CLB6/CLB6-uniprot.txt "CDD; cd20568; CYCLIN_CLBs_yeast_rpt1; 1."].
  UniProt assigns the subfamily
  [file:yeast/CLB6/CLB6-uniprot.txt "Belongs to the cyclin family. Cyclin AB subfamily."].
- One disordered region is annotated (residues 63-91, MobiDB-lite); this sits in
  the N-terminal region that carries the Clb6 degron (below).
- UniProt's curated function statement is minimal
  [file:yeast/CLB6/CLB6-uniprot.txt "Involved in G1/S and or S phase progression."] and its
  expression statement records the periodicity
  [file:yeast/CLB6/CLB6-uniprot.txt "Maximally expressed just before cell cycle start."].
- ComplexPortal curates the holoenzyme as a distinct complex
  [file:yeast/CLB6/CLB6-uniprot.txt "ComplexPortal; CPX-339; CLB6-CDC28 kinase complex."].

## Discovery and genetics

- *CLB5* and *CLB6* were described simultaneously by two groups in 1993 as a new
  pair of B-type cyclins transcribed in late G1 with *CLN1*, *CLN2* and the
  replication genes [PMID:8319908 "We describe a new family of B-type cyclin genes, CLB5
  and CLB6, whose transcripts appear in late G1 along with those of CLN1, CLN2,
  and many genes required for DNA replication."], and both associate with Cdc28
  [PMID:8253070 "Both cyclins have the potential to interact with the p34CDC28 kinase in vivo."].
- The two single mutants are not equivalent. *clb5* greatly extends S phase;
  *clb6* on its own has little or no replication phenotype
  [PMID:8319908 "Deletion of CLB6 has little or no effect, but deletion of CLB5 greatly extends
  S phase, and deleting both genes prevents the timely initiation of DNA replication."].
  Kuehne & Linder saw the *clb6* defect as a G1/S-timing rather than an S-phase
  one [PMID:8253070 "Loss of function mutants are viable, but clb5- mutants exhibit a delay in
  S phase whereas clb6- mutants show a delay in late G1 and/or S phase."].
- Origin-level dissection resolves the asymmetry: Clb6 fires early origins only
  [PMID:9734354 "Therefore, Clb5p promotes the timely activation of early and late origins, but
  Clb6p can activate only early origins."], and *clb6* origin firing is
  otherwise normal [PMID:9734354 "Origin firing appears normal in cIb6 mutants."].
- Either cyclin suffices for on-schedule S-phase entry; only Clb5 is needed for
  timely progression through S phase [PMID:16508019 "Either Clb5 or Clb6 can promote entry
  into S phase on schedule ( 1 , 8 , 35 ). However, Clb5 but not Clb6 is required for timely
  progression through S phase ( 8 , 35 )."].

## Why Clb5 and Clb6 differ: protein stability, not intrinsic specificity

This is the key CLB6-specific result and it reframes the origin-firing data.

- Clb6 is destroyed at the G1/S border while Clb5 persists to mitosis
  [PMID:16508019 "unlike Clb5, which is stable until mitosis, Clb6 is degraded rapidly at the G 1
  /S border"], with a half-life under 5 min in asynchronous cells
  [PMID:16508019 "Wild-type Clb6 appears to be very unstable in asynchronous cells, exhibiting a
  half-life of less than 5 min."].
- The mechanism is SCF(Cdc4), not APC/C: Clb6 lacks a functional destruction box
  (RXXL→KXXL) and instead carries Cdc4 phospho-degron motifs in its N terminus
  [PMID:16508019 "Clb6 lacks the destruction box motif responsible for the anaphase promoting
  complex-mediated destruction of Clb5 but contains putative Cdc4 degron motifs in the N
  terminus."], and is stabilized in `cdc34-3`/`cdc4-3` and by mutating the
  N-terminal S/T-P sites [PMID:16508019 "Clb6 was hyperstabilized in cdc34 - 3 and cdc4 - 3
  mutants at restrictive temperatures and when S/T-P phosphorylation sites in the N terminus were
  mutated to nonphosphorylatable residues."].
- Crucially, stabilized Clb6 does Clb5's job
  [PMID:16508019 "Finally, hyperstabilized Clb6 expressed from the CLB6 promoter rescued the slow
  S-phase defect exhibited by clb5Δ cells."], so the "early origins only"
  restriction reflects when Clb6 is present rather than which substrates it can
  reach [PMID:16508019 "the functional differences exhibited by Clb5 and Clb6 arise from the
  distinct mechanisms controlling their stability"].

**Curation consequence.** Clb6 should not be reviewed as a weak Clb5. The two
are interchangeable activators of S-phase Cdc28 whose outputs differ because one
is removed at the G1/S border; the GO annotations shared with CLB5 (G1/S
transition, positive regulation of DNA replication, CDK holoenzyme complex,
CDK regulator activity) are sound for Clb6 on that reading.

## Clb6-specific Cdc28 substrates

Two substrates are specifically attributed to Clb6-Cdc28 rather than to
Clb5-Cdc28, and both are nuclear proteins that Clb6 phosphorylation drives out
of the nucleus.

- **Swi6** (shared SBF/MBF subunit). Clb6-Cdc28 phosphorylates Ser160 and is
  required for Swi6 nuclear export [PMID:14993267 "We show that Clb6/Cdc28 kinase is
  required for this nuclear export. Furthermore, Cdc28 combined with the S-phase cyclin Clb6
  specifically phosphorylates serine 160 of Swi6 in vitro."]. Specificity was
  established against all nine cyclins
  [PMID:14993267 "In addition, by purifying all nine cyclins of Cdc28, we show that the specific
  phosphorylation of serine 160 is directed largely by Clb6-Cdc28 and not by other G 1 or mitotic
  cyclin-Cdc28 kinase complexes."], and this was the first direct demonstration of
  Clb6-Cdc28 substrate specificity
  [PMID:14993267 "Thus, for the first time, we provide direct evidence for Clb6/Cdc28 substrate
  specificity."]. Later work restates the asymmetry explicitly
  [PMID:29263158 "A previous study has shown that Clb6-Cdc28 but not Clb5-Cdc28 triggers nuclear
  export of transcription factor Swi6 in early S phase by specifically phosphorylating Swi6 at
  serine-160, thus altering Swi4/Swi6 (SBF) and Mbp1/Swi6 (MBF)-mediated transcription at the G 1
  /S transition ( 41 )."], as does Jackson et al.
  [PMID:16508019 "Moreover, Clb6 but not Clb5 is required to regulate the nuclear localization of
  the transcription factor Swi6 ( 12 )."].
- **Rnr2** (ribonucleotide reductase small subunit). Clb6-Cdc28 phosphorylates
  the N-terminal TPSK CDK site, weakening the Rnr2-Wtm1 nuclear anchor
  [PMID:29263158 "Our results support a model in which the S-phase cyclin-CDK complex Clb6-Cdc28
  phosphorylates Rnr2 at its N-terminal TPSK motif, which weakens the Rnr2-Wtm1 interaction and
  facilitates the release of preexisting Rnr2-Rnr4 from the nucleus ( Fig. 7 )."]; loss of
  CLB6 or of the site retains Rnr2-Rnr4 in the nucleus and sensitizes cells to
  hydroxyurea [PMID:29263158 "Deletion of CLB6 or removal of the CDK site results in an
  increased association of Rnr2 with its nuclear anchor Wtm1, nuclear retention of Rnr2-Rnr4, and
  an enhanced sensitivity to the RNR inhibitor hydroxyurea."].

Both lines converge on one specific process — Clb6-Cdc28 phosphorylation
releasing a protein from a nuclear anchor — which is why the GOA row
`GO:0032880 regulation of protein localization` (IMP, the Rnr2 paper) is
reviewed as too general and modified to `GO:0046827 positive regulation of
protein export from nucleus`. One caveat is recorded in the Swi6 paper itself:
whether Ser160 phosphorylation stimulates export or blocks re-import was not
settled [PMID:14993267 "Clearly, the question of whether phosphorylation triggers nuclear export
or prevents import requires further examination, but in either case Clb6 would play a determining
role."]. The Rnr2 result is unambiguous about release from the nucleus, so the
signed term is retained with the caveat noted in the review and as a suggested
question.

## Negative regulation of G1 and G2

- Clb5 and Clb6 also restrain the phases on either side of S. *clb6* mutants have
  a shorter pre-Start G1 *and* a shorter G2 and grow faster than wild type
  [PMID:7651421 "The consequences of this negative regulation were most apparent in clb6 mutants,
  which had a shorter pre-Start G1 phase as well as a shorter G2 phase than congenic wild-type
  cells."], and both cyclins down-regulate Cln2- and Clb2-associated kinase
  activity in vivo [PMID:7651421 "Nevertheless, both Clb5 and Clb6 were shown to be responsible
  for down-regulation of the protein kinase activities associated with Cln2, a G1 cyclin, and Clb2,
  a mitotic cyclin, in vivo."]. The authors' summary
  [PMID:7651421 "Thus, Clb5 and Clb6 may stabilize S phase by promoting DNA replication while
  inhibiting other cell cycle activities."].
- Geymonat et al. read the Swi6 axis the same way
  [PMID:14993267 "In this context, Clb6 can be seen as a negative regulator that curtails G 1 by
  promoting nuclear export of Swi6 in addition to other mechanisms of antagonizing G 1 Cdc28
  activity ( 4 )."], noting that *CLB6* overexpression inhibits and *CLB6*
  deletion stimulates SBF/MBF-dependent gene expression
  [PMID:14993267 "This conclusion is supported by the inhibitory effects of Clb6 overexpression and
  the stimulatory effects of CLB6 deletion on SBF- and MBF-dependent gene expression ( 4 )."].
- **Not proposed as a NEW annotation.** The down-regulation of Cln2/Clb2 kinase
  is reported as indirect ("dependent on and possibly mediated through the CDC6
  gene product" in PMID:7651421's abstract), and the primary measurements sit in
  full text that is not cached (PMID:7651421 is abstract-only). It is recorded as
  a suggested question and a knowledge gap instead of a
  `negative regulation of cyclin-dependent protein serine/threonine kinase
  activity` row.
- The transcriptional arm *is* actionable: the GOA row `GO:0006355 regulation of
  DNA-templated transcription` (IMP, PMID:8319908, ComplexPortal) is modified to
  `GO:0045892 negative regulation of DNA-templated transcription`, since the
  direction is stated consistently across PMID:14993267, PMID:7651421 and
  PMID:29263158. One conflicting observation is on record and is quoted in the
  review: the non-phosphorylatable *swi6-S160A* allele does not grossly change
  SBF/MBF transcription [PMID:14993267 "It is interesting that the S160A mutation that leads
  to nuclear localization of Swi6 does not reveal any major changes in SBF- or MBF-driven
  transcription ( 46 )."], which is why Geymonat et al. allow for additional
  routes [PMID:14993267 "Clb6 may have other roles in controlling Swi6-dependent transcription in
  addition to cellular localization of Swi6."].

## Meiosis

- *CLB5* and *CLB6* are the B-type cyclins that drive premeiotic S phase, and
  there the requirement is absolute [PMID:9732268 "Diploid clb5/clb5 clb6/clb6 mutants are
  unable to perform premeiotic DNA replication."]; they are named as the primary
  activators of the S-phase function of Cdc28 [PMID:9732268 "The B-type cyclins Clb5 and
  Clb6 are the primary activators of the S phase function of the budding yeast CDK Cdc28."].
- Clb6's contribution is again unmasked only in combination
  [PMID:9732268 "No delay or defect in DNA replication could be detected in clb6/clb6 mutants
  (data not shown)."], but it is real: the double mutant is far worse than
  *clb5/clb5* for both tetrad formation and spore viability
  [PMID:9732268 "this cyclin can clearly contribute to this process because inactivation of both
  CLB5 and CLB6 resulted in a more dramatic defect in both tetrad formation and spore viability as
  compared with clb5/clb5 mutants (Table 1 )."]. This redundancy pattern is what
  GO's IGI rows on `GO:0006279` record, and both the IGI and the IMP row are
  accepted on it.

## Localization

No paper in the cache localizes the Clb6 protein itself. The IBA `nucleus` row
is nevertheless well-grounded indirectly: both demonstrated Clb6-Cdc28
substrates are phosphorylated in the nucleus (Swi6 bound to SBF/MBF, Rnr2 held
by Wtm1), the holoenzyme acts at replication origins, and the Clb6 degron is
processed by the nuclear SCF(Cdc4). The `cytoplasm` IBA is kept as non-core and
the `microtubule organizing center` IBA — propagated from a sub-node seeded by
mitotic B-type cyclins — is marked as over-annotated, as in the CLB5 review.

The SGD `GO:0005575` ND row (2013) is now stale: ComplexPortal subsequently made
a literature-based CC annotation on CLB6 itself (CPX-339, the CLB6-CDC28 kinase
complex, from PMID:8319908), and the 1993 papers already reported the Clb6-Cdc28
association. Recorded as `nd_case: STALE` with `action: REMOVE`.

## Open questions carried into the review

1. Does any Clb6 pool localize to a sub-nuclear site (replication origins, SBF/MBF
   promoters) or is the holoenzyme nucleoplasmic? No direct Clb6 imaging exists.
2. Is the Ser160 effect on Swi6 export-stimulating or import-blocking?
3. Is the Clb5/Clb6 substrate difference entirely a consequence of the stability
   difference, as PMID:16508019 argues, or do Swi6 and Rnr2 require Clb6 docking
   features that Clb5 lacks?
4. Is the down-regulation of Cln2- and Clb2-associated kinase activity a direct
   Clb6-Cdc28 phosphorylation event, or entirely routed through Cdc6?
