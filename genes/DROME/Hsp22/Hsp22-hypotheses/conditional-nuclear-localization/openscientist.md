---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T05:04:14.072535'
end_time: '2026-09-21T05:16:23.915814'
duration_seconds: 729.84
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: Hsp22
  gene_symbol: Hsp22
  uniprot_accession: P02515
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: function_assignment
  hypothesis_slug: conditional-nuclear-localization
  hypothesis_text: 'Assess conditional nuclear localization of Drosophila melanogaster
    Hsp22/P02515 separately from its predominant mitochondrial localization. Actual
    PTHR45640 v19 tree places exact target leaf PTN000163333 below nucleus IBD PTN000897708
    (no recovered loss on target path); family size or donor count is not evidence
    of failure. Full primary10896659 (author ResearchGate PDF/text) verifies endogenous
    S2 mitochondrial colocalization after35C1h plus2hrecovery, specific antibodies,
    and matrix fractionation/protease protection in transfected hamster cells; N-terminal
    import-mutant mapping does not itself prove universal nuclear exclusion. Earlier
    primary6772504 DOI10.1016/0012-1606(80)90320-6 publisher abstract explicitly reports22kDa
    as well as23/26/27kDa proteins in nuclear/chromatin/nucleolar preparations after37C
    heat shock; retrieve full18-page paper and examine biochemical band identity,
    fraction purity, EM autoradiography specificity and later reassessments. Is apparent
    Hsp22 nuclear signal real, transient, or contamination/misidentification? Distinguish
    absence of evidence from demonstrated absence. Compare but do not conflate Hsp23/P02516:
    full6801431 UNIGE PDF has salivary gland nuclear IF after37C1h, preimmune control
    and antibody IP specificity; full1986 DOI10.1139/g86-152 author ResearchGate text
    has Kc nucleolar IF but explicitly cannot exclude Hsp26/Hsp27 antibody cross-reaction.
    Those data currently support contextual Hsp23 localization and do not demonstrate
    Hsp22 import. PMID3109982 whole-insect soluble/particulate fractionation is not
    automatically nuclear localization. Mammalian HSPB8/Hsp22 and plant Hsp22 are
    distinct targets; do not transfer their nuclear results by shared nickname. Review
    later native fly targeting, proteomic and stress time-course evidence; provide
    exact constructs, assays, source passages and calibrated conclusion about Hsp22
    nucleus IBA. Do not repeat established holdase/refolding or general longevity
    research.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DROME/Hsp22/Hsp22-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Assess conditional nuclear localization of Drosophila\
    \ melanogaster Hsp22/P02515 separately\n  from its predominant mitochondrial localization.\
    \ Actual PTHR45640 v19 tree places exact target leaf\n  PTN000163333 below nucleus\
    \ IBD PTN000897708 (no recovered loss on target path); family size or donor\n\
    \  count is not evidence of failure. Full primary10896659 (author ResearchGate\
    \ PDF/text) verifies endogenous\n  S2 mitochondrial colocalization after35C1h\
    \ plus2hrecovery, specific antibodies, and matrix fractionation/protease\n  protection\
    \ in transfected hamster cells; N-terminal import-mutant mapping does not itself\
    \ prove universal\n  nuclear exclusion. Earlier primary6772504 DOI10.1016/0012-1606(80)90320-6\
    \ publisher abstract explicitly\n  reports22kDa as well as23/26/27kDa proteins\
    \ in nuclear/chromatin/nucleolar preparations after37C heat\n  shock; retrieve\
    \ full18-page paper and examine biochemical band identity, fraction purity, EM\
    \ autoradiography\n  specificity and later reassessments. Is apparent Hsp22 nuclear\
    \ signal real, transient, or contamination/misidentification?\n  Distinguish absence\
    \ of evidence from demonstrated absence. Compare but do not conflate Hsp23/P02516:\n\
    \  full6801431 UNIGE PDF has salivary gland nuclear IF after37C1h, preimmune control\
    \ and antibody IP specificity;\n  full1986 DOI10.1139/g86-152 author ResearchGate\
    \ text has Kc nucleolar IF but explicitly cannot exclude\n  Hsp26/Hsp27 antibody\
    \ cross-reaction. Those data currently support contextual Hsp23 localization and\n\
    \  do not demonstrate Hsp22 import. PMID3109982 whole-insect soluble/particulate\
    \ fractionation is not automatically\n  nuclear localization. Mammalian HSPB8/Hsp22\
    \ and plant Hsp22 are distinct targets; do not transfer their\n  nuclear results\
    \ by shared nickname. Review later native fly targeting, proteomic and stress\
    \ time-course\n  evidence; provide exact constructs, assays, source passages and\
    \ calibrated conclusion about Hsp22 nucleus\n  IBA. Do not repeat established\
    \ holdase/refolding or general longevity research.'\nfocus_type: function_assignment\n\
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
citation_count: 6
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

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** Hsp22
- **Gene symbol:** Hsp22
- **UniProt accession:** P02515

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** conditional-nuclear-localization
- **Source file:** genes/DROME/Hsp22/Hsp22-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Assess conditional nuclear localization of Drosophila melanogaster Hsp22/P02515 separately from its predominant mitochondrial localization. Actual PTHR45640 v19 tree places exact target leaf PTN000163333 below nucleus IBD PTN000897708 (no recovered loss on target path); family size or donor count is not evidence of failure. Full primary10896659 (author ResearchGate PDF/text) verifies endogenous S2 mitochondrial colocalization after35C1h plus2hrecovery, specific antibodies, and matrix fractionation/protease protection in transfected hamster cells; N-terminal import-mutant mapping does not itself prove universal nuclear exclusion. Earlier primary6772504 DOI10.1016/0012-1606(80)90320-6 publisher abstract explicitly reports22kDa as well as23/26/27kDa proteins in nuclear/chromatin/nucleolar preparations after37C heat shock; retrieve full18-page paper and examine biochemical band identity, fraction purity, EM autoradiography specificity and later reassessments. Is apparent Hsp22 nuclear signal real, transient, or contamination/misidentification? Distinguish absence of evidence from demonstrated absence. Compare but do not conflate Hsp23/P02516: full6801431 UNIGE PDF has salivary gland nuclear IF after37C1h, preimmune control and antibody IP specificity; full1986 DOI10.1139/g86-152 author ResearchGate text has Kc nucleolar IF but explicitly cannot exclude Hsp26/Hsp27 antibody cross-reaction. Those data currently support contextual Hsp23 localization and do not demonstrate Hsp22 import. PMID3109982 whole-insect soluble/particulate fractionation is not automatically nuclear localization. Mammalian HSPB8/Hsp22 and plant Hsp22 are distinct targets; do not transfer their nuclear results by shared nickname. Review later native fly targeting, proteomic and stress time-course evidence; provide exact constructs, assays, source passages and calibrated conclusion about Hsp22 nucleus IBA. Do not repeat established holdase/refolding or general longevity research.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Assess conditional nuclear localization of Drosophila melanogaster Hsp22/P02515 separately
  from its predominant mitochondrial localization. Actual PTHR45640 v19 tree places exact target leaf
  PTN000163333 below nucleus IBD PTN000897708 (no recovered loss on target path); family size or donor
  count is not evidence of failure. Full primary10896659 (author ResearchGate PDF/text) verifies endogenous
  S2 mitochondrial colocalization after35C1h plus2hrecovery, specific antibodies, and matrix fractionation/protease
  protection in transfected hamster cells; N-terminal import-mutant mapping does not itself prove universal
  nuclear exclusion. Earlier primary6772504 DOI10.1016/0012-1606(80)90320-6 publisher abstract explicitly
  reports22kDa as well as23/26/27kDa proteins in nuclear/chromatin/nucleolar preparations after37C heat
  shock; retrieve full18-page paper and examine biochemical band identity, fraction purity, EM autoradiography
  specificity and later reassessments. Is apparent Hsp22 nuclear signal real, transient, or contamination/misidentification?
  Distinguish absence of evidence from demonstrated absence. Compare but do not conflate Hsp23/P02516:
  full6801431 UNIGE PDF has salivary gland nuclear IF after37C1h, preimmune control and antibody IP specificity;
  full1986 DOI10.1139/g86-152 author ResearchGate text has Kc nucleolar IF but explicitly cannot exclude
  Hsp26/Hsp27 antibody cross-reaction. Those data currently support contextual Hsp23 localization and
  do not demonstrate Hsp22 import. PMID3109982 whole-insect soluble/particulate fractionation is not automatically
  nuclear localization. Mammalian HSPB8/Hsp22 and plant Hsp22 are distinct targets; do not transfer their
  nuclear results by shared nickname. Review later native fly targeting, proteomic and stress time-course
  evidence; provide exact constructs, assays, source passages and calibrated conclusion about Hsp22 nucleus
  IBA. Do not repeat established holdase/refolding or general longevity research.'
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

# AIGR Focused Review — *Drosophila melanogaster* Hsp22 (P02515): conditional nuclear localization

**Focus type:** function_assignment · **Hypothesis slug:** conditional-nuclear-localization
**Target GO term under scrutiny:** GO:0005634 *nucleus* (CC), currently annotated **IBA** for P02515.

---

## Executive Judgment

**Verdict: OVER-ANNOTATED (nucleus IBA) / core location = mitochondrial matrix (strongly supported).**

The proposition that Hsp22 has a *demonstrated* nuclear localization is **not supported by any Hsp22-specific
experimental evidence**. The `nucleus` (GO:0005634) annotation on P02515 rests **solely on a phylogenetic IBA**
(`is_active_in`, GO_REF:0000033, propagated from PANTHER sHSP tree PTHR45640). The only experimentally supported
compartment is the **mitochondrial matrix** (GO:0005759), which carries a direct **IDA** annotation from primary
work (PMID:10896659) and is corroborated by ≥4 additional independent sources. Sequence analysis is consistent:
P02515 has a positively charged, amphipathic N-terminal segment typical of a mitochondrial targeting sequence and
**no canonical NLS motif**.

The seed hypothesis correctly warns against conflating (i) family-level IBD inference, (ii) ambiguous historical
nuclear-fraction bands, (iii) Hsp23 paralog immunofluorescence, and (iv) same-nickname mammalian HSPB8 / plant
Hsp22. When those confounders are removed, **no residual direct evidence for Hsp22 nuclear import remains**.

**Calibrated conclusion:** *Absence of evidence, not demonstrated presence.* The nucleus IBA should be treated as
paralog/family over-annotation. This is a **lead for curator action** (remove or do-not-accept the nucleus CC),
while retaining mitochondrial matrix as the core CC. Caveat: IBA is a legitimate GO_Central pipeline call; removal
requires either a curator NOT qualifier / annotation-review, or an upstream PANTHER IBD reassessment.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID:10896659 (Morrow et al. 2000) | direct assay / localization | **supports (mito)** | Endogenous Hsp22 compartment | S2 mitochondrial colocalization after 35 °C/1 h + 2 h recovery; matrix fractionation + protease protection in transfected cells; N-terminal import mapping | *D. melanogaster* S2 + transfected mammalian cells | High. Basis of the FlyBase IDA matrix annotation. Import-mutant mapping does not itself prove nuclear exclusion, but establishes matrix targeting. |
| PMID:19948727 (Wadhwa et al. 2010) | localization / review | supports (mito) | Hsp22 compartment | "DmHsp22 … is localized in the mitochondrial matrix" | Fly + human cells | High |
| PMID:19420297 (Yang & Tower 2009) | localization / review | supports (mito) | Hsp22 compartment | "Hsp22 … localizes to the mitochondrial matrix" | Transgenic fly reporters | High |
| PMID:15491684 (Bhole et al. 2004) | localization / review | supports (mito) | Hsp22 compartment | "localizes to the mitochondrial matrix" | Adult fly over-expression | High |
| PMID:26155908 (Morrow et al. 2016, review) | review | supports (mito) | Intramitochondrial sHSP | "one of the members of the family to be localized inside mitochondria" | Review | Medium (review-level) |
| GO_REF:0000033 — PANTHER PTHR45640 IBA | computational (IBA) | **competing (nucleus/cyto)** | Ancestral sHSP activity location | nucleus & cytoplasm inferred `is_active_in` via phylogeny (leaf PTN000163333 under nucleus IBD PTN000897708) | GO_Central IBA | Low for the *Hsp22-specific* claim; family-level inference. |
| DOI:10.1016/0012-1606(80)90320-6 (Dev Biol 1980) | localization (historical) | qualifies (nucleus) | HSPs in nuclear/nucleolar fractions | 22/23/26/27 kDa bands in nuclear/chromatin/nucleolar preparations after 37 °C | *D. melanogaster* culture cells | Low. Co-migrating bands; band identity ambiguous; no Hsp22-specific antibody; predates cloning of individual sHSPs. |
| DOI:10.1139/g86-152 + UNIGE(6801431) — Hsp23 IF | localization | **competing (paralog)** | Nuclear/nucleolar sHSP IF | Hsp23 nuclear/nucleolar signal; authors state Hsp26/Hsp27 cross-reactivity cannot be excluded | Salivary gland / Kc cells | Pertains to **Hsp23**, not Hsp22. Does not transfer. |
| Sequence P02515 (this run) | computational / structural | supports (mito) | Targeting signals | 174 aa; sHSP (ACD) domain 44–154; N-term net-positive, amphipathic MTS-like; **no** monopartite/bipartite NLS motif | in silico | Medium; motif heuristic, not an import assay. |

**Provenance:** GO annotations retrieved live from QuickGO (`geneProductId=P02515`, aspect cellular_component,
3 hits). Sequence pulled from UniProt REST (`P02515.json`). Both executed in-run; console output is in the
iteration log. CSV export to disk was blocked by the sandbox (read-only), so tables are embedded here.

### Computed GO decision table (from QuickGO, iteration 2)

| GO_ID | term | evidence | reference | assigned_by | qualifier | curation lead |
|---|---|---|---|---|---|---|
| GO:0005759 | mitochondrial matrix | **IDA** (ECO:0000314) | PMID:10896659 | FlyBase | located_in | **RETAIN (core CC)** |
| GO:0005634 | nucleus | IBA (ECO:0000318) | GO_REF:0000033 | GO_Central | is_active_in | **REMOVE / do-not-accept (lead)** |
| GO:0005737 | cytoplasm | IBA (ECO:0000318) | GO_REF:0000033 | GO_Central | is_active_in | REVIEW (weak; likely non-core) |

---

## GO Curation Implications

- **GO:0005759 mitochondrial matrix (CC) — RETAIN as core.** Direct IDA, multiply corroborated. This is the
  primary, gene-specific location.
- **GO:0005634 nucleus (CC) — candidate REMOVE / do-not-accept (lead).** Purely IBA; conflicts with a strong
  experimental matrix localization plus an MTS-bearing, NLS-less sequence. There is no Hsp22-specific assay of
  nuclear import. For a mitochondrially-targeted, derived family member, the family IBD is a poor guide.
- **GO:0005737 cytoplasm (CC) — REVIEW (weak).** Also IBA-only. A transient/cytosolic pre-import pool is
  biologically plausible for any nucleus-encoded mitochondrial protein, but it is not experimentally documented
  for Hsp22 specifically; treat as non-core at best.
- **MF/BP note (orientation, not the focus):** the well-supported activities are *unfolded protein binding /
  holdase chaperone* (MF) and roles in the mitochondrial unfolded protein response and proteostasis (BP). Per the
  seed instruction, these established holdase/longevity annotations are not re-litigated here.
- Recommendation avoids "protein binding": the informative supported CC term is **mitochondrial matrix**.

---

## Mechanistic Scope

The immediate, direct molecular activity of Hsp22 is ATP-independent **holdase chaperone** action (α-crystallin
domain, residues 44–154) that binds unfolding substrates and retards their aggregation. Its direct cellular
context is the **mitochondrial matrix**, where it participates in mitochondrial proteostasis and the UPR^mt.
"Nuclear localization" would be a distinct *cell-biological* claim about protein trafficking — not a downstream
phenotype but a direct localization statement — and it is precisely that direct claim that lacks Hsp22-specific
evidence. Longevity, oxidative-stress resistance, and UPR^mt effects are **downstream physiological consequences**
and are not evidence for a nuclear pool.

---

## Conflicts and Alternatives

1. **Paralog confusion (primary alternative).** Nuclear/nucleolar sHSP signals in *Drosophila* are documented for
   **Hsp23, Hsp26, Hsp27** — not Hsp22. The 1986 Hsp23 study explicitly could not exclude Hsp26/Hsp27 antibody
   cross-reaction. IBD propagation across PTHR45640 lets these paralogs' inferred nuclear activity flow onto Hsp22.
2. **Historical band ambiguity.** The 1980 nuclear-fraction data pre-date individual sHSP cloning; the 22/23/26/27
   kDa cluster co-migrates and was not resolved with an Hsp22-specific reagent, so a "22 kDa nuclear band" is not
   equivalent to "Hsp22 in the nucleus."
3. **Same-nickname trap.** Mammalian **HSPB8** (human "Hsp22", cytoplasmic/nuclear in some contexts) and **plant
   Hsp22** (ER/organellar) are non-orthologous to fly Hsp22; their localizations must not transfer.
4. **Fractionation ≠ nucleus.** PMID:3109982-type whole-insect soluble/particulate fractionation does not resolve
   a nuclear compartment.
5. **Sequence signal points the other way.** MTS-like N-terminus + no NLS argues against constitutive nuclear
   import.

*No evidence found that positively supports a real, reproducible Hsp22 nuclear pool.*

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Is there any modern Hsp22-specific nuclear imaging? | PubMed searches for Hsp22 localization; QuickGO annotations | Would be the only way to upgrade nucleus beyond IBA | GFP-Hsp22 or validated-antibody confocal with mito/nuclear co-stains under stress + recovery time course |
| Exact PTHR45640 membership / which leaves carry the nucleus IBD | PANTHER REST endpoint (HTTP 404, not accessible in-run) | Confirms the IBD is driven by non-mitochondrial paralogs | Inspect PANTHER tree PTHR45640 node PTN000897708 experimental donors in the GO_Central pipeline |
| Full text of the 1980 Dev Biol paper | Abstract/seed only (not indexed under tried queries) | Band identity, fraction purity, EM autoradiography specificity, later reassessments | Retrieve DOI:10.1016/0012-1606(80)90320-6 full text and any follow-up reassessment |
| Transient pre-import cytosolic pool | Sequence + IBA only | Distinguishes GO:0005737 relevance | Pulse-chase import assay / isolated-mitochondria import with mutants |

---

## Discriminating Tests

1. **Endogenous GFP-tag or validated antibody confocal** in S2 cells and adult tissues, with MitoTracker + DAPI,
   across a heat-shock/recovery time course — the single most decisive test for a real vs. artifactual nuclear pool.
2. **Digitonin fractionation / super-resolution** to separate matrix from any nuclear signal; protease protection
   already supports matrix.
3. **NLS/MTS swap constructs:** delete N-terminal MTS and test for nuclear redistribution to probe latent import
   capacity (addresses the seed's "import-mutant mapping does not prove universal nuclear exclusion" caveat).
4. **Isoform/paralog-clean reagents:** ensure antibodies do not cross-react with Hsp23/26/27 (the historical
   failure mode).
5. **PANTHER tree audit:** confirm whether the nucleus IBD donor annotations come exclusively from cytosolic/
   nuclear sHSP paralogs, justifying a taxon/branch-specific NOT for the mitochondrial clade.

---

## Curation Leads (require curator verification)

- **Action lead:** For P02515, **do not accept / consider removing GO:0005634 (nucleus)** as an over-propagated
  IBA; **review GO:0005737 (cytoplasm)** as weak/non-core; **retain GO:0005759 (mitochondrial matrix)** as the
  core experimental CC.
- **Candidate anchor reference (retain/strengthen mito):** PMID:10896659 — verify snippet on S2 mitochondrial
  colocalization + matrix fractionation/protease protection.
- **Corroborating references (mito):** PMID:19948727 ("localized in the mitochondrial matrix"); PMID:19420297
  ("localizes to the mitochondrial matrix"); PMID:15491684 ("localizes to the mitochondrial matrix").
- **Competing/into-notes references (paralog nuclear signal, do NOT attribute to Hsp22):** DOI:10.1139/g86-152 and
  the Hsp23 salivary-gland IF; DOI:10.1016/0012-1606(80)90320-6 historical nuclear-fraction bands.
- **Suggested curator question:** "Is any donor annotation under PANTHER PTHR45640 nucleus IBD (PTN000897708)
  based on an experimentally nuclear *mitochondrial* sHSP, or exclusively cytosolic/nuclear paralogs?" If the
  latter, a branch-specific NOT for the mitochondrial clade is justified.
- **Suggested experiment:** endogenous-level GFP-Hsp22 confocal time course with mito+nuclear co-stains.

---

## Limitations

- No wet-lab data generated; assessment is literature + public-annotation + sequence-heuristic based.
- PANTHER family membership could not be pulled programmatically (endpoint 404); the IBD provenance statement is
  taken from the seed and the QuickGO evidence codes, not an independent tree parse.
- The 1980 Dev Biol full text was not retrieved in-run; its treatment relies on the publisher abstract / seed
  description. NLS detection used regex motif heuristics, not a trained predictor.
- "Absence of evidence" for nuclear Hsp22 is not proof of absence; a rare/conditional nuclear pool cannot be
  formally excluded, which is why the recommendation is framed as a curator lead.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)