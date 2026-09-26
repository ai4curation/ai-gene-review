---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T02:49:19.809680'
end_time: '2026-09-21T03:08:03.788634'
duration_seconds: 1123.98
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: Egm
  gene_symbol: Egm
  uniprot_accession: Q5U117
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: function_assignment
  hypothesis_slug: medium-chain-catalysis-versus-assembly
  hypothesis_text: 'Drosophila melanogaster Egm/dACAD9 (Q5U117, CG9006) catalyzes
    medium-chain fatty acyl-CoA dehydrogenation and participates in medium-chain fatty
    acid catabolism. Assess molecular activity and physiological process separately.
    Egm has direct MCIA/complex-I assembly evidence (PMID34386730) and indirect lipid-metabolism
    mutant evidence (PMID16434470); neither excludes additional catalysis. Human ortholog
    ACAD9 has experimental GO0070991 from PMID16020546; the full paper tests C6-C12
    substrates and reports broad substrate use with a long-chain optimum, so preference
    is not exclusivity. Compare the human ACAD9 knockout study titled Complex I assembly
    function and fatty acid oxidation enzyme activity of ACAD9 both contribute to
    disease severity in ACAD9 deficiency (PMC4424958), which tests octanoate versus
    palmitate oxidation; verify its identifier before citing. Trace PTN000098033:
    current PAINT TSV places both terms there, but the served PTHR43884 v19 tree lacks
    that node and the exact Egm leaf. Do not invent a target lineage from the donor
    list. Determine whether target sequence, ortholog kinetics, physiological substrate
    flux or loss/divergence evidence supports the two claims without equating absence
    of fly assays or primary assembly role with negative evidence.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DROME/Egm/Egm-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Drosophila melanogaster Egm/dACAD9 (Q5U117, CG9006)\
    \ catalyzes medium-chain fatty acyl-CoA\n  dehydrogenation and participates in\
    \ medium-chain fatty acid catabolism. Assess molecular activity and\n  physiological\
    \ process separately. Egm has direct MCIA/complex-I assembly evidence (PMID34386730)\
    \ and\n  indirect lipid-metabolism mutant evidence (PMID16434470); neither excludes\
    \ additional catalysis. Human\n  ortholog ACAD9 has experimental GO0070991 from\
    \ PMID16020546; the full paper tests C6-C12 substrates\n  and reports broad substrate\
    \ use with a long-chain optimum, so preference is not exclusivity. Compare\n \
    \ the human ACAD9 knockout study titled Complex I assembly function and fatty\
    \ acid oxidation enzyme activity\n  of ACAD9 both contribute to disease severity\
    \ in ACAD9 deficiency (PMC4424958), which tests octanoate\n  versus palmitate\
    \ oxidation; verify its identifier before citing. Trace PTN000098033: current\
    \ PAINT TSV\n  places both terms there, but the served PTHR43884 v19 tree lacks\
    \ that node and the exact Egm leaf. Do\n  not invent a target lineage from the\
    \ donor list. Determine whether target sequence, ortholog kinetics,\n  physiological\
    \ substrate flux or loss/divergence evidence supports the two claims without equating\
    \ absence\n  of fly assays or primary assembly role with negative evidence.'\n\
    focus_type: function_assignment\ncontext: []\nreference_id: []"
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
- **Gene directory:** Egm
- **Gene symbol:** Egm
- **UniProt accession:** Q5U117

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** medium-chain-catalysis-versus-assembly
- **Source file:** genes/DROME/Egm/Egm-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Drosophila melanogaster Egm/dACAD9 (Q5U117, CG9006) catalyzes medium-chain fatty acyl-CoA dehydrogenation and participates in medium-chain fatty acid catabolism. Assess molecular activity and physiological process separately. Egm has direct MCIA/complex-I assembly evidence (PMID34386730) and indirect lipid-metabolism mutant evidence (PMID16434470); neither excludes additional catalysis. Human ortholog ACAD9 has experimental GO0070991 from PMID16020546; the full paper tests C6-C12 substrates and reports broad substrate use with a long-chain optimum, so preference is not exclusivity. Compare the human ACAD9 knockout study titled Complex I assembly function and fatty acid oxidation enzyme activity of ACAD9 both contribute to disease severity in ACAD9 deficiency (PMC4424958), which tests octanoate versus palmitate oxidation; verify its identifier before citing. Trace PTN000098033: current PAINT TSV places both terms there, but the served PTHR43884 v19 tree lacks that node and the exact Egm leaf. Do not invent a target lineage from the donor list. Determine whether target sequence, ortholog kinetics, physiological substrate flux or loss/divergence evidence supports the two claims without equating absence of fly assays or primary assembly role with negative evidence.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Drosophila melanogaster Egm/dACAD9 (Q5U117, CG9006) catalyzes medium-chain fatty acyl-CoA
  dehydrogenation and participates in medium-chain fatty acid catabolism. Assess molecular activity and
  physiological process separately. Egm has direct MCIA/complex-I assembly evidence (PMID34386730) and
  indirect lipid-metabolism mutant evidence (PMID16434470); neither excludes additional catalysis. Human
  ortholog ACAD9 has experimental GO0070991 from PMID16020546; the full paper tests C6-C12 substrates
  and reports broad substrate use with a long-chain optimum, so preference is not exclusivity. Compare
  the human ACAD9 knockout study titled Complex I assembly function and fatty acid oxidation enzyme activity
  of ACAD9 both contribute to disease severity in ACAD9 deficiency (PMC4424958), which tests octanoate
  versus palmitate oxidation; verify its identifier before citing. Trace PTN000098033: current PAINT TSV
  places both terms there, but the served PTHR43884 v19 tree lacks that node and the exact Egm leaf. Do
  not invent a target lineage from the donor list. Determine whether target sequence, ortholog kinetics,
  physiological substrate flux or loss/divergence evidence supports the two claims without equating absence
  of fly assays or primary assembly role with negative evidence.'
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

# AIGR Gene Hypothesis Deep Research — Final Report

## Target: *Drosophila melanogaster* Egm / dACAD9 (UniProt Q5U117, CG9006)
### Focus: function-assignment — "medium-chain catalysis versus complex-I assembly"

**Gene:** Egm (a.k.a. *Enigma*, CG9006), *D. melanogaster* · **UniProt:** Q5U117 (639 aa, "Complex I assembly factor Egm, mitochondrial") · **Focus type:** function_assignment · **Hypothesis slug:** medium-chain-catalysis-versus-assembly · **Iterations completed:** 3

---

## Summary

The seed hypothesis proposes that Egm/dACAD9 (a) catalyzes **medium-chain** fatty acyl-CoA dehydrogenation (GO:0070991) and (b) participates in **medium-chain** fatty acid catabolism (GO:0051793), and it asks that molecular activity and physiological process be assessed separately without treating the assembly role or the absence of fly assays as negative evidence for catalysis. After three iterations combining sequence orthology, domain analysis, active-site register mapping, ortholog enzymology, and phylogenetic-provenance checks, the conclusion is that the **specific "medium-chain" descriptor is over-annotated** and should not be retained at that specificity — while any generic catalytic role remains plausible but unproven in the fly.

Four independent lines converge. First, Egm is unambiguously the **ACAD9/VLCAD (long/very-long-chain) clade** ortholog — 37.2% identity to human ACAD9 and 36.9% to VLCAD versus only **28.0% to the canonical medium-chain enzyme MCAD/ACADM** — and it carries the ACAD9/ACADV-specific InterPro domain (PF21343 / IPR049448), not an MCAD signature. Second, the best-characterized ortholog (human ACAD9) has a **long-chain unsaturated** substrate optimum, and even that residual FAO activity is described in the literature as biologically controversial. Third, the canonical ACAD catalytic proton-acceptor glutamate maps onto a **glycine (Egm Gly446)** in a register-anchored alignment, so even generic dehydrogenase catalysis by the fly protein is inferential. Fourth, live PANTHER v19 maps Egm to PTHR48083:SF2 carrying only generic GO terms, so the medium-chain IBA terms cannot be traced to the served phylogenetic node — corroborating the seed's own concern about the PTN000098033 / PTHR43884 provenance.

The most important caveat is that **no direct fly acyl-CoA dehydrogenase assay exists** for or against any substrate. The correct curation posture is therefore not "refuted" but **"over-annotated":** the medium-chain-specific MF and BP terms are unsupported by any fly experiment and contradicted in direction by orthology and ortholog enzymology, whereas the well-evidenced core function is **mitochondrial complex-I assembly** (GO:0032981; MCIA localization GO:0160295). Absence of fly assays is not treated as evidence against catalysis — but neither is it evidence for the medium-chain specificity the annotation claims.

---

## Executive Judgment

**Verdict: Over-annotated — weakly/partially supported for "catalysis in general"; the specific "medium-chain" descriptor is not supported and should be removed, generalized, or re-anchored to the long/very-long-chain clade.**

Evaluating the two claims separately:

- **Any acyl-CoA dehydrogenase catalysis by Egm is plausible but unproven in the fly.** Egm carries an intact FAD-binding flavoprotein fold (GO:0050660, IEA) and is the clear ortholog of human ACAD9, an experimentally validated (if in-vivo-controversial) flavoenzyme. Catalysis cannot be excluded, and the assembly role does not exclude it. This is **weakly supported by orthology only**.
- **The "medium-chain" specificity is the weakest possible choice and is unsupported.** Egm is sequence-closest to the **ACAD9/VLCAD (long/very-long-chain) clade** and clearly separated from the medium-chain enzyme **ACADM/MCAD**. The ortholog's measured optimum is **long-chain**. On Egm the medium-chain terms are **IBA-only**, whereas FlyBase's ISS transfer gave Egm the **very-long-chain** term (GO:0017099), not medium-chain.
- **The primary, best-evidenced function is complex-I assembly** (GO:0032981; IDA localization to the MCIA complex GO:0160295; fly genetics in Murari 2021). The lipid/lifespan phenotypes (Mourikis 2006) are equally explained by loss of OXPHOS/complex-I as by a direct medium-chain flux, so they do **not** independently establish medium-chain catabolism.
- **The catalytic base glutamate appears degenerate in Egm.** A register-anchored alignment places the proton-acceptor Glu column (ACAD9 Glu426 / VLCAD Glu462) onto a **glycine (Egm Gly446)**; Egm carries no annotated active site. This weakens any *direct* catalysis call (caveat: the ACAD catalytic base can migrate between subfamilies, so structure-based superposition is needed to be definitive).
- **Domain + provenance corroboration.** InterPro assigns Egm the ACAD9/ACADV-specific C-terminal domain and no MCAD signature; live PANTHER v19 maps Egm to PTHR48083:SF2 carrying only generic GO:0016627/GO:0006635 — the served node does **not** carry the medium-chain terms.

**Bottom line for the curator:** Do not equate the assembly role or the absence of fly assays with negative evidence for catalysis — but the *medium-chain* specificity is a mis-transfer. If any substrate-resolved MF term is retained, it should be **long-/very-long-chain (GO:0004466 / GO:0017099)** rather than **medium-chain (GO:0070991)**, kept as **non-core** relative to the assembly function. The parallel BP term GO:0051793 is likewise better generalized or dropped.

---

## Key Findings

### Finding 1 — Egm is the ACAD9/VLCAD (long/very-long-chain) clade ortholog, not the medium-chain (MCAD) clade

Global Needleman-Wunsch alignment of the 639-aa Egm protein against the five human acyl-CoA dehydrogenase paralogs produced a clear clade ranking:

| Human paralog | Clade | Global identity to Egm |
|---|---|---|
| **ACAD9** (Q9H845) | long-chain / complex-I assembly | **37.2%** |
| **VLCAD (ACADVL, P49748)** | very-long-chain | **36.9%** |
| SCAD (ACADS, P16219) | short-chain | 29.3% |
| **MCAD (ACADM, P11310)** | **medium-chain** | **28.0%** |
| LCAD (ACADL, P28330) | long-chain | 27.5% |

Egm is closest to ACAD9 and VLCAD — the long/very-long-chain and complex-I-assembly clade — and separated by roughly **9 percentage points** from the medium-chain enzyme ACADM/MCAD, which (with LCAD) it resembles least. This is corroborated by nomenclature and annotation: UniProt names the protein "**Complex I assembly factor Egm, mitochondrial**," and FlyBase assigns Egm the long-chain term **GO:0017099 (very-long-chain acyl-CoA dehydrogenase activity)** by ISS, whereas the medium-chain term **GO:0070991 is present only by IBA**. The direction of the sequence evidence therefore points away from a medium-chain assignment and toward the long/very-long-chain + assembly identity. (Caveat: 37% identity is modest for any confident specificity transfer, and the ±1 scoring NW gives approximate absolute values, though the rank order is robust.)

### Finding 2 — Ortholog kinetics are long-chain, not medium-chain; the fly protein has no direct catalytic assay

The seed correctly notes that human ACAD9 was tested across C6–C12 substrates, but the primary enzymology reports a long-chain optimum. Ensenauer et al. 2005 ([PMID: 16020546](https://pubmed.ncbi.nlm.nih.gov/16020546/)) state that "**Purified mature ACAD-9 had maximal activity with long-chain unsaturated acyl-CoAs as substrates (C16:1-, C18:1-, C18:2-, C22:6-CoA)**," concluding a role in β-oxidation of long-chain *unsaturated* fatty acids. Broad substrate use with a long-chain optimum means preference is not exclusivity — but the *optimum itself is long-chain*, not medium-chain.

The knockout study whose identifier the seed asked to verify is **Schiff et al. 2015, [PMID: 25721401](https://pubmed.ncbi.nlm.nih.gov/25721401/) = PMC4424958** — title verified to match exactly ("Complex I assembly function and fatty acid oxidation enzyme activity of ACAD9 both contribute to disease severity in ACAD9 deficiency"). It states "**ACAD9 also retains enzyme ACAD activity for long-chain fatty acids in vitro, but the biological relevance of this function remains controversial partly because of the tissue specificity of ACAD9 expression**." So even in the human ortholog, residual FAO activity is framed as long-chain and its in-vivo significance is disputed.

For the fly protein, catalysis is entirely inferential. Mourikis et al. 2006 ([PMID: 16434470](https://pubmed.ncbi.nlm.nih.gov/16434470/); gene then named *Enigma*) describe "**a mitochondrial protein with homology to enzymes of the beta-oxidation of fatty acids and that mutations in this locus affect lipid homeostasis**" — homology-based, with lifespan-extension, oxidative-stress-resistance, and lipid-homeostasis phenotypes, not a demonstrated dehydrogenase assay. Murari et al. 2021 ([PMID: 34386730](https://pubmed.ncbi.nlm.nih.gov/34386730/)) address complex-I biogenesis. **No direct acyl-CoA dehydrogenase enzyme assay exists for Egm**, and certainly none demonstrating medium-chain specificity.

### Finding 3 — Egm lacks the canonical ACAD catalytic proton-acceptor glutamate

The ACAD mechanism requires a catalytic base glutamate that abstracts the α-proton. UniProt annotates this proton acceptor at ACAD9 Glu426, VLCAD Glu462, and MCAD Glu401. **Egm (Q5U117) has NO annotated active site.** A register-anchored, ungapped alignment of the conserved catalytic "F-E-G-T…IALTGL" motif — anchored by the invariant C-terminal "IALTGL" block and the upstream "RD" motif — places the catalytic-Glu column on a **glycine** in Egm:

```
ACAD9  PYERILRDTRILLIF[E]GTNEILRMYIALTGL   catalytic Glu426
VLCAD  GVERVLRDLRIFRIF[E]GTNDILRLFVALQGC   catalytic Glu462
Egm    TTELGLRDAAQLCTQ[G]ESLDTLGMFIALTGL   Gly446 at catalytic column
```

The Egm residue at the catalytic column is **Gly446**; a glutamate sits one position C-terminal (Egm447), but that column corresponds to the ACAD post-catalytic glycine, not the catalytic base. Conserved substrate/FAD-contacting residues *are* retained in Egm (D394 = MCAD D278; R408 = MCAD R281), so the flavoprotein pocket is partly intact, but substitution of the proton-acceptor glutamate by glycine means even *generic* dehydrogenase catalysis is not structurally guaranteed. (This is a computational inference from register-anchored alignment, not a structural assay; the ACAD catalytic base can migrate between subfamilies, so an AlphaFold/experimental active-site superposition would be needed to be definitive.)

### Finding 4 — Domain and PANTHER v19 provenance place Egm in the ACAD9/ACADV subfamily with only generic GO

Live InterPro for Q5U117 assigns the ACAD9/VLCAD-specific domains **PF21343 "ACAD9/ACADV, C-terminal domain"** and **IPR049448 "ACAD9/ACADV-like, C-terminal domain,"** alongside the generic ACAD domains PF00441/PF02770/PF02771 — and **no medium-chain (MCAD)-specific signature**. The live PANTHER geneinfo service (product version 19) maps Q5U117 to family PTHR48083, subfamily **PTHR48083:SF2**, with GO-slim MF **GO:0016627 "oxidoreductase activity, acting on the CH-CH group of donors,"** BP **GO:0006635 "fatty acid beta-oxidation,"** and CC **GO:0005737 "cytoplasm"** — **none medium-chain-specific**. InterPro still lists the legacy family PTHR43884 for the same protein, but the served v19 node does not carry GO:0070991 or GO:0051793. This directly matches the seed's observation that the PAINT TSV places the medium-chain terms at PTN000098033 while the served PTHR43884 v19 tree lacks that node and the exact Egm leaf — i.e., the medium-chain IBA annotations cannot be re-derived from the tree node actually served today.

---

## Mechanistic Model / Interpretation

The evidence supports a model in which Egm is a **dual-clade ACAD9-type protein whose demonstrable core function is mitochondrial complex-I assembly**, with any fatty-acid-oxidation role being ancestral, long/very-long-chain-biased, and unproven in the fly.

```
                     Egm / dACAD9 (Q5U117, CG9006)
                                |
          ┌─────────────────────┴──────────────────────┐
          |                                             |
   WELL-EVIDENCED CORE                        INFERRED / CONTESTED
   Complex-I assembly (MCIA)                  FAO catalytic activity
   - UniProt: "Complex I assembly            - ortholog optimum = LONG-chain
     factor Egm, mitochondrial"                unsaturated (PMID16020546)
   - fly complex-I biogenesis                - residual FAO "controversial"
     (PMID34386730)                            (PMID25721401)
   - human ACAD9 = 1 of 14 CI                - catalytic Glu -> Gly446
     assembly factors (PMID34556413)           (no annotated active site)
   GO:0032981 / MCIA CC GO:0160295           - NO direct fly assay
                                             - MEDIUM-chain = orthology-
                                               contradicted, IBA-only
```

Assessing the two axes separately, as the seed requests, sharpens rather than rescues the medium-chain call. On the **molecular-function** axis, three of the four evidence lines specifically undermine *medium-chain* specificity: identity is closest to the long/very-long-chain clade; the ortholog's measured optimum is long-chain unsaturated; and the catalytic base is degenerate. On the **biological-process** axis, the only fly phenotypes (lifespan, oxidative-stress response, lipid homeostasis) are consistent with a complex-I/OXPHOS defect and general lipid dysregulation, not with a specific block in medium-chain fatty acid catabolism. The dual-function biology of ACAD9 orthologs (Schiff 2015; the mouse model PMID: 34556413 describing "a combined defect in fatty acid oxidation and oxidative phosphorylation due to a dual role") means assembly and FAO functions genuinely coexist in the family — but the FAO half, where it operates, is long-chain.

Crucially, this interpretation does **not** treat the assembly role or the absence of fly assays as negative evidence against catalysis. The claim is narrower and more defensible: the *specific* medium-chain terms are (i) not supported by any direct fly experiment, (ii) contradicted in direction by the closest experimental ortholog, and (iii) untraceable to the currently served phylogenetic node that supposedly justifies them.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 16020546](https://pubmed.ncbi.nlm.nih.gov/16020546/) Ensenauer 2005 | Direct enzyme assay | **Qualifies / partially refutes** medium-chain specificity | ACAD9 substrate preference | Purified mature ACAD9 had **maximal activity with long-chain unsaturated acyl-CoAs (C16:1, C18:1, C18:2, C22:6)** | Human ACAD9, recombinant, in vitro | High for optimum = long-chain; abstract doesn't itemize C6–C12; in-vitro only |
| [PMID: 25721401](https://pubmed.ncbi.nlm.nih.gov/25721401/) Schiff 2015 (= PMC4424958, verified) | Knockout + patient correlation | **Qualifies** | Does ACAD9 FAO activity matter in vivo? | "retains ACAD activity for **long-chain** fatty acids in vitro, but the biological relevance… remains controversial"; residual activity inversely correlates with severity | Human HEK293 KO; 24 patients | Activity is long-chain, tissue-specific, "controversial" |
| [PMID: 34556413](https://pubmed.ncbi.nlm.nih.gov/34556413/) mouse *Acad9* | Genetic model | **Qualifies** | Dual role of ACAD9 | FAO role **and** second role as one of 14 CI assembly factors; total KO lethal; "considerable controversy remains over the relative role of these two functions" | Mouse tissue-specific KO | Confirms dual-function framing; unresolved primacy |
| [PMID: 34386730](https://pubmed.ncbi.nlm.nih.gov/34386730/) Murari 2021 | Fly genetics | **Supports** assembly (not catalysis) | Egm role in CI biogenesis | *Drosophila* complex-I assembly-factor / modular CI biogenesis | *Drosophila* in vivo | Supports assembly; does not assay dehydrogenase activity |
| [PMID: 16434470](https://pubmed.ncbi.nlm.nih.gov/16434470/) Mourikis 2006 | Mutant phenotype (homology naming) | **Qualifies (indirect)** | Egm/Enigma in lipid metabolism | *Enigma* = mitochondrial protein **with homology to β-oxidation enzymes**; mutations **affect lipid homeostasis**, extend lifespan, confer oxidative-stress resistance | *Drosophila* mutants | Homology-based; phenotypes equally consistent with OXPHOS/CI loss; no enzyme assay |
| [PMID: 28070495](https://pubmed.ncbi.nlm.nih.gov/28070495/) case report | Review/database | **Qualifies** | ACAD9 substrate scope | "implicated in the processing of palmitoyl-CoA and long-chain unsaturated substrates" | Human clinical | Review-level; long-chain framing |
| UniProt Q5U117 GO set (this run) | Database annotation | **Qualifies** | Current annotation status | Medium-chain terms are **IBA**; experimental-grade Egm terms are localization/assembly (MCIA IDA, matrix IDA); VLCAD term is **ISS** | Database | Medium-chain terms are phylogenetic only |
| Sequence identity (this run, NW) | Computational / evolutionary | **Refutes** medium-chain clade membership | Which ACAD subfamily is Egm? | ACAD9 37.2%, VLCAD 36.9%, SCAD 29.3%, **MCAD 28.0%**, LCAD 27.5% | In silico vs human paralogs | Egm ∈ ACAD9/VLCAD clade, ~9 pts from MCAD; ±1 scoring, rank order robust |
| Catalytic-residue mapping (this run) | Computational / structural-evolutionary | **Qualifies (weakens catalysis)** | Does Egm retain the ACAD catalytic base? | Proton-acceptor Glu (ACAD9 Glu426 / VLCAD Glu462) maps onto **Egm Gly446**; no annotated active site; substrate residues D394/R408 conserved | In silico | Register reliable (anchored by IALTGL + RD); catalytic base can migrate — needs structure |
| InterPro (live, this run) | Computational / database | **Refutes** medium-chain specificity | Which subfamily signatures does Egm carry? | **PF21343 / IPR049448 "ACAD9/ACADV C-terminal"** + generic ACAD domains; **no MCAD signature** | Domain models on Q5U117 | Domain-level corroboration |
| PANTHER v19 geneinfo (live, this run) | Computational / database | **Qualifies (provenance break)** | Trace PTN000098033 / PTHR43884 v19 | Served v19 maps Q5U117 to **PTHR48083:SF2** with GO:0016627 / GO:0006635 / GO:0005737 — **no medium-chain term** | PANTHERdb service, v19 | Confirms seed's flag; medium-chain IBA untraceable to served node |

---

## GO Curation Implications (leads — require curator verification)

**Molecular Function**
- **GO:0070991 "medium-chain acyl-CoA dehydrogenase activity" [IBA] on Egm — recommend REMOVE or REPLACE.** It is (a) IBA-only, (b) specificity-mismatched to Egm's ACAD9/VLCAD clade, and (c) not the optimum even for the human ortholog. If a substrate-resolved MF is desired, **generalize to GO:0003995 (acyl-CoA dehydrogenase activity)** or align to the clade with **GO:0004466 (long-chain)** / **GO:0017099 (very-long-chain)**. Given the degenerate catalytic base, treat any MF as **non-core / uncertain**.
- Retaining **GO:0050660 (FAD binding, IEA)** is fine; it reflects an intact flavoprotein fold consistent with either catalytic or scaffold roles.
- **Do not** downgrade to "protein binding"; the informative MF is the assembly-relevant **GO:0030674 (protein-macromolecule adaptor activity, ISS)** or a generalized ACAD term.

**Biological Process**
- **GO:0051793 "medium-chain fatty acid catabolic process" [IBA] — recommend generalize/remove.** If kept, generalize to **GO:0006635 (fatty acid beta-oxidation)**, which already has IMP support in fly, and treat as non-core.
- **GO:0032981 "mitochondrial respiratory chain complex I assembly" — retain as core BP** (TAS + fly genetics + MCIA localization).

**Cellular Component**
- Retain **GO:0160295 (MCIA complex)** and **GO:0005759 (mitochondrial matrix)** — IDA-grade, core.

### GO decision table (leads — require curator verification)

| GO term | Aspect | Current evidence on Egm | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0070991 medium-chain acyl-CoA dehydrogenase activity | MF | IBA (GO_Central) | **Remove or replace** → GO:0003995 (generic) or GO:0004466/GO:0017099 (long/VLC) | Wrong subfamily; ortholog optimum long-chain; catalytic Glu degenerate; PANTHER v19 node lacks term |
| GO:0051793 medium-chain fatty acid catabolic process | BP | IBA (GO_Central) | **Remove or generalize** → GO:0006635 (β-oxidation) | Same provenance/specificity issues; fly β-oxidation IMP covers generic BP |
| GO:0017099 very-long-chain acyl-CoA dehydrogenase activity | MF | ISS (FlyBase, from ACAD9) | **Retain as non-core / candidate**, flag catalytic-Glu caveat | Matches subfamily but no fly assay; catalytic base uncertain |
| GO:0003995 acyl-CoA dehydrogenase activity | MF | (parent) | **Candidate generic replacement** | Defensible fold-level activity if any MF is kept |
| GO:0050660 FAD binding | MF | IEA (InterPro) | **Retain** | Intact flavoprotein fold |
| GO:0032981 mito. respiratory chain complex I assembly | BP | TAS (FlyBase) + fly genetics | **Retain — core** | Best-evidenced function |
| GO:0160295 MCIA complex | CC | IDA (FlyBase) | **Retain — core** | Direct localization |
| GO:0005759 mitochondrial matrix | CC | IDA (FlyBase) | **Retain** | Direct localization |

**Net:** the assembly branch is core and well-supported; the medium-chain catalysis/catabolism branch is a phylogenetic carry-over that should be **non-core and either generalized or removed**, not retained at "medium-chain" specificity.

---

## Mechanistic Scope

The **immediate molecular function** being tested is FAD-dependent α,β-dehydrogenation of a medium-chain (C6–C12) fatty acyl-CoA to the 2-enoyl-CoA. Direct evidence for this specific reaction on Egm is **absent** (no fly assay). Nearest evidence = human ACAD9 in vitro, which favors **long-chain unsaturated** substrates. The catalytic base appears substituted (Gly446), further weakening a direct-catalysis interpretation.

The **assembly function** — chaperoning complex-I module assembly within the MCIA complex — is a distinct molecular activity (protein–protein scaffolding, not catalysis) and is the better-supported core. Downstream/derived observations that must **not** be conflated with the direct medium-chain claim include: fly lipid-homeostasis, lifespan extension, and oxidative-stress resistance (PMID: 16434470), all confounded by Egm's OXPHOS/complex-I role; human disease manifestations (cardiomyopathy, lactic acidosis) driven substantially by the assembly defect; and any inference drawn purely from loss of function, which cannot by itself localize activity to medium-chain substrates.

---

## Conflicts and Alternatives

1. **Specificity mismatch (clade/paralog confusion).** The "medium-chain" label properly belongs to **ACADM/MCAD**, a distinct subfamily (28% identity to Egm). Egm sits with **ACAD9/VLCAD**. Propagating MCAD's flagship term across the whole PTHR family is classic **paralog over-annotation / frequency bias**.
2. **In-vitro-only, controversial activity.** Even in human, ACAD9's FAO activity is "controversial" and tissue-specific (Schiff 2015; mouse model 2021). A physiological medium-chain catabolism claim for the fly is doubly indirect.
3. **Assembly vs. catalysis primacy.** UniProt/FlyBase both name the protein an **assembly factor first**. The seed correctly warns not to treat the assembly role as negative evidence for catalysis — but the converse also holds: the lipid phenotypes are not positive evidence for *direct* catalysis.
4. **Ancestral-node provenance break (PTN000098033) — partially confirmed.** The seed flags that the PAINT TSV places both medium-chain terms at PTN000098033 while the served PTHR43884 v19 tree lacks that node/leaf. Live checks corroborate a mismatch: PANTHER v19 geneinfo maps Egm to **PTHR48083:SF2** (different family than the InterPro-listed legacy PTHR43884), and that node carries only generic GO:0016627 and GO:0006635, **not** the medium-chain terms. No lineage was invented from the donor list; a curator should confirm against the authoritative PAINT export.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No direct Egm enzyme assay (for or against any substrate) | Literature + UniProt evidence codes | Determines whether Egm is a genuine dehydrogenase or a catalytically-degenerate assembly scaffold; the medium-chain claim cannot be confirmed or definitively refuted in the fly (hence "over-annotated," not "refuted") | Recombinant Egm ETF-linked ACAD assay across C4–C18 acyl-CoAs |
| Catalytic-base glutamate conservation in Egm | Partially resolved: register-anchored motif alignment maps ACAD9 Glu426 / VLCAD Glu462 onto **Egm Gly446** | Presence/absence of the catalytic Glu discriminates active enzyme vs. pseudo-enzyme | AlphaFold/experimental structure superposition to test whether a Glu from another element rescues the site (catalytic-base migration) |
| Chain-length values for human ACAD9 on C6–C12 | Abstracts only (optimum = long-chain) | Seed claims "broad substrate use"; magnitude of medium-chain activity sets the ceiling for any transfer | Read full Ensenauer 2005 substrate table |
| PTN000098033 phylogenetic support | Partially resolved: PANTHER v19 maps Egm to PTHR48083:SF2 with only generic GO; served node lacks the medium-chain terms | Retaining an IBA term requires a valid, current ancestral node | Curator to confirm against the authoritative PAINT export whether GO:0070991/GO:0051793 still resolve to a live v19 node for Egm |
| Global identity does not fix substrate specificity | NW ranking computed | Clade placement is necessary but not sufficient for substrate specificity | Direct assay (above) |

---

## Discriminating Tests / Proposed Follow-up Experiments

1. **Recombinant Egm ACAD assay** (ETF/DCPIP-coupled) across a C4–C18 acyl-CoA panel — directly tests whether Egm is catalytic and, if so, its chain-length optimum. *Prediction under seed:* measurable C6–C12 activity; *prediction under alternative:* negligible activity or long-chain optimum.
2. **Active-site residue audit / structure** — align Egm to MCAD/VLCAD/ACAD9 and test the catalytic base Glu and FAD-contacting residues; AlphaFold pocket geometry as a chain-length ruler. Loss of the catalytic Glu → assembly-scaffold (pseudo-enzyme) interpretation.
3. **Separation-of-function rescue** — express in *Egm*-null flies a catalytically-dead but assembly-competent Egm variant; if lipid/β-oxidation phenotypes persist while complex I is restored, catalysis is dispensable (phenotypes were OXPHOS-driven).
4. **Acylcarnitine profiling of *Egm* mutants** — a medium-chain acylcarnitine elevation (C6–C10) would support genuine medium-chain flux; a generalized/long-chain pattern or a pure OXPHOS signature would not.
5. **Cross-clade complementation** — test whether human ACAD9 (long-chain/assembly) but not human MCAD rescues *Egm* phenotypes — cross-clade rescue confirms functional orthology to ACAD9, not MCAD.
6. **Provenance audit** — re-map Egm through the exact GO/PANTHER release cited in the IBA annotation to confirm whether PTN000098033 legitimately carries the medium-chain terms for the Egm leaf.

---

## Curation Leads (require curator verification)

- **Action lead:** On Q5U117, treat **GO:0070991 [IBA]** and **GO:0051793 [IBA]** as **over-specified phylogenetic carry-over**; recommend **generalize** (to GO:0003995 / GO:0006635) or **remove**, pending PTN000098033 re-verification. Keep the **complex-I assembly** branch (GO:0032981, GO:0160295) as core.
- **Reference/snippet leads to verify:**
  - [PMID: 16020546](https://pubmed.ncbi.nlm.nih.gov/16020546/) — "Purified mature ACAD-9 had maximal activity with long-chain unsaturated acyl-CoAs as substrates (C16:1-, C18:1-, C18:2-, C22:6-CoA)."
  - [PMID: 25721401](https://pubmed.ncbi.nlm.nih.gov/25721401/) (PMC4424958, verified) — "ACAD9 also retains enzyme ACAD activity for long-chain fatty acids in vitro, but the biological relevance of this function remains controversial."
  - [PMID: 16434470](https://pubmed.ncbi.nlm.nih.gov/16434470/) — "Enigma encodes a mitochondrial protein with homology to enzymes of the beta-oxidation of fatty acids and that mutations in this locus affect lipid homeostasis."
  - [PMID: 34386730](https://pubmed.ncbi.nlm.nih.gov/34386730/) — fly complex-I biogenesis genetics (supports assembly, not catalysis).
- **Candidate replacement MF terms:** GO:0004466 (long-chain) or GO:0017099 (very-long-chain), matching Egm's ACAD9/VLCAD clade, or the parent GO:0003995 — **not** GO:0070991.
- **Suggested curator questions:** (a) Is there any direct *Drosophila* acyl-CoA dehydrogenase assay for Egm? (b) Does the served PTHR43884 v19 tree actually support PTN000098033 for these terms? (c) Should substrate-resolved MF terms be demoted to non-core given the primacy of the assembly role?

---

## Computational Provenance (this run)

- **Needleman-Wunsch global identity, Egm (Q5U117, 639 aa) vs human paralogs (UniProt FASTA, match=+1/mismatch=−1/gap=−1):** ACAD9 (Q9H845) **37.2%**, VLCAD (P49748) **36.9%**, SCAD (P16219) 29.3%, MCAD (P11310) **28.0%**, LCAD (P28330) 27.5%. → Egm ∈ ACAD9/VLCAD clade, not MCAD clade.
- **GO label resolution (QuickGO):** GO:0070991 = *medium-chain fatty acyl-CoA dehydrogenase activity* (MF); GO:0004466 = *long-chain…*; GO:0017099 = *very-long-chain…*; GO:0032981 = *mitochondrial respiratory chain complex I assembly* (BP).
- **UniProt GO evidence codes** pulled live for Q5U117/Q9H845/P11310/P49748/P28330 (see Evidence Matrix).
- **Catalytic-residue mapping:** UniProt "Proton acceptor" active sites = ACAD9 Glu426, VLCAD Glu462, MCAD Glu401; Egm has **none** annotated. Register-anchored ungapped alignment of the catalytic motif window (anchored by invariant C-terminal `IALTGL` and upstream `RD`) maps the catalytic Glu of ACAD9/VLCAD onto **Egm Gly446** (nearest Glu one residue off-register at Egm447). Conserved substrate/FAD residues in Egm: D394 (=MCAD D278), R408 (=MCAD R281).
- **InterPro (live):** Egm carries PF21343 / IPR049448 "ACAD9/ACADV C-terminal domain" plus generic ACAD domains; no MCAD-specific signature.
- **PANTHER v19 geneinfo (live):** Q5U117 → PTHR48083:SF2 with GO-slim MF GO:0016627, BP GO:0006635, CC GO:0005737; no medium-chain term.

*Limitations:* identities from a simple ±1 scoring NW (not BLOSUM), so absolute values are approximate but the rank order (ACAD9 ≈ VLCAD > SCAD/MCAD/LCAD) is robust. No direct fly enzyme data exist to test; the catalytic-base finding is an alignment inference pending structural confirmation; the PTHR43884 v19 / PTN000098033 discrepancy could not be fully reconstructed programmatically and is reported as an open provenance gap rather than resolved.

---

## Bottom Line

Egm/dACAD9 (Q5U117) is an **ACAD9/VLCAD-clade complex-I assembly factor**. Its well-supported core function is **mitochondrial complex-I assembly**; any fatty-acid-oxidation activity is ancestral, **long/very-long-chain-biased**, contested even in the human ortholog, and structurally uncertain in the fly (degenerate catalytic base). The seed's **medium-chain** MF (GO:0070991) and BP (GO:0051793) terms are **IBA-only, orthology-contradicted, and untraceable to the served phylogenetic node** — they should be removed or generalized/re-anchored to long/very-long-chain and treated as non-core. This judgment does not treat the assembly role or the absence of fly assays as positive evidence against catalysis; it finds no support for the *specific* medium-chain claim.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)