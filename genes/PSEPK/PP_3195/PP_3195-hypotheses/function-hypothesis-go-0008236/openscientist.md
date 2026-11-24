---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:40:32.650649'
end_time: '2026-10-24T05:04:30.196911'
duration_seconds: 1437.55
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: PSEPK
  gene: PP_3195
  gene_symbol: PP_3195
  uniprot_accession: Q88I07
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008236
  hypothesis_text: PP_3195 has serine-type peptidase activity (GO:0008236).
  term_context: '- Term: serine-type peptidase activity (GO:0008236)

    - Evidence type: IEA

    - Original reference: GO_REF:0000002'
  reference_context: '- GO_REF:0000002

    - file:PSEPK/PP_3195/PP_3195-deep-research-openscientist.md'
  source_file: genes/PSEPK/PP_3195/PP_3195-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008236\n  label: serine-type peptidase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000002"
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
citation_count: 5
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: PP_3195_GO_decision_table.csv
  path: openscientist_artifacts/PP_3195_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist PP 3195 GO decision table
- filename: PP_3195_family_homolog_EC.csv
  path: openscientist_artifacts/PP_3195_family_homolog_EC.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist PP 3195 family homolog EC
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
- **Gene directory:** PP_3195
- **Gene symbol:** PP_3195
- **UniProt accession:** Q88I07

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008236
- **Source file:** genes/PSEPK/PP_3195/PP_3195-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis

PP_3195 has serine-type peptidase activity (GO:0008236).

## Term and Decision Context

- Term: serine-type peptidase activity (GO:0008236)
- Evidence type: IEA
- Original reference: GO_REF:0000002

## Reference Context

- GO_REF:0000002
- file:PSEPK/PP_3195/PP_3195-deep-research-openscientist.md

## Source Context YAML

```yaml
term:
  id: GO:0008236
  label: serine-type peptidase activity
evidence_type: IEA
original_reference_id: GO_REF:0000002
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

# AIGR Gene Hypothesis Deep Research — PP_3195 (Q88I07): Serine-Type Peptidase Activity (GO:0008236)

**Organism:** *Pseudomonas putida* KT2440 (NCBITaxon:160488) · **Gene:** PP_3195 · **UniProt:** Q88I07
**Focus type:** function_assignment · **Hypothesis slug:** function-hypothesis-go-0008236
**Seed hypothesis:** PP_3195 has serine-type peptidase activity (GO:0008236) · **Evidence type (original):** IEA · **Original reference:** GO_REF:0000002

---

## Summary

The seed hypothesis — that PP_3195 (Q88I07) **has serine-type peptidase activity (GO:0008236)** — is **over-annotated and effectively refuted as a specific molecular function**. PP_3195 is, with high confidence, a **serine α/β-hydrolase** carrying an intact and correctly ordered Ser268–Asp358–His405 catalytic triad. That "serine hydrolase" layer of the annotation is defensible. But the specific claim that this triad hydrolyzes **peptide** bonds, together with the coupled proteolysis term (GO:0006508), rests entirely on a single non-specific InterPro-to-GO mapping — IPR001375 / Pfam PF00326 ("Prolyl oligopeptidase family") — propagated under GO_REF:0000002 as an IEA. That domain signature is shared by both serine peptidases *and* serine esterases, so the peptidase mapping is an annotation-propagation (frequency-bias) artifact rather than a specific prediction.

Three independent, mutually reinforcing lines of evidence point away from a peptidase and toward an **ester / C–C (ketone) hydrolase** identity. First, PP_3195 is **FdeB**, the predicted hydrolase of a **naringenin (flavonoid) catabolism** gene cluster (KEGG ortholog **K26184**, pathway ppu00946); its proposed KEGG reaction (R13077) is hydrolytic ring-opening of a **δ-lactone** — a cyclic ester — not peptide-bond cleavage. Second, at 420 aa with only a ~160-aa helical N-terminus, PP_3195 is **far too small** to contain the ~250–300-aa seven-bladed β-propeller that is a defining, substrate-gating feature of bona fide S9-family peptidases. Third, **all 25** experimentally characterized, EC-assigned reviewed members of PP_3195's actual InterPro family (**IPR050261**, "FrsA/Cutinase/Hydrolase-like") are ester or C–C/ketone hydrolases — **zero** are peptidases.

The most important caveat is that **FdeB itself has never been directly assayed**. The flanking *fde*-cluster enzymes (FdeE/FdeC/FdeG) were experimentally characterized, but FdeB's hydrolase activity is predicted, KEGG labels its reaction "unclear," and UniProt protein existence is **4 (Predicted)**. The recommended curation action is therefore to **remove or generalize the peptidase term** — not to swap in an equally strong but equally unproven specific peptidase alternative — and to favor a non-committal serine-hydrolase / carboxylic-ester-hydrolase molecular function alongside a flavonoid-catabolic-process term, all pending direct enzymatic verification.

---

## Executive Judgment

**Verdict: Over-annotated / effectively refuted as a specific molecular function.**

GO:0008236 (serine-type peptidase activity) and its coupled GO:0006508 (proteolysis) should not be retained as-is. They derive solely from a broad catalytic-domain signature whose name ("Prolyl oligopeptidase family") biases automated mappings toward peptidase, even though the clan contains many esterases. Every discriminating filter available — structural architecture, ortholog/pathway context, and family-wide enzymatic precedent — argues against peptidase activity and in favor of an ester/lactone (or activated C–C) hydrolase. The catalytic triad is real and high-confidence, but a triad alone cannot discriminate a peptidase from an esterase. The best-supported alternative identity (FdeB, flavonoid-degradation ester/lactone hydrolase) is a strong inference, not a demonstrated fact, because no member of this ortholog group has been directly assayed for PP_3195 and KEGG flags the reaction as "unclear."

---

## Key Findings

### Finding 1 — PP_3195 is a genuine serine α/β-hydrolase with an intact triad, but is structurally too small to be a classic S9 peptidase

UniProt Q88I07 describes a **420-amino-acid** protein annotated as a "Peptidase S9 prolyl oligopeptidase catalytic domain-containing protein," with **protein existence = 4 (Predicted)** — no experimental evidence of the protein or its function. The domain architecture is unambiguously that of the α/β-hydrolase superfamily: **Pfam PF00326** (Prolyl oligopeptidase family), **InterPro IPR001375** (Peptidase S9 catalytic domain) and **IPR029058** (Alpha/Beta hydrolase fold), with **CATH 3.40.50.1820** (α/β-hydrolase) plus **1.20.1440.110** (helical cap).

The canonical catalytic machinery is present and in the linear order expected for an α/β-hydrolase: **nucleophile Ser268** embedded in a GxSxG elbow motif (GLEG-**VSLGG**), **Asp358** (…VTHGEK**D**…), and **His405** (…INAG**H**YIAD…). The AlphaFold model **AF-Q88I07** is high quality: mean **pLDDT 91.6**, catalytic domain (residues 160–420) **pLDDT 97.1**, and the three triad residues at **pLDDT 96.7 / 95.4 / 97.7**. So the "serine hydrolase" layer of the annotation is structurally robust.

Crucially, however, the serine-type *peptidase* interpretation requires more than a triad. Bona fide S9-family serine peptidases have a **two-domain** architecture: the catalytic α/β-hydrolase domain **plus** a large N-terminal **seven-bladed β-propeller** (~250–300 aa) that regulates substrate access. As established for acylpeptide hydrolase (APH) from *Aeropyrum pernix* ([PMID: 15296741](https://pubmed.ncbi.nlm.nih.gov/15296741/)): "*The N-terminal domain is a regular seven-bladed beta-propeller, while the C-terminal domain has a canonical alpha/beta hydrolase fold and includes the active site and a conserved Ser445-Asp524-His556 catalytic triad.*" Prolyl oligopeptidase is ~710 aa, DPP-IV ~760 aa, and APH ~582 aa, each with this propeller. PP_3195, at **420 aa total** with a merely **~160-aa helical (not β-propeller) N-terminus**, cannot accommodate this feature. The structural size argument alone makes a classic S9 peptidase assignment implausible.

### Finding 2 — A competing, better-matched esterase annotation already exists; the peptidase IEA comes from a non-specific domain mapping

QuickGO for Q88I07 shows **three** IEA molecular-function/process annotations that are in direct tension:

1. **GO:0008236** serine-type peptidase activity — IEA/ECO:0000256, **GO_REF:0000002**, derived from InterPro **IPR001375** (the seed hypothesis);
2. **GO:0006508** proteolysis — same source (the BP partner of the peptidase call);
3. **GO:0052689** carboxylic ester hydrolase activity — IEA/ECO:0000256, **GO_REF:0000117**, from ARBA00028109.

InterPro places the protein in **FAMILY IPR050261 "FrsA/Cutinase/Hydrolase-like"** and PANTHER family **PTHR22946 "FrsA esterase."** The key problem is that **IPR001375 / PF00326 ("Prolyl oligopeptidase family")** is a **broad catalytic-domain signature shared by both serine peptidases and serine esterases**. The InterPro2GO rule that maps this domain to "serine-type peptidase activity" is therefore **non-specific** — it reflects the historical naming of the Pfam clan after prolyl oligopeptidase, not a specific prediction that any given member hydrolyzes peptides. In other words, GO:0008236 here is an artifact of domain-level annotation propagation, while the co-existing esterase term (GO:0052689) is more consistent with the protein's actual family placement. No experimental characterization exists to break the tie directly (protein existence: Predicted), but the weight of the family evidence favors the ester-hydrolase reading.

### Finding 3 — PP_3195 is FdeB, a flavonoid-degradation hydrolase whose proposed reaction is lactone (ester) hydrolysis, not peptide hydrolysis

KEGG assigns PP_3195 to **KO K26184** (symbol **fdeB**, "naringenin degradation protein FdeB"), pathway **ppu00946 "Degradation of flavonoids,"** orthology group **COG1506**. The reaction linked to this KO, **KEGG R13077**, is:

```
5-(4-Hydroxyphenyl)-3-oxovalero-δ-lactone  +  H2O
        ⇌  5-Hydroxy-5-(4-hydroxyphenyl)-3-oxopentanoate
        (KEGG COMMENT: "hydrolase; unclear reaction")
```

This is **hydrolytic ring-opening of a δ-lactone — a cyclic ester** — not cleavage of a peptide bond. The *fde* naringenin-degradation gene cluster was originally defined in *Herbaspirillum seropedicae* SmR1 ([PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/)), which characterized the FdeE monooxygenase, FdeC dioxygenase, and FdeG cyclase; **FdeB is the cluster's predicted hydrolase**, and K26184 orthologs span PP_3195 plus dozens of *Pseudomonas*, *Burkholderia*, and *Herbaspirillum* genomes. From that paper: "*a random mutant library of Herbaspirillum seropedicae SmR1 was constructed by Tn5 insertion and a mutant incapable of utilizing naringenin as a carbon source was isolated.*" In *P. putida* KT2440 the genomic neighborhood of PP_3195 is consistent with aromatic/flavonoid ring catabolism rather than proteolysis: **PP_3197** (glyoxalase/dioxygenase family), **PP_3198** (2Fe-2S ferredoxin), and **PP_3199** (putative monooxygenase). The physiological context therefore grounds PP_3195 in **flavonoid degradation**, not protein turnover.

**Caveat:** FdeB was **not** directly assayed in [PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/) (the biochemistry centered on FdeE/FdeC/FdeG), KEGG explicitly labels R13077 an "unclear reaction," and protein existence remains Predicted. The reaction direction and exact substrate specificity of FdeB thus remain to be demonstrated.

### Finding 4 — Every experimentally characterized member of PP_3195's InterPro family (IPR050261) is an esterase or C–C/ketone hydrolase; none is a peptidase

A UniProtKB query for `reviewed:true AND xref:interpro-IPR050261` (the "FrsA/Cutinase/Hydrolase-like" family to which Q88I07 belongs) returned **25 reviewed, EC-assigned members**. **All 25** are ester- or carbon–carbon-bond hydrolases; **none** is a peptidase:

| Sub-class | EC | Representative members |
|---|---|---|
| Cutinases | 3.1.1.74 | Q47RJ6, G9BY57 (leaf-branch compost cutinase), P0DX29 |
| PET hydrolase | 3.1.1.101 | A0A0K8P6T7 |
| FrsA carboxylesterases | 3.1.1.1 | P04335 (*E. coli*), Q8DF91 (*V. vulnificus*), A1JNX9 (*Y. enterocolitica*) |
| Esterase YjfP | 3.1.-.- | P39298 |
| BHET hydrolase | 3.1.1.- | Q9L2J6 |
| C–C bond hydrolases (ketonic/β-keto substrates) | 3.7.1.- / 3.7.1.19 | Q93NG6 (2,6-dihydropseudooxynicotine hydrolase), Q4WZB3 & G2X3G9 (heptaketide hydrolases AYG1), poxO/psoB/acrC/FUS2/xenA polyketide hydrolases |

**Count: 25/25 ester or C–C hydrolases; 0/25 peptidases.** Notably, the **EC 3.7.1.-** sub-class ("hydrolases acting on C–C bonds in ketonic substances") is a direct mechanistic match to FdeB's proposed KEGG reaction R13077 — hydrolytic ring-opening of a **β-keto δ-lactone** flavonoid intermediate. This family-wide precedent is the single strongest argument against the peptidase hypothesis: the serine triad in this clan is consistently deployed on ester and activated-carbonyl C–C bonds, never on peptide bonds.

---

## Mechanistic Model / Interpretation

The evidence converges on a coherent picture in which PP_3195 is a **serine hydrolase that opens an ester/lactone (or an activated C–C bond) during flavonoid catabolism**, and the "serine-type peptidase" label is an upstream domain-propagation artifact.

```
                         PP_3195 / Q88I07 (FdeB, 420 aa)
                         ┌─────────────────────────────────────────┐
  N-term ~160 aa helical │   α/β-hydrolase catalytic domain (160–420)│ C-term
  (CATH 1.20.1440.110)   │   Ser268 ··· Asp358 ··· His405 triad      │
  NOT a β-propeller →     └─────────────────────────────────────────┘
  cannot gate peptides             pLDDT 96–98 (high confidence)

   Serine triad chemistry is REAL ─┬─> on a PEPTIDE bond?  ✗  (no propeller, no family precedent, no assay)
                                   └─> on an ESTER / β-keto C–C bond?  ✓  (family precedent, KEGG R13077, cluster context)

   Physiological context:  Naringenin (flavonoid) ──FdeE/FdeC/FdeG──> β-keto δ-lactone intermediate
                                                                           │  + H2O
                                                            FdeB (PP_3195) │  (R13077, ester/lactone hydrolysis)
                                                                           ▼
                                                   5-OH-5-(4-OH-phenyl)-3-oxopentanoate → ring catabolism
```

**Why the peptidase annotation arose.** PF00326/IPR001375 is historically named "Prolyl oligopeptidase family," but it is a catalytic-domain clan spanning serine peptidases and serine esterases. An automated InterPro2GO rule mapped the domain to GO:0008236, and GO_REF:0000002 propagated it as IEA. Because many well-studied members of the broader clan are peptidases (frequency/annotation bias), the peptidase term rode along even though PP_3195's *specific* family (IPR050261) and *specific* ortholog (K26184/FdeB) are esterase / C–C-hydrolase.

**Three orthogonal filters all fail the peptidase call:**

| Filter | Peptidase expectation | PP_3195 observation | Verdict |
|---|---|---|---|
| Structural architecture | 7-bladed β-propeller + catalytic domain (~580–760 aa) | 420 aa, ~160-aa helical N-term only | Fails |
| Ortholog / pathway (KEGG) | protein turnover context | K26184 FdeB, flavonoid catabolism, R13077 lactone hydrolysis | Fails |
| Family precedent (IPR050261) | ≥ some characterized peptidases | 25/25 ester/C–C hydrolases, 0 peptidases | Fails |

The result is a strong, converging inference that the molecular function is a **carboxylic-ester / C–C(ketone) hydrolase**, not a serine peptidase — tempered by the fact that FdeB has never been assayed directly.

---

## Evidence Base

| Citation / Source | Evidence type | Supports/Refutes/Qualifies/Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt Q88I07 | review/database | Qualifies | Identity / evidence level | "Peptidase S9 prolyl oligopeptidase catalytic domain-containing protein", 420 aa, existence = Predicted (4) | *P. putida* KT2440 | High for content; no experimental data |
| IPR001375 / PF00326 / COG1506 → GO:0008236 (GO_REF:0000002) | computational (InterPro2GO) | Supports (weak) | Serine-type peptidase activity | Basis of seed IEA; domain shared by peptidases **and** esterases | Sequence | Non-specific; over-annotation-prone |
| Catalytic-triad analysis | structural/evolutionary (computed) | Supports hydrolase (not specifically peptidase) | Active serine hydrolase | Ser268 (GxSxG), Asp358, His405 in canonical order | AlphaFold AF-Q88I07, pLDDT 95–98 | Triad common to peptidases & esterases |
| AlphaFold AF-Q88I07 | structural (computed) | Refutes classic S9 peptidase | β-propeller present? | Single α/β-hydrolase + ~160-aa helical N-cap; **no** 7-bladed β-propeller | Model, mean pLDDT 91.6 | Model, not experimental structure |
| IPR050261; PANTHER PTHR22946; GO:0052689 (GO_REF:0000117) | computational (family) | Competing | Esterase vs peptidase | Family-level call is **esterase** (FrsA/cutinase/carboxylic ester hydrolase) | Sequence | Also IEA; unverified |
| KEGG K26184 / PP_3195 + REACTION R13077 | review/database (pathway) | **Refutes peptidase / Competing** | Substrate class | FdeB = flavonoid (naringenin) degradation **hydrolase**; proposed chemistry is **δ-lactone (ester) hydrolysis** | KEGG ppu00946 | "unclear reaction"; FdeB not directly assayed |
| [PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/) | mutant phenotype (primary) | Supports flavonoid-catabolism role of *fde* cluster | Pathway context | Tn5 mutant unable to use naringenin as carbon source; defines *fde* cluster (FdeE/FdeC/FdeG characterized) | *H. seropedicae* SmR1 | FdeB itself not individually assayed |
| KEGG neighborhood PP_3196–3199 | computational (synteny) | Supports flavonoid/aromatic catabolism | Operon context | Monooxygenase + ferredoxin + glyoxalase/dioxygenase cluster around PP_3195 | *P. putida* KT2440 | Annotation-based |
| [PMID: 15296741](https://pubmed.ncbi.nlm.nih.gov/15296741/) | structural (primary) | Qualifies/Refutes | S9 peptidases need β-propeller | APH: N-terminal 7-bladed β-propeller + C-terminal α/β-hydrolase, Ser445-Asp524-His556 | *A. pernix* | Architecture absent in PP_3195 |
| [PMID: 11772620](https://pubmed.ncbi.nlm.nih.gov/11772620/) | mutant/metabolic (primary) | Supports flavonoid-catabolism context | *P. putida* flavonoid degradation includes a hydrolysis step | Naringenin/quercetin catabolism includes "hydrolysis and cleavage of the C-ring" | *P. putida* PML2 | Different strain/route; FdeB not named |
| [PMID: 24085580](https://pubmed.ncbi.nlm.nih.gov/24085580/) | biochemical (primary) | Supports context | *P. putida* acts on flavonoids (quercetin→naringenin) | QuoA converts quercetin to naringenin | *P. putida* | Orientation only |
| [PMID: 8071218](https://pubmed.ncbi.nlm.nih.gov/8071218/) | biochemical pathway (primary) | Supports context | Bacterial flavonoid C-ring fission chemistry | *P. putida* degrades quercetin via A-ring fission | Rhizobia / *P. putida* | Orientation only |
| UniProt IPR050261 reviewed members | structural/evolutionary (computed homology) | **Refutes peptidase** | Nearest characterized homologs' function | **25/25 reviewed members are ester (EC 3.1.1.x) or C–C/ketone (EC 3.7.1.x) hydrolases; 0/25 peptidases** | Multi-organism SwissProt | Homology inference |

---

## GO Curation Implications

**Leads requiring curator verification** (treat the blinded prior review action as unknown):

1. **GO:0008236 (serine-type peptidase activity, MF) — REMOVE or GENERALIZE.** The term rests solely on a non-specific IPR001375→GO mapping (GO_REF:0000002, IEA). No structural, orthology, pathway, or family-level evidence supports peptidase activity; three independent filters argue against it. Recommended: remove the peptidase term, or at most generalize to the non-committal parent **GO:0016787 (hydrolase activity)** / **GO:0017171 (serine hydrolase activity)** if a serine-triad statement is desired.
2. **GO:0006508 (proteolysis, BP) — REMOVE.** This is the biological-process partner of the refuted peptidase call and shares its single weak source. It should fall with GO:0008236.
3. **GO:0052689 (carboxylic ester hydrolase activity, MF) — RETAIN / FAVOR** as the more defensible molecular-function annotation (already present via GO_REF:0000117). It is consistent with the IPR050261 family and the FdeB lactone-hydrolysis reaction. Consider, as a lead, a more specific child reflecting **EC 3.7.1.-** (hydrolase acting on C–C bonds in ketonic substances) if curators accept the KEGG R13077 assignment — but flag that R13077 is "unclear."
4. **Biological process — ADD as lead:** a **flavonoid catabolic process** term (consistent with ppu00946 and the *fde* cluster), e.g., **GO:0009812 (flavonoid metabolic process)** or a catabolic child, with evidence code reflecting ortholog-based inference (K26184/FdeB) and a note that direct assay is lacking.

**Evidence-code note:** Because FdeB has not been experimentally characterized, all retained/added terms should remain **IEA/ISS-level** (sequence/orthology-based), not experimental. The curation should explicitly flag "Predicted" protein existence.

**Bottom line for MF/BP/CC:** The supported MF is an **ester / C–C(ketone) hydrolase** (not peptidase); the supported BP is **flavonoid catabolism** (not proteolysis); no specific CC term is implicated. Avoid defaulting to "protein binding."

**GO decision table:**

| Term | Aspect | Current | Proposed action | Rationale |
|---|---|---|---|---|
| GO:0008236 serine-type peptidase activity | MF | IEA (GO_REF:0000002) | **Remove** (or generalize to GO:0017171 serine hydrolase activity) | Non-specific domain mapping; fails structural, ortholog, and family filters |
| GO:0006508 proteolysis | BP | IEA (GO_REF:0000002) | **Remove** | BP partner of refuted peptidase call |
| GO:0052689 carboxylic ester hydrolase activity | MF | IEA (GO_REF:0000117) | **Retain / favor** | Matches IPR050261 family and FdeB lactone hydrolysis |
| GO:0009812 flavonoid metabolic process (or catabolic child) | BP | — | **Add as lead** (ISS/IEA via K26184/FdeB) | KEGG ppu00946 + *fde* cluster context |
| EC 3.7.1.- / C–C(ketone) hydrolase child | MF | — | **Consider** (flag "unclear reaction") | Direct match to R13077; provisional |

---

## Mechanistic Scope

- **Immediate molecular function under test:** hydrolytic cleavage by a Ser–His–Asp catalytic triad. The triad chemistry is real and high-confidence; the open question is the **bond type** — peptide (seed hypothesis) vs. ester/lactone or activated C–C (competing, better-supported).
- **Direct gene-product activity (predicted, not assayed):** hydrolytic ring-opening of a β-keto δ-lactone flavonoid intermediate (KEGG R13077), i.e., ester/lactone hydrolase activity.
- **Downstream / pathway consequence (not the molecular function):** utilization of naringenin as a carbon source; funneling of flavonoid ring carbon toward protocatechuate and central metabolism. The *H. seropedicae* Tn5 growth phenotype ([PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/)) is a **pathway-level loss-of-function** readout for the cluster, not a direct demonstration of FdeB's bond specificity.
- **What is NOT in scope:** any protein-turnover / proteolytic role. No evidence places PP_3195 in protein degradation, signaling peptidase cascades, or peptide processing.

---

## Conflicts and Alternatives

- **Database carry-over / annotation propagation (primary conflict):** GO:0008236 and GO:0006508 originate from the broad PF00326/IPR001375 "prolyl oligopeptidase family" signature, whose name biases automated mappings toward peptidase even though the clan includes many esterases. This is the classic frequency-bias / paralog-overannotation failure mode.
- **Competing in-database annotation:** GO:0052689 (carboxylic ester hydrolase) already co-exists and better matches the IPR050261 family — a direct intra-record conflict favoring the esterase reading.
- **Architecture:** true S9 peptidases are two-domain (β-propeller + hydrolase); PP_3195 lacks the propeller.
- **"Unclear reaction" caveat:** KEGG R13077 is explicitly uncertain; the exact substrate, product, and directionality of FdeB are not experimentally fixed. The esterase/lactonase assignment, while better supported than peptidase, is itself provisional.
- **Ortholog-vs-assay gap:** The *fde* cluster's catalytic steps were demonstrated for FdeE/FdeC/FdeG, not FdeB. It is conceivable (though unsupported) that FdeB plays a non-hydrolytic or accessory role; the hydrolase assignment is by homology and cluster logic.
- **Organism/route differences:** The *H. seropedicae* meta-pathway (PMID 27059806) differs from the *P. putida* PML2 route (PMID 11772620); neither directly assays PP_3195.

---

## Limitations and Knowledge Gaps

All analyses are sequence-, structure-, pathway-, and literature-derived (UniProt, InterPro, QuickGO, KEGG, AlphaFold model, primary pathway literature). No wet-lab data exist for PP_3195 specifically; FdeB enzymology is inferred (KEGG "unclear reaction"); and explicit BLAST/MEROPS/ESTHER homology placement was not executed programmatically in this run.

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| FdeB has never been enzymatically assayed | UniProt (PE=4 Predicted), KEGG (R13077 "unclear"), PMID 27059806 (FdeB not assayed) | Determines whether any specific MF term (esterase vs C–C hydrolase) is experimentally warranted | Purify PP_3195/FdeB; test lactone/ester hydrolysis vs. peptide/ester panels |
| Exact substrate & reaction direction of R13077 | KEGG reaction record | Decides between GO:0052689 (ester hydrolase) and an EC 3.7.1.- C–C hydrolase child | LC-MS product identification from in vitro reaction |
| No experimental 3D structure | AlphaFold model only (high pLDDT) | Confirms absence of β-propeller and active-site geometry definitively | X-ray/cryo-EM structure; S268A active-site mutagenesis |
| Phenotype of *P. putida* KT2440 PP_3195 knockout on naringenin | Not available | Would directly tie PP_3195 to flavonoid catabolism in the target organism | Clean deletion + growth assay on naringenin as sole carbon source |
| Nearest experimentally characterized homolog | No BLAST/MEROPS/ESTHER run here | Needed to transfer a precise EC/term | phmmer/BLAST vs SwissProt; MEROPS clan SC; ESTHER |

---

## Discriminating Tests

1. **Direct enzymology (most decisive):** Express and purify PP_3195/FdeB; run a substrate panel contrasting (a) the proposed β-keto δ-lactone flavonoid intermediate, (b) generic ester substrates (e.g., p-nitrophenyl acetate/butyrate), and (c) peptide/amide substrates (e.g., Z-Gly-Pro-AMC, N-acetyl-Ala/Met-pNA, dipeptidyl-AMC, including proline-containing peptides for a prolyl-oligopeptidase control). Ester/lactone-only activity refutes GO:0008236.
2. **Active-site mutagenesis:** Ser268Ala should abolish activity, confirming the triad is catalytic and identifying the nucleophile actually used.
3. **In vivo genetics in the target organism:** Construct a markerless PP_3195 deletion in *P. putida* KT2440 and assay growth on naringenin/quercetin vs. glycerol control (mirroring the flavonoid-auxotrophy screens of [PMID: 11772620](https://pubmed.ncbi.nlm.nih.gov/11772620/) and [PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/)). Loss of growth on flavonoids but not glycerol supports the catabolic role.
4. **Metabolite profiling:** LC-MS/NMR of wild-type vs. mutant supernatants to detect accumulation of the predicted δ-lactone intermediate upstream of FdeB.
5. **Comparative/structural confirmation:** BLAST/phmmer vs SwissProt + MEROPS + ESTHER; superpose the AlphaFold model onto an S9 peptidase vs an FrsA/cutinase/lactonase to compare oxyanion hole and substrate pocket, reinforcing the "too small for S9 peptidase" argument.

---

## Proposed Follow-up Experiments / Actions

1. **Curation:** Enter leads to remove GO:0008236 and GO:0006508, retain/favor GO:0052689, and add a flavonoid-catabolic-process term — all at IEA/ISS confidence with a "Predicted protein; FdeB unassayed" note.
2. **Enzymology:** Recombinant PP_3195 substrate panel (lactone/ester vs. peptide) + Ser268Ala control.
3. **Genetics:** PP_3195 deletion in *P. putida* KT2440; naringenin vs. glycerol growth.
4. **Metabolomics:** LC-MS of mutant vs. WT for the predicted δ-lactone intermediate.
5. **Structure/homology:** Experimental structure or documented superposition vs. prolyl oligopeptidase to formally confirm the absent β-propeller; run MEROPS/ESTHER placement.

---

## Curation Leads (require curator verification)

**Candidate action change:** retire/generalize **GO:0008236** → **GO:0017171 (serine hydrolase activity)**; flag **GO:0052689 (carboxylic ester hydrolase)** / a lactonase term as the better-supported MF; **remove GO:0006508 (proteolysis)**; **add a flavonoid catabolic process BP** term (lead).

**Candidate references with exact snippets to verify:**

- [PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/) — "*a random mutant library of Herbaspirillum seropedicae SmR1 was constructed by Tn5 insertion and a mutant incapable of utilizing naringenin as a carbon source was isolated*" (defines the *fde* naringenin-degradation cluster containing FdeB = PP_3195 ortholog).
- [PMID: 11772620](https://pubmed.ncbi.nlm.nih.gov/11772620/) — "*The first step in the pathway involves 3,3'-didehydroxylation, followed by hydrolysis and cleavage of the C-ring*" (*P. putida* flavonoid catabolism includes a hydrolytic step).
- [PMID: 15296741](https://pubmed.ncbi.nlm.nih.gov/15296741/) — "*The N-terminal domain is a regular seven-bladed beta-propeller, while the C-terminal domain has a canonical alpha/beta hydrolase fold ... Ser445-Asp524-His556 catalytic triad*" (S9 peptidases need a β-propeller PP_3195 lacks).
- KEGG **K26184 / R13077** — FdeB = naringenin-degradation hydrolase; reaction is δ-lactone hydrolysis (database-level).

**Suggested curator questions:** (i) Should the peptidase IEA be demoted given KEGG FdeB and the FrsA esterase family? (ii) Is there MEROPS/ESTHER placement for Q88I07? (iii) Does the AlphaFold active-site pocket resemble a peptidase or an esterase?

**Suggested experiments:** recombinant esterase/lactonase vs peptidase substrate panel; ΔPP_3195 naringenin growth + metabolomics; S268A control.

---

*Prepared from 3 completed investigation iterations: 4 confirmed findings, 6 papers reviewed. All computational results (UniProt, QuickGO, KEGG, AlphaFold, InterPro/UniProtKB family survey) are reported as database/prediction-level evidence and are explicitly distinguished from experimental data, of which none exists for this gene product. Conclusions about peptidase vs. esterase/lactonase are inferential but convergent, not experimentally demonstrated for this protein.*


## Artifacts

- [OpenScientist PP 3195 GO decision table](openscientist_artifacts/PP_3195_GO_decision_table.csv)
- [OpenScientist PP 3195 family homolog EC](openscientist_artifacts/PP_3195_family_homolog_EC.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)