---
title: Horse and mammalian function-prediction benchmark design
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Horse and mammalian function-prediction benchmark design

**Start with the [40 selected horse genes](horse40.md) that have informative
released ProtNLM2 functional predictions.** Evaluate those horse records using
sequence evidence and characterized mammalian counterparts, then build a broader
mammalian set from the cases whose identity and evidence support projection.
Coverage determines the starting cohort: this is a targeted horse-first selection.

The selected set contains 89 GO predictions and 17 function descriptions across
40 distinct genes. Names alone are not an evaluation target or selection criterion.
The census and mammalian challenge leads below support subsequent review and
expansion. The original ARGO-ProtNLM-50 remains unchanged.

This is a selection and availability audit, dated **8 September 2026**, not a
completed biological adjudication or a newly scored benchmark.
[Parent project](../PROTNLM_EVALUATION.md).

## What is available

The [official ProtNLM2 accession list](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv)
contains **26,856 protein records**, including **404 horse records** (taxon 9796).
Horse is the fifth-largest species group in that list. Human has 151 records,
mouse 101, and rat 157. These are records with some ProtNLM2 output, not necessarily
GO predictions, distinct genes, or the full set of older ProtNLM name annotations.
The horse list has 357 distinct first gene-name labels, 41 unnamed records, and
six repeated labels. Gene symbols alone are therefore insufficient for deduplication.

All **813 listed records** across these four species returned predictions from
the API. The counts below come from those responses:

| Species | Records | With GO | GO statements | With function text | With location | Name only |
|---|---:|---:|---:|---:|---:|---:|
| Horse | 404 | 147 | 281 | 52 | 188 | 101 |
| Human | 151 | 43 | 64 | 25 | 70 | 47 |
| Mouse | 101 | 21 | 46 | 31 | 42 | 22 |
| Rat | 157 | 49 | 67 | 34 | 68 | 43 |

Columns overlap except “name only,” which excludes records with GO, function,
location **or keyword** predictions. Horse also has 25 keyword-bearing records.
There are 37 horse records with function text but no GO predictions, so a
GO-only selection would exclude much of the narrative evaluation opportunity.

The [census](mammal-benchmark/species-counts.csv),
[record inventory](mammal-benchmark/inventory.csv), and
[prediction statements](mammal-benchmark/prediction-statements.csv) distinguish GO,
function text, subcellular location, keywords and name-only records. The
[reproduction instructions](mammal-benchmark/README.md) describe the frozen inputs
and API queries. Model scores and Evidencer provenance remain in the raw snapshot;
neither is treated as biological ground truth.

**Release membership and API availability differ.** None of the 2,032 current
human, mouse and rat review accessions (1,888/77/67 respectively) exactly matches this
published accession list. However, direct API checks retrieve predictions for
human PUS3/Q9BZE2, NOVA2/Q9UNW9 and LONP2/Q86WA8 outside that list. PUS3 receives
tRNA processing and pseudouridine synthesis predictions. Conversely, API checks
for KLB/Q86Z14, ADPRHL1/Q8NDY3, PLD5/Q8N7P1, MAGI3/Q5TCQ9, PHYKPL/Q8IUZ5,
mouse Egf/P01132 and rat Casp3/P55213 returned HTTP 404. A missing accession-list
match does not prove that no prediction is served. Keep any supplemental API
cohort separately identified, and check availability before commissioning new runs.
The [supplemental response snapshot](mammal-benchmark/supplemental-api-examples.json)
preserves these examples outside the census denominator.

## Five immediate cases from the released mammalian records

These examples are selection leads based on actual API output. Identity,
orthology, sequence completeness and individual claims still need adjudication.

| Record | Actual ProtNLM2 output | Why it is useful |
|---|---|---|
| Horse MTMR9, [A0A9L0T3C1](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0T3C1) | Seven GO terms, including positive regulation of phosphatase activity, phosphatase binding, enzyme regulator activity and protein stabilization; no intrinsic phosphatase activity term | A promising **successful distinction** between an inactive enzyme homolog and its regulatory role. Human MTMR9 activates/stabilizes active partners; verify conservation before transferring each claim. |
| Horse PLD5, [A0A5F5PH10](https://rest.uniprot.org/uniprotkb/protnlm/A0A5F5PH10) | PLD phosphodiesterase **domain-containing** name, membrane location and intracellular organelle GO term | The output does **not** assert phospholipase catalysis. Test whether the evaluator distinguishes domain naming from activity, and measures missing informative function separately from false positives. |
| Horse MAGI3, [A0A9L0SMC6](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0SMC6) | PDZ domain-containing protein; no GO terms | A domain-level output on a scaffold with a degenerate guanylate-kinase-like domain. Useful for informativeness/coverage, not automatically an enzyme-activity error. |
| Rat Mtmr12, [A0A8I5ZMD5](https://rest.uniprot.org/uniprotkb/protnlm/A0A8I5ZMD5) | Myotubularin phosphatase **domain-containing** name, membrane location and cytoplasm GO term | Another case where the name alone must not be scored as an explicit phosphatase-activity claim. |
| Rat Ptk7, [A0A8I6ALM9](https://rest.uniprot.org/uniprotkb/protnlm/A0A8I6ALM9) | Correctly qualified inactive-kinase name, but function text includes adult visual-system lamina innervation and R1–R6 axon targeting; no GO terms | Strong lead for a **taxon-specific narrative error despite a sensible protein name**. Evidencer cites phmmer hit Q6AWJ9, the [Drosophila off-track protein](https://rest.uniprot.org/uniprotkb/Q6AWJ9.txt). Separate conserved adhesion/signaling claims from fly visual-system details. |

For MTMR9, primary studies demonstrate activation of MTMR6
([PMID:19038970](https://pubmed.ncbi.nlm.nih.gov/19038970/)) and regulation of MTMR8
and autophagy ([PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/)). These
support a transfer hypothesis; they are not horse experiments. Importantly,
absence of catalysis does not exclude regulation of dephosphorylation or autophagy.

## Existing mammalian reviews provide an evidence-search shortlist

I checked the exact accession/GO pairs below against live QuickGO, preserving
[query results](mammal-benchmark/candidate-goa-2026-09-08.json) and a compact
[source table](mammal-benchmark/candidate-goa-check.csv). Presence verifies the
annotation and its provenance; it does not by itself verify our proposed criticism.
Existing YAML decisions are leads, not benchmark labels.

| Candidate | Claim to test | Current annotation status | Role in the challenge set |
|---|---|---|---|
| Human KLB/Q86Z14 | Glycoside hydrolase activity, GO:0004553 | InterPro IEA present | Strong pseudoenzyme seed. The human structure identifies the missing catalytic glutamates in both domains; test retention of FGF co-receptor function. [Primary structure study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6594174/). |
| Human ADPRHL1/Q8NDY3 | ADP-ribosylarginine-protein hydrolase activity, GO:0003875 | UniProt IEA present | Pseudoenzyme seed requiring substrate-specific negative evidence. Do not turn lack of tested activity into a claim that every conceivable catalytic function is impossible. [Primary ARH-family assay](https://pubmed.ncbi.nlm.nih.gov/17075046/); inspect the local sequence analysis and additional assays for the exact arginine-linked substrate claim. |
| Human DPYSL2/Q16555 | Hydrolase activity, GO:0016787 | InterPro IEA present | CRMP versus active dihydropyrimidinase comparison. Use catalytic-site evidence and the existing OpenScientist investigation; preserve cytoskeletal function. CRMP1/DPYSL2/DPYSL5 are one family block, not three independent successes. |
| Human PLD5/Q8N7P1 | Generic catalytic activity, GO:0003824 | InterPro IEA present | Connects to an available horse record. Establish precisely which activity is refuted; do not infer complete catalytic inactivity solely from an inactive phospholipase motif. |
| Human MAGI3/Q5TCQ9 | GMP metabolic process, GO:0046037 | GOC logical-inference IEA present | Tests propagation from an erroneous kinase assignment into a process term. Evidence must address the biological process as well as the inactive domain. [Primary MAGI3 study](https://pubmed.ncbi.nlm.nih.gov/27205883/). |
| Mouse Egf/P01132 | Guanyl-nucleotide exchange factor activity, GO:0005085 | Ensembl IEA and GO_Central ISO present | Classic NPI candidate: receptor ligand versus downstream exchange-factor activity. Separate the ligand's signaling role from a molecular activity belonging to another protein. [Source protein record](https://rest.uniprot.org/uniprotkb/P01132.txt). |
| Rat Casp3/P55213 | Aspartic-type endopeptidase activity, GO:0004190 | Ensembl IEA and RGD ISO present | Classic NPI candidate: Asp cleavage specificity versus a cysteine catalytic nucleophile. Pair with its correct cysteine-protease function and an actual aspartic protease. [Source protein record](https://rest.uniprot.org/uniprotkb/P55213.txt). |
| Mouse Serpinh1/P19324 | Serine-protease inhibitor activity, GO:0004867 | InterPro IEA and PAINT IBA present | A non-inhibitory serpin/collagen chaperone, **not an inactive enzyme**. Keep as a separate family-function divergence class. [Primary Hsp47 structural study](https://pubmed.ncbi.nlm.nih.gov/22847422/). |
| Human PHYKPL/Q8IUZ5 | Transaminase activity, GO:0008483 | Absent in this live query; present in the cached review | Historical wrong-mechanism challenge. Purified human protein catalyzes ammoniophospholyase chemistry. Compare with active AGXT2; classify family/subfamily confusion separately from classic NPI. [Primary biochemical study](https://pubmed.ncbi.nlm.nih.gov/22241472/). |
| Mouse Cftr/P26361 | Isomerase activity, GO:0016853 | Absent in this live query; present in the cached review | Historical NPI lead requiring a frozen source annotation and evidence audit before admission. |
| Rat Hmgcs2/P22791 | Mevalonate-pathway farnesyl diphosphate biosynthesis, GO:0010142 | Absent in this live query; present in the cached review | Historical paralog/compartment challenge against cytosolic HMGCS1. Retain mitochondrial ketogenesis and the shared catalytic activity. |
| Rat Ratn1/P02761 | Insulin receptor activity, GO:0005009 | UniProt ISS present, **not IEA** | Strong architecture-mismatch lead: a secreted lipocalin versus an insulin receptor. Keep as a similarity-transfer comparator, outside electronic-only totals. |

An additional deliberate trap for an overzealous evaluator is human **PANK4**:
its pantothenate-kinase domain is inactive, but the protein also has a phosphatase
domain. It must not receive a blanket “non-enzymatic” label. See the
[primary kinase-assay paper](https://pubmed.ncbi.nlm.nih.gov/30927326/) and
[CoA-regulation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9352595/).

## Selected horse cohort and later mammalian expansion

The [40-gene list](horse40.md) starts with actual horse outputs. Selection is
manual and retrospective, based on specific functional claims, biological
variety, and useful contrasts. It includes 27 GO-bearing genes and 17 with
function descriptions; four have both. There are no name-only records and no
separate random-sample or mammalian-control quota.

- Examine the deposited horse sequence and exact predicted claim first.
- Use characterized human, mouse and rat counterparts to evaluate that claim
  after establishing orthology/subfamily placement and sequence completeness.
- Assess promising supported predictions alongside questionable ones. MTMR9 and
  PTPRN2 allow catalytic-versus-regulatory questions; DNMT3A and DNMT3L provide
  a within-cohort active/regulatory comparison. These are review questions, not
  predetermined verdicts.
- Retain the accession, sequence, method version and full prediction payload for
  each case. A matching mammalian gene symbol is only a lookup lead.
- Build any later ARGO-MAMMAL expansion around these horse-anchored cases and
  verified counterparts, supplementing it only where predictions are available.
  Group orthologs and paralogs by family rather than counting them as independent
  discoveries.

The selection cannot estimate whole-horse-proteome accuracy. Familiar cases may
also be in the model's training corpus, so results will describe performance on
this targeted cohort rather than unseen-sequence generalization.

## What to measure

- **Biological correctness of emitted claims:** COR/CNN/LSP/UNC/PLI/NPI/REP for
  actual GO predictions, with error mechanism recorded separately. A pseudoenzyme
  mechanism does not by itself determine whether a particular error is PLI or NPI.
- **Failure to avoid a specific known error:** fraction of eligible challenge
  proteins on which the model actually emits the predeclared false activity.
  Record whether it supplied any relevant output. Omission avoids a false positive
  but does not demonstrate recovery of the correct function.
- **Retention of useful function:** supported regulator, binding, scaffold,
  localization and process claims, and performance on active positive controls.
  This prevents “predict no catalysis” from winning by abstention.
- **Narrative correctness and completeness, separately from GO:** split function
  text into atomic claims; score conserved biology and taxon-specific claims
  individually. Rat PTK7 motivates this explicitly. A domain-containing name is
  not equivalent to an assertion of the corresponding enzyme activity.
- **Method-specific comparisons:** compare the same claim and target across
  ProtNLM2, ARBA, InterPro2GO and other available outputs. Report PAINT/IBA and
  curated ISO/ISS transfers separately. Keep current and historical annotation
  snapshots distinct. Agreement with an electronic method is not validation.

Do not collapse these into a single pooled accuracy score. Report denominators
by protein, family, claim type and evidence sufficiency; report novelty/annotation
overlap separately from biological correctness and training exposure.

## Practical sequence of work

- [x] Check the public accession list and inspect actual mammalian outputs.
- [x] Verify live provenance for the 12 candidate annotation pairs above.
- [x] Select 40 distinct horse genes with informative functional predictions and preserve their current sequences.
- [ ] Review the selected horse claims using primary studies and reproducible
  sequence/structure analyses, with verified mammalian counterparts where useful.
- [x] Preserve served predictions for all selected horse accessions.
- [ ] Establish prediction-time sequence identity and orthology before projecting
  cases into a broader mammalian benchmark.
- [ ] Obtain a second biological adjudication without showing predictor identity or
  the old AIGR action; resolve disagreements and preserve uncertainty.
- [ ] Score and publish cohort-specific results. The public API evaluates released,
  post-processed **ProtNLM2 plus Evidencer** output. Comparing the raw model with its
  filtering/corroboration requires additional outputs and cannot be inferred here.

Use the [function-prediction review skill](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/review-function-prediction/SKILL.md)
for the evidence standard. OpenScientist investigations can be substantive evidence
when their analyses support the claim; trace important results to artifacts and
sources and do not count the synthesis and its sources as independent replications.
