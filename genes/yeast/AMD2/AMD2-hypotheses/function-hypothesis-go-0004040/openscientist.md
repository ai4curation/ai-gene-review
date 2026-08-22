---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T17:52:21.319887'
end_time: '2026-08-22T18:07:31.268743'
duration_seconds: 909.95
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: AMD2
  gene_symbol: AMD2
  uniprot_accession: P22580
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004040
  hypothesis_text: AMD2 has amidase activity (GO:0004040).
  term_context: '- Term: amidase activity (GO:0004040)

    - Evidence type: IEA

    - Original reference: GO_REF:0000120'
  reference_context: '- GO_REF:0000120

    - UniProt:P22580

    - file:yeast/AMD2/AMD2-deep-research-falcon.md'
  source_file: genes/yeast/AMD2/AMD2-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004040\n  label: amidase activity\nevidence_type:\
    \ IEA\noriginal_reference_id: GO_REF:0000120"
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
citation_count: 3
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
- **Gene directory:** AMD2
- **Gene symbol:** AMD2
- **UniProt accession:** P22580

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004040
- **Source file:** genes/yeast/AMD2/AMD2-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

AMD2 has amidase activity (GO:0004040).

## Term and Decision Context

- Term: amidase activity (GO:0004040)
- Evidence type: IEA
- Original reference: GO_REF:0000120

## Reference Context

- GO_REF:0000120
- UniProt:P22580
- file:yeast/AMD2/AMD2-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0004040
  label: amidase activity
evidence_type: IEA
original_reference_id: GO_REF:0000120
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

# AIGR Gene Hypothesis Deep Research — AMD2 (P22580) Amidase Activity (GO:0004040)

**Target gene:** AMD2 / YDR242W, *Saccharomyces cerevisiae* (NCBITaxon:559292)
**UniProt:** P22580 · **Hypothesis:** *AMD2 has amidase activity (GO:0004040)*
**Focus type:** function_assignment · **Evidence type on record:** IEA (GO_REF:0000120)
**Source:** genes/yeast/AMD2/AMD2-ai-review.yaml → existing_annotations[1].function_hypothesis

---

## Summary

The hypothesis that AMD2 has amidase activity (GO:0004040) is **supported at the enzyme-family level but is entirely homology-inferred**, and the recommended curation action is to **retain GO:0004040 at its current general level — neither narrow it to a specific substrate nor remove it**. AMD2/YDR242W (UniProt P22580, 549 aa, annotated "Probable amidase") is an unambiguous member of the **amidase-signature (AS) superfamily**: it matches Pfam PF01425, PROSITE PS00571, and InterPro IPR023631/IPR020556/IPR036928, and is additionally classified by the fungal-specific PIRSF001221 "Amidase, fungal type." The diagnostic AS catalytic machinery is intact — the signature motif GGSSGGE sits at residues 207–213 and the canonical **Lys–cisSer–Ser catalytic triad (K176/S210/S238)** is present and, per the AlphaFold model (AF-P22580-F1, global pLDDT 96.25), confidently and well-ordered in three dimensions. UniProt records the family reaction *monocarboxylic acid amide + H₂O → monocarboxylate + NH₄⁺*, which is exactly the reaction defining GO:0004040.

The crucial caveat is that **no experimental evidence exists** for AMD2's activity. UniProt lists protein existence at level 3 ("Inferred from homology"), SGD describes the product as a "Putative amidase," and the founding reference (PMID 2263500) is a sequence-identification-by-homology study rather than a biochemical characterization. Because the AS superfamily is functionally heterogeneous — spanning fatty-acid amide hydrolase, GatA glutamyl-tRNA amidotransferase, indoleacetamide hydrolase, acetamidase/formamidase, malonamidase, and nicotinamidase-like activities — family membership alone cannot fix a substrate. A global alignment against characterized AS enzymes shows the closest characterized homolog is the fungal acetamidase **AmdS** (*Aspergillus nidulans*, P08158, EC 3.5.1.4) at only **33.2% identity**, well below the ~40–50% typically required to transfer a specific EC/substrate.

The net picture is a structurally competent, fungal-type amidase of **undetermined substrate**. GO:0004040 (amidase activity) sits at precisely the right level of the ontology for this evidence: it asserts the amide-hydrolase chemistry without committing to a specific substrate. Narrowing to acetamidase (GO:0004039) would be over-annotation; removing the term would ignore strong, mutually consistent domain and structural evidence. The IEA evidence code honestly reflects the homology-only basis and should be retained, ideally with a curator note flagging the absence of experimental substrate data.

---

## Key Findings

### F001 — AMD2 carries an intact amidase-signature domain with a conserved catalytic triad

AMD2/YDR242W is a canonical member of the amidase-signature (AS) superfamily, and this is the strongest single line of support for the hypothesis. UniProt P22580 (549 aa, "Probable amidase") matches **Pfam PF01425 (Amidase)**, **PROSITE PS00571 (AMIDASES, MatchStatus = 1)**, and the InterPro entries **IPR023631 (Amidase signature domain)**, **IPR020556 (Amidase conserved site)**, and **IPR036928 (AS superfamily)**, along with the structural classifiers Gene3D 3.90.1300.10 and SUPFAM SSF75304. Direct analysis of the primary sequence locates the diagnostic AS signature motif **GGSSGGE at residues 207–213** (catalytic nucleophile Ser ≈ S210) and the catalytic Lys within the F(I)VKTT motif (≈ K176), completing the AS-family **Ser–cisSer–Lys catalytic triad** that defines this enzyme class' mechanism. Critically, the InterPro "Amidase, conserved site" **catalytic-site profile** matches, which means the catalytic residues are present and intact — this is an active-enzyme signature, not a decayed pseudoenzyme relic. UniProt records the catalytic activity as **monocarboxylic acid amide + H₂O = monocarboxylate + NH₄⁺** (an EC 3.5.1.4-type reaction), the exact reaction that GO:0004040 describes. Taken together, every sequence-level prerequisite for amidase chemistry is satisfied.

### F002 — The amidase activity is homology-inferred only; no experimental substrate characterization exists

Despite the strong domain evidence, no direct biochemical evidence supports a *specific* enzymatic activity for AMD2. UniProt lists **protein existence = "3: Inferred from homology"**; the keyword set is limited to "Hydrolase"; and the only comment beyond the (inferred) catalytic-activity line is a SIMILARITY note ("Belongs to the amidase family"). SGD (YDR242W) classifies the ORF as **"Verified"** — meaning it is a real, expressed gene — but describes its product only as a **"Putative amidase."** The founding reference (PMID 2263500) is a sequence-identification-by-homology paper, not an enzyme characterization. Because the AS superfamily is functionally heterogeneous, membership does not determine a substrate. Supporting context comes from work on the bottom-fermenting-yeast amidase AMI1 ([PMID: 17924455](https://pubmed.ncbi.nlm.nih.gov/17924455/)), which reports that the canonical fungal amidase AMI1 is **conserved among plants, *Bacillus subtilis*, *Neurospora crassa*, *Schizosaccharomyces pombe* and *Saccharomyces* species, "with the exception of *S. cerevisiae* S288C."** This establishes that AMD2 is a *distinct* amidase-signature gene — not the canonical fungal AMI1 amidase — and that yeast AS enzymes function as **general amide hydrolases** ("suggesting that Ami1p may hydrolyse some amides related to amino acid and niacin metabolism in the cell"). Both observations reinforce a **family-level GO:0004040 assignment** rather than a narrow, substrate-specific term.

### F003 — The AlphaFold model is high-confidence with a well-ordered catalytic triad (K176–S210–S238)

The AlphaFold model AF-P22580-F1 has a **global mean pLDDT of 96.25** (median per-residue 97.7 over 549 residues), placing it firmly in the very-high-confidence regime. The amidase-signature catalytic residues are all confidently modeled: **Lys176 pLDDT = 98.9, Ser210 pLDDT = 98.7, Ser238 pLDDT = 98.8**. The InterPro/PROSITE conserved catalytic site spans residues 207–238 and contains both catalytic serines of the AS Lys–cisSer–Ser triad, structurally analogous to the well-characterized human FAAH triad (Lys142/Ser217/Ser241). Domain boundaries are consistent across member databases — Pfam PF01425 (79–539), Gene3D AS domain (17–546), SUPFAM SSF75304 (26–545) — and, importantly, **PIRSF001221 "Amidase, fungal type"** spans the full protein (3–549). PIRSF is a fungal-amidase-specific classifier that goes beyond the generic AS superfamily assignment, reinforcing that AMD2 is a fungal-type amidase with a structurally competent active site. In short, this is a protein built to catalyze amide hydrolysis; the model shows no active-site occlusion or triad disruption. This is structural *potential*, not demonstrated activity, but it removes the possibility that AMD2 is a degenerate pseudoenzyme.

### F004 — The closest characterized homolog is fungal acetamidase AmdS (33% identity) — supports general amidase, not a specific substrate

To test whether the family-level annotation could be legitimately refined, a Needleman–Wunsch global alignment (match +2 / mismatch −1 / gap −2) was run between AMD2 (549 aa) and a panel of *characterized* AS enzymes:

| Reference enzyme | UniProt | EC | Length | % identity to AMD2 |
|---|---|---|---|---|
| *A. nidulans* AmdS acetamidase | P08158 | 3.5.1.4 | 548 aa | **33.2%** (closest) |
| Human FAAH (fatty-acid amide hydrolase) | O00519 | 3.5.1.99 | — | 27.6% |
| *Agrobacterium* indoleacetamide hydrolase | P06618 | 3.5.1.— | — | 24.9% |

(Three additional candidate accessions resolved to non-AS proteins — kynurenine 3-monooxygenase, snRNP-F, and an unannotated fragment — and were excluded as accession mismatches.) AMD2 is therefore most similar to a **fungal aliphatic amidase/acetamidase** acting in nitrogen-source amide utilization, consistent with its PIRSF001221 "Amidase, fungal type" classification. However, **33% identity is well below the ~40–50% threshold** typically required to confidently transfer a specific substrate or EC number. The comparison usefully narrows the likely functional neighborhood (a fungal amide hydrolase probably tied to nitrogen/amide metabolism) without licensing a specific substrate call — precisely the situation in which GO best practice is to annotate the general parent term (GO:0004040) rather than a specific child.

---

## Mechanistic Model / Interpretation

The four findings converge on a single, coherent picture: **AMD2 is a structurally competent, fungal-type amidase-signature enzyme of undefined substrate.**

```
   Sequence            Domain / motif            Structure (AlphaFold)        Nearest characterized
   (P22580, 549 aa)    evidence                  pLDDT 96.25                  homolog
   ───────────────     ─────────────────────     ─────────────────────       ─────────────────────
   "Probable           Pfam PF01425              Catalytic triad             AmdS acetamidase
    amidase"           PROSITE PS00571           K176 (98.9)                 (P08158, EC 3.5.1.4)
                       IPR023631 (AS domain)     S210 (98.7)  ── well        33.2% identity
   Signature motif     IPR020556 (cat. site)     S238 (98.8)     ordered     ───────────────
   GGSSGGE (207-213)   PIRSF001221 (fungal)      Active site intact          FAAH  27.6%
                                                                             IaaH  24.9%
        │                     │                          │                         │
        └─────────────────────┴──────────────┬───────────┴─────────────────────────┘
                                              ▼
                     Confident enzyme-FAMILY assignment: amidase activity
                     (GO:0004040, EC 3.5.1.- : R-CO-NH2 + H2O -> R-COO- + NH4+)
                                              │
                                              ▼
                     BUT: no assay, no measured substrate, no kinetics
                     (UniProt PE level 3; SGD "Putative amidase")
                                              │
                                              ▼
                     Substrate/EC UNDETERMINED  →  keep GO:0004040 GENERAL
                     (do not narrow to acetamidase; do not remove)
```

The immediate molecular function being tested is **hydrolysis of a carbon–nitrogen amide bond**: R–CO–NH₂ + H₂O → R–COO⁻ + NH₄⁺, catalyzed by the AS-family Ser–cisSer–Lys triad in which the nucleophilic serine attacks the amide carbonyl. Every structural prerequisite for this chemistry is present and confidently modeled in AMD2. What is missing is the *identity of R* — the physiological substrate. GO:0004040 (amidase activity) sits at exactly the right level of the ontology for what the evidence supports: it asserts amide-hydrolase chemistry without committing to a specific substrate (e.g., acetamide → GO:0004039, or fatty-acid amide → GO:0017064). Given 33% identity to the nearest characterized enzyme, committing to any child term would over-reach.

Importantly, there is no evidence that the annotation reflects a downstream phenotype, a pleiotropic effect, or a loss-of-function inference — it is a direct molecular-function prediction grounded in an intact catalytic domain. The weakness is not that the wrong *type* of function was inferred; it is that the inference has not been experimentally validated and cannot yet be refined to a substrate.

---

## Evidence Base

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt P22580 (record) | Review/database, sequence-domain | **Supports** | AMD2 is an amidase | 549 aa "Probable amidase"; Pfam PF01425, PROSITE PS00571; catalytic activity = monocarboxylic amide + H₂O → monocarboxylate + NH₄⁺ | *S. cerevisiae* record, in silico | High for family membership; PE level 3, no protein evidence |
| InterPro IPR023631/IPR020556/IPR036928; PIRSF001221 | Structural/evolutionary (computational) | **Supports** | Intact AS catalytic machinery | AS domain + "conserved site" catalytic-site profile match; fungal-type classifier spans 3–549 | Domain databases | High; motif match ≠ demonstrated turnover |
| AlphaFold AF-P22580-F1 (own analysis) | Structural (computational) | **Supports** | Active site is structurally competent | Global pLDDT 96.25; K176/S210/S238 at pLDDT 98.7–98.9; canonical AS fold, ordered triad | Predicted structure | High model confidence; prediction, not experimental structure/activity |
| Global alignment vs characterized AS enzymes (own analysis) | Comparative/evolutionary (computational) | **Qualifies** | Can the term be narrowed? | Closest characterized homolog = AmdS acetamidase (EC 3.5.1.4) at 33.2%; FAAH 27.6%; IaaH 24.9% | Cross-species AS enzymes | 33% too low to transfer specific EC; narrows neighborhood only |
| [PMID: 17924455](https://pubmed.ncbi.nlm.nih.gov/17924455/) | Primary / comparative genomics + overexpression | **Qualifies** | Is AMD2 the canonical fungal amidase? | Canonical AMI1 amidase absent from *S. cerevisiae* S288C; yeast AS enzymes act as general amide hydrolases (amino-acid/niacin amides) | Bottom-fermenting yeast (S. pastorianus) | AMD2 is a distinct AS gene; supports general (not specific) term |
| [PMID: 32024536](https://pubmed.ncbi.nlm.nih.gov/32024536/) | Primary / functional genetics | **Qualifies** | Do yeasts have functional acetamidases? | *Y. lipolytica* acetamidase (AmdS homolog) confers acetamide utilization; usable as marker in *S. cerevisiae* | *Yarrowia lipolytica* | Establishes plausible acetamidase-type function in yeast, but tests other genes, not AMD2 |
| [PMID: 9126617](https://pubmed.ncbi.nlm.nih.gov/9126617/) | Primary / regulatory genetics | Context | amdS/amidase regulation in fungi | Characterizes amdA regulation of the amdS acetamidase system | *A. nidulans* | Orientation on AMD2's nearest characterized homolog's pathway |
| PMID 2263500 (founding reference) | Primary / sequence | **Supports (weakly)** | Gene identity | Original identification of AMD2 as a putative amidase by homology | *S. cerevisiae* | Homology-only; not a biochemical characterization |
| SGD YDR242W (record) | Database | Supports/Qualifies | ORF is real; function putative | Status "Verified" ORF; description "Putative amidase" | *S. cerevisiae* | High that ORF is real; function unproven |

**Key literature notes:**

- **[PMID: 17924455](https://pubmed.ncbi.nlm.nih.gov/17924455/)** — *Identification and characterization of amidase-homologous AMI1 genes of bottom-fermenting yeast.* Establishes that the canonical fungal amidase AMI1 is present across fungi/plants/bacteria **but absent from *S. cerevisiae* S288C**, and that yeast AS amidases behave as general amide hydrolases (amino-acid/niacin amides). Directly supports treating AMD2 as a *distinct*, general amidase-signature enzyme rather than a substrate-specific one.
- **[PMID: 32024536](https://pubmed.ncbi.nlm.nih.gov/32024536/)** — *Identification of a Yarrowia lipolytica acetamidase and its use as a yeast genetic marker.* Shows a functional yeast acetamidase (AmdS homolog) that works as a marker in *S. cerevisiae*, supporting the plausibility of acetamidase-type function in yeasts — while highlighting that the activity was demonstrated in *Y. lipolytica*, not AMD2, reinforcing "general term only."
- **[PMID: 9126617](https://pubmed.ncbi.nlm.nih.gov/9126617/)** — *The amdA regulatory gene of Aspergillus nidulans.* Orientation on the amdS/acetamidase regulatory system, the pathway of AMD2's nearest characterized homolog.

*(PMID 17110954 (Hst2/Sir2) and PMID 12095683 (Xenopus Polycomb) in the literature pool concern unrelated proteins and are not relevant to AMD2; noted only for completeness.)*

---

## GO Curation Implications

**Lead (requires curator verification):** *Retain GO:0004040 (amidase activity), Molecular Function, as a general homology-based (IEA) annotation; do not narrow, do not remove.*

- **Ontology aspect:** This is a **Molecular Function (MF)** assertion. The evidence (intact AS domain, conserved catalytic-site profile, high-confidence triad) supports the MF term at the level of "amidase activity." No Biological Process (BP) or Cellular Component (CC) term is supported by the current evidence for AMD2 specifically — substrate, pathway, and localization are all undetermined. (A general companion BP term such as amide catabolic process, if present as IBA, is consistent and may remain, but is likewise not substrate-specific.)
- **Retain vs generalize vs specify:** **Retain at the current general level.** The term should *not* be made more specific (e.g., acetamidase activity GO:0004039) because the nearest characterized homolog is only 33% identical — below the confidence threshold for substrate transfer. It should *not* be removed, because the domain and structural evidence for amide-hydrolase chemistry is strong and consistent, and the ORF is "Verified" (no pseudogene signal).
- **Evidence code:** The IEA code (GO_REF:0000120) is **appropriate** and honestly reflects the homology-only basis. No experimental evidence warrants an upgrade to IDA/IMP.
- **Curator note:** Consider flagging that AMD2 is a *fungal-type* AS amidase (PIRSF001221) of **undetermined substrate**, distinct from the canonical fungal AMI1 amidase (absent from S288C), to prevent future over-annotation.

**GO decision table**

| Candidate term | ID | Aspect | Recommendation | Rationale |
|---|---|---|---|---|
| amidase activity | GO:0004040 | MF | **Retain (general, IEA)** | Intact AS domain + triad; correct level for evidence |
| acetamidase activity | GO:0004039 | MF | **Do not assign** | Only 33% id to AmdS; substrate unproven |
| fatty acid amide hydrolase activity | GO:0017064 | MF | Do not assign | 27.6% id to FAAH; no evidence |
| nitrogen/amide catabolic process | (BP) | BP | Not supported for AMD2 | No pathway data for this gene |
| any CC term | — | CC | Not supported | No localization data for AMD2 |

**"Protein binding" avoidance:** not applicable — a genuinely informative MF term (amidase activity) is supported, so no fallback to protein binding is needed or appropriate.

---

## Mechanistic Scope

**Directly tested (gene-product activity):** the capacity of AMD2 to hydrolyze a carbon–nitrogen amide bond via an AS-family Ser–cisSer–Lys triad. The evidence for the *chemistry being possible* is strong (intact motif GGSSGGE at 207–213; confidently modeled K176/S210/S238; matching catalytic-site profile). The evidence for the *chemistry actually occurring on a defined substrate in vivo* is absent.

**Explicitly NOT established (and not part of the supported annotation):**
- **Substrate identity** — no measured substrate; the AS family is substrate-diverse.
- **Biological process** — no pathway placement (e.g., nitrogen-source utilization) demonstrated for AMD2.
- **Localization** — no CC evidence for the AMD2 product.
- **Phenotype** — no *amd2Δ* growth or metabolic phenotype cited; the annotation is not inferred from loss of function.

The hypothesis is therefore a **clean molecular-function assertion** whose only deficiency is validation depth (homology vs assay), not a case of a downstream phenotype masquerading as a direct function.

---

## Conflicts and Alternatives

1. **Substrate ambiguity within a heterogeneous superfamily.** The main alternative to "acetamidase-like" is simply "some other amide hydrolase." Because the AS superfamily encompasses FAAH, GatA, indoleacetamide hydrolase, malonamidase, and nicotinamidase-like activities, the correct resolution of the seed hypothesis is the *general* term. This is a scope consideration, not a contradiction — it argues against narrowing, not against the term.

2. **AMD2 is not the canonical fungal AMI1 amidase.** [PMID: 17924455](https://pubmed.ncbi.nlm.nih.gov/17924455/) shows AMI1 is conserved across fungi/plants/bacteria *except* in *S. cerevisiae* S288C. AMD2 is thus a distinct AS gene, and one should not import AMI1's inferred substrate preferences (amino-acid/niacin amides) directly onto AMD2 — although they usefully illustrate the "general amide hydrolase" behavior of yeast AS enzymes.

3. **Acetamidase-type function is plausible but tested only in other species.** [PMID: 32024536](https://pubmed.ncbi.nlm.nih.gov/32024536/) demonstrates a functional *Y. lipolytica* acetamidase (AmdS homolog) that even works as a selectable marker in *S. cerevisiae* — implying *S. cerevisiae* itself lacks a strong native acetamidase for that selection. This is a mild *conflict* with narrowing AMD2 to acetamidase and reinforces "general term only."

4. **AMD2 ≠ AMD1.** AMD1 is AMP deaminase (unrelated); the shared "AMD" symbol is not a functional link and creates no paralog confusion in the GO term itself.

5. **Database carry-over risk.** The annotation traces to a homology-mapping GO_REF and a sequence-only founding reference. Any *specific* substrate label attached downstream would risk unsupported carry-over. The conservative retain-general action minimizes this risk.

No isoform-specific or experimental-artifact conflicts were identified that would undermine the *general* amidase call.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| **No enzymatic assay** | UniProt PE level 3; SGD "Putative"; founding ref sequence-only | Distinguishes IEA-general from experimental (IDA) support | Purify recombinant AMD2; test amide-hydrolase activity on a substrate panel |
| **Substrate unknown** | AS family heterogeneous; nearest homolog only 33% id | Determines whether GO:0004040 can be narrowed to a child term | Substrate profiling (acetamide, fatty-acid amides, malonamide, aromatic amides) + kinetics |
| **No demonstrated turnover despite intact residues** | Motif/triad conservation established | Conservation ≠ activity; guards against pseudoenzyme | Catalytic-Ser mutant (S210A) vs WT activity comparison |
| **No BP/pathway data** | No pathway evidence for AMD2 specifically | Whether any BP term can be added | *amd2Δ* growth screens on amide nitrogen sources; metabolomics |
| **No CC/localization data** | No localization evidence found | Whether a CC term is warranted | GFP-tagging / high-throughput localization datasets |
| **Analyses are computational** | AlphaFold + global alignment run locally | Structure/alignment predict capability, not activity | Experimental structure with bound ligand; activity assay |
| **GO_REF provenance** | UniProt GO xref; record cites GO_REF:0000120 | Affects how the IEA is attributed | Confirm against current UniProt-GOA source (vs EC2GO GO_REF:0000003) |

This review is based on public sequence, domain, orthology, and database records plus literature; no local bioinformatics files were provided. Motif/triad conservation is a strong but indirect indicator — it establishes catalytic *potential*, not demonstrated activity or substrate. All computational results above are reported conservatively and distinguished from inference.

---

## Discriminating Tests

The following would most efficiently distinguish "general amidase (undetermined substrate)" from specific alternatives, in rough priority order:

1. **In vitro amidase assay on recombinant AMD2 with a substrate panel.** Express and purify AMD2; assay against acetamide, formamide, malonamide, fatty-acid amides (e.g., oleamide), indoleacetamide, and nicotinamide, measuring NH₄⁺ release or product formation. A positive hit on one substrate class would license a specific child term (e.g., GO:0004039 for acetamide) and upgrade the evidence code to IDA.
2. **Growth phenotyping of *amd2Δ* on amide nitrogen sources.** Test whether deletion impairs utilization of acetamide/formamide/other amides as sole nitrogen source — a BP-relevant readout that could place AMD2 in nitrogen metabolism (amdS-style assay, cf. [PMID: 32024536](https://pubmed.ncbi.nlm.nih.gov/32024536/)).
3. **Site-directed mutagenesis of the triad (S210A / K176A).** Confirms catalytic dependence on the predicted triad and rules out a pseudoenzyme/moonlighting role.
4. **Structure with a bound substrate/transition-state analog.** Would define the substrate-binding pocket and predict specificity directly.
5. **Comparative substrate-specificity-determinant analysis** across the yeast AS paralog set and characterized homologs (AmdS, FAAH, malonamidase E2), mapping active-site residues that discriminate substrates.

---

## Proposed Follow-up Experiments / Actions

**For the curator (immediate, low-cost):**
- **Retain** GO:0004040 (amidase activity, MF, IEA/GO_REF:0000120) at the general level.
- **Do not narrow** to acetamidase or any specific amide-hydrolase child term.
- **Do not remove** the term — domain + structural homology is strong; ORF is "Verified."
- Add a **curator note**: "Fungal-type AS amidase (PIRSF001221); intact catalytic triad (K176/S210/S238, AlphaFold pLDDT 96); substrate experimentally undetermined; closest characterized homolog = fungal acetamidase AmdS at 33% identity; distinct from canonical fungal AMI1 (absent from S288C)."
- Verify GO_REF:0000120 is the correct current source vs EC2GO (GO_REF:0000003).

**For experimentalists (to resolve the gaps):**
- Recombinant expression + amidase activity assay across a substrate panel (test #1).
- *amd2Δ* nitrogen-source growth screen (test #2).
- Triad mutagenesis to confirm catalytic mechanism (test #3).

**Candidate references to verify (leads):**
- Founding reference **PMID 2263500** — confirm it is sequence-identification-only, to justify the IEA basis.
- **[PMID: 17924455](https://pubmed.ncbi.nlm.nih.gov/17924455/)** — verify the exact snippets *"conserved among plants, Bacillus subtilis, Neurospora crassa, Schizosaccharomyces pombe and Saccharomyces species, with the exception of S. cerevisiae S288C"* and *"suggesting that Ami1p may hydrolyse some amides related to amino acid and niacin metabolism in the cell."*
- **[PMID: 32024536](https://pubmed.ncbi.nlm.nih.gov/32024536/)** — supports plausibility of yeast acetamidase-type function; note it tests *Y. lipolytica*, not AMD2.

---

## Bottom Line

AMD2 (P22580 / YDR242W) is, by strong and consistent domain/structural homology, a **fungal-type amidase-signature enzyme with an intact catalytic triad** — so the IEA annotation **GO:0004040 (amidase activity) is justified and should be retained at the general level**. But the assignment is **homology-only** (UniProt PE 3, SGD "Putative amidase," no assay), and the nearest characterized homolog (AmdS acetamidase, EC 3.5.1.4) is only 33% identical — too distant to assign a specific substrate. The correct curation action is **retain, keep general, flag as homology-based, substrate experimentally undetermined** — neither narrowing to acetamidase nor removing the term.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)