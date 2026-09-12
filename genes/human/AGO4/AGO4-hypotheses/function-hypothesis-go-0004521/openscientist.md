---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T16:25:05.494403'
end_time: '2026-07-06T16:57:13.562799'
duration_seconds: 1928.07
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: AGO4
  gene_symbol: AGO4
  uniprot_accession: Q9HCK5
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004521
  hypothesis_text: AGO4 has RNA endonuclease activity (GO:0004521).
  term_context: '- Term: RNA endonuclease activity (GO:0004521)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - file:human/AGO4/AGO4-deep-research-falcon.md'
  source_file: genes/human/AGO4/AGO4-ai-review.yaml
  source_selector: existing_annotations[3].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004521\n  label: RNA endonuclease activity\n\
    evidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 4
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
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
- filename: provenance_evidence_matrix.csv
  path: openscientist_artifacts/provenance_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
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
- **Gene directory:** AGO4
- **Gene symbol:** AGO4
- **UniProt accession:** Q9HCK5

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004521
- **Source file:** genes/human/AGO4/AGO4-ai-review.yaml
- **Source selector:** existing_annotations[3].function_hypothesis

## Seed Hypothesis

AGO4 has RNA endonuclease activity (GO:0004521).

## Term and Decision Context

- Term: RNA endonuclease activity (GO:0004521)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- file:human/AGO4/AGO4-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0004521
  label: RNA endonuclease activity
evidence_type: IBA
original_reference_id: GO_REF:0000033
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

Do not rely on literature alone. Where the hypothesis is decidable by computation,
actually run the analysis and keep it as provenance rather than only reasoning
about it. Match the analysis to the question, for example:

- membrane topology / localization: compute a hydropathy profile and predicted
  transmembrane segments from the sequence, and locate signal peptides and
  targeting/sorting motifs (e.g. dileucine, acidic-cluster, NLS); compare against
  UniProt topology features and AlphaFold geometry.
- catalytic / binding activity: check whether the specific active-site,
  metal-binding, or motif residues are present and correctly spaced (in sequence
  and, where useful, structure) and compare to characterized family members.
- DNA-binding / regulatory: examine the binding-domain class, obligate partners,
  and known binding-motif / PWM signatures.
- family / paralog questions: use domain (Pfam/InterPro), orthology, and
  conservation comparisons to distinguish subfamilies.

Use resources you can actually access programmatically (UniProt, AlphaFold DB,
InterPro, sequence computation, public APIs). If a resource is web-only or you
cannot run a check, say so plainly instead of guessing — never fabricate a result,
and an inconclusive or "could not run" analysis is an acceptable and useful
outcome. Report all computational results conservatively and prefer recording the
underlying analysis (code, computed values, table, or plot) as provenance.

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

# AGO4 RNA Endonuclease Activity (GO:0004521) — Hypothesis Deep Research Report

**Target gene:** AGO4 (Argonaute-4), *Homo sapiens* (NCBITaxon:9606)
**UniProt:** Q9HCK5 · **Term:** GO:0004521 "RNA endonuclease activity" · **Evidence:** IBA (GO_REF:0000033)
**Focus type:** function_assignment — does AGO4 directly have RNA-endonuclease (slicer) activity?

---

## Summary

The IBA-propagated annotation of **RNA endonuclease activity (GO:0004521)** to human AGO4 is **refuted / over-annotated** and should be removed or negatively qualified. Argonaute "slicer" activity is a metal-dependent, RNase-H-like reaction carried out by the PIWI domain, and it strictly requires an intact catalytic tetrad of four residues (the DEDH tetrad: Asp-Glu-Asp-His) that coordinate two catalytic Mg²⁺ ions. Direct sequence analysis anchored on the experimentally validated human AGO2 catalytic residues (D597/E637/D669/H807) shows that human AGO4 has **two of the four catalytic residues non-conservatively substituted**: the catalytic aspartate (AGO2 Asp669) is a **glycine (Gly671)** in AGO4, and the catalytic histidine (AGO2 His807) is an **arginine (Arg809)**. Loss of either residue is sufficient to abolish catalysis; AGO4 has lost both. AGO4 therefore cannot perform RNA-guided endonucleolytic cleavage.

This computational conclusion is independently corroborated by database curation and primary literature. UniProt annotates catalytic Mg²⁺-coordinating binding sites for AGO2 (597/669/807) and AGO3 (598/638/670/808) but **none** for AGO4 (or AGO1). The primary RNAi literature consistently establishes that among the four human paralogs only **AGO2** is a constitutive slicer, with **AGO3** added later as a conditional slicer; **AGO1, AGO3, and AGO4 were classically defined as slicer-independent effectors**, and non-AGO2 paralogs had to be *engineered* to become catalytically active. AGO4's genuine molecular role is as a slicer-independent miRNA effector that silences targets by recruiting the TNRC6/GW182 machinery, which drives translational repression and deadenylation-coupled mRNA decay — a mechanism that does not require endonucleolytic cleavage.

The single important caveat: the IBA annotation is technically defensible in the narrow phylogenetic sense that AGO4 descends from an ancestral Argonaute that had endonuclease activity and still adopts the PIWI fold. But GO annotation should reflect the **actual molecular function of the specific gene product**. By that standard AGO4 is a pseudo-catalytic, structurally slicer-dead paralog, and the annotation is a classic case of **paralog over-annotation via phylogenetic propagation** from the active AGO2 lineage.

---

## Key Findings

### Finding 1 — AGO4 lacks the intact DEDH catalytic tetrad required for slicer activity

The defining requirement for Argonaute endonuclease/slicer activity is a catalytic tetrad arranged within the RNase-H-like PIWI domain that together coordinate two catalytic Mg²⁺ ions and perform phosphodiester-bond hydrolysis of the target RNA. In human AGO2 — the one mammalian Argonaute unambiguously demonstrated to be an active slicer — these residues are **Asp597, Glu637, Asp669, and His807** (the "DEDH" tetrad).

A global (Needleman–Wunsch) alignment of human AGO2 (Q9UKV8) against its three paralogs, anchored on these positions, gives:

| Paralog | UniProt | Res 1 (AGO2 D597) | Res 2 (AGO2 E637) | Res 3 (AGO2 D669) | Res 4 (AGO2 H807) | Tetrad status | Native slicer? |
|---|---|---|---|---|---|---|---|
| **AGO2** | Q9UKV8 | **D**597 | **E**637 | **D**669 | **H**807 | **D-E-D-H** intact | Yes (validated positive control) |
| **AGO3** | Q9H9G7 | **D**598 | **E**638 | **D**670 | **H**808 | **D-E-D-H** intact | Conditionally yes (Park 2017) |
| **AGO1** | (paralog) | D | E | D | **R805** | D-E-D-**R** broken | No |
| **AGO4** | Q9HCK5 | D589 | E629 | **G671** | **R809** | D-E-**G**-**R** broken | **No** |

The two critical AGO4 substitutions are visible in clean, ungapped alignment windows:

- **Catalytic Asp → Gly:** AGO2 `IFYRDGVSE` vs AGO4 `IYYRGGVSE` — the catalytic aspartate (D669) aligns to a **glycine** in AGO4.
- **Catalytic His → Arg:** AGO2 `AYYAHLVAF` vs AGO4 `AYYARLVAF` — the catalytic histidine (H807) aligns to an **arginine** in AGO4.

Both substitutions are non-conservative and hit residues individually essential for the two-metal-ion mechanism. The catalytic aspartate is a direct metal ligand; replacing it with side-chain-less glycine removes a required coordinating carboxylate. The catalytic histidine positions/activates the nucleophilic water and stabilizes the transition state; replacing it with arginine alters charge, geometry, and hydrogen-bonding capacity. AGO4 is **79.7% identical** to AGO2 overall, so these are specific, functionally consequential changes at otherwise strongly conserved catalytic positions — not divergence in an unconserved region. The intact AGO3 tetrad, sitting in the same alignment as a positive family control, sharpens the contrast: the loss is AGO4-specific.

### Finding 2 — UniProt independently annotates catalytic Mg²⁺-binding sites for AGO2/AGO3 but not for AGO4

As an orthogonal cross-check, the UniProt feature tables were compared across paralogs. UniProt annotates Mg²⁺-coordinating catalytic binding sites for AGO2 (positions 597, 669, 807) and AGO3 (positions 598, 638, 670, 808), consistent with those two proteins retaining the tetrad. UniProt annotates **no** catalytic binding sites for AGO4 (Q9HCK5) or AGO1. This database-level curation fully matches the de novo alignment and reflects the community consensus that AGO4 is not a metal-dependent nuclease.

### Finding 3 — Primary literature consistently classifies AGO4 as slicer-independent

Three independent primary papers converge on the conclusion that AGO4 is not a catalytically active slicer:

- **AGO2 is the sole constitutive mammalian slicer.** Liu et al. established that of the mammalian Argonautes, "a single mammalian family member, Argonaute2, [is] responsible for messenger RNA cleavage activity" [PMID: 15284456](https://pubmed.ncbi.nlm.nih.gov/15284456/). This directly argues against endonuclease activity in AGO4.
- **AGO4 explicitly described as slicer-independent.** Park et al. state that "Of the four human Argonaute (AGO) paralogs, only AGO2 has been shown to have slicer activity. The others (AGO1, AGO3 and AGO4) have been thought to assemble with microRNAs to form slicer-independent effector complexes" [PMID: 29040713](https://pubmed.ncbi.nlm.nih.gov/29040713/). Critically, this paper adds **AGO3** (not AGO4) as a newly demonstrated conditional slicer — AGO4 remains slicer-independent.
- **Non-AGO2 paralogs must be engineered to become active.** Hauptmann et al. "mutated inactive human Ago1 and Ago3 and generated catalytic Argonaute proteins" [PMID: 23665583](https://pubmed.ncbi.nlm.nih.gov/23665583/), showing that catalytic activity had to be *restored by engineering* — confirming the non-AGO2 paralogs are natively inactive. AGO4 was not among the rescued set.

### Finding 4 — AGO4's actual effector mechanism is nuclease-independent silencing via TNRC6/GW182

AGO4's functional role in the miRNA pathway does not depend on endonuclease activity. Lazzaretti et al. showed that all four human Argonautes (AGO1–AGO4) recruit the GW182/TNRC6 family, and that the TNRC6 proteins execute silencing through their C-terminal silencing domains — *independently* of Argonaute catalysis — by promoting translational repression and mRNA deadenylation/decay [PMID: 19383768](https://pubmed.ncbi.nlm.nih.gov/19383768/). This provides a coherent, catalysis-free mechanistic account of AGO4-mediated silencing and removes any functional necessity for AGO4 to be a slicer.

---

## Mechanistic Model / Interpretation

The Argonaute PIWI domain adopts an **RNase-H-like fold**; when the DEDH tetrad is intact it performs guide-directed, two-metal-ion endonucleolytic cleavage ("slicing") of a complementary target RNA. AGO4 retains the fold and can bind a miRNA guide and base-pair with targets, but its catalytic center is structurally incomplete:

```
       Guide RNA (miRNA)
             |
   5'........XXXXXXXXX........3'   target mRNA
             |||||||||
        [ PIWI domain ]
         D--E--D--H   <-- catalytic tetrad coordinates 2x Mg2+
             \  |  /
              Mg2+ Mg2+  --> phosphodiester hydrolysis (SLICING)

 AGO2:  D597 - E637 - D669 - H807   => INTACT  => active slicer
 AGO3:  D598 - E638 - D670 - H808   => INTACT  => conditional slicer
 AGO1:  D    - E    - D    - R805   => His->Arg => DEAD
 AGO4:  D589 - E629 - G671 - R809   => Asp->Gly + His->Arg => DEAD
```

Because the two-metal-ion mechanism requires the full complement of coordinating side chains, the AGO4 active site cannot assemble a competent catalytic center. AGO4 instead functions as a **structurally slicer-dead effector**:

```
   AGO4 (slicer-dead) + miRNA  ->  binds target mRNA
                     |
                 recruits TNRC6/GW182 (via GW-binding surface)
                     |
        TNRC6 C-terminal silencing domain
                     |
        translational repression + deadenylation/decay
                     |
              GENE SILENCING (no endonucleolytic cut)
```

This model reconciles all four findings: the missing catalytic residues (F1), the absent UniProt catalytic-site annotations (F2), the literature classification as slicer-independent (F3), and the demonstrated nuclease-independent silencing route (F4). The GO:0004521 annotation is best explained as an artifact of **phylogenetic (IBA) propagation** from an ancestral/AGO2 catalytic function, applied without accounting for the paralog-specific loss of catalytic residues in the AGO4 lineage.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limits |
|---|---|---|---|---|---|---|
| This analysis (provenance) | Structural/evolutionary (computational) | **Refutes** | AGO4 retains the DEDH catalytic tetrad | AGO4 tetrad = D589-E629-**G671**-**R809**; catalytic Asp→Gly and His→Arg vs active AGO2 D-E-D-H; AGO3 intact (D598-E638-D670-H808) as positive control; 79.7% identity to AGO2 | Full-length human AGO1–4 (UniProt); NW alignment | High for the two clean, ungapped substitutions; pairwise (not full MSA) |
| UniProt Q9HCK5 / Q9UKV8 / Q9H9G7 | Review/database | **Refutes** | AGO4 has an annotated catalytic center | Catalytic Mg²⁺-coordinating sites annotated for AGO2 (597/669/807) and AGO3 (598/638/670/808) but **none for AGO4** (or AGO1) | Curated database features | Database-level curator judgement, not an assay |
| [PMID: 15284456](https://pubmed.ncbi.nlm.nih.gov/15284456/) | Direct assay / genetics | **Refutes** | Which mammalian Argonaute cleaves mRNA | "a single mammalian family member, Argonaute2, being responsible for messenger RNA cleavage activity" | Mammalian RNAi biochemistry | Seminal; conclusion durable |
| [PMID: 29040713](https://pubmed.ncbi.nlm.nih.gov/29040713/) | Direct assay + structure | **Refutes / qualifies** | AGO4 has slicer activity | Only AGO2 shown to slice; AGO1/AGO3/AGO4 "slicer-independent"; adds AGO3 (not AGO4) as active | Recombinant human AGO cleavage assays | AGO4 not shown active anywhere |
| [PMID: 23665583](https://pubmed.ncbi.nlm.nih.gov/23665583/) | Mutant/engineering | **Qualifies** | Non-AGO2 AGOs are intrinsically active | Inactive Ago1/Ago3 had to be mutated to generate catalytic enzymes | Human AGO1/AGO3 | AGO4 not among rescued set |
| [PMID: 19383768](https://pubmed.ncbi.nlm.nih.gov/19383768/) | Interaction / cell assay | **Qualifies (alt. function)** | AGO4's real mechanism | AGO1–AGO4 recruit TNRC6/GW182 → silencing by translational repression + deadenylation, independent of AGO catalysis | Human cells, tethering | Supports non-endonucleolytic role |

---

## GO Curation Implications (leads — require curator verification)

- **Lead action:** Do **not** retain GO:0004521 (RNA endonuclease activity) as a direct molecular-function annotation for AGO4. The IBA propagation is contradicted by AGO4's own sequence/structure and by UniProt, and should be **removed or marked `NOT`** for this gene. If the pipeline retains IBA statements, flag this one as an over-annotation contradicted by sequence and database evidence.
- **Better-supported MF terms:** RNA binding (**GO:0003723**) and/or miRNA binding (**GO:0035198**) — AGO4 binds small-RNA guides and recognizes targets by base pairing.
- **Better-supported BP terms:** gene silencing by miRNA (**GO:0035195**) / post-transcriptional gene silencing (**GO:0016441**) via translational repression and deadenylation — **not** slicing-based cleavage.
- **Well-supported CC terms:** RISC complex (**GO:0016442**) / cytoplasmic ribonucleoprotein granule (P-body).
- Preserve the key distinction: AGO4 is a **non-catalytic** RISC/effector subunit. Avoid defaulting to "protein binding" (GO:0005515) when RNA/miRNA-binding and silencing terms are supported.

---

## Mechanistic Scope

The **immediate molecular activity under test** is RNA-guided phosphodiester-bond hydrolysis (slicing) by the PIWI (RNase-H-like) domain, requiring the DEDH tetrad plus two catalytic Mg²⁺. AGO4 lacks two of these residues → the direct activity is **absent**.

It is important to separate:

- **Direct activity tested, absent:** endonucleolytic RNA cleavage / slicing.
- **Direct activity present (not the term under review):** miRNA-guide binding and target-mRNA recognition.
- **Downstream / pathway consequence (present):** target-mRNA silencing — but executed via TNRC6/GW182-recruited translational repression and deadenylation-coupled decay, not by AGO4 catalysis.
- **Not applicable:** organismal loss-of-function phenotypes of AGO4 are downstream and cannot be used to infer catalytic activity.

Even where AGO4 contributes to "RNA degradation" at the pathway level, that degradation is performed by downstream deadenylases/decay machinery recruited via TNRC6 — not by AGO4 endonuclease chemistry.

---

## Conflicts and Alternatives

- **Paralog carry-over / frequency bias (most likely source):** The IBA is driven by the well-characterized AGO2 slicer and the shared Argonaute/PIWI domain. Catalytic competence does not transfer to all paralogs; this is the classic paralog-overannotation pattern.
- **AGO3 nuance:** AGO3 *does* retain the tetrad and has guide-dependent slicer activity ([PMID: 29040713](https://pubmed.ncbi.nlm.nih.gov/29040713/)) — so "all AGOs except AGO2 are inactive" is itself too strong. But AGO3's intact tetrad is exactly what AGO4 lacks, which *sharpens* (not weakens) the AGO4 conclusion.
- **AGO1 comparison:** AGO1 also loses the catalytic His (His→Arg805) and is likewise slicer-inactive (rescuable only by engineering, [PMID: 23665583](https://pubmed.ncbi.nlm.nih.gov/23665583/)) — a consistent picture.
- **Fold retention ≠ catalysis:** AGO4 retains the PIWI/RNase-H fold and binds RNA, which may superficially justify an "endonuclease-fold" call. GO:0004521 asserts *activity*, not fold; the fold is present while the chemistry is not.
- **In vitro vs in vivo:** No primary study reports native AGO4 endonuclease activity; there is no positive experimental evidence to weigh against the refuting sequence/database evidence. No isoform/organism artifact was found that would rescue AGO4 activity.

---

## Limitations and Knowledge Gaps

1. **Sequence-based inference, not a direct AGO4 enzyme assay.** *Checked:* alignment against validated AGO2 residues + UniProt cross-check. *Why it matters:* GO curation ideally rests on a direct assay. *Resolution:* a reconstituted in vitro slicer assay with purified guide-loaded AGO4 on a fully complementary target (as done for AGO3 in PMID 29040713).
2. **No structural active-site superposition was executed as provenance.** *Checked:* residue identity/spacing in sequence only. *Why it matters:* an AlphaFold/PDB superposition on AGO2 would confirm geometric disruption and rule out compensatory rearrangement. *Resolution:* superpose AlphaFold Q9HCK5 onto AGO2 (e.g., PDB 4W5N/4F3T) and score catalytic-pocket geometry.
3. **AGO4 not directly rescued in engineering studies.** PMID 23665583 restored Ago1/Ago3 but did not report a catalytic-AGO4 mutant, leaving open (though unlikely) additional catalysis-blocking features beyond the tetrad. *Resolution:* engineer AGO4 back-mutations (Gly671→Asp, Arg809→His) and assay.
4. **Non-slicer nuclease activities not formally excluded.** GO:0004521 is broader than "slicer." *Checked:* only slicer-relevant residues. *Why it matters:* AGO4 could in principle have a distinct non-canonical RNA-cleaving activity. *Resolution:* biochemical nuclease screen. No literature supports any such activity for AGO4.
5. **Nuclear / non-canonical AGO4 roles** (reported nuclear and interferon-related functions) were not exhaustively mined; none are expected to require intrinsic endonuclease activity.

Analytical limitations: pairwise NW alignment (not a full MSA); catalytic-residue identity taken from the established hAGO2 D597/E637/D669/H807 tetrad; database annotations are curator-level. None of these weaken the core conclusion, which rests on two non-conservative substitutions in clean, ungapped alignment blocks.

---

## Proposed Follow-up Experiments / Actions

**Discriminating experiments**

1. **Reconstituted slicer assay (definitive):** purify guide-loaded human AGO4, incubate with a 5′-labeled fully complementary target RNA + Mg²⁺, assay for site-specific cleavage. Include AGO2 positive control and an AGO4 "restored-tetrad" (Gly671→Asp, Arg809→His) mutant. Expected: AGO2 cleaves, wild-type AGO4 does not.
2. **Structural active-site superposition (fast, computational):** align AlphaFold AGO4 (Q9HCK5) onto AGO2 catalytic PIWI structure; quantify absence/displacement of catalytic carboxylate and imidazole. Provenance-friendly and directly on-point.
3. **Gain-of-function engineering:** test whether the AGO4 double back-mutant (± N-terminal AGO2 elements) gains slicer activity, mirroring the AGO1/AGO3 engineering logic.
4. **Comparative paralog panel:** run AGO1/AGO2/AGO3/AGO4 side by side to demonstrate the AGO2(+)/AGO3(conditional)/AGO1,AGO4(–) pattern predicted by the tetrad analysis.

**Curation actions (leads to verify)**

- Remove / do-not-propagate GO:0004521 IBA on AGO4; consider a `NOT GO:0004521` annotation to record the tested-and-absent activity.
- Add/retain better-supported terms: MF GO:0003723 / GO:0035198; BP GO:0035195 / GO:0016441; CC GO:0016442.
- **Candidate snippets to cite (verify verbatim):**
  - PMID 29040713: *"Of the four human Argonaute (AGO) paralogs, only AGO2 has been shown to have slicer activity. The others (AGO1, AGO3 and AGO4) have been thought to assemble with microRNAs to form slicer-independent effector complexes."*
  - PMID 15284456: *"a single mammalian family member, Argonaute2, being responsible for messenger RNA cleavage activity."*
  - PMID 23665583: *"we have mutated inactive human Ago1 and Ago3 and generated catalytic Argonaute proteins."*

---

## Conclusion

Human AGO4 does **not** have RNA endonuclease (slicer) activity. Its PIWI catalytic tetrad is disrupted at two of four positions (catalytic Asp669→Gly671 and His807→Arg809 relative to active AGO2 D-E-D-H), UniProt annotates no catalytic metal-binding sites for AGO4, and primary literature consistently classifies AGO4 as a slicer-independent miRNA effector that silences targets through TNRC6/GW182-mediated translational repression and mRNA decay. The GO:0004521 IBA annotation is a paralog over-annotation propagated from ancestral/AGO2 catalytic function and should be **removed or `NOT`-qualified**, with AGO4's molecular function better captured by RNA/miRNA-binding, RISC-component, and miRNA-mediated-silencing terms.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.csv)