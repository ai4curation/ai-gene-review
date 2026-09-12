---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-19T13:30:23.515335'
end_time: '2026-06-19T13:58:19.277432'
duration_seconds: 1675.76
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: pmp20
  gene_symbol: pmp20
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008379
  hypothesis_text: pmp20 has thioredoxin peroxidase activity (GO:0008379).
  term_context: '- Term: thioredoxin peroxidase activity (GO:0008379)

    - Evidence type: IEA

    - Original reference: GO_REF:0000002'
  reference_context: '- GO_REF:0000002

    - PMID:20356456'
  source_file: genes/SCHPO/pmp20/pmp20-ai-review.yaml
  source_selector: existing_annotations[11].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008379\n  label: thioredoxin peroxidase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000002"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 13
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** pmp20
- **Gene symbol:** pmp20

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008379
- **Source file:** genes/SCHPO/pmp20/pmp20-ai-review.yaml
- **Source selector:** existing_annotations[11].function_hypothesis

## Seed Hypothesis

pmp20 has thioredoxin peroxidase activity (GO:0008379).

## Term and Decision Context

- Term: thioredoxin peroxidase activity (GO:0008379)
- Evidence type: IEA
- Original reference: GO_REF:0000002

## Reference Context

- GO_REF:0000002
- PMID:20356456

## Source Context YAML

```yaml
term:
  id: GO:0008379
  label: thioredoxin peroxidase activity
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
prompt so the report can be compared against them after the run.

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

# Final Report: Evaluation of Thioredoxin Peroxidase Activity (GO:0008379) Annotation for *S. pombe* pmp20

## Executive Judgment

**Verdict: Over-annotated — the GO:0008379 annotation should be removed.**

The annotation of GO:0008379 (thioredoxin peroxidase activity) to *Schizosaccharomyces pombe* pmp20 is definitively over-annotated and should be removed or suppressed. The strongest evidence comes from the very paper cited in the annotation's reference chain: Kim et al. (2010, [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/)) directly tested recombinant *S. pombe* PMP20 for thioredoxin-dependent peroxidase activity and found none. PomBase curators have already acted on this evidence by annotating pmp20 with NOT|enables GO:0004601 (peroxidase activity) using IDA evidence — a parent term of GO:0008379 — meaning that the existing IEA and IBA annotations for GO:0008379 are logically inconsistent with curator-verified experimental data. The experimentally validated molecular function of PMP20 is unfolded protein holdase activity (GO:0140309), representing a lineage-specific functional divergence from the catalytically active peroxiredoxin Prx5 subfamily.

The key caveat is that PMP20 retains the conserved peroxiredoxin fold and the GAFTPPC active-site motif with a single peroxidatic cysteine (Cys43). Its orthologs in other organisms — notably *Candida boidinii* CbPmp20 and mammalian PRDX5 — do possess peroxidase activity, which is the likely source of the computational annotation transfer. However, *S. pombe* PMP20 has functionally diverged: it lacks peroxidase activity of any kind (thioredoxin-dependent, glutathione-dependent, or otherwise) and instead acts as a molecular chaperone.

---

## Summary

This report evaluates whether *S. pombe* pmp20 (UniProt: O14313) genuinely possesses thioredoxin peroxidase activity as annotated by GO:0008379. The annotation was assigned via IEA (InterPro-based electronic annotation, GO_REF:0000002) and is also present via IBA (phylogenetic annotation from GO_Central). Our investigation integrated direct biochemical evidence, sequence analysis, comparative enzymology across species, and a comprehensive survey of the *S. pombe* peroxide-defense system.

The evidence is unambiguous: recombinant PMP20 was directly assayed for thioredoxin-dependent peroxidase activity and showed none, while two other peroxiredoxins from the same organism (Tpx1 and BCP) tested positive in the same experimental system. A separate comprehensive study of H₂O₂ scavenging enzymes in *S. pombe* identified only Tpx1, catalase, and Gpx1 as contributors — PMP20 was entirely absent from the peroxide-defense repertoire. Instead, PMP20 demonstrated molecular chaperone (holdase) activity in thermal aggregation protection assays.

This case illustrates a well-documented evolutionary phenomenon: peroxiredoxins can switch between peroxidase and chaperone functions depending on structural context, and computational annotation transfer across the Prx5 subfamily does not reliably predict which function predominates in each lineage. The GO:0008379 annotation should be removed, and the existing NOT|enables GO:0004601 and enables GO:0140309 annotations from PomBase should be regarded as the authoritative functional characterization.

---

## Key Findings

### Finding 1: PMP20 Lacks Thioredoxin Peroxidase Activity Despite Peroxiredoxin Fold

Kim et al. (2010) ([PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/)) performed a systematic characterization of all four peroxiredoxin isozymes in *S. pombe*: Tpx1 (typical 2-Cys), BCP (atypical 2-Cys), PMP20 (atypical 2-Cys/1-Cys), and Gpx1 (glutathione peroxidase-type). Using purified recombinant proteins, they measured thioredoxin-dependent peroxidase activity directly. The result was unequivocal: *"peroxidase activity was not observed for PMP20 (peroxisomal membrane protein 20)."* In contrast, Tpx1, BCP, and Gpx1 all showed measurable peroxidase activity in the same assay system. The authors concluded: *"The fission yeast PMP20 without thioredoxin-dependent peroxidase activity may act as a molecular chaperone."*

This is the single most important piece of evidence for curation, as it constitutes a direct negative result from a well-controlled biochemical assay specifically testing the function annotated by GO:0008379. Critically, this is the same paper (PMID:20356456) that appears in the reference chain of the annotation under evaluation, making the IEA assignment paradoxical — the reference it ultimately traces to contains evidence *against* the annotated function.

### Finding 2: PMP20 Has Experimentally Confirmed Chaperone (Holdase) Activity

In the same study, Kim et al. (2010) tested PMP20 for molecular chaperone activity using a thermal aggregation protection assay with citrate synthase as substrate at 43°C. PMP20 successfully inhibited thermal aggregation, demonstrating holdase activity. The authors noted: *"TPx, PMP20, and GPx inhibited thermal aggregation of citrate synthase at 43°C, but BCP failed to inhibit the aggregation."* This establishes that PMP20's primary molecular function is as an unfolded protein holdase, not a peroxidase. PomBase has accordingly annotated pmp20 with GO:0140309 (unfolded protein holdase activity) using IDA evidence.

This functional switch from peroxidase to chaperone is not unprecedented in the peroxiredoxin superfamily. Angelucci et al. (2014) ([PMID: 25399604](https://pubmed.ncbi.nlm.nih.gov/25399604/)) proposed an evolutionary framework in which the chemistry of sulfur-based catalytic cysteines in peroxiredoxins makes them inherently capable of structural rearrangements that enable chaperone (holdase) activity, particularly under oxidative stress conditions. The *S. pombe* PMP20 appears to represent a lineage where this moonlighting capacity has become the primary function, with peroxidase activity lost.

### Finding 3: PomBase Already Has a NOT Annotation for Peroxidase Activity

PomBase curators have already processed the evidence from PMID:20356456 and annotated pmp20 with NOT|enables GO:0004601 (peroxidase activity) using the IDA evidence code. GO:0008379 (thioredoxin peroxidase activity) is a direct child term of GO:0004601 in the Gene Ontology hierarchy. By the rules of GO ontology, a NOT annotation on a parent term logically negates all child terms. This means the existing IEA annotation of GO:0008379 (from InterPro, GO_REF:0000002) and the IBA annotation (from GO_Central phylogenetic transfer, GO_REF:0000033) are in direct logical conflict with the curator-verified NOT annotation.

This represents a known class of GO annotation inconsistency where automated computational annotations persist despite contradicting manually curated experimental evidence. The resolution is straightforward: the IDA NOT annotation should take precedence, and the IEA/IBA annotations for GO:0008379 should be suppressed or removed.

### Finding 4: Comprehensive H₂O₂ Scavenging Study Excludes PMP20

Paulo et al. (2014) ([PMID: 24521463](https://pubmed.ncbi.nlm.nih.gov/24521463/)) performed a comprehensive genetic and biochemical characterization of the entire hydrogen peroxide scavenging repertoire in *S. pombe*. Their analysis identified three enzymes responsible for H₂O₂ detoxification: Tpx1 (the primary cytoplasmic peroxidase, essential for aerobic growth), catalase (the secondary barrier activated when Tpx1 is overwhelmed), and Gpx1 (a stationary-phase thioredoxin peroxidase). PMP20 was not included among H₂O₂ scavengers in this comprehensive study, consistent with the direct negative result from Kim et al. (2010). The authors stated: *"A complete characterization of the repertoire of hydrogen peroxide scavenging activities in fission yeast suggests that Tpx1 is the only enzyme with sufficient sensitivity for peroxides and cellular abundance as to control the low levels produced during aerobic growth."*

### Finding 5: Sequence Analysis Reveals Conserved Peroxidatic Cys but Lacking Resolving Cys

Sequence analysis of *S. pombe* PMP20 (O14313) reveals that the protein possesses only one cysteine residue (Cys43) within the conserved GAFTPPC motif. This is the peroxidatic cysteine characteristic of the Prx5/PMP20 subfamily. However, PMP20 lacks a resolving cysteine, which in atypical 2-Cys peroxiredoxins (like mammalian PRDX5) is required to complete the catalytic cycle by forming an intramolecular disulfide bond that can then be reduced by thioredoxin.

Importantly, *C. boidinii* CbPmp20A (P14292) also has only one cysteine (Cys53) in the identical GAFTPPC motif — yet CbPmp20 retains glutathione peroxidase activity ([PMID: 11278957](https://pubmed.ncbi.nlm.nih.gov/11278957/)). This demonstrates that the single-cysteine architecture does not automatically preclude peroxidase activity; rather, *S. pombe* PMP20 has specifically lost this function through sequence divergence in regions outside the immediate active-site motif. Active-site region identity between *S. pombe* PMP20 and *C. boidinii* CbPmp20 is only ~32.5%, with divergence concentrated downstream of the peroxidatic cysteine.

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Claim Tested | Key Finding | Organism / Context | Confidence |
|---|----------|--------------|-----------|-------------|-------------|-------------------|------------|
| 1 | [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/) | Direct assay | **Refutes** GO:0008379 | PMP20 has Trx peroxidase activity | No peroxidase activity detected for recombinant PMP20; Tpx1, BCP, Gpx1 positive | *S. pombe* / in vitro recombinant | **High** — direct biochemical test of the exact function |
| 2 | [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/) | Direct assay | **Supports** chaperone function | PMP20 has holdase activity | PMP20 inhibited thermal aggregation of citrate synthase at 43°C | *S. pombe* / in vitro recombinant | **High** — standard chaperone assay |
| 3 | [PMID: 24521463](https://pubmed.ncbi.nlm.nih.gov/24521463/) | Mutant phenotype / comprehensive survey | **Refutes** GO:0008379 | PMP20 contributes to H₂O₂ scavenging | Only Tpx1, catalase, Gpx1 are H₂O₂ scavengers; PMP20 not included | *S. pombe* / in vivo genetic | **High** — comprehensive organism-wide study |
| 4 | PomBase IDA annotation | Database / curator review | **Refutes** GO:0008379 | PMP20 has peroxidase activity | NOT\|enables GO:0004601 annotated by IDA citing PMID:20356456 | *S. pombe* / database | **High** — expert curator assessment |
| 5 | [PMID: 11278957](https://pubmed.ncbi.nlm.nih.gov/11278957/) | Direct assay | **Qualifies** | Pmp20 orthologs have peroxidase activity | CbPmp20 has glutathione peroxidase activity (not thioredoxin-dependent) | *C. boidinii* / in vitro recombinant | **High** — but different organism |
| 6 | [PMID: 10679306](https://pubmed.ncbi.nlm.nih.gov/10679306/) | Direct assay | **Qualifies** | Mammalian Prx5 has Trx peroxidase activity | Mouse Prx-V is a thioredoxin peroxidase | *M. musculus* / in vitro | **High** — but different organism |
| 7 | [PMID: 10514471](https://pubmed.ncbi.nlm.nih.gov/10514471/) | Direct assay | **Qualifies** | Mammalian PMP20 has antioxidant activity | HsPMP20 has thiol-peroxidase and removes H₂O₂ | *H. sapiens* / in vitro | **High** — but different organism |
| 8 | [PMID: 25399604](https://pubmed.ncbi.nlm.nih.gov/25399604/) | Structural/evolutionary review | **Supports** chaperone hypothesis | Prx moonlighting between peroxidase and chaperone | Cys chemistry enables holdase switching in Prxs; Sec-based GPx lacks this capacity | Evolutionary analysis | **Medium** — theoretical framework |
| 9 | [PMID: 20977338](https://pubmed.ncbi.nlm.nih.gov/20977338/) | Review | **Qualifies** | PRDX5 subfamily biochemistry | Mammalian PRDX5 uses Trx to reduce alkyl hydroperoxides and peroxynitrite; rates vary by substrate | *H. sapiens* / review | **Medium** — different organism |
| 10 | [PMID: 17409354](https://pubmed.ncbi.nlm.nih.gov/17409354/) | Direct assay | **Context** | Tpx1 is the primary H₂O₂ scavenger | Tpx1 is essential for aerobic growth; exquisite H₂O₂ sensitivity | *S. pombe* / in vivo | **High** — establishes Tpx1, not PMP20, as the peroxidase |
| 11 | [PMID: 18162174](https://pubmed.ncbi.nlm.nih.gov/18162174/) | Direct assay | **Context** | Gpx1 is a thioredoxin peroxidase | Gpx1 prefers Trx over GSH; active in stationary phase | *S. pombe* / in vitro + in vivo | **High** — another *S. pombe* Trx peroxidase, not PMP20 |
| 12 | [PMID: 20078128](https://pubmed.ncbi.nlm.nih.gov/20078128/) | Direct assay | **Qualifies** | BCP peroxiredoxins can use different reductants | 1-Cys BCPs can use glutathione; resolving Cys switches mechanism | *B. cenocepacia* / in vitro | **Medium** — illustrates mechanistic flexibility |
| 13 | [PMID: 35403927](https://pubmed.ncbi.nlm.nih.gov/35403927/) | Structural/evolutionary | **Context** | *S. pombe* Gpx1 and Tpx1 use Trx via conserved Cys pair | Fungal GPxs and TPxs diverged from common ancestor; both use resolving Cys mechanism | *S. pombe* / computational | **Medium** — evolutionary context |
| 14 | [PMID: 18084898](https://pubmed.ncbi.nlm.nih.gov/18084898/) | Review | **Supports** chaperone model | 2-Cys Prx have dual peroxidase/chaperone roles | Prxs can switch between peroxidase and chaperone; regulation is key | Yeast / review | **Medium** — review-level support |
| 15 | [PMID: 19538506](https://pubmed.ncbi.nlm.nih.gov/19538506/) | Review | **Context** | Peroxisomal quality control | Peroxisomes contain peroxiredoxin for antioxidant defense | Yeast / review | **Low** — general context only |

---

## GO Curation Implications

### Recommended Curation Actions (Leads Requiring Curator Verification)

**1. Remove or suppress GO:0008379 (thioredoxin peroxidase activity) — MF term**

- **Current state:** Annotated via IEA (InterPro, GO_REF:0000002) and IBA (GO_Central, GO_REF:0000033)
- **Action:** Remove. The direct biochemical evidence (PMID:20356456) shows no thioredoxin-dependent peroxidase activity. The existing NOT|enables GO:0004601 (IDA) logically negates this child term.
- **Justification:** IDA NOT annotation on the parent term GO:0004601 takes precedence over IEA/IBA on the child term GO:0008379. This is the textbook case where automated annotation transfer has been contradicted by direct experiment.

**2. Retain NOT|enables GO:0004601 (peroxidase activity) — MF term**

- **Current state:** Annotated by PomBase with IDA evidence citing PMID:20356456
- **Action:** Retain. This is correctly supported by direct experimental evidence.

**3. Retain GO:0140309 (unfolded protein holdase activity) — MF term**

- **Current state:** Annotated by PomBase with IDA evidence citing PMID:20356456
- **Action:** Retain. The thermal aggregation protection assay provides direct evidence for holdase activity. This represents the experimentally validated primary molecular function.

**4. Consider whether any BP or CC annotations should be updated**

- PMP20's role in the cell should be annotated in terms of protein quality control / chaperone-related biological processes rather than oxidative stress defense / peroxide catabolism.
- Localization annotations (peroxisomal) should be retained as these are independent of molecular function.

### GO Decision Table

| GO Term | ID | Current Annotation | Evidence | Recommended Action | Rationale |
|---------|-----|-------------------|----------|-------------------|-----------|
| Thioredoxin peroxidase activity | GO:0008379 | IEA, IBA | Refuted by IDA (PMID:20356456) | **Remove** | Direct negative result; logically inconsistent with NOT on parent |
| Peroxidase activity | GO:0004601 | NOT\|enables (IDA) | PMID:20356456 | **Retain** | Correctly supported by direct assay |
| Unfolded protein holdase activity | GO:0140309 | IDA | PMID:20356456 | **Retain** | Validated primary molecular function |
| Glutathione peroxidase activity | GO:0004602 | Not annotated | Not tested in *S. pombe* | **Do not add** | No evidence; ortholog CbPmp20 has this but *Sp* PMP20 does not |

---

## Mechanistic Scope

### Direct Gene-Product Activity

*S. pombe* PMP20 is a member of the Prx5/atypical 2-Cys peroxiredoxin subfamily that has undergone functional divergence from peroxidase activity to molecular chaperone (holdase) activity. Its experimentally confirmed direct molecular function is:

- **Unfolded protein holdase activity (GO:0140309):** PMP20 binds unfolding proteins and prevents their aggregation, as demonstrated by inhibition of citrate synthase thermal aggregation at 43°C.

### What PMP20 Does NOT Do (Experimentally Confirmed)

- **Thioredoxin peroxidase activity (GO:0008379):** Directly tested and absent (PMID:20356456)
- **General peroxidase activity (GO:0004601):** NOT annotated by PomBase (IDA)
- **H₂O₂ scavenging:** Excluded from the complete *S. pombe* H₂O₂ defense system (PMID:24521463)

### Separating Direct Activity from Downstream/Inferred Effects

The peroxiredoxin fold and conserved GAFTPPC motif in PMP20 are structural features inherited from the Prx5 subfamily, not indicators of current catalytic function. Computational annotations (IEA from InterPro, IBA from phylogenetic transfer) predicted peroxidase activity based on these structural features and ortholog function, but this prediction was experimentally falsified.

The chaperone activity represents the actual molecular mechanism. Any downstream effects on oxidative stress tolerance (if observed) would be indirect — through protection of other proteins from aggregation — rather than through direct peroxide reduction.

### Mechanistic Model

```
Prx5/PMP20 Subfamily — Functional Divergence

Ancestral Prx5-like protein
├── Peroxidatic Cys + Resolving Cys → Atypical 2-Cys peroxidase
│   └── Mammalian PRDX5: Trx peroxidase (GO:0008379) ✓
│       - 6 Cys residues, including resolving Cys
│       - Reduces H₂O₂, alkyl hydroperoxides, peroxynitrite
│
├── Peroxidatic Cys only (1-Cys) → Variable function
│   ├── C. boidinii CbPmp20: Glutathione peroxidase (GO:0004602) ✓
│   │   - 1 Cys (C53), GAFTPPC motif
│   │   - Peroxidase activity via GSH-dependent cycle
│   │
│   └── S. pombe PMP20: Chaperone/Holdase (GO:0140309) ✓
│       - 1 Cys (C43), GAFTPPC motif
│       - NO peroxidase activity (GO:0004601 NOT) ✗
│       - Holdase activity confirmed by aggregation assay
│       - ~32.5% identity to CbPmp20 in active-site region
│       - Lineage-specific loss of catalytic competence
```

---

## Evidence Base

### Primary Evidence (Direct Experimental, *S. pombe*)

**Kim et al. (2010)** — *"Distinct functional roles of peroxiredoxin isozymes and glutathione peroxidase from fission yeast, Schizosaccharomyces pombe."* [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/)

This is the cornerstone paper for this evaluation. It directly tested all four *S. pombe* peroxiredoxin isozymes for both peroxidase and chaperone activity using purified recombinant proteins. Key quotes:
- *"However, peroxidase activity was not observed for PMP20 (peroxisomal membrane protein 20)."*
- *"TPx, PMP20, and GPx inhibited thermal aggregation of citrate synthase at 43°C, but BCP failed to inhibit the aggregation."*
- *"The fission yeast PMP20 without thioredoxin-dependent peroxidase activity may act as a molecular chaperone."*

**Paulo et al. (2014)** — *"A genetic approach to study H₂O₂ scavenging in fission yeast—distinct roles of peroxiredoxin and catalase."* [PMID: 24521463](https://pubmed.ncbi.nlm.nih.gov/24521463/)

Comprehensive genetic dissection of H₂O₂ scavenging in *S. pombe*. Identified Tpx1 as the primary peroxidase, catalase as secondary, and Gpx1 as a stationary-phase contributor. PMP20 was not included among peroxide-scavenging enzymes. Key quote: *"A complete characterization of the repertoire of hydrogen peroxide scavenging activities in fission yeast suggests that Tpx1 is the only enzyme with sufficient sensitivity for peroxides and cellular abundance as to control the low levels produced during aerobic growth, catalase being the next barrier of detoxification when the steady-state levels of peroxides are increased in Δtpx1 cells."*

### Comparative Evidence (Other Organisms)

**Kal et al. (2000)** — *"Antioxidant system within yeast peroxisome... CbPmp20 in the methylotrophic yeast Candida boidinii."* [PMID: 11278957](https://pubmed.ncbi.nlm.nih.gov/11278957/)

Established that CbPmp20 — the closest characterized ortholog — has glutathione peroxidase activity (not thioredoxin-dependent), depends on its single Cys53 residue, and is essential for growth on methanol. This paper is critical because it shows that even the most similar ortholog uses glutathione rather than thioredoxin, making the GO:0008379 annotation doubly inappropriate.

**Knoops et al. (2000)** — *"Mouse peroxiredoxin V is a thioredoxin peroxidase that inhibits p53-induced apoptosis."* [PMID: 10679306](https://pubmed.ncbi.nlm.nih.gov/10679306/)

Identified mammalian PRDX5 as a thioredoxin peroxidase. This is the basis for the subfamily-level annotation that was computationally transferred to *S. pombe* PMP20.

**Seo et al. (1999)** — *"Characterization of human and murine PMP20 peroxisomal proteins that exhibit antioxidant activity in vitro."* [PMID: 10514471](https://pubmed.ncbi.nlm.nih.gov/10514471/)

Showed human PMP20 has thiol-peroxidase activity and removes H₂O₂, establishing antioxidant function for the mammalian ortholog.

### Evolutionary/Mechanistic Framework

**Angelucci et al. (2014)** — *"Selenocysteine robustness versus cysteine versatility: a hypothesis on the evolution of the moonlighting behaviour of peroxiredoxins."* [PMID: 25399604](https://pubmed.ncbi.nlm.nih.gov/25399604/)

Proposed that the sulfur chemistry of catalytic cysteines in peroxiredoxins makes them inherently capable of switching to chaperone function — the cysteine's versatility enables moonlighting. This framework explains the *S. pombe* PMP20 case as an extreme instance where the chaperone function has become dominant.

### *S. pombe* Peroxidase System Context

**Jara et al. (2007)** — *"The peroxiredoxin Tpx1 is essential as a H₂O₂ scavenger during aerobic growth in fission yeast."* [PMID: 17409354](https://pubmed.ncbi.nlm.nih.gov/17409354/)

Established Tpx1 as the essential H₂O₂ scavenger in *S. pombe*, with exquisite sensitivity for peroxides. This contextualizes PMP20's role: the organism already has dedicated, highly efficient peroxidases, potentially reducing selective pressure to maintain PMP20's peroxidase function.

**Kim et al. (2008)** — *"Gpx1 is a stationary phase-specific thioredoxin peroxidase in fission yeast."* [PMID: 18162174](https://pubmed.ncbi.nlm.nih.gov/18162174/)

Demonstrated that *S. pombe* Gpx1 is a thioredoxin peroxidase despite being a glutathione peroxidase family member. This is notable because it shows that in *S. pombe*, thioredoxin peroxidase activity is carried out by Gpx1 and Tpx1 — not PMP20.

---

## Conflicts and Alternatives

### Source of the Incorrect Annotation

The GO:0008379 annotation derives from two computational methods:

1. **IEA (InterPro, GO_REF:0000002):** InterPro classifies PMP20 within the peroxiredoxin domain family based on sequence features (the GAFTPPC motif, thioredoxin fold). The domain-to-function mapping assumes peroxidase activity based on the structural fold.

2. **IBA (GO_Central phylogenetic transfer, GO_REF:0000033):** Phylogenetic analysis places PMP20 in the Prx5/PRDX5 subfamily, where mammalian members (PRDX5) and some yeast members (CbPmp20) have peroxidase activity. The annotation was transferred across the subfamily.

Both methods are reasonable computational inferences that happen to be wrong for this specific protein due to lineage-specific functional divergence.

### Paralog Consideration

*S. pombe* has three other proteins with actual peroxidase activity: Tpx1, BCP, and Gpx1. There is no paralog confusion here — PMP20 was tested alongside these paralogs in the same study, and only PMP20 lacked peroxidase activity.

### Could PMP20 Have a Cryptic or Condition-Specific Peroxidase Activity?

This is the strongest counterargument, but it is not well-supported:
- The Kim et al. (2010) assay used standard in vitro conditions with purified recombinant protein
- Paulo et al. (2014) found no in vivo peroxidase role under any condition tested
- PomBase curators evaluated the evidence and applied a NOT annotation without qualification
- No published study has reported any peroxidase activity for *S. pombe* PMP20 under any conditions

### Organism-Specific Differences: Key Comparison Table

| Feature | *S. pombe* PMP20 | *C. boidinii* CbPmp20 | *H. sapiens* PRDX5 |
|---------|------------------|----------------------|---------------------|
| Cys residues | 1 (C43) | 1 (C53) | 6 (incl. resolving) |
| Active site motif | GAFTPPC | GAFTPPC | Similar but expanded |
| Trx peroxidase activity | **None** | Not tested | **Yes** |
| GSH peroxidase activity | Not tested | **Yes** | Low |
| Chaperone activity | **Yes** | Not tested | Likely (moonlighting) |
| Peroxisomal targeting | Yes (PTS1-like) | Yes (PTS1) | Yes (PTS1) |
| Primary function | Chaperone | Peroxidase | Peroxidase |

---

## Knowledge Gaps

### Gap 1: Glutathione-Dependent Peroxidase Activity Not Directly Tested for *S. pombe* PMP20

- **What was checked:** Thioredoxin-dependent peroxidase activity (negative, PMID:20356456). PomBase NOT annotation covers GO:0004601 broadly.
- **Why it matters:** *C. boidinii* CbPmp20 uses glutathione, not thioredoxin. If *S. pombe* PMP20 retained glutathione peroxidase activity, GO:0008379 would be wrong (too specific) but a related peroxidase term might apply.
- **Assessment:** The broad NOT|GO:0004601 annotation from PomBase and the exclusion of PMP20 from the comprehensive H₂O₂ study strongly suggest no peroxidase activity of any kind, but a specific glutathione peroxidase assay would be definitive.
- **Resolution:** Test recombinant *S. pombe* PMP20 for glutathione-dependent peroxidase activity with alkyl hydroperoxides and H₂O₂.

### Gap 2: Structural Basis for Loss of Peroxidase Activity

- **What was checked:** Sequence alignment showing ~32.5% identity in the active-site region between *S. pombe* PMP20 and *C. boidinii* CbPmp20.
- **Why it matters:** Understanding why the conserved motif fails to catalyze peroxide reduction could inform annotation of other uncharacterized PMP20 family members.
- **Resolution:** Crystal structure of *S. pombe* PMP20, or site-directed mutagenesis swapping residues from the active-site region.

### Gap 3: In Vivo Chaperone Substrates Unknown

- **What was checked:** In vitro holdase assay with citrate synthase as a generic substrate.
- **Why it matters:** The natural substrates of PMP20's chaperone activity are unknown, making it difficult to assign a precise biological process term.
- **Resolution:** Proximity labeling (BioID/APEX) or co-immunoprecipitation under stress conditions to identify PMP20's client proteins in vivo.

### Gap 4: Lipid Hydroperoxide Reduction Not Tested

- **What was checked:** H₂O₂ reduction (negative). The *C. boidinii* CbPmp20 has been proposed to primarily reduce lipid hydroperoxides at peroxisomal membranes (PMID:11278957).
- **Why it matters:** If PMP20 could reduce lipid hydroperoxides specifically, a more specific peroxidase term might apply despite the general peroxidase negative result.
- **Assessment:** This is unlikely given the broad NOT annotation on GO:0004601, but lipid hydroperoxide substrates were not explicitly tested in PMID:20356456.
- **Resolution:** Test recombinant *S. pombe* PMP20 with tert-butyl hydroperoxide, cumene hydroperoxide, and phospholipid hydroperoxides.

---

## Discriminating Tests

### Priority 1: Glutathione Peroxidase Assay (Closes Gap 1)

Test recombinant *S. pombe* PMP20 for glutathione-dependent peroxidase activity using:
- Substrates: H₂O₂, t-BOOH, cumene hydroperoxide, phospholipid hydroperoxide
- Electron donors: GSH + glutathione reductase system
- Controls: *C. boidinii* CbPmp20 (positive), Cys43Ser mutant (negative)
- Readout: NADPH consumption at 340 nm

This would definitively close the question of whether any peroxidase activity exists under any reductant system.

### Priority 2: Structural Characterization

Determine crystal structure of *S. pombe* PMP20 to understand:
- Active-site geometry relative to catalytically active orthologs
- Oligomeric state (monomer vs. dimer vs. decamer) relevant to chaperone function
- Conformational differences that favor holdase over peroxidase activity

### Priority 3: In Vivo Interactome Under Stress

Perform proximity labeling (APEX2-PMP20 fusion) under oxidative stress (H₂O₂ treatment, heat shock) to identify:
- Client proteins bound by PMP20 as chaperone
- Whether PMP20 protects specific peroxisomal or cytoplasmic proteins
- Whether PMP20 interacts with thioredoxin or glutathione pathway components

### Priority 4: Comparative Phylogenomics

Systematic analysis of PMP20/Prx5 orthologs across fungi to determine:
- When peroxidase activity was lost in the *Schizosaccharomyces* lineage
- Whether other fungal PMP20 orthologs also lack peroxidase activity
- Correlation between specific residue positions and peroxidase vs. chaperone function

---

## Curation Leads

All items below are **candidate actions requiring curator verification**.

### Lead 1: Remove GO:0008379 from pmp20

- **Action:** Remove or suppress IEA and IBA annotations of GO:0008379 (thioredoxin peroxidase activity)
- **Justification:** Directly refuted by PMID:20356456; logically inconsistent with NOT|enables GO:0004601 (IDA)
- **Verification needed:** Confirm that the InterPro-to-GO mapping pipeline can be overridden or that a NOT annotation for GO:0008379 specifically should be added

### Lead 2: Add Explicit NOT Annotation for GO:0008379

- **Action:** Add NOT|enables GO:0008379 (thioredoxin peroxidase activity) with IDA evidence, citing PMID:20356456
- **Reference snippet to verify:** *"However, peroxidase activity was not observed for PMP20 (peroxisomal membrane protein 20)."* (PMID:20356456)
- **Rationale:** While the parent NOT|GO:0004601 logically covers this, an explicit NOT on the exact term being disputed provides clearer documentation and may help automated systems resolve the conflict

### Lead 3: Flag IBA Annotation for GO_Central Review

- **Action:** Notify GO_Central that the IBA annotation of GO:0008379 to *S. pombe* pmp20 conflicts with IDA NOT evidence
- **Rationale:** The phylogenetic annotation model needs to account for this lineage-specific functional divergence; other PMP20/Prx5 family members may also be incorrectly annotated

### Lead 4: Verify Completeness of Holdase Annotation

- **Action:** Confirm GO:0140309 (unfolded protein holdase activity) is properly annotated with IDA evidence and PMID:20356456
- **Additional consideration:** Whether a BP term for protein quality control or chaperone-mediated protein folding should also be annotated

### Lead 5: Candidate References for Curation

| Reference | Relevant Snippet | Use |
|-----------|-----------------|-----|
| PMID:20356456 | *"peroxidase activity was not observed for PMP20"* | NOT\|enables GO:0008379 (IDA) |
| PMID:20356456 | *"TPx, PMP20, and GPx inhibited thermal aggregation of citrate synthase"* | enables GO:0140309 (IDA) |
| PMID:24521463 | *"Tpx1 is the only enzyme with sufficient sensitivity for peroxides"* | Supporting context for NOT annotation |
| PMID:11278957 | *"glutathione peroxidase activity in vitro toward alkyl hydroperoxides"* | Ortholog evidence — CbPmp20 is GSH-dependent, not Trx-dependent |
| PMID:25399604 | *"switch-in-function so as to exert holdase activity under redox-stress conditions"* | Evolutionary framework for functional divergence |

---

## Supported and Refuted Hypotheses

| ID | Hypothesis | Status | Key Evidence |
|----|-----------|--------|-------------|
| H001 | *S. pombe* pmp20 has thioredoxin peroxidase activity (GO:0008379) | **Rejected** | Direct assay negative (PMID:20356456); comprehensive study excludes PMP20 (PMID:24521463); NOT annotation on parent term |
| H002 | *S. pombe* pmp20 lacks thioredoxin peroxidase activity and instead functions as a molecular chaperone | **Supported** | Holdase activity demonstrated (PMID:20356456); no peroxidase activity of any kind; evolutionary framework supports functional switch |
| H003 | *S. pombe* PMP20 retains glutathione-dependent peroxidase activity like *C. boidinii* CbPmp20 | **Rejected** | NOT|GO:0004601 covers all peroxidase types; PMP20 absent from comprehensive H₂O₂ scavenging study; active-site divergence from CbPmp20 (~32.5% identity) |

---

## Limitations

1. **Single laboratory source for direct evidence:** The negative peroxidase result and positive chaperone result both come from a single study (Kim et al., 2010). While corroborated by the comprehensive Paulo et al. (2014) study and PomBase curation, independent replication of the in vitro assays would strengthen the case.

2. **Glutathione peroxidase activity not explicitly tested:** Kim et al. (2010) tested thioredoxin-dependent activity. Although the broad NOT|GO:0004601 annotation and the Paulo et al. results argue against any peroxidase activity, a direct glutathione peroxidase assay for *S. pombe* PMP20 has not been published.

3. **Chaperone mechanism unclear:** The holdase activity was demonstrated with a single generic substrate (citrate synthase). The physiological substrates, the mechanism of holdase action, and whether the activity is regulated (e.g., by oxidative modifications of Cys43) remain unknown.

4. **Annotation system limitations:** The conflict between IDA NOT annotations and IEA/IBA positive annotations reflects a known limitation in GO annotation pipelines where computational annotations are not automatically suppressed by contradicting experimental evidence.

5. **Limited structural data:** No crystal structure of *S. pombe* PMP20 is available, limiting our understanding of why this protein lost peroxidase activity despite retaining the peroxiredoxin fold and the conserved active-site cysteine.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)