---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:37:20.885420'
end_time: '2026-08-31T19:57:27.618676'
duration_seconds: 1206.73
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: mus81
  gene_symbol: mus81
  uniprot_accession: P87231
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: free_text
  hypothesis_slug: mitochondrial-localization-and-mtdna-function
  hypothesis_text: Schizosaccharomyces pombe Mus81 has a genuine mitochondrial localization
    and direct role in mitochondrial DNA metabolism, rather than the mitochondrial
    HDA signal being a high-throughput localization artifact.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/mus81/mus81-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe Mus81 has a genuine\
    \ mitochondrial localization and direct role in\n  mitochondrial DNA metabolism,\
    \ rather than the mitochondrial HDA signal being a high-throughput localization\n\
    \  artifact.\nfocus_type: free_text\ncontext: []\nreference_id: []"
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
citation_count: 3
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** mus81
- **Gene symbol:** mus81
- **UniProt accession:** P87231

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** mitochondrial-localization-and-mtdna-function
- **Source file:** genes/SCHPO/mus81/mus81-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Schizosaccharomyces pombe Mus81 has a genuine mitochondrial localization and direct role in mitochondrial DNA metabolism, rather than the mitochondrial HDA signal being a high-throughput localization artifact.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe Mus81 has a genuine mitochondrial localization and direct role in
  mitochondrial DNA metabolism, rather than the mitochondrial HDA signal being a high-throughput localization
  artifact.
focus_type: free_text
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

# Focused Hypothesis Report — *S. pombe* Mus81 mitochondrial localization & mtDNA function

**Gene:** mus81 (UniProt **P87231**, MUS81_SCHPO), *Schizosaccharomyces pombe* (NCBITaxon:284812)
**Source review:** genes/SCHPO/mus81/mus81-ai-review.yaml — free-text hypothesis
**Seed hypothesis:** *Mus81 has a genuine mitochondrial localization and a direct role in mitochondrial DNA metabolism, rather than the mitochondrial HDA signal being a high-throughput localization artifact.*

---

## Executive Judgment

**Verdict: Refuted (the mitochondrial/mtDNA claim is over-annotated; the HDA mitochondrion signal is best treated as a high-throughput localization artifact).**

Four independent lines of evidence converge against the seed hypothesis:

1. **Annotation provenance.** QuickGO shows the mitochondrion term (GO:0005739, HDA) **and** the nucleus term (GO:0005634, HDA) for Mus81 both trace to a **single reference, PMID:16823372** (Matsuyama et al. 2006 — genome-wide C-terminal YFP tagging of ~90% of the *S. pombe* proteome). This is one high-throughput imaging dataset that reported a dual/ambiguous signal. In contrast, every **low-throughput direct assay (IDA)** for Mus81 comes from dedicated papers and places it in **nuclear** complexes (Holliday junction resolvase complex GO:0048476, PMID:11719193/14527419; nuclear replication fork GO:0043596, PMID:17363897), and the curated UniProt subcellular-location statement is **Nucleus** only.

2. **Sequence (with positive control).** The Mus81 N-terminus has **no canonical mitochondrial targeting presequence**, shown directly by side-by-side comparison with the bona fide mitochondrial resolvase Cce1/Ydc2 (UniProt Q10423, curated *Mitochondrion*):

   | Protein (first 30 aa) | Arg | R+K | D+E | Net charge | 1st acidic pos | GRAVY |
   |---|---|---|---|---|---|---|
   | **Cce1/Ydc2** (Q10423, genuine mito) `MATVKLSFLQHICKLTGLSRSGRKDELLRR` | 4 | 7 | 2 | **+5** | **25** | −0.25 |
   | **Mus81** (P87231, claimed mito) `MDCGNPLFLQWIQEWMEESTRRFPKSYQTW` | 2 | 3 | 4 | **−1** | **2** | −0.92 |

   Cce1/Ydc2 has the textbook Arg-rich, net-positive presequence with no acidic residue until position 25; Mus81 is net-**negative** with an acidic residue (Asp) immediately at position 2 — the opposite of an import signal.

3. **Biological redundancy.** *S. pombe* already possesses a **dedicated mitochondrial Holliday-junction resolvase, Ydc2/SpCce1** (RuvC/CCE1 family), which localizes exclusively to mitochondria and is the enzyme responsible for mtDNA maintenance (loss → mtDNA aggregation/depletion). Mus81 is a structurally unrelated **nuclear XPF-family** endonuclease. There is no functional niche that requires Mus81 in mitochondria, and no primary literature reports any mitochondrial or mtDNA role for Mus81.

4. **No conservation.** Direct QuickGO cross-check: *S. cerevisiae* MUS81 (Q04149) and human MUS81 (Q96NY9) carry **only nuclear** cellular-component annotations and **no** mitochondrion term. The mitochondrion call is unique to *S. pombe* Mus81 and to one HDA reference — not a conserved feature of the MUS81 family.

**Most important caveat:** This assessment is negative/inferential. An HDA call is weak positive evidence, not proof of absence; a genuine minor mitochondrial pool cannot be excluded without a targeted, endogenously-tagged localization experiment. The sequence check is a heuristic (TargetP/MitoFates could not be executed programmatically here). But the balance of evidence is strongly against a genuine, functional mitochondrial role.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt **P87231** (database) | Review/database | Qualifies | Where is Mus81 annotated? | Curated location = **Nucleus** only; mitochondrion = **HDA**; nucleus complexes = **IDA** | *S. pombe*, curated record | High for provenance; HDA is low-specificity |
| QuickGO / **PMID:16823372** (Matsuyama 2006) | Localization (high-throughput) | Refutes (artifact source) | Origin of the mito call | Mitochondrion **and** nucleus HDA calls both come from the **same** genome-wide C-terminal YFP study; a single ambiguous HT dataset | *S. pombe* proteome screen | High for provenance; HT dual-localization is low-specificity |
| **This report** (computed, N-term MTS + positive control) | Computational | Refutes | Does Mus81 carry an MTS? | Mus81 first-30: net **−1**, acidic at pos 2, GRAVY −0.92 → **no MTS**; positive control Cce1/Ydc2 (Q10423): net **+5**, first acidic pos 25 → canonical MTS | Sequence heuristic + control | Medium-high; heuristic, but validated against a true mito protein |
| PMID **11719193** (Boddy 2001) | Direct assay / interaction | Refutes (context) | Mus81 identity/locale | Mus81-Eme1 identified as **nuclear** structure-specific endonuclease (basis of IDA GO:0048476) | *S. pombe* | High |
| 23584455 | Direct assay / mutant | Refutes (context) | Mus81 core function | Mus81-Eme1 is a **nuclear** HJ resolvase activated by CDK/ATR (Eme1 phospho) to prevent chromosomal rearrangements | *S. pombe* | High |
| 22855558 | Mutant phenotype | Refutes (context) | Mus81 substrate/locale | Resolves **meiotic nuclear** joint molecules (crossovers); regulated by Smc5/6 | *S. pombe* meiosis | High |
| 19470480 | Mutant phenotype | Refutes (context) | Mus81 role | Mus81-Eme1 generates **nuclear** meiotic crossovers at DSBs | *S. pombe* meiosis | High |
| 23982516 | Structural / biochem | Refutes (context) | Mus81 mechanism | WH domain of MUS81 binds branched DNA; yeast phenocopy links to nuclear DNA-damage sensitivity | Human + *S. pombe* | High |
| **10954073** | Localization + mutant | Competing | Which enzyme handles mtDNA junctions? | **SpCCE1/Ydc2-GFP localizes exclusively to mitochondria**; ydc2Δ → mtDNA aggregation | *S. pombe* | High — identifies the true mt resolvase |
| **12823554** | Mutant / rescue | Competing | Ydc2 mtDNA role | ydc2Δ → **mtDNA depletion**, rescued only by active full-length Ydc2; mutants localize to mitochondria | *S. pombe* | High |
| 11726496 | Structural | Competing | Nature of mt resolvase | Ydc2 = eukaryotic RuvC-family mt HJ resolvase (crystal structure) | *S. pombe* | High |
| 9421521 / 9343409 | Biochemical | Competing | Ydc2 identity | Ydc2 is the functional *S. pombe* CCE1 homolog, a mt HJ resolvase | *S. pombe* | High |
| QuickGO orthologs **Q04149** (*S. cerevisiae*), **Q96NY9** (human) | Structural/evolutionary (comparative) | Refutes | Is the mito call conserved? | Both orthologs have **exclusively nuclear** CC terms; **no** GO:0005739 in either — mito call is *S. pombe*-only & single-study | Budding yeast + human | High for provenance; annotation completeness caveat |
| PubMed "Mus81 mitochondria/mtDNA" | Absence of evidence | Refutes | Any mt role for Mus81? | **No papers returned** | — | Absence, not proof |

---

## GO Curation Implications (leads — require curator verification)

- **GO:0005739 `mitochondrion` (CC), evidence HDA:PomBase — lead: consider REMOVE or DO-NOT-PROPAGATE / NOT-core.** It is unsupported by any focused assay, contradicted by the curated Nucleus location, by the absence of an MTS, and by the existence of a dedicated mitochondrial resolvase (Ydc2). At minimum it should not be treated as representing a biological function. If retained, flag as high-throughput-only and non-core.
- **Retain nuclear CC terms:** GO:0048476 `Holliday junction resolvase complex` (IDA) and GO:0043596 `nuclear replication fork` (IDA); GO:0005634 `nucleus` is well supported. These are the genuine location.
- **MF:** retain `crossover junction endonuclease activity` / structure-specific (5'-flap / branched DNA) endonuclease activity.
- **BP:** retain nuclear DNA repair / recombination / replication-fork processing / meiotic recombination. Do **not** add mtDNA-metabolism BP terms to Mus81.
- Avoid a bare "protein binding" fallback — the informative, supported terms are the nuclear resolvase MF/CC/BP set above.

---

## Mechanistic Scope

**Direct molecular activity (supported):** Mus81, in a heterodimer with Eme1, is a Mg²⁺-dependent structure-specific endonuclease that incises branched DNA (3'-flaps, D-loops, replication forks, nicked Holliday junctions) in the **nucleus**, resolving recombination/replication intermediates. Activity is cell-cycle/DNA-damage regulated via CDK/ATR phosphorylation of Eme1.

**Claimed but unsupported (seed hypothesis):** import into mitochondria and direct action on mtDNA. This is not an observed direct activity; it is inferred only from a high-throughput localization dataset. The corresponding mtDNA-junction-processing function in *S. pombe* is performed by the unrelated Ydc2/SpCce1.

---

## Conflicts and Alternatives

- **Dedicated-enzyme alternative (strongest):** Ydc2/SpCce1 already fulfills mitochondrial HJ resolution/mtDNA maintenance; a second, unrelated nuclease for the same niche is biologically unnecessary and unreported.
- **Artifact of high-throughput tagging:** N-terminal or over-expression YFP/GFP tagging commonly yields low-level spurious mitochondrial signals; the HDA code is exactly this class of data.
- **Paralog/ortholog carry-over (checked directly):** QuickGO CC annotations for *S. cerevisiae* MUS81 (Q04149) and human MUS81 (Q96NY9) are **exclusively nuclear** (nucleus, nuclear chromosome, nuclear replication fork, HJ resolvase complex, telomeric/chromosomal region, nucleoplasm) with **no mitochondrion (GO:0005739)** term in either. The mitochondrion call exists **only** for *S. pombe* Mus81 and **only** via the single HDA reference PMID:16823372 — i.e., it is species-specific and not conserved, arguing against genuine, conserved mitochondrial biology.
- **Not excluded:** a small, functionally minor mitochondrial pool, or a stress-specific relocalization, cannot be ruled out by these data alone.

---

## Knowledge Gaps

1. **Provenance of the exact HDA dataset — RESOLVED.** Checked: QuickGO → the mitochondrion HDA (and nucleus HDA) call both derive from PMID:16823372 (Matsuyama et al. 2006), a **C-terminal (3′) YFP** genome-wide screen. Residual gap: raw image for Mus81 in that dataset not inspected here; a C-terminal tag would not mask an N-terminal MTS, so the mito signal most plausibly reflects HT imaging ambiguity/overexpression. Resolve: inspect the original localization image/record.
2. **Endogenous localization.** Checked: curated Nucleus statement + IDA nuclear complexes. Gap: no endogenously-tagged, mitochondria-co-stained Mus81 image was located. Resolve: mNeonGreen knock-in Mus81 + MitoTracker/mtDNA co-staining and fractionation.
3. **Formal MTS prediction.** Checked: manual N-terminal charge/hydropathy heuristic (no MTS). Gap: TargetP2/MitoFates/DeepMito not runnable programmatically here. Resolve: run these predictors on P87231.
4. **mtDNA phenotype of mus81Δ.** Checked: literature — none reported. Gap: no direct test of mtDNA copy number/integrity in mus81Δ. Resolve: qPCR mtDNA copy number and mtDNA topology in mus81Δ vs ydc2Δ.

---

## Discriminating Tests

1. **Endogenous knock-in localization + fractionation:** tag chromosomal *mus81* with a fluorophore; co-image with a mitochondrial marker and quantify Mn-fold enrichment; biochemically fractionate and immunoblot for Mus81 in purified mitochondria (with nuclear/cytosolic controls).
2. **mtDNA functional assay:** measure mtDNA copy number, aggregation, and petite/respiration phenotypes in *mus81Δ* vs *ydc2Δ* vs WT. Ydc2Δ shows mtDNA aggregation/depletion; a genuine Mus81 role predicts a (possibly redundant) mtDNA phenotype, whereas an artifact predicts none.
3. **MTS predictors** (TargetP2, MitoFates, DeepMito) on P87231 and a fused N-terminal-Mus81(1–40)-GFP import assay.
4. **Epistasis:** *mus81Δ ydc2Δ* double mutant — synthetic mtDNA defect would argue for a real (backup) mitochondrial role; no aggravation argues against.

---

## Curation Leads (require curator verification)

- **Action change:** Mark GO:0005739 `mitochondrion` (HDA) as **non-core / candidate removal** for Mus81; keep nuclear CC/MF/BP terms as the core annotation.
- **Candidate supporting references (verify snippets):**
  - PMID **10954073**: "*a SpCCE1-GFP fusion localises exclusively to the mitochondria of S. pombe*" — identifies the true mitochondrial resolvase (competes with the Mus81 mt claim).
  - PMID **12823554**: "*Cells that lacked Ydc2 showed a significant depletion of mtDNA content*" — the mtDNA-maintenance function is Ydc2's, not Mus81's.
  - PMID **23584455**: DNA-damage-induced activation of the **nuclear** Mus81-Eme1 resolvase — Mus81's genuine role/location.
  - UniProt **P87231**: curated SUBCELLULAR LOCATION = Nucleus; mitochondrion term is HDA only.
- **Suggested curator questions:** Which high-throughput study underlies the HDA mitochondrion call, and what tag/expression was used? Is there any endogenous, non-HT evidence for Mus81 in mitochondria?
- **Suggested experiments:** endogenous-tag co-localization + fractionation; mtDNA copy-number/topology in mus81Δ; MTS predictions and N-terminal import assay.

---

### Provenance note
Computational analyses run here (code + raw outputs in the iteration transcript): (1) live UniProt REST fetch of P87231 (length 608; curated Nucleus; GO-CC evidence codes as tabulated); (2) **QuickGO annotation query** for P87231 → both mitochondrion and nucleus HDA terms map to PMID:16823372; nuclear IDA terms map to PMID:11719193/14527419/17363897; (3) N-terminal targeting-signal feature calculation for Mus81 vs the mitochondrial positive control Cce1/Ydc2 (Q10423): Mus81 first-30 net −1, acidic at pos 2, GRAVY −0.92; Cce1/Ydc2 net +5, first acidic pos 25, GRAVY −0.25. Writing to a provenance directory was blocked by sandbox permissions; results are reproducible from the recorded code. No result was fabricated; dedicated MTS predictor tools (TargetP2/MitoFates/DeepMito) could not be executed in this environment and are listed as gaps.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)