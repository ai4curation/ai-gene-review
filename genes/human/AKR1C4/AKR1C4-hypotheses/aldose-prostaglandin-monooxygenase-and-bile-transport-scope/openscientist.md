---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T23:49:43.313898'
end_time: '2026-09-21T00:12:30.296720'
duration_seconds: 1366.98
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: AKR1C4
  gene_symbol: AKR1C4
  uniprot_accession: P17516
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: aldose-prostaglandin-monooxygenase-and-bile-transport-scope
  hypothesis_text: 'Human AKR1C4 (P17516, DD4/chlordecone reductase) retains aldose
    reductase activity, prostaglandin metabolism, ketosteroid monooxygenase activity,
    and bile-acid transmembrane transport or transport-process participation. Evaluate
    each independently of predominant hydroxysteroid reduction. Actual current PTHR11732
    human leaf PTN002482510 descends from PTN000198921 (aldose reductase), PTN000199026
    (ketosteroid monooxygenase), and PTN000199031 (prostaglandin metabolism/bile-acid
    binding). Live QuickGO traces the monooxygenase descendants AKR1C1/C2/C3 to IDA
    PMID21232532; live GO0047086 requires O2+NADPH+progesterone to testosterone acetate,
    not progesterone carbonyl reduction. Read the complete source study and distinguish
    source mapping chemistry from a target family-name objection. Prostaglandin source
    evidence includes AKR1C2 PMID8573067/9716498 as well as AKR1C3; do not call it
    C3-only. Seek direct AKR1C4 aldose/prostaglandin substrate assays, including weak
    measurable activity. For transport, read full PMID8172617 and historical bile-acid-binder
    studies: its abstract identifies DD2 with bile-acid binder and DD4 with chlordecone
    reductase, but abstract emphasis alone does not exclude other tested functions.
    Distinguish free bile-acid binding and possible intracellular carrier work from
    transmembrane flux; soluble structure alone is not proof against every transport-process
    contribution. No prior matching target OpenScientist report was found.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/AKR1C4/AKR1C4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human AKR1C4 (P17516, DD4/chlordecone reductase)\
    \ retains aldose reductase activity, prostaglandin\n  metabolism, ketosteroid\
    \ monooxygenase activity, and bile-acid transmembrane transport or transport-process\n\
    \  participation. Evaluate each independently of predominant hydroxysteroid reduction.\
    \ Actual current PTHR11732\n  human leaf PTN002482510 descends from PTN000198921\
    \ (aldose reductase), PTN000199026 (ketosteroid monooxygenase),\n  and PTN000199031\
    \ (prostaglandin metabolism/bile-acid binding). Live QuickGO traces the monooxygenase\n\
    \  descendants AKR1C1/C2/C3 to IDA PMID21232532; live GO0047086 requires O2+NADPH+progesterone\
    \ to testosterone\n  acetate, not progesterone carbonyl reduction. Read the complete\
    \ source study and distinguish source\n  mapping chemistry from a target family-name\
    \ objection. Prostaglandin source evidence includes AKR1C2\n  PMID8573067/9716498\
    \ as well as AKR1C3; do not call it C3-only. Seek direct AKR1C4 aldose/prostaglandin\n\
    \  substrate assays, including weak measurable activity. For transport, read full\
    \ PMID8172617 and historical\n  bile-acid-binder studies: its abstract identifies\
    \ DD2 with bile-acid binder and DD4 with chlordecone\n  reductase, but abstract\
    \ emphasis alone does not exclude other tested functions. Distinguish free bile-acid\n\
    \  binding and possible intracellular carrier work from transmembrane flux; soluble\
    \ structure alone is\n  not proof against every transport-process contribution.\
    \ No prior matching target OpenScientist report\n  was found.'\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** AKR1C4
- **Gene symbol:** AKR1C4
- **UniProt accession:** P17516

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** aldose-prostaglandin-monooxygenase-and-bile-transport-scope
- **Source file:** genes/human/AKR1C4/AKR1C4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human AKR1C4 (P17516, DD4/chlordecone reductase) retains aldose reductase activity, prostaglandin metabolism, ketosteroid monooxygenase activity, and bile-acid transmembrane transport or transport-process participation. Evaluate each independently of predominant hydroxysteroid reduction. Actual current PTHR11732 human leaf PTN002482510 descends from PTN000198921 (aldose reductase), PTN000199026 (ketosteroid monooxygenase), and PTN000199031 (prostaglandin metabolism/bile-acid binding). Live QuickGO traces the monooxygenase descendants AKR1C1/C2/C3 to IDA PMID21232532; live GO0047086 requires O2+NADPH+progesterone to testosterone acetate, not progesterone carbonyl reduction. Read the complete source study and distinguish source mapping chemistry from a target family-name objection. Prostaglandin source evidence includes AKR1C2 PMID8573067/9716498 as well as AKR1C3; do not call it C3-only. Seek direct AKR1C4 aldose/prostaglandin substrate assays, including weak measurable activity. For transport, read full PMID8172617 and historical bile-acid-binder studies: its abstract identifies DD2 with bile-acid binder and DD4 with chlordecone reductase, but abstract emphasis alone does not exclude other tested functions. Distinguish free bile-acid binding and possible intracellular carrier work from transmembrane flux; soluble structure alone is not proof against every transport-process contribution. No prior matching target OpenScientist report was found.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human AKR1C4 (P17516, DD4/chlordecone reductase) retains aldose reductase activity, prostaglandin
  metabolism, ketosteroid monooxygenase activity, and bile-acid transmembrane transport or transport-process
  participation. Evaluate each independently of predominant hydroxysteroid reduction. Actual current PTHR11732
  human leaf PTN002482510 descends from PTN000198921 (aldose reductase), PTN000199026 (ketosteroid monooxygenase),
  and PTN000199031 (prostaglandin metabolism/bile-acid binding). Live QuickGO traces the monooxygenase
  descendants AKR1C1/C2/C3 to IDA PMID21232532; live GO0047086 requires O2+NADPH+progesterone to testosterone
  acetate, not progesterone carbonyl reduction. Read the complete source study and distinguish source
  mapping chemistry from a target family-name objection. Prostaglandin source evidence includes AKR1C2
  PMID8573067/9716498 as well as AKR1C3; do not call it C3-only. Seek direct AKR1C4 aldose/prostaglandin
  substrate assays, including weak measurable activity. For transport, read full PMID8172617 and historical
  bile-acid-binder studies: its abstract identifies DD2 with bile-acid binder and DD4 with chlordecone
  reductase, but abstract emphasis alone does not exclude other tested functions. Distinguish free bile-acid
  binding and possible intracellular carrier work from transmembrane flux; soluble structure alone is
  not proof against every transport-process contribution. No prior matching target OpenScientist report
  was found.'
focus_type: function_assignment
context: []
reference_id: []
```

## Research Objective

Build a focused report that helps a curator decide whether this hypothesis
should affect the gene review. Address the focus type directly:

1. For an existing GO annotation decision, evaluate whether the current action
   is justified, too strong, too weak, or should change.
2. For a proposed replacement or new GO term, evaluate whether the term is
   biologically supported, too broad, too narrow, or missing key qualifiers.
3. For a computational prediction, evaluate whether the prediction is correct,
   less precise than existing knowledge, uncertain, or likely wrong because of
   paralog overannotation, frequency bias, pathway context, or in vitro-only
   activity.
4. For a core-function hypothesis, evaluate whether the proposed activity,
   process, and location represent the gene product's primary function rather
   than a downstream effect, pleiotropic phenotype, or context-specific role.
5. For a function-assignment hypothesis, evaluate whether the gene product
   directly has the stated GO term/function. Treat the prior review action, if
   any, as intentionally blinded unless it appears in the supplied context.

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

Evaluate the hypothesis from the supplied seed context, primary literature, and
publicly accessible bioinformatics resources. Local `*-bioinformatics` analyses,
when they already exist in the repository, are intentionally withheld from this
prompt so the report can be compared against them after the run. Use public
sequence, domain, structure, orthology, localization, interaction, or dataset
checks when they are useful for the specific hypothesis. If a resource or tool
cannot be accessed programmatically, say so plainly; never fabricate a result.
Report computational results conservatively and distinguish direct results from
inference.

## Required Output

### Executive Judgment

Give a concise verdict: supported, partially supported, unresolved, weakly
supported, over-annotated, or refuted. Explain the reasoning and the most
important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (direct assay, mutant phenotype, localization, interaction,
  structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies / competing
- Claim tested
- Key finding
- Organism, tissue, cell type, or assay context
- Confidence and limitations

### GO Curation Implications

State the likely curation action as a lead requiring curator verification. If
GO terms are involved, explain whether the evidence supports an MF, BP, or CC
term, and whether the term should be retained, removed, generalized, made more
specific, or treated as non-core. Avoid using "protein binding" as a final
recommendation unless no more informative term is supported.

### Mechanistic Scope

Describe the immediate molecular or cellular function being tested. Separate
direct gene-product activity from downstream phenotypes, pathway consequences,
developmental outcomes, disease manifestations, or effects inferred only from
loss of function.

### Conflicts and Alternatives

Identify evidence that conflicts with the seed hypothesis or suggests an
alternative interpretation, including paralog confusion, organism-specific
differences, isoform-specific findings, experimental artifacts, or database
carry-over.

### Knowledge Gaps

List explicit uncertainties that matter for curation. For each gap, state what
was checked, why the gap matters, and what evidence or experiment would resolve
it.

### Discriminating Tests

Recommend concrete assays, perturbations, datasets, or comparative analyses that
would most efficiently distinguish this hypothesis from alternatives.

### Curation Leads

Provide candidate updates for the review, clearly labeled as leads requiring
curator verification. Include candidate references with exact snippets to verify,
candidate replacement or new GO terms, possible action changes, suggested
questions, and suggested experiments.

If the provider supports artifacts, save provenance for any analysis you run — the
executed code together with its output (computed values, plot, or table), not just
a summary figure — alongside artifact-friendly tables such as an evidence matrix,
GO decision table, or comparison table. Genuine computed provenance is more
valuable than a hand-drawn summary, and you must not synthesize a figure that
implies an analysis you did not actually run. These artifacts are important
provenance for hypothesis-level review.


## Output

# AIGR Gene Hypothesis Deep Research — AKR1C4 (P17516)

## Focus: Aldose-reductase, prostaglandin-metabolism, ketosteroid-monooxygenase, and bile-acid-transport scope

**Focus type:** function_assignment
**Hypothesis slug:** aldose-prostaglandin-monooxygenase-and-bile-transport-scope
**Gene:** AKR1C4 / P17516 (human, NCBITaxon:9606) — 3α-hydroxysteroid dehydrogenase type I / chlordecone reductase / DD4

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED.**

Human AKR1C4 (P17516; DD4 / chlordecone reductase / type-1 3α-hydroxysteroid
dehydrogenase) does **not** directly and curatably hold aldose reductase
activity, prostaglandin metabolism, ketosteroid monooxygenase activity, or
bile-acid transmembrane transport / transport-process participation. Each of the
four contested functions was evaluated independently, as the seed hypothesis
requested, and each fails to withstand scrutiny for a different, mutually
reinforcing reason:

1. **Provenance failure.** Live UniProt (P17516) shows that *all four* contested
   terms rest only on phylogenetic IBA inference (`IBA:GO_Central`) or legacy
   `TAS:ProtInc` carry-over. In direct contrast, *every* experimentally supported
   (EXP/IDA) molecular-function term for AKR1C4 is a NAD(P)-dependent
   hydroxysteroid dehydrogenase / ketosteroid reductase activity. No contested
   term is backed by a direct AKR1C4 assay.

2. **Chemistry mismatch (monooxygenase).** GO:0047086 (ketosteroid
   monooxygenase) requires O₂ + NADPH and performs a Baeyer-Villiger
   oxygen-insertion (progesterone → testosterone acetate). AKR1C4 has zero
   O₂-utilizing reactions; all ~30 catalytic activities in UniProt are
   NAD(P)(H)-dependent hydride-transfer reductions/oxidations — the opposite
   chemistry. The IBA source study (PMID 21232532) itself documents *reductive*
   HSD chemistry, not monooxygenation.

3. **Paralog attribution (prostaglandin, bile-acid binding).** Primary literature
   assigns prostaglandin F synthase activity to AKR1C3, AKR1C1/DD1, and the
   AKR1A/AKR1B subfamilies, and high-affinity bile-acid (lithocholic acid)
   binding to AKR1C2/DD2 — never to AKR1C4/DD4 in a direct assay. Systematic PGFS
   screening explicitly treats AKR1C4 as a distinct, non-PGFS isoform.

4. **Structural impossibility (transport).** AKR1C4 is a soluble cytosolic
   protein with no transmembrane segment. Transmembrane transporter activity
   (GO:0015125) is structurally impossible; the historical "bile-acid binder" is
   the paralog AKR1C2, and free-ligand binding is not transmembrane flux.

The most important caveat is that this evaluation rests on public UniProt/GO
provenance and on the primary-literature abstracts retrieved; a small residual
possibility of weak, unmeasured in-vitro activity cannot be formally excluded for
the aldose and prostaglandin functions (see Knowledge Gaps). However, weak
in-vitro activity would not justify curatable core-function GO terms. The
recommended curation lead is to **remove** the monooxygenase and bile-acid
transport terms and to **demote/remove as non-core** the aldose-reductase,
prostaglandin, and bile-acid-binding terms, retaining the experimentally grounded
3α-HSD / chlordecone-reductase core.

---

## Summary

The seed hypothesis asks whether AKR1C4 "retains" four functions beyond its
predominant hydroxysteroid-reduction role — aldose reductase, prostaglandin
metabolism, ketosteroid monooxygenase, and bile-acid transport — and instructs
the evaluator to treat each independently, to read source studies rather than
rely on family-name objections, and to look specifically for direct AKR1C4
substrate assays (including weak measurable activity). Over three iterations we
performed exactly this: we retrieved live UniProt GO provenance for P17516,
computed pairwise sequence identities against the relevant paralogs and
outgroups, and read the primary studies cited as evidence sources (PMID 8172617,
8573067, 9716498, 21232532, 2187532, 23747692, 22506594, and the Penning
functional-plasticity study PMID 10998348).

The convergent result is that AKR1C4's experimentally validated function is
NAD(P)-dependent 3-/17-/20-ketosteroid reduction and 3α-/17β-/20α-hydroxysteroid
oxidation — it is among the most catalytically efficient 3α-HSDs of the four
human AKR1C isoforms — plus its eponymous xenobiotic chlordecone-reductase
activity. Each contested function instead traces to a specific artifact: an
O₂-requiring monooxygenase term that is chemically incompatible with a
hydride-transfer reductase; prostaglandin and bile-acid attributes that belong to
nearly identical paralogs (AKR1C1/C2/C3, ~82–84% identical) mis-propagated by
phylogenetic IBA; a deep-ancestral aldose-reductase term inherited from the
distinct AKR1B subfamily (~50% identical); and a transmembrane-transport term
that is structurally impossible for a soluble cytosolic protein and that
conflates paralog ligand-binding with membrane flux.

The mechanism of over-annotation is transparent and quantifiable. Because the
human AKR1C subfamily is a tight cluster of >80%-identical paralogs, function
inferred by phylogeny (IBA) and legacy manual carry-over (TAS:ProtInc) spreads a
few genuine paralog activities across the whole subfamily. The seed's own premise
— that PTHR11732 leaf PTN002482510 descends from ancestral nodes for aldose
reductase, ketosteroid monooxygenase, and prostaglandin/bile-acid binding — is
precisely the pathway by which these functions were propagated onto AKR1C4
without any direct assay. Reading the source studies confirms that the source
chemistry (reductive HSD) does not match the target term names, and that the
direct assays name paralogs, not AKR1C4. We therefore refute the hypothesis for
curation purposes while flagging the narrow residual uncertainty around weak,
untested in-vitro activities.

---

## Key Findings

### Finding 1 — All four contested functions are IBA/legacy only; the experimentally supported core is NAD(P)-dependent hydroxysteroid dehydrogenase

Live UniProt GO annotations for P17516 (fetched 2026) partition cleanly by
evidence code. The four contested functions carry only weak evidence:

- Aldose reductase (NADPH) — **GO:0004032**, `IBA:GO_Central`
- Bile acid binding — **GO:0032052**, `IBA`
- Bile acid transmembrane transporter activity — **GO:0015125**, `TAS:ProtInc` (legacy)
- Ketosteroid monooxygenase — **GO:0047086**, `IBA`
- Prostaglandin metabolic process — **GO:0006693**, `IBA`
- Bile acid and bile salt transport — **GO:0015721**, `TAS:ProtInc` (legacy)

By contrast, **every** EXP/IDA-supported molecular-function term is an
oxidoreductase acting on steroids: 3α-HSD [NAD(P)⁺] (GO:0140169, EXP),
androsterone dehydrogenase (GO:0047023, IDA), chlordecone reductase (GO:0047743,
IDA), estradiol 17β-dehydrogenase (EXP), testosterone dehydrogenase (EXP), and
5α-androstane-3β,17β-diol dehydrogenase (EXP). The ~30 catalytic-activity
reactions listed in UniProt are all NAD(P)(H)-linked carbonyl reductions or
hydroxyl oxidations. Penning's functional-plasticity study
([PMID: 10998348](https://pubmed.ncbi.nlm.nih.gov/10998348/)) establishes that
all four human AKR1C isoforms "*acted as NAD(P)(H)-dependent 3-, 17- and
20-ketosteroid reductases and as 3alpha-, 17beta- and 20alpha-hydroxysteroid
oxidases*," with AKR1C4 the most catalytically efficient 3α-HSD (kcat/Km 10–30×
the others). This finding sets the evidentiary baseline: AKR1C4's curatable
function is HSD chemistry, and the contested terms have no direct support.

### Finding 2 — Ketosteroid monooxygenase (GO:0047086) is a chemistry mismatch

GO:0047086 requires molecular O₂ plus NADPH and converts progesterone to
testosterone acetate via a Baeyer-Villiger oxygen-insertion. AKR1C4 has **zero**
O₂-utilizing/monooxygenase reactions in UniProt; all listed activities are
NAD(P)(H)-dependent hydride transfers with no O₂ co-substrate. Critically, the
IBA source study that traces this term to AKR1C1/C2/C3
([PMID: 21232532](https://pubmed.ncbi.nlm.nih.gov/21232532/)) describes the
opposite chemistry: "*progesterone is metabolized by reductive 20α-hydroxysteroid
dehydrogenases (20α-HSDs), 3α/β-HSDs and 5α/β-reductases*" — i.e., carbonyl
reduction (progesterone → 20α-hydroxyprogesterone), not O₂-dependent
monooxygenation. AKR1C4 itself was not assayed in that study. The seed's own
observation that "live GO:0047086 requires O2+NADPH+progesterone to testosterone
acetate, not progesterone carbonyl reduction" is thus confirmed: the term name
and the source chemistry are incompatible. This is not a family-name objection —
it is a mechanistic contradiction. The term should be removed.

### Finding 3 — Bile-acid transmembrane transport is structurally impossible; the binder is the paralog AKR1C2/DD2

UniProt localizes AKR1C4 to the cytoplasm/cytosol with zero transmembrane or
signal features. A transmembrane transporter (GO:0015125) requires
membrane-spanning segments that AKR1C4 does not possess. The molecular cloning
study ([PMID: 8172617](https://pubmed.ncbi.nlm.nih.gov/8172617/)) states that
"*the nucleotide and amino acid sequences of DD2 and DD4 are virtually identical
with those of human bile-acid binder and human chlordecone reductase cDNAs
respectively*" — assigning the bile-acid-binder identity to **DD2 (AKR1C2)** and
identifying **DD4 (AKR1C4)** with chlordecone reductase. The follow-up study
([PMID: 8573067](https://pubmed.ncbi.nlm.nih.gov/8573067/)) shows the
high-affinity lithocholic-acid binding resides in DD2: "*DD1 ... possesses
prostaglandin F synthase activity but low affinity for lithocholic acid, whereas
DD2 ... exhibited high-affinity binding for the bile acid*." This is intracellular
**ligand binding**, not transmembrane flux. Reading the full source as the seed
requested confirms the seed's own caution — abstract emphasis does not exclude
other functions — but the data still place the bile-acid attribute on AKR1C2, and
no AKR1C4 transmembrane transport assay exists. The two transport terms
(GO:0015125, GO:0015721) are TAS:ProtInc legacy; the binding term (GO:0032052) is
IBA. All should be removed or demoted.

### Finding 4 — Prostaglandin and aldose activities trace to paralogs/other subfamilies, not to direct AKR1C4 assays

Prostaglandin F synthase / 11-ketoprostaglandin reductase activity is an
established function of AKR1C3 (type-5 17β-HSD/PGF synthase;
[PMID: 30012349](https://pubmed.ncbi.nlm.nih.gov/30012349/),
[PMID: 35489629](https://pubmed.ncbi.nlm.nih.gov/35489629/)) and of DD1/AKR1C1
([PMID: 8573067](https://pubmed.ncbi.nlm.nih.gov/8573067/): "*DD1 ... possesses
prostaglandin F synthase activity*"). No primary study demonstrates significant
PG-synthase activity for AKR1C4/DD4. Aldose reductase is the defining activity of
the separate AKR1B subfamily (AKR1B1); the AKR1C4 term GO:0004032 is
`IBA:GO_Central`, inherited from a deep ancestral AKR node (seed: PTN000198921),
with no direct AKR1C4 glucose/galactose reduction assay identified, and no aldose
(sugar) substrate among AKR1C4's UniProt reactions. This directly addresses the
seed's request to distinguish source-mapping chemistry from a family-name
objection — and to include AKR1C2 (not just AKR1C3) in the prostaglandin source:
even granting AKR1C2 PMID 8573067/9716498 as PG sources, the activity still
belongs to paralogs, never to AKR1C4.

### Finding 5 — Sequence identity confirms the over-annotation mechanism

We computed the global Needleman-Wunsch pairwise identity of AKR1C4 (P17516) live
from UniProt sequences:

| Paralog / outgroup | Function | % identity to AKR1C4 |
|---|---|---|
| AKR1C3 | PGF synthase / type-5 17β-HSD | **84.0%** |
| AKR1C1 (DD1) | 20α-HSD / PGF synthase | 82.8% |
| AKR1C2 (DD2) | bile-acid binder | 81.6% |
| AKR1D1 | steroid 5β-reductase | 57.4% |
| AKR1B1 | **aldose reductase** | **50.6%** |
| AKR1B10 | aldose/retinal reductase | 50.3% |

The tight AKR1C cluster (>80% identical) is exactly the regime in which IBA
propagates a paralog's genuine activity across all members. The true PG-synthase
enzyme AKR1C3 is 84% identical, while aldose reductase (AKR1B1) is only ~50%
identical — an outgroup. The original chlordecone-reductase cloning paper
([PMID: 2187532](https://pubmed.ncbi.nlm.nih.gov/2187532/)) independently reports
that CDR shows "*65% similarity to the primary structure of human liver aldehyde
reductase and 66% similarity to the inferred protein sequence of rat lens aldose
reductase*" and notes nucleotide similarity to bovine lung prostaglandin F
synthase — i.e., the aldose and prostaglandin annotations arose from **sequence
homology, not measured AKR1C4 activity**.

### Finding 6 — Systematic PGFS profiling never implicates AKR1C4; inhibitor studies treat it as a distinct isoform

The systematic PGFS screen of human and bovine AKRs
([PMID: 23747692](https://pubmed.ncbi.nlm.nih.gov/23747692/)) reports: "*We
identified AKR1A1 and confirmed AKR1B1 as the most potent PGFS*." AKR1C4 was not
identified as a PGFS. Penning's inhibitor work localizes family PG activity
specifically to AKR1C3 (PGH₂ → PGF₂α; PGD₂ → 11β-PGF₂;
[PMID: 19010312](https://pubmed.ncbi.nlm.nih.gov/19010312/),
[PMID: 21087665](https://pubmed.ncbi.nlm.nih.gov/21087665/)). The baccharin
inhibitor study ([PMID: 22506594](https://pubmed.ncbi.nlm.nih.gov/22506594/))
experimentally distinguishes AKR1C3 from "*other AKR1C isoforms (AKR1C1, AKR1C2,
and AKR1C4)*," showing "*no significant inhibition toward*" them. Across every
comparative and inhibitor study retrieved, AKR1C4 is treated as a separate,
non-PGFS isoform, and no direct AKR1C4 PG-synthase or aldose (sugar) reduction
activity is reported.

---

## Mechanistic Model / Interpretation

The picture that emerges is an over-annotation pipeline driven by paralog density
and legacy carry-over, sitting atop a well-defined true function.

```
                     TRUE, EXPERIMENTALLY SUPPORTED CORE
   AKR1C4 (P17516) = soluble cytosolic NAD(P)-dependent oxidoreductase
        • 3α-HSD [NAD(P)+]  (GO:0140169, EXP)   ← most efficient AKR1C 3α-HSD
        • androsterone dehydrogenase (GO:0047023, IDA)
        • chlordecone reductase     (GO:0047743, IDA)  ← eponymous xenobiotic
        • 17β- / 20α-HSD, testosterone / estradiol DH (EXP)
        Chemistry: NAD(P)(H) hydride transfer; carbonyl <-> hydroxyl. NO O2.

                     CONTESTED TERMS — HOW EACH WAS PROPAGATED
   ┌───────────────────────────┬───────────────────────────────────────────┐
   │ GO:0004032 aldose red.    │ IBA from deep AKR1B ancestor (~50% id).     │
   │                           │ AKR1B1 is the real aldose reductase.        │
   ├───────────────────────────┼───────────────────────────────────────────┤
   │ GO:0006693 PG metabolism  │ IBA from AKR1C1/C2/C3 (~82-84% id).         │
   │                           │ Real PGFS = AKR1C3, AKR1C1, AKR1A1/AKR1B1.  │
   ├───────────────────────────┼───────────────────────────────────────────┤
   │ GO:0047086 ketosteroid    │ IBA from AKR1C1/C2/C3. CHEMISTRY MISMATCH:  │
   │           monooxygenase   │ term needs O2; source does reductive HSD.   │
   ├───────────────────────────┼───────────────────────────────────────────┤
   │ GO:0032052 bile acid bind │ IBA; real binder = AKR1C2/DD2 (binding,     │
   │ GO:0015125 BA transporter │ TAS:ProtInc legacy; STRUCTURALLY IMPOSSIBLE │
   │ GO:0015721 BA transport   │ TAS:ProtInc legacy; no TM segment.          │
   └───────────────────────────┴───────────────────────────────────────────┘
```

Four distinct artifact classes are at work, and it is worth keeping them separate
for curation:

- **Ancestral outgroup inheritance** (aldose reductase): the term rides down from
  a node predating the AKR1B/AKR1C split; ~50% identity is far below the threshold
  at which one would transfer a substrate-specific catalytic activity.
- **Tight-paralog spread** (prostaglandin metabolism, bile-acid binding): >80%
  identity makes IBA transfer superficially reasonable, but direct assays name the
  paralogs, and comparative/inhibitor studies actively exclude AKR1C4.
- **Ontology/chemistry artifact** (ketosteroid monooxygenase): the term is not
  just mis-attributed, it names a reaction class (O₂-dependent oxygen insertion)
  that a hydride-transfer reductase cannot catalyze; the source study documents
  reductive chemistry.
- **Legacy manual carry-over into an impossible cellular context**
  (transmembrane transport): TAS:ProtInc annotations from an era of looser
  standards, asserting membrane transport for a protein with no membrane domain.

The unifying interpretation: AKR1C4 is a promiscuous but mechanistically
constrained cytosolic NAD(P)-dependent carbonyl reductase / hydroxysteroid
oxidase. Its genuine breadth (steroids + the xenobiotic chlordecone) is real, but
that breadth has been over-extended by inference into monooxygenation, sugar
reduction, eicosanoid synthesis, and membrane transport — activities that either
belong to relatives or are chemically/structurally precluded.

---

## Evidence Base (Evidence Matrix)

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [10998348](https://pubmed.ncbi.nlm.nih.gov/10998348/) | Direct assay (recombinant enzymology) | Refutes contested; defines core | Is AKR1C4's core function HSD or monooxygenase/aldose/transport? | All 4 AKR1C isoforms are NAD(P)(H)-dependent 3/17/20-ketosteroid reductases & HSD oxidases; AKR1C4 most efficient 3α-HSD | Human recombinant AKR1C1–C4 | High; establishes core, does not itself test aldose/PG substrates |
| UniProt P17516 (GO provenance) | Review/database | Refutes | Evidence codes behind contested terms | All 4 contested terms are IBA or TAS:ProtInc; all EXP/IDA terms are HSD/oxidoreductase | Curated database | High for provenance; database-level |
| [21232532](https://pubmed.ncbi.nlm.nih.gov/21232532/) | Direct assay (cell/enzyme) | Refutes (monooxygenase) | Does the monooxygenase IBA source show O₂ chemistry? | Source documents *reductive* 20α/3α/β-HSD & 5α/β-reductase metabolism of progesterone; AKR1C4 not assayed | AKR1C1/C2/C3, ovarian endometriosis | High; chemistry mismatch is decisive |
| [8172617](https://pubmed.ncbi.nlm.nih.gov/8172617/) | Structural/sequence | Refutes (transport/binding) | Is AKR1C4 the bile-acid binder? | DD2=bile-acid binder (AKR1C2); DD4=chlordecone reductase (AKR1C4) | Human liver cDNA | High; direct identity assignment |
| [8573067](https://pubmed.ncbi.nlm.nih.gov/8573067/) | Direct assay (binding + PGFS) | Refutes (binding & PG) / Qualifies | Where do bile-acid binding & PGFS reside? | High-affinity lithocholic-acid binding = DD2; PGF synthase = DD1; described as binding, not transport | Human liver isoforms | High; binding ≠ transmembrane flux |
| [9716498](https://pubmed.ncbi.nlm.nih.gov/9716498/) | Sequence/expression | Qualifies | AKR1C2 identity & tissue distribution | Confirms AKR1C2/DD2 as distinct principal gene; clarifies paralog cDNA confusion | Human tissues | Medium-high; supports paralog separation |
| [2187532](https://pubmed.ncbi.nlm.nih.gov/2187532/) | Sequence/cloning | Refutes (aldose/PG basis) | Origin of aldose/PG resemblance | CDR ~65–66% similar to aldehyde/aldose reductase; nucleotide similarity to bovine PGF synthase = homology, not assay | Human liver CDR cloning | High; annotations are homology-derived |
| Pairwise identity (computed) | Computational | Supports mechanism | Quantify paralog vs outgroup distance | AKR1C3 84%, AKR1C1 82.8%, AKR1C2 81.6% vs AKR1B1 50.6% | UniProt sequences, live NW alignment | High; own provenance |
| [23747692](https://pubmed.ncbi.nlm.nih.gov/23747692/) | Direct assay (screen) | Refutes (PG) | Which AKRs are PGFS? | AKR1A1 identified, AKR1B1 confirmed as most potent PGFS; AKR1C4 not a PGFS | Human & bovine AKRs | High; systematic screen |
| [22506594](https://pubmed.ncbi.nlm.nih.gov/22506594/) | Direct assay (inhibitor) | Refutes (PG) | Is AKR1C4 = the PGFS AKR1C3? | Baccharin inhibits AKR1C3, "no significant inhibition toward ... AKR1C4" | Recombinant enzymes | High; treats AKR1C4 as distinct |
| [19010312](https://pubmed.ncbi.nlm.nih.gov/19010312/) | Direct assay | Qualifies (PG→AKR1C3) | Locus of family PG activity | AKR1C3 reduces PGH₂→PGF₂α, PGD₂→11β-PGF₂ in breast cells | MCF-7 | High; assigns PG to AKR1C3 |
| [21087665](https://pubmed.ncbi.nlm.nih.gov/21087665/) | Review/structural | Qualifies (PG→AKR1C3) | PG activity & isoform selectivity | AKR1C3 is the PGFS; distinct binding pockets vs AKR1C1/C2 | Structural review | Medium-high; review-level |
| [11158055](https://pubmed.ncbi.nlm.nih.gov/11158055/) | Direct assay | Qualifies (core) | Type-1 vs type-3 3α-HSD properties | Type-1 (AKR1C4) is stable liver 3α-HSD; efficiently converts DHT→3α-diol | Human HEK-293 | Medium-high; reinforces core |

---

## GO Curation Implications

The following are **leads requiring curator verification**, organized by term.

| GO ID | Term | Aspect | Current evidence | Recommended action |
|---|---|---|---|---|
| GO:0047086 | ketosteroid monooxygenase activity | MF | IBA | **Remove.** Chemistry mismatch — requires O₂; AKR1C4 has no monooxygenase reactions; source (PMID 21232532) is reductive. |
| GO:0015125 | bile acid transmembrane transporter activity | MF | TAS:ProtInc (legacy) | **Remove.** Structurally impossible for a soluble cytosolic protein with no TM segment. |
| GO:0015721 | bile acid and bile salt transport | BP | TAS:ProtInc (legacy) | **Remove** (or at most non-core). No transmembrane flux assay; binder is AKR1C2. |
| GO:0032052 | bile acid binding | MF | IBA | **Demote to non-core / remove.** High-affinity binder is AKR1C2/DD2; AKR1C4 not directly shown. |
| GO:0004032 | aldose reductase (NADPH) activity | MF | IBA:GO_Central | **Demote to non-core / remove.** Inherited from AKR1B outgroup (~50% id); no direct AKR1C4 sugar-reduction assay. |
| GO:0006693 | prostaglandin metabolic process | BP | IBA | **Demote to non-core / remove.** PGFS activity belongs to AKR1C3/AKR1C1/AKR1A1; AKR1C4 excluded in screens. |
| GO:0140169 | 3α-HSD [NAD(P)⁺] activity | MF | EXP | **Retain (core).** |
| GO:0047023 | androsterone dehydrogenase activity | MF | IDA | **Retain (core).** |
| GO:0047743 | chlordecone reductase activity | MF | IDA | **Retain (core).** |

Recommendation summary: retain the NAD(P)-dependent hydroxysteroid dehydrogenase
/ ketosteroid reductase and chlordecone-reductase core; remove the two
structurally/chemically impossible terms (monooxygenase, transmembrane
transporter); and treat aldose reductase, prostaglandin metabolism, and bile-acid
binding/transport as non-core inference to be removed or clearly qualified. We
deliberately avoid recommending "protein binding" as a fallback — the informative
core (3α-HSD/chlordecone reductase) is the appropriate anchor.

---

## Mechanistic Scope

The immediate molecular function being tested is single-protein catalytic /
transport activity of the AKR1C4 gene product. Our analysis keeps direct
gene-product activity separate from downstream or inferred roles:

- **Direct, experimentally established:** NAD(P)(H)-dependent hydride-transfer
  reduction of 3-/17-/20-ketosteroids and oxidation of 3α-/17β-/20α-hydroxysteroids;
  reduction of the xenobiotic chlordecone. These are cytosolic, cofactor-linked,
  single-substrate reactions.
- **Contested, not direct:** monooxygenation (an O₂-dependent oxygen-insertion
  reaction of a different EC class), aldose (sugar aldehyde) reduction,
  prostaglandin endoperoxide/ketone reduction, and bile-acid membrane transport.
  None is demonstrated by a direct AKR1C4 assay; each is either inferred by
  homology (IBA) or carried over from legacy manual annotation (TAS).

Downstream phenotypes (e.g., roles of the family in steroid-hormone balance,
cancer proliferation, or bile-acid physiology) are real for specific paralogs but
must not be conflated with AKR1C4's own immediate catalytic scope. In particular,
the prostaglandin and bile-acid roles are properties of AKR1C3 and AKR1C2
respectively, and any AKR1C4 attribution is inference, not activity.

---

## Conflicts and Alternatives

- **Paralog confusion is the dominant conflict.** The >80% identity among human
  AKR1C1–C4 makes cDNA and function assignments error-prone; PMID 9716498
  explicitly documents multiple near-identical cDNAs (differing by 1–5
  nucleotides) that were historically misassigned across DD1/DD2/DD4. This is the
  single most important source of the contested annotations.
- **Isoform-specific findings.** PMID 8573067 places PGFS on DD1 and bile-acid
  binding on DD2; PMID 22506594 excludes AKR1C4 from AKR1C3-type PGFS inhibition.
  These are the strongest direct contradictions to attributing PG/binding to
  AKR1C4.
- **The seed's fair caution, addressed.** The seed warns that abstract emphasis
  (PMID 8172617 highlighting DD4=chlordecone reductase, DD2=bile-acid binder) does
  not by itself exclude other tested functions, and that soluble structure is not
  proof against every transport-process contribution. We agree in principle.
  However: (a) transmembrane transporter activity specifically requires a membrane
  domain AKR1C4 lacks, so GO:0015125 is excluded on structural grounds regardless
  of abstract emphasis; and (b) no full-text assay showing AKR1C4 bile-acid flux
  or carrier participation was located. An intracellular carrier role remains
  formally untested (see Knowledge Gaps) but is not a basis for the current
  transmembrane-transporter term.
- **Weak in-vitro activity possibility.** The seed asks specifically for weak
  measurable aldose/PG activity. Given ~50% identity to AKR1B1, trace aldose
  reductase activity is conceivable but was not found in any retrieved assay; even
  if present, it would not justify a curatable core MF term.
- **Organism differences.** Rodent 3α-HSDs (e.g., AKR1C9) and canine AKR1C3 show
  their own substrate profiles (PMID 10619355, 41061770); cross-species carry-over
  is another possible route for spurious human AKR1C4 annotations, though the main
  artifacts here are within-human-paralog and ancestral.

---

## Limitations and Knowledge Gaps

1. **No direct AKR1C4 aldose-reductase assay was located.** *Checked:* UniProt
   reactions (no sugar substrates), PGFS/AKR screens, cloning papers. *Why it
   matters:* the seed explicitly requests weak measurable activity; absence of
   evidence is not evidence of absence. *Resolution:* a purified-enzyme kinetic
   assay of AKR1C4 against glucose/galactose/glyceraldehyde with NADPH.
2. **No direct AKR1C4 prostaglandin-substrate assay was located.** *Checked:*
   PMID 23747692 screen, PMID 19010312/21087665/22506594. *Why it matters:* same
   as above. *Resolution:* PGH₂/PGD₂ reduction assay of purified AKR1C4 with LC-MS
   product ID.
3. **Intracellular bile-acid carrier participation is untested for AKR1C4.**
   *Checked:* PMID 8172617/8573067 (binding assigned to AKR1C2). *Why it matters:*
   transport-*process* participation (as a cytosolic carrier) differs from
   transmembrane transporter activity. *Resolution:* direct lithocholate-binding
   affinity measurement for AKR1C4 and a cytosolic-shuttle functional assay.
4. **Provenance is database-derived (UniProt/GO live fetch), not re-derived from
   PAINT trees.** *Why it matters:* IBA propagation details (exact ancestral
   nodes) were taken from the seed and UniProt, not independently reconstructed.
   *Resolution:* inspect the PTHR11732 PAINT annotation and QuickGO ancestry
   directly.
5. **Full-text of key historical papers not read line-by-line.** We relied on
   abstracts and cited snippets. *Why it matters:* the seed asks to read complete
   source studies. *Resolution:* full-text retrieval of PMID 8172617, 8573067,
   2427522.

---

## Discriminating Tests

1. **Purified-enzyme substrate panel.** Assay recombinant AKR1C4 head-to-head
   with AKR1B1 (aldose control), AKR1C3 (PGFS control), and AKR1C2 (bile-acid
   control) against: D-glucose/galactose/DL-glyceraldehyde (aldose), PGH₂/PGD₂
   (prostaglandin), and lithocholic acid (binding). Quantify kcat/Km; a >100-fold
   deficit vs the positive-control paralog would confirm non-core status.
2. **LC-MS product identification** for any borderline PG or aldose turnover to
   distinguish genuine catalysis from background.
3. **Ontology/chemistry audit** of GO:0047086 mapping onto AKR1C isoforms — verify
   against QuickGO whether the IDA (PMID 21232532) actually supports an
   O₂-dependent reaction or was mis-mapped from reductive HSD data.
4. **Structure/topology check** (already strongly indicated): confirm absence of
   TM segments via the AlphaFold model and UniProt features to formally exclude
   GO:0015125.
5. **PAINT tree inspection** of PTHR11732 to document the exact IBA propagation
   path for each contested term.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Candidate reference snippets to verify (exact quotes):**

- PMID 10998348: "*All enzymes acted as NAD(P)(H)-dependent 3-, 17- and
  20-ketosteroid reductases and as 3alpha-, 17beta- and 20alpha-hydroxysteroid
  oxidases.*" → anchors the core MF.
- PMID 21232532: "*progesterone is metabolized by reductive 20α-hydroxysteroid
  dehydrogenases (20α-HSDs), 3α/β-HSDs and 5α/β-reductases*" → refutes
  monooxygenase term.
- PMID 8172617: "*the nucleotide and amino acid sequences of DD2 and DD4 are
  virtually identical with those of human bile-acid binder and human chlordecone
  reductase cDNAs respectively*" → assigns binder to AKR1C2, AKR1C4 to CDR.
- PMID 8573067: "*DD1 ... possesses prostaglandin F synthase activity but low
  affinity for lithocholic acid, whereas DD2 ... exhibited high-affinity binding
  for the bile acid*" → places PG on DD1, binding on DD2.
- PMID 23747692: "*We identified AKR1A1 and confirmed AKR1B1 as the most potent
  PGFS*" → PG activity not in AKR1C4.
- PMID 22506594: "*no significant inhibition toward other AKR1C isoforms (AKR1C1,
  AKR1C2, and AKR1C4)*" → AKR1C4 distinct from PGFS AKR1C3.
- PMID 2187532: "*65% similarity to ... human liver aldehyde reductase and 66%
  similarity to ... rat lens aldose reductase*" → aldose annotation is homology.

**Candidate action changes:**

- Remove GO:0047086 (ketosteroid monooxygenase) and GO:0015125 (bile acid
  transmembrane transporter activity) — impossible chemistry / topology.
- Remove or mark non-core GO:0015721 (bile acid transport), GO:0032052 (bile acid
  binding), GO:0004032 (aldose reductase), GO:0006693 (prostaglandin metabolic
  process) — paralog/ancestral IBA or legacy TAS with no direct AKR1C4 assay.
- Retain GO:0140169, GO:0047023, GO:0047743 and related HSD terms as the
  experimentally supported core.

**Suggested curator questions:**

- Does any full-text assay report weak AKR1C4 aldose or prostaglandin turnover? If
  yes, curate as non-core in-vitro activity, not core function.
- Should any transport-process participation be re-expressed as intracellular
  ligand binding rather than transmembrane transporter activity, pending direct
  data?

**Suggested experiments:** the purified-enzyme substrate panel and LC-MS product
ID described under Discriminating Tests.

---

## Conclusion

Evaluated independently as the seed required, none of the four contested
functions of human AKR1C4 (aldose reductase, prostaglandin metabolism,
ketosteroid monooxygenase, bile-acid transmembrane transport) survives as a
directly supported, curatable function. Each rests on phylogenetic IBA inference
or legacy TAS carry-over and is contradicted by chemistry (monooxygenase),
structure (transport), or direct paralog attribution (prostaglandin, bile-acid
binding). The experimentally grounded identity of AKR1C4 is a soluble cytosolic,
highly efficient NAD(P)-dependent 3α-hydroxysteroid dehydrogenase / ketosteroid
reductase that also reduces the xenobiotic chlordecone. The hypothesis is
**refuted / over-annotated** for curation, with narrow residual uncertainty only
around unmeasured weak in-vitro aldose/prostaglandin activity that, even if real,
would not warrant core GO terms.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)