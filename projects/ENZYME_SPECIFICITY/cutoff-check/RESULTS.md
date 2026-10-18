# Trusted-cutoff check of electronic enzyme annotations

Back to [Enzyme Specificity Project](../ENZYME_SPECIFICITY.md).

**Bottom line:** most enzyme misannotations in automatically annotated databases are
overpredictions: the sequence resembles a family but does not belong to it. A family HMM
scored against its curated trusted cutoff catches many of them. On 38 reviewed electronic
enzyme rows, 11 of 12 accepted rows that had a family model passed the cutoff, and 11 of
14 removed rows that had one failed it. This check reproduces steps 2 and 4 of Schnoes et
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
   threshold. As with HMMER `--cut_tc`, a hit passes only if both its full-sequence and
   best-domain scores reach TC.

| Verdict | Meaning |
|---|---|
| `ABOVE_TC` | A function-level target family passes TC |
| `BETWEEN_NC_TC` | Best target hit lies between the noise and trusted cutoffs (Schnoes's lenient band), or only a domain-level model passes |
| `BTC` | Target family hit, but below its noise cutoff |
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
```

## Evaluation set

[genes.yaml](genes.yaml) lists 20 *P. putida* KT2440 reviews that each have a REMOVE on
an electronic enzyme row for a paralog or wrong-reaction reason, plus human PHYKPL and
HADH. The ACCEPT rows on the same genes serve as controls. The set is **enriched for
REMOVE rows by construction**, so the counts below show agreement on this set, not a
general error rate. The runner reads every IEA/IBA molecular-function row that maps to a
complete EC number (38 rows; PHYKPL has none, as its transaminase term carries no complete
EC). The reviewer's action is never an input to the check. Raw output:
[results.yaml](results.yaml), NCBIfam release `hmm_PGAP/20.0`.

| Verdict | ACCEPT | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED |
|---|---|---|---|---|
| ABOVE_TC | 11 | 0 | 3 | 0 |
| BTC | 1 | 0 | 9 | 3 |
| NO_MODEL | 0 | 2 | 7 | 0 |
| SFA | 0 | 0 | 2 | 0 |

### Where the check and the reviewer agree

Several of the reviewers' REMOVE calls are recovered by scores alone. In each case the
competing family it finds is the function the reviewer accepted:

| Gene | Removed term | Target score / TC | Family the protein passes instead |
|---|---|---|---|
| prpB | isocitrate lyase | 69.1 / 562 | methylisocitrate lyase (NF008455.0, 552.4 / 353) |
| phnX | phosphoglycolate phosphatase | 35.4 / 180 | phosphonoacetaldehyde hydrolase (TIGR01422.2) |
| nspC | diaminopimelate decarboxylase | 43.7 / 298 | carboxynorspermidine decarboxylase (TIGR01047.1) |
| PP_3599 | 4-hydroxy-tetrahydrodipicolinate synthase | 108.7 / 206 | 5-dehydro-4-deoxyglucarate dehydratase (TIGR03249.1) |
| mdh | L-lactate dehydrogenase | 215.9 / 304 | malate dehydrogenase (NF004863.0) |
| hisI | phosphoribosyl-ATP diphosphatase | 152.0 / 187 | phosphoribosyl-AMP cyclohydrolase (NF000768.0) |
| purM | phosphoribosylamine-glycine ligase | no hit (SFA) | AIR synthase, PurM (TIGR00878.1) |
| puuD | urate oxidase | no hit (SFA) | T6SS sheath large subunit TssC (TIGR03355.1) |

Even a `NO_MODEL` verdict carries information through the competing-family list: kdsC
(N-acylneuraminate cytidylyltransferase) passes the KDO 8-P phosphatase family; mqo2 and
mqo3 ((S)-2-hydroxyglutarate dehydrogenase) pass malate:quinone oxidoreductase; serA
passes phosphoglycerate dehydrogenase.

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
  wins on raw score, the acetyl model on margin over TC. The reviewer settled it from
  the curated UniProt entry and an experimental annotation.
- **PP_2325 2-dehydropantoate 2-reductase: ABOVE_TC for "putative 2-dehydropantoate
  2-reductase" (NF004887.0), but REMOVE.** The reviewer relied on biochemistry of the
  *P. aeruginosa* ortholog, which is inactive on ketopantoate. Experimental data outrank
  an HMM, and the model's own name is hedged.
- **Human HADH (3S)-3-hydroxyacyl-CoA dehydrogenase: BTC (317.7 / 508), but ACCEPT.**
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
  in `review.reason`. A `BTC` with no competitor points to `MODIFY` toward a more general
  activity, which is the paper's own remedy: annotate only "at the level of function for
  which there is strong evidence".
- `ABOVE_TC` does not establish activity: check catalytic residues (pseudoenzymes), and
  check whether the family is broader than the specificity in question.
- `NO_MODEL` is expected for most eukaryote-specific enzymes and says nothing either way.
- Never use the check alone to remove an experimental annotation.

## Limitations

- Only target families and the families InterPro already reports are scored, not the
  whole library. A lack of hits therefore does not establish that the protein lacks the
  superfamily (Schnoes step 1).
- Coverage depends on NCBIfam's EC/GO mappings and is mainly prokaryotic.
- The NCBIfam release and the InterPro and QuickGO responses can change. Results are tied
  to the recorded release.
