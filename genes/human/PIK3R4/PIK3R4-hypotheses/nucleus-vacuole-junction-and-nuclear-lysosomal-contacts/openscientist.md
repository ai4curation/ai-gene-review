---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T20:58:03.284276'
end_time: '2026-09-20T21:12:15.549601'
duration_seconds: 852.27
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: PIK3R4
  gene_symbol: PIK3R4
  uniprot_accession: Q99570
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: nucleus-vacuole-junction-and-nuclear-lysosomal-contacts
  hypothesis_text: Human PIK3R4/VPS15 (Q99570) localizes to a nucleus-vacuole junction
    (GO:0071561). Examine the actual term definition, PTN000426471 ancestral assignment,
    target localization and human nuclear-lysosomal membrane-contact biology. Distinguish
    generic nuclear contact or lysosomal trafficking from the defined junction, and
    positive evidence of lineage-specific architecture from a yeast-only assumption
    based on the word vacuole. Evaluate whether the human VPS34/VPS15 complex participates
    in a relevant contact-site structure, without treating a predominant endosomal/autophagic
    location as proof of exclusivity.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/PIK3R4/PIK3R4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human PIK3R4/VPS15 (Q99570) localizes to a nucleus-vacuole\
    \ junction (GO:0071561). Examine\n  the actual term definition, PTN000426471 ancestral\
    \ assignment, target localization and human nuclear-lysosomal\n  membrane-contact\
    \ biology. Distinguish generic nuclear contact or lysosomal trafficking from the\
    \ defined\n  junction, and positive evidence of lineage-specific architecture\
    \ from a yeast-only assumption based\n  on the word vacuole. Evaluate whether\
    \ the human VPS34/VPS15 complex participates in a relevant contact-site\n  structure,\
    \ without treating a predominant endosomal/autophagic location as proof of exclusivity.\n\
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
citation_count: 10
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: artifacts_PIK3R4_GO_decision_table.csv
  path: openscientist_artifacts/artifacts_PIK3R4_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist PIK3R4 GO decision table
- filename: artifacts_PIK3R4_NVJ_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_PIK3R4_NVJ_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist PIK3R4 NVJ evidence matrix
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
- **Gene directory:** PIK3R4
- **Gene symbol:** PIK3R4
- **UniProt accession:** Q99570

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** nucleus-vacuole-junction-and-nuclear-lysosomal-contacts
- **Source file:** genes/human/PIK3R4/PIK3R4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human PIK3R4/VPS15 (Q99570) localizes to a nucleus-vacuole junction (GO:0071561). Examine the actual term definition, PTN000426471 ancestral assignment, target localization and human nuclear-lysosomal membrane-contact biology. Distinguish generic nuclear contact or lysosomal trafficking from the defined junction, and positive evidence of lineage-specific architecture from a yeast-only assumption based on the word vacuole. Evaluate whether the human VPS34/VPS15 complex participates in a relevant contact-site structure, without treating a predominant endosomal/autophagic location as proof of exclusivity.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human PIK3R4/VPS15 (Q99570) localizes to a nucleus-vacuole junction (GO:0071561). Examine
  the actual term definition, PTN000426471 ancestral assignment, target localization and human nuclear-lysosomal
  membrane-contact biology. Distinguish generic nuclear contact or lysosomal trafficking from the defined
  junction, and positive evidence of lineage-specific architecture from a yeast-only assumption based
  on the word vacuole. Evaluate whether the human VPS34/VPS15 complex participates in a relevant contact-site
  structure, without treating a predominant endosomal/autophagic location as proof of exclusivity.
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

# AIGR Deep Research Report — PIK3R4 / VPS15 (Q99570)

## Hypothesis under review

> **Human PIK3R4/VPS15 (Q99570) localizes to a nucleus-vacuole junction (GO:0071561).**
> Distinguish the defined organelle contact site from generic nuclear contact or
> lysosomal trafficking, and evaluate whether the human VPS34/VPS15 complex
> participates in a relevant contact-site structure, without treating a
> predominant endosomal/autophagic location as proof of exclusivity.

- **Focus type:** function_assignment
- **Term in question:** GO:0071561 — *nucleus-vacuole junction* (cellular_component)
- **Source review:** `genes/human/PIK3R4/PIK3R4-ai-review.yaml`

---

## Summary

The nucleus-vacuole junction annotation on human PIK3R4 (GO:0071561) is **not
supported by any human experimental evidence**. It is an **IBA-only,
phylogenetically propagated (PAINT) annotation** carried over from experimentally
annotated *Saccharomyces cerevisiae* orthologs into a taxon that does not possess
a vacuole and has no described nucleus-vacuole junction. Every piece of positive,
human-specific evidence places the PIK3R4-containing class III PI3K complex at
**Rab7-positive late endosomes and autophagosomes**, not at the nuclear envelope
or a defined nuclear–lysosomal contact site.

Three independent lines of reasoning converge on this conclusion. First, the term
is structurally organism-specific: GO:0071561 is explicitly defined as the contact
formed between the **vacuole membrane and the outer nuclear membrane**, mediated in
*S. cerevisiae* by the direct interaction of **Vac8p and Nvj1p** — two proteins
that build the junction and are unrelated to VPS15/VPS34. Second, the human
annotation has no experimental basis: the only GO:0071561 annotation on Q99570 is
evidence code IBA (ECO:0000318, GO_REF:0000033), inferred from the yeast ortholog
via PANTHER node PTN000426471. Third, the annotation is internally inconsistent —
only PIK3R4 carries the human NVJ term while its obligate catalytic partner
PIK3C3/VPS34 (Q8NEB9) does not.

**Verdict: over-annotated / refuted for human.** The most important caveat is that
absence of a curated human NVJ annotation is not absolute proof that human class
III PI3K never visits a nuclear-envelope contact site — human nuclear-lysosomal /
nuclear-envelope membrane-contact biology is an active field and remains
incompletely mapped. However, the specific GO:0071561 term denotes a defined yeast
organelle, and there is currently **zero positive human evidence** for it.
Curation should reflect the state of evidence, not a phylogenetic guess.

---

## Executive Judgment

**Verdict: Over-annotated / refuted for human.**

Three converging lines of evidence:

1. **The term is structurally organism-specific.** GO:0071561 is the contact
   between the vacuole membrane and the outer nuclear membrane, built in yeast by
   Vac8p and Nvj1p. It is not architecturally a "Vps15 structure."
2. **The human annotation has no experimental basis.** The only GO:0071561
   annotation on Q99570 is IBA, inferred from the yeast ortholog via PANTHER
   PTN000426471. All human *experimental* CC annotations are
   endosomal/autophagosomal.
3. **The annotation is internally inconsistent.** Only PIK3R4 carries the human
   NVJ term; PIK3C3/VPS34 does not. A genuine complex-resident localization would
   annotate both subunits. The single-subunit, IBA-only pattern is the signature
   of an isolated PAINT propagation artifact.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 28533415](https://pubmed.ncbi.nlm.nih.gov/28533415/) | Structural (crystal) | Qualifies (defines the term) | What builds the NVJ | NVJ is mediated by direct Vac8p–Nvj1p interaction; junction defined by these two proteins | *S. cerevisiae* | High. Establishes organism-specific architecture, not Vps15-based |
| [PMID: 42375028](https://pubmed.ncbi.nlm.nih.gov/42375028/) | Review | Qualifies | Nature of NVJ | NVJ is "a central membrane contact site in yeast" connecting nuclear ER and vacuole | Yeast (review) | High as orientation; review-level |
| [PMID: 23335340](https://pubmed.ncbi.nlm.nih.gov/23335340/) | Localization (IDA) | Supports (in yeast only) | Do Vps15/Vps34 sit at NVJ? | Yeast VPS15 (P22219) and VPS34 (P22543) carry IDA NVJ annotations | *S. cerevisiae* | High for yeast; source of the ancestral PANTHER assignment |
| [PMID: 14617358](https://pubmed.ncbi.nlm.nih.gov/14617358/) | Localization (IDA) | Refutes (for human) | Where does human PIK3R4 localize? | hVPS34/p150(PIK3R4) complex colocalizes with Rab7 on **late endosomes** | Human cells | High. Direct human experimental evidence, non-nuclear |
| QuickGO annotation set (Q99570) | Database | Refutes | Evidence basis of human NVJ term | Only NVJ annotation is IBA (GO_REF:0000033), withFrom PANTHER:PTN000426471 + SGD | Human | High. No human experimental support |
| QuickGO (Q8NEB9) | Database | Refutes | Is the partner subunit annotated? | Human PIK3C3/VPS34 has **0** NVJ annotations | Human | High. Complex-level inconsistency |
| UniProt Q99570 | Database | Refutes | Curated human subcellular location | Late endosome; cytoplasmic vesicle/autophagosome; membrane. No nuclear/vacuole terms | Human | High |
| NCBI PubMed searches | Computational (literature) | Refutes | Any human NVJ/nuclear-envelope report? | "PIK3R4 nuclear envelope" = 0; "nucleus lysosome contact site VPS34" = 0 | Human | Moderate–high; negative literature search |

---

## Key Findings

### F001 — GO:0071561 is a structurally yeast-defined organelle contact site

The QuickGO record for GO:0071561 (aspect cellular_component) defines the term as
"an organelle membrane contact site formed between the **vacuole membrane and the
outer nuclear membrane**. In *S. cerevisiae* these contacts are mediated through
direct physical interaction between **Vac8p and Nvj1p**." The synonyms are
"nucleus-vacuole membrane contact site" and "NVJ."

The crystal structure of the Vac8p–Nvj1p interface
([PMID: 28533415](https://pubmed.ncbi.nlm.nih.gov/28533415/)) confirms that the
junction is physically built by these two proteins — *"Formation of the
nucleus-vacuole junction (NVJ) is mediated by direct interaction between the
vacuolar protein Vac8p and the outer nuclear endoplasmic reticulum membrane
protein Nvj1p."* Disrupting this interaction abolishes NVJs and piecemeal
microautophagy of the nucleus (PMN). The "at a glance" review
([PMID: 42375028](https://pubmed.ncbi.nlm.nih.gov/42375028/)) reinforces that the
NVJ is *"a central membrane contact site in yeast that connects the nuclear
endoplasmic reticulum and the vacuole."*

**Implication:** The junction is architecturally defined by Vac8p/Nvj1p, not by
Vps15/Vps34. Even in yeast, Vps15/Vps34 are *residents* at the junction, not its
structural scaffold. The term therefore carries strong organism-specific and
organelle-specific meaning that does not transfer cleanly to a vacuole-less taxon.

### F002 — The human PIK3R4 NVJ annotation is IBA-only; human localization is endosomal/autophagosomal

In the QuickGO annotation set for UniProtKB:Q99570 (human PIK3R4), the **only**
nucleus-vacuole junction annotation is **IBA** (ECO:0000318, GO_REF:0000033 /
PAINT), with `withFrom` = **PANTHER:PTN000426471** and **SGD:S000000301** — i.e.,
inferred phylogenetically from the yeast ortholog, with **no human experimental
support**.

By contrast, every human *experimental* CC annotation is non-nuclear:

- **Late endosome** — IDA (ECO:0000314), [PMID: 14617358](https://pubmed.ncbi.nlm.nih.gov/14617358/)
- **Membrane** — HDA, PMID:19946888
- **Autophagosome** and **cytosol** — Reactome TAS

UniProt Q99570 lists subcellular location = **Late endosome; Cytoplasmic
vesicle / autophagosome; Membrane** (keywords: Endosome, Cytoplasmic vesicle; no
nuclear or vacuolar terms). The primary human study
([PMID: 14617358](https://pubmed.ncbi.nlm.nih.gov/14617358/)) reports that *"the
hVPS34/p150 complex colocalized with rab7 on late endosomes and hVPS34 activity
was dependent on nucleotide cycling of rab7."* Here p150 is PIK3R4.

Across all organisms, GO:0071561 has ~5,093 gene-product annotations,
overwhelmingly **IEA** (GO_REF:0000118) and **IBA** (GO_REF:0000033), spanning
plants, nematodes, birds, and fungi — a classic signature of automated /
phylogenetic over-propagation of a yeast-specific structural term.

### F003 — Yeast Vps15/Vps34 have genuine NVJ localization; the human paralog does not (lineage-specific architecture)

In *S. cerevisiae* (taxon 559292), both **VPS15 (P22219)** and **VPS34 (P22543)**
carry **IDA (ECO:0000314)** NVJ annotations from
[PMID: 23335340](https://pubmed.ncbi.nlm.nih.gov/23335340/), alongside the
canonical NVJ builders **NVJ1 (P38881)** and **VAC8 (P39968)** (IDA,
PMID:10888680). So the ancestral source that propagated to PANTHER node
PTN000426471 is **experimentally grounded in yeast**.

The crucial asymmetry: the equivalent human evidence is **absent**. No human
PIK3R4/VPS34 dataset places the complex at the nuclear envelope or a defined
nucleus–lysosome junction. This is exactly the pattern the seed hypothesis asked
us to distinguish — *positive evidence of lineage-specific architecture* versus a
*yeast-only assumption based on the word "vacuole."* The evidence favors the
former: the junction is a real yeast structure that simply has no demonstrated
human counterpart for this complex.

### F004 — No human literature or database record places PIK3R4 at the nuclear envelope, vacuole, or a nucleus–lysosome junction

Targeted NCBI PubMed searches returned:

- `PIK3R4 nuclear envelope` → **0 hits**
- `nucleus lysosome contact site VPS34` → **0 hits**
- `PIK3R4 nucleus` → **1 hit** (PMID:33906557, an autophagy/intestinal-barrier
  review — not a localization study)

The three human PIK3R4 "localization" hits concern autophagy initiation via ULK1
(PMID:37992308), a VPS15/PIK3R4 ciliopathy affecting IFT20 release from the
cis-Golgi (PMID:27882921), and Vps34/PIK3C3 complex-subunit characterization
(PMID:27630019) — **all non-nuclear, non-vacuolar**. Combined with the curated
UniProt/QuickGO human locations (late endosome, autophagosome, membrane), there is
**no positive human evidence** for the seed hypothesis.

### F005 — The human NVJ annotation is internally inconsistent (single-subunit, IBA-only)

QuickGO shows that human **PIK3C3/VPS34 (Q8NEB9) has 0 annotations** to
GO:0071561, whereas in yeast **both** Vps15 (P22219) and Vps34 (P22543) carry
experimental IDA NVJ annotations (PMID:23335340). Across all human proteins
(taxon 9606), the **only** GO:0071561 annotation is PIK3R4 (IBA, GO_REF:0000033);
**no human protein** has any experimental (IDA/IPI/IMP/HDA) NVJ annotation.

A genuine complex-resident localization would annotate **both obligate subunits**.
The single-subunit, IBA-only pattern is diagnostic of an **isolated phylogenetic
(PAINT) propagation** rather than a real human cellular structure.

---

## Mechanistic Model / Interpretation

The class III PI3K (VPS34/PIK3C3 catalytic + VPS15/PIK3R4 regulatory pseudokinase
scaffold) is deeply conserved, and its *core biochemistry* (PI3P production for
endosomal sorting and autophagy) transfers across eukaryotes. What does **not**
transfer is the specific yeast **nucleus-vacuole junction** organelle, which is a
lineage-specific architecture built by Vac8p–Nvj1p.

```
YEAST (S. cerevisiae)                        HUMAN (H. sapiens)
---------------------                        ------------------
Nucleus (outer NE)                           Nucleus
   | Nvj1p  <-- junction scaffold            (no Nvj1p / Vac8p orthologous NVJ)
   | Vac8p  <-- junction scaffold
Vacuole membrane                             Lysosome (no defined NVJ described
   +-- Vps15/Vps34 RESIDE at NVJ (IDA,        for class III PI3K)
       PMID:23335340)
                                             Vps15(PIK3R4)/Vps34(PIK3C3)
                                                +-- Late endosome (Rab7+, IDA
                                                    PMID:14617358)
                                                +-- Autophagosome, cytosol,
                                                    membrane (experimental)

PANTHER node PTN000426471 (Vps15 family)
   |  IBA / PAINT propagation
   v
Human PIK3R4 gets GO:0071561 -- WITHOUT any human experimental support,
and WITHOUT the partner PIK3C3 receiving the same term.
```

The annotation flow is transparent: yeast Vps15/Vps34 were experimentally seen at
the NVJ → this became the ancestral state at PANTHER node PTN000426471 →
PAINT/IBA propagated the CC term GO:0071561 down to human PIK3R4. The propagation
crossed an organelle boundary that does not exist in human (no vacuole; no
demonstrated NVJ), and it landed on only one of the two complex subunits. Both the
**biology** (organism-specific organelle) and the **annotation metadata**
(IBA-only, single-subunit, cross-taxon frequency bias) point to over-annotation.

---

## Evidence Base

| Paper | PMID | Role in this analysis |
|---|---|---|
| *Mechanistic insight into the nucleus-vacuole junction based on the Vac8p-Nvj1p crystal structure.* | [28533415](https://pubmed.ncbi.nlm.nih.gov/28533415/) | Defines the NVJ as a Vac8p–Nvj1p structure; establishes the term's organism-specific architecture |
| *The nucleus-vacuole junction at a glance.* | [42375028](https://pubmed.ncbi.nlm.nih.gov/42375028/) | Review confirming NVJ is a yeast contact site (nuclear ER ↔ vacuole) |
| Yeast Vps15/Vps34 NVJ IDA source | [23335340](https://pubmed.ncbi.nlm.nih.gov/23335340/) | Experimental basis for the ancestral (yeast) NVJ annotation propagated to PANTHER PTN000426471 |
| hVPS34/p150(PIK3R4)–Rab7 late-endosome study | [14617358](https://pubmed.ncbi.nlm.nih.gov/14617358/) | Direct human experimental localization: late endosome, not NVJ |

Database orientation used (labeled as database-level support): QuickGO term and
annotation records for GO:0071561, Q99570 (PIK3R4), Q8NEB9 (PIK3C3); UniProt
Q99570 subcellular location; PANTHER node PTN000426471.

---

## GO Curation Implications

**Lead (requires curator verification): Remove or NOT-qualify GO:0071561 on human
PIK3R4 (Q99570).**

- The term is a **CC** term denoting a yeast-specific organelle contact site.
- The current human annotation is **IBA-only** (GO_REF:0000033, PANTHER
  PTN000426471) with **no human experimental support** and **no partner-subunit
  corroboration** (PIK3C3 lacks it).
- Recommended action: **remove** the human GO:0071561 annotation, or apply a
  **NOT** qualifier if the curator prefers to preserve the phylogenetic trail
  while signaling absence of human evidence. As PAINT annotations are generated by
  the PAINT curation team, the cleaner route may be a **PAINT curation note** at
  node PTN000426471 flagging that the NVJ CC term should not be propagated beyond
  fungi (organism-specific organelle), since human/metazoa lack the vacuole and a
  described NVJ.
- **Retain** the well-supported human CC terms: **late endosome** (GO:0005770,
  IDA, PMID:14617358), **autophagosome** (GO:0005776), **cytosol**, **membrane**,
  and **phosphatidylinositol 3-kinase complex, class III** (GO:0005942) / its
  autophagy-specific variants.
- The **yeast** NVJ annotations on Vps15/Vps34 (P22219/P22543, IDA, PMID:23335340)
  remain valid and should not be touched.

This avoids a "protein binding" fallback — the informative replacement is the
experimentally supported endosomal/autophagosomal localization already present.

---

## Mechanistic Scope

The claim being tested is strictly a **cellular-component / localization**
assertion: does the gene product physically reside at a defined nucleus-vacuole
junction? This is distinct from PIK3R4's **molecular function** (regulatory
pseudokinase scaffold of the class III PI3K / VPS34 complex) and its **biological
processes** (autophagy initiation, endosomal PI3P production, vesicular
trafficking), all of which are well supported and unaffected by this review.

The refutation applies only to the **direct localization** at GO:0071561. It does
not challenge:

- PIK3R4's role as the VPS15 regulatory subunit of class III PI3K.
- Its established late-endosomal, autophagosomal, and membrane localization.
- Any downstream autophagy or trafficking phenotype.

We are separating **direct gene-product localization** (the term under review)
from **pathway function** (intact) and from **loss-of-function phenotypes**
(irrelevant to this CC assertion).

---

## Conflicts and Alternatives

1. **Paralog/ortholog carry-over (primary alternative, and the most likely
   explanation):** The human term derives from yeast orthologs via PANTHER
   PTN000426471. This is not paralog confusion within human, but **cross-species
   phylogenetic carry-over** of an organism-specific organelle term. The
   ~5,093-annotation, IEA/IBA-dominated spread of GO:0071561 across plants,
   nematodes, and birds confirms systematic over-propagation.

2. **Organism-specific organelle absence:** Humans have no vacuole; the lysosome
   is the functional analog, but no nucleus-**lysosome** junction resembling the
   yeast NVJ has been described for the class III PI3K complex. Applying a
   vacuole-defined term to human cells is a category mismatch unless a human
   structure is demonstrated.

3. **Genuine-but-undiscovered human contact site (the seed's steelman):** Nuclear
   envelope–lysosome and nuclear-envelope membrane contact biology is an active
   frontier. It remains *possible* that human class III PI3K transiently visits a
   nuclear-envelope contact site. However, (a) there is currently no positive
   human data, and (b) even if found, it would likely warrant a **new/more
   generic** contact-site term rather than the yeast-specific GO:0071561. This
   keeps the door open scientifically while still supporting removal of the
   specific term now.

4. **Single-subunit inconsistency as artifact signal:** The fact that only PIK3R4
   (not PIK3C3) carries the term is best explained by annotation mechanics (which
   ortholog groups were PAINT-annotated), not by a biological scenario in which
   only the regulatory subunit visits the junction without its catalytic partner.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Human nuclear-envelope contact biology is incompletely mapped | PubMed negative searches; UniProt/QuickGO curated locations | A future human MCS finding could re-open a (generic) contact-site term | Proximity-labeling (APEX/BioID) of PIK3R4 at the nuclear envelope; high-resolution imaging |
| PMID:14617358 read at abstract/snippet level only | Snippet verified via QuickGO withFrom + abstract | Confirms late-endosome, but full text may add nuance | Full-text review of localization panels |
| PANTHER node PTN000426471 propagation logic not directly inspected in PAINT UI | Inferred from QuickGO withFrom fields | Curators may prefer to fix at the PAINT node rather than per-gene | Inspect PTN000426471 in the PAINT/PANTHER tree and add a curation note |
| Did not exhaustively survey all metazoan orthologs | Spot-checked cross-taxon annotation counts | Confirms breadth of over-propagation but not every case | Systematic audit of GO:0071561 IBA annotations outside fungi |
| Yeast IDA source (PMID:23335340) reviewed via database metadata, not full text | QuickGO IDA records | Establishes ancestral validity; not central to human verdict | Full-text confirmation of yeast Vps15/Vps34 NVJ imaging |

---

## Discriminating Tests

1. **Proximity labeling of endogenous PIK3R4** (BioID/TurboID or APEX2) with
   nuclear-envelope, lysosomal, and endosomal reference markers. If PIK3R4
   proximity partners are dominated by Rab7/late-endosome/autophagosome proteins
   and lack nuclear-envelope/INM proteins, this refutes a human NVJ localization.

2. **Two-subunit co-localization requirement:** Simultaneous imaging of PIK3R4 and
   PIK3C3. A real complex-resident junction localization must show **both**
   subunits at the site; PIK3R4-only signal argues against it.

3. **PANTHER/PAINT node audit at PTN000426471:** Confirm the propagation path and
   evaluate whether GO:0071561 should be restricted to fungal descendants.

4. **Ortholog conservation check for the junction scaffold:** Test whether human
   has functional orthologs of Nvj1p/Vac8p forming an NVJ-like structure. Absence
   of the scaffold strengthens the "no human NVJ" conclusion.

5. **Systematic GO:0071561 annotation audit** across non-fungal taxa to quantify
   the over-propagation and inform a term-scope fix.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Proposed action change**
- Remove (or NOT-qualify) **GO:0071561 (nucleus-vacuole junction)** on human
  PIK3R4 (Q99570); prefer fixing at PAINT node **PTN000426471** so the term is
  not propagated beyond fungi.
- Retain: **GO:0005770 late endosome** (IDA, PMID:14617358), **GO:0005776
  autophagosome**, **GO:0005942 class III PI3K complex**, cytosol/membrane.
- Leave yeast Vps15/Vps34 (P22219/P22543) NVJ IDA annotations unchanged.

**Candidate references with snippets to verify**
- [PMID: 28533415](https://pubmed.ncbi.nlm.nih.gov/28533415/): *"Formation of the
  nucleus-vacuole junction (NVJ) is mediated by direct interaction between the
  vacuolar protein Vac8p and the outer nuclear endoplasmic reticulum membrane
  protein Nvj1p."* → NVJ is a Vac8p/Nvj1p structure, not a Vps15 structure.
- [PMID: 42375028](https://pubmed.ncbi.nlm.nih.gov/42375028/): *"The
  nucleus-vacuole junction (NVJ) is a central membrane contact site in yeast..."*
  → yeast-specific organelle.
- [PMID: 14617358](https://pubmed.ncbi.nlm.nih.gov/14617358/): *"The hVPS34/p150
  complex colocalized with rab7 on late endosomes..."* → human localization is
  endosomal.

**Suggested curator questions**
- Should organism-specific CC terms like GO:0071561 be blocked from IBA
  propagation into taxa lacking the organelle (vacuole)?
- Is a NOT qualifier or outright removal preferred for IBA-only, single-subunit,
  cross-taxon over-propagations?

**Suggested experiments** — see Discriminating Tests above (PIK3R4 proximity
labeling; two-subunit co-localization; PAINT node audit).

---

## Conclusion

The seed hypothesis is **refuted for human as stated**. Human PIK3R4/VPS15
(Q99570) has **no direct evidence** of localizing to a nucleus-vacuole junction.
GO:0071561 is a **structurally yeast-defined** contact site built by Vac8p–Nvj1p
([PMID: 28533415](https://pubmed.ncbi.nlm.nih.gov/28533415/)); the human
annotation is **IBA-only**, phylogenetically propagated (PANTHER PTN000426471 /
PAINT) from experimentally annotated yeast Vps15/Vps34
([PMID: 23335340](https://pubmed.ncbi.nlm.nih.gov/23335340/)) into a taxon that
lacks a vacuole and any described NVJ. Human PIK3R4 is instead experimentally
localized to **Rab7+ late endosomes and autophagosomes**
([PMID: 14617358](https://pubmed.ncbi.nlm.nih.gov/14617358/)), and only PIK3R4 —
not its obligate partner PIK3C3 — carries the term, marking it an isolated
propagation artifact. **Curation lead:** remove or NOT-qualify GO:0071561 on human
PIK3R4 while retaining its late-endosome, autophagosome, and class III PI3K
complex CC terms; yeast NVJ annotations remain valid.


## Artifacts

- [OpenScientist PIK3R4 GO decision table](openscientist_artifacts/artifacts_PIK3R4_GO_decision_table.csv)
- [OpenScientist PIK3R4 NVJ evidence matrix](openscientist_artifacts/artifacts_PIK3R4_NVJ_evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)