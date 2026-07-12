---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-12T12:05:26.496136'
end_time: '2026-07-12T12:23:21.414456'
duration_seconds: 1074.92
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: tipA
  gene_symbol: tipA
  uniprot_accession: Q94489
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: tipa-pp2c-phosphatase
  hypothesis_text: TipA is a functional PP2C-family (PPM), metal-dependent protein
    serine/threonine phosphatase
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: 'hypothesis: TipA is a functional PP2C-family (PPM), metal-dependent
    protein serine/threonine phosphatase

    focus_type: function_assignment

    context: []

    reference_id: []'
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

- **Organism code:** DICDI
- **Taxon:** Dictyostelium discoideum (NCBITaxon:44689)
- **Gene directory:** tipA
- **Gene symbol:** tipA
- **UniProt accession:** Q94489

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** tipa-pp2c-phosphatase
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

TipA is a functional PP2C-family (PPM), metal-dependent protein serine/threonine phosphatase

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: TipA is a functional PP2C-family (PPM), metal-dependent protein serine/threonine phosphatase
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

# Focused Curation Report — *Dictyostelium discoideum* **tipA** (UniProt Q94489)

**Hypothesis evaluated:** *TipA is a functional PP2C-family (PPM), metal-dependent protein serine/threonine phosphatase.*
**Focus type:** function_assignment · **Slug:** tipa-pp2c-phosphatase
**Date:** 2026-07-12 · **Iterations:** 1–3

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (family/fold supported; catalytic "functional phosphatase" claim UNRESOLVED — over-annotation risk if asserted with experimental confidence).**

- The **domain/fold assignment is well supported.** Q94489 is annotated by multiple orthogonal signature databases as a PPM/PP2C-type phosphatase domain (InterPro IPR001932/IPR053287, Gene3D 3.60.40.10, SUPFAM SSF81606, PANTHER PTHR21586 "TIPA"; UniProt domain 388–706). AlphaFold models this region as a confident PP2C fold (domain mean pLDDT ≈ 81).
- The **"functional / catalytically active phosphatase" part is not demonstrated.** There is **no biochemical evidence** — no phosphatase assay, no metal-dependence test, and no substrate has ever been reported for TipA. The only functional study (Stege et al. 1999, PMID 10402673) is a developmental-genetic phenotype (tip formation, cell sorting), not an enzymatic characterization.
- A **conserved-motif red flag:** the invariant PP2C metal-1/general-acid signature **[VY]-D-G-H-x-G ("DGH")** — present in human PPM1A and in the *Dictyostelium* functional PP2C **Spalten/SpnA** — is **absent** from TipA (the equivalent position reads **ADGC**, His→Cys).
- **Counter-nuance from structure:** despite the linear-motif loss, the AlphaFold model assembles a **spatial cluster of aspartate carboxylates (D413, D430, D576, D642, D646) plus His645** into a pocket resembling a PP2C bimetal active site. So a *divergent* but real metal-dependent active site remains plausible; this is not a clearly collapsed pseudophosphatase.
- **Family-wide catalytic-motif loss (over-annotation signal, added Iteration 2):** across the entire TIPA-specific PP2C-like family (InterPro IPR053287, n=100; Dictyostelium, Drosophila CG9801, Caenorhabditis, Trichinella, cnidarians, molluscs, Entamoeba), the canonical DGHxG motif is present in **0%** and a bare DGH in only **7%**, versus **79%** in the canonical PP2C family (IPR001932). The TIPA family is a divergent lineage that systematically lacks the invariant catalytic His, so **family/domain membership cannot by itself justify a "functional phosphatase" call** — this is a textbook paralog/frequency-bias over-annotation scenario. TipA's His645 is a *Dictyostelium-specific* substitution (family consensus has Ser here), i.e., a speculative species-specific candidate general acid, not a conserved catalytic signature.

- **Metal binding vs catalysis (Iteration 3):** the metal-coordinating **aspartate scaffold is conserved family-wide** (N-terminal motif 80%, C-terminal 86%, both 69% of 100 members) while the **catalytic general-acid His is not** (7%). This cleanly separates a plausibly retained *metal-binding* capacity from an *unsupported catalytic* capacity — the molecular signature of a metal-binding but catalytically divergent/pseudo-PP2C.

**Bottom line for the curator:** the PP2C **domain membership** can be annotated (computational/ISS-level), and **metal ion binding (GO:0046872)** is the best-supported computed inference. A **protein Ser/Thr phosphatase activity term should NOT be asserted with experimental evidence**; catalytic activity is unproven and the canonical catalytic His motif is degenerate across the whole TIPA lineage. Treat "functional metal-dependent Ser/Thr phosphatase" as a hypothesis to be tested, not an established fact.

---

## Evidence Matrix

| # | Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|----------|--------------|---------------------------|--------------|-------------|---------|--------------------------|
| 1 | UniProt Q94489; InterPro IPR001932/IPR053287; SUPFAM SSF81606; Gene3D 3.60.40.10; PANTHER PTHR21586 | Structural/evolutionary (database) | Supports (domain) | TipA contains a PP2C/PPM domain | PPM-type phosphatase domain at 388–706; PANTHER "TIPA" family | Sequence/profile | High for fold membership; profile match ≠ catalytic competence |
| 2 | This work — direct motif scan | Computational | Refutes/Qualifies (catalysis) | Canonical PP2C catalytic motif conserved? | Invariant **DGH** (metal-1 Asp + general-acid His) present in PPM1A ("VYDGHAGS") and Spalten O15743 ("VYDGHGGT") but **absent in TipA** ("VADGCNWG", His→Cys) | Q94489 vs P35813 vs O15743 | High (direct motif, reproducible). Single-motif view; ignores 3D relocation |
| 3 | This work — AlphaFold AF-Q94489-F1 (v6) geometry | Computational (structural) | Qualifies/Supports (catalysis plausible) | Does an active-site pocket assemble in 3D? | Domain pLDDT ≈ 81; Asp413/430/576/642/646 + His645 cluster within ~4–6 Å into a PP2C-like pocket | Predicted structure | Moderate. AF omits metals; rotamer distances uncertain; not proof of activity |
| 4 | Stege, Laub, Loomis 1999 (**PMID 10402673**) | Mutant phenotype | Supports BP/CC; silent on MF | What does TipA do biologically? | tipA-null: defective cell sorting, tip formation on mounds, reduced prespore/prestalk gene expression; cell-autonomous; acts in parallel with tipB/C/D | *D. discoideum* development | High for phenotype; **no enzyme assay**; does not establish catalytic mechanism |
| 5 | Aubry & Firtel 1998 (**PMID 9585512**) | Direct assay (paralog control) | Competing/Qualifies | Is there a bona fide *Dictyostelium* developmental PP2C? | Spalten (SpnA) encodes a **functional PP2C** (demonstrated), essential for cell-type differentiation; PP2C domain is the effector | *D. discoideum* development | High; shows a *different* gene is the validated developmental PP2C — TipA activity not assayed |
| 5b | This work — InterPro family motif census | Computational (evolutionary) | Qualifies/Refutes (family-based inference) | Does TIPA-family membership imply catalytic residues? | Canonical DGHxG in **0/100** TIPA-family (IPR053287) vs **79/100 (DGH)** in canonical PP2C (IPR001932); family shares divergent motifs "ADG[VC]NWG" and "(T/I)SDG[IV]xDN" but lacks the general-acid His | 100 cross-species family members | High (reproducible census). Motif-based; does not exclude activity via non-canonical mechanism |
| 5c | This work — metal-Asp scaffold census (Iteration 3) | Computational (evolutionary) | Qualifies (metal binding yes, catalysis no) | Are the metal-coordinating aspartates conserved family-wide? | Metal-Asp scaffolds retained: N-term [AG]DG[VCA]N[WF] **80/100**, C-term SDG-Asp **86/100**, both **69/100**; but catalytic His only **7/100**. TipA has both scaffolds + rare His645 | 100 TIPA-family members | High. Signature of metal-binding but catalytically divergent/pseudo-PP2C |
| 6 | Das, Helps, Cohen, Barford 1996 (**PMID 9003755**) | Structural (reference) | Orientation | What residues make PP2C catalytic? | PP2C is Mn²⁺/Mg²⁺-dependent; a **binuclear metal centre** with metal-bound water provides nucleophile/general acid; requires conserved Asp ligands | Human PP2Cα | High; establishes why metal-Asp/His conservation matters |

---

## GO Curation Implications (leads — require curator verification)

- **Molecular Function.** Do **not** assign an experimentally-supported protein Ser/Thr phosphatase MF term. Options, in order of conservatism:
  - Acceptable as **computational/ISS or IBA** (from PANTHER PTHR21586 "TIPA"): `GO:0004722` protein serine/threonine phosphatase activity **or** the more generic `GO:0016791` phosphatase activity — **with an ISS/IEA evidence code and a caveat note** that the canonical catalytic His motif is degenerate and activity is unassayed.
  - `GO:0046872` metal ion binding is the **best-supported computed inference** (the metal-coordinating aspartate scaffold is conserved family-wide: N-term 80%, C-term 86%, both 69%), but is still only sequence-level (ISS/IEA) — no metal-binding assay exists.
  - If the review’s prior action asserted an **experimental** MF phosphatase term, that is **too strong** → recommend downgrading to computational or removing pending assay.
- **Biological Process (retain).** `GO:0031154` culmination involved in sorocarp development (IMP) and `GO:0030587` sorocarp development (HMP) are supported by Stege et al. 1999 (PMID 10402673). Keep.
- **Cellular Component (retain).** `GO:0005737` cytoplasm (IDA, dictyBase). Keep.
- **Net:** the seed hypothesis, if used to add an experimentally-weighted MF phosphatase annotation, is **too strong**; a computational MF annotation with an explicit "atypical/unverified active site" caveat is defensible.

---

## Mechanistic Scope

- **Immediate molecular function under test:** metal-dependent hydrolysis of phosphoserine/phosphothreonine on protein substrates by a PPM/PP2C catalytic domain. This requires a binuclear Mn²⁺/Mg²⁺ centre coordinated by conserved aspartates plus a general acid (PMID 9003755).
- **What the evidence actually shows:** TipA *has* the PP2C fold and can *geometrically* assemble a candidate metal-binding pocket, but **no dephosphorylation, metal dependence, or substrate** has been measured.
- **Downstream/indirect layers (not the MF):** the tipA-null phenotype (cell sorting, tip formation, delayed prespore/prestalk differentiation, aggregate morphogenesis) is a **developmental outcome**, not direct evidence of catalytic activity. Attributing the phenotype to phosphatase catalysis is inference, not demonstration.

---

## Conflicts and Alternatives

1. **Paralog confusion (important).** The validated *Dictyostelium* developmental **PP2C is Spalten/SpnA (PMID 9585512), not TipA.** Spalten retains the intact DGH catalytic motif; TipA does not. A curator should ensure phosphatase evidence is not being transferred from Spalten (or the broader PP2C family) onto TipA by homology/family inference.
2. **Pseudophosphatase possibility.** Loss of the invariant general-acid His (DGH→DGC) is a classic hallmark of degenerate/pseudo-phosphatases. TipA could function as a **non-catalytic scaffold/adaptor** whose PP2C-like fold binds phospho-proteins without turning them over.
3. **Divergent-but-active possibility.** The AlphaFold carboxylate+His cluster leaves open that TipA is a *sequence-atypical* active phosphatase (His role relocated to His645). This cannot be resolved without an assay.
4. **Prediction-quality caveats.** Family-level annotation (PANTHER "TIPA") is prone to frequency/paralog bias; AlphaFold does not model catalysis; the linear-motif call ignores 3D. Each tool, alone, is weak — hence the "unresolved" MF verdict.
5. **Family-wide degeneracy quantified (Iteration 2).** The catalytic His loss is not idiosyncratic to TipA but is shared by the whole TIPA/IPR053287 lineage (0/100 with DGHxG vs 79/100 in canonical PP2C). This means any "functional phosphatase" annotation propagated from family/domain membership is unsupported by conserved catalytic residues; if the review's assignment derives from InterPro2GO/PANTHER family inference, that is the specific over-annotation to flag.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| No enzyme activity data | PubMed searches returned **no** biochemical assay for TipA | "Functional phosphatase" is the crux of the hypothesis | In vitro phosphatase assay (pNPP + protein/phosphopeptide substrate) ± Mn²⁺/Mg²⁺ |
| Catalytic-residue identity | Motif scan (reliable) + AF geometry (suggestive); pairwise alignment was **unreliable** (failed even on the functional Spalten control) | Determines active vs pseudo-phosphatase | Structure-guided HMM/MSA of PPM family with metal modeling; site-directed mutagenesis of candidate Asp/His |
| Substrate & physiological target | None known | Needed to link catalysis to the tip/sorting phenotype | Phosphoproteomics of tipA-null vs WT; substrate trapping |
| Metal dependence | Not tested | Defines "metal-dependent" claim | Activity assay ± EDTA / with Mn²⁺, Mg²⁺ titration |
| Is His645 the general acid? | Inferred from AF cluster only | Distinguishes divergent-active from dead | H645A / D642A / D646A catalytic mutants + activity |

---

## Discriminating Tests (most efficient first)

1. **In vitro phosphatase assay** of recombinant TipA (or its 388–706 domain) on a generic substrate (pNPP or phosphopeptide) with and without Mn²⁺/Mg²⁺ — directly settles "functional metal-dependent phosphatase."
2. **Structure-guided catalytic mutagenesis** (candidate metal ligands D413/D430/D576/D642/D646 and His645) → test loss of activity and whether mutants fail to rescue the tipA-null developmental phenotype (links catalysis to biology).
3. **Rigorous PPM-family MSA/HMM with metal-site mapping** (e.g., against solved PP2C structures) to formally score active-site integrity rather than relying on a single linear motif.
4. **Phosphoproteomics** of tipA⁻ vs WT during aggregation/tip formation to identify candidate substrates (hyperphosphorylated targets).
5. **Comparative check of the PANTHER "TIPA" subfamily (PTHR21586, incl. Drosophila CG9801)** for conservation/loss of catalytic residues to see if the whole subfamily is degenerate.

---

## Curation Leads (require curator verification)

- **Candidate references to cite/verify:**
  - PMID **10402673** (Stege 1999) — snippet: *"null mutations in tipA showed a primary defect in cell sorting and the formation of tips on the developing mound"* → supports BP/CC only, **not** MF.
  - PMID **9585512** (Aubry & Firtel 1998) — snippet: *"a carboxy-terminal domain that encodes a functional PP2C"* → the validated developmental PP2C is **Spalten**, useful as paralog control (do not transfer to TipA).
  - PMID **9003755** (Das 1996) — snippet: *"Mn²⁺- or Mg²⁺-dependent protein Ser/Thr phosphatase … binds two manganese ions … provide a nucleophile and general acid"* → defines the catalytic requirements TipA has not been shown to meet.
- **Candidate GO actions:**
  - Keep BP `GO:0031154`, `GO:0030587`; keep CC `GO:0005737`.
  - If an MF phosphatase term exists with experimental evidence → **downgrade to ISS/IEA or remove** (too strong).
  - If adding MF, use ISS/IBA `GO:0004722` (or `GO:0016791`) **with a caveat** that the catalytic His motif is atypical and activity is unverified. Avoid a bare "protein binding" fallback.
- **Suggested curator questions:**
  1. Is any experimental phosphatase evidence for TipA in the source, or is the assignment homology-only?
  2. Is the MF being transferred from Spalten/family membership (paralog carry-over)?
- **Suggested experiments:** see Discriminating Tests 1–2.

---

## Provenance / Reproducibility

- UniProt Q94489 (759 aa; domain 388–706), P35813 (PPM1A), O15743 (Spalten/SpnA) fetched via UniProt REST.
- Active-site motif scan (`DG[HN].G`, `[ILVMFC]DG[ILVMFAWI]`): **DGH present in PPM1A@60 and Spalten@749; absent in TipA (ADGC@430)**.
- AlphaFold AF-Q94489-F1 v6: domain mean pLDDT 80.8; carboxylate cluster D413/D430/D576/D642/D646 + His645 within ~4–6 Å.
- InterPro family motif census (Iteration 2): IPR053287 (TIPA) n=100 → DGHxG 0%, DGH 7%; IPR001932 (canonical PP2C, reviewed) n=100 → DGH 79%. Conserved TIPA-family motifs: "ADG[VC]NWG" and "(T/I)SDG[IV]xDN"; His645 is a Dictyostelium-specific substitution of the family-consensus Ser.
- Pairwise BLOSUM62 global alignment was **explicitly judged unreliable** (failed on the functional Spalten control) and was therefore **not** used for residue-level conclusions.

*Limitations:* all sequence/structure analyses are computational; no wet-lab activity data exist. Conclusions distinguish direct results (motif presence/absence, fold confidence) from inference (catalytic competence).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)