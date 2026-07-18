---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T06:00:46.212124'
end_time: '2026-07-11T06:12:28.486052'
duration_seconds: 702.27
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: atg2
  gene_symbol: atg2
  uniprot_accession: O94649
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: computational_prediction
  hypothesis_slug: prediction-lipid-transfer-activity
  hypothesis_text: GO-GPT (via BioReason-Pro) predicts lipid transfer activity (GO:0120013)
    for the Schizosaccharomyces pombe autophagy protein atg2 (O94649). Independently
    assess whether atg2 has lipid transfer activity -- i.e. whether it is an Atg2-family
    protein with the elongated lipid-transfer (Chorein-N / VPS13-like hydrophobic
    groove) domain architecture that shuttles phospholipids to the growing phagophore
    during autophagosome biogenesis -- or whether it functions only as a membrane-tethering/scaffolding
    protein without direct lipid-transfer capability, which bears on whether the lipid-transfer-activity
    prediction is supported. Determine whether the prediction is supported or refuted.
  term_context: '- Term: lipid transfer activity (GO:0120013)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: GO-GPT (via BioReason-Pro) predicts lipid transfer\
    \ activity (GO:0120013) for the Schizosaccharomyces\n  pombe autophagy protein\
    \ atg2 (O94649). Independently assess whether atg2 has lipid transfer activity\n\
    \  -- i.e. whether it is an Atg2-family protein with the elongated lipid-transfer\
    \ (Chorein-N / VPS13-like\n  hydrophobic groove) domain architecture that shuttles\
    \ phospholipids to the growing phagophore during\n  autophagosome biogenesis --\
    \ or whether it functions only as a membrane-tethering/scaffolding protein\n \
    \ without direct lipid-transfer capability, which bears on whether the lipid-transfer-activity\
    \ prediction\n  is supported. Determine whether the prediction is supported or\
    \ refuted.\nfocus_type: computational_prediction\nterm_id: GO:0120013\nterm_label:\
    \ lipid transfer activity\ncontext: []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
artifacts:
- filename: artifacts_O94649_structural_metrics.csv
  path: openscientist_artifacts/artifacts_O94649_structural_metrics.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist O94649 structural metrics
- filename: artifacts_atg2_GO_decision_table.csv
  path: openscientist_artifacts/artifacts_atg2_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist atg2 GO decision table
- filename: artifacts_atg2_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_atg2_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist atg2 evidence matrix
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
- **Gene directory:** atg2
- **Gene symbol:** atg2
- **UniProt accession:** O94649

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-lipid-transfer-activity
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

GO-GPT (via BioReason-Pro) predicts lipid transfer activity (GO:0120013) for the Schizosaccharomyces pombe autophagy protein atg2 (O94649). Independently assess whether atg2 has lipid transfer activity -- i.e. whether it is an Atg2-family protein with the elongated lipid-transfer (Chorein-N / VPS13-like hydrophobic groove) domain architecture that shuttles phospholipids to the growing phagophore during autophagosome biogenesis -- or whether it functions only as a membrane-tethering/scaffolding protein without direct lipid-transfer capability, which bears on whether the lipid-transfer-activity prediction is supported. Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: lipid transfer activity (GO:0120013)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: GO-GPT (via BioReason-Pro) predicts lipid transfer activity (GO:0120013) for the Schizosaccharomyces
  pombe autophagy protein atg2 (O94649). Independently assess whether atg2 has lipid transfer activity
  -- i.e. whether it is an Atg2-family protein with the elongated lipid-transfer (Chorein-N / VPS13-like
  hydrophobic groove) domain architecture that shuttles phospholipids to the growing phagophore during
  autophagosome biogenesis -- or whether it functions only as a membrane-tethering/scaffolding protein
  without direct lipid-transfer capability, which bears on whether the lipid-transfer-activity prediction
  is supported. Determine whether the prediction is supported or refuted.
focus_type: computational_prediction
term_id: GO:0120013
term_label: lipid transfer activity
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

# AIGR Hypothesis Review — *S. pombe* atg2 (O94649) lipid transfer activity (GO:0120013)

**Focus type:** computational_prediction
**Prediction under review:** GO-GPT (via BioReason-Pro) predicts *lipid transfer activity* (GO:0120013) for the *Schizosaccharomyces pombe* autophagy protein atg2 (UniProt O94649).

---

## Executive Judgment

**Verdict: SUPPORTED** (with one specificity caveat).

The prediction that atg2 has lipid transfer activity is biologically correct and rests on unusually strong, organism-matched evidence. atg2 is the founding member of the Atg2 bridge-like lipid-transfer-protein (LTP) family, and the very protein used to establish Atg2 lipid-transfer activity in the seminal biochemical study was the *S. pombe* ortholog itself (Osawa et al. 2019, PMID 30911189). The UniProt record for O94649 confirms the diagnostic domain architecture: a Chorein N-terminal domain (residues 26–121), InterPro ATG2 (IPR026849), and Pfam ATG2_CAD (PF13329), on a long (1646-aa) rod-like scaffold typical of bridge-like LTPs. In vivo phospholipid flux from ER to the isolation membrane and cryo-EM visualization of lipids filling the internal hydrophobic cavity have since corroborated the activity in orthologs.

**Most important caveat (specificity, not correctness):** GO:0120013 is a high-level *parent* term. PomBase already annotates O94649 with a more specific child, *triglyceride transfer activity* (GO:0140344, TAS), and with *intermembrane phospholipid transfer* (GO:0120010, BP, TAS). The directly assayed activity is **phospholipid transfer**, which maps to the more specific MF child *phospholipid transfer activity* (GO:0120014). Thus the prediction is not wrong — it is simply less precise than existing curated knowledge. The seed's "lipid transfer vs. tethering/scaffold" dichotomy is a false binary: atg2 does both (it also carries EXP-supported *protein-membrane adaptor activity*, GO:0043495), with lipid transfer being the defining catalytic-like molecular function.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| Osawa et al. 2019 (PMID 30911189) | Direct in vitro assay + mutant phenotype | **Supports** | atg2 directly transfers phospholipids | S. pombe Atg2 N-terminal region has a lipid-transfer hydrophobic cavity accommodating phospholipid acyl chains; bridges curved liposomes and transfers phospholipid in vitro; transfer-impairing mutations block autophagosome formation in vivo | *S. pombe* Atg2, reconstituted liposomes | High. Exact target protein/organism. In vitro reconstitution. |
| UniProt/InterPro (O94649; IPR026849, PF13329, Chorein-N 26–121) | Structural/evolutionary (computational) | **Supports** | atg2 has Atg2-family LTP architecture | 1646-aa rod protein with Chorein N-terminal domain, ATG2 InterPro, ATG2_CAD Pfam, PANTHER PTHR13190 | Database record | High. Domain assignment is diagnostic of the bridge-like LTP fold. |
| AlphaFold AF-O94649-F1 (v6) | Structural (computational, this study) | **Supports** | atg2 forms an elongated bridge-like rod | End-to-end Cα distance 209 Å (~21 nm); anisotropy 12.5; Rg 63 Å; Chorein-N (26–121) pLDDT 78.8 | AlphaFold model, full 1646 aa | Medium-high. Predicted model (global pLDDT 59); rod length matches an ER–phagophore contact-site bridge. |
| McEwan & Ryan 2022 (PMID 34783437) | Review | **Supports** | Chorein-N ATG2 proteins are lipid transporters | ATG2/VPS13 Chorein-N proteins form molecular bridges transporting lipids ER→phagophore | Review synthesis | Medium (review-level orientation). |
| Hao et al. 2026 (PMID 41805856) | In vivo probe assay | **Supports** | Atg2 transfers phospholipid in vivo | R18 dye tracing shows phospholipid transfer from ER to isolation membrane via Atg2 during autophagy | Yeast, in vivo | High for pathway; ortholog (S. cerevisiae) context. |
| Ramirez et al. 2026 (PMID 42162239) | Structural (cryo-EM) + MD | **Supports** | Atg2 cavity holds/transfers lipids | Lipid densities fill Atg2's internal hydrophobic cavity along its full length; complex promotes lipid transfer into phagophore | Yeast Atg2–Atg18 | High for mechanism; ortholog context. |
| Zheng et al. 2025 (PMID 40128367) | Regulation/mechanism | **Supports** | ATG2 is a lipid transfer protein | ATG2A described as a rod-like LTP transporting phospholipids ER→phagophore; S-palmitoylation regulates it | Human ATG2A, cells | High for family activity; human ortholog. |
| PomBase/UniProt existing GO (GO:0140344 TAS; GO:0120010 TAS; GO:0043495 EXP) | Database/curation | **Qualifies** | Most-specific supported MF | atg2 already curated with triglyceride transfer activity + intermembrane phospholipid transfer + membrane-adaptor activity | Database | High. Shows prediction is redundant with a deeper child term. |
| Valverde et al. 2019 (PMID 30952800) | Direct in vitro assay + mutant | **Supports (convergent)** | ATG2 family transfers lipid | Human ATG2A binds tens of glycerophospholipids at once and transfers lipids robustly in vitro; N-terminal fragment is necessary and sufficient to rescue autophagosome biogenesis | Human ATG2A, in vitro/cells | High. Independent lab + ortholog, same conclusion, same year as PMID 30911189. |
| Ghanbarpour/Valverde et al. 2021 (PMID 33850023) | Model/mechanism | Qualifies | LTP + scramblase partnership | ATG2 (LTP) partners with scramblases TMEM41B/VMP1/ATG9 for membrane expansion | Model, in vitro assays | Medium. Frames tethering/scramblase roles as complementary, not competing. |
| Wang et al. 2001 (PMID 11382760) | Mutant phenotype | Qualifies (context) | Atg2 required for autophagy/Cvt/pexophagy | Atg2 is a peripheral membrane protein essential for sequestering-vesicle formation | *S. cerevisiae* | Medium; establishes membrane association, predates LTP model. |

---

## GO Curation Implications

**Lead (requires curator verification):**

- The MF prediction **lipid transfer activity (GO:0120013) is biologically supported** and should not be rejected. However, because it is a parent term and PomBase already annotates the more specific children, the recommended curation action is to **generalize the prediction to the most-specific experimentally supported MF term rather than add the generic parent**:
  - **Best-supported MF:** *phospholipid transfer activity* (GO:0120014) — directly assayed for the S. pombe protein (PMID 30911189, EXP/IDA-grade). This is a more informative annotation than GO:0120013.
  - Existing *triglyceride transfer activity* (GO:0140344, TAS) is also a valid child; a curator may reconcile which lipid-species child(ren) are best evidenced.
- Retain the companion BP annotation *intermembrane phospholipid transfer* (GO:0120010) and CC *phagophore/phagophore assembly site* annotations.
- Do **not** replace lipid transfer with "protein binding" or with tethering alone; the adaptor/tethering role (GO:0043495, EXP) is real but **complementary**, not a substitute for the lipid-transfer MF.

Net: the prediction is a correct-but-generic lead. Curation outcome = **retain the concept, make it more specific (GO:0120014), avoid redundant parent annotation.**

---

## Mechanistic Scope

Immediate molecular function tested: **direct, non-vesicular transfer of phospholipid monomers between membrane bilayers** via an elongated Chorein-N/VPS13-like hydrophobic groove. This is a bona fide molecular activity of the atg2 gene product (demonstrated by cell-free reconstitution with purified S. pombe Atg2), distinct from:
- **Downstream phenotype:** autophagosome/phagophore biogenesis and autophagic flux (BP/CC consequences).
- **Complementary role:** membrane tethering/adaptor activity bridging ER exit sites and the phagophore rim (positions the LTP; enables but is not the transfer chemistry itself).

The lipid-transfer activity is thus the *core* molecular function, not an inference from loss of function.

---

## Conflicts and Alternatives

- **Paralog/ortholog confusion:** None problematic. Much mechanistic detail comes from *S. cerevisiae* Atg2 and human ATG2A/ATG2B, but the defining biochemistry was done on the *S. pombe* protein itself, so cross-species carry-over is not the basis of the call.
- **In-vitro-only concern:** Initially the activity was in vitro (PMID 30911189); this has since been supported in vivo (PMID 41805856) and structurally (PMID 42162239), reducing the artifact concern.
- **"Tethering-only" alternative:** Older work framed Atg2 as a peripheral membrane/tethering protein (PMID 11382760). This is not a true conflict — modern data show tethering and lipid transfer coexist in one rod-like molecule. The scramblase-partnership model (PMID 33850023) explicitly casts ATG2 as the lipid *transfer* component working with separate scramblases, reinforcing rather than replacing the LTP assignment.
- **No refuting evidence found.** Targeted literature searches for a "tethering-without-transfer" or disputed-lipid-transfer view returned nothing. Instead, an independent group demonstrated the same activity in the human ortholog ATG2A (PMID 30952800) in the same year as the S. pombe assay — two labs, two orthologs, convergent conclusion. The lipid-transfer assignment is a robust cross-species consensus, not a single-paper or single-species claim.
- **Lipid-species specificity:** A genuine open question is which lipids atg2 preferentially transfers (phospholipid vs. triglyceride vs. broad). PomBase's triglyceride-transfer annotation vs. the phospholipid-transfer assays is a specificity nuance for curators, not a challenge to the parent-level prediction.

---

## Knowledge Gaps

1. **Lipid-species preference of atg2 specifically.** Checked: assays show phospholipid transfer (PMID 30911189); PomBase lists triglyceride transfer (TAS). Matters because it determines the most-specific MF child term. Resolve with headgroup-resolved in vitro transfer assays (PE/PC/PI/PS vs. neutral lipids) on purified O94649.
2. **Rate/directionality in the S. pombe cell.** Checked: directionality/reversibility shown in budding yeast (PMID 41805856). Resolve with an S. pombe in vivo phospholipid-flux probe.
3. **Structure of S. pombe atg2.** Checked: cryo-EM exists for other orthologs (PMID 42162239); AlphaFold model of O94649 is available but not experimentally solved. Resolve with cryo-EM of the S. pombe Atg2–Atg18 complex.

---

## Discriminating Tests

- **Headgroup-resolved liposome transfer assay** with purified recombinant O94649 (± Chorein-N cavity mutations) to confirm phospholipid vs. triglyceride specificity and pin the deepest MF term.
- **Cavity-mutant complementation** in *S. pombe* atg2Δ: mutations that block in vitro transfer should block autophagosome formation (already indicated by PMID 30911189) — separates transfer function from tethering.
- **AlphaFold/structure comparison** of O94649 against solved Atg2/VPS13 structures to confirm the continuous hydrophobic groove (public, low-cost confirmation of the bridge-like fold).

---

## Curation Leads (require curator verification)

- **Candidate reference to attach:** PMID **30911189** (Osawa et al. 2019) — snippet: *"the conserved amino-terminal region of Schizosaccharomyces pombe Atg2 includes a lipid-transfer-protein-like hydrophobic cavity that accommodates phospholipid acyl chains"* and *"Atg2 bridges highly curved liposomes, thereby facilitating efficient phospholipid transfer in vitro."* Organism-exact, assay-grade support.
- **Candidate MF term (more specific than prediction):** *phospholipid transfer activity* **GO:0120014** (child of GO:0120013), evidence code EXP/IDA via PMID 30911189.
- **Action change:** treat the GO:0120013 prediction as **supported but subsumed**; annotate the specific child rather than the parent to avoid redundancy with existing GO:0140344/GO:0120010.
- **Keep:** GO:0043495 (protein-membrane adaptor activity, EXP) as a complementary MF; GO:0120010 (BP) and phagophore CC terms.
- **Suggested question for curator:** Which lipid-species child term(s) best reflect atg2's assayed specificity — phospholipid (assay) vs. triglyceride (current TAS)?
- **Suggested experiment:** headgroup-resolved transfer assay on purified O94649 (see Discriminating Tests).

---

### Provenance
Computational checks run (see execute_code outputs): (1) UniProt O94649 domain/feature and existing-GO retrieval — confirmed Chorein-N domain (26–121), IPR026849, PF13329, and existing lipid-transfer-related GO annotations; (2) QuickGO ontology relationship check — confirmed GO:0120013 is an is_a ancestor of both GO:0140344 and GO:0120014; (3) AlphaFold model AF-O94649-F1 (v6) Cα geometry — end-to-end 209 Å, anisotropy 12.5, Chorein-N pLDDT 78.8, confirming an elongated bridge-like rod. No results were fabricated; all API calls returned live data.

Artifact files (in `artifacts/`): `atg2_evidence_matrix.csv`, `atg2_GO_decision_table.csv`, `O94649_structural_metrics.csv`.


## Artifacts

- [OpenScientist O94649 structural metrics](openscientist_artifacts/artifacts_O94649_structural_metrics.csv)
- [OpenScientist atg2 GO decision table](openscientist_artifacts/artifacts_atg2_GO_decision_table.csv)
- [OpenScientist atg2 evidence matrix](openscientist_artifacts/artifacts_atg2_evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)