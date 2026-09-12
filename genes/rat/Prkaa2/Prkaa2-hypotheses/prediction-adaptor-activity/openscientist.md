---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T06:34:37.742611'
end_time: '2026-07-11T06:46:50.902482'
duration_seconds: 733.16
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: rat
  gene: Prkaa2
  gene_symbol: Prkaa2
  uniprot_accession: Q09137
  taxon_id: NCBITaxon:10116
  taxon_label: Rattus norvegicus
  focus_type: computational_prediction
  hypothesis_slug: prediction-adaptor-activity
  hypothesis_text: GO-GPT (via BioReason-Pro) predicts protein-macromolecule adaptor
    activity (GO:0030674) for rat Prkaa2 (Q09137), the catalytic alpha-2 subunit of
    AMP-activated protein kinase (AMPK). Independently assess whether the AMPK alpha-2
    catalytic subunit has protein-macromolecule adaptor/scaffolding activity (bridging
    two macromolecules to bring them into proximity), or whether its molecular function
    is protein serine/threonine kinase activity, with the scaffolding/adaptor role
    in the AMPK heterotrimer belonging to the beta scaffold subunit rather than the
    catalytic alpha subunit -- which would make the adaptor-activity prediction a
    misassignment. Determine whether the prediction is supported or refuted.
  term_context: '- Term: protein-macromolecule adaptor activity (GO:0030674)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: GO-GPT (via BioReason-Pro) predicts protein-macromolecule\
    \ adaptor activity (GO:0030674) for\n  rat Prkaa2 (Q09137), the catalytic alpha-2\
    \ subunit of AMP-activated protein kinase (AMPK). Independently\n  assess whether\
    \ the AMPK alpha-2 catalytic subunit has protein-macromolecule adaptor/scaffolding\
    \ activity\n  (bridging two macromolecules to bring them into proximity), or whether\
    \ its molecular function is protein\n  serine/threonine kinase activity, with\
    \ the scaffolding/adaptor role in the AMPK heterotrimer belonging\n  to the beta\
    \ scaffold subunit rather than the catalytic alpha subunit -- which would make\
    \ the adaptor-activity\n  prediction a misassignment. Determine whether the prediction\
    \ is supported or refuted.\nfocus_type: computational_prediction\nterm_id: GO:0030674\n\
    term_label: protein-macromolecule adaptor activity\ncontext: []\nreference_id:\n\
    - doi:10.64898/2026.03.19.712954"
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
citation_count: 10
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

- **Organism code:** rat
- **Taxon:** Rattus norvegicus (NCBITaxon:10116)
- **Gene directory:** Prkaa2
- **Gene symbol:** Prkaa2
- **UniProt accession:** Q09137

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-adaptor-activity
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

GO-GPT (via BioReason-Pro) predicts protein-macromolecule adaptor activity (GO:0030674) for rat Prkaa2 (Q09137), the catalytic alpha-2 subunit of AMP-activated protein kinase (AMPK). Independently assess whether the AMPK alpha-2 catalytic subunit has protein-macromolecule adaptor/scaffolding activity (bridging two macromolecules to bring them into proximity), or whether its molecular function is protein serine/threonine kinase activity, with the scaffolding/adaptor role in the AMPK heterotrimer belonging to the beta scaffold subunit rather than the catalytic alpha subunit -- which would make the adaptor-activity prediction a misassignment. Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: protein-macromolecule adaptor activity (GO:0030674)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: GO-GPT (via BioReason-Pro) predicts protein-macromolecule adaptor activity (GO:0030674) for
  rat Prkaa2 (Q09137), the catalytic alpha-2 subunit of AMP-activated protein kinase (AMPK). Independently
  assess whether the AMPK alpha-2 catalytic subunit has protein-macromolecule adaptor/scaffolding activity
  (bridging two macromolecules to bring them into proximity), or whether its molecular function is protein
  serine/threonine kinase activity, with the scaffolding/adaptor role in the AMPK heterotrimer belonging
  to the beta scaffold subunit rather than the catalytic alpha subunit -- which would make the adaptor-activity
  prediction a misassignment. Determine whether the prediction is supported or refuted.
focus_type: computational_prediction
term_id: GO:0030674
term_label: protein-macromolecule adaptor activity
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

## Target: rat *Prkaa2* (Q09137), AMPK α2 catalytic subunit
## Hypothesis: `prediction-adaptor-activity` — GO:0030674 protein-macromolecule adaptor activity
## Focus type: computational_prediction
## Reference context: doi:10.64898/2026.03.19.712954

---

## Summary

The GO-GPT/BioReason-Pro prediction of **protein-macromolecule adaptor activity (GO:0030674)** for rat *Prkaa2* (Q09137), the AMP-activated protein kinase (AMPK) α2 **catalytic** subunit, is **refuted**. It is best classified as a **subunit-level mis-assignment / over-annotation**. The genuine molecular function of the AMPK α subunit is **protein serine/threonine kinase activity**; the adaptor/scaffolding role in the AMPK heterotrimer belongs to the **β** subunit.

Three independent lines of evidence converge. First, the Q09137 domain architecture is a canonical protein kinase (kinase domain res 16–268, catalytic proton-acceptor res 139, ATP-binding pocket res 22–30/45) plus an autoinhibitory sequence — with no carbohydrate-binding module, no glycogen-binding domain, and no dedicated scaffold module. Its high-confidence molecular-function annotations are all catalytic (GO:0004674, GO:0004672, GO:0004679), each supported by direct-assay (IDA) evidence. Second, structural and biochemical studies show the β subunit physically bridges α and γ, and that β's carbohydrate-binding module forms the ADaM interface with the α kinase domain; reviews explicitly name β "the scaffolding subunit."

Third and decisively, the IDA source paper anchoring the GO:0030674 annotation on Q09137 — PMID:15695819 — is a **β-subunit paper**. Its title and results describe the AMPK β subunit *tethering* α and γ via its C-terminal sequence (β1 residues 186–270). The experimentally demonstrated adaptor/tethering activity is a property of β, not of the α2 catalytic subunit that carries the annotation. The recommended curation action is to **remove GO:0030674 from *Prkaa2*** and, if preserved, transfer it to the AMPK β subunits (*Prkab1*/*Prkab2*). The α subunit's legitimate participation in heterotrimer assembly is already captured by GO:0044877 (protein-containing complex binding, IDA), which should be retained instead of adaptor activity.

---

## Key Findings

### Finding 1 — The core molecular function of Q09137 is protein Ser/Thr kinase activity, not adaptor activity

The domain architecture of UniProt Q09137 is that of a classical protein kinase: a protein kinase domain spanning residues 16–268, a catalytic active site (proton acceptor) at residue 139, an ATP-binding region (residues 22–30 and 45), and a C-terminal autoinhibitory sequence (AIS, residues ~291–376). There is **no carbohydrate-binding module (CBM), no glycogen-binding domain, and no dedicated scaffold/adaptor domain** anywhere in the α2 sequence. This is the signature of an enzyme, not a scaffold.

Consistent with this, the existing high-quality molecular-function GO annotations for Q09137 are all catalytic and supported by direct-assay evidence: **GO:0004674 protein serine/threonine kinase activity (IDA:RGD)**, **GO:0004672 protein kinase activity (IDA:RGD)**, and **GO:0004679 AMP-activated protein kinase activity (IDA:UniProtKB)**. Multiple primary and structural sources describe AMPKα as *the catalytic subunit* and AMPKβ as *the scaffold*.

Supporting quotations from the literature:

- [PMID:23721051](https://pubmed.ncbi.nlm.nih.gov/23721051/): "AMP-activated protein kinase (AMPK) is a sensor of energy status composed of a catalytic subunit (AMPKα), a scaffolding subunit (AMPKβ) and a regulatory subunit involved in nucleotide binding (AMPKγ)." — Explicitly assigns the catalytic role to α and the scaffolding role to β, directly contradicting adaptor activity for the α subunit.
- [PMID:20529674](https://pubmed.ncbi.nlm.nih.gov/20529674/): "The catalytic (alpha) subunit of AMPK/SNF1, Snf1 in yeast, contains a protein Ser/Thr kinase domain (KD), an auto-inhibitory domain (AID), and a region that mediates interactions with the two regulatory (beta and gamma) subunits." — Describes the α subunit as a Ser/Thr kinase with an autoinhibitory domain, consistent with kinase (not adaptor) as its molecular function.
- [PMID:26635351](https://pubmed.ncbi.nlm.nih.gov/26635351/): "AMP-activated protein kinase (AMPK) is a serine/threonine protein kinase that serves as a pleotropic regulator of whole body energy homoeostasis." — Confirms the enzyme's molecular function is serine/threonine protein kinase activity, carried by the catalytic α subunit.

### Finding 2 — The scaffold/adaptor role in the AMPK heterotrimer belongs to the β subunit

Structural studies establish that within the AMPK αβγ core, the **β subunit binds both α and γ**, physically bridging them. The β subunit's carbohydrate-binding module forms the ADaM (Allosteric Drug and Metabolite) site — the interaction surface between the α kinase domain and the β CBM. Reviews of AMPK structure identify β as "the scaffolding subunit." The α subunit contributes its kinase domain to that interface but does not itself act as the bridge.

Because the α subunit's contact with β during subunit assembly is a subunit-of-a-complex interaction rather than a bridging function between two *distinct* macromolecules, the appropriate molecular-function term for the α side of this interaction is **protein-containing complex binding (GO:0044877)** — which is already annotated to Q09137 by IDA:RGD — not GO:0030674 adaptor activity.

Supporting quotations:

- [PMID:18079111](https://pubmed.ncbi.nlm.nih.gov/18079111/): "The previously determined crystal structure of the core of mammalian alphabetagamma complex shows that beta binds alpha and gamma." — Demonstrates that the β subunit is the physical bridge between α and γ, i.e. the adaptor/scaffold, not α.
- [PMID:30478170](https://pubmed.ncbi.nlm.nih.gov/30478170/): "...binds the AMPK ADaM site, which forms the interaction surface between the kinase domain (KD) of the α-subunit and the carbohydrate-binding module (CBM) of the β-subunit." — Shows the α subunit contributes its kinase domain to the interface while the β CBM is the scaffolding module.

### Finding 3 — The IDA source (PMID:15695819) demonstrates adaptor activity of the BETA subunit, not α2

This is the decisive finding. QuickGO shows that the GO:0030674 (protein-macromolecule adaptor activity) annotation on Q09137 is a **single, rat-specific IDA assigned by RGD, referenced to PMID:15695819**. The annotation is **not** present on human PRKAA2 (P54646), on PRKAA1 orthologs, or on any AMPK β subunit (PRKAB1 Q9Y478, PRKAB2 Q9UGI9). This pattern — one isolated rat annotation, absent from orthologs and paralogs — is itself a red flag for a curation error.

Examination of the cited paper resolves the issue conclusively. PMID:15695819 (Iseli et al., 2005, *J. Biol. Chem.*) is titled ***"AMP-activated protein kinase beta subunit tethers alpha and gamma subunits via its C-terminal sequence (186-270)."*** The paper reports that the β subunit's conserved C-terminal 85-residue sequence (β1 186–270) "is the primary αγ binding sequence responsible for the formation of the AMPK αβγ heterotrimer." In other words, the experimentally demonstrated adaptor/tethering activity is a property of the **β** subunit. The α subunit is described as the catalytic subunit and merely provides a docking region (α1 313–473) that β binds.

Supporting quotations:

- [PMID:15695819](https://pubmed.ncbi.nlm.nih.gov/15695819/): "The conserved C-terminal 85-residue sequence of the beta subunit (90% between beta1 and beta2) is the primary alphagamma binding sequence responsible for the formation of the AMPK alphabetagamma heterotrimer." — The cited IDA source demonstrates that the adaptor/tethering activity bridging α and γ is a function of the **β** subunit, not the α2 catalytic subunit that carries the GO:0030674 annotation.
- [PMID:15695819](https://pubmed.ncbi.nlm.nih.gov/15695819/): "Truncation of the alpha subunit reveals that beta1 binding requires the alpha1-(313-473) sequence." — Shows the α subunit is a binding partner (provides a docking region) rather than the bridging adaptor, which is β.

---

## Mechanistic Model / Interpretation

The AMPK holoenzyme is an obligate αβγ heterotrimer with a clean division of molecular labor. The following schematic captures the assignment of function to subunit:

```
                    AMP / ADP / ATP
                          │
                          ▼
                   ┌──────────────┐
                   │   γ subunit  │   (nucleotide sensor; CBS/Bateman domains)
                   │  (Prkag1/2/3)│
                   └──────┬───────┘
                          │  bound by β C-terminus (186–270)
                          ▼
   ┌───────────────────────────────────────────────┐
   │              β subunit  (Prkab1/2)             │  ◄── ADAPTOR / SCAFFOLD
   │   CBM (glycogen binding) + C-terminal tether   │      GO:0030674 belongs HERE
   │   "tethers alpha and gamma"  (PMID:15695819)   │
   └───────────────────────────────────────────────┘
                          │  β binds α1 (313–473)
                          ▼
   ┌───────────────────────────────────────────────┐
   │           α subunit  (Prkaa2 = Q09137)         │  ◄── CATALYTIC
   │  Kinase domain (16–268) + AIS (291–376)        │      GO:0004674 kinase activity
   │  phosphorylates downstream substrates (pThr172)│      GO:0044877 complex binding
   └───────────────────────────────────────────────┘
                          │
                          ▼
              Ser/Thr phosphorylation of
        ACC, ULK1, TSC2, HMGCR, etc. (catabolic switch)
```

Function-to-subunit mapping:

| Subunit | Gene(s) | Primary molecular function | Correct MF GO term |
|---|---|---|---|
| α (catalytic) | *Prkaa2* (Q09137), *Prkaa1* | Protein Ser/Thr kinase; phosphorylates substrates; provides α1(313–473) docking region to β | **GO:0004674** protein serine/threonine kinase activity; GO:0004679 AMPK activity; GO:0044877 protein-containing complex binding |
| β (regulatory/scaffold) | *Prkab1*, *Prkab2* | **Scaffold/adaptor**: tethers α and γ; glycogen binding via CBM | **GO:0030674** protein-macromolecule adaptor activity |
| γ (regulatory) | *Prkag1/2/3* | Adenine-nucleotide sensing (CBS domains) | nucleotide binding |

The prediction under review takes a function that genuinely exists within the AMPK complex — an adaptor/scaffolding activity — and assigns it to the wrong subunit. The mechanistic error is category-level: the **α subunit is the enzyme that acts *on* substrates**, whereas the **β subunit is the structural glue that *holds the complex together*.** Being *bound by* a scaffold (as α is by β) does not confer adaptor activity on the bound partner. The distinction between GO:0044877 (this protein is part of / binds a complex) and GO:0030674 (this protein bridges two other macromolecules) is exactly the distinction that the annotation conflates.

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [15695819](https://pubmed.ncbi.nlm.nih.gov/15695819/) | Direct assay (interaction mapping) | **Refutes** (decisive) | Is adaptor activity a property of α2? | The **β** subunit C-terminal sequence (186–270) is the primary αγ-binding/tethering sequence; α provides only a docking region (α1 313–473) | Rat/mammalian AMPK subunit truncation & binding assays | High. This is the exact IDA source cited for GO:0030674 on Q09137 — and it is a β-subunit paper |
| [18079111](https://pubmed.ncbi.nlm.nih.gov/18079111/) | Structural | Refutes | Which subunit bridges α and γ? | Crystal structure of αβγ core: "beta binds alpha and gamma" | Mammalian AMPK core | High |
| [30478170](https://pubmed.ncbi.nlm.nih.gov/30478170/) | Structural | Refutes/Qualifies | Which module scaffolds the α kinase domain? | ADaM site = interface between α kinase domain and β CBM | Full-length AMPK crystal structures | High |
| [23721051](https://pubmed.ncbi.nlm.nih.gov/23721051/) | Review/database | Refutes | Which subunit is the scaffold? | "catalytic subunit (AMPKα), a scaffolding subunit (AMPKβ)" | AMPK review | Medium (review-level, but explicit subunit assignment) |
| [20529674](https://pubmed.ncbi.nlm.nih.gov/20529674/) | Review/biochemical | Supports (α = kinase) | What is the α subunit's domain content? | α = Ser/Thr kinase domain + AID + subunit-interaction region | Yeast SNF1/AMPK homolog | Medium-high |
| [26635351](https://pubmed.ncbi.nlm.nih.gov/26635351/) | Review/enzymology | Supports (α = kinase) | What is AMPK's molecular function? | "AMPK is a serine/threonine protein kinase" | α1/α2 heterotrimer enzymology | Medium-high |
| [17851534](https://pubmed.ncbi.nlm.nih.gov/17851534/) | Structural | Qualifies | Subunit architecture of SNF1 core | β glycogen-binding domain interacts with γ; α regulatory sequence sequestered by γ | Yeast SNF1 crystal structure | Medium (yeast) |
| QuickGO record (Q09137) | Database | Refutes (provenance) | Is GO:0030674 broadly supported? | Single rat-specific RGD IDA to PMID:15695819; absent from human PRKAA2, PRKAA1, and all β subunits | UniProt/QuickGO | High for provenance; database-level |

---

## GO Curation Implications

**Lead requiring curator verification:** Remove **GO:0030674 (protein-macromolecule adaptor activity)** from rat *Prkaa2* (Q09137).

Rationale for the recommended action:

1. **The MF term is mis-assigned at the subunit level.** GO:0030674 describes a bridging activity between two macromolecules. In the AMPK heterotrimer, this bridging is performed by the β subunit (PMID:15695819, PMID:18079111), not the α catalytic subunit.
2. **The supporting IDA does not support the annotation as placed.** PMID:15695819 experimentally demonstrates the β subunit's tethering function; it does not demonstrate adaptor activity for α2. The annotation therefore fails the "evidence supports the term for *this* gene product" test.
3. **The retained/strengthened MF terms should be the catalytic ones already present:** GO:0004674 (protein serine/threonine kinase activity, IDA), GO:0004672 (protein kinase activity, IDA), and GO:0004679 (AMP-activated protein kinase activity, IDA). These represent the α2 subunit's genuine, directly-assayed molecular function.
4. **The α-side of subunit assembly is already correctly captured** by GO:0044877 (protein-containing complex binding, IDA:RGD). This is the informative, non-"protein binding" term that describes the α subunit being incorporated into the heterotrimer.
5. **Optional transfer lead:** GO:0030674 is appropriately annotated to the AMPK **β** subunits (*Prkab1*/*Prkab2*), where the tethering activity was actually demonstrated. This is a separate curation action on a different gene product and should be verified independently.

### GO decision table

| Gene product | Term | Current | Recommended action | Basis |
|---|---|---|---|---|
| *Prkaa2* Q09137 | GO:0030674 adaptor activity | Present (RGD IDA, PMID:15695819) | **Remove** | Mis-assigned; source paper demonstrates β-subunit function |
| *Prkaa2* Q09137 | GO:0004674 Ser/Thr kinase activity | Present (IDA) | **Retain (core MF)** | Domain architecture + direct assay |
| *Prkaa2* Q09137 | GO:0004679 AMPK activity | Present (IDA) | Retain | Direct assay |
| *Prkaa2* Q09137 | GO:0044877 complex binding | Present (IDA) | Retain | Correctly captures α incorporation into heterotrimer |
| *Prkab1*/*Prkab2* (β) | GO:0030674 adaptor activity | Absent | **Candidate add** (verify) | PMID:15695819 demonstrates β tethers α and γ |

---

## Mechanistic Scope

The molecular function under test is **adaptor/scaffolding activity — the physical bridging of two distinct macromolecules to bring them into proximity.** This is an immediate, direct molecular property of a protein.

- **Direct α2 gene-product activity:** protein Ser/Thr kinase catalysis (phosphotransfer to substrate Ser/Thr residues), plus being incorporated into the αβγ complex via its α1(313–473)-equivalent docking region.
- **Not α2's direct activity (the seed's proposed adaptor role):** tethering α to γ — this is performed by the β subunit's C-terminal sequence.
- **Downstream / not molecular-function-level:** AMPK's roles in energy homeostasis, GLUT4 expression, mitochondrial biogenesis, autophagy regulation, and neuronal development (e.g., PMID:21233771, PMID:30359677, PMID:24295634) are *biological processes* driven by the kinase activity, not evidence for an adaptor molecular function.

The seed hypothesis correctly frames the discriminating question — is adaptor activity a property of the catalytic α subunit, or of the β scaffold? The evidence answers unambiguously: it is the β subunit's.

---

## Conflicts and Alternatives

- **Subunit confusion (the actual error):** The annotation conflates the α (catalytic) and β (scaffold) subunits. The source paper (PMID:15695819) is a β-subunit study; the annotation sits on the α2 gene product. This is the single most important conflict, and it resolves *against* the prediction.
- **"Complex binding" vs "adaptor activity":** A defensible-but-weaker alternative reading is that the α subunit's participation in the heterotrimer justifies some interaction term. This is true — but the correct term is GO:0044877 (already present), not GO:0030674. Adaptor activity requires bridging two *other* macromolecules, which α does not do.
- **Organism specificity / database carry-over:** The annotation is rat-specific (RGD) and does not propagate to the human ortholog (P54646) or to PRKAA1, indicating an isolated curation event rather than a robustly conserved, orthology-supported function.
- **No competing primary evidence found:** Across 33 papers reviewed, no primary study demonstrates that the AMPK α2 catalytic subunit acts as a macromolecular adaptor/scaffold bridging two other proteins. The consistent picture is α = kinase, β = scaffold.

---

## Limitations and Knowledge Gaps

1. **QuickGO/UniProt provenance was read from database records, not re-derived programmatically here.** The conclusion that the annotation is a single rat-specific RGD IDA to PMID:15695819 relies on database inspection; a curator should confirm the current annotation state directly in QuickGO/RGD, as annotations can be updated.
2. **Full text of PMID:15695819 was assessed via title and abstract-level evidence.** The subunit assignment is unambiguous from the title and reported results, but a curator verifying the removal should confirm the exact experimental claims in the full text.
3. **GO:0030674 definition edge cases.** Under the strict GO definition (bridging two *distinct* macromolecules), α does not qualify. If a curator interprets "adaptor activity" loosely to include any subunit that contributes an assembly interface, the interpretation should be confirmed against current GO documentation.
4. **β-subunit transfer not independently curated here.** The recommendation to add GO:0030674 to *Prkab1*/*Prkab2* is a lead, not a completed curation; it needs its own evidence review on those gene products.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

All items below are **leads requiring curator verification.**

**Action change (primary lead):**
- Remove **GO:0030674 (protein-macromolecule adaptor activity)** from *Prkaa2* / Q09137 (currently RGD IDA, PMID:15695819).

**Candidate reference with exact snippet to verify:**
- PMID:15695819 — verify: *"The conserved C-terminal 85-residue sequence of the beta subunit (90% between beta1 and beta2) is the primary alphagamma binding sequence responsible for the formation of the AMPK alphabetagamma heterotrimer."* and *"Truncation of the alpha subunit reveals that beta1 binding requires the alpha1-(313-473) sequence."* These confirm the adaptor function belongs to β, and that α is the bound partner.

**Retained / strengthened terms (verify present and well-evidenced):**
- GO:0004674 protein serine/threonine kinase activity (IDA) — core MF.
- GO:0004679 AMP-activated protein kinase activity (IDA).
- GO:0044877 protein-containing complex binding (IDA) — use instead of adaptor activity.

**Candidate new/transfer term (separate gene products, verify independently):**
- Consider GO:0030674 on *Prkab1* / *Prkab2*, where PMID:15695819 demonstrates the tethering activity.

**Discriminating tests to resolve any residual doubt:**
1. Subunit-swap / truncation binding assays (as in PMID:15695819): deleting β C-terminal 186–270 abolishes αγ tethering; α alone cannot bridge β and γ.
2. Structural interface mapping in existing full-length crystal structures (PMID:30478170, PMID:29480466): tabulate direct α–γ contacts; if α–γ contacts are β-mediated, α cannot be the adaptor.
3. In vitro reconstitution: test whether purified α2 can co-recruit two macromolecules without β (predicted: it cannot).
4. Orthology/annotation-conservation check: confirm GO:0030674 is absent on all α orthologs and addable on β orthologs.

**Suggested questions for the curator:**
- Does current QuickGO still show GO:0030674 on Q09137 as a single RGD IDA to PMID:15695819?
- Under the strict GO:0030674 definition, does contributing an assembly interface count as adaptor activity, or is bridging of two *distinct* macromolecules required? (This report assumes the latter.)

---

## Conclusion

The prediction that rat *Prkaa2* (AMPK α2 catalytic subunit, Q09137) has **protein-macromolecule adaptor activity (GO:0030674)** is **refuted**. The α2 subunit's genuine molecular function is **protein serine/threonine kinase activity**; the adaptor/scaffolding role in the AMPK heterotrimer is carried by the **β** subunit, and the very paper cited to support the annotation (PMID:15695819) is a demonstration of the **β subunit's** tethering activity. The GO:0030674 annotation should be **removed** from *Prkaa2* and, if preserved at all, transferred to the AMPK β subunits. This is a textbook example of a computational prediction producing a subunit-level mis-assignment by attaching a real complex-level function (scaffolding) to the wrong member of the complex.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)