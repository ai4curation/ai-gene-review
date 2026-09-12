---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-09T12:56:20.269556'
end_time: '2026-07-09T13:28:52.038462'
duration_seconds: 1951.77
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: LysB
  gene_symbol: LysB
  uniprot_accession: Q08694
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: computational_prediction
  hypothesis_slug: prediction-chitinase-immune
  hypothesis_text: BioReason-Pro SFT predicts chitinase activity (GO:0004568) and
    immune roles (negative regulation of innate immune response GO:0045824; defense
    response to Gram-negative bacterium GO:0050829) for the Drosophila melanogaster
    protein LysB (Q08694). Independently assess whether LysB is a chitinase versus
    a lysozyme/muramidase, and whether its physiological role is digestive versus
    immune, given that Drosophila LysB-family proteins are described as stomach/gut
    acidic digestive lysozymes. Determine whether the chitinase-activity and immune-response
    predictions are supported or are misassignments (e.g. lysozyme-vs-chitinase fold
    confusion and digestive-vs-immune conflation).
  term_context: '- Term: chitinase activity (GO:0004568)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: BioReason-Pro SFT predicts chitinase activity\
    \ (GO:0004568) and immune roles (negative regulation\n  of innate immune response\
    \ GO:0045824; defense response to Gram-negative bacterium GO:0050829) for the\n\
    \  Drosophila melanogaster protein LysB (Q08694). Independently assess whether\
    \ LysB is a chitinase versus\n  a lysozyme/muramidase, and whether its physiological\
    \ role is digestive versus immune, given that Drosophila\n  LysB-family proteins\
    \ are described as stomach/gut acidic digestive lysozymes. Determine whether the\n\
    \  chitinase-activity and immune-response predictions are supported or are misassignments\
    \ (e.g. lysozyme-vs-chitinase\n  fold confusion and digestive-vs-immune conflation).\n\
    focus_type: computational_prediction\nterm_id: GO:0004568\nterm_label: chitinase\
    \ activity\ncontext: []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
artifacts:
- filename: artifacts_lysB_fold_check.md
  path: openscientist_artifacts/artifacts_lysB_fold_check.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist lysB fold check
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
- **Gene directory:** LysB
- **Gene symbol:** LysB
- **UniProt accession:** Q08694

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-chitinase-immune
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

BioReason-Pro SFT predicts chitinase activity (GO:0004568) and immune roles (negative regulation of innate immune response GO:0045824; defense response to Gram-negative bacterium GO:0050829) for the Drosophila melanogaster protein LysB (Q08694). Independently assess whether LysB is a chitinase versus a lysozyme/muramidase, and whether its physiological role is digestive versus immune, given that Drosophila LysB-family proteins are described as stomach/gut acidic digestive lysozymes. Determine whether the chitinase-activity and immune-response predictions are supported or are misassignments (e.g. lysozyme-vs-chitinase fold confusion and digestive-vs-immune conflation).

## Term and Decision Context

- Term: chitinase activity (GO:0004568)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: BioReason-Pro SFT predicts chitinase activity (GO:0004568) and immune roles (negative regulation
  of innate immune response GO:0045824; defense response to Gram-negative bacterium GO:0050829) for the
  Drosophila melanogaster protein LysB (Q08694). Independently assess whether LysB is a chitinase versus
  a lysozyme/muramidase, and whether its physiological role is digestive versus immune, given that Drosophila
  LysB-family proteins are described as stomach/gut acidic digestive lysozymes. Determine whether the
  chitinase-activity and immune-response predictions are supported or are misassignments (e.g. lysozyme-vs-chitinase
  fold confusion and digestive-vs-immune conflation).
focus_type: computational_prediction
term_id: GO:0004568
term_label: chitinase activity
context: []
reference_id:
- doi:10.64898/2026.03.19.712954
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

# AIGR Gene Hypothesis Deep Research — LysB (Q08694, DROME)

**Focus type:** computational_prediction · **Hypothesis slug:** prediction-chitinase-immune
**Term under evaluation:** chitinase activity (GO:0004568)
**Reference context:** doi:10.64898/2026.03.19.712954

---

## Summary

The BioReason-Pro SFT model predicts that *Drosophila melanogaster* LysB (UniProt **Q08694**) has **chitinase activity (GO:0004568)** and two immune roles — **negative regulation of innate immune response (GO:0045824)** and **defense response to Gram-negative bacterium (GO:0050829)**. Independent evaluation from sequence classification, domain architecture, a custom catalytic-site alignment, primary expression literature, and the current GO annotation record indicates that all three predictions are either **wrong** or **unsupported by the physiological evidence**. The overall verdict is **REFUTED / OVER-ANNOTATED**.

LysB is a **glycoside hydrolase family 22 (GH22) C-type lysozyme (muramidase, EC 3.2.1.17)** — not a chitinase (EC 3.2.1.14; GH18/GH19). Its molecular function is peptidoglycan hydrolysis. The "chitinase" prediction is best explained as a **fold/activity misassignment** arising from the well-documented, weak chito-oligosaccharide side-activity that C-type lysozymes possess, together with the general confusion between lysozyme and chitinase glycosidase folds. Physiologically, the Drosophila *LysB–E* cluster comprises **constitutive, midgut-restricted, acidic digestive lysozymes** that are transcriptionally **repressed** (not induced) by bacterial infection and are **not expressed in fat body or hemocytes** — the opposite of what an induced humoral immune effector or an immune *regulator* would look like. This makes **GO:0045824** unsupported and biologically implausible for LysB, and it substantially weakens the case for **GO:0050829**, which exists in the GO record only as an ISS "by similarity" carry-over with no experimental basis.

For a curator, the actionable conclusion is: **do not add GO:0004568 or GO:0045824**; treat the existing **GO:0050829** as low-confidence (ISS-only, conflicting with digestive biology) and consider flagging it for review or "non-core" status; and **retain the well-supported core terms** — **GO:0003796 (lysozyme activity, MF)** and **GO:0005576 (extracellular region, CC)** — ideally complemented by a BP term reflecting **digestion / bacteriophagy** rather than immunity.

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED.**

All three predicted terms fail independent evaluation:

- **GO:0004568 (chitinase activity):** Refuted. LysB is a GH22 muramidase with a conserved lysozyme catalytic dyad and no GH18/GH19 chitinase domain or active-site motif. The only "chitinase-like" property is the weak chitodextrin side-activity intrinsic to C-type lysozymes, which is captured by the canonical lysozyme catalytic-activity description and does not warrant a chitinase MF term.
- **GO:0045824 (negative regulation of innate immune response):** Refuted/unsupported. No experimental or credible computational basis; contradicts the constitutive, infection-repressed, midgut-restricted expression profile.
- **GO:0050829 (defense response to Gram-negative bacterium):** Weakly supported at best; present only as a single ISS "by similarity" annotation, in tension with the digestive role.

The most important caveat is that a minority of insect c-type lysozymes are genuinely dual-function (digestive + mild immune effector), so a low-level bactericidal activity for LysB cannot be fully excluded — but even the strongest reading of that literature would never justify a *negative regulator of immunity* assignment, and the Drosophila-specific expression data argue against an immune-effector role.

---

## Key Findings

### Finding 1 — LysB is a GH22 C-type lysozyme (EC 3.2.1.17), not a chitinase

UniProt Q08694 carries the recommended name **"Lysozyme B"**, EC number **3.2.1.17** (lysozyme/muramidase), and the family SIMILARITY statement **"Belongs to the glycosyl hydrolase 22 family."** The domain architecture is **exclusively** C-type lysozyme with no chitinase signature whatsoever:

| Resource | Identifier | Assignment |
|---|---|---|
| InterPro | IPR001916 / IPR000974 | Glycoside hydrolase family 22 / C-type lysozyme |
| Pfam | PF00062 | Lys (lysozyme) |
| CDD | cd16899 | LYZ_C_invert (invertebrate C-type lysozyme) |
| PANTHER | PTHR11407 | LYSOZYME C |
| SUPFAM | SSF53955 | Lysozyme-like superfamily |

No GH18 or GH19 chitinase domain (e.g., Pfam PF00704 / Glyco_hydro_18, or Glyco_hydro_19) is present. The GO molecular-function annotation for Q08694 is **GO:0003796 lysozyme activity**, not GO:0004568 chitinase activity.

Critically, the mechanistic origin of the model's error is visible in the enzyme's own catalytic-activity description. The canonical C-type lysozyme reaction hydrolyzes the β-1,4 linkage between *N*-acetylmuramic acid (MurNAc) and *N*-acetylglucosamine (GlcNAc) in **peptidoglycan** — "**and between N-acetyl-D-glucosamine residues in chitodextrins.**" This weak activity on chito-oligosaccharides is an intrinsic, well-known side-property of C-type lysozymes and is almost certainly the textual/feature signal that led a machine-learning model to over-predict full **endochitinase** activity. A weak in-vitro side-activity on short chitodextrins is **not** equivalent to biological chitinase activity (processive hydrolysis of insoluble chitin polymer), which is carried out by structurally distinct GH18/GH19 enzymes.

This finding is anchored in the review-level statement that **"Lysozymes from family 22 of glycoside hydrolases are usually part of the defense system against bacteria"** ([PMID: 17825580](https://pubmed.ncbi.nlm.nih.gov/17825580/)), confirming that C-type/digestive insect lysozymes belong to GH22 — a family distinct from the chitinase families.

### Finding 2 — Drosophila LysB is a constitutive midgut digestive lysozyme, not an induced immune effector

The defining expression study of the Drosophila lysozyme locus ([PMID: 8159165](https://pubmed.ncbi.nlm.nih.gov/8159165/), Daffre et al. 1994) reports that **"four closely related genes, LysB, C, D and E, are all strongly expressed in the midgut of larvae and adults"** and that **"None of the genes is expressed in the fat body or haemocytes."** In insects, the fat body and hemocytes are the principal tissues of the systemic humoral immune response; the complete absence of LysB expression there is direct evidence against a humoral/immune-effector role. The same work notes that all of these genes except LysP encode **acidic** proteins "highly reminiscent" of the acidic digestive lysozymes of mammalian foregut fermenters — a hallmark of enzymes optimized for acidic gut lumen conditions and bacteriolytic digestion.

An independent study of the same locus ([PMID: 1588905](https://pubmed.ncbi.nlm.nih.gov/1588905/), Kylsten et al. 1992) found that lysozyme transcription **decreases** after bacterial injection and concluded that these genes **"have been recruited for the digestion of bacteria present in fermenting food."** A gene whose transcription is *repressed* by infection and whose product acts in the gut lumen to digest dietary bacteria is behaving as a **digestive enzyme**, not as an inducible immune effector and certainly not as a *negative regulator* of the innate immune response.

Consistent with the primary literature, UniProt Q08694 states in its FUNCTION field that LysB is **"Unlikely to play an active role in the humoral immune defense. May have a function in the digestion of bacteria in the food,"** and its TISSUE SPECIFICITY field localizes expression to the midgut with peak expression in the 3rd larval instar.

The digestive-lysozyme model is reinforced by comparative work across arthropods: housefly (*Musca domestica*) digestive lysozymes MdL1/MdL2 are acidic-optimum midgut enzymes ([PMID: 19099150](https://pubmed.ncbi.nlm.nih.gov/19099150/)), the first crystal structure of a digestive lysozyme was solved from housefly ([PMID: 17825580](https://pubmed.ncbi.nlm.nih.gov/17825580/)), and synanthropic mites use acidic digestive lysozymes to exploit bacteria as a food source, with maximal activity at the acidic pH of the gut ([PMID: 18357505](https://pubmed.ncbi.nlm.nih.gov/18357505/)). These establish "acidic midgut digestive lysozyme" as a recurrent, well-characterized functional class into which Drosophila LysB clearly falls.

### Finding 3 — Sequence analysis confirms the C-type lysozyme catalytic dyad and the absence of a chitinase active site

To test the classification directly rather than relying on database labels, an in-run global alignment (Needleman–Wunsch, implemented in NumPy) was performed between the **mature LysB sequence** (122 aa, after removing the signal peptide, residues 1–18) and **hen egg-white lysozyme (HEWL)**, the archetypal GH22 C-type lysozyme:

| Metric | Result |
|---|---|
| Identity to HEWL | **41.3%** (50/121 aligned positions) |
| HEWL catalytic Glu35 | **Conserved** (→ Glu in LysB) |
| HEWL catalytic Asp52 | **Conserved** (→ Asp in LysB) |
| Cysteine count | **8** (4 disulfides), matching HEWL's C-type scaffold |
| GH18 chitinase catalytic motif (DxxDxDxE) | **Absent** |
| Enzyme classification | EC 3.2.1.17 (lysozyme), **not** EC 3.2.1.14 (chitinase) |

The conservation of **both** HEWL catalytic residues (the Glu general acid and the Asp that stabilizes/participates in catalysis) together with the eight-cysteine (four-disulfide) C-type lysozyme fold is diagnostic of a functional GH22 muramidase. The **absence** of the GH18 chitinase catalytic signature (the DxxDxDxE motif that defines the GH18 active site) is direct negative evidence against the chitinase prediction: LysB does not possess the active-site chemistry required for a genuine chitinase.

### Finding 4 — The current GO record contains no chitinase or immune-regulation term; the sole defense term is ISS-only

A QuickGO retrieval (performed in-run) returned **6 annotations** for Q08694 spanning **three distinct terms**:

| GO term | Aspect | Evidence in the record |
|---|---|---|
| **GO:0003796** lysozyme activity | MF | Supported four independent ways: ISS from P00697; **IBA** from GO_Central (PANTHER PTN004256961, including HEWL P00698); **IEA** from InterPro IPR000974 / EC 3.2.1.17; and ISS with reference PMID:8159165 |
| **GO:0050829** defense response to Gram-negative bacterium | BP | **Single ISS** annotation, by-similarity to UniProtKB P00697 (GO_REF:0000024, FlyBase). No experimental evidence. |
| **GO:0005576** extracellular region | CC | ISS |

Two facts are decisive for the curation decision:

1. **GO:0004568 (chitinase activity) is entirely absent** from the current annotation set, and **GO:0045824 (negative regulation of innate immune response) is entirely absent.** Both predicted terms would therefore be **new additions**, and neither is justified by any experimental or well-founded computational evidence.
2. The one immune-adjacent term that does exist — **GO:0050829** — rests on a **single ISS "by similarity"** annotation with no experimental support, and it is in tension with the digestive, infection-repressed expression profile documented in Finding 2. It should be treated as low-confidence, not as corroboration of the seed hypothesis.

---

## Mechanistic Model / Interpretation

The seed hypothesis effectively bundles two distinct claims, and both fail for the same underlying reason — **conflation of superficially related categories**:

```
  BioReason-Pro prediction                Reality (this analysis)
  ─────────────────────────               ────────────────────────────────
  MF: chitinase activity      ──►  GH22 C-type lysozyme (muramidase, EC 3.2.1.17)
      (GO:0004568)                  · Glu35/Asp52 dyad conserved (41% id to HEWL)
                                     · 8 Cys / 4 disulfides, lysozyme fold
                                     · NO GH18/GH19 chitinase domain or motif
                                     · "chitinase" = weak chitodextrin SIDE-activity
                                       intrinsic to C-type lysozymes → misread as
                                       full endochitinase

  BP: neg. reg. innate         ──►  Constitutive DIGESTIVE lysozyme
      immune response                · midgut-restricted; NOT in fat body/hemocytes
      (GO:0045824)                   · transcription REPRESSED by infection
  BP: defense vs Gram-neg.           · "recruited for digestion of bacteria in food"
      (GO:0050829, ISS-only)         · immune terms = digestive-vs-immune conflation
```

**Molecular axis (lysozyme vs chitinase).** Both lysozymes and chitinases are glycoside hydrolases that cleave β-1,4 glycosidic bonds in GlcNAc-containing polymers, so they share a substrate chemistry motif. But they are **different enzyme families with different folds and active sites**: GH22 (lysozyme) versus GH18/GH19 (chitinase). C-type lysozymes have a documented, weak ability to hydrolyze short **chitodextrins** — this is even written into the UniProt/Rhea catalytic-activity string for Q08694. A model trained to associate GlcNAc-hydrolysis language with "chitinase" will over-predict GO:0004568 for a lysozyme. The direct evidence (conserved lysozyme dyad, correct fold, absent chitinase motif) refutes a genuine chitinase assignment.

**Physiological axis (digestive vs immune).** Insect lysozymes occupy two functionally divergent niches: (i) **inducible immune-effector** lysozymes expressed in fat body/hemolymph and up-regulated by infection, and (ii) **constitutive digestive** lysozymes expressed in an acidic midgut and used to lyse and digest dietary/gut bacteria (the "bacteriophagy" strategy shared with ruminants, foregut-fermenting mammals, and acaridid mites). Drosophila LysB belongs unambiguously to class (ii): midgut-restricted, acidic, constitutive, and infection-**repressed**. A negative *regulator* of innate immunity (GO:0045824) would be a signaling/regulatory role entirely unlike a secreted gut hydrolase; nothing in the evidence supports it, and the model likely generated it by over-generalizing "lysozyme → immunity" and then inverting it to fit a repression signal.

The coherent model is therefore: **LysB is a secreted, extracellular (GO:0005576), acidic midgut muramidase (GO:0003796) whose biological process is the digestion of bacteria in food (bacteriophagy), not immune defense or immune regulation.**

---

## Evidence Matrix

| # | Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt Q08694 (database) | Review/database | **Refutes** chitinase; **supports** lysozyme | Is LysB a chitinase or a lysozyme? | Recommended name "Lysozyme B", EC 3.2.1.17, GH22 family; MF = GO:0003796 lysozyme activity | *D. melanogaster* protein record | High for classification; database-level, curated |
| 2 | InterPro/Pfam/CDD/PANTHER/SUPFAM (database) | Structural/evolutionary (computational) | **Refutes** chitinase | Does LysB carry a chitinase domain? | Exclusively C-type lysozyme domains (IPR001916/000974, PF00062, cd16899, PTHR11407, SSF53955); no GH18/GH19 | Domain architecture | High; concordant across 5 resources |
| 3 | [PMID: 17825580](https://pubmed.ncbi.nlm.nih.gov/17825580/) | Structural/review | **Refutes** chitinase; supports digestive lysozyme | Are family-22 lysozymes a defense/digestive class distinct from chitinases? | "Lysozymes from family 22 of glycoside hydrolases are usually part of the defense system against bacteria"; first digestive-lysozyme crystal structure | Housefly digestive lysozyme | High; direct structural family evidence |
| 4 | In-run alignment (this run) | Computational | **Refutes** chitinase | Does LysB have a lysozyme dyad and lack a chitinase motif? | 41.3% id to HEWL; Glu35/Asp52 conserved; 8 Cys; GH18 DxxDxDxE motif absent | Mature LysB vs HEWL | Moderate–high; custom NW alignment, single reference (HEWL) |
| 5 | [PMID: 8159165](https://pubmed.ncbi.nlm.nih.gov/8159165/) | Localization / expression | **Refutes** immune roles; supports digestive | Where is LysB expressed? | "LysB, C, D and E... strongly expressed in the midgut"; "None... expressed in the fat body or haemocytes" | Larval & adult midgut | High; primary study of the locus |
| 6 | [PMID: 1588905](https://pubmed.ncbi.nlm.nih.gov/1588905/) | Expression / mutant-adjacent | **Refutes** immune induction; supports digestive | Is LysB induced or repressed by infection? | Transcription decreases after bacterial injection; "recruited for the digestion of bacteria present in fermenting food" | Drosophila gut | High; primary study |
| 7 | QuickGO for Q08694 (database) | Review/database | **Refutes** both predicted terms | Do current GO annotations include chitinase/immune-reg? | No GO:0004568 and no GO:0045824; GO:0050829 is single ISS by-similarity; core = GO:0003796 + GO:0005576 | GO annotation record | High; retrieved in-run |
| 8 | [PMID: 19099150](https://pubmed.ncbi.nlm.nih.gov/19099150/) | Direct assay (ortholog) | **Qualifies/supports** digestive | Do insect gut lysozymes act as acidic digestive enzymes? | MdL1/MdL2 housefly midgut lysozymes, acidic pH optimum (~4.8) | Housefly midgut | Moderate; ortholog, not LysB itself |
| 9 | [PMID: 18357505](https://pubmed.ncbi.nlm.nih.gov/18357505/) | Direct assay (comparative) | **Qualifies/supports** digestive | Is bacteriophagy a general digestive-lysozyme strategy? | Acidic digestive lysozymes let mites use bacteria as food; gut-pH activity optimum | Acaridid mites | Moderate; comparative, not Drosophila |
| 10 | [PMID: 19161941](https://pubmed.ncbi.nlm.nih.gov/19161941/) | Direct assay (ortholog) | **Competing/qualifies** | Can an insect c-type lysozyme have immune activity? | Housefly MdLys mildly up-regulated by bacteria; recombinant protein inhibits G− and G+ bacteria | Housefly midgut/fat body | Moderate; shows some insect lysozymes are dual-function, but MdLys differs from LysB (expressed in fat body, infection-induced) |

---

## Evidence Base (literature summary)

| Paper | PMID | Role in this evaluation |
|---|---|---|
| *The lysozyme locus in Drosophila melanogaster: an expanded gene family adapted for expression in the digestive tract* | [8159165](https://pubmed.ncbi.nlm.nih.gov/8159165/) | **Primary, decisive.** LysB–E strongly midgut-expressed; none in fat body/hemocytes; acidic, digestive-lysozyme-like. |
| *The lysozyme locus in Drosophila melanogaster: different genes are expressed in midgut and salivary glands* | [1588905](https://pubmed.ncbi.nlm.nih.gov/1588905/) | **Primary, decisive.** Transcription decreases after bacterial injection; recruited for digestion of dietary bacteria. |
| *The crystal structure of a lysozyme c from housefly Musca domestica, the first structure of a digestive lysozyme* | [17825580](https://pubmed.ncbi.nlm.nih.gov/17825580/) | Confirms GH22 family placement and digestive-lysozyme structural class. |
| *Cloning, purification and comparative characterization of two digestive lysozymes from Musca domestica larvae* | [19099150](https://pubmed.ncbi.nlm.nih.gov/19099150/) | Ortholog evidence: acidic-optimum midgut digestive lysozymes. |
| *Digestive function of lysozyme in synanthropic acaridid mites enables utilization of bacteria as a food source* | [18357505](https://pubmed.ncbi.nlm.nih.gov/18357505/) | Comparative evidence: acidic digestive lysozyme = bacteriophagy strategy. |
| *Molecular characterization and expression analysis of a chicken-type lysozyme gene from housefly (Musca domestica)* | [19161941](https://pubmed.ncbi.nlm.nih.gov/19161941/) | Competing/qualifying: some insect c-type lysozymes are dual digestive/immune — but MdLys (fat-body-expressed, infection-induced) differs from LysB. |

---

## GO Curation Implications

**Lead (requires curator verification):**

1. **GO:0004568 (chitinase activity, MF) — DO NOT ADD.** The prediction is a fold/activity misassignment. LysB is a GH22 muramidase with a conserved lysozyme catalytic dyad and no GH18/GH19 chitinase domain or active-site motif. The only "chitinase-like" property is the intrinsic weak chitodextrin side-activity of C-type lysozymes, which is already captured by the lysozyme catalytic-activity description and does not warrant a chitinase MF term (in vitro-only, side-activity, not the biological function).

2. **GO:0045824 (negative regulation of innate immune response, BP) — DO NOT ADD.** No experimental or credible computational support. The term is biologically implausible for a secreted digestive hydrolase and contradicts the constitutive, infection-repressed, midgut-restricted expression profile.

3. **GO:0050829 (defense response to Gram-negative bacterium, BP) — FLAG / treat as non-core.** Present in the record only as a **single ISS "by similarity"** to HEWL-type P00697, with no experimental basis, and in tension with digestive biology. Recommend curator review; at minimum it should not be treated as core function, and it should not be cited as corroboration of the immune hypothesis.

4. **GO:0003796 (lysozyme activity, MF) — RETAIN (core).** Well supported by four independent evidence lines (ISS, IBA, IEA/InterPro-EC, and ISS to PMID:8159165) and by the in-run catalytic-dyad analysis. This is the correct primary molecular function.

5. **GO:0005576 (extracellular region, CC) — RETAIN.** Consistent with a secreted gut lysozyme.

6. **Consider ADDING a digestion-focused BP term** (curator lead): a term reflecting **digestion / catabolism of bacterial cell wall in the gut / bacteriophagy** would more accurately capture the biological process than any immune term. Candidate directions include a peptidoglycan catabolic process or digestion term; the exact choice should be curator-verified against GO structure and the PMID:8159165 / PMID:1588905 evidence.

**Aspect summary:** MF = lysozyme activity (retain), not chitinase (reject). BP = digestion/bacteriophagy (add, curator-verify), not immune regulation (reject) and not defense-response as core (downgrade). CC = extracellular region (retain).

---

## Mechanistic Scope

The immediate molecular function under test is **glycoside-hydrolase activity on a GlcNAc-containing polymer**. The direct gene-product activity of LysB is **muramidase/lysozyme activity** — hydrolysis of the MurNAc–GlcNAc β-1,4 bond in bacterial peptidoglycan — as established by family classification, domain content, the conserved Glu/Asp catalytic dyad, and EC 3.2.1.17. This is distinct from **chitinase activity**, which requires the GH18/GH19 fold and active site that LysB lacks.

Everything in the immune framing of the seed hypothesis is either **downstream/indirect** or **absent**:
- "Defense response to Gram-negative bacterium" is an inferred phenotype-level consequence, imported by similarity, not a demonstrated function of LysB.
- "Negative regulation of innate immune response" is a regulatory/signaling process category with no mechanistic link to a secreted digestive hydrolase; there is no evidence LysB participates in immune signaling.
- The digestive role (lysing dietary bacteria in the acidic midgut) is the direct physiological deployment of the muramidase activity — a **nutritional/digestive** process, not an immune-defense process, even though the underlying chemistry (bacteriolysis) is shared with immune lysozymes.

---

## Conflicts and Alternatives

- **Paralog / family carry-over confusion.** The Drosophila lysozyme locus contains a tandem cluster (LysB–E, plus LysP, LysS, etc.). Annotations and predictions can bleed across paralogs and across the broader "lysozyme/glycosidase" family. The GO:0050829 ISS to HEWL (P00697) is a concrete example of **defense-response carry-over** from a canonical immune lysozyme to a digestive one.

- **Dual-function orthologs are real but do not rescue the immune prediction.** Housefly MdLys ([PMID: 19161941](https://pubmed.ncbi.nlm.nih.gov/19161941/)) is expressed in midgut *and* fat body, is mildly infection-induced, and its recombinant protein inhibits bacteria — i.e., some insect c-type lysozymes are genuinely dual digestive/immune. This is a legitimate **competing consideration**. However, it does **not** apply to Drosophila LysB, which — unlike MdLys — is **not** expressed in fat body/hemocytes and is **repressed** (not induced) by infection ([PMID: 8159165](https://pubmed.ncbi.nlm.nih.gov/8159165/); [PMID: 1588905](https://pubmed.ncbi.nlm.nih.gov/1588905/)). Even the strongest immune interpretation would be a mild bactericidal *effector* activity, never *negative regulation* of the immune response (GO:0045824).

- **Weak in-vitro chitodextrin activity vs biological chitinase.** C-type lysozymes can slowly hydrolyze short chito-oligosaccharides. Treating this in-vitro side-activity as a biological chitinase function would be an over-annotation; the physiological substrate is peptidoglycan.

- **Organism/tissue specificity.** Evidence supporting digestion comes partly from orthologs (housefly, mites). While the Drosophila-specific expression data are decisive against the immune-effector/regulator interpretation, direct enzymatic assays of purified Q08694 protein are not in the reviewed literature set (see Knowledge Gaps).

---

## Limitations and Knowledge Gaps

1. **No direct enzymatic assay of purified LysB (Q08694).** Checked: the primary literature reviewed here characterizes the *locus* expression (PMID:8159165, 1588905) and orthologous digestive lysozymes (housefly, mites), but not a purified recombinant LysB kinetic assay. This matters because the definitive discriminator between lysozyme and chitinase, and between digestive and immune roles, is a direct activity/pH-profile assay on the LysB protein. *Resolution:* recombinant expression + muramidase vs chitinase activity assays and an acidic-pH-optimum profile.

2. **Alignment used a single reference (HEWL).** The in-run NW alignment (41% identity, conserved dyad) is robust for classification but is a custom implementation against one archetype. *Resolution:* a multiple-sequence alignment across GH22 members and a structural superposition (e.g., AlphaFold model vs HEWL and vs a GH18 chitinase) would strengthen the fold assignment. Structural tools (Phenix/superpose) were available but not required given the concordant sequence/domain evidence.

3. **GO:0050829 provenance.** It is ISS-by-similarity to P00697; the exact rationale and whether FlyBase intends it as core is not fully resolved from the record alone. *Resolution:* curator inspection of GO_REF:0000024 and the FlyBase gene report.

4. **No in-run structural confidence metrics (pLDDT/PAE).** An AlphaFold confidence check was not run; it would add independent support for the lysozyme fold but is not necessary to reach the verdict.

5. **Reference doi:10.64898/2026.03.19.712954** (the source of the BioReason-Pro prediction) was not independently retrieved; the evaluation treats the prediction as stated in the seed context.

---

## Discriminating Tests

The following would most efficiently separate the seed hypothesis from the digestive-lysozyme interpretation:

1. **Enzymatic assay of recombinant LysB.** Measure muramidase activity on *Micrococcus lysodeikticus* cell walls vs endochitinase activity on a fluorogenic chitin substrate (e.g., 4-MU-chitotrioside) and on insoluble/colloidal chitin. Prediction: strong acidic-pH muramidase activity, negligible/only weak short-chitodextrin activity, no processive chitin degradation. This directly refutes GO:0004568.

2. **pH–activity profile.** Digestive insect lysozymes have acidic optima (~4.8, cf. housefly MdL1/MdL2, [PMID: 19099150](https://pubmed.ncbi.nlm.nih.gov/19099150/)). An acidic optimum supports a gut-digestive role.

3. **Infection-challenge transcriptomics.** RNA-seq/qPCR of LysB after septic injury vs oral bacterial feeding, in gut vs fat body. Prediction: no fat-body induction, repression in gut — inconsistent with an immune effector and with a negative regulator of immunity.

4. **Loss-of-function phenotype.** LysB knockdown/knockout scored for gut bacterial digestion/clearance and nutritional phenotype vs systemic immune-response readouts (AMP induction, survival to infection). Prediction: digestive/nutritional phenotype, not altered immune signaling.

5. **Structural superposition.** AlphaFold model of LysB superposed on HEWL (GH22) and on a GH18 chitinase (TIM-barrel). Prediction: RMSD-close to HEWL, fold-incompatible with the chitinase TIM-barrel.

6. **Comparative catalytic-residue mapping** across the Drosophila Lys cluster and canonical GH18/GH19 chitinases to confirm the absence of the chitinase catalytic glutamate context in all LysB-family members.

---

## Proposed Follow-up Actions (Curation Leads)

All items are **leads requiring curator verification.**

**Candidate action changes**
- **Reject** proposed GO:0004568 (chitinase activity) and GO:0045824 (negative regulation of innate immune response) — do not add.
- **Downgrade / flag** GO:0050829 (defense response to Gram-negative bacterium) as ISS-only, non-core, conflicting with digestive expression data.
- **Retain** GO:0003796 (lysozyme activity, MF) and GO:0005576 (extracellular region, CC) as core.
- **Consider adding** a digestion/bacteriophagy BP term (curator to select the exact term; e.g., a peptidoglycan catabolic / digestion term).

**Candidate references with snippets to verify**
- [PMID: 8159165](https://pubmed.ncbi.nlm.nih.gov/8159165/): "*four closely related genes, LysB, C, D and E, are all strongly expressed in the midgut of larvae and adults*" and "*None of the genes is expressed in the fat body or haemocytes.*" → supports digestive, refutes immune-effector.
- [PMID: 1588905](https://pubmed.ncbi.nlm.nih.gov/1588905/): "*have been recruited for the digestion of bacteria present in fermenting food*" → supports digestive; note transcription decreases after bacterial injection.
- [PMID: 17825580](https://pubmed.ncbi.nlm.nih.gov/17825580/): "*Lysozymes from family 22 of glycoside hydrolases are usually part of the defense system against bacteria*" → confirms GH22 family placement (distinct from chitinase families).
- UniProt Q08694 FUNCTION: "*Unlikely to play an active role in the humoral immune defense. May have a function in the digestion of bacteria in the food.*"

**Suggested curator questions**
- Should GO:0050829 remain given it is ISS-only and conflicts with midgut-digestive, infection-repressed biology?
- Is there an appropriate GO BP term for gut bacteriophagy/digestion that should replace the immune framing?
- Does FlyBase hold any direct enzymatic data on Q08694 that would confirm the acidic muramidase profile?

**Suggested experiments** — see Discriminating Tests above (recombinant muramidase-vs-chitinase assay; acidic pH profile; challenge transcriptomics; LOF phenotype; structural superposition).

---

## Bottom Line

LysB (Q08694) is a **GH22 C-type digestive lysozyme (muramidase, EC 3.2.1.17)**. The BioReason-Pro predictions of **chitinase activity (GO:0004568)** and **negative regulation of innate immune response (GO:0045824)** are **refuted / over-annotated**: the chitinase call is a fold/side-activity misassignment, and the immune-regulation call conflates a constitutive, infection-repressed, midgut-restricted digestive enzyme with an immune regulator. The pre-existing **GO:0050829** annotation is ISS-only and should be treated as low-confidence, non-core. Curators should retain **GO:0003796 (lysozyme activity)** and **GO:0005576 (extracellular region)** and consider adding a **digestion/bacteriophagy** BP term rather than any immune term.


## Artifacts

- [OpenScientist lysB fold check](openscientist_artifacts/artifacts_lysB_fold_check.md)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)