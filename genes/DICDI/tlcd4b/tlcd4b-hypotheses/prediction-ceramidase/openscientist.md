---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-09T14:09:51.401589'
end_time: '2026-07-09T14:22:36.548777'
duration_seconds: 765.15
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: tlcd4b
  gene_symbol: tlcd4b
  uniprot_accession: Q550S9
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: computational_prediction
  hypothesis_slug: prediction-ceramidase
  hypothesis_text: BioReason-Pro SFT predicts N-acylsphingosine amidohydrolase (ceramidase)
    activity (GO:0017040) and ceramide metabolic process (GO:0006672) for the Dictyostelium
    discoideum protein tlcd4b (Q550S9). Independently assess whether tlcd4b -- a TLC
    (TRAM/LAG1/CLN8) domain-containing protein -- has the catalytic machinery of a
    ceramidase (N-acylsphingosine amidohydrolase), or whether the TLC-domain family
    lacks ceramidase catalytic activity (TLC-domain proteins function in lipid sensing/homeostasis
    and membrane biology and are distinct from the acid/neutral/alkaline ceramidase
    enzyme families), which would make the ceramidase-activity prediction a paralog/family
    misassignment. Determine whether the predictions are supported or refuted.
  term_context: '- Term: N-acylsphingosine amidohydrolase activity (GO:0017040)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: BioReason-Pro SFT predicts N-acylsphingosine amidohydrolase\
    \ (ceramidase) activity (GO:0017040)\n  and ceramide metabolic process (GO:0006672)\
    \ for the Dictyostelium discoideum protein tlcd4b (Q550S9).\n  Independently assess\
    \ whether tlcd4b -- a TLC (TRAM/LAG1/CLN8) domain-containing protein -- has the\
    \ catalytic\n  machinery of a ceramidase (N-acylsphingosine amidohydrolase), or\
    \ whether the TLC-domain family lacks\n  ceramidase catalytic activity (TLC-domain\
    \ proteins function in lipid sensing/homeostasis and membrane\n  biology and are\
    \ distinct from the acid/neutral/alkaline ceramidase enzyme families), which would\
    \ make\n  the ceramidase-activity prediction a paralog/family misassignment. Determine\
    \ whether the predictions\n  are supported or refuted.\nfocus_type: computational_prediction\n\
    term_id: GO:0017040\nterm_label: N-acylsphingosine amidohydrolase activity\ncontext:\
    \ []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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
citation_count: 7
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: tlcd4b_GO_decision_table.csv
  path: openscientist_artifacts/tlcd4b_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist tlcd4b GO decision table
- filename: tlcd4b_family_comparison.csv
  path: openscientist_artifacts/tlcd4b_family_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist tlcd4b family comparison
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
- **Gene directory:** tlcd4b
- **Gene symbol:** tlcd4b
- **UniProt accession:** Q550S9

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-ceramidase
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

BioReason-Pro SFT predicts N-acylsphingosine amidohydrolase (ceramidase) activity (GO:0017040) and ceramide metabolic process (GO:0006672) for the Dictyostelium discoideum protein tlcd4b (Q550S9). Independently assess whether tlcd4b -- a TLC (TRAM/LAG1/CLN8) domain-containing protein -- has the catalytic machinery of a ceramidase (N-acylsphingosine amidohydrolase), or whether the TLC-domain family lacks ceramidase catalytic activity (TLC-domain proteins function in lipid sensing/homeostasis and membrane biology and are distinct from the acid/neutral/alkaline ceramidase enzyme families), which would make the ceramidase-activity prediction a paralog/family misassignment. Determine whether the predictions are supported or refuted.

## Term and Decision Context

- Term: N-acylsphingosine amidohydrolase activity (GO:0017040)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: BioReason-Pro SFT predicts N-acylsphingosine amidohydrolase (ceramidase) activity (GO:0017040)
  and ceramide metabolic process (GO:0006672) for the Dictyostelium discoideum protein tlcd4b (Q550S9).
  Independently assess whether tlcd4b -- a TLC (TRAM/LAG1/CLN8) domain-containing protein -- has the catalytic
  machinery of a ceramidase (N-acylsphingosine amidohydrolase), or whether the TLC-domain family lacks
  ceramidase catalytic activity (TLC-domain proteins function in lipid sensing/homeostasis and membrane
  biology and are distinct from the acid/neutral/alkaline ceramidase enzyme families), which would make
  the ceramidase-activity prediction a paralog/family misassignment. Determine whether the predictions
  are supported or refuted.
focus_type: computational_prediction
term_id: GO:0017040
term_label: N-acylsphingosine amidohydrolase activity
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

# AIGR Gene Hypothesis Deep Research — Final Report

**Target gene:** *tlcd4b* (UniProt **Q550S9**), *Dictyostelium discoideum* (NCBITaxon:44689)
**Focus type:** computational_prediction
**Hypothesis slug:** prediction-ceramidase
**Predicted terms under test:** N-acylsphingosine amidohydrolase (ceramidase) activity (**GO:0017040**); ceramide metabolic process (**GO:0006672**)
**Prediction source:** BioReason-Pro SFT (ref doi:10.64898/2026.03.19.712954)

---

## Summary

The BioReason-Pro SFT model predicts that the *Dictyostelium discoideum* protein **tlcd4b (Q550S9)** has **N-acylsphingosine amidohydrolase (ceramidase) activity (GO:0017040)** and participates in the **ceramide metabolic process (GO:0006672)**. This investigation independently evaluates that prediction against sequence, domain, structural, comparative-genomic, and primary-literature evidence. The molecular-function prediction is **refuted**: tlcd4b is a **TLCD4-family TLC (TRAM/LAG1/CLN8) domain membrane protein**, not a member of any ceramidase enzyme family, and it lacks the catalytic machinery that every characterized ceramidase possesses. The prediction is best explained as a **paralog / protein-family misassignment** — a ceramide-*associated* membrane protein was mislabeled with the *catalytic* term for ceramide breakdown.

Three converging lines of evidence support this verdict. First, every domain-annotation resource assigns tlcd4b exclusively to the TLC/TLCD4 family (Pfam PF03798; six of six InterPro signatures TLC-family, zero ceramidase-family); UniProt states it "belongs to the TLCD4 family." Second, the three ceramidase enzyme classes each have a distinct, unrelated catalytic fold — acid (Ntn/CBAH hydrolase), neutral (Zn²⁺ carboxypeptidase-like), and alkaline (CREST-superfamily Zn²⁺-amidase with a conserved 3-His + Asp + Ser center) — none of which is a TLC domain, and tlcd4b contains none of these active-site constellations. Third, the *Dictyostelium* genome already encodes dedicated ceramidases in the correct families (neutral *dcd2A/B*, alkaline *dcd3A/B*, acid-type *dcd1A/B*), none of which is tlcd4b, so there is no missing enzymatic role for tlcd4b to fill.

The second predicted term, **ceramide metabolic process (GO:0006672)**, is at most **weakly and indirectly supported** and is **non-catalytic**. The human ortholog of this family, **TMEM56**, modulates ceramide (particularly hexosylceramide) levels and physically interacts with **ceramide synthase 2 (CerS2)** — a *regulatory* connection to ceramide metabolism, not an amidohydrolase activity. Accordingly, the curation recommendation is to **reject GO:0017040**, treat **GO:0006672 as non-core** (or replace it with a regulatory term such as regulation of ceramide metabolic process, or retain the existing lipid-homeostasis annotation), and keep the evidence-appropriate ER/membrane/lipid-homeostasis annotations. The principal caveat is that no direct enzymatic assay of tlcd4b exists; the refutation rests on strong domain/structural/comparative evidence plus family-level functional data, which is the appropriate and sufficient evidence class for a computational-prediction review.

---

## Executive Judgment

**Verdict: REFUTED (for the molecular-function prediction GO:0017040); WEAKLY / INDIRECTLY SUPPORTED and non-catalytic (for the biological-process prediction GO:0006672).**

tlcd4b is a small (257-residue), polytopic (6 transmembrane helices) membrane protein whose entire annotated domain content is the **TLC (TRAM/LAG1/CLN8) domain**. TLC-domain proteins act in lipid sensing/homeostasis and membrane biology; they are structurally and evolutionarily distinct from every known ceramidase enzyme family. The catalytic apparatus of ceramidases is absent from tlcd4b, and the genome contains dedicated ceramidase genes elsewhere. The prediction is therefore a paralog/family misassignment.

**Most important caveat:** No direct enzymatic assay of tlcd4b (positive or negative) exists. The refutation is inferential — grounded in family assignment, absence of catalytic signatures/residues, comparative genomics, structure prediction, and ortholog functional data — not in a biochemical demonstration that tlcd4b fails to hydrolyze ceramide. For a computational-prediction review this evidence class is expected and is sufficient to reject the MF prediction.

---

## Key Findings

### Finding 1 — tlcd4b is a TLCD4-family TLC-domain membrane protein, not a member of any ceramidase enzyme family

UniProt entry **Q550S9** describes a 257-amino-acid protein with **6 predicted transmembrane helices** and a single **TLC domain spanning residues ~44–243**. The domain assignments are internally consistent across every major resource: **Pfam PF03798 (TRAM_LAG1_CLN8)**, **InterPro IPR006634 (TLC domain) and IPR050846 (TLCD family)**, and **PROSITE profile PS50922 (TLC)**. The UniProt SIMILARITY line explicitly states the protein "belongs to the **TLCD4 family**." The existing GO annotation set comprises endoplasmic reticulum localization (IBA), membrane, and lipid homeostasis (IBA) — **no catalytic (enzymatic) annotation of any kind**.

This matters because every experimentally characterized ceramidase belongs to a family that is structurally and evolutionarily **unrelated** to the TLC domain:

- **Acid ceramidase (ASAH1):** an N-terminal-nucleophile (Ntn) / CBAH-type hydrolase.
- **Neutral ceramidase (ASAH2):** a Zn²⁺-dependent enzyme with a **carboxypeptidase-like fold**. As reviewed by [PMID: 24064302](https://pubmed.ncbi.nlm.nih.gov/24064302/): *"Neutral CDase contains a zinc ion in the active site that functions as a catalytic center, and the hydrolysis of the N-acyl linkage in ceramide proceeds through a mechanism that is similar to that described for zinc-dependent carboxypeptidase."*
- **Alkaline ceramidase (ACER):** a member of the **CREST superfamily** of integral-membrane hydrolases. As shown by [PMID: 36048828](https://pubmed.ncbi.nlm.nih.gov/36048828/): *"ACERs are members of the CREST superfamily of integral-membrane hydrolases. All CREST members conserve a set of three Histidine, one Aspartate, and one Serine residue."*

None of these families contains a TLC domain, and the TLC domain is not a hydrolase fold. Because family membership is the single most reliable predictor of catalytic activity for well-studied enzyme classes, the assignment of tlcd4b to the TLCD4 family is prima facie incompatible with the ceramidase prediction.

### Finding 2 — The TLCD4/TMEM56 family regulates ceramide metabolism through protein interaction, not by intrinsic ceramidase catalysis

The strongest functional evidence for the family's true role comes from the human ortholog **TMEM56** (the mammalian counterpart of *Dictyostelium* tlcd4b / tmem56b). [PMID: 42087192](https://pubmed.ncbi.nlm.nih.gov/42087192/) reports that this TRAM-LAG1-CLN8 domain protein *"modulates ceramide metabolism, particularly affecting levels of hexosylated ceramides"* and that *"Co-immunoprecipitation assays indicate that TMEM56 physically interacts with ceramide synthase 2 (CerS2), suggesting a role in lipid signaling pathways."* The same work links TMEM56 to SDF-1-mediated cell migration.

Critically, TMEM56 is described throughout as a **regulator** of ceramide metabolism — it changes ceramide levels by interacting with a biosynthetic enzyme (CerS2), **not** by directly hydrolyzing the N-acyl bond of ceramide. There is no report of intrinsic amidohydrolase/ceramidase catalytic activity anywhere in the TLCD4/TMEM56 family.

A targeted motif scan of the tlcd4b sequence (Q550S9) reinforces this: the protein contains **no Lag1/ceramide-synthase catalytic motif** (the RxxH…P…P constellation is absent) and only **7 histidines with no organized Zn-amidase active-site geometry**. It therefore possesses neither the ceramide-synthase acyltransferase machinery nor the ceramidase amidohydrolase machinery — consistent with a **non-catalytic, membrane-embedded regulatory/lipid-sensing role** rather than an enzymatic one.

This finding directly reframes the second predicted term (GO:0006672, ceramide metabolic process): the family is genuinely *associated* with ceramide metabolism, but as a modulator/regulator, which is a fundamentally different claim from possessing ceramidase catalytic activity.

### Finding 3 — Dictyostelium encodes dedicated ceramidases (dcd1/dcd2/dcd3) in the proper enzyme families; tlcd4b is not among them

A taxonomy-restricted UniProt search (taxon 44689, "ceramidase") returns **six dedicated ceramidase genes**, each mapping to a canonical ceramidase Pfam family:

| Gene | Accession | Length (aa) | Pfam family | Ceramidase class |
|------|-----------|-------------|-------------|------------------|
| dcd2A | Q54BK2 | 714 | PF04734 + PF17048 | Neutral ceramidase |
| dcd2B | Q55G11 | 718 | PF04734 + PF17048 | Neutral ceramidase |
| dcd3A | Q6TMJ1 | 288 | PF05875 | Putative alkaline ceramidase |
| dcd3B | Q55DQ0 | 285 | PF05875 | Putative alkaline ceramidase |
| dcd1A | Q55BZ5 | 441 | (acid-type) | Acid-type ceramidase |
| dcd1B | Q54CS6 | 500 | (acid-type) | Acid-type ceramidase |

**None of these is tlcd4b (Q550S9).** Conversely, InterProScan of Q550S9 returns **6 signatures, all TLC-family** (IPR006634, IPR050846, PF03798, PS50922, PANTHER PTHR13439, SMART SM00724) and **zero ceramidase-family signatures**. The genome thus already contains a full complement of bona fide ceramidases in the correct families; there is no functional "gap" that tlcd4b would need to fill, removing the parsimony argument that might otherwise motivate an unexpected ceramidase assignment.

Structural evidence agrees. The **AlphaFold model AF-Q550S9-F1 is high-confidence** (mean pLDDT 90.6; 95% of residues > 70) and depicts a **compact, multi-helical membrane bundle** consistent with a TLC lipid-handling fold — not the globular α/β hydrolase or Zn-carboxypeptidase architecture of a ceramidase active site.

Finally, historical biochemical work independently corroborates the family boundaries. [PMID: 10652340](https://pubmed.ncbi.nlm.nih.gov/10652340/) (neutral ceramidase purification) reports that *"the amino acid sequence of a fragment obtained from the purified enzyme was homologous to those deduced from the genes encoding an alkaline ceramidase of Pseudomonas aeruginosa and a hypothetical protein of the slime mold Dictyostelium discoideum. However, no significant sequence similarities were found in other known functional proteins including acid ceramidases."* The genuine *Dictyostelium* ceramidase homolog identified in these studies is a neutral/alkaline (dcd2-type) protein — a separate gene from the TLC protein tlcd4b. [PMID: 10781606](https://pubmed.ncbi.nlm.nih.gov/10781606/) similarly maps the human mitochondrial/nonlysosomal ceramidase to a distinct conserved protein family with a *Dictyostelium* homolog, again not a TLC protein.

---

## Mechanistic Model / Interpretation

The evidence supports a clear separation between **what tlcd4b is** and **what a ceramidase is**:

```
                    PREDICTED (BioReason-Pro SFT)          ACTUAL (evidence-based)
                    ------------------------------          -----------------------
 Molecular class    Ceramidase enzyme                       TLC-domain membrane protein
                    (N-acylsphingosine amidohydrolase)      (TLCD4 family)
 Fold / machinery   Catalytic hydrolase (Ntn / Zn-          6-TM helical bundle;
                    carboxypeptidase / CREST Zn-amidase)    TLC lipid-sensing domain;
                                                            NO catalytic center
 Reaction           Ceramide + H2O -> sphingosine +         None (non-catalytic)
                    free fatty acid
 Role in ceramide   Direct catabolism (bond cleavage)       Indirect regulation via
   metabolism                                               interaction with ceramide
                                                            synthase (CerS2 in ortholog)
```

**Why the prediction likely fired.** BioReason-Pro SFT appears to have keyed on the protein's genuine association with **sphingolipid / ceramide biology** — the TLC domain is co-named with CLN8 and LAG1, both connected to ceramide/sphingolipid pathways — and generalized from "ceramide-associated membrane protein" to the specific catalytic term "ceramidase." This is a textbook **frequency-bias / paralog-overannotation error**: a family that is *adjacent* to ceramide metabolism is misassigned the *catalytic* term for that pathway. The correct family-level function is **lipid homeostasis / regulation of ceramide metabolism via protein–protein interaction**, which the model collapsed into an enzyme activity it does not possess.

**Reconciling the two predicted terms.** GO:0017040 (ceramidase activity, MF) and GO:0006672 (ceramide metabolic process, BP) are not equally wrong. The MF term is refuted outright. The BP term captures a real, if indirect, biological association — but only in the sense that the family *regulates* ceramide pools. A curator should treat these as separable decisions.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|----------|---------------|-----------|--------------|-------------|---------|--------------------------|
| UniProt Q550S9 (database) | Structural/evolutionary (domain) | **Refutes** | tlcd4b is a ceramidase | 257 aa, 6 TM, TLC domain (44–243); Pfam PF03798; assigned to **TLCD4 family**; no catalytic GO | *D. discoideum*, in silico | High for family ID; database-level |
| InterProScan of Q550S9 | Computational | **Refutes** | tlcd4b has ceramidase signatures | 6/6 signatures TLC-family; 0 ceramidase signatures | in silico | High; signature-based |
| [PMID: 36048828](https://pubmed.ncbi.nlm.nih.gov/36048828/) | Structural/mechanistic (review of ACER) | **Refutes (family boundary)** | Ceramidases share TLC machinery | ACERs are CREST-superfamily Zn²⁺-amidases with conserved 3His+Asp+Ser; unrelated to TLC | Alkaline ceramidase family | High; establishes distinct active site |
| [PMID: 24064302](https://pubmed.ncbi.nlm.nih.gov/24064302/) | Structural/mechanistic (review of nCDase) | **Refutes (family boundary)** | Ceramidases share TLC machinery | Neutral CDase uses a Zn carboxypeptidase-like fold/mechanism; unrelated to TLC | Neutral ceramidase family | High; distinct fold |
| [PMID: 42087192](https://pubmed.ncbi.nlm.nih.gov/42087192/) | Interaction + lipidomics (ortholog) | **Qualifies** | Family role in ceramide metabolism | TMEM56 (TLCD4/TMEM56 ortholog) modulates ceramide levels, interacts with **CerS2**; no ceramidase activity reported | Human cells | Moderate–high; ortholog, not tlcd4b itself |
| UniProt taxon 44689 "ceramidase" search | Comparative genomics (database) | **Refutes** | tlcd4b is *the* Dictyostelium ceramidase | 6 dedicated ceramidases (dcd1/2/3) in canonical families; tlcd4b absent | *D. discoideum* | High; genome-level |
| AlphaFold AF-Q550S9-F1 | Structural (predicted) | **Refutes** | tlcd4b has a hydrolase fold | High-confidence (pLDDT 90.6) compact 6-helix membrane bundle; TLC-like, not hydrolase | in silico | Moderate–high; predicted structure, no ligand |
| [PMID: 10652340](https://pubmed.ncbi.nlm.nih.gov/10652340/) | Direct assay + sequence (historical) | **Refutes / competing** | Which Dictyostelium protein is the ceramidase | Purified neutral ceramidase is homologous to a *Dictyostelium* neutral/alkaline (dcd2-type) protein, not a TLC protein | Mouse liver + sequence homology | Moderate; homology assignment |
| [PMID: 10781606](https://pubmed.ncbi.nlm.nih.gov/10781606/) | Cloning + assay (historical) | **Qualifies / competing** | Ceramidase family identity | Human mitochondrial ceramidase homologous to a distinct conserved family incl. a *Dictyostelium* homolog; not TLC | Human, HEK293/MCF7 | Moderate |
| [PMID: 16086686](https://pubmed.ncbi.nlm.nih.gov/16086686/) | Review/context (CLN8/TLC) | **Qualifies** | TLC-domain function | TLC (TRAM/Lag1/CLN8) family has postulated roles in lipid synthesis, transport or sensing | Human EPMR brain | Low–moderate; contextual |

---

## GO Curation Implications

**Lead requiring curator verification.**

- **GO:0017040 — N-acylsphingosine amidohydrolase (ceramidase) activity (MF): DO NOT ANNOTATE / REJECT the prediction.** The evidence (family assignment, absence of any ceramidase signature, absence of catalytic-residue constellation, presence of dedicated ceramidase genes elsewhere in the genome, and family-level functional data) refutes direct ceramidase activity. This term should not be added on the basis of the BioReason-Pro SFT prediction.

- **GO:0006672 — ceramide metabolic process (BP): treat as NON-CORE and, if used at all, only as regulatory involvement.** The family is genuinely connected to ceramide metabolism, but as a **regulator** (via interaction with ceramide synthase), not as a ceramide-hydrolyzing enzyme. A more defensible, better-supported alternative is a regulatory term such as **"regulation of ceramide metabolic process" (GO:2000303)** or the existing **lipid homeostasis** annotation, supported at IBA/ISS grade. Curators should not use GO:0006672 to imply catalytic activity.

- **Retain the existing, evidence-appropriate annotations:** endoplasmic reticulum (CC, IBA), membrane (CC), and lipid homeostasis (BP, IBA). These correctly capture a non-catalytic, membrane-resident, lipid-homeostasis role.

- **Avoid "protein binding" as the terminal recommendation.** The most informative supported statement is a **TLC-domain lipid-homeostasis / regulator-of-ceramide-metabolism** characterization (via CerS interaction in the ortholog), which is more specific than generic binding.

---

## Mechanistic Scope

The immediate molecular function under test is **direct hydrolysis of the amide (N-acyl) bond of ceramide** to yield sphingosine and a free fatty acid (ceramidase / N-acylsphingosine amidohydrolase activity). This is a **catalytic** claim about the gene product itself.

The evidence indicates tlcd4b does **not** perform this reaction. What tlcd4b (and its family) actually contributes is upstream and **non-catalytic**: a multi-pass membrane TLC-domain protein that participates in **lipid sensing/homeostasis** and, at the family level, **modulates ceramide pools indirectly** by physically associating with a biosynthetic enzyme (ceramide synthase / CerS2 in the human ortholog). The observed changes in ceramide (and hexosylceramide) levels upon perturbation of the family member are therefore **downstream consequences of a regulatory interaction**, not the signature of an intrinsic amidohydrolase. Distinguishing these is central to the curation decision: a lipidomic phenotype in a knockout does not by itself license a catalytic MF annotation.

---

## Conflicts and Alternatives

- **Paralog / family misassignment (primary alternative, strongly favored).** The prediction most plausibly arises from conflating a ceramide-*associated* membrane protein with a ceramide-*hydrolyzing* enzyme. The genome-level presence of dedicated ceramidases (dcd1/2/3) shows the ceramidase function is carried by other genes.

- **Regulatory vs. catalytic (partial reconciliation).** The one genuine grain of truth in the prediction is the family's connection to ceramide metabolism (PMID 42087192). This supports a *regulatory* BP association but actively argues **against** the catalytic MF term, because the mechanism demonstrated is interaction-based, not enzymatic.

- **Ortholog-based inference caveat.** The functional data (TMEM56/CerS2 interaction) come from the human ortholog, not from tlcd4b directly. Organism-specific divergence is possible, but this weakens, not strengthens, the ceramidase claim — no ortholog in the family shows ceramidase activity.

- **Historical homology "false friend."** Older literature (PMID 10652340, 10781606) repeatedly notes a *Dictyostelium* protein homologous to neutral/alkaline ceramidases. A superficial reading could misattribute that homology to tlcd4b; in fact it refers to the dcd2-type genes, reinforcing that the true ceramidase is a different locus.

---

## Limitations and Knowledge Gaps

1. **No direct enzymatic assay of tlcd4b.** No published in vitro ceramidase assay (positive or negative) exists for Q550S9. *Checked:* literature and UniProt. *Why it matters:* a direct negative assay would convert a strong inferential refutation into a definitive one. *Resolution:* express and purify tlcd4b and assay for ceramidase activity across acid/neutral/alkaline pH with cation panels.

2. **No experimental structure.** The refutation of a hydrolase fold rests on the AlphaFold model (high confidence, but predicted, ligand-free). *Why it matters:* rules out an unexpected cryptic active site only inferentially. *Resolution:* experimental structure or structure-guided active-site mutagenesis.

3. **tlcd4b-specific functional data are absent in *Dictyostelium*.** Family function is inferred from the human ortholog TMEM56. *Why it matters:* *Dictyostelium*-specific roles (e.g., in phagosome ceramide enrichment; cf. [PMID: 29963848](https://pubmed.ncbi.nlm.nih.gov/29963848/)) are plausible but uncharacterized for this specific gene. *Resolution:* knockout/knock-in lipidomics and localization in *D. discoideum*.

4. **BP-term granularity.** Whether the correct term is "ceramide metabolic process," a regulatory child term, or simply "lipid homeostasis" is not fully resolved by current evidence. *Resolution:* curator judgment plus any *Dictyostelium* lipidomic phenotype.

---

## Discriminating Tests

1. **Direct ceramidase assay** on recombinant tlcd4b (fluorogenic or radiolabeled ceramide; acid/neutral/alkaline pH ± Zn²⁺/Ca²⁺). A clean negative would definitively refute GO:0017040; a positive would be extraordinary and require replication.
2. **Active-site residue audit** against the CREST 3His+Asp+Ser (ACER) and Zn-carboxypeptidase (nCDase) templates — structural superposition of AF-Q550S9-F1 onto solved ceramidase structures to confirm the absence of a catalytic constellation.
3. **Co-IP / proximity labeling in *Dictyostelium*** to test whether tlcd4b, like TMEM56, associates with a ceramide synthase (Lag1-family CerS), confirming a regulatory rather than catalytic role.
4. **Knockout lipidomics in *D. discoideum*** (compare with dcd1/dcd2/dcd3 knockouts): a ceramidase loss should raise ceramide/lower sphingosine; a regulator loss should shift ceramide-synthase-dependent species (e.g., hexosylceramides) as seen for TMEM56.
5. **Phylogenetic reconciliation** placing Q550S9 within the TLCD4 clade and confirming dcd1/2/3 occupy the ceramidase clades — formally demonstrating the misassignment.

---

## Proposed Follow-up Actions (Curation Leads)

All items below are **leads requiring curator verification.**

- **Action:** Reject/do-not-add **GO:0017040 (N-acylsphingosine amidohydrolase activity, MF)** from the BioReason-Pro SFT prediction — classify as **paralog/family overannotation**.
- **Action:** Down-rank **GO:0006672 (ceramide metabolic process, BP)** to non-core; if retained, replace with a **regulatory** term (e.g., **regulation of ceramide metabolic process, GO:2000303**) or keep the existing **lipid homeostasis** annotation, at IBA/ISS grade.
- **Retain:** ER (CC), membrane (CC), lipid homeostasis (BP).
- **Candidate references to verify with exact snippets:**
  - [PMID: 42087192](https://pubmed.ncbi.nlm.nih.gov/42087192/): *"TMEM56 physically interacts with ceramide synthase 2 (CerS2), suggesting a role in lipid signaling pathways."* → family is a regulator, not a ceramidase.
  - [PMID: 36048828](https://pubmed.ncbi.nlm.nih.gov/36048828/): *"ACERs are members of the CREST superfamily of integral-membrane hydrolases. All CREST members conserve a set of three Histidine, one Aspartate, and one Serine residue."* → ceramidase active site absent from TLC family.
  - [PMID: 24064302](https://pubmed.ncbi.nlm.nih.gov/24064302/): neutral ceramidase uses a Zn carboxypeptidase-like mechanism → distinct fold.
  - [PMID: 10652340](https://pubmed.ncbi.nlm.nih.gov/10652340/): genuine *Dictyostelium* ceramidase homolog is neutral/alkaline (dcd2-type), not TLC.
- **Suggested curator questions:** Is there any *Dictyostelium*-specific assay or phenotype for tlcd4b? Does the review already annotate dcd1/2/3 as the ceramidases? Should the BP term be a regulatory child term?
- **Suggested experiments:** direct ceramidase assay on recombinant Q550S9; active-site structural superposition; *Dictyostelium* knockout lipidomics and CerS co-IP.

---

## Evidence Base (Literature Summary)

| PMID | Title (abbrev.) | Role in this review |
|------|-----------------|---------------------|
| [42087192](https://pubmed.ncbi.nlm.nih.gov/42087192/) | *TMEM56 regulates cell migration by changing intracellular ceramide levels* | Defines the true family function: regulator interacting with CerS2, not a ceramidase |
| [36048828](https://pubmed.ncbi.nlm.nih.gov/36048828/) | *Alkaline ceramidase catalyzes hydrolysis via Zn²⁺-dependent amidase mechanism* | Establishes ACER/CREST active site distinct from TLC |
| [24064302](https://pubmed.ncbi.nlm.nih.gov/24064302/) | *Structure/mechanism of neutral ceramidase* | Establishes nCDase Zn-carboxypeptidase fold distinct from TLC |
| [10652340](https://pubmed.ncbi.nlm.nih.gov/10652340/) | *Neutral ceramidase from mouse liver* | Maps genuine Dictyostelium ceramidase to dcd2-type, not TLC |
| [10781606](https://pubmed.ncbi.nlm.nih.gov/10781606/) | *Human mitochondrial ceramidase cloning* | Ceramidase family distinct from TLC; separate Dictyostelium homolog |
| [16086686](https://pubmed.ncbi.nlm.nih.gov/16086686/) | *Sphingolipid changes in EPMR/CLN8* | Context: TLC (TRAM/Lag1/CLN8) family in lipid synthesis/transport/sensing |
| [29963848](https://pubmed.ncbi.nlm.nih.gov/29963848/) | *Ceramide synthase in phagocytosis* | Context: ceramide biology in Dictyostelium is synthase-driven |
| [20951822](https://pubmed.ncbi.nlm.nih.gov/20951822/) | *Sphingolipids and cisplatin sensitivity* | Context: Dictyostelium sphingolipid enzymology is well-characterized (S1P lyase, SK, CerS) |
| [15190000](https://pubmed.ncbi.nlm.nih.gov/15190000/) | *S1P lyase/SK and platinum drugs* | Context: dedicated sphingolipid enzymes in Dictyostelium |

---

## Bottom Line

The BioReason-Pro SFT ceramidase prediction for tlcd4b (Q550S9) is a **family/paralog misassignment** and should be **refuted** at the molecular-function level. tlcd4b is a TLCD4-family TLC-domain membrane protein with no ceramidase catalytic machinery; genuine ceramidase activity in *Dictyostelium* is encoded by dedicated genes (dcd1/dcd2/dcd3) in the canonical enzyme families. The only defensible remnant of the prediction is a **non-catalytic, regulatory association with ceramide metabolism**, mirroring the human ortholog TMEM56's interaction with ceramide synthase — which should be curated, if at all, as a regulatory/homeostasis role and never as ceramidase activity.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist tlcd4b GO decision table](openscientist_artifacts/tlcd4b_GO_decision_table.csv)
- [OpenScientist tlcd4b family comparison](openscientist_artifacts/tlcd4b_family_comparison.csv)