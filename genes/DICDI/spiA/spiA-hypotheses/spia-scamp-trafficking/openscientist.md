---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-12T12:05:26.496142'
end_time: '2026-07-12T12:17:45.464590'
duration_seconds: 738.97
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: spiA
  gene_symbol: spiA
  uniprot_accession: Q02465
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: spia-scamp-trafficking
  hypothesis_text: SpiA is a secretory carrier membrane protein (SCAMP family) that
    functions in vesicular membrane trafficking
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: SpiA is a secretory carrier membrane protein (SCAMP\
    \ family) that functions in vesicular membrane\n  trafficking\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
citation_count: 8
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
- **Gene directory:** spiA
- **Gene symbol:** spiA
- **UniProt accession:** Q02465

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** spia-scamp-trafficking
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

SpiA is a secretory carrier membrane protein (SCAMP family) that functions in vesicular membrane trafficking

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: SpiA is a secretory carrier membrane protein (SCAMP family) that functions in vesicular membrane
  trafficking
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

# SpiA (Q02465) — SCAMP Family Membership vs. Vesicular Trafficking Function

**Target gene:** spiA (Q02465, DD31_DICDI), *Dictyostelium discoideum* (NCBITaxon:44689)
**Seed hypothesis:** *SpiA is a secretory carrier membrane protein (SCAMP family) that functions in vesicular membrane trafficking.*
**Focus type:** function_assignment

---

## Summary

The seed hypothesis bundles two separable claims, and the evidence pulls them apart sharply. The **family claim — that SpiA is a SCAMP (secretory carrier membrane protein) — is well supported** by concordant, independent domain and sequence evidence: SpiA carries the SCAMP Pfam domain (PF04144), the InterPro SCAMP signature (IPR007273), and the PANTHER subfamily assignment (PTHR10687:SF2), plus a canonical four-transmembrane-helix membrane core and ~28% mean identity to the five human SCAMPs concentrated in that core. Critically, SpiA is the *single* SCAMP-family gene in the entire *D. discoideum* genome, so this is not a paralog-confused call.

The **functional claim — that SpiA "functions in vesicular membrane trafficking" — is only weakly (homology-only) supported and is not the gene's demonstrated primary function.** Every trafficking-flavored GO annotation on the protein (exocytosis, recycling endosome membrane, trans-Golgi network membrane, protein transport) carries a phylogenetic (IBA) or electronic (IEA) evidence code with no organism-specific experimental backing. The *only* directly demonstrated function of SpiA is a **structural, spore-coat-associated role in maintaining spore viability during dormancy**, established by targeted gene deletion (Richardson & Loomis 1992, [PMID: 1592257](https://pubmed.ncbi.nlm.nih.gov/1592257/)). SpiA is also a *divergent* SCAMP that lacks the N-terminal NPF motif repeats that mechanistically drive canonical SCAMP–EH-domain trafficking interactions.

**Bottom line for the curator:** Retain the SCAMP-family molecular identity and the experimentally grounded spore/sorocarp terms as core. Treat the vesicular-trafficking GO terms as **non-core, homology-only annotations** that do not represent the gene product's primary function. The seed hypothesis should *narrow* the review — SpiA is a SCAMP, but its established biology is spore-coat maintenance, not general membrane trafficking. Verdict: **partially supported / over-annotated on the trafficking claim.**

---

## Key Findings

### Finding 1 — SpiA is confidently a SCAMP-family multi-pass membrane protein

SpiA (Q02465, DD31_DICDI) is unambiguously a SCAMP on structural and domain grounds. The UniProt entry describes a **269-amino-acid protein with four predicted transmembrane helices** (approximately residues 111–131, 139–159, 177–197, and 225–245), matching the canonical SCAMP membrane core of four TM segments flanked by cytoplasmic N- and C-termini. Three independent classification resources converge: **Pfam PF04144 (SCAMP)**, **InterPro IPR007273 (SCAMP)**, and **PANTHER PTHR10687:SF2 (Secretory carrier-associated membrane protein)**, and UniProt carries the SIMILARITY comment "Belongs to the SCAMP family" (ECO:0000305, curator inference). This is the robust half of the hypothesis — supported by multiple orthogonal signatures, with no competing family assignment. The caveat is that it is homology/domain-level evidence, not a direct biochemical demonstration.

### Finding 2 — SpiA lacks canonical SCAMP NPF trafficking motifs and is structurally divergent

A direct sequence scan of Q02465 found **zero NPF (Asn-Pro-Phe) motifs** and zero NPY variants. This matters mechanistically: canonical mammalian SCAMP1–3 carry two to four N-terminal NPF repeats that bind EH-domain proteins (e.g., intersectin, EHD family) to recruit the machinery driving endocytic and exocytic vesicle trafficking. SpiA's N-terminal cytoplasmic region (~residues 1–110) is instead **short, partly disordered (annotated disordered 1–35), and Ser/Ala/Pro-rich**, not an NPF-repeat interaction module, and the protein is shorter (269 aa) than the long mammalian SCAMPs (~330 aa). The absence of the very motif that mechanistically links SCAMPs to vesicle traffic undermines the specific trafficking claim. *Caveat:* the short human SCAMP4/SCAMP5 (229/235 aa) are also NPF-less yet still traffic, so NPF absence is suggestive rather than decisive.

### Finding 3 — The demonstrated function of SpiA is spore-coat-associated stability, not trafficking

The decisive evidence is the loss-of-function study of Richardson & Loomis 1992 ([PMID: 1592257](https://pubmed.ncbi.nlm.nih.gov/1592257/)). Using homologous recombination to delete *spiA*, they found that **spiA-null cells develop normally and produce morphologically normal spores** (indistinguishable from wild type by transmission and scanning EM). The defect is one of **durability, not formation**: as spiA-null spores age, they lose viability far faster than the parent — after 11 days submerged in dilute buffer (conditions preventing germination), **spiA-null spore viability dropped ~10⁵-fold versus only ~10-fold for the parent** — a phenotype rescued by reinserting an intact *spiA* copy. The gene product **Dd31 (30 kDa) associates with the inner face of the spore coat in a detergent-resistant manner**, consistent with a structural role stabilizing the dormant spore. The experimental GO annotations mirror this biology: **spore wall (GO:0031160, IDA)**, **sorocarp development (GO:0030587, IMP)**, and **culmination (GO:0031154, IEP)** — while all trafficking terms remain IBA/IEA.

### Finding 4 — SpiA is the ONLY SCAMP gene in *D. discoideum*, ruling out paralog confusion

UniProt searches restricted to organism 44689 return **exactly one protein** for Pfam PF04144, one for InterPro IPR007273, and one for PANTHER PTHR10687 — Q02465/spiA in all three cases. There is therefore **no within-organism paralog-confusion risk**. For comparison, humans carry five SCAMPs (SCAMP1 O15126 338 aa, SCAMP2 O15127 329 aa, SCAMP3 O14828 347 aa, SCAMP4 Q969E2 229 aa, SCAMP5 Q8TAC9 235 aa). SpiA (269 aa) is closest in size to the short SCAMP4/5 subgroup, which also lack NPF repeats yet still function in synaptic-vesicle trafficking — keeping the trafficking hypothesis alive as a possibility but not a fact. The single-copy status cuts both ways: it removes paralog confusion but implies *Dictyostelium* has repurposed its lone ancestral SCAMP toward a lineage-specific, developmentally restricted spore-coat role.

### Finding 5 — Quantitative confirmation: ~28% identity to human SCAMPs, concentrated in the TM core

Global Needleman–Wunsch alignment of SpiA against the five human SCAMPs gave **SCAMP1 30.6%, SCAMP3 30.6%, SCAMP2 28.9%, SCAMP4 26.6%, SCAMP5 23.8% (mean 28.1%)**. The highest identity is to the *long* SCAMP1/SCAMP3 rather than the size-matched short SCAMP4/5, indicating that conservation is concentrated in the transmembrane core rather than the cytoplasmic tails. This twilight-zone identity, combined with concordant Pfam/InterPro/PANTHER HMM hits, solidly confirms genuine but divergent SCAMP-family membership while explaining why the trafficking-associated N-terminal features are not conserved.

---

## Mechanistic Model / Interpretation

```
                    SEED HYPOTHESIS
    "SpiA is a SCAMP that functions in vesicular trafficking"
                          |
         +----------------+----------------+
         |                                 |
   CLAIM A: family                  CLAIM B: function
   "is a SCAMP"                     "vesicular trafficking"
         |                                 |
   SUPPORTED (strong)              WEAK / homology-only
   - PF04144, IPR007273,           - all trafficking GO = IBA/IEA
     PTHR10687:SF2                  - NO NPF motifs (canonical SCAMP
   - 4-TM core                        trafficking motif absent)
   - 28.1% id to human SCAMPs      - divergent, short disordered N-term
   - single-copy (no paralog       - NO organism-specific trafficking assay
     confusion)                          |
                                   DEMONSTRATED FUNCTION instead:
                                   - spiA-null: normal spores that lose
                                     viability 10^5-fold on aging
                                   - Dd31 on INNER spore coat,
                                     detergent-resistant
                                   - GO: spore wall (IDA), sorocarp
                                     dev (IMP), culmination (IEP)
```

The most parsimonious model is that *Dictyostelium* possesses a single, ancestral SCAMP that has been **evolutionarily specialized as a structural component of the dormant spore's inner coat**. Its SCAMP membrane architecture (4-TM core) is retained and likely inserts into spore-coat/plasma membranes, but the trafficking-adaptor module (N-terminal NPF repeats) that defines canonical SCAMP trafficking has been lost or never elaborated in this lineage. Developmental regulation (PKA → SrfA → spiA) places SpiA firmly in a terminal-differentiation/sporulation program, not a constitutive membrane-traffic pathway.

An important caveat preserves a minimal trafficking possibility: the spore coat itself is assembled from secreted prespore-vesicle contents, and clathrin-mediated traffic is required for spore differentiation ([PMID: 9053320](https://pubmed.ncbi.nlm.nih.gov/9053320/)). So SpiA operates *within* a trafficking-dependent developmental context, but the data localize SpiA to the *product* (the inner coat) rather than the *machinery* (vesicles/adaptors). Being embedded in a trafficking-dependent process is not the same as being a trafficking effector — indeed, the clathrin data place spiA expression *downstream* of the trafficking machinery.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt Q02465 (PF04144, IPR007273, PTHR10687:SF2) | Structural/evolutionary + computational | Supports | SpiA is a SCAMP-family protein | SCAMP domain + 4 TM helices = canonical SCAMP core | *D. discoideum* record | High for family; homology-based (ECO:0000305/IEA) |
| Sequence scan of Q02465 (this work) | Computational | Qualifies/refutes trafficking | Does SpiA have canonical SCAMP trafficking motifs? | **Zero NPF/NPY motifs**; short, disordered, Ser/Ala/Pro-rich N-terminus; 269 aa vs ~330 aa | In-silico | Weakened caveat: short human SCAMP4/5 also NPF-less yet traffic |
| Needleman–Wunsch alignment (this work) | Structural/evolutionary + computational | Supports family; qualifies trafficking | Quantitative SCAMP identity | 28.1% mean identity to 5 human SCAMPs, concentrated in TM core | Sequence | High; conservation in core not termini |
| UniProt taxon-44689 search (this work) | Computational | Qualifies | Paralog confusion? | Exactly one SCAMP gene in *D. discoideum* (=spiA); human has 5 | Genome-wide | High; rules out within-organism paralog cross-annotation |
| Richardson & Loomis 1992, [PMID: 1592257](https://pubmed.ncbi.nlm.nih.gov/1592257/) | Mutant phenotype + localization | Refutes trafficking as core; supports spore role | What does SpiA do? | spiA-null → normal spores lose viability 10⁵-fold on aging; Dd31 on inner spore coat, detergent-resistant; rescued by re-insertion | *D. discoideum* spores | High; decisive functional study. No trafficking assay done |
| Escalante & Sastre 1998, [PMID: 9729488](https://pubmed.ncbi.nlm.nih.gov/9729488/) | Expression/regulation | Qualifies (context) | When/where is spiA expressed | Late prespore/spore maturation marker; mRNA reduced in srfA-null | Sporulation | Medium-high; spore-specific, not vegetative-trafficking context |
| SrfA/PKA study, [PMID: 12204259](https://pubmed.ncbi.nlm.nih.gov/12204259/) | Expression/regulation | Qualifies (context) | Regulation of spiA | spiA induced via PKA→SrfA at culmination | Sporulation | Medium; regulatory context |
| Niswonger & O'Halloran 1997, [PMID: 9053320](https://pubmed.ncbi.nlm.nih.gov/9053320/) | Mutant phenotype (clathrin) | Competing/context | Is spiA downstream of trafficking machinery? | Clathrin-minus cells fail to express spiA and make no spores | Development | Medium; places spiA downstream of, not as, trafficking effector |
| stkA/stalky, [PMID: 11100898](https://pubmed.ncbi.nlm.nih.gov/11100898/); [PMID: 8898200](https://pubmed.ncbi.nlm.nih.gov/8898200/) | Mutant phenotype/expression | Qualifies (context) | spiA as spore-pathway marker | spiA fails to express in stalky mutants; spore-specific transcript | Cell-fate | Medium; confirms spore-specificity |
| yelA, [PMID: 9254905](https://pubmed.ncbi.nlm.nih.gov/9254905/) | Mutant phenotype/expression | Qualifies (context) | spiA as sporulation marker | spiA precociously expressed in yelA-null | Development | Low-medium; regulatory context only |

---

## GO Curation Implications

**Likely curation action (leads requiring curator verification):**

- **Retain (direct evidence):** `GO:0031160 spore wall` (IDA), `GO:0030587 sorocarp development` (IMP), `GO:0031154 culmination involved in sorocarp development` (IEP). Consider adding `GO:0016021 integral component of membrane` (4 TM helices) and a spore-coat CC consistent with the detergent-resistant inner-coat localization.
- **Keep but flag as non-core / homology-only:** `GO:0006887 exocytosis` (IBA), `GO:0055038 recycling endosome membrane` (IBA), `GO:0032588 trans-Golgi network membrane` (IBA), `GO:0015031 protein transport` (IEA). Do **not** upgrade to experimental; the divergent, NPF-less sequence weakens automatic SCAMP propagation, and no *Dictyostelium* trafficking assay exists.
- **Family/MF term:** the SCAMP-family membrane-protein assignment is justified from PF04144/IPR007273; avoid asserting a specific vesicular-transport MF beyond family membership, and avoid "protein binding" as a final recommendation.
- **Seed-hypothesis-as-core-function:** Do **not** record "vesicular membrane trafficking" as SpiA's primary function; the supported core function is spore-coat-associated maintenance of spore viability within sorocarp development.

### GO Decision Table (computed — lead requiring curator verification)

| GO_ID | term | aspect | evidence code | curation lead | rationale |
|---|---|---|---|---|---|
| GO:0031160 | spore wall | CC | IDA (dictyBase) | **RETAIN** | Direct: Dd31 on inner face of spore coat (PMID 1592257) |
| GO:0030587 | sorocarp development | BP | IMP (dictyBase) | **RETAIN** | Direct: spiA-null spore-instability phenotype (PMID 1592257) |
| GO:0031154 | culmination in sorocarp development | BP | IEP (dictyBase) | **RETAIN** | Spore/prespore-specific expression at culmination |
| GO:0016021 | integral component of membrane | CC | (add) ISS/IEA | **ADD-LEAD** | 4 predicted TM helices; supported by topology |
| GO:0006887 | exocytosis | BP | IBA (GO_Central) | **KEEP-NONCORE** | Homology-only; no *Dictyostelium* assay |
| GO:0055038 | recycling endosome membrane | CC | IBA (GO_Central) | **KEEP-NONCORE** | Homology-only; conflicts with spore-coat localization |
| GO:0032588 | trans-Golgi network membrane | CC | IBA (GO_Central) | **KEEP-NONCORE** | Homology-only; no organism-specific data |
| GO:0015031 | protein transport | BP | IEA (InterPro) | **KEEP-NONCORE** | Electronic family propagation only |

---

## Mechanistic Scope

The immediate molecular identity tested is an integral, multi-pass (4-TM) SCAMP-family membrane protein. The direct cellular function demonstrated is association with the inner face of the spore coat and maintenance of spore structural integrity/viability during dormancy. The proposed "vesicular membrane trafficking" is a **family-level inference, not a measured activity**; the spore-instability phenotype is the demonstrated loss-of-function outcome and is developmental/structural, not a generic trafficking defect. Distinctions to keep clear:

- **Direct activity (demonstrated):** membrane-embedded, inner-spore-coat protein required to maintain spore viability during dormancy.
- **Direct activity (hypothesized, homology-only):** SCAMP-type vesicular carrier — not shown in *Dictyostelium*, and weakened by NPF-motif absence.
- **Downstream/context phenotype:** the spore-viability decay on aging is the *readout* of losing a structural protein, not evidence of a trafficking defect.
- **Pathway context:** spore-coat assembly overall depends on vesicular secretion and clathrin ([PMID: 9053320](https://pubmed.ncbi.nlm.nih.gov/9053320/)), but those functions belong to other genes; SpiA is a cargo/product component, not the machinery.

---

## Conflicts and Alternatives

- **Divergent-paralog / over-propagation risk:** SpiA lacks canonical SCAMP NPF EH-binding repeats, so IBA transfer of exocytosis/recycling-endosome/TGN terms from long metazoan/plant SCAMPs may over-annotate this specialized ortholog. *Caveat:* short human SCAMP4/5 are also NPF-less yet still traffic, so NPF absence is suggestive, not decisive.
- **Single-SCAMP genome:** *D. discoideum* encodes exactly one SCAMP-family gene — spiA itself. This removes classic paralog confusion (no separate housekeeping SCAMP to mis-map), but implies the lone ancestral SCAMP was co-opted/neofunctionalized for a terminal spore-coat role, so uncritically propagating generic SCAMP trafficking terms is risky.
- **Developmental specialization:** SpiA is expressed only at terminal spore differentiation, unlike housekeeping SCAMPs that operate constitutively.
- **Downstream vs. effector:** clathrin-minus data ([PMID: 9053320](https://pubmed.ncbi.nlm.nih.gov/9053320/)) place spiA expression *downstream* of the trafficking machinery, arguing SpiA is a differentiation product rather than a trafficking effector.

---

## Limitations and Knowledge Gaps

1. **Direct trafficking assay in *Dictyostelium* — none exists.** Checked PubMed; no *Dictyostelium* SCAMP/exocytosis study found. Resolving this would determine whether the IBA terms are real.
2. **Membrane topology/orientation** — predicted (4 TM) but not experimentally mapped; matters for whether cytoplasmic loops could engage trafficking partners.
3. **Interaction partners** — no known EH-domain or SNARE partners; NPF absence predicts none. An interactome would test the trafficking mechanism.
4. **N-terminal function unknown** — the Ser/Ala/Pro-rich disordered N-terminus is uncharacterized and may mediate a *Dictyostelium*-specific interaction (e.g., with coat proteins such as SP85/PsB, [PMID: 12455962](https://pubmed.ncbi.nlm.nih.gov/12455962/)).
5. **Structure not experimentally solved** — only predicted TM topology is available; an AlphaFold model exists but was not parsed here.
6. **Single functional study** — the definitive phenotype rests largely on one 1992 deletion study; modern reproduction with quantitative trafficking assays would strengthen the negative-for-trafficking case.

Overall, conclusions about trafficking are conservative because they hinge on absence of evidence plus motif divergence rather than a direct negative assay.

---

## Discriminating Tests

- **GFP-SpiA live imaging** across vegetative and developing cells: does it traffic through endosomes/TGN/plasma membrane, or only deposit at the forming spore coat?
- **Endocytosis/exocytosis assays in spiA-null vegetative cells** (fluid-phase uptake, lysosomal-enzyme secretion, contractile-vacuole dynamics) to test for a generic trafficking phenotype.
- **Interaction proteomics (BioID/AP-MS)** for EH-domain proteins/SNAREs (trafficking) vs. spore-coat proteins such as SP85/PsB, SP60, cotB (structural).
- **Domain-swap/rescue:** can a mammalian SCAMP rescue spiA-null spore instability, and can SpiA rescue a SCAMP-trafficking defect? Tests functional equivalence.
- **Comparative genomics across Amoebozoa** to determine whether the single-SCAMP, spore-specialized configuration is lineage-conserved.

---

## Curation Leads (require curator verification)

- **Reference to verify:** [PMID: 1592257](https://pubmed.ncbi.nlm.nih.gov/1592257/) (Richardson & Loomis 1992) — snippet: *"Dd31 is associated with the inner face of spore coat fragments in a detergent-resistant manner. This location is consistent with its observed role in maintaining stability of the spores."* Supports spore-coat CC + spore-stability BP as the core function.
- **Reference to verify:** [PMID: 9729488](https://pubmed.ncbi.nlm.nih.gov/9729488/) (Escalante & Sastre 1998) — spiA as srfA-dependent spore maturation marker.
- **Reference to verify:** [PMID: 9053320](https://pubmed.ncbi.nlm.nih.gov/9053320/) — clathrin (not SpiA) is the trafficking component required upstream of spiA expression.
- **Candidate action changes:** retain direct spore terms; add `GO:0016021 integral component of membrane`; keep trafficking terms with IBA/IEA codes but **do not treat as core**; add a curator note that SpiA is a divergent, NPF-less SCAMP with no organism-specific trafficking evidence.
- **Suggested questions for curator:** Should IBA exocytosis/recycling-endosome/TGN terms be retained for a lineage-specific, motif-divergent SCAMP with a demonstrated non-trafficking phenotype? Is a spore-coat structural-constituent term warranted?
- **Suggested experiments:** GFP-SpiA localization time-course; endo/exocytosis assays in spiA-null; interaction proteomics — as detailed under Discriminating Tests.

---

## Evidence Base (Literature Summary)

| PMID | Title (abbrev.) | Role in this evaluation |
|---|---|---|
| [1592257](https://pubmed.ncbi.nlm.nih.gov/1592257/) | *Disruption of spiA leads to spore instability* | **Decisive.** Establishes spore-coat structural role; refutes trafficking as primary function |
| [9729488](https://pubmed.ncbi.nlm.nih.gov/9729488/) | *SRF homolog required for spore differentiation* | Regulatory context; spiA as spore maturation marker |
| [12204259](https://pubmed.ncbi.nlm.nih.gov/12204259/) | *SrfA mediates PKA activation during sporulation* | PKA→SrfA→spiA regulatory axis |
| [9053320](https://pubmed.ncbi.nlm.nih.gov/9053320/) | *Clathrin required for spore differentiation* | Trafficking machinery is upstream of, and separate from, SpiA |
| [11100898](https://pubmed.ncbi.nlm.nih.gov/11100898/) | *STKA-dependent genes* | spiA is a spore-pathway transcript |
| [8898200](https://pubmed.ncbi.nlm.nih.gov/8898200/) | *Cell fate gene stalky* | spiA fails in stalky mutants |
| [9254905](https://pubmed.ncbi.nlm.nih.gov/9254905/) | *yelA null precocious sporulation* | spiA as precocious-sporulation marker |
| [12455962](https://pubmed.ncbi.nlm.nih.gov/12455962/) | *Outside-in signaling by spore coat protein SP85* | Spore-coat assembly context (potential SpiA partners) |
| [10556070](https://pubmed.ncbi.nlm.nih.gov/10556070/) | *Adenylyl cyclase acrA in late development* | Sporulation regulatory context |

---

## Conclusion

The seed hypothesis is **half right and half over-reaching**. SpiA is genuinely a SCAMP-family, four-transmembrane membrane protein — a call supported by concordant domain assignments, quantitative sequence identity (~28% to human SCAMPs, concentrated in the TM core), and single-copy status that rules out paralog confusion. But "functions in vesicular membrane trafficking" is an inference from mammalian homology that is (a) mechanistically weakened by SpiA's loss of the canonical NPF trafficking motifs, and (b) not the gene product's demonstrated primary function. The one direct functional study shows SpiA is a detergent-resistant inner-spore-coat protein whose loss causes accelerated spore-viability decay — a structural, developmentally restricted role. For curation, keep the SCAMP identity and the experimentally grounded spore/sorocarp terms as core, and treat the trafficking GO terms as non-core, homology-only annotations that must not be presented as SpiA's primary function.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)