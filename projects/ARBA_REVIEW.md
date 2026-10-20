---
title: "ARBA Rule Review"
collections: [FUNCTION_PREDICTION]
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
species: [human, PSEPK, yeast, worm, DROME, mouse, SCHPO]
manifest:
  artifacts:
    - href: https://claude.ai/artifact/TAqNknNyGr8Rxdxobpwtfb
      title: Project brief
---

# ARBA Rule Review

**Bottom line:** UniProt's ARBA rules fail in two different ways, and they need
different fixes. Most failures are **construction failures**: mega-rules that OR
together tens to thousands of condition sets under one generic term, which
produce annotations that are true but say nothing (cytoplasm, membrane,
catalytic activity, system development). A smaller set are **consequent
failures**, where the rule asserts something false for the proteins it matches:
an activity the protein lacks, a process another protein performs, a process
that does not exist in the organism, or the function of a paralog. Of 6,051
ARBA annotations judged in our gene reviews, 75% were kept, 13% were rejected
as over-annotation or removed, and the rest were modified or left undecided.
Of the 1,394 not kept, 62% were true but uninformative and 9% were wrong.

We are doing this because ARBA output is the only annotation many proteins in
poorly curated organisms have, so its failure modes decide how far those
annotations can be trusted. Failures come first here; whether ARBA adds
anything new is only worth asking once we know where it goes wrong.

## Two sources of evidence

| | Rule reviews | Gene reviews |
|---|---|---|
| Unit judged | a whole rule (conditions, logic, consequent) | one annotation on one gene |
| Size | 76 rules in [`rules/arba/`](../rules/arba/) | 6,051 annotations from 2,305 rules |
| Question | is the rule well built and is its consequent right? | is this annotation true and useful for this gene? |
| Main bias | rules were mostly picked because GO curators flagged them | genes are weighted toward well-studied organisms |

The two barely overlap: only 26 of the 76 reviewed rules appear in any gene
review, and the rules whose annotations gene reviewers reject most often have
no rule review. They can also disagree for good reason. ARBA00028334
("regulation of gene expression", 930 condition sets when reviewed; 932 in the
current download) is still live in UniProt, and our own rule review proposes
deprecating it, yet gene reviewers kept 21 of its 38 annotations as true but
non-core; a badly built rule can still emit many true rows.

Where both exist they agree on the specific errors:

- ARBA00090718 assigns (S)-2-hydroxyglutarate dehydrogenase activity to SerA
  family proteins. The rule review says DEPRECATE; the *P. putida* serA review
  removed the row, because SerA makes the (R) enantiomer.
- ARBA00089174 assigns adaptive thermogenesis from PM20D1 FunFams across
  Eukaryota. The rule review says the scope should be mammals; the fission-yeast
  cps1 review removed the row.
- ARBA00035068 and ARBA00047230 assign myotubularin phosphatase activities. The
  rule reviews flag missing exclusion of non-catalytic members; the fly CG6051
  review removed both rows, because CG6051 is a FYVE protein with no phosphatase
  domain.

## Rule-level failure modes

Classification of all 76 rule reviews:
[ARBA_REVIEW/rule_failure_modes.yaml](ARBA_REVIEW/rule_failure_modes.yaml).
Each rule has one primary mode and any number of secondary ones.

| Mode | Primary | Any | What it means |
|---|---:|---:|---|
| Mega-rule | 31 | 41 | tens to thousands of OR'd condition sets, impossible to audit |
| Too general | 0 | 25 | consequent true but uninformative (keyword classes such as Transferase, Kinase) |
| Heterogeneous consequent | 14 | 24 | unrelated families pooled under a term that fits only some of them |
| Logic error | 3 | 17 | AND over signatures that rarely co-occur, duplicate conditions, zero matches |
| Arbitrary taxon | 0 | 14 | restrictions such as Primates, Mus or Homo with no biological reason |
| Spurious signature | 8 | 8 | signature not diagnostic of the function; association looks data-mined |
| Non-catalytic homolog | 2 | 5 | activity assigned to pseudoenzymes or cofactors |
| Activity mismatch | 4 | 4 | wrong specific activity, or two activities conflated |
| Mechanism overextended | 3 | 4 | a lineage-specific mechanism applied across taxa |
| Stale | 1 | 3 | obsolete consequent or withdrawn rule |
| Substrate or cargo | 2 | 2 | the protein is what the process acts on |
| Too specific | 2 | 2 | claims direction, location or a precise sub-process |
| Redundant with InterPro2GO | 1 | 2 | every condition already maps to the same term |
| Sound | 4 | 4 | rule or its core correct |

One further rule (ARBA00022603) could not be assessed.

Cases worth knowing:

- **Scale.** The largest rules are ARBA00022679 (Transferase keyword, 4,473
  condition sets, about 14 million proteins), ARBA00022801 (Hydrolase, 4,070),
  ARBA00023002 (Oxidoreductase, 2,105) and ARBA00004173 (Mitochondrion, 1,490).
- **Sound biology, bad construction.** Several rules have a correct core buried
  in a mega-rule: helicases, superoxide dismutase, UMP biosynthesis, spliceosome
  components, isoprenoid metabolism (64 of 94 sets sound, human subset fully
  correct) and the mitochondrion rule (TOM40, MIC60, COX subunits).
- **Heterogeneous consequents.** ARBA00028655 assigns phosphatidylinositol
  biosynthesis from 25 condition sets, of which 2 identify PI synthase; the
  rest are PI kinases, phosphatases and GPI-anchor enzymes. ARBA00004218 assigns
  acrosome to 35 families including epithelial sodium channels and complement.
- **Logic errors.** ARBA00047244 ANDs three urease signatures that sit on
  separate bacterial subunits, so at most 10 of 851 ureases match.
- **One signature, two consequents.** CATH FunFam `3.40.50.720:FF:000041`
  drives both a correct call (ARBA00093701, L-serine biosynthesis) and a wrong
  one (ARBA00090718, (S)-2-hydroxyglutarate dehydrogenase). The signature is
  fine; the second consequent is not.
- **Maintenance.** ARBA00028538 asserts GO:0046467, which GO obsoleted on
  2025-12-09; UniProt modified the rule six days later without noticing.

## Annotation-level failure modes

From [ARBA_REVIEW/GENE_SIDE_RESULTS.md](ARBA_REVIEW/GENE_SIDE_RESULTS.md),
generated by
[ARBA_REVIEW/gene_side_failures.py](ARBA_REVIEW/gene_side_failures.py).

**The more general the term, the more often it is rejected.** Generality is the
number of is_a/part_of descendants of the term in GO.

| ARBA term | Rows | Kept | Modified | Over-annotated | Removed |
|---|---:|---:|---:|---:|---:|
| very general (>200 descendants) | 1,347 | 55% | 15% | 25% | 3% |
| general (21-200) | 1,642 | 75% | 11% | 12% | 2% |
| specific (1-20) | 1,984 | 83% | 8% | 4% | 2% |
| leaf | 1,078 | 86% | 5% | 4% | 3% |

The removal rate is flat at 2-3% across all levels: general terms are rejected
for saying too little, while specific terms are about as likely to be wrong.

**What went wrong in the 1,394 rows not kept:**

| Kind | Rows | Share |
|---|---:|---:|
| true but uninformative (a more specific term exists) | 867 | 62% |
| overreach (indirect effect, no evidence, too specific) | 179 | 13% |
| wrong | 125 | 9% |
| different term needed | 105 | 8% |
| unclassified | 118 | 8% |

These categories come from the proposed replacement term for MODIFY rows and
from keyword cues in the review's reason for the rest, so they are approximate;
every row's category and cue is in `gene_side_rows.tsv` for checking.

**The 133 annotations reviewers removed**, classified by hand in
[ARBA_REVIEW/gene_side_remove_modes.yaml](ARBA_REVIEW/gene_side_remove_modes.yaml):

| Mode | Rows | Example |
|---|---:|---|
| wrong location | 15 | integral membrane PSEPK/pgsA annotated to cytoplasm |
| wrong activity | 15 | HEXA, a hydrolase, annotated as an acetylglucosaminyltransferase |
| wrong process | 14 | GCK annotated to nicotinamide nucleotide metabolism |
| wrong taxon | 13 | stomatal patterning and drought response on the *Aspergillus* regulator flbD |
| role confusion | 13 | SPHK1 and SPHK2, which make S1P, annotated as S1P receptors |
| too general | 11 | XIAP annotated to protein-containing complex |
| wrong paralog | 11 | MAP2K1, an ERK-pathway kinase, annotated to stress-activated MAPK signalling |
| unsupported | 10 | no evidence in the organism, or mutants argue against it |
| term misread | 8 | SIX3 and SIX6, eye-development factors, annotated to visual perception |
| indirect | 8 | BAX and BAK1 annotated to regulation of intracellular signal transduction |
| non-catalytic homolog | 7 | CASK, whose guanylate kinase domain is inactive, annotated with GMP kinase activity |
| wrong direction | 3 | PTEN annotated to positive regulation of macromolecule metabolism |
| other | 5 | obsolete term, pseudogene, false domain prediction, too specific |

Role confusion is the mode GO curation guidance warns about most: the protein
is next to the step, not doing it. Besides SPHK1/2 it covers RGS20 (a GTPase
activator) annotated with GTPase activity, the fly FYVE protein CG6051 (binds
PI3P) annotated as a PI3P phosphatase, Pcbd1/2 (regenerate the phenylalanine
hydroxylase cofactor) annotated with phenylalanine hydroxylase activity, and
the ERAD ligases RNF5 and RNF185 annotated to ER mannose trimming.

## How the two levels connect

| Rule-level mode | What it produces in gene reviews |
|---|---|
| mega-rule, too general | the bulk of over-annotation: cytoplasm (ARBA00026971, 23 of 155 rows rejected), membrane, catalytic activity, system development |
| heterogeneous consequent | wrong process and wrong activity rows |
| substrate or cargo | role confusion |
| non-catalytic homolog | non-catalytic homolog |
| mechanism overextended | wrong taxon |
| activity mismatch | wrong activity |

The rules behind the most rejected gene-review rows are mostly single-term
rules for generic terms that no rule review has looked at (cytoplasm,
membrane, animal organ development, catalytic activity, protein-containing
complex). Per-rule counts are in
[ARBA_REVIEW/gene_side_rules.tsv](ARBA_REVIEW/gene_side_rules.tsv).

## Redundancy between rules, and the generic rules

From [ARBA_REVIEW/RULE_REDUNDANCY.md](ARBA_REVIEW/RULE_REDUNDANCY.md),
generated by [ARBA_REVIEW/rule_redundancy.py](ARBA_REVIEW/rule_redundancy.py)
from UniProt's full ARBA rule set (82,771 rules, of which 12,936 assert a GO
term) and QuickGO annotation counts.

**ARBA keeps one rule per GO term.** No term is asserted by two rules: every
family that predicts a term is folded into that term's single rule as another
OR'd condition set. So redundancy never arises between rules for the same
term; it arises across levels, between a generic rule and a more specific one.

**A large share of the rule base is dead weight.** 62% of all condition sets
(145,142 of 232,979) are covered by a condition set of a rule asserting a more
specific term: same or fewer signatures, no negative conditions, same or no
taxon restriction. UniProt keeps only the most specific ARBA term on a protein
(only 6 of 2,411 reviewed genes carry an ARBA term together with an ARBA
descendant of it), so a covered set never emits anything. 2,678 rules are
covered in every set, and 57 of 60 sampled ones produce no annotations at all;
in a random sample of all GO rules, 19 of 60 produce none. These rules cost
maintenance and auditing, not annotation quality.

**Where generic rules do fire, the gene usually has a better term already.**
For 36 generic rules (term with more than 200 GO descendants, at least 10
reviewed annotations), a more specific term from another source (curation,
PAINT, InterPro2GO) was already on the gene in 80-100% of reviewed cases for all
but four of them. Reviews track this:

| Group | Rules | Specific term already present | Reviews kept | Proposed action |
|---|---|---|---|---|
| Generic activity | catalytic activity; oxidoreductase activity | 95-100% | 13-27% | deprecate |
| Generic development and regulation | system development; animal organ development; cell development; regulation of multicellular organismal process; regulation of intracellular signal transduction; cellular response to oxygen-containing compound | 91-100% | 23-47% | deprecate |
| Other generic process and complex terms | protein-containing complex; lipid metabolic process; response to stress; regulation of gene expression; signal transduction; anatomical structure morphogenesis | 82-97% | 26-62% | deprecate, or restrict to proteins with no more specific annotation |
| Generic membranes | membrane; endomembrane system | 97-98% | 54-63% | deprecate membrane; review endomembrane system |
| Main compartments | nucleus; plasma membrane; cytoplasm | 32%, 43%, 80% | 79%, 81%, 72% | keep: nucleus and plasma membrane often add the only location; cytoplasm is mostly redundant but rarely wrong |

The proposed actions are judgements from these numbers, not computed; several
rules rest on 10-15 reviewed annotations. The sample is biased toward
well-studied genes, so in poorly curated proteomes a generic rule may more
often be the only annotation, and there it is closer to the unique-annotation
question below than to redundancy.

## Unvetted predictions used as evidence in our own reviews

Our gene reviews also cite predictions as if they were evidence. Validation now
applies two global rules to every UniProt quote, whatever it supports:

- A quoted statement must not rest only on an unvetted prediction: an ARBA
  association rule, annotation imported unchecked from the submitter, a
  machine-generated protein name (ProtNLM), or an electronic GO line. Family
  and domain classification (NCBIfam, signature matches, curated UniRule rules
  such as HAMAP, "Belongs to the X family" notes) is not in this group: it
  reliably establishes membership, and membership is a fair argument for
  function. A family note whose only evidence is ARBA is still an unvetted
  prediction. ARBA is different in kind: its rules transfer annotation from
  co-occurring signatures, guilt by association.
- A quote must not be a label that restates an annotation: protein names and
  EC numbers, keywords, or the record's own GO lines.
- Protein existence (`PE`) is not evidence of function: it may argue that an
  annotation rests on prediction, but not support accepting one. An accepted ND
  annotation needs evidence that the literature was searched.

Across all gene reviews (as of 2026-10-20), 1,795 quotes in 600 reviews rest
on unvetted predictions; ARBA is a source for 1,045 of them, electronic GO lines
for 399 and imported submitter annotation for 354. They support 505 accepted
electronic annotations and 388 core functions. Separately, 3,252 quotes in 971
reviews are labels: mostly protein names (2,430) and the record's own GO lines
(680). Most of the rise since the 2026-10-16 counts comes from a fix to the
check: it now locates quotes copied with their flat-file line code
(`DR   GO; ...`), about a tenth of all UniProt quotes, which it had skipped
silently. The rest is new reviews. Nine quotes cite protein existence to accept
a function or support a core function, four of them for ND root terms.

All three are warnings (`uniprot_quote_unvetted_prediction`,
`uniprot_quote_restating_field`, `uniprot_quote_existence_as_support`). The
inventory is in
[ARBA_REVIEW/UNIPROT_QUOTE_AUDIT.md](ARBA_REVIEW/UNIPROT_QUOTE_AUDIT.md), from
[ARBA_REVIEW/uniprot_quote_audit.py](ARBA_REVIEW/uniprot_quote_audit.py).

## Quality of the rule reviews themselves

The rule reviews are useful but uneven, and some of their arguments do not hold:

- Many reviews cite a limit of 12 condition sets as best practice. The limit is
  the analysis tool's cap, not an ARBA or GO guideline.
- One review (ARBA00022603) is UNDECIDED with no rule data. Two concern rules
  already withdrawn from UniProt (ARBA00088072, ARBA00095398).
- 26 of the 75 reviews that state a confidence put it at 0.5 or below.

## What ARBA adds

Only after the failures: 96% of the ARBA annotations reviewers accepted repeat
the same or a more specific term already present from curation, PAINT or another
pipeline. The remaining 112 annotations ([UNIQUE_ACCEPTS.md](ARBA_REVIEW/UNIQUE_ACCEPTS.md),
from `unique_accepts.py`) are mostly in less-curated organisms (32 in
*P. putida* alone), and being the only source is not evidence of being right;
some of those acceptances rest only on UniProt text that ARBA itself generated.

For process annotations specifically, the
[ARBA deployment check](PATHWAY_SATISFIABILITY/arba_deployment/README.md)
tests whether a protein's activity plus a curated pathway module entails the
ARBA term in that organism. Where the module's process is exactly the ARBA
term, reviewers kept 93% of entailed annotations and removed none.

## Next steps

- Send UniProt the inert rules (covered in every condition set) and the
  covered condition sets as pruning candidates, and the generic rules proposed
  for deprecation above.
- Measure generic-rule redundancy on a poorly curated proteome (e.g. all
  *P. putida* ARBA annotations via QuickGO) to test the bias noted above.
- Check the keyword heuristic against a hand-labelled sample of
  over-annotation and MODIFY rows, as was done for REMOVE.
- Re-ground the accepted annotations, core functions and new annotations whose
  only support is an unvetted prediction, starting with ARBA annotations
  supported by ARBA text.
- Report the role-confusion and non-catalytic-homolog cases to UniProt with
  the gene reviews as evidence, since these are wrong rather than vague.

## Files

- [ARBA_REVIEW/rule_failure_modes.yaml](ARBA_REVIEW/rule_failure_modes.yaml):
  failure modes of the 76 rule reviews
- [ARBA_REVIEW/gene_side_failures.py](ARBA_REVIEW/gene_side_failures.py):
  gene-review breakdown; writes `GENE_SIDE_RESULTS.md`, `gene_side_rows.tsv`
  and `gene_side_rules.tsv`
- [ARBA_REVIEW/gene_side_remove_modes.yaml](ARBA_REVIEW/gene_side_remove_modes.yaml):
  hand classification of the 133 removed annotations
- [ARBA_REVIEW/uniprot_quote_audit.py](ARBA_REVIEW/uniprot_quote_audit.py):
  inventory of UniProt quotes that cite unvetted predictions or labels; writes
  `UNIPROT_QUOTE_AUDIT.md` and `uniprot_quote_findings.tsv`
- [ARBA_REVIEW/rule_redundancy.py](ARBA_REVIEW/rule_redundancy.py):
  redundancy across all ARBA GO rules and the generic-rule review; writes
  `RULE_REDUNDANCY.md` and `rule_redundancy.tsv`
- [docs/rule_review_workflow.md](../docs/rule_review_workflow.md): how rule
  reviews are made
