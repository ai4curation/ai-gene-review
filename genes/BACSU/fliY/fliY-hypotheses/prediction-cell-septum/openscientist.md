---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-10T04:21:00.782914'
end_time: '2026-07-10T04:30:42.085890'
duration_seconds: 581.3
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: BACSU
  gene: fliY
  gene_symbol: fliY
  uniprot_accession: P24073
  taxon_id: NCBITaxon:224308
  taxon_label: Bacillus subtilis (strain 168)
  focus_type: computational_prediction
  hypothesis_slug: prediction-cell-septum
  hypothesis_text: BioReason-Pro SFT predicts cell septum localization (GO:0030428)
    for the Bacillus subtilis protein fliY (P24073). Independently determine fliY's
    identity and domain architecture -- is it a flagellar motor-switch / C-ring component
    (CheC/FliM/FliN/FliY family) of the flagellar basal body -- and assess whether
    cell-septum (division site) localization is supported for it, or whether it localizes
    to the flagellar basal body / cytoplasmic membrane rather than the cell-division
    septum, which would make the cell-septum prediction a misassignment. Determine
    whether the prediction is supported or refuted.
  term_context: '- Term: cell septum (GO:0030428)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: BioReason-Pro SFT predicts cell septum localization\
    \ (GO:0030428) for the Bacillus subtilis\n  protein fliY (P24073). Independently\
    \ determine fliY's identity and domain architecture -- is it a flagellar\n  motor-switch\
    \ / C-ring component (CheC/FliM/FliN/FliY family) of the flagellar basal body\
    \ -- and assess\n  whether cell-septum (division site) localization is supported\
    \ for it, or whether it localizes to the\n  flagellar basal body / cytoplasmic\
    \ membrane rather than the cell-division septum, which would make the\n  cell-septum\
    \ prediction a misassignment. Determine whether the prediction is supported or\
    \ refuted.\nfocus_type: computational_prediction\nterm_id: GO:0030428\nterm_label:\
    \ cell septum\ncontext: []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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
- filename: fliY_GO_decision_table.md
  path: openscientist_artifacts/fliY_GO_decision_table.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist fliY GO decision table
- filename: fliY_provenance.md
  path: openscientist_artifacts/fliY_provenance.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist fliY provenance
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BACSU
- **Taxon:** Bacillus subtilis (strain 168) (NCBITaxon:224308)
- **Gene directory:** fliY
- **Gene symbol:** fliY
- **UniProt accession:** P24073

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-cell-septum
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

BioReason-Pro SFT predicts cell septum localization (GO:0030428) for the Bacillus subtilis protein fliY (P24073). Independently determine fliY's identity and domain architecture -- is it a flagellar motor-switch / C-ring component (CheC/FliM/FliN/FliY family) of the flagellar basal body -- and assess whether cell-septum (division site) localization is supported for it, or whether it localizes to the flagellar basal body / cytoplasmic membrane rather than the cell-division septum, which would make the cell-septum prediction a misassignment. Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: cell septum (GO:0030428)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: BioReason-Pro SFT predicts cell septum localization (GO:0030428) for the Bacillus subtilis
  protein fliY (P24073). Independently determine fliY's identity and domain architecture -- is it a flagellar
  motor-switch / C-ring component (CheC/FliM/FliN/FliY family) of the flagellar basal body -- and assess
  whether cell-septum (division site) localization is supported for it, or whether it localizes to the
  flagellar basal body / cytoplasmic membrane rather than the cell-division septum, which would make the
  cell-septum prediction a misassignment. Determine whether the prediction is supported or refuted.
focus_type: computational_prediction
term_id: GO:0030428
term_label: cell septum
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

**Gene:** *fliY* (UniProt **P24073**, FLIY_BACSU) — *Bacillus subtilis* strain 168 (NCBITaxon:224308)
**Focus type:** computational_prediction
**Hypothesis slug:** prediction-cell-septum
**Term under evaluation:** cell septum — **GO:0030428** (cellular component)
**Reference context:** doi:10.64898/2026.03.19.712954

---

## Summary

The BioReason-Pro SFT model predicts that *B. subtilis* FliY (P24073) localizes to the **cell septum (GO:0030428)**. This report evaluates that computational prediction against primary literature, curated database records, and independent public bioinformatics resources. **The prediction is refuted with high confidence.** FliY is the **flagellar motor-switch phosphatase** — a C-ring component of the flagellar basal body and a member of the CheC/FliM/FliN (FliN/MopA/SpaO) family. Its identity is established by a diagnostic three-part domain architecture, an aflagellate null-mutant phenotype, direct CheY-P phosphatase biochemistry, a solved family structure, and a switch-complex localization. Every localization datum places FliY at the flagellar basal-body C-ring on the cytoplasmic face of the plasma membrane, not at the mid-cell division site.

Three independent evidence streams converge. First, **primary literature** (five papers) ties FliY to the flagellum: a *fliY* null mutant has no flagella, FliY dephosphorylates CheY-P "at the location of its action, the flagellar switch," and structural work states plainly that "FliY is localized in the flagellar switch complex." Second, **curated annotation** (UniProt) names the protein "Flagellar motor switch phosphatase FliY" and annotates it to bacterial-type flagellum basal body (GO:0009425) and plasma membrane (GO:0005886). Third, **independent computed checks** run in this investigation — a live InterPro domain query and a STRING v12 interaction network — return only flagellar/T3SS domains and an interaction neighborhood composed entirely of flagellar and chemotaxis proteins, with zero cell-division genes and zero division-site domains.

The most plausible origin of the model error is not biological but lexical/structural: FliY carries the structural-superfamily label **"SpoA-like" (SSF101801)**, where "SpoA" means **Surface Presentation Of Antigens** — a type-III secretion system (T3SS) export-apparatus fold shared with the flagellar C-ring — **not** sporulation or septation. In *Bacillus*, a genus defined by sporulation and asymmetric septum formation, this token is an easy trap. Combined with a generic "oligomeric ring at the membrane" analogy shared between the flagellar C-ring and the cytokinetic FtsZ ring, it can readily produce a spurious "cell septum" call. Curators should reject GO:0030428 for this gene and affirm its flagellar CC, phosphatase MF, and chemotaxis/motility BP annotations.

---

## Key Findings

### Finding 1 — FliY is a flagellar motor-switch C-ring phosphatase, not a cell-division protein

*B. subtilis* FliY (P24073, 378 aa) is identified in UniProt as **"Flagellar motor switch phosphatase FliY."** Its domain architecture is diagnostic of the flagellar switch/C-ring and contains nothing associated with the divisome:

- **N-terminal CheC-like phosphatase domain** — Pfam **PF04509 (CheC)** / InterPro **IPR007597**
- **Middle FliM-like region**
- **C-terminal FliN-like C-ring domain** — Pfam **PF01052 (FliMN_C)** / InterPro **IPR001543**
- Family: **FliN/MopA/SpaO**

The genetics tie FliY unambiguously to the flagellum. A *fliY::cat* null mutant produces **no flagella**, and motility is restored by plasmid-borne *fliY* — a classic loss-of-function result placing the gene in flagellar function ([PMID: 1447979](https://pubmed.ncbi.nlm.nih.gov/1447979/)):

> "A fliY::cat null mutant has no flagella. Motility can be restored to the mutant by expression of fliY from a plasmid."

Biochemically, FliY is a **CheY-P phosphatase** acting at the flagellar switch. It resembles the *E. coli* switch protein FliN only in its C-terminal part, while an N-terminal domain is homologous to FliM and to CheC ([PMID: 12920116](https://pubmed.ncbi.nlm.nih.gov/12920116/)):

> "we have identified the phosphatase as FliY, which resembles E. coli switch protein FliN only in its C-terminal part, while an additional N-terminal domain is homologous to another switch protein FliM and to CheC."

Structurally and by localization, FliY resides in the flagellar switch complex ([PMID: 23532838](https://pubmed.ncbi.nlm.nih.gov/23532838/)):

> "FliY is localized in the flagellar switch complex, which also contains the stator-coupling protein FliG and the target of CheY-P, FliM."

UniProt subcellular-location annotations are **bacterial-type flagellum basal body (GO:0009425)** and **plasma membrane (GO:0005886, cytoplasmic side, peripheral)** — consistent with a C-ring protein attached to the MS-ring (FliF) at the base of the flagellar motor. There is no annotation to any division-site component.

### Finding 2 — The cell-septum (GO:0030428) prediction is refuted / a misassignment

No primary literature associates *B. subtilis* FliY with the **division septum, FtsZ ring, divisome, or cytokinesis**. Every localization datum — UniProt subcellular location, the structural study ([PMID: 23532838](https://pubmed.ncbi.nlm.nih.gov/23532838/)), and the switch-complex organization study ([PMID: 30455280](https://pubmed.ncbi.nlm.nih.gov/30455280/)) — places FliY at the **flagellar basal-body C-ring on the cytoplasmic side of the cell membrane**. The structural paper explicitly distinguishes FliY's location from that of its soluble homologs ([PMID: 23532838](https://pubmed.ncbi.nlm.nih.gov/23532838/)):

> "Unlike CheC and CheX, FliY is localized in the flagellar switch complex."

The domain content (CheC phosphatase + FliM + FliN; FliN/MopA/SpaO family) is **exclusively flagellar/T3SS-related** and contains **no division-site homology** — no FtsZ, FtsA, SepF, DivIVA, or SPOR domains. GO:0030428 (cell septum) would require the protein to be part of the division machinery localized to mid-cell; none of that is supported. This is a **category error**, not merely an overly broad or overly narrow term, so no qualifier can rescue it.

### Finding 3 — Independent computed provenance (InterPro + STRING) corroborates the flagellar C-ring, not the septum

Two independent public-resource checks were executed in this investigation, and both corroborate the flagellar assignment while excluding any division link:

- **InterPro (live query, P24073, 378 aa):** Returns only flagellar/T3SS domains — NCBIfam **NF005995 "flagellar motor switch phosphatase FliY"** (residues 3–374); **CheC-like phosphatase superfamily** (31–228) with two PF04509 catalytic lobes (36–72, 133–169); and a C-terminal **FliN C-ring domain PF01052** (298–368; IPR012826 "Flagellar motor switch FliN," 295–370). **No FtsZ/FtsA/SepF/DivIVA/SPOR division domains are present.**
- **STRING v12 (species 224308):** The top-30 functional partners are **all flagellar** (*fliM, fliG, fliF, fliN*-region, *flg\**, *flh\**) **or chemotaxis** (*cheY, cheC, cheA, cheW, cheD, cheV, cheB*) genes, each with a combined score **≥0.998**, and **zero cell-division genes** (no *ftsZ/ftsA/sepF/divIVA*).

The structural-superfamily label **"SpoA-like" (SSF101801, ~295–376)** is the **T3SS "Surface Presentation Of Antigens" fold**, not a sporulation/septation fold — the most likely lexical source of a septum misassignment.

---

## Mechanistic Model / Interpretation

FliY is a structural and catalytic component of the **flagellar switch complex (C-ring)** that caps the cytoplasmic face of the flagellar basal body. It performs two integrated jobs at that location:

1. **Switch/rotor structural role.** As a FliM/FliN-family C-ring protein it helps build the switch that controls the direction of flagellar rotation (CW/CCW), coupling to FliG (stator interaction) and FliM.
2. **CheY-P phosphatase.** Via its N-terminal CheC-like domain, FliY binds and dephosphorylates the chemotaxis response regulator CheY-P **at its site of action**, resetting the switching signal and tuning rotational bias.

This is spatially and functionally distinct from the cell-division septum. The two "rings" a model might confuse are contrasted below.

```
   FLAGELLAR C-RING (where FliY actually is)        CELL-DIVISION SEPTUM (GO:0030428 — where FliY is NOT)
   ------------------------------------------        ----------------------------------------------------
   Location: base of each flagellum, at the          Location: mid-cell division site
             cytoplasmic face of the membrane
   Core proteins: FliG, FliM, FliY/FliN,             Core proteins: FtsZ, FtsA, SepF, ZapA, DivIVA,
                  MS-ring (FliF), stators                            FtsW/FtsI, SPOR-domain proteins
   Function: rotation-direction switch +             Function: cytokinesis / septal peptidoglycan synthesis
             CheY-P dephosphorylation
   FliY domains present: CheC (PF04509),             Division domains present in FliY: NONE
             FliM-like, FliN (PF01052)
```

The prediction error is best explained as a **structural-analogy plus lexical artifact**: (i) both the flagellar C-ring and the cytokinetic Z-ring are membrane-proximal oligomeric rings, and (ii) the SCOP/structural label "SpoA-like" (T3SS Surface Presentation Of Antigens) superficially resembles sporulation/septation vocabulary — especially in *Bacillus*. Neither similarity constitutes evidence for septal localization.

### GO component comparison

| Attribute | Flagellar C-ring / basal body (FliY reality) | Cell septum (GO:0030428 prediction) |
|---|---|---|
| Supported by primary literature? | Yes (5 papers) | No |
| Supported by UniProt CC annotation? | Yes — GO:0009425, GO:0005886 | No |
| Supported by InterPro domains? | Yes — CheC + FliM + FliN | No division domains |
| Supported by STRING network? | Yes — all top partners flagellar/chemotaxis | No division partners |
| Verdict | **Correct** | **Refuted** |

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 1447979](https://pubmed.ncbi.nlm.nih.gov/1447979/) | Mutant phenotype, sequence | Refutes septum / supports flagellum | Is FliY a flagellar component? | *fliY::cat* null mutant has **no flagella**; plasmid *fliY* restores motility; FliY N-term ~FliM, C-term ~FliN | *B. subtilis*, in vivo | High; foundational identity paper |
| [PMID: 12920116](https://pubmed.ncbi.nlm.nih.gov/12920116/) | Direct assay + localization | Refutes septum / supports flagellum | Where and what does FliY act on? | FliY is the **CheY-P phosphatase** acting **at the flagellar switch**; FliM/CheC N-term + FliN C-term | *B. subtilis*, biochemical | High; defines activity and location |
| [PMID: 14749334](https://pubmed.ncbi.nlm.nih.gov/14749334/) | Direct assay (in vitro/in vivo) | Supports flagellum/chemotaxis | Is FliY a CheY-P phosphatase (CYX family)? | FliY (and CheC) hydrolyze CheY-P; FliY acts constitutively; CheD enhances CheC | *B. subtilis* | High; establishes phosphatase family |
| [PMID: 23532838](https://pubmed.ncbi.nlm.nih.gov/23532838/) | Structural + localization | Refutes septum / supports flagellum | Where does FliY localize; what is its fold? | FliY resembles FliM, dimerizes via FliN-like C-domain, and is **localized in the flagellar switch complex** ("Unlike CheC and CheX") | Family structure (*T. maritima*) applied to FliY | High; direct localization statement |
| [PMID: 30455280](https://pubmed.ncbi.nlm.nih.gov/30455280/) | Structural/organizational | Supports flagellum | How is the switch complex organized? | Maps the *B. subtilis* flagellar switch (FliG/FliM/FliY/FliN); CW/CCW control | *B. subtilis* | High; corroborates C-ring context |
| [PMID: 15546616](https://pubmed.ncbi.nlm.nih.gov/15546616/) | Structural/evolutionary | Qualifies/supports identity | Does FliY belong to the CheC phosphatase family? | FliY and FliM resemble CheC; **phosphatase activity attributed only to FliY** | *T. maritima* comparative | Medium-high; cross-species inference |
| [PMID: 17675386](https://pubmed.ncbi.nlm.nih.gov/17675386/) | Genetic/physiological | Supports flagellum/chemotaxis | Is FliY part of the CheC-FliY-CheX system? | Places FliY in the three-phosphatase system controlling rotational bias | *B. subtilis* / *E. coli* | Medium; contextual |
| UniProt P24073 (FLIY_BACSU) | Database | Refutes septum | Curated CC/MF | Name "Flagellar motor switch phosphatase"; CC = flagellum basal body + plasma membrane (cytoplasmic side) | Curated | Orientation-level; consistent with primary lit |
| InterPro (live query, this run) | Computational (domain) | Refutes septum | What domains does FliY contain? | Only flagellar/T3SS domains (NF005995, CheC PF04509, FliN PF01052); **no division domains** | Public resource, 378 aa | High for domain content |
| STRING v12 (species 224308, this run) | Computational (interaction) | Refutes septum | What are FliY's functional partners? | Top-30 all flagellar/chemotaxis (score ≥0.998); **zero division genes** | Public resource | High; unambiguous network |
| SCOP/SUPERFAMILY SSF101801 "SpoA-like" | Computational (structural class) | Competing / artifact source | Does "SpoA" imply sporulation/septum? | "SpoA" = T3SS **Surface Presentation Of Antigens**, not sporulation | Public resource | High; explains likely error origin |

---

## Evidence Base

- ***Identification and characterization of FliY, a novel component of the Bacillus subtilis flagellar switch complex.*** [PMID: 1447979](https://pubmed.ncbi.nlm.nih.gov/1447979/) — The foundational genetics: a *fliY* null mutant is aflagellate, establishing FliY as a flagellar (not division) gene.
- ***Bacillus subtilis hydrolyzes CheY-P at the location of its action, the flagellar switch.*** [PMID: 12920116](https://pubmed.ncbi.nlm.nih.gov/12920116/) — Identifies FliY as the CheY-P phosphatase and defines its FliN/FliM/CheC domain composition and switch location.
- ***Bacillus subtilis CheC and FliY are members of a novel class of CheY-P-hydrolyzing proteins in the chemotactic signal transduction cascade.*** [PMID: 14749334](https://pubmed.ncbi.nlm.nih.gov/14749334/) — Places FliY in the CYX CheY-P phosphatase family; FliY acts constitutively at the switch.
- ***Structure and activity of the flagellar rotor protein FliY: a member of the CheC phosphatase family.*** [PMID: 23532838](https://pubmed.ncbi.nlm.nih.gov/23532838/) — Direct structural + localization evidence: FliY resembles FliM and is localized in the flagellar switch complex, explicitly *unlike* soluble CheC/CheX.
- ***Organization of the Flagellar Switch Complex of Bacillus subtilis.*** [PMID: 30455280](https://pubmed.ncbi.nlm.nih.gov/30455280/) — Situates FliY within the CW/CCW rotational switch complex.
- ***Structure and function of an unusual family of protein phosphatases: the bacterial chemotaxis proteins CheC and CheX.*** [PMID: 15546616](https://pubmed.ncbi.nlm.nih.gov/15546616/) — Comparative structural work assigning phosphatase activity to FliY within the CheC fold.
- ***CheX in the three-phosphatase system of bacterial chemotaxis.*** [PMID: 17675386](https://pubmed.ncbi.nlm.nih.gov/17675386/) — Physiological context of the CheC-FliY-CheX phosphatase system.

Every paper supports the flagellar/chemotaxis identity of FliY. **None** provides any support for a cell-septum or divisome role, and no conflicting paper was found.

---

## GO Curation Implications (leads — require curator verification)

- **GO:0030428 (cell septum, CC): DO NOT ADD — reject the prediction.** Unsupported by any evidence; treat as a computational false positive / category error.
- **Retain / affirm CC:** **GO:0009425** (bacterial-type flagellum basal body) and **GO:0005886 / GO:0009898** (plasma membrane, cytoplasmic side) — supported by curated UniProt and family localization ([PMID: 23532838](https://pubmed.ncbi.nlm.nih.gov/23532838/), [PMID: 30455280](https://pubmed.ncbi.nlm.nih.gov/30455280/)). A more specific flagellar motor-switch/C-ring CC term is a defensible refinement over generic plasma membrane.
- **MF:** phosphoprotein phosphatase activity on CheY-P is well supported ([PMID: 12920116](https://pubmed.ncbi.nlm.nih.gov/12920116/), [PMID: 14749334](https://pubmed.ncbi.nlm.nih.gov/14749334/)); GO:0004721 is justified, and a more specific "response regulator / CheY-P dephosphorylation" framing is defensible.
- **BP:** chemotaxis (GO:0006935), flagellum assembly (GO:0044780), regulation of flagellum-dependent motility (GO:1902021), and dephosphorylation (GO:0016311) are appropriate.
- We deliberately avoid recommending "protein binding" (GO:0005515); more informative MF/BP/CC terms are supported.

---

## Mechanistic Scope

**Immediate molecular function:** FliY binds phosphorylated CheY (CheY-P) via a FliM-like N-terminal segment and dephosphorylates it through CheC-like active centers, terminating the chemotactic switching signal at its site of action — the flagellar C-ring. **Cellular location:** flagellar basal-body C-ring, peripherally attached to the MS-ring (FliF) on the cytoplasmic face of the membrane. **Downstream / pleiotropic effects (not the tested location):** swimming and swarming behavior, tumble bias, and chemotactic adaptation. None of these involve the cell-division septum. The seed hypothesis conflates the immediate CC (flagellar switch) with an unrelated CC (division septum).

---

## Conflicts and Alternatives

- **Paralog / lexical confusion (most likely cause).** The structural superfamily label **"SpoA-like" (SSF101801)** stands for **Surface Presentation Of Antigens**, a T3SS export-apparatus fold shared with the flagellar C-ring — **not** sporulation or septation. In *Bacillus*, a token-level match to "Spo"/septum is a plausible driver of the misprediction. This is an artifact, not competing biology.
- **Generic ring analogy.** The flagellar C-ring and the FtsZ division ring are both membrane-proximal cytoplasmic rings. A model reasoning "ring at membrane → division site" would err here.
- **Organism specificity.** *E. coli* lacks a FliY (it uses FliN + the phosphatase CheZ); *B. subtilis* FliY fuses FliM/FliN/CheC functions — but always in a flagellar context. No genuine division paralog of FliY exists.

No genuine competing evidence for GO:0030428 was identified.

---

## Limitations and Knowledge Gaps

1. **Native *B. subtilis* FliY imaging.** What was checked: UniProt CC and the structural/organizational papers. Why it matters: the refutation rests on switch-complex localization inferred from structure/complex composition rather than a dedicated FliY-fluorescent-fusion experiment explicitly excluding mid-cell signal. Resolving evidence: a FliY-GFP image showing peripheral/basal-body foci and absence of a mid-cell septal band, co-stained with FtsZ/DivIVA.
2. **Direct P24073 structure.** What was checked: family-level structures (largely *T. maritima*). Why it matters: the *B. subtilis* fold is inferred by strong homology. Resolving evidence: an AlphaFold model of P24073 confirming the CheC + FliN architecture (not run here).
3. **Reproducibility of the public-resource checks.** What was checked: a single live InterPro query and a single STRING v12 network. Why it matters: databases update; the negative result should be reproducible but was captured once. Resolving evidence: re-run and archive the raw JSON.
4. **Exact model-error trigger is inferred.** What was checked: candidate lexical/structural sources (SSF101801 "SpoA-like"). Why it matters: confirming the trigger improves error attribution. Resolving evidence: feature attribution / interpretability on the BioReason-Pro SFT input for P24073.

None of these gaps weaken the refutation; they concern only the mechanism of the model error and provenance completeness.

---

## Discriminating Tests

1. **FliY fluorescent-fusion localization (definitive).** Express FliY-GFP/mNeonGreen in *B. subtilis* and image: expect peripheral/basal-body puncta colocalizing with FliM/FliG, and **no enrichment at the FtsZ mid-cell band**. Co-stain with FtsZ or DivIVA to test septal exclusion directly.
2. **Divisome co-immunoprecipitation / BACTH.** Test FliY against FtsZ, FtsA, SepF, DivIVA. Predicted result: **no interaction** (consistent with STRING).
3. **Domain scan of P24073.** InterProScan/HMMER for any FtsZ/SepF/DivIVA/FtsA/SPOR domain — expect none (already confirmed by the live InterPro query).
4. **Reproduce public-resource provenance.** Re-run and archive InterPro (P24073) and STRING v12 (224308) outputs; confirm absence of division domains/partners.
5. **Model-error attribution.** Feature attribution on the BioReason-Pro SFT input to confirm whether the "SpoA-like"/"Spo" token or a structural-ring embedding drove the septum call.

---

## Curation Leads (require curator verification)

**Candidate references with exact snippets to verify:**

- [PMID: 1447979](https://pubmed.ncbi.nlm.nih.gov/1447979/) — "A fliY::cat null mutant has no flagella. Motility can be restored to the mutant by expression of fliY from a plasmid." (Supports flagellar identity; refutes division role.)
- [PMID: 12920116](https://pubmed.ncbi.nlm.nih.gov/12920116/) — "we have identified the phosphatase as FliY, which resembles E. coli switch protein FliN only in its C-terminal part, while an additional N-terminal domain is homologous to another switch protein FliM and to CheC." (Domain architecture + phosphatase.)
- [PMID: 23532838](https://pubmed.ncbi.nlm.nih.gov/23532838/) — "FliY is localized in the flagellar switch complex, which also contains the stator-coupling protein FliG and the target of CheY-P, FliM"; "Unlike CheC and CheX, FliY is localized in the flagellar switch complex." (Direct localization; refutes septum.)

**Candidate GO decision table:**

| Term | Aspect | Recommended action | Basis |
|---|---|---|---|
| GO:0030428 cell septum | CC | **Reject / do not add** | No literature, domain, or interaction support |
| GO:0009425 bacterial-type flagellum basal body | CC | **Retain / affirm** | Structure + localization |
| GO:0005886 / GO:0009898 plasma membrane (cytoplasmic side) | CC | **Retain** (consider specific flagellar motor-switch CC term) | UniProt CC; C-ring attachment |
| GO:0004721 phosphoprotein phosphatase activity (CheY-P) | MF | **Support / retain** | PMID 12920116, 14749334 |
| GO:0006935 chemotaxis; GO:1902021 regulation of flagellum-dependent motility | BP | **Support** | PMID 1447979, 17675386 |

**Suggested curator questions:**
- Is there any *B. subtilis* dataset (fluorescence, cryo-ET, proximity labeling) placing FliY at mid-cell? (Expected: no.)
- Was the septum prediction driven by the "SpoA-like" (T3SS SPOA) superfamily label or a ring-assembly analogy? Flag as a recurring failure mode for flagellar C-ring proteins.

**Suggested experiments:** FliY-GFP localization vs. FtsZ; BACTH/co-IP against divisome components (see Discriminating Tests).

---

## Conclusion

The cell-septum (GO:0030428) prediction for *B. subtilis* fliY (P24073) is **refuted**. FliY is the **flagellar motor-switch phosphatase**, a **CheC/FliM/FliN-family C-ring component** of the flagellar basal body that binds and dephosphorylates CheY-P on the cytoplasmic side of the plasma membrane. Five primary papers, curated UniProt annotations, and two independent computed checks (InterPro domain map; STRING interaction network) place it at the flagellar switch with **zero** support for a division-septum role. The misassignment most plausibly stems from the misleading **"SpoA-like" (T3SS Surface Presentation Of Antigens)** structural label and a generic membrane-ring analogy. Curators should **not** annotate FliY to cell septum and should instead affirm its flagellar CC, phosphatase MF, and chemotaxis/motility BP terms.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist fliY GO decision table](openscientist_artifacts/fliY_GO_decision_table.md)
- [OpenScientist fliY provenance](openscientist_artifacts/fliY_provenance.md)