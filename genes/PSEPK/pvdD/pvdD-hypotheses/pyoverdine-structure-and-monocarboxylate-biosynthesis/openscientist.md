---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T01:42:14.403977'
end_time: '2026-09-21T02:08:04.159130'
duration_seconds: 1549.76
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: PSEPK
  gene: pvdD
  gene_symbol: pvdD
  uniprot_accession: Q88F79
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: pyoverdine-structure-and-monocarboxylate-biosynthesis
  hypothesis_text: Pseudomonas putida KT2440 PvdD (Q88F79, PP_4219) participates in
    monocarboxylic acid biosynthesis (GO:0072330) through construction of its native
    pyoverdine. Determine the structures and count of free carboxyl groups for the
    actual KT2440 products, including succinamide/cyclized PVD2 and the linear or
    succinate variants, using primary structural papers PMID:25895945 and PMID:28631237
    and subsequent PMID:31451546. Verify which groups are carboxylic acids versus
    amides or cyclic hydroxamates; do not infer the count solely from amino-acid names.
    Relate the demonstrated NRPS reaction to the GO definition and chemical-class
    ontology. Being a pyoverdine rather than enterobactin synthetase does not alone
    exclude this broad chemical class.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/PSEPK/pvdD/pvdD-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Pseudomonas putida KT2440 PvdD (Q88F79, PP_4219)\
    \ participates in monocarboxylic acid biosynthesis\n  (GO:0072330) through construction\
    \ of its native pyoverdine. Determine the structures and count of free\n  carboxyl\
    \ groups for the actual KT2440 products, including succinamide/cyclized PVD2 and\
    \ the linear or\n  succinate variants, using primary structural papers PMID:25895945\
    \ and PMID:28631237 and subsequent PMID:31451546.\n  Verify which groups are carboxylic\
    \ acids versus amides or cyclic hydroxamates; do not infer the count\n  solely\
    \ from amino-acid names. Relate the demonstrated NRPS reaction to the GO definition\
    \ and chemical-class\n  ontology. Being a pyoverdine rather than enterobactin\
    \ synthetase does not alone exclude this broad chemical\n  class.\nfocus_type:\
    \ function_assignment\ncontext: []\nreference_id: []"
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

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida KT2440 (NCBITaxon:160488)
- **Gene directory:** pvdD
- **Gene symbol:** pvdD
- **UniProt accession:** Q88F79

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** pyoverdine-structure-and-monocarboxylate-biosynthesis
- **Source file:** genes/PSEPK/pvdD/pvdD-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Pseudomonas putida KT2440 PvdD (Q88F79, PP_4219) participates in monocarboxylic acid biosynthesis (GO:0072330) through construction of its native pyoverdine. Determine the structures and count of free carboxyl groups for the actual KT2440 products, including succinamide/cyclized PVD2 and the linear or succinate variants, using primary structural papers PMID:25895945 and PMID:28631237 and subsequent PMID:31451546. Verify which groups are carboxylic acids versus amides or cyclic hydroxamates; do not infer the count solely from amino-acid names. Relate the demonstrated NRPS reaction to the GO definition and chemical-class ontology. Being a pyoverdine rather than enterobactin synthetase does not alone exclude this broad chemical class.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Pseudomonas putida KT2440 PvdD (Q88F79, PP_4219) participates in monocarboxylic acid biosynthesis
  (GO:0072330) through construction of its native pyoverdine. Determine the structures and count of free
  carboxyl groups for the actual KT2440 products, including succinamide/cyclized PVD2 and the linear or
  succinate variants, using primary structural papers PMID:25895945 and PMID:28631237 and subsequent PMID:31451546.
  Verify which groups are carboxylic acids versus amides or cyclic hydroxamates; do not infer the count
  solely from amino-acid names. Relate the demonstrated NRPS reaction to the GO definition and chemical-class
  ontology. Being a pyoverdine rather than enterobactin synthetase does not alone exclude this broad chemical
  class.
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

# AIGR Deep Research Report — *pvdD* (Q88F79, PP_4219), *Pseudomonas putida* KT2440

## Focus: Function-assignment hypothesis — "PvdD participates in monocarboxylic acid biosynthesis (GO:0072330)"

**Organism:** *Pseudomonas putida* KT2440 (NCBITaxon:160488) · **Gene:** pvdD · **UniProt:** Q88F79 · **Locus:** PP_4219 · **Focus type:** function_assignment

---

## Summary

The seed hypothesis proposes that *P. putida* KT2440 PvdD should be curated under **GO:0072330 "monocarboxylic acid biosynthetic process"** because, in building its native pyoverdine, it produces molecules that could fall within the broad monocarboxylic-acid chemical class. Importantly, the hypothesis asks the reviewer to do the honest chemistry — to count the *free* carboxyl groups of the *actual* KT2440 products (PVD G4R and G4R A, the succinamide/cyclized and succinate/linear variants) rather than inferring the count from amino-acid names — and to consider that "being a pyoverdine rather than an enterobactin synthetase does not alone exclude this broad chemical class."

Performing exactly that structural accounting **refutes** the hypothesis. The native KT2440 pyoverdine is a **polycarboxylic** chromopeptide siderophore carrying **2–3 free carboxylic acid groups** (Asp β-COOH, threo-β-hydroxy-Asp β-COOH, and — in the succinate variant only — the free succinate carboxyl). A molecule with two or three free carboxyls is, by the term's own definition, **not** a monocarboxylic acid. The chemical-class defense the hypothesis invites therefore fails on chemistry, not on taxonomy. Separately, PvdD's *direct* molecular activity is nonribosomal peptide synthesis — it is the terminal, chain-releasing NRPS subunit — and it does not itself synthesize the succinyl side chain (the fragment that most resembles a small monocarboxylic acid); that acyl group is installed by separate maturation enzymes.

The annotation itself is also weak and unstable. **All nine current GO annotations on Q88F79 are IEA** (electronic, zero experimental). GO:0072330 specifically originates from **UniProtKB-ARBA** association-rule automation and is **absent from the live GOA/QuickGO extract**, where the corresponding broad automated process term is instead GO:0044550 "secondary metabolite biosynthetic process." GO:0072330 co-occurs with a cluster of clearly erroneous **enterobactin**-branch TreeGrafter mismaps — a textbook signature of NRPS-family paralog over-annotation. The correct, biologically supported terms are **GO:0002049 "pyoverdine biosynthetic process"** and **GO:0019290 "siderophore biosynthetic process"** (BP), with **GO:0031177 "phosphopantetheine binding"** retained (MF). **Verdict: REFUTED / OVER-ANNOTATED.**

---

## Key Findings

### Finding 1 — The native KT2440 pyoverdine is a polycarboxylic chromopeptide siderophore, not a monocarboxylic acid

The hypothesis is right to demand a genuine free-carboxyl count from the *actual* structures. When that accounting is performed, it defeats the hypothesis rather than supporting it.

Structural mass-spectrometry studies define the real KT2440 products — the pyoverdines **PVD G4R** and **G4R A** — as a three-part architecture: (i) a dihydroxyquinoline-type chromophore, (ii) a heptapeptide chain **Asp–Orn–OHAsp–Dab–Gly–Ser–cOHOrn**, and (iii) a C-4 diacid side chain attached to the chromophore (succinic acid or its monoamide/"succinamide" derivative; a malamide/malic variant is reported for the related *P. taiwanensis* strain, not KT2440). *[PMID: 25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/)* states that the pyoverdine "consists of a dihydroxyquinoline-type chromophore, a peptide chain of variable length and conformation, and a **side chain composed of a dicarboxylic acid or its monoamide derivative**," and that "the three PVDs of *P. putida* possess the same peptide chain of seven amino acids, **Asp-Orn-OHAsp-Dab-Gly-Ser-cOHOrn**, with a cyclicized portion present in two of the PVDs."

**Free-carboxyl accounting:**

| Carboxyl source | Chemical status | Free –COOH? |
|---|---|---|
| Asp β-carboxyl | free carboxylic acid | ✅ 1 |
| OHAsp β-carboxyl | free carboxylic acid (also α-hydroxy-acid Fe ligand) | ✅ 1 |
| Side-chain dicarboxylic acid (succinate variant) | free carboxylic acid | ✅ 1 (0 in succinamide/monoamide variant) |
| Chromophore C1-carboxyl | **amide**-bonded to the peptide | ❌ (amide, not acid) |
| C-terminal cyclo-hydroxyornithine (cOHOrn) | **cyclic hydroxamate** | ❌ (not a carboxylic acid) |

Thus the molecule carries **2–3 free carboxylic acid groups** — it is **polycarboxylic**. Its iron-binding triad is **catecholate (chromophore) + hydroxamate (cOHOrn) + α-hydroxy-carboxylate (OHAsp)**, a classic mixed-ligand siderophore rather than a simple organic acid. Product identity is independently confirmed by *[PMID: 28631237](https://pubmed.ncbi.nlm.nih.gov/28631237/)*: "In *Pseudomonas* sp. *putida* KT2[2]40 samples, the known pyoverdines **G4R and G4R A** were readily confirmed."

Because GO:0072330 is defined by a product class carrying **exactly one** carboxyl group, a molecule with two or three free carboxyls is excluded by the term's own definition. The hypothesis's chemical-class reasoning, applied rigorously, lands on refutation.

### Finding 2 — GO:0072330 on Q88F79 is automated ARBA over-annotation; the direct function is the terminal NRPS module of pyoverdine biosynthesis

The UniProt Q88F79 entry describes a **3,470-amino-acid** multi-modular protein with Pfam architecture **Condensation (PF00668) + AMP-binding/adenylation (PF00501) + PP-binding/thiolation-PCP (PF00550) + a second AMP-binding module + Thioesterase (PF00975)** — the canonical signature of a **terminal, chain-releasing NRPS subunit** that adds the final residues and releases/cyclizes the mature peptide.

The direct functional evidence comes from the well-characterized *P. aeruginosa* ortholog. *[PMID: 25015884](https://pubmed.ncbi.nlm.nih.gov/25015884/)* establishes that "the *Pseudomonas aeruginosa* nonribosomal peptide synthetase (NRPS) **PvdD contains two modules that each incorporate an l-threonine residue at the C-terminal end of pyoverdine**." *[PMID: 26268580](https://pubmed.ncbi.nlm.nih.gov/26268580/)* reinforces the mechanism: "**Non-ribosomal peptide synthetase (NRPS) enzymes govern the assembly of amino acids and related monomers into peptide-like natural products.**" PvdD's immediate biochemical acts are therefore ATP-dependent amino-acid adenylation, phosphopantetheine-mediated thiolation, condensation (peptide-bond formation), and thioesterase-catalyzed release/macrocyclization — **nonribosomal peptide synthesis**, not the biosynthesis of a free monocarboxylic acid.

Within the IEA-only GO panel, GO:0072330 is an **IEA:UniProtKB-ARBA** call. The remaining machine annotations include an **enterobactin cluster that is simply wrong** for a pyoverdine synthetase — GO:0009366 "enterobactin synthetase complex," GO:0047527 "2,3-dihydroxybenzoate–serine ligase activity," and GO:0009239 "enterobactin biosynthetic process" — all TreeGrafter mismaps arising because both enterobactin and pyoverdine systems are NRPS-family. Only **GO:0031177 (phosphopantetheine binding)** and the generic amino-acid-activation concept are appropriate; GO:0072330 is not.

### Finding 3 — GO definitions and live QuickGO provenance confirm GO:0072330 is inapt automated annotation; all Q88F79 evidence is IEA

To make the decision auditable, term definitions and the live annotation set were pulled directly from EBI QuickGO.

- **GO:0072330 "monocarboxylic acid biosynthetic process"** = "the chemical reactions and pathways resulting in the **formation of monocarboxylic acids, any organic acid containing one carboxyl (–COOH) group**." The KT2440 pyoverdine has 2–3 free carboxyls → **fails** the single-COOH definition. Reinforced by *[PMID: 25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/)*: the side chain is "**a dicarboxylic acid or its monoamide derivative**."
- **GO:0002049 "pyoverdine biosynthetic process"** = "formation of the siderochrome pyoverdine" → **exact fit**.
- **GO:0019290 "siderophore biosynthetic process"** → fits as the parent process.
- **GO:0043041** ("amino acid activation for nonribosomal peptide biosynthetic process") is now **OBSOLETE** — cannot be retained verbatim.

A **live QuickGO extract for Q88F79 returned 9 annotations, ALL IEA** (ECO:0000501 UniProt or ECO:0007826 TreeGrafter), **zero experimental**:

| Aspect | GO ID | Term | Evidence / source | Assessment |
|---|---|---|---|---|
| MF | GO:0003824 | catalytic activity | IEA (UniProt) | Correct but generic |
| MF | GO:0031177 | phosphopantetheine binding | IEA (UniProt) | **Correct — retain** |
| MF | GO:0047527 | 2,3-DHB–serine ligase activity | IEA (TreeGrafter) | **Wrong (enterobactin mismap)** |
| BP | GO:0009239 | enterobactin biosynthetic process | IEA (TreeGrafter) | **Wrong (enterobactin mismap)** |
| BP | GO:0043041 | amino acid activation for NRP biosynthesis | IEA | **Obsolete** |
| BP | GO:0044550 | secondary metabolite biosynthetic process | IEA (UniProt) | Correct but broad |
| CC | GO:0005737 | cytoplasm | IEA | Plausible |
| CC | GO:0005829 | cytosol | IEA | Plausible |
| CC | GO:0009366 | enterobactin synthetase complex | IEA (TreeGrafter) | **Wrong (enterobactin mismap)** |

Notably, **GO:0072330 appears in the UniProtKB entry (ARBA prediction) but is NOT in the current GOA/QuickGO extract**, where the broad automated BP is instead GO:0044550. This instability — the term flickering between resources across releases — is itself diagnostic of a low-confidence, non-curated automated call that should not be promoted into a curated review.

---

## Mechanistic Model / Interpretation

The refutation rests on separating three levels: the **enzyme's direct reaction**, the **product's chemical class**, and the **automated annotation provenance**. All three point away from GO:0072330.

```
   DIRECT MOLECULAR FUNCTION (what PvdD actually catalyzes)
   ┌─────────────────────────────────────────────────────────────┐
   │  PvdD = terminal NRPS subunit (3,470 aa)                      │
   │  [C] – [A] – [T/PCP] – [A] – [T/PCP] – [TE]                   │
   │   condensation · adenylation · thiolation · thioesterase      │
   │  → activates aa, forms peptide bonds, releases C-terminus     │
   │  MF: GO:0031177 (Ppant binding); NRPS / amino-acid activation │
   └─────────────────────────────────────────────────────────────┘
                              │  assembles
                              ▼
   PRODUCT (native KT2440 pyoverdine: PVD G4R / G4R A)
   ┌─────────────────────────────────────────────────────────────┐
   │  Chromophore (dihydroxyquinoline, catecholate Fe ligand)      │
   │      │ C1-carboxyl = AMIDE to peptide (not free acid)         │
   │      │ side chain = succinate / succinamide / malamide        │
   │  Peptide: Asp–Orn–OHAsp–Dab–Gly–Ser–cOHOrn                    │
   │      Asp β-COOH ........ FREE acid (1)                        │
   │      OHAsp β-COOH ...... FREE acid + α-OH-acid Fe ligand (1)  │
   │      cOHOrn ............ CYCLIC HYDROXAMATE (not acid)        │
   │  Side-chain COOH (succinate variant only) .... FREE acid (1)  │
   │  ───────────────────────────────────────────────            │
   │  Σ FREE carboxyls = 2–3  →  POLYCARBOXYLIC                    │
   └─────────────────────────────────────────────────────────────┘
                              │  therefore
                              ▼
   CHEMICAL-CLASS TEST against GO:0072330
   ┌─────────────────────────────────────────────────────────────┐
   │  GO:0072330 = "one carboxyl (-COOH) group" (monocarboxylic)  │
   │  Product carries 2–3 free carboxyls  →  DOES NOT MATCH        │
   │  Correct BP: GO:0002049 pyoverdine biosynthetic process       │
   │              GO:0019290 siderophore biosynthetic process      │
   └─────────────────────────────────────────────────────────────┘
```

The key logical trap the seed sets — "do not infer the count solely from amino-acid names" and "the broad chemical class is not excluded just because it's a pyoverdine" — is answered by doing the accounting properly. The molecule is polycarboxylic, so it fails the **mono**carboxylic definition. The broad-class defense would apply only if the product had exactly one free carboxyl; it does not. And even under the most permissive reading, PvdD does not *synthesize* the succinyl acyl group (installed by separate acylation/tailoring machinery), so attributing free-acid production to PvdD's catalytic activity is doubly unsupported. PvdD's thioesterase-mediated macrocyclization (to cyclo-OHOrn) in fact *removes* a free carboxyl by lactamization rather than creating a monocarboxylic acid.

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/) | Direct structural (LC–HR-MS/MS) | **Refutes** | Product carboxyl count | Pyoverdine = dihydroxyquinoline chromophore + Asp-Orn-OHAsp-Dab-Gly-Ser-cOHOrn peptide + **dicarboxylic-acid or monoamide** side chain → **polycarboxylic** | *P. putida* KT2440 supernatant | High for structure; carboxyl tally is interpretation of reported moieties; count varies by variant but always >1 |
| [PMID: 28631237](https://pubmed.ncbi.nlm.nih.gov/28631237/) | Direct structural (LC–HR-MS/MS) | **Supports (product identity)** | Which pyoverdines does KT2440 make? | Confirms **G4R and G4R A** as native KT2440 pyoverdines | *P. putida* KT2440 & *P. taiwanensis* VLB120 | High; the malamide/OHAsn variant reported is for *P. taiwanensis*, not KT2440 |
| [PMID: 25015884](https://pubmed.ncbi.nlm.nih.gov/25015884/) | Mutant/biochemical (domain swaps; ortholog) | **Supports (true function) / Refutes scope** | What does PvdD catalyze? | *P. aeruginosa* PvdD = **two-module terminal NRPS** adding C-terminal residues of pyoverdine | *P. aeruginosa*; ortholog of Q88F79 | High for mechanism; transfer by orthology (KT2440 C-terminus is Ser/cOHOrn, strain-specific) |
| [PMID: 26268580](https://pubmed.ncbi.nlm.nih.gov/26268580/) | Biochemical / domain-engineering | **Supports (function class)** | Is PvdD an NRPS? | NRPS enzymes **assemble amino acids into peptide-like products**; thiolation-domain portability in pyoverdine NRPS | Pyoverdine NRPS systems | High for NRPS classification |
| [PMID: 19459056](https://pubmed.ncbi.nlm.nih.gov/19459056/) | Structural / physiological | **Qualifies (product identity)** | Does KT2440 make a single characterized pyoverdine? | KT2440 produces "an already characterised pyoverdine"; no second siderophore | *P. putida* KT2440 vs *P. entomophila* | Medium-high; orients on siderophore biology |
| UniProt Q88F79 / EBI QuickGO (this run) | Computational / database (definition + provenance) | **Refutes** | Is GO:0072330 apt, supported, stable? | GO:0072330 = single-COOH class (product fails it); Q88F79 has 9/9 IEA annotations, 0 experimental; GO:0072330 in UniProt but **absent from live GOA** (GO:0044550 there instead); enterobactin terms are mismaps | GOA/QuickGO, 2026 | High for provenance; snapshot in time |

### How the literature supports or challenges the findings

- ***Structural characterization of multiple pyoverdines...*** [PMID: 25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/) — Primary structural anchor defining the KT2440 scaffold and the dicarboxylic/monoamide side chain. **Challenges** the monocarboxylic classification by demonstrating multiple carboxyl groups.
- ***Structural characterization of pyoverdines produced by P. putida KT2440...*** [PMID: 28631237](https://pubmed.ncbi.nlm.nih.gov/28631237/) — Independently confirms G4R/G4R A identity. **Supports** the product identity used in the accounting.
- ***Biosynthesis of novel Pyoverdines by domain substitution in an NRPS of P. aeruginosa.*** [PMID: 25015884](https://pubmed.ncbi.nlm.nih.gov/25015884/) — Direct functional characterization of PvdD as a two-module terminal NRPS in the ortholog. **Supports** the true molecular function.
- ***Portability of the thiolation domain in recombinant pyoverdine NRPS.*** [PMID: 26268580](https://pubmed.ncbi.nlm.nih.gov/26268580/) — Establishes NRPS mechanism/engineering for pyoverdine synthetases. **Supports** the NRPS classification.
- ***Siderophore-mediated iron acquisition in P. entomophila L48 and P. putida KT2440.*** [PMID: 19459056](https://pubmed.ncbi.nlm.nih.gov/19459056/) — Physiological context; KT2440 makes a single characterized pyoverdine and no second siderophore. **Orients** the siderophore biology.

---

## GO Curation Implications (leads — require curator verification)

- **GO:0072330 (monocarboxylic acid biosynthetic process, BP):** *Do not curate / recommend removal of reliance on it.* IEA-ARBA only, chemically inapt (product is polycarboxylic), unstable across releases, and not PvdD's direct activity. Not suitable as a positive curation statement.
- **GO:0009366 / GO:0047527 / GO:0009239 (enterobactin complex / DHB-Ser ligase / enterobactin biosynthesis):** *Remove* — wrong pathway/product (pyoverdine ≠ enterobactin); NRPS-family paralog mismap.
- **GO:0044550 (secondary metabolite biosynthetic process, BP):** present in live GOA (IEA:UniProt); acceptable as a broad parent but should be superseded by the specific siderophore/pyoverdine terms.
- **GO:0043041 (BP):** now **OBSOLETE** — do not retain verbatim; replace with a current NRPS/pyoverdine term.
- **Retain / prefer instead:**
  - **MF:** **GO:0031177 phosphopantetheine binding** (retain); consider adenylation/ligase and NRPS thioesterase activity terms supported by domain content (GO:0003824 "catalytic activity" is too generic).
  - **BP:** add the specific **GO:0002049 pyoverdine biosynthetic process** and/or **GO:0019290 siderophore biosynthetic process**.
  - **CC:** cytoplasm/cytosol (GO:0005737/GO:0005829) plausible; remove enterobactin synthetase complex (GO:0009366).
- Avoid "protein binding" as an endpoint; specific NRPS/siderophore terms are supported.

---

## Mechanistic Scope

**Direct activity (what PvdD does):** ATP-dependent amino-acid adenylation → phosphopantetheine-mediated thiolation → condensation (peptide-bond formation) → thioesterase-catalyzed release/macrocyclization of the C-terminal pyoverdine peptide. This is captured by NRPS/peptide-biosynthesis MF concepts and by **GO:0002049 / GO:0019290** at the process level; **GO:0031177** is directly supported by the PP-binding/PCP domains.

**Out of scope (downstream / other enzymes):** chromophore formation, N-acylation with the succinate/malate side chain, side-chain amidation, and iron chelation. The **free carboxyls** in the finished siderophore are properties of the *assembled multi-enzyme product* and of separate building-block and tailoring enzymes — **not** a monocarboxylic-acid product of PvdD. Iron acquisition and growth/competition phenotypes are downstream physiological consequences, not PvdD's molecular function.

---

## Conflicts and Alternatives

1. **Paralog confusion:** the enterobactin annotations and the ARBA monocarboxylic-acid rule both derive from the generic NRPS/AMP-binding domain, not from PvdD-specific evidence.
2. **Strain-specificity:** the malic-acid side chain and the Orn-Asp-OHAsn-Thr… sequence emphasized by [PMID: 28631237](https://pubmed.ncbi.nlm.nih.gov/28631237/) pertain to *P. taiwanensis* VLB120; the KT2440 backbone is Asp-Orn-OHAsp-Dab-Gly-Ser-cOHOrn ([PMID: 25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/)). Do not conflate.
3. **Product-variant ambiguity:** succinate vs. succinamide (monoamide) vs. malamide variants shift the exact free-carboxyl count (2 vs. 3), but every variant is polycarboxylic (≥2 free –COOH), so the monocarboxylic classification fails regardless.
4. **Charitable reading:** even if the succinate side chain is formally a monocarboxylic acyl group, that acyl group is not synthesized by PvdD, so the term still fails for PvdD specifically.
5. **The seed's "subsequent" reference:** PMID:31451546 (arginine biosynthesis modulating pyoverdine production under oxidative-stress adaptation) is a physiology/genetics paper — it provides **no** pyoverdine structural/carboxyl data and does **not** support a monocarboxylic-acid function for PvdD.
6. **Annotation instability:** GO:0072330 (UniProtKB-ARBA) vs GO:0044550 (live GOA) for the same protein shows the broad automated BP is version-dependent and should not drive curation.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| No experimental GO evidence for Q88F79 itself | Live QuickGO extract: 9/9 IEA, 0 experimental | The entire GO panel is automation; any curated term needs a defensible code | Direct KT2440 PvdD assay or curated ISS/IBA transfer from *P. aeruginosa* PvdD |
| Exact free-carboxyl count under physiological/iron-bound state | Structural definitions from PMID:25895945/28631237 | Chelation may deprotonate/engage the OHAsp carboxyl; affects count (2 vs 3), not the mono-vs-poly conclusion | pH-dependent titration / crystal or NMR structure of Fe-pyoverdine |
| Which enzyme installs the succinyl/free acid | Domain architecture of PvdD (no acyltransferase) | Confirms PvdD does not make the free-acid moiety, weakening any monocarboxylic claim | Pathway mapping of the pyoverdine acylation/tailoring step (PvdN/PvdO/PvdP-type enzymes) |
| KT2440 PvdD precise module/substrate assignment | Ortholog (*P. aeruginosa*) + domain architecture | Determines which residues PvdD adds in KT2440 | KT2440-specific NRPS module/substrate mapping or ΔpvdD product analysis |
| ARBA rule provenance for GO:0072330 | Observed term in UniProt, absent in GOA | Understanding why ARBA fired helps prevent re-annotation | Inspect the specific ARBA association rule and its features |

---

## Discriminating Tests

1. **Curator provenance check (fastest, decisive):** Confirm in QuickGO/GOA that GO:0072330 is IEA:UniProtKB-ARBA and absent from the curated GOA extract for Q88F79. This alone justifies not promoting it.
2. **Structural free-COOH audit:** For each KT2440 variant (G4R, G4R A, succinamide, malamide), enumerate free carboxyls from published structures; enumerate protonation-state–resolved carboxyls of apo- vs ferri-pyoverdine. Expected: ≥2 in all cases → fails monocarboxylic definition.
3. **Domain-architecture verification:** Re-run InterPro/Pfam on Q88F79 to confirm C-A-T-A-T-TE terminal-NRPS architecture and PP-binding domains (supporting GO:0031177), and the absence of enterobactin-specific domains that would justify the mismapped terms.
4. **Ortholog cross-check:** Align Q88F79 with *P. aeruginosa* PvdD to confirm orthology and transfer the two-module terminal-NRPS function ([PMID: 25015884](https://pubmed.ncbi.nlm.nih.gov/25015884/)) as ISS/IBA.
5. **Mutant experiment (definitive in-organism):** Delete *pvdD* in KT2440 and confirm loss/truncation of PVD G4R/G4R A by LC–HR-MS/MS, establishing GO:0002049 with experimental evidence, plus complementation to show PvdD builds the C-terminal peptide (not the acyl side chain).

---

## Proposed Follow-up Actions / Curation Leads (verify before applying)

- **Action:** Reject the hypothesis as a basis to assert GO:0072330; flag GO:0072330 and all enterobactin terms as IEA over-annotations.
- **Candidate references (with snippets to verify):**
  - [PMID: 25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/): "*side chain composed of a **dicarboxylic acid or its monoamide derivative***"; "*the same peptide chain of seven amino acids, **Asp-Orn-OHAsp-Dab-Gly-Ser-cOHOrn***." → polycarboxylic structure.
  - [PMID: 28631237](https://pubmed.ncbi.nlm.nih.gov/28631237/): "*the known pyoverdines **G4R and G4R A** were readily confirmed*." → product identity.
  - [PMID: 25015884](https://pubmed.ncbi.nlm.nih.gov/25015884/): "*PvdD contains **two modules** that each incorporate an l-threonine residue at the C-terminal end of pyoverdine*." → true molecular function.
  - [PMID: 26268580](https://pubmed.ncbi.nlm.nih.gov/26268580/): "*NRPS enzymes govern the **assembly of amino acids**... into peptide-like natural products*." → NRPS classification.
- **Candidate replacement / new GO terms:** GO:0002049 (pyoverdine biosynthetic process), GO:0019290 (siderophore biosynthetic process); retain GO:0031177 (phosphopantetheine binding). Note GO:0043041 is obsolete.
- **Suggested curator questions:** Does any source provide experimental (EXP/IDA/IMP) support for GO:0072330 on PvdD? Should broad chemical-class BP terms be suppressed when a specific pathway term exists?
- **Suggested experiments:** ΔpvdD deletion + LC–HR-MS/MS pyoverdine readout for in-organism experimental evidence; InterPro/Pfam re-scan to document domain support for GO:0031177 and absence of enterobactin domains.

---

## Conclusion

The hypothesis that PvdD (Q88F79) should be curated under **GO:0072330 "monocarboxylic acid biosynthetic process"** is **refuted**. The native KT2440 pyoverdine is a **polycarboxylic** chromopeptide siderophore (2–3 free –COOH), which fails the term's single-carboxyl definition; the annotation is unsupported, unstable **IEA:UniProtKB-ARBA** automation co-occurring with erroneous enterobactin mismaps; and PvdD's direct function is **nonribosomal peptide synthesis** (terminal NRPS module of the pyoverdine synthetase). The curation should instead use **GO:0002049 (pyoverdine biosynthetic process)** and **GO:0019290 (siderophore biosynthetic process)**, retain **GO:0031177 (phosphopantetheine binding)**, and remove the erroneous enterobactin terms (GO:0009366, GO:0047527, GO:0009239).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)