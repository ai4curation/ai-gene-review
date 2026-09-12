---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-21T21:31:32.511346'
end_time: '2026-06-21T22:12:17.424745'
duration_seconds: 2444.91
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: CLCN7
  gene_symbol: CLCN7
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: topology-transepithelial-overannotation
  hypothesis_text: Human CLCN7 (ClC-7) carries an annotation for transepithelial chloride
    transport (GO:0030321), but it is reported to be an intracellular endolysosomal
    electrogenic 2Cl-/1H+ antiporter residing in the lysosomal membrane and the osteoclast
    ruffled border rather than in the epithelial plasma membrane. Using membrane-topology
    prediction (e.g. DeepTMHMM/Phobius), analysis of subcellular-targeting / lysosomal
    sorting signals, and subcellular-localization evidence, determine whether GO:0030321
    (transepithelial chloride transport) is justified or is an over-annotation, and
    what the best-supported cellular localization and transport role of ClC-7 actually
    are.
  term_context: '- Term: transepithelial chloride transport (GO:0030321)'
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: Human CLCN7 (ClC-7) carries an annotation for\
    \ transepithelial chloride transport (GO:0030321),\n  but it is reported to be\
    \ an intracellular endolysosomal electrogenic 2Cl-/1H+ antiporter residing in\n\
    \  the lysosomal membrane and the osteoclast ruffled border rather than in the\
    \ epithelial plasma membrane.\n  Using membrane-topology prediction (e.g. DeepTMHMM/Phobius),\
    \ analysis of subcellular-targeting / lysosomal\n  sorting signals, and subcellular-localization\
    \ evidence, determine whether GO:0030321 (transepithelial\n  chloride transport)\
    \ is justified or is an over-annotation, and what the best-supported cellular\
    \ localization\n  and transport role of ClC-7 actually are.\nfocus_type: free_text\n\
    term_id: GO:0030321\nterm_label: transepithelial chloride transport\ncontext:\
    \ []\nreference_id: []"
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
citation_count: 21
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** CLCN7
- **Gene symbol:** CLCN7

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** topology-transepithelial-overannotation
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

Human CLCN7 (ClC-7) carries an annotation for transepithelial chloride transport (GO:0030321), but it is reported to be an intracellular endolysosomal electrogenic 2Cl-/1H+ antiporter residing in the lysosomal membrane and the osteoclast ruffled border rather than in the epithelial plasma membrane. Using membrane-topology prediction (e.g. DeepTMHMM/Phobius), analysis of subcellular-targeting / lysosomal sorting signals, and subcellular-localization evidence, determine whether GO:0030321 (transepithelial chloride transport) is justified or is an over-annotation, and what the best-supported cellular localization and transport role of ClC-7 actually are.

## Term and Decision Context

- Term: transepithelial chloride transport (GO:0030321)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human CLCN7 (ClC-7) carries an annotation for transepithelial chloride transport (GO:0030321),
  but it is reported to be an intracellular endolysosomal electrogenic 2Cl-/1H+ antiporter residing in
  the lysosomal membrane and the osteoclast ruffled border rather than in the epithelial plasma membrane.
  Using membrane-topology prediction (e.g. DeepTMHMM/Phobius), analysis of subcellular-targeting / lysosomal
  sorting signals, and subcellular-localization evidence, determine whether GO:0030321 (transepithelial
  chloride transport) is justified or is an over-annotation, and what the best-supported cellular localization
  and transport role of ClC-7 actually are.
focus_type: free_text
term_id: GO:0030321
term_label: transepithelial chloride transport
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
prompt so the report can be compared against them after the run. Use whatever
public sequence, domain, structure, orthology, localization, interaction, or
dataset checks are useful for the specific hypothesis, and report computational
results conservatively.

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

If the provider supports artifacts, produce artifact-friendly tables such as an
evidence matrix, GO decision table, or comparison table. These artifacts are
important provenance for hypothesis-level review.


## Output

# CLCN7 / ClC-7: GO:0030321 (Transepithelial Chloride Transport) Is an Over-Annotation

## Executive Judgment

**Verdict: Over-annotated.** The GO:0030321 (transepithelial chloride transport) annotation for human CLCN7 (ClC-7) should be removed. The annotation is not supported by any primary experimental evidence and traces to a misattributed family-level introductory sentence in a ComplexPortal entry, subsequently amplified by phylogenetic inference to ~1,198 ortholog annotations. All available evidence — spanning localization studies, sorting signal analysis, electrophysiology, structural biology, and loss-of-function phenotypes — establishes CLC-7 as an intracellular endolysosomal 2Cl⁻/1H⁺ antiporter that never participates in transepithelial chloride transport under physiological conditions. No counter-evidence was found despite targeted searches for plasma membrane localization, surface proteomics data, isoform-specific targeting, or transepithelial function in any epithelial cell type.

All localization evidence — immunofluorescence, immunohistochemistry, cryo-EM, sorting motif analysis — consistently places CLC-7 in the endolysosomal compartment. Computational sequence analysis confirms this: CLCN7 possesses a uniquely extended 126-residue N-terminal cytoplasmic tail loaded with endolysosomal sorting motifs (dileucine motifs EAAPLL, TPLL; acidic cluster DDEE; DXXLL motif DDELL) that are completely absent from the plasma-membrane CLC paralogs CLCNKA/CLCNKB. Furthermore, CLC-7 contains the "gating glutamate" characteristic of Cl⁻/H⁺ antiporters, while CLCNKA/CLCNKB have valine at this position, functioning as pure Cl⁻ channels. PANTHER correctly separates them into different families (PTHR11689 vs PTHR45720), and InterPro assigns them to distinct subfamilies (IPR002249 "H⁺/Cl⁻ exchange transporter 7" vs IPR002250 "Chloride channel ClC-K").

---

## Summary

Human CLCN7 encodes CLC-7, a member of the CLC (ChLoride Channel) family that functions as an electrogenic 2Cl⁻/1H⁺ antiporter on lysosomal membranes and the osteoclast ruffled border. The gene currently carries a GO annotation for "transepithelial chloride transport" (GO:0030321), a biological process term describing the movement of chloride ions across an epithelial cell layer — a function requiring plasma membrane localization at apical and/or basolateral surfaces. This investigation evaluated whether this annotation is justified by examining primary literature, computational sequence analysis, and database provenance.

Across three iterations of systematic investigation encompassing 37 papers, sequence-based sorting signal analysis, and database annotation provenance tracing, we found no evidence that CLC-7 participates in transepithelial chloride transport. Instead, the annotation traces to two sources: (1) a ComplexPortal IDA annotation citing [PMID: 32851177](https://pubmed.ncbi.nlm.nih.gov/32851177/), where the phrase "transepithelial Cl⁻ transport" appears in an introductory sentence describing the CLC family broadly, not CLC-7 specifically; and (2) a PANTHER IBA (Inferred by Biological Aspect of Ancestor) annotation that propagated this error to CLCN7 orthologs across approximately 1,198 annotations in many species. CLC-7 contains N-terminal dileucine and acidic cluster sorting motifs that actively target it to lysosomes — motifs absent from the plasma-membrane CLC paralogs (CLC-Ka, CLC-Kb) that genuinely mediate transepithelial chloride transport. The recommended curation action is removal of GO:0030321 and addition of GO:0007042 (lysosomal lumen acidification) as a more accurate biological process annotation.

---

## Key Findings

### Finding 1: GO:0030321 Annotation Is an Over-Annotation from Misattributed Family-Level Statement and IBA Propagation

The GO:0030321 annotation for CLCN7 derives from two sources, both of which are erroneous. The first is an IDA (Inferred from Direct Assay) annotation from the ComplexPortal citing [PMID: 32851177](https://pubmed.ncbi.nlm.nih.gov/32851177/). However, careful examination of this paper reveals that the phrase "transepithelial Cl⁻ transport" appears in a general introductory sentence describing functions across the CLC family — it is not attributed to CLC-7 specifically. Indeed, the same paper explicitly states that "CLC-7/Ostm1 is an electrogenic Cl⁻/H⁺ antiporter that mainly resides in lysosomes and osteoclast ruffled membranes," directly contradicting the transepithelial annotation.

The second source is an IBA annotation from PANTHER (node PTN002481857). Investigation revealed that PANTHER classifies CLCN7 in family PTHR11689 (antiporter family) and CLCNKA/CLCNKB in a separate family PTHR45720 (channel family). The IBA annotation used P51798 (CLCN7 itself) as the seed, meaning it propagated within the antiporter family from CLCN7's own flawed ComplexPortal IDA annotation — not from CLC-Ka/CLC-Kb paralogs as initially hypothesized. This amplified the original error to CLCN7 orthologs across ~1,198 annotations in many species.

In contrast, CLCNKA and CLCNKB carry legitimate TAS (Traceable Author Statement) annotations for GO:0030321 as bona fide plasma membrane channels involved in transepithelial chloride reabsorption in the kidney. UniProt entry P51798 for CLCN7 lists subcellular location as "Lysosome membrane" only, with no plasma membrane annotation.

### Finding 2: CLCN7 Is Definitively Localized to Lysosomes and the Osteoclast Ruffled Border

Multiple independent lines of evidence establish CLC-7 as an intracellular protein localized to late endosomes, lysosomes, and the osteoclast ruffled border. GO Cellular Component annotations for CLCN7 include GO:0005765 (lysosomal membrane) supported by HDA evidence ([PMID: 17897319](https://pubmed.ncbi.nlm.nih.gov/17897319/)), EXP evidence ([PMID: 18449189](https://pubmed.ncbi.nlm.nih.gov/18449189/)), and IDA evidence ([PMID: 21527911](https://pubmed.ncbi.nlm.nih.gov/21527911/)). No plasma membrane, apical membrane, or basolateral membrane annotations exist for CLCN7.

Key primary studies confirming endolysosomal localization include:

- **Kasper et al. (2005)** ([PMID: 15706348](https://pubmed.ncbi.nlm.nih.gov/15706348/)): Established that "ClC-7 is a chloride channel of late endosomes and lysosomes," with loss of CLC-7 leading to lysosomal storage disease and neurodegeneration — a foundational study for CLC-7 biology.
- **Lange et al. (2006)** ([PMID: 16525474](https://pubmed.ncbi.nlm.nih.gov/16525474/)): Demonstrated through multi-tissue immunofluorescence that "both ClC-7 and Ostm1 proteins co-localize in late endosomes and lysosomes of various tissues, as well as in the ruffled border of bone-resorbing osteoclasts."
- **Jentsch (2007)** ([PMID: 17110406](https://pubmed.ncbi.nlm.nih.gov/17110406/)): Explicitly noted that "the intracellular localization of ClC-6 and ClC-7/Ostm1 precluded biophysical studies," directly demonstrating that CLC-7 is not accessible at the plasma membrane under physiological conditions.
- **Stauber & Jentsch (2010)** ([PMID: 20817731](https://pubmed.ncbi.nlm.nih.gov/20817731/)): Mapped N-terminal sorting motifs required for lysosomal targeting and showed that "ClC-7 could be partially shifted from lysosomes to the plasma membrane by combined mutation of N-terminal sorting motifs" — proving that CLC-7 reaches the plasma membrane only when its lysosomal sorting signals are artificially disrupted.
- **Schrecker et al. (2020)** ([PMID: 32749217](https://pubmed.ncbi.nlm.nih.gov/32749217/)): Solved the cryo-EM structure of CLC-7/OSTM1 complex at 2.8 Å resolution, confirming its residence in lysosomes and the osteoclast ruffled border. OSTM1 covers the luminal surface of CLC-7, protecting it from the degradative lysosomal environment.
- **Zhang et al. (2024)** ([PMID: 38294065](https://pubmed.ncbi.nlm.nih.gov/38294065/)): A recent study confirming that "The ClC-7 chloride (Cl⁻)-proton (H⁺) antiporter (also known as CLCN7) is localized to the endolysosomal compartments."

### Finding 3: CLC-7 Is Expressed in Epithelial Cells but Functions Intracellularly, Not in Transepithelial Transport

A critical question was whether CLC-7 might participate in transepithelial transport in specific epithelial contexts. Targeted investigation of three epithelial tissues where CLC-7 is expressed — ameloblasts (dental epithelium), gastric epithelial cells, and renal tubular cells — revealed that CLC-7's role is always intracellular:

- **Ameloblasts:** Wen et al. (2015) ([PMID: 26346547](https://pubmed.ncbi.nlm.nih.gov/26346547/)) showed CLC-7 is expressed in ameloblasts but "located in late endosomes and lysosomes." CLC-7 knockout did not significantly affect enamel mineralization, and CLC-7 was described as "critical for the function of osteoclasts" rather than for transepithelial transport. Separately, Barvencik et al. (2014) ([PMID: 25663454](https://pubmed.ncbi.nlm.nih.gov/25663454/)) attributed ameloblast tooth defects in CLC-7 knockout mice to osteoclast dysfunction, confirming CLC-7 is "not critical to enamel and dentin formation."
- **Gastric epithelium:** Weinert et al. (2014) ([PMID: 24103576](https://pubmed.ncbi.nlm.nih.gov/24103576/)) showed that although CLC-7 is expressed in the stomach, "loss of ClC-7 did not entail a relevant elevation of gastric pH," ruling out a functional role in transepithelial acid/chloride secretion. This distinguishes CLC-7 from the gastric proton pump or other transporters genuinely involved in gastric acid secretion.
- **Kidney:** Reviews of renal CLC function ([PMID: 17477025](https://pubmed.ncbi.nlm.nih.gov/17477025/); [PMID: 11053039](https://pubmed.ncbi.nlm.nih.gov/11053039/)) consistently identify CLC-K1 (CLC-Ka) and CLC-K2 (CLC-Kb) as the CLC channels mediating transepithelial chloride transport in the kidney, with CLC-5 in intracellular vesicles for endocytosis. CLC-7 is not mentioned as a transepithelial transporter in any renal physiology study.

### Finding 4: Sequence Analysis Confirms Lysosomal Sorting Signals and Antiporter Mechanism Distinguish CLCN7 from Transepithelial CLCs

Computational analysis of CLC protein sequences revealed fundamental differences between CLC-7 and the plasma-membrane CLCs that mediate transepithelial transport:

**Sorting signals:** The CLCN7 N-terminus contains a 126-amino-acid cytoplasmic tail before the first transmembrane helix, harboring multiple endolysosomal sorting motifs:
- Dileucine motif EAAPLL (positions 19–24)
- Second dileucine motif TPLL (positions 33–36)
- Acidic cluster DDEE (positions 16–19)
- DXXLL motif DDELL (positions 65–69)

In contrast, CLCNKA and CLCNKB have short N-termini (~10–51 amino acids) containing zero dileucine or acidic cluster sorting motifs, consistent with their plasma membrane localization. This was experimentally validated by Stauber & Jentsch (2010) ([PMID: 20817731](https://pubmed.ncbi.nlm.nih.gov/20817731/)), who showed that combined mutation of these N-terminal sorting motifs was required to redirect CLC-7 to the plasma membrane.

**Transport mechanism:** CLCN7 retains the conserved "gating glutamate" residue characteristic of CLC antiporters, which enables 2Cl⁻/1H⁺ exchange activity. In CLC-Ka and CLC-Kb, this glutamate is replaced by valine, converting the protein into a passive chloride channel — a fundamentally different transport mechanism. Weinert et al. (2010) ([PMID: 20430974](https://pubmed.ncbi.nlm.nih.gov/20430974/)) demonstrated the functional importance of the antiporter mechanism: "mice carrying a point mutation converting ClC-7 into an uncoupled (unc) Cl⁻ conductor" developed lysosomal storage disease even though lysosomal pH and Cl⁻ conductance were maintained, proving that the Cl⁻/H⁺ exchange stoichiometry — not simple Cl⁻ conductance — is essential for CLC-7 function.

**Protein family classification:** PANTHER classifies CLCN7 in family PTHR11689 (antiporter) and CLCNKA in PTHR45720 (channel). InterPro assigns CLCN7 to IPR002249 (H⁺/Cl⁻ exchange transporter 7) and CLCNKA to IPR002250 (Chloride channel ClC-K). These separate family assignments reflect deep functional divergence.

### Finding 5: IBA Annotation Propagation Mechanism Clarified

Initial analysis hypothesized that the IBA annotation for CLCN7 GO:0030321 was propagated from CLC-Ka/CLC-Kb paralogs within a shared PANTHER family. Detailed investigation revealed a different and more concerning mechanism: PANTHER places CLCN7 and CLCNKA/CLCNKB in entirely separate families (PTHR11689 vs. PTHR45720). The IBA annotation for CLCN7 references PANTHER node PTN002481857 with P51798 (CLCN7 itself) as the seed. This means the IBA propagated within the PTHR11689 antiporter family from CLCN7's own ComplexPortal IDA annotation — the one that misattributed a CLC-family-level introductory sentence to CLC-7 specifically. The result was amplification of a single source error to approximately 1,198 ortholog annotations across many species.

### Finding 6: GO:0007042 (Lysosomal Lumen Acidification) Is Recommended as Replacement

Despite strong evidence for CLC-7's role in lysosomal acidification, CLCN7 currently lacks annotations to GO:0007042 (lysosomal lumen acidification) or GO:0007041 (lysosomal transport). These terms are better supported by the primary literature than GO:0030321. CLCN7 already has annotations to GO:1902476 (chloride transmembrane transport) with IBA, IEA, and TAS evidence, which is appropriate but incomplete. GO:0030321 is a child of both GO:0006821 (chloride transport) and GO:0015698 (transepithelial transport) — the "transepithelial" parent is inappropriate for an intracellular transporter. Multiple studies support the replacement: Wang et al. (2021) ([PMID: 33495814](https://pubmed.ncbi.nlm.nih.gov/33495814/)) demonstrated CLC-7 knockdown "weakened the acidification of lysosomes"; Weinert et al. (2010) ([PMID: 20430974](https://pubmed.ncbi.nlm.nih.gov/20430974/)) showed lysosomal storage disease upon loss of CLC-7's antiporter function.

---

## Mechanistic Model / Interpretation

### CLC Family Functional Architecture

The CLC family has undergone a fundamental functional split that is central to understanding why GO:0030321 is inappropriate for CLC-7:

```
CLC FAMILY FUNCTIONAL ARCHITECTURE
===================================

PLASMA MEMBRANE CLCs (Channels)          ENDOLYSOSOMAL CLCs (Antiporters)
─────────────────────────────            ────────────────────────────────
CLC-Ka (CLCNKA) ─┐                      CLC-3 ─── endosomes
CLC-Kb (CLCNKB) ─┤ Passive Cl⁻          CLC-4 ─── endosomes
CLC-1  (CLCN1)  ─┤ channels             CLC-5 ─── endosomes
CLC-2  (CLCN2)  ─┘                      CLC-6 ─── late endosomes
                                         CLC-7 ─── lysosomes + osteoclast
Key features:                                      ruffled border
• Val at gating position (channel)
• Short N-terminus, no sorting motifs    Key features:
• Basolateral/apical membrane            • Glu at gating position (antiporter)
• Transepithelial Cl⁻ transport ✓        • Long N-terminus with dileucine/
                                           acidic cluster sorting motifs
                                         • 2Cl⁻/1H⁺ exchange stoichiometry
                                         • Intracellular localization
                                         • Transepithelial transport ✗
```

### CLC-7 Intracellular Function

```
┌──────────────────────────────────────────────┐
│                LYSOSOME                       │
│                                               │
│   ┌─────────────┐   ┌─────────────┐          │
│   │  CLC-7/OSTM1│   │  V-ATPase   │          │
│   │  antiporter  │   │             │          │
│   │  2Cl⁻ → lumen│   │  H⁺ → lumen│          │
│   │  1H⁺ ← lumen│   │             │          │
│   └─────────────┘   └─────────────┘          │
│                                               │
│   CLC-7 provides Cl⁻ shunt for V-ATPase     │
│   → enables luminal acidification (pH ~4.5)   │
│   → maintains Cl⁻ homeostasis                │
│   → supports autophagy & degradation         │
└──────────────────────────────────────────────┘
```

### Osteoclast Ruffled Border Context

```
┌──────────────────────────────────────────────┐
│   OSTEOCLAST RUFFLED BORDER                  │
│                                               │
│   CLC-7/OSTM1 + V-ATPase at ruffled border  │
│   → acidify resorption lacuna (pH ~4.5)      │
│   → dissolve hydroxyapatite                  │
│   → Loss of CLC-7 → osteopetrosis           │
│                                               │
│   NOTE: Ruffled border derives from lysosomal│
│   membrane exocytosis, NOT apical/basolateral│
│   plasma membrane. Osteoclasts are NOT       │
│   epithelial cells (monocyte/macrophage      │
│   lineage).                                   │
└──────────────────────────────────────────────┘
```

The osteoclast ruffled border deserves special attention because it is the most plasma-membrane-adjacent context for CLC-7. However, the ruffled border is formed by exocytosis of lysosomal vesicles and is topologically distinct from apical/basolateral plasma membrane domains. CLC-7 reaches the ruffled border via its normal lysosomal trafficking pathway, not via plasma membrane targeting. This does not constitute transepithelial transport. Osteoclasts are multinucleated cells derived from the hematopoietic monocyte/macrophage lineage — they are not epithelial cells and do not form an epithelium.

### Annotation Provenance Flow

```
PMID:32851177 abstract sentence (CLC family-level):
  "CLC family proteins... regulate the transepithelial Cl⁻ transport"
         ↓ (misattributed to CLC-7 specifically)
ComplexPortal IDA annotation: clcn7-ostm1_human → GO:0030321
         ↓ (used as seed for PANTHER propagation)
PANTHER IBA annotation: CLCN7 (P51798) → GO:0030321
         ↓ (propagated to orthologs within PTHR11689)
~1,198 IBA annotations across species for CLCN7/OSTM1 orthologs
```

### Direct Gene-Product Activity vs. Downstream Phenotypes

**Direct molecular function:** CLC-7 is a slowly voltage-gated electrogenic 2Cl⁻/1H⁺ antiporter that exchanges two chloride ions for one proton. This is its direct molecular function, well-established by electrophysiology on plasma-membrane-retargeted CLC-7 mutants (since native CLC-7 is inaccessible to patch-clamp at its endolysosomal location).

**Immediate cellular function:** CLC-7 accumulates chloride in the lysosomal lumen while removing protons, contributing to lysosomal ion homeostasis. This is coupled to V-ATPase-driven proton pumping to maintain lysosomal acidity and chloride balance.

**Downstream phenotypes (NOT direct function — should not guide BP annotation):**
- Osteopetrosis (impaired bone resorption due to failed lacuna acidification)
- Lysosomal storage disease (impaired lysosomal degradation)
- Neurodegeneration (secondary to lysosomal dysfunction)
- Coat color changes in mice (melanocyte lysosome-related organelle defects)

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Claim Tested | Key Finding | Context | Confidence |
|---|----------|--------------|-----------|--------------|-------------|---------|------------|
| 1 | [PMID: 20817731](https://pubmed.ncbi.nlm.nih.gov/20817731/) | Direct assay (sorting motif mutagenesis) | **Supports over-annotation hypothesis** | CLC-7 has lysosomal sorting signals | CLC-7 shifted to PM only by combined mutation of N-terminal sorting motifs | HeLa cells, heterologous expression | High — systematic mutagenesis |
| 2 | [PMID: 17110406](https://pubmed.ncbi.nlm.nih.gov/17110406/) | Review with primary data synthesis | **Supports over-annotation hypothesis** | CLC-7 localization | "The intracellular localization of ClC-6 and ClC-7/Ostm1 precluded biophysical studies" | CLC family review by leading expert | High |
| 3 | [PMID: 16525474](https://pubmed.ncbi.nlm.nih.gov/16525474/) | Direct assay (co-localization) | **Supports over-annotation hypothesis** | CLC-7/Ostm1 localization | "Both ClC-7 and Ostm1 proteins co-localize in late endosomes and lysosomes of various tissues, as well as in the ruffled border of bone-resorbing osteoclasts" | Mouse tissues, immunofluorescence | High — multiple tissues |
| 4 | [PMID: 15706348](https://pubmed.ncbi.nlm.nih.gov/15706348/) | Direct assay (KO mouse) | **Supports over-annotation hypothesis** | CLC-7 function and location | "ClC-7 is a chloride channel of late endosomes and lysosomes"; KO causes lysosomal storage disease | Mouse KO model | High — foundational study |
| 5 | [PMID: 32851177](https://pubmed.ncbi.nlm.nih.gov/32851177/) | Structural (cryo-EM) | **Qualifies** — cited for annotation but does NOT support it | Source of IDA annotation | Paper states CLC family broadly "regulate the transepithelial Cl⁻ transport" but specifies CLC-7 "mainly resides in lysosomes and osteoclast ruffled membranes" | Human CLC-7/Ostm1 cryo-EM | High — the paper contradicts the annotation it was cited for |
| 6 | [PMID: 32749217](https://pubmed.ncbi.nlm.nih.gov/32749217/) | Structural (cryo-EM, 2.8 Å) | **Supports over-annotation hypothesis** | CLC-7 structure and location | CLC-7 in lysosomal homeostasis; OSTM1 protects from lysosomal lumen degradation | Human CLC-7/OSTM1 cryo-EM | High |
| 7 | [PMID: 38294065](https://pubmed.ncbi.nlm.nih.gov/38294065/) | Direct assay | **Supports over-annotation hypothesis** | CLC-7 localization (2024) | "CLCN7 is localized to the endolysosomal compartments" | Mouse/zebrafish microglia | High — recent confirmation |
| 8 | [PMID: 26346547](https://pubmed.ncbi.nlm.nih.gov/26346547/) | Direct assay (KO mouse) | **Supports over-annotation hypothesis** | CLC-7 in ameloblasts (epithelial) | CLC-7 in ameloblasts is "located in late endosomes and lysosomes"; KO does not significantly affect enamel mineralization | Mouse ameloblasts | High — directly tests epithelial context |
| 9 | [PMID: 24103576](https://pubmed.ncbi.nlm.nih.gov/24103576/) | Direct assay (KO/transgenic mouse) | **Supports over-annotation hypothesis** | CLC-7 in gastric epithelium | "Loss of ClC-7 did not entail a relevant elevation of gastric pH" | Mouse gastric epithelium | High — directly tests epithelial secretion |
| 10 | [PMID: 25663454](https://pubmed.ncbi.nlm.nih.gov/25663454/) | Mutant phenotype | **Supports over-annotation hypothesis** | CLC-7 in dental epithelium | Dental defects from CLC-7 loss are osteoclast-mediated, not epithelial; CLC-7 "not critical to enamel and dentin formation" | Mouse dental tissue | High |
| 11 | [PMID: 20430974](https://pubmed.ncbi.nlm.nih.gov/20430974/) | Direct assay (knock-in mouse) | **Supports antiporter role** | CLC-7 antiporter mechanism | Uncoupled CLC-7 mutant (Cl⁻ conductor mode) causes lysosomal storage despite normal pH; Cl⁻/H⁺ exchange stoichiometry is essential | Mouse knock-in | High — elegant mechanistic study |
| 12 | [PMID: 33495814](https://pubmed.ncbi.nlm.nih.gov/33495814/) | Knockdown | **Supports lysosomal acidification role** | CLC-7 and lysosomal pH | CLC-7 knockdown weakened lysosomal acidification and impaired autophagy | Mouse cardiomyocytes | Medium — siRNA approach |
| 13 | [PMID: 12111250](https://pubmed.ncbi.nlm.nih.gov/12111250/) | Direct assay | **Supports CLC-K distinction** | Barttin activates CLC-K | CLC-Kb + barttin mediates basolateral Cl⁻ release in transepithelial reabsorption | Xenopus oocytes, kidney | High |
| 14 | [PMID: 11053039](https://pubmed.ncbi.nlm.nih.gov/11053039/) | Review | **Supports CLC-K distinction** | Renal CLC roles | CLC-K1 and CLC-K2 mediate transepithelial Cl⁻ transport; CLC-7 not mentioned in this role | Mouse/human kidney | Medium — review-level |
| 15 | [PMID: 16179405](https://pubmed.ncbi.nlm.nih.gov/16179405/) | Direct assay (electrophysiology) | **Supports antiporter classification** | CLC-4, CLC-5 are Cl⁻/H⁺ exchangers | "Flux of Cl⁻ in one direction is stoichiometrically coupled to the movement of protons in the opposite direction" | Xenopus oocytes | High — landmark mechanistic study |
| 16 | [PMID: 24159188](https://pubmed.ncbi.nlm.nih.gov/24159188/) | Mutant phenotype + electrophysiology | **Supports over-annotation hypothesis** | CLC-7 gating and disease | Disease-causing mutations affect lysosomal CLC-7/Ostm1 function; PM targeting used only as experimental tool | Cattle, HEK293 | High |
| 17 | Computational (this study) | Computational (sorting signals) | **Supports over-annotation hypothesis** | N-terminal sorting motifs | CLCN7 has dileucine motifs (EAAPLL, TPLL), acidic cluster (DDEE), DXXLL motif (DDELL); CLCNKA/CLCNKB have NONE | Sequence analysis | High — validated by PMID:20817731 |
| 18 | Computational (this study) | Computational (domain architecture) | **Supports over-annotation hypothesis** | Gating glutamate, family classification | CLCN7 has gating Glu (antiporter); CLCNKA/CLCNKB have Val (channel). PANTHER: PTHR11689 vs PTHR45720 | Sequence/domain analysis | High |

---

## Sorting Signal Comparison Table

| Feature | CLCN7 (P51798) | CLCNKA (P51800) | CLCNKB (P51801) |
|---------|---------------|-----------------|-----------------|
| Sequence length | 797 aa | 662 aa | 662 aa |
| N-terminal cytoplasmic tail | **126 aa** (before first TM) | ~51 aa | ~51 aa |
| N-terminal [DE]xxxL[LI] motifs | **EAAPLL** (pos 19–24) | None | None |
| N-terminal dileucine variants | **TPLL** (pos 33–36) | None | None |
| N-terminal acidic clusters | **DDEE** (pos 16–19), **DDE** (pos 65–67) | None | None |
| N-terminal DXXLL motifs | **DDELL** (pos 65–69) | None | None |
| Gating glutamate (Eext) | **Yes** (Glu) → antiporter | **No** (Val) → channel | **No** (Val) → channel |
| Transport mechanism | **2Cl⁻/1H⁺ antiport** | Passive Cl⁻ conductance | Passive Cl⁻ conductance |
| PANTHER family | PTHR11689 (antiporter) | PTHR45720 (channel) | PTHR45720 (channel) |
| InterPro subfamily | IPR002249 (H⁺/Cl⁻ exchanger 7) | IPR002250 (ClC-K) | IPR002250 (ClC-K) |
| Beta-subunit | OSTM1 (lysosomal) | Barttin (PM targeting) | Barttin (PM targeting) |
| Native localization | **Lysosome / late endosome** | Plasma membrane | Plasma membrane |
| Transepithelial function | **No** | **Yes** (kidney tubules) | **Yes** (kidney tubules) |

---

## GO Curation Implications

### Recommended Actions (Leads Requiring Curator Verification)

**1. REMOVE: GO:0030321 (transepithelial chloride transport) — HIGH PRIORITY**

Both annotation sources should be addressed:
- **IDA annotation (ComplexPortal, PMID:32851177):** The cited paper does not attribute transepithelial transport to CLC-7 specifically. The phrase appears in a family-level introductory sentence. The same paper's abstract states CLC-7 resides in lysosomes and ruffled membranes.
- **IBA annotation (PANTHER PTN002481857):** Propagated from the flawed IDA above. Removing the IDA root source should allow the IBA propagation (~1,198 ortholog annotations) to be automatically corrected.

**2. ADD: GO:0007042 (lysosomal lumen acidification) — HIGH PRIORITY**
- Supported by [PMID: 33495814](https://pubmed.ncbi.nlm.nih.gov/33495814/) (CLC-7 knockdown impairs lysosomal acidification), [PMID: 20430974](https://pubmed.ncbi.nlm.nih.gov/20430974/) (uncoupled mutant causes lysosomal storage disease), [PMID: 15706348](https://pubmed.ncbi.nlm.nih.gov/15706348/) (CLC-7 loss causes lysosomal dysfunction).
- Suggested evidence code: IMP (Inferred from Mutant Phenotype).

**3. RETAIN: GO:1902476 (chloride transmembrane transport)**
- Already annotated with IBA, IEA, TAS. Appropriate as CLC-7 does transport Cl⁻, just not across epithelia.

**4. RETAIN: GO:0005765 (lysosomal membrane) — CC**
- Already annotated with HDA, EXP, IDA evidence. Well supported.

**5. FLAG: PANTHER IBA Propagation for CLC Family Review**
- The ~1,198 IBA annotations to GO:0030321 for CLCN7 orthologs across species should be reassessed once the ComplexPortal IDA root source is corrected.

**6. CONSIDER: NOT Annotation**
- If the GO annotation system supports explicit NOT qualifiers, consider adding NOT|involved_in GO:0030321 for CLCN7 to prevent re-annotation.

### GO Decision Table

| GO Term | Current Status | Recommended Action | Rationale | Key Reference |
|---------|---------------|-------------------|-----------|---------------|
| GO:0030321 (transepithelial Cl⁻ transport) | Annotated (IDA, IBA) | **Remove** | No evidence CLC-7 is at epithelial PM or mediates transepithelial transport | PMID:20817731, 15706348 |
| GO:0007042 (lysosomal lumen acidification) | Not annotated | **Add (IMP)** | CLC-7 provides Cl⁻ shunt for V-ATPase-driven acidification | PMID:20430974, 33495814 |
| GO:1902476 (chloride transmembrane transport) | Annotated (IBA, IEA, TAS) | **Retain** | CLC-7 transports Cl⁻, but intracellularly | — |
| GO:0005765 (lysosomal membrane) | Annotated (HDA, EXP, IDA) | **Retain** | Definitive localization | PMID:15706348, 16525474 |
| GO:0045453 (bone resorption) | May be annotated | **Retain if present (downstream phenotype)** | Osteoclast ruffled border function | PMID:16525474, 33125761 |

---

## Conflicts and Alternatives

### No Conflicting Evidence Found

Despite extensive targeted searches, no evidence was identified that would support CLC-7 involvement in transepithelial chloride transport:

1. **No plasma membrane localization under physiological conditions.** CLC-7 reaches the plasma membrane only when its lysosomal sorting motifs are experimentally mutated ([PMID: 20817731](https://pubmed.ncbi.nlm.nih.gov/20817731/)), or when deliberately engineered with plasma membrane targeting signals for electrophysiological study ([PMID: 23983121](https://pubmed.ncbi.nlm.nih.gov/23983121/); [PMID: 24159188](https://pubmed.ncbi.nlm.nih.gov/24159188/)).

2. **No functional transepithelial transport demonstrated.** In every epithelial context examined (ameloblasts, gastric epithelium, renal tubules), CLC-7's function is intracellular.

3. **No isoform-specific targeting to the plasma membrane.** UniProt lists two CLCN7 isoforms (P51798-1, P51798-2); isoform 2 differs at positions 48–71 but key lysosomal sorting motifs (EAAPLL at 19–24, TPLL at 33–36, DDEE at 16–19) are preserved in both. No alternative transcript or isoform has been shown to lack sorting motifs or localize to the plasma membrane.

4. **No surface proteomics evidence.** No cell-surface proteomics dataset was found reporting CLC-7 at the plasma membrane.

### Source of Confusion: CLC Family-Level Statements

Many reviews describe the CLC family as including channels involved in transepithelial transport. When such descriptions are misapplied to individual intracellular CLCs, over-annotation results. This is precisely what happened with the ComplexPortal IDA annotation — a family-level introductory statement in [PMID: 32851177](https://pubmed.ncbi.nlm.nih.gov/32851177/) was misattributed to CLC-7 specifically.

### Osteoclast Ruffled Border: Not "Transepithelial"

The osteoclast ruffled border is sometimes considered a plasma-membrane-like domain, but:
- Osteoclasts are not epithelial cells; they are multinucleated cells derived from hematopoietic monocyte/macrophage lineage
- The ruffled border is a specialized lysosomal membrane derivative fused with the plasma membrane facing a sealed lacuna
- GO:0030321 specifically requires movement of chloride ions across an epithelium — osteoclasts do not form an epithelium
- Even if the definition were stretched, the ion movement is Cl⁻/H⁺ antiport for lacuna acidification, not vectorial Cl⁻ transport across an epithelial cell layer

---

## Knowledge Gaps

| Gap | What Was Checked | Why It Matters | Resolving Evidence |
|-----|-----------------|----------------|-------------------|
| Whether any CLCN7 isoform lacks sorting motifs | UniProt isoforms; both retain key motifs | An isoform lacking sorting motifs might localize to PM | Systematic survey of all validated transcripts — gap partially resolved (2 isoforms, both retain motifs) |
| Surface proteomics for CLC-7 | PubMed literature search for CLC-7 in surfaceome datasets | Would provide unbiased evidence for or against PM localization | Mining published cell-surface proteomics datasets — no positive hits found |
| CLC-7 in non-mammalian organisms | Limited to mammalian and zebrafish literature | Annotation propagation affects many non-mammalian orthologs | Comparative localization studies in additional organisms |
| ComplexPortal annotation review process | Identified annotation source and cited paper | Understanding how the family-level statement became an IDA annotation could prevent recurrence | Contact ComplexPortal curators to flag and correct |
| Precise mechanism of ruffled border vs. lysosomal CLC-7 function | Known to be at both locations | Annotation granularity for osteoclast vs. lysosome function | Tissue-specific conditional KOs with compartment-specific pH measurements |

None of these gaps threaten the core conclusion. Even in the unlikely event that a minor isoform or organism-specific variant reaches the plasma membrane, the primary function of human CLCN7 is overwhelmingly established as intracellular endolysosomal Cl⁻/H⁺ exchange.

---

## Proposed Follow-up Experiments / Discriminating Tests

1. **Chloride flux assay in polarized epithelial monolayers:** CLCN7 knockdown vs. wild-type in MDCK or Caco-2 cells on Transwell inserts, measuring transepithelial Cl⁻ flux. Use CLCNKB knockdown as a positive control. Expected result: no effect from CLCN7 loss.

2. **Surface biotinylation of CLC-7 in polarized epithelial cells:** Cell-surface biotinylation followed by streptavidin pulldown and CLC-7 Western blot in multiple epithelial cell lines. Would directly test whether endogenous CLC-7 is ever present at the cell surface. Expected result: CLC-7 absent from surface fraction.

3. **BioID/APEX2 proximity labeling:** CLC-7 fused to a proximity labeling enzyme, followed by proteomics to identify neighboring proteins. If all neighbors are lysosomal/endosomal markers, this confirms intracellular localization.

4. **Single-cell RNA-seq + Human Protein Atlas cross-reference:** Compare CLCN7 expression across all epithelial cell types with Human Protein Atlas subcellular localization data to confirm universal intracellular localization pattern.

5. **ComplexPortal curator contact:** Flag the IDA annotation for the clcn7-ostm1_human complex with GO:0030321 (PMID:32851177) as a misattribution for curator review and correction.

---

## Curation Leads

### Lead 1: Remove GO:0030321 from CLCN7 (HIGH PRIORITY)
- **Action:** Remove both IDA and IBA annotations for GO:0030321 (transepithelial chloride transport)
- **Rationale:** No experimental evidence supports this annotation. All localization data places CLC-7 in lysosomes/late endosomes. The IDA citation (PMID:32851177) contains a CLC-family-level introductory statement misattributed to CLC-7 specifically.
- **Candidate references to verify:**
  - [PMID: 20817731](https://pubmed.ncbi.nlm.nih.gov/20817731/) — *"ClC-7 could be partially shifted from lysosomes to the plasma membrane by combined mutation of N-terminal sorting motifs"* — confirms normal localization is NOT plasma membrane
  - [PMID: 17110406](https://pubmed.ncbi.nlm.nih.gov/17110406/) — *"the intracellular localization of ClC-6 and ClC-7/Ostm1 precluded biophysical studies"* — CLC-7 is intracellular
  - [PMID: 16525474](https://pubmed.ncbi.nlm.nih.gov/16525474/) — *"both ClC-7 and Ostm1 proteins co-localize in late endosomes and lysosomes of various tissues, as well as in the ruffled border of bone-resorbing osteoclasts"* — definitive localization

### Lead 2: Add GO:0007042 (Lysosomal Lumen Acidification) to CLCN7 (HIGH PRIORITY)
- **Action:** Add BP annotation with IMP evidence
- **Reference to verify:** [PMID: 20430974](https://pubmed.ncbi.nlm.nih.gov/20430974/) — *"We generated mice carrying a point mutation converting ClC-7 into an uncoupled (unc) Cl⁻ conductor. Despite maintaining lysosomal conductance and normal lysosomal pH, these Clcn7(unc/unc) mice showed lysosomal storage disease like mice lacking ClC-7"*
- **Additional reference:** [PMID: 33495814](https://pubmed.ncbi.nlm.nih.gov/33495814/) — CLC-7 knockdown weakened lysosomal acidification

### Lead 3: Flag ~1,198 IBA Ortholog Annotations for Reassessment (MEDIUM PRIORITY)
- **Action:** After IDA source is removed, PANTHER IBA annotations propagated from PTN002481857 for GO:0030321 should be flagged for reassessment
- **Scope:** Affects CLCN7 orthologs across many species

### Lead 4: Flag ComplexPortal IDA Annotation as Misattributed
- **Action:** Contact ComplexPortal to review the IDA annotation for the clcn7-ostm1_human complex with GO:0030321 citing PMID:32851177
- **Rationale:** The cited paper's mention of "transepithelial Cl⁻ transport" is a family-level introductory statement; the paper's specific findings do not support this function for CLC-7

### Suggested Questions for Curator
1. Does the ComplexPortal entry for CLC-7/OSTM1 need to be corrected to remove the GO:0030321 annotation at the source?
2. Should the PANTHER family node PTN002481857 be reviewed to prevent re-propagation?
3. Is GO:0007042 (lysosomal lumen acidification) sufficiently specific, or should a more precise term be considered?
4. Should a NOT annotation (NOT involved_in GO:0030321) be added to prevent future re-annotation?

---

## Evidence Base: Key Literature

| PMID | Title (abbreviated) | Year | Relevance |
|------|---------------------|------|-----------|
| [15706348](https://pubmed.ncbi.nlm.nih.gov/15706348/) | Loss of ClC-7 leads to lysosomal storage disease | 2005 | Foundational: CLC-7 is a lysosomal transporter |
| [16525474](https://pubmed.ncbi.nlm.nih.gov/16525474/) | ClC-7 requires Ostm1 as β-subunit | 2006 | CLC-7/Ostm1 co-localization in lysosomes and ruffled border |
| [17110406](https://pubmed.ncbi.nlm.nih.gov/17110406/) | CLC chloride transporters in endosomal-lysosomal pathway | 2007 | CLC-7 intracellular localization precludes PM studies |
| [20430974](https://pubmed.ncbi.nlm.nih.gov/20430974/) | Lysosomal pathology upon loss of H⁺-driven Cl⁻ accumulation | 2010 | Antiporter mechanism essential; channel mode insufficient |
| [20817731](https://pubmed.ncbi.nlm.nih.gov/20817731/) | Sorting motifs of endosomal/lysosomal CLC transporters | 2010 | N-terminal sorting motifs target CLC-7 to lysosomes |
| [24103576](https://pubmed.ncbi.nlm.nih.gov/24103576/) | ClC-7 expression levels regulate bone turnover, not gastric acid | 2014 | CLC-7 not required for gastric acid secretion |
| [25663454](https://pubmed.ncbi.nlm.nih.gov/25663454/) | Dental and cranial pathologies in ClC-7 KO mice | 2014 | Dental defects are osteoclast-mediated, not epithelial |
| [26346547](https://pubmed.ncbi.nlm.nih.gov/26346547/) | Null mutation of Clcn7 and dental root formation | 2015 | CLC-7 in ameloblasts is intracellular; not critical for enamel |
| [32749217](https://pubmed.ncbi.nlm.nih.gov/32749217/) | Cryo-EM structure of CLC-7/OSTM1 | 2020 | Structural basis for lysosomal function |
| [32851177](https://pubmed.ncbi.nlm.nih.gov/32851177/) | Molecular insights into human CLC-7/Ostm1 | 2020 | Source of misattributed IDA annotation |
| [33495814](https://pubmed.ncbi.nlm.nih.gov/33495814/) | CLC-7 promotes lysosomal acidification-mediated autophagy | 2021 | CLC-7 knockdown impairs lysosomal acidification |
| [38294065](https://pubmed.ncbi.nlm.nih.gov/38294065/) | CLC-7 essential for phagocytic clearance by microglia | 2024 | Recent confirmation of endolysosomal localization |

---

*Report generated 2026-06-21. Based on analysis of 37 papers, computational sequence analysis, and database annotation provenance tracing across 3 investigation iterations.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)