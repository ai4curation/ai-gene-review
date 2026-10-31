# CLB6 (S. cerevisiae, P32943, YGR109C) — curation notes

Reviewed 2026-10-31 for [Yeast Cell Cycle & Translation Control](../../../projects/YEAST_CELL_CYCLE.md)
(issue #3960). Companion reviews: `genes/yeast/CLB5` (paralog), `genes/yeast/CLB2`,
`genes/yeast/CDC28`, `genes/yeast/CLN1`, `genes/yeast/CLN2`, `genes/yeast/CLN3`,
`genes/yeast/SIC1`, `genes/yeast/WHI5`.

Deep research was unavailable this run: the only configured provider is `claude_code`
and `just deep-research yeast CLB6 --provider perplexity` failed with
`Provider 'perplexity' not available`. This file therefore holds the literature
synthesis, as it does for CLN1. Per CLAUDE.md, nothing here is named
`-deep-research-<provider>.md`.

## What Clb6 is

Clb6 is a 380-residue B-type cyclin of the cyclin A/B subfamily (UniProt
`CC SIMILARITY`: "Belongs to the cyclin family. Cyclin AB subfamily."; two
cyclin-box repeats, Pfam `Cyclin_N` + `Cyclin_C`, PANTHER PTHR10177). It has no
catalytic activity of its own: it is the regulatory subunit that binds and
activates the single essential CDK Cdc28 (Cdk1), forming the curated
Clb6-Cdc28 kinase complex (ComplexPortal `CPX-339`; UniProt
`CC INTERACTION`: "P32943; P00546: CDC28; NbExp=3").

`CLB6` sits tail-to-tail with `CLB1` on chromosome VII, mirroring the
`CLB5`/`CLB2` pair, and the two S-phase cyclins arose by duplication
[PMID:8253070 "Two new B-type cyclin genes from Saccharomyces cerevisiae, called CLB5 and CLB6, are located in a tail to tail arrangement adjacent to the G2/M phase promoting cyclins CLB2 and CLB1, respectively"].
Transcription is late-G1, in the MBF/SBF G1/S program with `CLN1`, `CLN2` and the
replication genes
[PMID:8319908 "whose transcripts appear in late G1 along with those of CLN1, CLN2, and many genes required for DNA replication"],
and expression is cell-cycle periodic
[PMID:8253070 "Both genes are periodically expressed, peaking early in the cell cycle"].
UniProt records the same: `CC DEVELOPMENTAL STAGE` "Maximally expressed just
before cell cycle start."

## Core activity: S-phase CDK activator

Clb5 and Clb6 are the two cyclins that supply Cdc28 with its S-phase activity
[PMID:9732268 "The B-type cyclins Clb5 and Clb6 are the primary activators of the S phase function of the budding yeast CDK Cdc28"].
The activation is cyclin-specific, not merely permissive: when all nine Cdc28
cyclins were purified and assayed on one substrate, Swi6 Ser160 phosphorylation
was driven by Clb6 and essentially not by the others
[PMID:14993267 "by purifying all nine cyclins of Cdc28, we show that the specific phosphorylation of serine 160 is directed largely by Clb6-Cdc28 and not by other G 1 or mitotic cyclin-Cdc28 kinase complexes"].
That paper is the IDA/IMP source for the `GO:0016538` rows and is the first
direct demonstration of Clb6-Cdc28 substrate specificity
[PMID:14993267 "Thus, for the first time, we provide direct evidence for Clb6/Cdc28 substrate specificity"].

## G1/S and replication

`clb6` single mutants are viable with a mild late-G1/S delay, while the double
mutant with `clb5` cannot start replication on time
[PMID:8253070 "Loss of function mutants are viable, but clb5- mutants exhibit a delay in S phase whereas clb6- mutants show a delay in late G1 and/or S phase"];
[PMID:8319908 "Deletion of CLB6 has little or no effect, but deletion of CLB5 greatly extends S phase, and deleting both genes prevents the timely initiation of DNA replication"].
Clb6 can trigger S-phase entry on its own but cannot carry the cell through S
phase
[PMID:16508019 "Although either Clb5 or Clb6 can trigger the timely entry into S phase, Clb6 cannot promote normal progression through S phase without Clb5"].

The reason is protein stability, not activity: Clb5 persists to mitosis and is
destroyed by APC/C via a destruction box, whereas Clb6 lacks that box, carries
Cdc4 degrons in its N terminus and is destroyed by SCF(Cdc4) right at the G1/S
border
[PMID:16508019 "unlike Clb5, which is stable until mitosis, Clb6 is degraded rapidly at the G1/S border"];
[PMID:16508019 "Clb6 lacks the destruction box motif responsible for the anaphase promoting complex-mediated destruction of Clb5 but contains putative Cdc4 degron motifs in the N terminus"].
Turnover needs both Cdc28 and Pho85
[PMID:16508019 "Efficient degradation of Clb6 requires the activities of both Cdc28 and Pho85"],
and a hyperstabilized Clb6 rescues the `clb5` slow-S-phase defect
[PMID:16508019 "hyperstabilized Clb6 expressed from the CLB6 promoter rescued the slow S-phase defect exhibited by clb5Delta cells"].
Hence the division of labour recorded in the later literature: Clb5 fires early
and late origins, Clb6 only the early ones
[PMID:29263158 "Clb5 is required for the firing of both early and late replication origins, while Clb6 is only involved in the firing of the early origins"].

## Two Clb6-specific substrates

Both are nuclear proteins that Clb6-Cdc28 phosphorylation sends to the
cytoplasm, and in both cases the paralog Clb5 does not substitute:

1. **Swi6** (SBF/MBF subunit). Clb6-Cdc28 phosphorylates Ser160 and is required
   for Swi6 nuclear export
   [PMID:14993267 "We show that Clb6/Cdc28 kinase is required for this nuclear export"];
   the authors read Clb6 as a negative-feedback limb that curtails G1 transcription
   [PMID:14993267 "In this context, Clb6 can be seen as a negative regulator that curtails G 1 by promoting nuclear export of Swi6"],
   consistent with `CLB6` deletion raising SBF/MBF-dependent expression
   [PMID:14993267 "This conclusion is supported by the inhibitory effects of Clb6 overexpression and the stimulatory effects of CLB6 deletion on SBF- and MBF-dependent gene expression"].
2. **Rnr2** (ribonucleotide reductase small subunit). Clb6-Cdc28 phosphorylates
   the N-terminal TPSK motif, breaking the Rnr2-Wtm1 nuclear anchor so that
   Rnr2-Rnr4 is released to the cytoplasm and can form active RNR holoenzyme in S
   phase
   [PMID:29263158 "Deletion of CLB6 or removal of the CDK site results in an increased association of Rnr2 with its nuclear anchor Wtm1, nuclear retention of Rnr2-Rnr4, and an enhanced sensitivity to the RNR inhibitor hydroxyurea"].
   This is explicitly Clb6 and not Clb5
   [PMID:29263158 "our results demonstrate that the redistribution of R2 in S phase is specifically controlled by Clb6 but not its paralog Clb5, with which it shares 50% primary sequence identity"].

Together these make nuclear export the one process GOA records for Clb6 with two
independent Clb6-specific lines of evidence, which is why the `GO:0032880
regulation of protein localization` row is refined to `GO:0046827 positive
regulation of protein export from nucleus` rather than kept at the parent.

## Meiosis

`CLB5`/`CLB6` are also needed for premeiotic S phase, but the requirement is
only visible in the double mutant: the `clb6` homozygote replicates normally
[PMID:9732268 "No delay or defect in DNA replication could be detected in clb6/clb6 mutants (data not shown)"],
whereas `clb5/clb5 clb6/clb6` diploids make no premeiotic DNA at all
[PMID:9732268 "combining clb5 and clb6 mutations yielded a profound defect in which no premeiotic DNA replication could be detected even after 24 hr"]
and then segregate unreplicated chromosomes because the meiotic replication
checkpoint is never armed
[PMID:9732268 "We conclude that CLB5 and CLB6 are essential for premeiotic DNA replication and, consequently, for activation of a meiotic DNA replication checkpoint"].
So the claim behind the two `GO:0006279` rows holds, but it is a redundant,
meiosis-specific contribution: `KEEP_AS_NON_CORE` for both rows (the `IGI` and
the `IMP` share a term, so they take consistent actions), where `CLB5`'s own
review could `ACCEPT` it because the `clb5` single mutant does have a phenotype.

## Annotation decisions and why

- **`GO:0016538` → `GO:0061575` (4 rows, MODIFY).** Clb6 does not merely regulate
  Cdc28, it activates it; PMID:14993267 shows cyclin-specific stimulation of
  Cdc28 kinase activity by Clb6. `GO:0061575 cyclin-dependent protein
  serine/threonine kinase activator activity` is an `is_a` child of `GO:0016538`
  and is the term the CLN1/CLN2/CLN3 reviews settled on. Note for a later pass:
  `genes/yeast/CLB5` still `ACCEPT`s the parent `GO:0016538` on all three of its
  rows, so the two paralog reviews are inconsistent on this point; CLB5 is the one
  that should move.
- **`GO:0005515` → `GO:0019901` (2 rows, MODIFY).** Both IPI rows are with
  `UniProtKB:P00546` (Cdc28), so the informative term is `protein kinase binding`.
  Bare protein binding is uninformative per the protein-binding policy.
- **`GO:0044772` → `GO:0000082` (MODIFY).** The ARBA/InterPro IEA term is true but
  entailed by the `GO:0000082` rows this review accepts; the gene already carries
  the specific term.
- **`GO:0006355` → `GO:0045892` (MODIFY).** The row itself is an abstract-only
  ComplexPortal IMP from PMID:8319908 that I cannot read, but the direction of
  Clb6's effect on transcription is established independently by PMID:14993267
  (Swi6 export; `CLB6` deletion *raises* SBF/MBF output). The sign is the
  informative part, so the general term is refined rather than left alone. This
  differs from `CLB5`, which left its identical row `UNDECIDED` — correctly, since
  no Clb5-specific transcription result exists.
- **`GO:0005815 microtubule organizing center` (MARK_AS_OVER_ANNOTATED).** An IBA
  from a cyclin node whose donors are mitotic/spindle cyclins (`SGD:S000006323`
  = CLB2, PomBase `cdc13`/`cig2`, rat Ccnb). The SPB/spindle role in this family
  belongs to Clb3, Clb4 and Clb5 (PMID:8319908 "Clb5 also has a function, along
  with Clb3 and Clb4, in the formation of mitotic spindles"); nothing places Clb6
  there, and Clb6 is gone by the time spindles form. Same call as the CLB5 review.
- **`GO:0007089 traversing start control point` (MARK_AS_OVER_ANNOTATED).** Start
  in budding yeast is executed by the Cln cyclins; Clb5/Clb6 act after Start, on
  origin firing, and `CLB5`/`CLB6` transcription is itself downstream of Cln
  activity (PMID:8319908). Same call as the CLB5 review. The IBA node is seeded
  by *S. pombe* `SPAPB2B4.03`, where the cyclin-Start relationship differs.
- **`GO:0005575` ND (REMOVE, `nd_case: STALE`).** The SGD CC ND carries the bulk
  2013-08-07 date. Literature on this gene product does support a CC annotation:
  PMID:8253070 showed Clb6-Cdc28 association in vivo, and ComplexPortal has since
  made the `GO:0000307` IPI row from PMID:8319908 for the Clb6-Cdc28 holoenzyme
  (`CPX-339`). That is not a bare protein-binding IPI — it is a complex term in
  the CC aspect — so the "no data" claim is no longer true.

## `NEW` candidates considered and rejected

- **`GO:0046827 positive regulation of protein export from nucleus`** is not
  proposed as `NEW`: `GO:0032880` already covers the claim and is refined to it by
  MODIFY, so a separate row would be redundant.
- **`GO:0033314 mitotic DNA replication checkpoint signaling` / meiotic
  equivalent.** PMID:9732268 shows `clb5 clb6` diploids fail to arrest before
  meiosis I, but the paper's own reading is that the checkpoint is never armed
  because no replication happens — the cyclins are upstream of the signal, not
  part of it
  [PMID:9732268 "presumably because no replication signal can be generated"].
  Proposing a checkpoint term would annotate necessity rather than participation.
- **A term for Rnr2/RNR regulation** (e.g. regulation of ribonucleoside
  diphosphate reductase activity). Clb6 acts on RNR subunit localization, which
  `GO:0046827` captures; an activity-regulation term would assert a mechanism the
  paper attributes to subunit assembly, not to Clb6.
- **`GO:0006281`/hydroxyurea-sensitivity terms.** `clb6Δ` HU sensitivity in
  PMID:29263158 is a downstream consequence of dNTP supply; a DNA-repair process
  term is not warranted.

## Open questions recorded in the review

Clb6's two documented private substrates are both nuclear-export events, which
raises the question of whether export is a theme of Clb6-Cdc28 or an artifact of
which substrates were looked at; and the SCF(Cdc4)-driven destruction at G1/S
means Clb6's entire functional window is minutes wide, which no GO term expresses.
Both are in `suggested_questions`, with matching `suggested_experiments`.
