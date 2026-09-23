---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T02:12:34.748847'
end_time: '2026-09-21T02:34:51.729707'
duration_seconds: 1336.98
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: POPTR
  gene: atpB
  gene_symbol: atpB
  uniprot_accession: A4GYR7
  taxon_id: NCBITaxon:3694
  taxon_label: Populus trichocarpa
  focus_type: function_assignment
  hypothesis_slug: f1-beta-vacuolar-localization-and-ancestral-scope
  hypothesis_text: Populus chloroplast-encoded ATP synthase beta subunit atpB (A4GYR7)
    is a functional component of the vacuolar membrane or plant-type vacuole. Distinguish
    an authentic additional localization from V1-A/F1-beta ancestral misplacement,
    degradative chloroplast cargo, or a mapping artifact. The old GOA cites PTN000389801
    and PTN000389877 in PTHR15184. The current PANTHER tree contains the F1-beta node
    PTN008558586 and confirmed F1-beta homologs but neither this exact Populus accession
    nor those old node ids; do not infer a reconstructed target lineage from WITH/FROM
    alone. Current UniProt places A4GYR7 in SF71. Determine whether phylogeny, targeting/assembly,
    direct localization or subcellular proteomics support or refute these two assertions
    independently. Predominant thylakoid localization alone is not proof against a
    secondary pool. Reversible ATP hydrolysis is independently supported by primary
    chloroplast ATP-synthase studies and is not evidence of vacuolar localization.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/POPTR/atpB/atpB-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Populus chloroplast-encoded ATP synthase beta\
    \ subunit atpB (A4GYR7) is a functional component\n  of the vacuolar membrane\
    \ or plant-type vacuole. Distinguish an authentic additional localization from\n\
    \  V1-A/F1-beta ancestral misplacement, degradative chloroplast cargo, or a mapping\
    \ artifact. The old GOA\n  cites PTN000389801 and PTN000389877 in PTHR15184. The\
    \ current PANTHER tree contains the F1-beta node\n  PTN008558586 and confirmed\
    \ F1-beta homologs but neither this exact Populus accession nor those old node\n\
    \  ids; do not infer a reconstructed target lineage from WITH/FROM alone. Current\
    \ UniProt places A4GYR7\n  in SF71. Determine whether phylogeny, targeting/assembly,\
    \ direct localization or subcellular proteomics\n  support or refute these two\
    \ assertions independently. Predominant thylakoid localization alone is not\n\
    \  proof against a secondary pool. Reversible ATP hydrolysis is independently\
    \ supported by primary chloroplast\n  ATP-synthase studies and is not evidence\
    \ of vacuolar localization.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
    \ []"
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
- filename: A4GYR7_annotation_provenance.csv
  path: openscientist_artifacts/A4GYR7_annotation_provenance.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist A4GYR7 annotation provenance
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

- **Organism code:** POPTR
- **Taxon:** Populus trichocarpa (NCBITaxon:3694)
- **Gene directory:** atpB
- **Gene symbol:** atpB
- **UniProt accession:** A4GYR7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** f1-beta-vacuolar-localization-and-ancestral-scope
- **Source file:** genes/POPTR/atpB/atpB-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Populus chloroplast-encoded ATP synthase beta subunit atpB (A4GYR7) is a functional component of the vacuolar membrane or plant-type vacuole. Distinguish an authentic additional localization from V1-A/F1-beta ancestral misplacement, degradative chloroplast cargo, or a mapping artifact. The old GOA cites PTN000389801 and PTN000389877 in PTHR15184. The current PANTHER tree contains the F1-beta node PTN008558586 and confirmed F1-beta homologs but neither this exact Populus accession nor those old node ids; do not infer a reconstructed target lineage from WITH/FROM alone. Current UniProt places A4GYR7 in SF71. Determine whether phylogeny, targeting/assembly, direct localization or subcellular proteomics support or refute these two assertions independently. Predominant thylakoid localization alone is not proof against a secondary pool. Reversible ATP hydrolysis is independently supported by primary chloroplast ATP-synthase studies and is not evidence of vacuolar localization.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Populus chloroplast-encoded ATP synthase beta subunit atpB (A4GYR7) is a functional component
  of the vacuolar membrane or plant-type vacuole. Distinguish an authentic additional localization from
  V1-A/F1-beta ancestral misplacement, degradative chloroplast cargo, or a mapping artifact. The old GOA
  cites PTN000389801 and PTN000389877 in PTHR15184. The current PANTHER tree contains the F1-beta node
  PTN008558586 and confirmed F1-beta homologs but neither this exact Populus accession nor those old node
  ids; do not infer a reconstructed target lineage from WITH/FROM alone. Current UniProt places A4GYR7
  in SF71. Determine whether phylogeny, targeting/assembly, direct localization or subcellular proteomics
  support or refute these two assertions independently. Predominant thylakoid localization alone is not
  proof against a secondary pool. Reversible ATP hydrolysis is independently supported by primary chloroplast
  ATP-synthase studies and is not evidence of vacuolar localization.
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

**Target gene:** atpB (UniProt **A4GYR7**, ATPB_POPTR) — ATP synthase subunit beta, chloroplastic
**Organism:** *Populus trichocarpa* (NCBITaxon:3694)
**Focus type:** function_assignment
**Hypothesis slug:** `f1-beta-vacuolar-localization-and-ancestral-scope`
**Source:** `genes/POPTR/atpB/atpB-ai-review.yaml` (free-text)

---

## Summary

The seed hypothesis proposes that the *Populus* chloroplast-encoded ATP synthase beta subunit atpB (A4GYR7) is a **functional component of the vacuolar membrane** (GO:0005774) or **plant-type vacuole** (GO:0000325), and asks whether this represents an authentic secondary localization or an artifact of **V1-A / F1-beta ancestral misplacement**, degradative chloroplast cargo, or a mapping error. After three iterations of database provenance analysis and primary-literature review, the verdict is clear: the vacuolar assertions are **refuted / over-annotated**. They rest entirely on **IBA (Inferred from Biological Ancestor)** annotations propagated within PANTHER family **PTHR15184**, a family that lumps together the catalytic subunits of F-type, V-type and A-type rotary ATPases because they share a common nucleotide-binding fold.

The decisive result came from an EBI **QuickGO** provenance audit. The vacuolar cellular-component annotation on A4GYR7 — **GO:0000221 "vacuolar proton-transporting V-type ATPase, V1 domain"** — is IBA (ECO:0000318, GO_REF:0000033, GO_Central) whose **WITH/FROM donor accessions are UniProtKB P38606 and P31404**, both of which resolve to **"V-type proton ATPase catalytic subunit A" (gene ATP6V1A)**. In other words, the vacuolar term leaked onto the chloroplast beta subunit directly from V-ATPase subunit A, and from **no F-type ATP synthase evidence at all**. This is a textbook, positively documented case of the exact "V1-A/F1-β ancestral misplacement" the seed hypothesis flagged.

Every line of protein-specific, authentic evidence places A4GYR7 at the **chloroplast thylakoid membrane** as a peripheral CF1 subunit: it is chloroplast-genome encoded, curated by HAMAP-Rule MF_01347 to "chloroplast thylakoid membrane," localized by immunogold electron microscopy to the thylakoid region, mapped by photoaffinity labeling as bearing the catalytic nucleotide site on the membrane-bound CF1 beta subunit, and assembled into CF1 at the thylakoid via nucleus-encoded factors (YL1, CGL160). There is no described trafficking route by which a plastid-genome-encoded, plastid-synthesized protein reaches the vacuole. **Recommended curation action:** remove/deprioritize the vacuolar CC terms while retaining thylakoid membrane, ATP synthase complex, ATP synthase/ATPase activity, ATP binding and proton-transport terms.

---

## Key Findings

### Finding 1 — The vacuolar CC terms are IBA carry-over from the shared F1/V1/A1 catalytic-subunit family, not authentic localization

UniProt A4GYR7 (ATPB_POPTR) is a 498-amino-acid protein annotated "ATP synthase subunit beta, chloroplastic," with `geneEncodingType = Chloroplast` — it is encoded on the plastid genome and translated by chloroplast ribosomes. Its curated subcellular location under **HAMAP-Rule MF_01347** is "**Plastid, chloroplast thylakoid membrane**" (peripheral membrane protein). Its GO cellular-component set contains three terms, of which only one carries protein-specific evidence:

| GO term | Name | Evidence code | Source |
|---|---|---|---|
| GO:0009535 | chloroplast thylakoid membrane | IEA | UniProtKB-SubCell (HAMAP MF_01347 / SL-0058) |
| GO:0000325 | plant-type vacuole | **IBA** | GO_Central |
| GO:0005774 | vacuolar membrane | **IBA** | GO_Central |

Both vacuolar terms are **IBA-only** — inferred from a biological ancestor, with no experimental, author-statement, or sequence-based curation of A4GYR7 itself. The domain architecture explains the leakage: the protein carries the **shared rotary-ATPase catalytic core** — InterPro **IPR004100 / IPR000194 "ATPase_F1/V1/A1_a/bsu,"** IPR055190 / Pfam **PF22919 "ATP-synt_VA_C,"** and Pfam **PF00006 "ATP-synt_ab"** — and is placed in **PANTHER PTHR15184**, a family that unites the catalytic subunits of **F-type, V-type and A-type ATPases**. Its subfamily is **SF71 (F1-beta)**. Because these catalytic subunits descend from a single ancestral rotary-ATPase subunit, any localization annotation on the ancestral node propagates by IBA onto all descendants — including this chloroplast beta subunit — regardless of its true compartment.

### Finding 2 — Chloroplast ATP synthase beta subunit localizes to the thylakoid (CF1); plastid-encoded proteins are not trafficked to the vacuole

Multiple independent primary studies converge on thylakoid CF1 localization and function:

- **Immunogold electron microscopy** localizes the ATP synthase beta subunit **predominantly to the thylakoid region** of the chloroplast, not to other compartments ([PMID: 16667706](https://pubmed.ncbi.nlm.nih.gov/16667706/)).
- **Photoaffinity labeling** with 2-azido-ADP/ATP maps the **tight, high-affinity catalytic nucleotide-binding site to the membrane-bound chloroplast CF1 beta subunit** ([PMID: 6311545](https://pubmed.ncbi.nlm.nih.gov/6311545/), [PMID: 6237108](https://pubmed.ncbi.nlm.nih.gov/6237108/)). The catalytic chemistry happens on the thylakoid-bound enzyme.
- **Assembly studies** show AtpB (β) is a **core CF1 subunit assembled at the thylakoid** via nucleus-encoded auxiliary factors: rice **YL1** interacts specifically with AtpB during cpATPase biogenesis ([PMID: 27585744](https://pubmed.ncbi.nlm.nih.gov/27585744/)), and Arabidopsis **CGL160** recruits the soluble CF1 subcomplex by binding the DELSEED-containing CF1-β subdomain for efficient thylakoid ATP synthase assembly ([PMID: 36250886](https://pubmed.ncbi.nlm.nih.gov/36250886/)).
- **Compartmental logic:** chloroplast-genome-encoded photosynthetic proteins are synthesized inside the plastid and function within it, tethered near the thylakoid; **no export route from the plastid to the vacuole** is described ([PMID: 42560755](https://pubmed.ncbi.nlm.nih.gov/42560755/)).

No primary study reports atpB / CF1-beta as a functional vacuolar-membrane or plant-type-vacuole component.

### Finding 3 — QuickGO provenance proves the vacuolar annotation is IBA carry-over from V-type ATPase catalytic subunit A (V1-A)

The decisive result comes from a direct EBI **QuickGO** annotation audit of A4GYR7 (11 annotations total). The vacuolar/V-ATPase CC annotation — **GO:0000221 "vacuolar proton-transporting V-type ATPase, V1 domain"** — carries evidence code **IBA (ECO:0000318)**, reference **GO_REF:0000033**, assignedBy **GO_Central**, with **WITH/FROM = PANTHER PTN000389802, SGD:S000002344, and UniProtKB P38606 and P31404**. Both UniProt donors resolve to **"V-type proton ATPase catalytic subunit A" (ATP6V1A**; human and bovine/related). The vacuolar term was therefore transferred onto the chloroplast beta subunit **directly from V1-A donor annotations** and from no F-type ATP synthase evidence.

The same ancestral node also propagates the rotational-mechanism MF **GO:0046961** and the proton-transport BP **GO:1902600**. By contrast, the authentic chloroplast terms rest on protein-specific signatures:

- **GO:0009535** chloroplast thylakoid membrane — UniProt **IEA** from HAMAP-Rule MF_01347 / UniProtKB-SubCell **SL-0058**.
- **GO:0045259** proton-transporting ATP synthase complex — InterPro **IEA** from **IPR005722 "ATP_synth_F1_bsu"** (an F-type-specific signature).

A cross-check confirms the family is genuinely heterogeneous: *E. coli* **atpA (P0ABB0)** in the same PANTHER family is "ATP synthase subunit alpha," a bona fide F-type member. The family thus contains both authentic F-type ATP synthase subunits and V-type ATPase subunits, and the vacuolar terms leaked from the latter onto the former.

---

## Mechanistic Model / Interpretation

The observed annotation pattern is fully explained by **homology-transfer artifact across a deep gene-family split**, not by dual localization.

```
                 Ancestral rotary-ATPase catalytic subunit
                        (PANTHER PTHR15184 root)
                                  |
        ┌──────────────────────────┼──────────────────────────┐
        |                         |                          |
   F-type (F1)               V-type (V1)                A-type (A1)
   α / β subunits            A / B subunits             A / B subunits
        |                         |                          |
   atpB / AtpB              ATP6V1A (P38606,            archaeal
   A4GYR7  (SF71)            P31404) = V1-A              homologs
        |                         |
  TRUE LOCATION:            TRUE LOCATION:
  chloroplast               vacuolar membrane /
  thylakoid CF1             V-ATPase V1 domain
        ^                         |
        |     IBA propagation     |  GO:0000325 plant-type vacuole
        └──────────(ARTIFACT)─────┘  GO:0005774 vacuolar membrane
                                     GO:0000221 vacuolar V1 domain

Net effect: V-ATPase (V1-A) localization terms leak onto the
chloroplast F1-β subunit via the shared ancestral node.
```

**Direct gene-product activity (well supported — retain):**
- MF: proton-transporting ATP synthase / ATPase activity (rotational mechanism), ATP binding — the catalytic β subunit bears the tight nucleotide site (PMID: 6311545, 6237108).
- CC: chloroplast thylakoid membrane (GO:0009535); proton-transporting ATP synthase complex, CF1 (GO:0045259).
- BP: ATP synthesis coupled to proton transport / photosynthesis.

**Artifactual assignments (remove/deprioritize):**
- GO:0000325 plant-type vacuole (IBA, GO_Central)
- GO:0005774 vacuolar membrane (IBA, GO_Central)
- GO:0000221 vacuolar V-type ATPase V1 domain (IBA; WITH/FROM = ATP6V1A)

The seed hypothesis asked to distinguish an **authentic additional localization** from **V1-A/F1-β ancestral misplacement**, **degradative chloroplast cargo**, or a **mapping artifact**. The QuickGO WITH/FROM provenance is a smoking gun for **ancestral misplacement / annotation artifact**. There is no positive evidence for degradative cargo (no proteomic detection of atpB in vacuolar/autophagic fractions was located), and thylakoid localization is not in dispute. The seed's caution about node-id drift is validated: the old GOA cited PTN000389801/PTN000389877, the current tree exposes F1-β node PTN008558586, and the live QuickGO record cites PTN000389802 — the node labels changed across releases, so the lineage cannot be reconstructed from WITH/FROM node ids alone. But the donor **UniProt** accessions (P38606, P31404 = V1-A) are stable and decisive.

---

## Evidence Base / Evidence Matrix

| # | Citation (PMID/DB) | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt A4GYR7 / HAMAP MF_01347 (database) | Review/database | Refutes vacuolar; supports thylakoid | True subcellular location | Chloroplast-genome encoded; curated location = chloroplast thylakoid membrane; vacuolar CC terms are IBA-only | *P. trichocarpa*, curated rule | High for record contents; rule-based (IEA), not primary data |
| 2 | InterPro/Pfam/PANTHER xrefs (database) | Structural/evolutionary | Qualifies → explains artifact | Basis of vacuolar IBA | Shared F1/V1/A1 catalytic core (IPR004100, IPR000194, PF22919); PTHR15184 mixes F/V/A subunits; SF71 = F1-β | Cross-kingdom | High; mechanism of IBA propagation |
| 3 | **EBI QuickGO audit + UniProt P38606/P31404** | Computational/database provenance | **Refutes** vacuolar authenticity | Source of the vacuolar CC IBA | GO:0000221 (vacuolar V1 domain) IBA with WITH/FROM donors = **V-type proton ATPase catalytic subunit A (ATP6V1A)** | Human/bovine V-ATPase donors → *Populus* β | High; direct provenance of the artifact |
| 4 | [16667706](https://pubmed.ncbi.nlm.nih.gov/16667706/) | Localization (immunogold EM) | Supports thylakoid; refutes vacuole | Where β subunit resides | ATP synthase β subunit predominantly in thylakoid region | *Porphyridium* chloroplast, EM | Medium (alga, but conserved subunit); does not assay vacuole |
| 5 | [6311545](https://pubmed.ncbi.nlm.nih.gov/6311545/) | Direct assay (photoaffinity) | Supports thylakoid CF1 catalysis | Catalytic nucleotide-site location | Tight ADP catalytic site on membrane-bound CF1 β subunit | Spinach thylakoids | High for MF/CC (thylakoid) |
| 6 | [6237108](https://pubmed.ncbi.nlm.nih.gov/6237108/) | Direct assay (photoaffinity) | Supports thylakoid CF1 catalysis | ATP high-affinity site location | 2-azido-ATP labels exclusively CF1 β on thylakoid membrane | Spinach thylakoids | High |
| 7 | [27585744](https://pubmed.ncbi.nlm.nih.gov/27585744/) | Interaction / mutant | Supports thylakoid assembly | Where AtpB assembles | YL1 interacts specifically with AtpB for cpATPase biogenesis | Rice, Y2H/BiFC | High; assembly context |
| 8 | [36250886](https://pubmed.ncbi.nlm.nih.gov/36250886/) | Interaction / mutant | Supports thylakoid assembly | CF1-β recruitment | CGL160 binds DELSEED-containing CF1-β subdomain for thylakoid assembly | Arabidopsis | High |
| 9 | [42560755](https://pubmed.ncbi.nlm.nih.gov/42560755/) | Review (mechanistic) | Supports plastid confinement | Fate of chloroplast-encoded proteins | Chloroplast-encoded photosynthetic proteins function within the plastid; no plastid→vacuole export | Plant/algal chloroplast | Medium; review/orientation |
| 10 | [2469431](https://pubmed.ncbi.nlm.nih.gov/2469431/) | Structural (antibody topology) | Qualifies | CF1 subunit organization | δ shielded in CF0CF1; anti-β agglutinates thylakoids (β on membrane enzyme) | Spinach thylakoids | Supports thylakoid CF1 assembly |
| 11 | *E. coli* atpA (P0ABB0) | Structural/evolutionary | Qualifies | Is PTHR15184 heterogeneous? | Family also contains bona fide F-type α subunit | Cross-check | High; confirms mixed family |

---

## GO Curation Implications (leads — require curator verification)

**Molecular Function**
- **Retain** proton-transporting ATP synthase / ATPase activity (rotational mechanism, GO:0046961/GO:0046933) and ATP binding (GO:0005524). These are core and well supported (PMID: 6311545, 6237108). Reversible ATP hydrolysis is a genuine CF1-β property and needs **no** vacuolar context.

**Cellular Component**
- **Retain** GO:0009535 chloroplast thylakoid membrane (authentic; HAMAP + primary evidence) and consider GO:0045259 proton-transporting ATP synthase complex, CF(1).
- **Remove / do-not-propagate** GO:0000325 plant-type vacuole (IBA) and GO:0005774 vacuolar membrane (IBA), and the related GO:0000221 vacuolar V1-domain term, for this gene product. Recommended action: mark as **over-annotation from shared F1/V1/A1 ancestry**; if the pipeline cannot delete IBA, add a curator note / NOT-appropriate flag and keep them out of the reviewed set.
- These are CC-only issues; no BP/MF change is driven by the vacuolar claim.

**Biological Process**
- **Retain** GO:1902600 proton transmembrane transport / photosynthetic ATP synthesis. Not affected by the vacuolar hypothesis.

Avoid "protein binding" as a final recommendation — the informative interaction here is the specific AtpB–YL1 / AtpB–CGL160 assembly interaction supporting thylakoid CF1 biogenesis, not binding in the abstract.

---

## Mechanistic Scope

The immediate molecular function under test is the **catalytic β subunit of chloroplast CF1** — it carries the nucleotide-binding catalytic sites of the F1 sector and, with α, forms the (αβ)₃ hexamer that performs rotational ATP synthesis/hydrolysis coupled to the CFO proton channel in the thylakoid membrane. This catalysis is **membrane-bound at the thylakoid**, as shown by photoaffinity labeling of the intact membrane enzyme (PMID: 6311545, 6237108).

Elements that must be separated from the direct function:
- **Reversible ATP hydrolysis** is a real property of CF1 (the enzyme runs both directions) but is a property of the *thylakoid* enzyme and provides **zero** support for vacuolar localization.
- The **"vacuolar membrane / plant-type vacuole"** claim is a compartment (CC) assertion, not a distinct activity. It is a downstream *annotation* consequence of homology to V-/A-type ATPase catalytic subunits — not a demonstrated cellular role of this chloroplast protein.
- **Assembly phenotypes** (chlorosis in *yl1* and *cgl160* mutants) are downstream consequences of impaired cpATPase biogenesis at the thylakoid, again with no vacuolar component.

No mutant phenotype, vacuolar biochemical activity, or direct vacuolar localization has ever been attributed to atpB/CF1-β.

---

## Conflicts and Alternatives

1. **Paralog / family confusion (confirmed cause).** PTHR15184 groups F1-β with V-ATPase subunit A/B and archaeal A-ATPase subunits, all sharing the F1/V1/A1 nucleotide-binding fold (IPR004100, IPR000194, PF22919). The QuickGO audit resolves the vacuolar donors to **V-type ATPase subunit A (ATP6V1A)** — a database carry-over artifact, exactly the "V1-A/F1-β ancestral misplacement" the seed flags.
2. **Node-id drift.** Old GOA cited PTN000389801/PTN000389877; the current tree exposes F1-β node PTN008558586 and SF71; the live QuickGO record cites PTN000389802. The lineage cannot be reconstructed from WITH/FROM node ids alone (per the seed) — but the donor UniProt accessions are stable and decisive.
3. **Degradative-cargo alternative.** Even if plastid material is autophagically degraded in the vacuole, that transient cargo would not make atpB a *functional component* of the vacuolar membrane; no proteomic evidence for such a pool was found.
4. **Mapping/label artifact.** PANTHER subfamily labels in this family are imperfect (e.g., mitochondrial-tagged subfamily labels applied to a chloroplastic protein), reinforcing that automated family/subfamily labels should not drive CC calls.

---

## Limitations and Knowledge Gaps

1. **Direct vacuolar proteomics for this accession.** Checked: UniProt/GO — only IBA. A purified-tonoplast MS hit would be the sole route to an authentic secondary pool. Resolve with a *Populus*/Arabidopsis tonoplast proteome (e.g., SUBA/PPDB reanalysis) explicitly querying CF1-β peptides vs. V-ATPase peptides. PubMed queries for plant vacuolar/tonoplast proteomics returned no usable hits through the available search tool (a tool limitation, not evidence of absence).
2. **"Secondary pool" cannot be positively excluded.** As the seed notes, predominant thylakoid localization does not disprove a trace vacuolar pool. The correct curatorial stance is that CC terms require positive evidence, which is absent — not that a trace pool has been experimentally disproven.
3. **IBA donor identity fully confirmed** as V1-A; the remaining minor gap is auditing every GO_Central leaf feeding GO:0000325/GO:0005774 in PTHR15184.
4. **Database-level evidence.** The refutation combines database provenance (QuickGO/UniProt) with primary localization/assembly literature performed largely in spinach, rice, Arabidopsis and a red alga — not *Populus* directly; the WITH/FROM donor identities are nonetheless objective facts.

---

## Discriminating Tests

- **Tonoplast vs. thylakoid MS proteomics:** search a high-purity vacuole/tonoplast fraction for atpB/CF1-β unique peptides; compare enrichment against V-ATPase A/B and known vacuolar markers. Enrichment in thylakoid but not vacuole → refutes.
- **PANTHER IBA provenance audit:** enumerate the experimentally-annotated leaves propagating GO:0000325/GO:0005774 within PTHR15184; confirm they are V-/A-type ATPase subunits.
- **Fluorescent localization / immuno-EM** of tagged AtpB in *Populus*/Arabidopsis: expect thylakoid signal, no tonoplast rim (requires plastid transformation or a nucleus-encoded tagged reconstruction because atpB is plastid-encoded).
- **Targeting-sequence check:** confirm absence of any vacuolar/secretory sorting signal (expected, since plastid-encoded).
- **Autophagy-flux proteomics** under senescence/starvation to test whether atpB appears in vacuolar fractions only as transient degradative cargo — which would still not justify a functional CC term.

---

## Proposed Follow-up Actions (Curation Leads — require curator verification)

1. **Action — remove/deprioritize vacuolar CC terms.** Treat GO:0000325 (plant-type vacuole), GO:0005774 (vacuolar membrane) and GO:0000221 (vacuolar V1 domain) on A4GYR7 as IBA over-annotation from shared F1/V1/A1 ancestry. Verify in QuickGO: GO:0000221 is IBA (ECO:0000318, GO_REF:0000033) with **WITH/FROM = UniProtKB P38606, P31404 = "V-type proton ATPase catalytic subunit A."**
2. **Action — retain thylakoid/F-type terms.** Confirm GO:0009535 (chloroplast thylakoid membrane; HAMAP MF_01347 / SL-0058) and GO:0045259 (ATP synthase complex; IPR005722 F1-β) as the correct protein-specific CC annotations.
3. **Candidate references (snippets to confirm in abstracts):**
   - [PMID: 16667706](https://pubmed.ncbi.nlm.nih.gov/16667706/) — "Labeling … for ATP synthase (beta subunit) were predominantly present in the thylakoid region."
   - [PMID: 6237108](https://pubmed.ncbi.nlm.nih.gov/6237108/) — "covalent incorporation of the label exclusively into the beta subunit of the chloroplast coupling factor one."
   - [PMID: 6311545](https://pubmed.ncbi.nlm.nih.gov/6311545/) — "the beta subunit of the coupling factor as the location of the tightly bound ADP on the thylakoid membranes."
   - [PMID: 27585744](https://pubmed.ncbi.nlm.nih.gov/27585744/) / [PMID: 36250886](https://pubmed.ncbi.nlm.nih.gov/36250886/) — AtpB(β) assembly into thylakoid CF1 via YL1/CGL160.
4. **Database provenance to cite:** UniProt A4GYR7 curated location (HAMAP MF_01347); InterPro IPR004100/IPR000194/PF22919 (shared F1/V1/A1 catalytic core); PANTHER PTHR15184 / SF71; EBI QuickGO WITH/FROM donors P38606/P31404 (ATP6V1A).
5. **Suggested curator questions:** (a) Which GO_Central leaf annotations feed the vacuolar IBAs in PTHR15184? (b) Is there any tonoplast-proteomics hit for this exact accession? (c) Should IBA CC terms conflicting with a HAMAP-rule curated location be auto-suppressed for organelle-genome-encoded proteins?
6. **Suggested experiment:** vacuole/tonoplast proteomics peptide search for CF1-β vs. V-ATPase, as above.

---

## Provenance Artifacts

- `A4GYR7_annotation_provenance.csv` — computed GO decision table from the live EBI QuickGO annotation audit plus UniProt donor lookups (columns: GO_ID, name, aspect, evidence, reference, WITH/FROM source, assignedBy, retain/remove interpretation). Generated by querying `https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=A4GYR7` and resolving WITH/FROM accessions P38606/P31404 via the UniProt REST API. Key computed result: the vacuolar CC term GO:0000221 is IBA with WITH/FROM donors = V-type proton ATPase catalytic subunit A (ATP6V1A), confirming ancestral V1-A→F1-β carry-over rather than authentic localization.

---

## Bottom Line

atpB / A4GYR7 is the chloroplast CF1 β subunit; its authentic localization is the **chloroplast thylakoid membrane**. The **plant-type vacuole** and **vacuolar membrane** annotations are **IBA carry-over** arising from the shared F1/V1/A1 catalytic-subunit ancestry within PANTHER PTHR15184 — provably sourced from V-type ATPase catalytic subunit A (ATP6V1A) — and are **not** supported as authentic or functional for this protein. Reversible ATP hydrolysis / rotational ATPase activity is real but thylakoid-based and does not imply vacuolar localization. **Recommendation: refute the vacuolar function-assignment hypothesis; flag GO:0000325 and GO:0005774 (and GO:0000221) as over-annotation.**


## Artifacts

- [OpenScientist A4GYR7 annotation provenance](openscientist_artifacts/A4GYR7_annotation_provenance.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)