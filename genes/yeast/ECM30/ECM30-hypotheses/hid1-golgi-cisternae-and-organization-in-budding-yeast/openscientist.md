---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T05:19:11.242139'
end_time: '2026-09-21T05:46:01.670016'
duration_seconds: 1610.43
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: ECM30
  gene_symbol: ECM30
  uniprot_accession: Q06673
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: hid1-golgi-cisternae-and-organization-in-budding-yeast
  hypothesis_text: Saccharomyces cerevisiae ECM30 (Q06673) participates in Golgi organization
    and associates with medial/trans Golgi cisternae. Actual PANTHER treeinfo confirms
    leaf PTN001853777 descending from the asserted eukaryotic node PTN000491103. PMID:40899782
    experimentally establishes Golgi stacking for fission-yeast SPAC17A5.16/Hid1/Ftp105
    and explicitly notes divergent ECM30 and unstacked Golgi in budding yeast. Does
    this target divergence change the inherited functions, or do unstacked cisternae
    retain analogous organization/localization? Membrane includes peripheral association;
    lack of transmembrane helices, a cytoplasmic GFP pool and missing target experiments
    are not functional losses. Consider direct ECM30-Ubp15 complex/Gap1 sorting evidence
    (PMID:20620961 and PMID:20093466) separately from metazoan dense-core secretion.
    Evaluate specific functional retention/loss rather than donor count or ortholog
    labels.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/ECM30/ECM30-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Saccharomyces cerevisiae ECM30 (Q06673) participates\
    \ in Golgi organization and associates\n  with medial/trans Golgi cisternae. Actual\
    \ PANTHER treeinfo confirms leaf PTN001853777 descending from\n  the asserted\
    \ eukaryotic node PTN000491103. PMID:40899782 experimentally establishes Golgi\
    \ stacking for\n  fission-yeast SPAC17A5.16/Hid1/Ftp105 and explicitly notes divergent\
    \ ECM30 and unstacked Golgi in budding\n  yeast. Does this target divergence change\
    \ the inherited functions, or do unstacked cisternae retain\n  analogous organization/localization?\
    \ Membrane includes peripheral association; lack of transmembrane\n  helices,\
    \ a cytoplasmic GFP pool and missing target experiments are not functional losses.\
    \ Consider direct\n  ECM30-Ubp15 complex/Gap1 sorting evidence (PMID:20620961\
    \ and PMID:20093466) separately from metazoan\n  dense-core secretion. Evaluate\
    \ specific functional retention/loss rather than donor count or ortholog\n  labels.\n\
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
citation_count: 7
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** ECM30
- **Gene symbol:** ECM30
- **UniProt accession:** Q06673

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** hid1-golgi-cisternae-and-organization-in-budding-yeast
- **Source file:** genes/yeast/ECM30/ECM30-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae ECM30 (Q06673) participates in Golgi organization and associates with medial/trans Golgi cisternae. Actual PANTHER treeinfo confirms leaf PTN001853777 descending from the asserted eukaryotic node PTN000491103. PMID:40899782 experimentally establishes Golgi stacking for fission-yeast SPAC17A5.16/Hid1/Ftp105 and explicitly notes divergent ECM30 and unstacked Golgi in budding yeast. Does this target divergence change the inherited functions, or do unstacked cisternae retain analogous organization/localization? Membrane includes peripheral association; lack of transmembrane helices, a cytoplasmic GFP pool and missing target experiments are not functional losses. Consider direct ECM30-Ubp15 complex/Gap1 sorting evidence (PMID:20620961 and PMID:20093466) separately from metazoan dense-core secretion. Evaluate specific functional retention/loss rather than donor count or ortholog labels.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae ECM30 (Q06673) participates in Golgi organization and associates
  with medial/trans Golgi cisternae. Actual PANTHER treeinfo confirms leaf PTN001853777 descending from
  the asserted eukaryotic node PTN000491103. PMID:40899782 experimentally establishes Golgi stacking for
  fission-yeast SPAC17A5.16/Hid1/Ftp105 and explicitly notes divergent ECM30 and unstacked Golgi in budding
  yeast. Does this target divergence change the inherited functions, or do unstacked cisternae retain
  analogous organization/localization? Membrane includes peripheral association; lack of transmembrane
  helices, a cytoplasmic GFP pool and missing target experiments are not functional losses. Consider direct
  ECM30-Ubp15 complex/Gap1 sorting evidence (PMID:20620961 and PMID:20093466) separately from metazoan
  dense-core secretion. Evaluate specific functional retention/loss rather than donor count or ortholog
  labels.
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

# AIGR Gene Hypothesis Deep Research — ECM30 (Q06673), *Saccharomyces cerevisiae*

**Focus:** function_assignment — "hid1-golgi-cisternae-and-organization-in-budding-yeast"
**Source file:** `genes/yeast/ECM30/ECM30-ai-review.yaml`
**Target:** ECM30 / Q06673 (HID1/Ecm30 family, PANTHER PTHR21575:SF12)

---

## Executive Judgment

**Verdict: Partially supported but over-annotated for direct function assignment.**

The seed hypothesis proposes that budding-yeast ECM30 "participates in Golgi organization and associates with medial/trans Golgi cisternae." This report finds that these Golgi terms *do exist* on the UniProt/QuickGO record for Q06673, that ECM30 *is* a bona fide HID1-family ortholog, and that the phylogenetic anchoring the hypothesis cites (PANTHER leaf PTN001853777 under node PTN000491103) is real. **However**, every one of the Golgi-related Gene Ontology annotations on ECM30 — GO:0007030 (Golgi organization, BP), GO:0005797 (Golgi medial cisterna, CC), GO:0000138 (Golgi trans cisterna, CC), and GO:0016020 (membrane, CC) — carries the evidence code **IBA** (Inferred from Biological Ancestor, GO_REF:0000033, the PAINT phylogenetic pipeline). Not one is backed by a direct experiment in *S. cerevisiae*. The **only** experimentally derived localization for ECM30 in budding yeast is **cytoplasm** (GO:0005737, HDA from the genome-wide GFP-localization study PMID:14562095). ECM30's molecular function annotation is **ND** (no data), and PANTHER itself assigns no specific MF or BP to the family, leaving both at the ontology root.

The IBA Golgi terms propagate from **human HID1 (Q8IV36)**, which has genuine IDA (direct experimental) evidence for Golgi-cisterna localization and functions in trans-Golgi-network **large dense-core vesicle (LDCV) biogenesis and regulated secretion** — a metazoan-specific neuroendocrine process with **no counterpart in budding yeast**. The one primary experimental paper that directly addresses this family in a fungus, PMID:40899782 (Hooks et al., 2025), attributes a Golgi-*stacking maintenance* role specifically to a *Schizosaccharomyces pombe* HID paralog (SPAC17A5.16) and **explicitly notes that ECM30 is divergent and that budding-yeast Golgi is unstacked**. Because *S. cerevisiae* Golgi cisternae are natively dispersed/unstacked, the stacking function cannot even be assayed in this organism and cannot be transferred to ECM30.

**Bottom line for curation:** The Golgi terms are inference-level (IBA), anchored on a metazoan protein performing a process absent in yeast, and contradicted by the sole experimental datum (cytoplasm). They should be **retained only with an explicit "IBA / not experimentally verified in *S. cerevisiae*" caveat** (or the cisterna terms generalized to GO:0005794 "Golgi apparatus"), should **not** be promoted to experimental status, and should **not** ground a new core "Golgi organization" molecular/biological function. The better-supported functional leads for ECM30 — the UniProt cell-wall phenotype (ECM = Extracellular Mutant) and the physical association with the deubiquitinase **Ubp15** in the ART/Rsp5 ubiquitin-dependent permease-trafficking network — should be foregrounded instead.

---

## Key Findings

### F001 — ECM30's Golgi-cisterna GO terms are IBA-only; the sole experimental localization in *S. cerevisiae* is cytoplasm

UniProt Q06673 carries two Golgi-cisterna cellular-component annotations — **GO:0005797 (Golgi medial cisterna)** and **GO:0000138 (Golgi trans cisterna)** — and both are stamped with evidence code **IBA:GO_Central** (Inferred from Biological Ancestor). The membrane term **GO:0016020** is likewise IBA. In sharp contrast, the only experimentally grounded localization is **GO:0005737 (cytoplasm)**, supported by an HDA (high-throughput direct-assay) annotation from SGD. The UniProt FUNCTION comment reads "*Required to form the correct cell wall composition,*" reflecting the gene's original identification as an **E**xtra**c**ellular **M**utant. Sequence analysis shows **no transmembrane helices** (only five disordered regions), and the protein belongs to the HID1/Ecm30 family (InterPro IPR026705, Pfam PF12722, PANTHER PTHR21575).

Critically, these Golgi-cisterna IBA terms propagate from **human HID1 (Q8IV36)**, which *does* have IDA experimental evidence for GO:0005797 and GO:0000138 and functions in **trans-Golgi-network large dense-core vesicle (LDCV) biogenesis and regulated secretion** — a metazoan neuroendocrine process that has no equivalent in budding yeast. The IBA machinery propagates the *localization label* down the tree but cannot propagate the *biological context*, which is precisely where the assignment breaks down for ECM30.

### F002 — The Golgi-stacking structural role is fission-yeast-specific; budding-yeast Golgi is unstacked and ECM30 is explicitly flagged as divergent

The single most directly relevant primary paper, **PMID:40899782** (Hooks et al., 2025), used transmission electron microscopy to show that a *Schizosaccharomyces pombe* HID paralog mutant (SPAC17A5.16) "*lacks a stacked Golgi apparatus (GA) form, suggesting a role in maintaining GA structure.*" The paper documents that *Schizosaccharomyces* **uniquely expanded** the HID family to three paralogs, whereas other eukaryotes are monogenic, and that Dikarya (including *S. cerevisiae*) retained HID (ECM30) but lost the related DYM gene. Because budding-yeast Golgi cisternae are **natively unstacked and dispersed**, a stacking-maintenance function is not assayable in *S. cerevisiae* and is not transferable to ECM30. The paper's own framing — explicitly naming ECM30 as divergent alongside the unstacked budding-yeast Golgi — directly undercuts a simple ortholog-based transfer of the metazoan/fission-yeast Golgi-structural role.

> Verified quote (PMID:40899782): "*Transmission electron microscopy revealed that the SPAC17A5.16 mutant lacks a stacked Golgi apparatus (GA) form, suggesting a role in maintaining GA structure.*"

This finding is the crux of the discriminating logic: even the closest experimental evidence for a Golgi-organization role in a fungus is paralog-specific and organism-specific, and its authors flag ECM30 as the divergent case.

### F003 — The ECM30–Ubp15 / Gap1 link rests on high-throughput network datasets, supporting endomembrane trafficking rather than Golgi structural organization

The two PMIDs the seed hypothesis cites as "direct ECM30–Ubp15/Gap1 sorting evidence" are, on inspection, **genome-scale network datasets, not targeted assays**. **PMID:20620961** (Benschop et al., *Molecular Cell* 2010) is a mass-spectrometry-derived "consensus of core protein complex compositions" describing 409 complexes; it places ECM30 with Ubp15 by co-complex membership. **PMID:20093466** (Costanzo et al., *Science* 2010) is the genome-scale genetic-interaction map ("The genetic landscape of a cell"); it clusters ECM30 by genetic-interaction profile, not by a direct Gap1-trafficking experiment. Neither is a mechanistic Gap1-sorting assay. This does not refute a trafficking role — indeed it points toward one — but it means the ECM30–Ubp15 relationship is **association-level evidence** for a trafficking-cofactor role, not direct evidence for Golgi structural organization.

### F004 — PANTHER assigns ECM30 only a Golgi-cisterna CC term; molecular function and biological process remain root-level (unknown)

PANTHER v19 geneinfo maps Q06673 to family **PTHR21575**, subfamily **PTHR21575:SF12**. The GO-slim cellular-component annotations are "Golgi cisterna" (GO:0031985), "Golgi trans cisterna" (GO:0000138), and "membrane" (GO:0016020). Decisively, the **molecular_function annotation is GO:0003674 (root)** and the **biological_process annotation is GO:0008150 (root)** — meaning PANTHER assigns **no specific MF or BP** to this family/subfamily at all. The phylogenetic resource that anchors the hypothesis therefore supports, at most, a Golgi-cisterna *localization* label and offers no positive evidence for a "Golgi organization" biological process or any molecular activity.

### F005 — ECM30's partner Ubp15 functions in ubiquitin-dependent endocytic membrane-protein trafficking (ART–Rsp5 network), supporting a trafficking-cofactor role over Golgi structural organization

**PMID:28298493** (Ho, MacGurn & Emr, *Mol Biol Cell* 2017) establishes that "*the stability of ARTs is regulated by the deubiquitinating enzymes (DUBs) Ubp2 and Ubp15. By counteracting the E3 ubiquitin ligase Rsp5, Ubp2 and Ubp15 prevent hyperubiquitination and proteasomal degradation of ARTs,*" and that "*loss of both Ubp2 and Ubp15 results in a defect in Hxt6 endocytosis.*" ARTs (arrestin-related trafficking adaptors) directly govern ubiquitin-dependent endocytosis of nutrient permeases, including **Gap1**. Because ECM30 co-purifies with Ubp15 in consensus complexes (PMID:20620961), the most parsimonious functional context for ECM30 is as a component/cofactor within the ubiquitin-dependent membrane-trafficking machinery — coherent with the Gap1 connection raised in the seed hypothesis, and distinct from the metazoan dense-core-secretion role that anchors the Golgi IBA terms. A PubMed title/abstract search returns **no dedicated experimental study of ECM30**, confirming the absence of primary functional characterization.

> Quote (PMID:28298493): "*By counteracting the E3 ubiquitin ligase Rsp5, Ubp2 and Ubp15 prevent hyperubiquitination and proteasomal degradation of ARTs.*"

### F006 — Complete QuickGO inventory confirms all five Golgi/localization+process terms are IBA; the sole experimental annotation is cytoplasm; MF is ND

A full QuickGO annotation pull for Q06673 (9 records) itemizes the evidence base precisely:

| GO ID | Term | Aspect | Evidence | Reference |
|-------|------|--------|----------|-----------|
| GO:0007030 | Golgi organization | BP | **IBA** | GO_REF:0000033 |
| GO:0000138 | Golgi trans cisterna | CC | **IBA** | GO_REF:0000033 |
| GO:0005797 | Golgi medial cisterna | CC | **IBA** | GO_REF:0000033 |
| GO:0005829 | cytosol | CC | **IBA** | GO_REF:0000033 |
| GO:0016020 | membrane | CC | **IBA** | GO_REF:0000033 |
| GO:0005737 | cytoplasm | CC | **IEA + HDA** | GO_REF:0000044 / **PMID:14562095** |
| GO:0003674 | molecular_function | MF | **ND** | — |
| GO:0008150 | biological_process | BP | **ND** | — |

GO_REF:0000033 is the PAINT/IBA phylogenetic inference reference. The single experimental (HDA) annotation is **cytoplasm**, from Huh et al. 2003 (PMID:14562095), the genome-wide GFP-localization study. This inventory is the strongest single piece of evidence for the executive judgment: the entire Golgi footprint on ECM30 is phylogenetic inference, and the only wet-lab observation is cytoplasmic.

---

## Mechanistic Model / Interpretation

The evidence assembles into a coherent picture in which **the Golgi annotations on ECM30 are a phylogenetic shadow of the metazoan HID1 function, not an experimentally observed budding-yeast activity**.

```
   METAZOA                          FISSION YEAST                 BUDDING YEAST
   (human HID1, Q8IV36)             (S. pombe HID paralogs)       (S. cerevisiae ECM30, Q06673)
   ─────────────────────           ──────────────────────        ─────────────────────────────
   IDA: Golgi medial/trans          TEM: SPAC17A5.16 mutant       IBA-only Golgi terms
   cisterna localization            lacks STACKED Golgi           (medial/trans cisterna,
        │                           → maintains GA structure       Golgi organization, membrane)
        │                                  │                                │
        ▼                                  ▼                                ▼
   TGN large dense-core             3 HID paralogs (unique         Native Golgi is UNSTACKED;
   vesicle (LDCV) biogenesis;       expansion); stacked Golgi      ECM30 explicitly "divergent"
   regulated neuroendocrine                                        (PMID:40899782)
   secretion                                                              │
        │                                                                 ▼
        └──── IBA/PAINT propagation ─────────────────────────►   Only experimental datum:
              (GO_REF:0000033) carries the LABEL                  CYTOPLASM (HDA, PMID:14562095)
              but NOT the biological context                      MF = ND;  PANTHER MF/BP = root
                                                                          │
                                                                          ▼
                                                          Better-supported functional context:
                                                          ECM30–Ubp15 complex (PMID:20620961)
                                                          → ART/Rsp5 ubiquitin-dependent
                                                            permease trafficking (PMID:28298493)
                                                          + cell-wall phenotype (UniProt, ECM)
```

Two functional narratives compete for ECM30, and they should be kept separate for curation:

1. **The inherited "Golgi organization / cisterna" narrative** — real as an ontology annotation but entirely IBA, anchored on a metazoan protein whose defining role (LDCV biogenesis) does not exist in yeast, and directly undercut by the observation that budding-yeast Golgi is unstacked and ECM30 is divergent. This is a *label transfer*, not a demonstrated function.

2. **The "endomembrane / ubiquitin-dependent trafficking cofactor" narrative** — supported by the physical Ubp15 association and the well-characterized role of Ubp15 in the ART–Rsp5 network that controls permease (including Gap1) endocytosis, plus the original cell-wall (ECM) phenotype. This is association-level but organism-native and mechanistically plausible.

The key interpretive move is that IBA can faithfully transfer a *localization compartment* while silently dropping the *process context*. Even if ECM30 does touch a Golgi/endomembrane compartment (consistent with a trafficking cofactor), that does not license the specific claim that it performs "Golgi organization" as a core molecular/biological function, because that process is (a) not assayable in unstacked budding-yeast Golgi and (b) not experimentally observed for ECM30.

---

## Evidence Base

| Citation | Evidence type | Supports / refutes / qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|----------|---------------|-------------------------------|--------------|-------------|---------|--------------------------|
| [PMID:40899782](https://pubmed.ncbi.nlm.nih.gov/40899782/) | Mutant phenotype (TEM); structural/evolutionary | **Qualifies / partially refutes** | Does the HID family maintain Golgi structure, and does this transfer to ECM30? | *S. pombe* SPAC17A5.16 mutant lacks stacked Golgi; ECM30 explicitly divergent; budding-yeast Golgi unstacked | *S. cerevisiae* / *S. pombe*, EM | High for fission yeast; explicitly flags non-transferability to ECM30 |
| [PMID:14562095](https://pubmed.ncbi.nlm.nih.gov/14562095/) | Localization (HDA, GFP genome-wide) | **Refutes/qualifies Golgi claim** | Where does ECM30 localize in budding yeast? | Cytoplasm — the only experimental localization for ECM30 | *S. cerevisiae*, genome-wide GFP | High as the sole wet-lab datum; high-throughput, single-condition |
| [PMID:20620961](https://pubmed.ncbi.nlm.nih.gov/20620961/) | Interaction (MS co-complex) | **Qualifies (supports trafficking alt.)** | Does ECM30 physically associate with Ubp15? | ECM30 in consensus core complex with Ubp15 | *S. cerevisiae*, MS complexes | Medium; co-complex membership, not targeted assay |
| [PMID:20093466](https://pubmed.ncbi.nlm.nih.gov/20093466/) | Genetic interaction (genome-scale) | **Qualifies** | ECM30 functional neighborhood | ECM30 clusters by genetic-interaction profile | *S. cerevisiae*, SGA map | Medium; profile clustering, not mechanism |
| [PMID:28298493](https://pubmed.ncbi.nlm.nih.gov/28298493/) | Mutant phenotype / mechanism | **Supports trafficking alternative** | Function of Ubp15 (ECM30's partner) | Ubp15 (with Ubp2) counteracts Rsp5 to stabilize ARTs; controls permease endocytosis | *S. cerevisiae* | High for Ubp15; indirect for ECM30 |
| PANTHER PTHR21575:SF12 (database) | Computational / evolutionary | **Qualifies** | What does phylogeny assign to ECM30? | Only Golgi-cisterna CC; MF and BP at root (unknown) | Cross-species tree | Database-level; anchors the IBA terms |
| QuickGO / UniProt Q06673 (database) | Database inventory | **Qualifies** | Evidence codes on ECM30 GO terms | All Golgi/organization/membrane terms IBA; only cytoplasm experimental; MF ND | *S. cerevisiae* | Database-level; definitive for evidence-code status |
| [PMID:23824189](https://pubmed.ncbi.nlm.nih.gov/23824189/) | Mechanism | Context (α-arrestin/Gap1 trafficking) | α-arrestin regulation of permease sorting | Calcineurin switch controls Aly1/Art6 trafficking of Gap1/Dip5 | *S. cerevisiae* | Context for the trafficking network |
| [PMID:23424197](https://pubmed.ncbi.nlm.nih.gov/23424197/) | Comparative mechanism | Context | Conservation of Gap1/GLUT4 endosomal sorting | Ubiquitin-dependent nutrient-transporter sorting conserved yeast↔mammal | Yeast / adipocyte | Context; supports trafficking framing |

**Human HID1 (Q8IV36)** anchors the IBA propagation: it carries IDA evidence for the Golgi-cisterna terms and functions in TGN LDCV biogenesis / regulated secretion — a metazoan-specific process. This is the origin of ECM30's inherited Golgi labels and the reason the labels do not carry a yeast-relevant biological context.

---

## GO Curation Implications

**Lead requiring curator verification.** The evidence does not support treating the Golgi terms as experimentally established core functions of ECM30. Recommended actions:

- **GO:0007030 "Golgi organization" (BP, IBA):** *Do not promote; treat as non-core.* This BP is IBA-only, unsupported by any yeast experiment, and its underlying phenotype (Golgi stacking) is not assayable in budding yeast (F002, F004, F006). Retain only with an explicit "IBA / not verified in *S. cerevisiae*" caveat, or flag for removal pending curator review. It should **not** ground a new core molecular/biological function.
- **GO:0005797 (Golgi medial cisterna) and GO:0000138 (Golgi trans cisterna) (CC, IBA):** *Retain with caveat or generalize.* Consider generalizing to **GO:0005794 "Golgi apparatus"** to avoid over-specific cisternal claims that rest on metazoan IDA, while acknowledging the family-level Golgi association. Keep the IBA caveat explicit.
- **GO:0016020 (membrane, CC, IBA):** Retain as a weak, generic term; note the absence of transmembrane helices means any membrane association is peripheral, consistent with the seed's own framing.
- **GO:0005737 (cytoplasm, CC, HDA/IEA):** *Retain — this is the only experimental localization.* It should be given interpretive priority over the IBA cisterna terms.
- **Molecular function:** Remains **ND**. Do **not** invent an MF; "protein binding" would be uninformative. If any MF lead is pursued, it should be developed from the Ubp15/ubiquitin-trafficking association, not from the Golgi labels.

The net curation message: **the Golgi annotations are genuine but inference-level and organism-mismatched; retain conservatively with caveats or generalize, do not upgrade to experimental, and do not create a core Golgi-organization function for ECM30.**

---

## Mechanistic Scope

The immediate molecular activity being tested — "participates in Golgi organization / associates with medial-trans Golgi cisternae" — is a **cellular-localization + biological-process claim**, not a defined enzymatic or binding activity (ECM30 has no MF assigned). The direct gene-product evidence available for ECM30 in budding yeast is limited to (i) cytoplasmic localization (HDA) and (ii) physical co-complex membership with Ubp15. Everything Golgi-related is *inferred* from the metazoan/fission-yeast relatives.

Downstream/indirect layers that must be kept separate from the direct claim:
- **Cell-wall composition phenotype** (UniProt FUNCTION; the ECM origin) — a *loss-of-function pleiotropic phenotype*, not a direct molecular activity.
- **Gap1 permease sorting** — a *pathway consequence* mediated by the Ubp15/ART/Rsp5 network, in which ECM30's contribution is inferred through its Ubp15 association, not demonstrated directly.
- **Metazoan LDCV biogenesis / regulated secretion** — a *developmental/cell-type-specific outcome* of human HID1 with no yeast counterpart; the source of the inherited Golgi labels, and explicitly out of scope for ECM30's direct function.

---

## Conflicts and Alternatives

1. **Metazoan-to-yeast label carry-over (primary conflict).** The Golgi-cisterna terms originate from human HID1 IDA evidence for a neuroendocrine LDCV process absent in yeast. IBA transfers the compartment label but not the process, producing an annotation that looks Golgi-specific but has no yeast experimental basis (F001, F006).
2. **Paralog/organism-specificity.** The one direct fungal experiment (PMID:40899782) attributes Golgi stacking to a *S. pombe* paralog and expressly flags ECM30 as divergent with an unstacked Golgi — so even the closest experimental relative's function does not transfer (F002).
3. **Association vs. mechanism.** The Ubp15/Gap1 links cited as "direct" are actually high-throughput network datasets (PMID:20620961, PMID:20093466); they support a trafficking-cofactor alternative but are not mechanistic Gap1-sorting assays (F003).
4. **Localization contradiction.** The sole experimental localization is cytoplasm, not Golgi (F006), which either contradicts a stable Golgi-cisterna residence or indicates a large soluble/peripheral pool consistent with a cytoplasmic trafficking cofactor.
5. **Competing better-supported model.** The Ubp15/ART–Rsp5 ubiquitin-dependent permease-trafficking network (PMID:28298493) offers an organism-native, mechanistically grounded alternative context for ECM30 that the Golgi terms do not.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|-----|------------------|-----------------------------|-----------------------|
| No dedicated ECM30 experimental study | PubMed title/abstract search; QuickGO/UniProt records | The entire Golgi footprint is inference; no primary paper defines ECM30's activity | A targeted localization + functional study of ECM30 in *S. cerevisiae* |
| ECM30 subcellular localization beyond "cytoplasm" | HDA GFP datum (PMID:14562095) | Cytoplasm is the only experimental localization; unclear if any Golgi/endomembrane pool exists | High-resolution co-localization (ECM30-GFP with Golgi/TGN and endosomal markers) |
| Direct role in Gap1 sorting | PMID:20620961/20093466 (network only); PMID:28298493 (Ubp15) | Seed treats ECM30–Ubp15/Gap1 as "direct"; it is association-level | *ecm30Δ* Gap1-GFP trafficking assay under N-source shift |
| Molecular function of ECM30 | UniProt MF = ND; PANTHER MF = root | No MF assigned; curation cannot add MF without evidence | Biochemical characterization / structure-guided activity assay |
| Whether any Golgi-organization phenotype exists in yeast | PMID:40899782 (stacking not assayable in budding yeast) | The BP term GO:0007030 rests on a non-assayable process | Golgi-morphology/organization readouts in *ecm30Δ* (e.g., cisternal maturation markers) |

This analysis relied on public database records (UniProt, QuickGO, PANTHER), the provided literature abstracts/snippets, and one directly relevant primary paper (PMID:40899782). No local `*-bioinformatics` analyses were available (intentionally withheld). Several evidence items (Ubp15 association, Gap1 links) are network/high-throughput in nature, and the absence of any dedicated ECM30 primary study is itself a major limitation — the negative finding (no experimental Golgi evidence) is robust, but a positive alternative function for ECM30 remains unproven. Conclusions about evidence codes (IBA, HDA, ND) are database-level facts and are the firmest part of this report; conclusions about ECM30's "true" function are appropriately held as leads, not settled claims.

---

## Proposed Follow-up Experiments / Actions

### Discriminating experiments

1. **ECM30-GFP high-resolution co-localization** with early/medial/trans-Golgi (e.g., Sec21, Sed5, Sec7) and endosomal markers, quantifying the cytoplasmic vs. membrane-associated pool. Distinguishes genuine cisternal residence from a soluble cytoplasmic cofactor.
2. **Fractionation / peripheral-membrane test** (carbonate/salt wash) to determine whether any ECM30 membrane association is peripheral (consistent with no TM helix) vs. absent.
3. **Gap1-GFP trafficking in *ecm30Δ*** across nitrogen-source shifts, with Ubp15 epistasis, to test whether ECM30 contributes to permease sorting through the Ubp15/ART–Rsp5 axis (the competing model).
4. **Golgi-organization readouts in *ecm30Δ*** (cisternal maturation dynamics via 4D imaging of Sec7/Sed5), to test whether any organization phenotype exists at all in unstacked budding-yeast Golgi.
5. **Cross-complementation:** express human HID1 or *S. pombe* SPAC17A5.16 in *ecm30Δ* and vice versa, to test functional conservation vs. divergence directly.
6. **Targeted ECM30–Ubp15 co-IP and mutual dependency** (protein stability, localization) to convert the network-level association into direct mechanistic evidence.

### Curation leads (require curator verification)

**Candidate references and exact snippets to verify:**
- **PMID:40899782** — verify snippet: "*Transmission electron microscopy revealed that the SPAC17A5.16 mutant lacks a stacked Golgi apparatus (GA) form, suggesting a role in maintaining GA structure.*" Use to document that the Golgi-structural role is fission-yeast-paralog-specific and that ECM30 is divergent.
- **PMID:14562095** (Huh et al. 2003) — verify the HDA cytoplasm localization for ECM30; foreground as the sole experimental localization.
- **PMID:28298493** — verify snippet: "*By counteracting the E3 ubiquitin ligase Rsp5, Ubp2 and Ubp15 prevent hyperubiquitination and proteasomal degradation of ARTs.*" Use to frame the Ubp15/trafficking alternative.
- **PMID:20620961** — verify ECM30–Ubp15 co-complex membership; label explicitly as MS-consensus (not targeted).

**Candidate GO actions:**
- Add "IBA / not verified in *S. cerevisiae*" caveat to GO:0007030, GO:0005797, GO:0000138, GO:0016020.
- Consider generalizing GO:0005797/GO:0000138 → **GO:0005794 (Golgi apparatus)**.
- Do **not** promote any Golgi term to experimental (IDA/HDA) status.
- Do **not** add a core Golgi-organization MF/BP; MF stays ND unless new evidence.
- Retain **GO:0005737 (cytoplasm)** as the priority experimental localization.

**Suggested curator questions:**
- Should metazoan-anchored IBA Golgi terms remain on a yeast gene whose only experimental localization is cytoplasm and whose Golgi is unstacked?
- Is the ECM30–Ubp15/cell-wall context a better-supported annotation target than the Golgi labels?


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)