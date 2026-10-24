---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T01:58:03.304386'
end_time: '2026-09-21T02:23:21.727026'
duration_seconds: 1518.42
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: AKR1D1
  gene_symbol: AKR1D1
  uniprot_accession: P51857
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: aldose-monooxygenase-and-alcohol-reduction-specificity
  hypothesis_text: Human AKR1D1 (P51857) retains aldose-reductase, ketosteroid-monooxygenase
    and alcohol/17beta-hydroxysteroid-dehydrogenase capacities in addition to its
    established Delta4-3-ketosteroid 5beta-reduction. Evaluate exact reaction chemistry,
    direct product identification and source-specific context. Current PTHR11732 leaf
    PTN002482523 descends from PTN000198921 (aldose reductase) and PTN000199026 (ketosteroid
    monooxygenase); GO0047086 requires O2/NADPH and progesterone conversion to testosterone
    acetate. Descendant AKR1C1/C2/C3 IDA sources all trace to PMID21232532, whose
    full text must be read. PMID18407998 provides Glu120-dependent C5 hydride-transfer
    structure, not a blanket exclusion of additional chemistry. PMID11342103 underlies
    UniProt RHEA53484 17-keto-to-17beta-hydroxy conversion; assess whether the product/position
    and intact-cell background support intrinsic 17beta-HSD activity or reflect a
    different steroid transformation. Distinguish this from Reactome alcohol-dehydrogenase
    labels for actual Delta4-double-bond reductions. Full PMID21255593 demonstrates
    broad C18-C27 steroid reduction and discusses substrate inhibition resolving older
    negative assays (PMID7508385). Do not infer loss of ancestral aldose or other
    capacity from predominant steroid use or target assay absence alone.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/AKR1D1/AKR1D1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human AKR1D1 (P51857) retains aldose-reductase,\
    \ ketosteroid-monooxygenase and alcohol/17beta-hydroxysteroid-dehydrogenase\n\
    \  capacities in addition to its established Delta4-3-ketosteroid 5beta-reduction.\
    \ Evaluate exact reaction\n  chemistry, direct product identification and source-specific\
    \ context. Current PTHR11732 leaf PTN002482523\n  descends from PTN000198921 (aldose\
    \ reductase) and PTN000199026 (ketosteroid monooxygenase); GO0047086\n  requires\
    \ O2/NADPH and progesterone conversion to testosterone acetate. Descendant AKR1C1/C2/C3\
    \ IDA sources\n  all trace to PMID21232532, whose full text must be read. PMID18407998\
    \ provides Glu120-dependent C5 hydride-transfer\n  structure, not a blanket exclusion\
    \ of additional chemistry. PMID11342103 underlies UniProt RHEA53484\n  17-keto-to-17beta-hydroxy\
    \ conversion; assess whether the product/position and intact-cell background\n\
    \  support intrinsic 17beta-HSD activity or reflect a different steroid transformation.\
    \ Distinguish this\n  from Reactome alcohol-dehydrogenase labels for actual Delta4-double-bond\
    \ reductions. Full PMID21255593\n  demonstrates broad C18-C27 steroid reduction\
    \ and discusses substrate inhibition resolving older negative\n  assays (PMID7508385).\
    \ Do not infer loss of ancestral aldose or other capacity from predominant steroid\n\
    \  use or target assay absence alone.\nfocus_type: function_assignment\ncontext:\
    \ []\nreference_id: []"
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
- **Gene directory:** AKR1D1
- **Gene symbol:** AKR1D1
- **UniProt accession:** P51857

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** aldose-monooxygenase-and-alcohol-reduction-specificity
- **Source file:** genes/human/AKR1D1/AKR1D1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human AKR1D1 (P51857) retains aldose-reductase, ketosteroid-monooxygenase and alcohol/17beta-hydroxysteroid-dehydrogenase capacities in addition to its established Delta4-3-ketosteroid 5beta-reduction. Evaluate exact reaction chemistry, direct product identification and source-specific context. Current PTHR11732 leaf PTN002482523 descends from PTN000198921 (aldose reductase) and PTN000199026 (ketosteroid monooxygenase); GO0047086 requires O2/NADPH and progesterone conversion to testosterone acetate. Descendant AKR1C1/C2/C3 IDA sources all trace to PMID21232532, whose full text must be read. PMID18407998 provides Glu120-dependent C5 hydride-transfer structure, not a blanket exclusion of additional chemistry. PMID11342103 underlies UniProt RHEA53484 17-keto-to-17beta-hydroxy conversion; assess whether the product/position and intact-cell background support intrinsic 17beta-HSD activity or reflect a different steroid transformation. Distinguish this from Reactome alcohol-dehydrogenase labels for actual Delta4-double-bond reductions. Full PMID21255593 demonstrates broad C18-C27 steroid reduction and discusses substrate inhibition resolving older negative assays (PMID7508385). Do not infer loss of ancestral aldose or other capacity from predominant steroid use or target assay absence alone.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human AKR1D1 (P51857) retains aldose-reductase, ketosteroid-monooxygenase and alcohol/17beta-hydroxysteroid-dehydrogenase
  capacities in addition to its established Delta4-3-ketosteroid 5beta-reduction. Evaluate exact reaction
  chemistry, direct product identification and source-specific context. Current PTHR11732 leaf PTN002482523
  descends from PTN000198921 (aldose reductase) and PTN000199026 (ketosteroid monooxygenase); GO0047086
  requires O2/NADPH and progesterone conversion to testosterone acetate. Descendant AKR1C1/C2/C3 IDA sources
  all trace to PMID21232532, whose full text must be read. PMID18407998 provides Glu120-dependent C5 hydride-transfer
  structure, not a blanket exclusion of additional chemistry. PMID11342103 underlies UniProt RHEA53484
  17-keto-to-17beta-hydroxy conversion; assess whether the product/position and intact-cell background
  support intrinsic 17beta-HSD activity or reflect a different steroid transformation. Distinguish this
  from Reactome alcohol-dehydrogenase labels for actual Delta4-double-bond reductions. Full PMID21255593
  demonstrates broad C18-C27 steroid reduction and discusses substrate inhibition resolving older negative
  assays (PMID7508385). Do not infer loss of ancestral aldose or other capacity from predominant steroid
  use or target assay absence alone.
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

# AKR1D1 (P51857) Function-Assignment Review: Does It Retain Aldose-Reductase, Ketosteroid-Monooxygenase, and Alcohol/17β-HSD Capacities?

**Gene:** AKR1D1 (steroid 5β-reductase / aldo-keto reductase family 1 member D1)
**Organism:** *Homo sapiens* (NCBITaxon:9606) · **UniProt:** P51857
**Focus type:** function_assignment · **Hypothesis slug:** aldose-monooxygenase-and-alcohol-reduction-specificity

---

## Summary

The seed hypothesis is **partially supported but over-annotated on the accessory activities.** It is **correct on its core claim and on substrate breadth**: AKR1D1's directly-supported molecular function is Δ4-3-oxosteroid (Δ4-3-ketosteroid) **5β-reductase** (EC 1.3.1.3, GO:0047787), and it does reduce a broad C18–C27 range of Δ4-3-ketosteroids. Direct homogeneous-enzyme kinetics establish this, and the seed's secondary point — that earlier negative/conflicting assays are explained by **substrate inhibition** rather than absence of activity — is well founded.

However, the seed's central proposition — that AKR1D1 **"retains"** ancestral aldose-reductase, ketosteroid-monooxygenase, and alcohol/17β-HSD capacities *in addition to* its 5β-reductase activity — is **not supported by direct evidence and is contradicted by structure–mechanism reasoning.** These accessory GO terms rest on weak provenance: phylogenetic inference (IBA:GO_Central), a single reaction-record electronic annotation (IEA:RHEA), a reaction-class mislabel from Reactome (TAS), or a paralog expression study that does not even assay AKR1D1. Critically, AKR1D1 carries a **His→Glu120 substitution** at the position occupied by the catalytic histidine of every general carbonyl-reducing AKR (including aldose reductase). Glu120 is the residue AKR1D1 *requires* for its unique β-face hydride transfer to the Δ4 C=C double bond, and it mechanistically **disfavors** the carbonyl↔alcohol chemistry that aldose reductase, alcohol dehydrogenase, and 17β-HSD demand. Ketosteroid monooxygenase is chemically impossible for an NADPH oxidoreductase, since it requires O₂-dependent Baeyer–Villiger oxygenation.

The appropriate curation posture is therefore to **retain the core 5β-reductase MF** and to **flag the accessory terms for removal, NOT-qualification, or downgrade to non-core**, pending curator verification. The seed's methodological warning — "do not infer loss of ancestral capacity from predominant steroid use or target-assay absence alone" — is valid, but here the evidence is not merely *absence of assay*; it is a **positive mechanistic reason** (the catalytic-His replacement) plus **traceable database carry-over** for each accessory term.

---

## Executive Judgment

**Verdict: Partially supported — over-annotated on aldose-reductase, ketosteroid-monooxygenase, alcohol-dehydrogenase, and 17β-HSD; core 5β-reductase strongly supported.**

The single most important structural fact is that AKR1D1 has repurposed the AKR catalytic histidine into Glu120, which is essential for its double-bond reduction chemistry but incompatible with efficient aldehyde/ketone carbonyl reduction. Every accessory annotation either requires that lost carbonyl chemistry (aldose reductase, alcohol dehydrogenase, 17β-HSD) or requires oxygenase chemistry an AKR cannot perform (ketosteroid monooxygenase). The provenance for each accessory term is weak, and the AKR1C IDA source the seed relies on assays the paralogs, not AKR1D1.

**Most important caveat:** No study has directly assayed purified AKR1D1 against canonical aldose or monooxygenase substrates and formally reported a null. The exclusion is inferred from structure, sequence, and GO/reaction definitions — a strong but not airtight basis. The one accessory term that most warrants a full-text re-read before a hard NOT is 17β-HSD (RHEA:53484, from PMID11342103), because its intact-cell background could mask whether the observed 17β-hydroxy product reflects intrinsic AKR1D1 activity.

---

## Key Findings

### F001 — The His→Glu120 substitution mechanistically disfavors general carbonyl reduction

The aldo-keto reductase (AKR) superfamily performs carbonyl reduction using a conserved catalytic tetrad of **Asp–Tyr–Lys–His**. In AKR1D1, UniProt P51857 confirms that Asp53, Tyr58, and Lys87 are present, but the conserved catalytic **histidine is replaced by glutamate at position 120** (residue 120 = E in AKR1D1, whereas the aligned His117 = H in the paralog AKR1C2). This single substitution is not incidental: it is the molecular basis of AKR1D1's distinct chemistry.

Di Costanzo, Drury, Penning & Christianson (2008; [PMID: 18407998](https://pubmed.ncbi.nlm.nih.gov/18407998/)) solved the crystal structure and demonstrated that the catalytic dyad is **Tyr58 + Glu120**, and that both **Y58F and E120A mutants are devoid of activity**. Glu120 enables β-face hydride transfer onto the Δ4 C=C double bond via an enolate intermediate — a reaction chemistry that is *unique* among AKRs and fundamentally different from reducing a free aldehyde or ketone carbonyl. The verified quote:

> "Each steroid carbonyl accepts hydrogen bonds from catalytic residues Tyr(58) and Glu(120). The Y58F and E120A mutants are devoid of activity, supporting a role for this dyad in the catalytic mechanism."

This is the linchpin structural argument: the residue the seed hypothesis would need to invoke for general carbonyl chemistry (the catalytic His) has been repurposed into the residue (Glu120) that makes AKR1D1 a double-bond reductase. The seed correctly notes that PMID18407998 is "not a blanket exclusion of additional chemistry" — a single active-site study cannot exhaustively rule out trace promiscuous side reactions. But it does establish a *positive* mechanistic reason to doubt efficient aldose/ketone carbonyl reduction, which is stronger than mere silence.

### F002 — Core 5β-reductase function is robustly supported across broad substrates; multifunctional labels rest on weak/indirect evidence

Chen, Drury & Penning (2011; [PMID: 21255593](https://pubmed.ncbi.nlm.nih.gov/21255593/)) used **homogeneous (purified) enzyme** to show that AKR1D1 reduces all C18, C19, C21, and C27 Δ4-3-ketosteroids tested at physiological pH. Crucially, they observed **substrate inhibition** with C18–C21 steroids when the C11 position is unsubstituted, explaining why earlier assays (e.g., Kondo et al. 1994, [PMID: 7508385](https://pubmed.ncbi.nlm.nih.gov/7508385/)) sometimes reported weak or negative activity for particular substrates. The verified quote:

> "AKR1D1 proficiently reduced all the steroids tested at physiological pH, indicating AKR1D1 is the only enzyme necessary for all the 5β-steroid metabolites present in humans. Substrate inhibition was observed with C18 to C21 steroids provided that the C11 position was unsubstituted."

The physiological centrality of this activity is independently confirmed by human disease genetics: biallelic loss-of-function variants cause **Congenital Bile Acid Synthesis defect type 2 (CBAS2)**, presenting with neonatal cholestasis, coagulopathy, and failure to thrive ([PMID: 41387259](https://pubmed.ncbi.nlm.nih.gov/41387259/); [PMID: 26418565](https://pubmed.ncbi.nlm.nih.gov/26418565/), the P133R mutation). These confirm that the Δ4-3-ketosteroid 5β-reduction step in bile-acid synthesis is AKR1D1's essential in-vivo role.

By contrast, each accessory annotation has thin provenance: **17β-HSD (GO:0072582)** is only IEA:RHEA from a single reaction record (RHEA:53484); **alcohol dehydrogenase, NADP+ (GO:0008106)** is only TAS:Reactome; **aldose reductase (GO:0004032)** and **ketosteroid monooxygenase (GO:0047086)** are only IBA:GO_Central (phylogenetic inference).

The seed asserts that the AKR1C IDA multifunctionality traces to [PMID: 21232532](https://pubmed.ncbi.nlm.nih.gov/21232532/). That paper is an **endometriosis expression study** that assays AKR1C1/AKR1C2/AKR1C3 (the paralogs) — not AKR1D1 — and reports **negligible AKR1D1 mRNA**:

> "significantly increased mRNA levels of AKR1C1, AKR1C2, AKR1C3 and SRD5A1, and negligible mRNA levels of AKR1D1"

An expression study of the paralogs that finds AKR1D1 barely expressed cannot transfer 17β/20α-HSD multifunctionality onto AKR1D1. This is the clearest example of **paralog carry-over** in the annotation set.

### F003 — The Reactome "alcohol dehydrogenase" label maps entirely to Δ4-double-bond reductions, not C-OH oxidation

Querying the Reactome ContentService for UniProt P51857 returns exactly **five reactions** for AKR1D1, all within the three bile-acid synthesis pathways (R-HSA-193368 / 193775 / 193807). Every one of the five (R-HSA-192033, 192067, 193746, 193821, 193824) has the form **"4-cholesten-…-3-one is reduced to 5β-cholestan-…-3-one"** — i.e., the stereospecific reduction of the Δ4 C=C double bond of a 3-oxo bile-acid intermediate to the 5β product. **None is an alcohol (C-OH) oxidation or reduction.**

Therefore the TAS:Reactome GO:0008106 ("alcohol dehydrogenase, NADP+") annotation is a **reaction-class mislabel** applied to the 5β-reductase reaction — not evidence of a distinct alcohol dehydrogenase activity. The seed hypothesis explicitly asked to "distinguish this from Reactome alcohol-dehydrogenase labels for actual Δ4-double-bond reductions," and the Reactome content resolves the question directly in favor of *mislabel*, not *genuine additional activity*.

### F004 — Pairwise alignment confirms AKR1D1 Glu120 occupies the exact position of aldose reductase's catalytic His

A Needleman–Wunsch global alignment of AKR1D1 (P51857) against human aldose reductase AKR1B1 (P15121) gives **52.5% identity** — consistent with the ~50% cited historically (PMID7508385). The catalytic residues co-align cleanly: AKR1D1 Tyr58 ↔ AKR1B1 Tyr49 (the proton donor), Asp53 ↔ Asp44, and Lys87 ↔ Lys78 — all conserved. But at the decisive position, **AKR1D1 Glu120 aligns to AKR1B1 His111**, the catalytic histidine of aldose reductase. The local motif contrast is diagnostic: AKR1B1 "YLI**H**WPT" vs AKR1D1 "YII**E**VPM" — the His→Glu substitution *and* loss of the adjacent Trp (Trp→Val).

This is a direct sequence-level confirmation of the structural argument in F001: the residue aldose reductase uses for aldehyde/aldose carbonyl reduction is precisely the residue AKR1D1 has substituted. It makes the ancestral **aldose reductase (GO:0004032)** activity mechanistically unlikely to be retained at a physiologically meaningful level.

### F005 — GO term definitions confirm the accessory annotations require chemistry AKR1D1 cannot perform

Reading the QuickGO definitions of the accessory terms against AKR1D1's mechanism shows a systematic mismatch:

| GO term | Definition (reaction) | Chemistry required | AKR1D1 capability |
|---|---|---|---|
| GO:0047086 ketosteroid monooxygenase | O₂ + NADPH + progesterone = H₂O + NADP+ + testosterone acetate | **O₂-consuming Baeyer–Villiger monooxygenation** | None — AKR1D1 is an NADPH oxidoreductase, not an oxygenase; chemically impossible |
| GO:0004032 aldose reductase | alditol + NAD(P)+ = aldose + NAD(P)H | Carbonyl↔alcohol using catalytic His | His replaced by Glu120 (F001/F004) |
| GO:0008106 alcohol dehydrogenase (NADP+) | alcohol + NADP+ = aldehyde/ketone + NADPH | Carbonyl↔alcohol using catalytic His | His replaced by Glu120; Reactome reactions all Δ4 reductions (F003) |
| GO:0072582 17β-HSD | 17β-hydroxysteroid + NADP+ = 17-oxosteroid + NADPH | C17 carbonyl↔alcohol redox | His replaced by Glu120; single IEA:RHEA record |
| **GO:0047787 Δ4-3-oxosteroid 5β-reductase (core)** | reduces progesterone, androstenedione, 17α-OH-progesterone, testosterone, bile-acid intermediates | **β-face hydride transfer to Δ4 C=C** | **Yes — established (F002)** |

The **ketosteroid monooxygenase** term is the most decisively excludable: no aldo-keto reductase can perform an O₂-dependent Baeyer–Villiger oxygenation converting progesterone to testosterone acetate. The remaining three accessory terms all require the carbonyl↔alcohol interconversion chemistry that depends on the catalytic His that AKR1D1 has repurposed as Glu120.

---

## Mechanistic Model / Interpretation

The unifying mechanistic story is a **single active-site substitution that redirects catalysis**:

```
   AKR superfamily (general carbonyl reductases, e.g. AKR1B1, AKR1C):
   catalytic tetrad = Asp - Tyr - Lys - HIS
                                        |
                                        +--> protonates/positions substrate CARBONYL
                                             -> aldose reductase, 17b-HSD, alcohol DH chemistry

   AKR1D1 (steroid 5b-reductase):
   catalytic tetrad = Asp53 - Tyr58 - Lys87 - GLU120   (HIS -> GLU)
                                                 |
                                                 +--> enables b-face HYDRIDE transfer to the
                                                      Delta4 C=C double bond (enolate mechanism)
                                                      -> Delta4-3-ketosteroid 5b-reduction ONLY
```

Everything downstream follows from this. AKR1D1 sits near the top of the aldo-keto reductase family tree that also produced the general carbonyl reducers, so **phylogenetic (IBA) pipelines and paralog-based annotation transfer** naturally propose that AKR1D1 "retains" ancestral aldose-reductase and monooxygenase activities. But AKR1D1 is a *specialist* whose defining innovation (Glu120) is chemically incompatible with efficient carbonyl reduction. The five Reactome reactions confirm that in the human bile-acid pathway, AKR1D1 does exactly one kind of chemistry — Δ4→5β reduction of 3-oxo bile-acid intermediates — regardless of whether a given database labels that step "alcohol dehydrogenase" or "5β-reductase."

The seed hypothesis makes a legitimate epistemic point ("do not infer loss from predominant steroid use alone"), and it is correct that absence-of-assay is not proof-of-absence. The resolution is that this case does **not** rest on absence of assay: it rests on (1) a positive structural/mechanistic reason (His→Glu120), (2) sequence-level confirmation that Glu120 sits at aldose reductase's catalytic-His position, (3) GO definitions that demand incompatible chemistry, and (4) traceable database carry-over for every accessory term. That is a stronger basis for down-weighting the accessory activities than "we didn't look."

**Bottom line:** AKR1D1 = Δ4-3-oxosteroid 5β-reductase (specialist). The accessory aldose/monooxygenase/ADH/17β-HSD labels are over-annotations arising from phylogenetic inference, reaction-class mislabels, and paralog confusion — not from demonstrated AKR1D1 activities.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 18407998](https://pubmed.ncbi.nlm.nih.gov/18407998/) | Structural (crystal + mutagenesis) | **Refutes** accessory carbonyl activities; supports core | What is the catalytic dyad; is the catalytic His present? | Catalytic dyad = Tyr58 + Glu120; Y58F and E120A devoid of activity; Glu120 enables β-face hydride transfer to Δ4 C=C | Human liver AKR1D1, recombinant enzyme, X-ray | High. Single-enzyme active-site study; not a formal exclusion of trace promiscuity |
| [PMID: 21255593](https://pubmed.ncbi.nlm.nih.gov/21255593/) | Direct assay (homogeneous enzyme kinetics) | **Supports** core; **qualifies** older negatives | Substrate scope of 5β-reduction; cause of prior negatives | Reduces all C18–C27 Δ4-ketosteroids at physiological pH; substrate inhibition (C11-unsubstituted C18–C21) explains earlier negatives | Purified human AKR1D1 | High for steroid activity; did not assay aldose/monooxygenase substrates directly |
| [PMID: 7508385](https://pubmed.ncbi.nlm.nih.gov/7508385/) | Direct assay (historical) | **Qualifies** | Broad Δ4-3-ketosteroid range; some negatives | Broad steroid substrate range; some negatives later attributed to substrate inhibition | Human, recombinant | Medium; superseded by PMID21255593 on kinetics |
| [PMID: 11342103](https://pubmed.ncbi.nlm.nih.gov/11342103/) | Direct assay (intact-cell context) | **Qualifies/competing** | Basis of RHEA:53484 17-keto→17β-OH | Underlies UniProt IEA:RHEA 17β-HSD annotation; product/position and intact-cell background need scrutiny | Human | Medium; single reaction record; intact-cell background confounds intrinsic-activity claim |
| [PMID: 21232532](https://pubmed.ncbi.nlm.nih.gov/21232532/) | Expression (mRNA) | **Refutes** paralog transfer | Does the cited AKR1C IDA source apply to AKR1D1? | Assays AKR1C1/2/3, not AKR1D1; reports negligible AKR1D1 mRNA | Human endometrium/endometriosis | High that it does NOT support AKR1D1 multifunctionality |
| [PMID: 26418565](https://pubmed.ncbi.nlm.nih.gov/26418565/) | Mutant phenotype + kinetics | **Supports** core physiological role | Is 5β-reduction the essential in-vivo function? | P133R impairs NADPH binding/hydride transfer → bile acid deficiency (CBAS2) | Human recombinant + disease | High |
| [PMID: 41387259](https://pubmed.ncbi.nlm.nih.gov/41387259/) | Mutant phenotype (clinical) | **Supports** core physiological role | Physiological consequence of AKR1D1 loss | Biallelic LOF → CBAS2, near-absent primary bile acids, fatal infant outcome | Human infant, postmortem biochem + genetics | High for physiology; not accessory enzymology |
| Reactome (R-HSA-192033/192067/193746/193821/193824) | Database (pathway) | **Refutes** ADH label as distinct activity | Do "alcohol dehydrogenase" labels denote C-OH chemistry? | All 5 AKR1D1 reactions are Δ4→5β reductions of 3-oxo bile-acid intermediates; none is C-OH oxidation | Human bile-acid synthesis | High; database-level but reaction chemistry explicit |
| QuickGO term definitions | Database (ontology) | **Refutes** accessory MF terms | Do accessory GO defs match AKR1D1 chemistry? | GO:0047086 needs O₂/Baeyer–Villiger; GO:0004032/0008106/0072582 need catalytic-His carbonyl redox | N/A | High for chemical-incompatibility argument |
| UniProt P51857 + AKR1B1 (P15121) alignment | Computational (sequence) | **Refutes** aldose reductase retention | Does Glu120 occupy the aldose-reductase catalytic-His site? | 52.5% identity; Glu120↔His111; Tyr/Asp/Lys conserved; adjacent Trp lost | In silico Needleman–Wunsch | High for positional homology; sequence alone doesn't prove zero activity |

---

## GO Curation Implications

**Core MF term — retain.**
- **GO:0047787** (Δ4-3-oxosteroid 5β-reductase activity, MF) is strongly supported by direct homogeneous-enzyme kinetics (PMID21255593), structure/mechanism (PMID18407998), and disease genetics (PMID26418565, PMID41387259). **Retain as the primary/core molecular function.**
- Associated BP: bile acid biosynthetic process (and steroid metabolic process) is well supported by CBAS2 disease genetics — **retain**.

**Accessory MF terms — flag for curator action (leads requiring verification):**

| GO term | Current evidence | Recommended lead action |
|---|---|---|
| GO:0047086 ketosteroid monooxygenase | IBA:GO_Central | **Remove / NOT** — requires O₂-dependent Baeyer–Villiger oxygenation impossible for an AKR (F005). Highest-confidence removal. |
| GO:0004032 aldose reductase | IBA:GO_Central | **Remove or downgrade to non-core** — catalytic His replaced by Glu120 (F001/F004); ancestral inference only, no AKR1D1 direct assay. |
| GO:0008106 alcohol dehydrogenase (NADP+) | TAS:Reactome | **Remove / re-map** — Reactome reactions are all Δ4→5β reductions, a reaction-class mislabel, not C-OH oxidation (F003). |
| GO:0072582 17β-HSD | IEA:RHEA (RHEA:53484) | **Downgrade to non-core / verify** — single reaction record from PMID11342103 in an intact-cell background; product/position may reflect a different steroid transformation. Treat as uncertain pending re-read. |

**Avoid "protein binding" as a fallback** — a specific, informative MF (GO:0047787) is well supported, so no generic term is needed.

---

## Mechanistic Scope

The immediate molecular function under test is **NADPH-dependent reduction of the Δ4 C=C double bond of 3-oxosteroids to yield 5β-dihydro products** (β-face hydride transfer via an enolate intermediate, gated by Tyr58/Glu120). This is a *direct catalytic activity* of the AKR1D1 gene product.

Distinguished from this direct activity:
- **Downstream pathway consequence:** production of 5β bile-acid intermediates and, ultimately, primary bile acids (cholic/chenodeoxycholic acid). A pathway output, not a separate molecular function.
- **Disease manifestation (loss of function):** CBAS2 — neonatal cholestasis, coagulopathy, failure to thrive, potential fatal outcome. Phenotypes of enzyme deficiency, not evidence of additional enzymatic activities.
- **Inferred/ancestral activities (aldose reductase, ketosteroid monooxygenase):** *evolutionary inferences* transferred from ancestral or paralogous AKRs, not measured AKR1D1 activities.
- **Reaction-class labels (alcohol dehydrogenase):** database annotations attached to the same 5β-reductase reactions, not distinct chemistries.

---

## Conflicts and Alternatives

1. **Paralog confusion (strongest confound).** The seed traces AKR1C1/C2/C3 IDA multifunctionality to PMID21232532, but that paper assays the AKR1C paralogs and reports *negligible AKR1D1 expression*. Any transfer of 17β/20α-HSD activity from AKR1C to AKR1D1 is paralog carry-over, not direct evidence.
2. **Reaction-class mislabel.** The Reactome "alcohol dehydrogenase (NADP+)" descriptor is applied to reactions that are chemically Δ4→5β reductions. A curator reading only the GO label could mistake this for a genuine second activity.
3. **Database carry-over via phylogenetic inference.** GO:0004032 and GO:0047086 are IBA (inferred from biological ancestor). AKR1D1's ancestral position in the AKR tree makes such inference *expected* but not *correct* given the His→Glu120 innovation.
4. **Intact-cell / product-identity ambiguity (17β-HSD).** RHEA:53484 (from PMID11342103) records a 17-keto→17β-hydroxy conversion. In an intact-cell background, the observed product could arise from a coupled activity or paralog rather than intrinsic AKR1D1 17β-HSD chemistry. This one warrants a full-text re-read before any hard NOT call.
5. **The seed's valid counter-argument.** "Do not infer loss from predominant steroid use or target-assay absence alone" is methodologically sound. The rebuttal is that the case rests on *positive* mechanistic and provenance evidence, not on assay silence — but a curator should note that no study has *directly assayed and formally excluded* trace aldose-reductase or monooxygenase activity of purified AKR1D1.

---

## Limitations and Knowledge Gaps

1. **No direct negative assay for aldose/monooxygenase activity on purified AKR1D1.** PMID21255593 assayed steroids, not aldoses or a Baeyer–Villiger reaction. The exclusion is inferred from structure/mechanism and definitions, not from a targeted null. *Resolution:* assay purified AKR1D1 against canonical aldose-reductase substrates (glyceraldehyde, glucose) and against the GO:0047086 progesterone→testosterone-acetate reaction with O₂/NADPH.
2. **PMID11342103 (17β-HSD / RHEA:53484) not read in full.** The product position (C17) and the intact-cell background remain unverified. This is the single accessory term where a genuine (if minor) activity cannot yet be firmly excluded. *Resolution:* obtain and read the full text; determine whether the 17β-OH product reflects intrinsic AKR1D1 activity or a coupled/paralog contribution.
3. **PMID21232532 read from abstract snippet only.** "Negligible AKR1D1 mRNA" is from the abstract; the enzymology attributed to AKR1C is not AKR1D1's regardless, so this gap is low-risk for the conclusion.
4. **Alignment is global pairwise, not a full structural superposition.** The Glu120↔His111 positional homology is high-confidence but sequence-derived; a structural superposition of AKR1D1 (e.g., PDB 3BUR/3COT) onto AKR1B1 would make it definitive.
5. **Substrate-inhibition kinetics not independently reproduced here.** The claim that substrate inhibition resolves older negatives rests on PMID21255593; not independently re-derived.

---

## Discriminating Tests

The following would most efficiently separate "retained ancestral activities" from "specialist 5β-reductase over-annotated":

1. **Targeted enzymology on purified recombinant AKR1D1** against:
   - **Aldose reductase substrates** (DL-glyceraldehyde, glucose) + NADPH → measures GO:0004032 directly. Predicted: negligible/absent.
   - **Ketosteroid monooxygenase reaction** (progesterone + O₂ + NADPH → testosterone acetate) → measures GO:0047086 directly. Predicted: absent (no oxygenase chemistry).
   - **17β-HSD reaction** (17-keto ↔ 17β-hydroxy steroid), cell-free → tests whether RHEA:53484 reflects intrinsic activity. Predicted: absent or negligible relative to 5β-reduction.
2. **E120→H "back-mutation" gain-of-function test.** Introduce Glu120His and assay for gain of general carbonyl-reduction activity. If the His→Glu substitution is the specificity switch, restoring His should confer measurable carbonyl reduction while abolishing 5β-reduction.
3. **Structural superposition** of AKR1D1 (PDB 3BUR) onto AKR1B1 (PDB 1US0) to confirm Glu120 occupies the aldose-reductase catalytic-His pocket in 3D.
4. **Full-text extraction of PMID11342103** to determine the exact product, position, and whether the assay was cell-free — the decisive check for the 17β-HSD term.
5. **Provenance trace of RHEA:53484 → UniProt IEA** to confirm the annotation is a single-reaction electronic inference rather than curated experimental support.

---

## Curation Leads (require curator verification)

**Retain (core):**
- **GO:0047787** Δ4-3-oxosteroid 5β-reductase activity (MF) — supported by [PMID: 21255593](https://pubmed.ncbi.nlm.nih.gov/21255593/), [PMID: 18407998](https://pubmed.ncbi.nlm.nih.gov/18407998/), [PMID: 26418565](https://pubmed.ncbi.nlm.nih.gov/26418565/).
  - *Snippet to verify (PMID21255593):* "AKR1D1 proficiently reduced all the steroids tested at physiological pH… Substrate inhibition was observed with C18 to C21 steroids provided that the C11 position was unsubstituted."
- BP: bile acid biosynthetic process; steroid metabolic process — supported by CBAS2 genetics ([PMID: 41387259](https://pubmed.ncbi.nlm.nih.gov/41387259/)).

**Flag for removal / NOT (leads):**
- **GO:0047086** ketosteroid monooxygenase (IBA) → *remove/NOT.* Requires O₂-dependent Baeyer–Villiger oxygenation; AKR1D1 is an NADPH oxidoreductase.
- **GO:0004032** aldose reductase (IBA) → *remove or non-core.* Catalytic His replaced by Glu120 (F001/F004); ancestral inference only.
- **GO:0008106** alcohol dehydrogenase, NADP+ (TAS:Reactome) → *remove/re-map.* All AKR1D1 Reactome reactions are Δ4→5β reductions, not C-OH oxidation (F003).

**Downgrade / verify (lead):**
- **GO:0072582** 17β-HSD (IEA:RHEA, RHEA:53484) → *non-core / verify.* Requires full read of [PMID: 11342103](https://pubmed.ncbi.nlm.nih.gov/11342103/); product position and intact-cell background must be checked before a hard NOT.

**Suggested curator questions:**
1. Has purified AKR1D1 ever been directly assayed and found negative for aldose-reductase or monooxygenase activity, or is the exclusion purely mechanistic/inferential?
2. Does RHEA:53484 (17β-HSD) derive from an intact-cell or cell-free assay in PMID11342103?
3. Should IBA terms conflicting with an experimentally defined specialist function be auto-flagged for review?

**Suggested experiments:** the E120H back-mutation gain-of-function assay and the targeted aldose/monooxygenase enzymology in "Discriminating Tests."

---

## Evidence Base (literature synthesis)

- *Crystal structure of human liver Δ4-3-ketosteroid 5β-reductase (AKR1D1) and implications for substrate binding and catalysis.* [PMID: 18407998](https://pubmed.ncbi.nlm.nih.gov/18407998/) — Establishes Tyr58/Glu120 catalytic dyad; Y58F and E120A null. **Core structural pillar** for the specificity argument.
- *Substrate specificity and inhibitor analyses of human steroid 5β-reductase (AKR1D1).* [PMID: 21255593](https://pubmed.ncbi.nlm.nih.gov/21255593/) — Homogeneous-enzyme kinetics across C18–C27 Δ4-ketosteroids; substrate inhibition resolves older negatives. **Core functional pillar.**
- *In-Depth Dissection of the P133R Mutation in Steroid 5β-Reductase (AKR1D1).* [PMID: 26418565](https://pubmed.ncbi.nlm.nih.gov/26418565/) — Disease mutation impairs NADPH binding/hydride transfer → bile acid deficiency. Confirms core physiological role.
- *Variants in AKR1D1 and Infant Mortality.* [PMID: 41387259](https://pubmed.ncbi.nlm.nih.gov/41387259/) — Biallelic LOF causes CBAS2 with near-absent primary bile acids. Confirms in-vivo essentiality of the 5β-reduction step.
- *AKR1D1 and CYP7B1 mutations in inborn errors of bile acid metabolism.* [PMID: 31337596](https://pubmed.ncbi.nlm.nih.gov/31337596/); infant cholestasis case reports [PMID: 30254413](https://pubmed.ncbi.nlm.nih.gov/30254413/), [PMID: 36739965](https://pubmed.ncbi.nlm.nih.gov/36739965/), [PMID: 38034430](https://pubmed.ncbi.nlm.nih.gov/38034430/) — Consistent disease genetics reinforcing the bile-acid-synthesis role.
- *Endometriosis expression study.* [PMID: 21232532](https://pubmed.ncbi.nlm.nih.gov/21232532/) — Assays AKR1C1/2/3, reports negligible AKR1D1 — refutes paralog transfer of multifunctionality.
- *17β-conversion source.* [PMID: 11342103](https://pubmed.ncbi.nlm.nih.gov/11342103/) — Basis of RHEA:53484 17β-HSD annotation; requires full-text scrutiny (open gap).
- Database/computational: Reactome ContentService (5 Δ4→5β reactions), QuickGO term definitions, UniProt P51857, and AKR1D1↔AKR1B1 pairwise alignment (52.5% identity; Glu120↔His111).

---

## Conclusion

The seed hypothesis is **right about the core and about substrate breadth**, and it makes a fair methodological point about not inferring loss from assay absence. But its central claim — that AKR1D1 *retains* aldose-reductase, ketosteroid-monooxygenase, and alcohol/17β-HSD capacities as genuine additional functions — is **not supported by direct evidence and is contradicted by a coherent structure–mechanism–provenance chain**. AKR1D1 is a specialist Δ4-3-oxosteroid 5β-reductase whose defining Glu120 substitution repurposes the AKR catalytic histidine; the Reactome "alcohol dehydrogenase" label is a reaction-class mislabel for the same 5β reduction; ketosteroid monooxygenase is chemically impossible for an oxidoreductase; and the AKR1C IDA source assays the paralogs, not AKR1D1. The accessory GO terms should be flagged for removal, NOT-qualification, or downgrade to non-core — with the 17β-HSD (RHEA) term the one that most warrants a full-text re-read before a hard call.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)