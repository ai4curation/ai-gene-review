# Trusted-cutoff check of electronic enzyme annotations

Back to [Enzyme Specificity Project](../ENZYME_SPECIFICITY.md).

**Bottom line:** most enzyme misannotations in automatically annotated databases are
overpredictions: the sequence resembles a family but does not belong to it. A family HMM
scored against its curated trusted cutoff catches many of them. On 37 reviewed electronic
enzyme rows, 11 of 12 accepted rows that had a family model passed the cutoff, and 10 of
13 removed rows that had one failed it. This check reproduces steps 2 and 4 of Schnoes et
al. 2009. It can tell an annotation lacks family support. It cannot show that a protein
is catalytically active, and it needs a family model to exist.

## Method

Schnoes et al. [PMID:20011109] judged an enzyme annotation correct only if the sequence
"scored sufficiently well against hand curated hidden Markov models (HMMs) to be
considered a member of the annotated family". They found that "The majority of
misannotations in the NR database were found to be overpredictions of these two types
(85%, SFA + BTC)".

`ai_gene_review.validation.enzyme_family_cutoff` applies the same test with NCBIfam
models (the successor to TIGRFAMs). Each model carries curated trusted (TC) and noise
(NC) cutoffs, and the release table maps models to EC numbers and GO terms:

1. GO term → EC numbers (QuickGO cross-references). Only complete EC numbers are used,
   because the test concerns a single reaction, not a class such as `oxidoreductase
   activity`.
2. Target families are the NCBIfam models that carry the EC or GO term. Observed families
   are those InterPro already reports for the protein.
3. The UniProt sequence is scored against each model with pyhmmer, with no reporting
   threshold and with HMMER's acceleration filters switched off, so a divergent sequence
   is scored instead of being discarded early (Schnoes scored permissively for the same
   reason). A non-positive bit score counts as no hit. As with HMMER `--cut_tc`, a hit
   passes only if both its full-sequence and best-domain scores reach TC.

| Verdict | Meaning |
|---|---|
| `ABOVE_TC` | A function-level target family passes TC |
| `BETWEEN_NC_TC` | Best target hit lies between the noise and trusted cutoffs (Schnoes's lenient band), or only a domain-level model passes |
| `BTC` | Target family hit, but below its noise cutoff (for a model with no curated noise cutoff, below its trusted cutoff, as the note says) |
| `SFA` | No target family hit; the protein matches other families |
| `NO_MODEL` | No NCBIfam model carries the function; inconclusive |

Every verdict also lists any other function-level family the protein passes at TC. Below
a cutoff, that is the paper's mandelate racemase case, where the sequence "scored above
the TC for the fuconate dehydratase family". On a pass, it marks overlapping families for
different reactions (MetX below). It can also list a broad family that coexists with the
target, such as "HAD-IA family hydrolase" next to phosphonoacetaldehyde hydrolase for
phnX, so read the list rather than counting it.

```bash
uv run python -m ai_gene_review.validation.enzyme_family_cutoff Q88KF6 --go GO:0004451
uv run python projects/ENZYME_SPECIFICITY/cutoff-check/run_cutoff_check.py
uv run python projects/ENZYME_SPECIFICITY/cutoff-check/page/build_page.py OUT.html  # results page
```

## Evaluation set

[genes.yaml](genes.yaml) lists 20 *P. putida* KT2440 reviews that each have a REMOVE on
an electronic enzyme row for a paralog or wrong-reaction reason, plus human PHYKPL and
HADH. The ACCEPT rows on the same genes serve as controls. The set is **enriched for
REMOVE rows by construction**, so the counts below show agreement on this set, not a
general error rate. The runner reads every live IEA/IBA molecular-function row that maps
to a complete EC number (37 rows; PHYKPL has none, as its transaminase term carries no
complete EC). Rows marked `retired` (retired or replaced in GOA) are skipped, since they
are not live annotations. The reviewer's action is never an input to the check, and
actions are read from the reviews at run time. Raw output: [results.yaml](results.yaml), which lists every target
family's score for each row; NCBIfam release `hmm_PGAP/20.0`. Where a row has several
target families, the scores quoted below are for the best one, the highest score as a
fraction of its trusted cutoff.

| Verdict | ACCEPT | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED |
|---|---|---|---|---|
| ABOVE_TC | 11 | 0 | 3 | 0 |
| BTC | 1 | 0 | 8 | 3 |
| NO_MODEL | 0 | 2 | 7 | 0 |
| SFA | 0 | 0 | 2 | 0 |

### Where the check and the reviewer agree

Several of the reviewers' REMOVE calls are recovered by scores alone. In each case the
competing family it finds is the function the reviewer accepted:

| Gene | Removed term | Target score / TC | Family the protein passes instead |
|---|---|---|---|
| prpB | isocitrate lyase | 58.4 / 275.9 (TIGR01346.1) | methylisocitrate lyase (NF008455.0, 552.4 / 353) |
| phnX | phosphoglycolate phosphatase | 35.4 / 180 (TIGR01449.2) | phosphonoacetaldehyde hydrolase (TIGR01422.2) |
| nspC | diaminopimelate decarboxylase | 43.7 / 297.9 (TIGR01048.1) | carboxynorspermidine decarboxylase (TIGR01047.1) |
| PP_3599 | 4-hydroxy-tetrahydrodipicolinate synthase | 108.7 / 206.1 (TIGR00674.1) | 5-dehydro-4-deoxyglucarate dehydratase (TIGR03249.1) |
| mdh | L-lactate dehydrogenase | 215.9 / 303.5 (TIGR01771.1) | malate dehydrogenase (NF004863.0) |
| hisI | phosphoribosyl-ATP diphosphatase | 152.0 / 187 (NF002747.0) | phosphoribosyl-AMP cyclohydrolase (NF000768.0) |
| purM | phosphoribosylamine-glycine ligase | no hit (SFA) | AIR synthase, PurM (TIGR00878.1) |
| puuD | urate oxidase | no hit (SFA) | T6SS sheath large subunit TssC (TIGR03355.1) |

Even a `NO_MODEL` verdict carries information through the competing-family list: kdsC
(N-acylneuraminate cytidylyltransferase) passes the KDO 8-P phosphatase family; mqo2 and
mqo3 ((S)-2-hydroxyglutarate dehydrogenase) pass malate:quinone oxidoreductase; serA
passes phosphoglycerate dehydrogenase.

### Undecided rows below the cutoff: what the follow-up found

Three rows the reviewers left UNDECIDED fall below their target family's cutoff with no
competing family above its own: ptxD hydroxypyruvate reductase and glyoxylate reductase
(80.8 / 403, NF012013.0) and PP_4638 methylenetetrahydrofolate reductase [NAD(P)H]
(26.3 / 293.7, TIGR00676.1). An earlier version of this page called these reviews to
revisit. A follow-up ([followup_scan.py](followup_scan.py), output
[followup.yaml](followup.yaml)) scored each protein against the sister model that matters
and scanned the whole KT2440 proteome. Neither verdict decides its row:

- **ptxD.** The only target model was GhrA, and ptxD resembles GhrB, so a low GhrA score
  was expected. NCBIfam has a GhrB model, NF011938.0, but it carries no EC number and only
  a general GO term, so the check never scored it as a target. Against it ptxD scores
  418.1 / 492, below the cutoff that E. coli GhrB passes at 690.3. No KT2440 protein passes
  that model, and ptxD is the closest, so the scan finds no other GhrB that would make
  ptxD a paralog. Its substrate stays open, as the review says.
- **PP_4638.** KT2440's canonical MetF, Q88D51, passes TIGR00676.1 (340.2 / 293.7), and
  PP_4638 does not (26.3). That confirms what the review already records: PP_4638 is not a
  MetF. The review keeps the row open because PP_4638's divergent MTHFR-like fold might
  carry noncanonical folate chemistry, and models built on canonical MetF cannot test
  that, so the row stays UNDECIDED.

A third row, PP_0556 NAD+ kinase, was flagged in the earlier run only because the runner
read a retired row. It no longer runs on retired rows.

### Where they disagree, and why

- **pyrC′ dihydroorotase: ABOVE_TC (864.7 / 644), but REMOVE.** PyrC′ is a pseudoenzyme
  that "lacks specific histidyl residues thought to be critical for DHOase enzymatic
  function" [PMID:7896697]. Family membership is real; catalysis is lost. This is
  Schnoes's step 3 (functional residues), which this check does not perform. Use
  `family_residue_validator` and the [Pseudoenzymes](../../PSEUDOENZYMES.md) workflow.
- **metXS homoserine O-acetyltransferase: ABOVE_TC, but REMOVE.** The protein passes
  both "homoserine O-acetyltransferase MetX" (NF001209.0, 579.9 / 331) and the
  "homoserine O-succinyltransferase MetX" model (NF047916.1, 697.8 / 560, family type
  `exception`). Each MetX row therefore lists the other model as a competitor that also
  passes. That flags the pair for review but does not settle it: the succinyl model
  wins on raw score, the acetyl model on score relative to its cutoff. The reviewer settled it from
  the curated UniProt entry and an experimental annotation.
- **PP_2325 2-dehydropantoate 2-reductase: ABOVE_TC, but REMOVE.** It passes both
  TIGR00745.1 (246.3 / 141.4) and the "putative 2-dehydropantoate 2-reductase" model
  NF004887.0 (541.1 / 360). The reviewer relied on biochemistry of the *P. aeruginosa*
  ortholog, which is inactive on ketopantoate. Experimental data outrank an HMM, and a
  family whose members include inactive paralogs cannot fix the substrate.
- **Human HADH (3S)-3-hydroxyacyl-CoA dehydrogenase: BTC (238.3 / 312, NF006143.0), but ACCEPT.**
  The accepted function has direct experimental support. NCBIfam cutoffs are set on
  prokaryotic members, so divergent eukaryotic orthologs fall below them. This is the
  paper's own caveat about trusted cutoffs, and the reason a BTC must never by itself
  override experimental evidence.

## How to use it in a review

- Run it on **electronic** enzyme rows (IEA from EC2GO or InterPro2GO, ARBA, UniRule,
  IBA), above all in multi-reaction superfamilies such as enolase, HAD, amidohydrolase,
  crotonase, VOC and SDR/MDR.
- `BTC` or `SFA` together with a competing family that passes is strong support for
  replacing the term (`MODIFY` to the competing activity, or `REMOVE`). Record the scores
  in `review.reason`. A `BTC` with no competitor says only that the protein is not in the
  family that carries the term. Before acting on it, run the check with `--library`, which
  reports the protein's closest function-level families from the whole NCBIfam library
  (see the [best-family sweep](sweep/RESULTS.md)): if it sits just outside a sister
  family, the BTC says nothing about its activity. Only when no
  related family fits either does it point to `MODIFY` toward a more general activity, the
  paper's own remedy: annotate only "at the level of function for which there is strong
  evidence".
- `ABOVE_TC` does not establish activity: check catalytic residues (pseudoenzymes), and
  check whether the family is broader than the specificity in question. Subunit models
  carry the whole complex's EC number, and a family that became a target only through its
  GO metadata can carry the sister reaction's term (six such models are listed in the
  [best-family sweep](sweep/RESULTS.md)).
- `NO_MODEL` is expected for most eukaryote-specific enzymes and says nothing either way.
- Never use the check alone to remove an experimental annotation.

## Specificity fingerprints

The metXS case shows the gap that remains once family membership is settled:
paralogs for different reactions can pass the same family models.
`ai_gene_review.validation.specificity_fingerprint` (`just enzyme-fingerprint-check`)
adds the step from Kinateder et al. 2024 [PMID:38284491]: read the residues an alanine
scan showed to decide the reaction, at the matching positions of the query. Fingerprints
are curated in `conf/specificity_fingerprints.yaml`, each citing its mutagenesis paper.
Read a verdict with its fingerprint's notes in that file: for the HolPase fingerprint a
`PARTIAL` that misses only D18 is a weak positive, and `CONTRAST` is effectively
unreachable because the paralogous phosphoserine phosphatases sit below its identity
floor. The first one, for the *P. aeruginosa* histidinol-phosphate phosphatase PA0335, finds
its full fingerprint in *P. putida* PP_5147.

## Limitations

- By default only target families and the families InterPro already reports are scored.
  With `--library` the protein is also scanned against every function-level model (with
  HMMER's default filters), and its closest families are reported. Without it, a lack of
  hits does not establish that the protein lacks the superfamily (Schnoes step 1).
- Coverage depends on NCBIfam's EC/GO mappings and is mainly prokaryotic.
- Target families are those whose EC numbers or GO terms include the annotated activity.
  A closely related model that carries only a general term (NCBIfam's GhrB model, for
  ptxD) is not scored as a target, so a BTC can mean only "not this sister family".
  The check cannot find that sister family by itself: besides target families it scores
  only the families InterPro reports, and InterPro reports none for ptxD because its
  scores fall below each model's reporting threshold. Run with `--library`, which finds
  GhrB as ptxD's closest family, or score named candidates as `followup_scan.py` does.
- A BTC with no competing family says the annotation lacks family support. It cannot
  rule out an activity carried by a divergent family that no model covers.
- The NCBIfam release and the InterPro and QuickGO responses can change. Results are tied
  to the recorded release.
