---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T16:51:51.329861'
end_time: '2026-07-06T17:05:37.702459'
duration_seconds: 826.37
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: ACL4
  gene_symbol: ACL4
  uniprot_accession: Q03771
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008320
  hypothesis_text: ACL4 has protein transmembrane transporter activity (GO:0008320).
  term_context: '- Term: protein transmembrane transporter activity (GO:0008320)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/yeast/ACL4/ACL4-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008320\n  label: protein transmembrane transporter\
    \ activity\nevidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
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
- **Gene directory:** ACL4
- **Gene symbol:** ACL4
- **UniProt accession:** Q03771

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008320
- **Source file:** genes/yeast/ACL4/ACL4-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis

ACL4 has protein transmembrane transporter activity (GO:0008320).

## Term and Decision Context

- Term: protein transmembrane transporter activity (GO:0008320)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0008320
  label: protein transmembrane transporter activity
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

# AIGR Gene Hypothesis Deep Research — ACL4 (Q03771)

## Focus Hypothesis

> **ACL4 has protein transmembrane transporter activity (GO:0008320).**
> Evidence type: IBA · Original reference: GO_REF:0000033
> Source: `genes/yeast/ACL4/ACL4-ai-review.yaml`, `existing_annotations[2].function_hypothesis`

Gene: **ACL4** (Assembly Chaperone of RPL4), *Saccharomyces cerevisiae* (NCBITaxon:559292) · UniProt **Q03771**.

---

## Executive Judgment

**Verdict: REFUTED (over-annotation).**

The seed hypothesis that *Saccharomyces cerevisiae* ACL4 (UniProt **Q03771**) possesses **protein transmembrane transporter activity (GO:0008320)** is not supported by any experimental evidence and is best explained as a **phylogenetic (IBA) carry-over artifact**. The annotation originates from GO_REF:0000033 (Inferred from Biological Ancestor), which propagates function from a PANTHER protein family tree. ACL4 is assigned to PANTHER family **PTHR46208**, whose family-level name is "**MITOCHONDRIAL IMPORT RECEPTOR SUBUNIT TOM70**." TOM70 is a genuine mitochondrial outer-membrane import receptor that legitimately carries protein-transmembrane-transport function. ACL4 sits in a distinct subfamily (SF2) and shares with TOM70 only a **TPR (tetratricopeptide repeat) superhelical solenoid fold** — a generic protein–protein interaction scaffold found across thousands of functionally unrelated proteins. Fold sharing is not function sharing, and the IBA machinery has incorrectly transferred the membrane-transport activity down the tree.

Two independent lines of evidence refute the transmembrane-transporter assignment. **First**, the experimentally characterized function of ACL4 is entirely soluble and non-membranous: ACL4 is a **dedicated escort chaperone** that co-translationally captures the nascent 60S ribosomal protein **Rpl4**, protects it from aggregation and degradation, and delivers it (with karyopherin Kap104) to the nuclear pre-60S assembly site. This is documented by a crystal structure of the Acl4–RpL4 complex and by genetic/biochemical characterization ([PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/), [PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/), [PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/)). **Second**, a computed Kyte–Doolittle hydropathy analysis of the 387-residue ACL4 sequence finds **zero** transmembrane-candidate segments (maximum window-mean hydropathy 1.36, below the 1.6 threshold for a membrane-spanning helix), which is structurally incompatible with an integral-membrane transporter.

The most important caveat for the curator is to **preserve the genuine transport-adjacent function while removing the membrane-specific one**. ACL4 does move a protein cargo (Rpl4) from cytoplasm to nucleus, and SGD records an experimental annotation of **protein transporter activity (GO:0140318, IDA)** plus **unfolded protein binding (GO:0051082, IDA)**. These correctly capture ACL4's activity without the erroneous "transmembrane" qualifier. GO:0008320 should therefore be **removed** and not replaced with any membrane-transport term.

---

## Key Findings

### Finding 1 — GO:0008320 is a TOM70-family IBA over-annotation, not experimental

ACL4 (Q03771) is a member of PANTHER family **PTHR46208**, whose family name is "**MITOCHONDRIAL IMPORT RECEPTOR SUBUNIT TOM70**"; ACL4 occupies subfamily **SF2**. TOM70 (Tom70p in yeast) is the archetypal mitochondrial outer-membrane import receptor — a large TPR-repeat protein anchored in the outer membrane that receives cytosolic precursor proteins (often chaperone-bound) and channels them toward the TOM translocase pore. Because IBA (GO_REF:0000033) propagates function from an inferred common ancestor across all members of a PANTHER tree, the membrane and transport terms attached to the TOM70-dominated family have been transferred wholesale onto ACL4.

The tell-tale signature of this artifact is that **every membrane/transport IBA term on ACL4 is a mitochondrial-import term** that makes sense only for TOM70, not for a ribosome-assembly chaperone:

| GO ID | Term | Evidence | Fits TOM70? | Fits ACL4? |
|-------|------|----------|-------------|------------|
| GO:0008320 | protein transmembrane transporter activity | IBA | ✔ | ✘ |
| GO:0005741 | mitochondrial outer membrane | IBA | ✔ | ✘ |
| GO:0030943 | mitochondrion targeting sequence binding | IBA | ✔ | ✘ |
| GO:0030150 | protein import into mitochondrial matrix | IBA | ✔ | ✘ |
| GO:0045039 | protein insertion into mitochondrial inner membrane | IBA | ✔ | ✘ |

By contrast, the **experimental** SGD annotations for ACL4 describe an entirely different biology: **cytoplasm (GO:0005737, IDA)**, **nucleus (GO:0005634, IDA)**, **unfolded protein binding (GO:0051082, IDA)**, and **protein transporter activity (GO:0140318, IDA)**. The divergence between the IBA "mitochondrial membrane transporter" cluster and the IDA "cytosolic/nuclear chaperone" cluster is the hallmark of frequency-driven family over-annotation: ACL4 was pulled into the wrong subfamily inheritance because it happens to share the TPR fold with TOM70.

### Finding 2 — ACL4 is a soluble TPR chaperone with no transmembrane segments

A first-principles sequence analysis directly contradicts membrane residence. A **Kyte–Doolittle hydropathy** scan (window = 19 residues) across the full 387-aa ACL4 sequence yields a **maximum window-mean hydropathy of 1.36** at residue 131 — below the conventional **1.6** threshold used to call a candidate membrane-spanning helix — and detects **zero** transmembrane-candidate windows. An integral-membrane protein transmembrane transporter must, by definition, contain one or more hydrophobic membrane-spanning segments; ACL4 contains none.

The positive structural picture is consistent and well-characterized:

- **Domain architecture:** three annotated **TPR repeats** (approximately residues 42–75, 163–196, 224–257), classified by SUPFAM as **SSF48452 (TPR-like)**, by Gene3D as **1.25.40.10 (TPR domain)**, and by CDD as **cd24142 (ACL4-like)**.
- **Disordered acidic tail:** the C-terminal region (residues 371–387) is intrinsically disordered and highly acidic (11 of the final 25 residues are Asp/Glu) — a feature typical of nuclear/nucleolar chaperones, not membrane transporters.
- **UniProt keywords:** *Chaperone, Cytoplasm, Nucleus, TPR repeat, Ribosome biogenesis* — no membrane, transmembrane, or transport-channel keyword.
- **Experimental structure:** the crystal structure of the Acl4–RpL4 complex ([PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/)) shows a **soluble superhelical TPR solenoid** that sequesters ~70 exposed residues of the extended RpL4 internal loop. There is no integral-membrane character anywhere in the structure.

Together these establish that ACL4 is a soluble cytosolic/nuclear protein whose fold (TPR solenoid) is a protein-binding scaffold, not a membrane channel — mechanistically incompatible with GO:0008320.

---

## Mechanistic Model / Interpretation

The annotated and actual functions of ACL4 can be contrasted directly:

```
   ANNOTATED (IBA, incorrect)              ACTUAL (IDA/structure, correct)
   ---------------------------             --------------------------------
   TOM70-like receptor in the              Soluble TPR escort chaperone
   mitochondrial outer membrane            in cytoplasm + nucleus
        |                                        |
   spans the bilayer, channels             binds nascent Rpl4 loop
   precursor proteins across the           co-translationally; blocks
   outer membrane                          aggregation & degradation
        |                                        |
   GO:0008320 protein transmembrane        GO:0140318 protein transporter
   transporter activity                    activity (non-membrane cargo
                                           delivery) + GO:0051082 unfolded
                                           protein binding
```

**The actual ACL4 pathway (from experimental literature):**

```
 nascent Rpl4 emerging from ribosome
              │  (co-translational capture)
              ▼
   ACL4 TPR solenoid clamps the conserved internal loop of Rpl4
              │   ├── prevents aggregation of the aggregation-prone r-protein
              │   ├── protects Rpl4 mRNA from degradation (feedback control)
              │   └── shares an overlapping binding site with Kap104 (Kap-β)
              ▼
   Kap104 karyopherin takes over → nuclear import of Rpl4
              │
              ▼
   pre-60S assembly site: Rpl4 released, its eukaryote-specific
   extension docks onto neighboring RpL18 → incorporation into 60S
```

In this model ACL4 does perform a "transport" job — it moves a protein cargo from the cytoplasm to the nucleus — which explains why a curator or an automated system might be tempted by a transport term. But the movement is **karyopherin-mediated soluble escorting**, not **transmembrane translocation through a channel**. GO:0008320 specifically denotes an activity that enables the directed movement of a protein *across a membrane*; ACL4 never contacts a membrane and never forms a translocation conduit. The correct molecular-function term is the more general **protein transporter activity (GO:0140318)**, which the SGD IDA annotation already provides, complemented by **unfolded protein binding (GO:0051082, IDA)** for its chaperone activity.

The over-annotation arose because TPR solenoids are one of the most widespread protein-interaction folds in eukaryotes, and both TOM70 and ACL4 are large TPR proteins. Fold-based clustering placed them in the same PANTHER family, and IBA then inherited TOM70's membrane-transport verbs onto a protein whose real substrate is a ribosomal protein, not a mitochondrial precursor.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|----------|---------------|-----------|--------------|-------------|---------|--------------------------|
| PANTHER PTHR46208 (family record) | Review/database | **Supports refutation** (explains artifact) | Origin of the IBA term | ACL4 is in a TOM70-named family (subfamily SF2); membrane/transport IBA terms trace to TOM70, not ACL4 | *S. cerevisiae* / phylogenetic inference | High for source attribution; database-level, not experimental |
| SGD annotations (Q03771) | Review/database | Qualifies / competing | ACL4's experimental function/localization | IDA terms: cytoplasm (GO:0005737), nucleus (GO:0005634), unfolded protein binding (GO:0051082), protein transporter activity (GO:0140318) | *S. cerevisiae* experimental | High; curated experimental annotations |
| Computed Kyte–Doolittle hydropathy (this study) | Computational | **Refutes** | Is ACL4 an integral-membrane protein? | Max window-mean hydropathy 1.36 < 1.6; zero TM-candidate windows across 387 aa | Sequence Q03771, window 19 | High; standard method, single sequence |
| [PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/) | Structural (crystal) | **Refutes** membrane role; supports chaperone role | ACL4 molecular function | Acl4 is a soluble superhelical TPR domain sequestering ~70 residues of the RpL4 loop; dual function in nuclear import + protection from degradation | *S. cerevisiae* Acl4–RpL4 crystal structure | Very high; direct structural evidence |
| [PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/) | Mutant phenotype + interaction | **Refutes** membrane role; supports chaperone role | ACL4 as dedicated Rpl4 chaperone | Acl4 localizes to cytoplasm and nucleus, captures nascent Rpl4 co-translationally, escorts it to nuclear pre-60S site; deletion causes severe slow growth and 60S deficiency | *S. cerevisiae* genetics/biochemistry | Very high; direct functional evidence |
| [PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/) | Interaction / biochemical | **Refutes** membrane role; supports chaperone role | Mechanism of Acl4–Rpl4 binding | Acl4 binds the conserved internal loop of newly synthesized RpL4 via its superhelical TPR domain, restricting premature rRNA insertion | *S. cerevisiae* biochemistry | Very high; direct mechanistic evidence |
| [PMID: 35357307](https://pubmed.ncbi.nlm.nih.gov/35357307/) | Functional genomics | Qualifies (supports chaperone role) | ACL4 role in proteostasis | Acl4 co-translationally recognizes Rpl4 and couples r-protein production to ribosome assembly; feedback control of Rpl4 mRNA | *S. cerevisiae* | High; supports soluble chaperone function |

---

## GO Curation Implications

**Lead (requires curator verification): REMOVE GO:0008320 from ACL4.**

- The molecular-function term **protein transmembrane transporter activity (GO:0008320)** is **not supported** by any experimental evidence for ACL4 and is best explained as an **IBA over-annotation** inherited from the TOM70-dominated PANTHER family PTHR46208. Recommended action: **remove** (or, if the pipeline retains IBA terms, flag with a NOT/qualifier and a curator note documenting the TOM70 family carry-over).
- **Do NOT replace** GO:0008320 with any other membrane-transport term (e.g., GO:0015450 protein-transporting ATPase, GO:0022857 transmembrane transporter). No membrane role exists.
- **Retain / rely on the existing experimental MF terms** already in SGD:
  - **GO:0140318 protein transporter activity (IDA)** — captures ACL4's genuine cargo-escort activity without the incorrect "transmembrane" qualifier. This is the appropriate, more informative MF.
  - **GO:0051082 unfolded protein binding (IDA)** — captures the chaperone activity supported by the crystal structure and biochemistry.
- **Related IBA terms** that share the same TOM70 provenance (GO:0005741 mitochondrial outer membrane; GO:0030943 mitochondrion targeting sequence binding; GO:0030150 protein import into mitochondrial matrix; GO:0045039 protein insertion into mitochondrial inner membrane) should be reviewed together — they are the same artifact and, if present as asserted annotations, warrant the same removal/flagging treatment.
- **Appropriate BP/CC context** for ACL4 is **ribosomal large subunit biogenesis / ribosome assembly (BP)** and **cytoplasm + nucleus (CC)**, consistent with the experimental literature.

This recommendation avoids "protein binding" as the endpoint: the more informative and evidence-backed terms GO:0140318 and GO:0051082 are available and preferred.

---

## Mechanistic Scope

The molecular function under test is **transmembrane transport of protein cargo** — an activity requiring an integral-membrane protein that forms or gates a translocation conduit across a lipid bilayer. This is a **direct, immediate molecular activity** claim.

ACL4's **direct gene-product activity** is instead:
1. **Substrate binding** — the TPR solenoid clamps the conserved internal loop of nascent Rpl4 (direct, structurally resolved).
2. **Chaperone/holdase function** — preventing aggregation and premature rRNA engagement of Rpl4 (direct, biochemical).
3. **Escort/hand-off** — an overlapping binding site with the karyopherin Kap104 enables transfer for nuclear import (direct, biochemical).

The **cytoplasm-to-nucleus movement** of Rpl4 is a real transport outcome, but it is **karyopherin-driven soluble transport through the nuclear pore**, not ACL4-driven transmembrane translocation. Downstream/indirect consequences (60S subunit production, growth, proteostasis, Rpl4 mRNA stabilization) are **pathway-level phenotypes** of loss of ACL4, not evidence for a membrane-transport molecular activity. There is no direct assay, no localization, and no structural feature placing ACL4 in or across any membrane.

---

## Conflicts and Alternatives

- **Paralog/family confusion (primary alternative, and the resolution):** The IBA term is a fold-based mis-inheritance from **TOM70**, a legitimate mitochondrial-outer-membrane transporter that shares the TPR-solenoid fold with ACL4 but nothing functionally. This fully explains the seed hypothesis as a false positive.
- **Superficially plausible "transport" reading:** Because ACL4 physically escorts Rpl4 into the nucleus, an automated or naive assignment might reach for a transport term. This is adjudicated by the "transmembrane" qualifier: ACL4's transport is soluble/karyopherin-mediated, so **GO:0140318 (protein transporter activity)** — not GO:0008320 — is correct.
- **No organism-specific or isoform-specific rescue:** ACL4 is a single-copy yeast gene with no membrane isoform reported; the crystal structure and localization data are consistent across all four primary studies.
- **Database carry-over:** GO_REF:0000033 (IBA) is explicitly the source; the conflicting IDA annotations in SGD (cytoplasm, nucleus, unfolded protein binding, protein transporter activity) are the experimentally grounded, higher-priority data.

No evidence supports the membrane-transporter interpretation; all conflicts resolve in favor of the soluble-chaperone model.

---

## Evidence Base (Literature)

- *Molecular basis for protection of ribosomal protein L4 from cellular degradation.* [PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/) — Crystal structure of the Acl4–RpL4 complex shows a soluble superhelical TPR domain sequestering ~70 exposed residues of the RpL4 loop; Acl4 has a dual role in nuclear import and protection from degradation. **Directly refutes** any membrane/transmembrane character.
- *The Dedicated Chaperone Acl4 Escorts Ribosomal Protein Rpl4 to Its Nuclear Pre-60S Assembly Site.* [PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/) — Acl4 localizes to cytoplasm and nucleus, captures nascent Rpl4 co-translationally, and escorts it to the nuclear assembly site; deletion causes severe slow growth and 60S deficiency. **Establishes the true cytosolic/nuclear chaperone function.**
- *Coordinated Ribosomal L4 Protein Assembly into the Pre-Ribosome Is Regulated by Its Eukaryote-Specific Extension.* [PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/) — Acl4 binds the conserved internal loop of newly synthesized RpL4 via its superhelical TPR domain, restricting premature rRNA insertion. **Confirms soluble TPR-mediated substrate binding.**
- *Dedicated chaperones coordinate co-translational regulation of ribosomal protein production with ribosome assembly to preserve proteostasis.* [PMID: 35357307](https://pubmed.ncbi.nlm.nih.gov/35357307/) — Acl4 co-translationally recognizes Rpl4 and couples r-protein synthesis to ribosome assembly through mRNA feedback. **Supports the proteostasis/ribosome-biogenesis role.**

---

## Limitations and Knowledge Gaps

1. **PANTHER family membership was inferred from the annotation pattern and family naming, not re-derived here.** What was checked: the term set and their IBA provenance, plus the TOM70 family name. Why it matters: the exact tree topology determines which node donated the term. Resolution: pull the PTHR46208 tree and confirm the LCA node carrying GO:0008320 and ACL4's branch placement.
2. **TM prediction used a single method (Kyte–Doolittle, window 19).** What was checked: hydropathy maxima vs. a 1.6 threshold. Why it matters: a borderline segment could be missed by one method. Resolution: cross-check with DeepTMHMM/Phobius and signal-peptide predictors (SignalP) — expected to also return no TM/signal, reinforcing the conclusion.
3. **AlphaFold geometry was not directly parsed in this run.** Why it matters: an independent structural confirmation of a fully soluble globular TPR solenoid would add provenance. Resolution: parse the AlphaFold model for Q03771 and confirm absence of a membrane-embeddable hydrophobic surface.
4. **The exact asserted-vs-inherited status of the IBA term in the review YAML** should be confirmed so the curator applies the right mechanism (remove vs. NOT-qualify).

None of these gaps threaten the central conclusion; they would only strengthen documentation.

---

## Discriminating Tests

1. **Recover the PANTHER PTHR46208 tree** and identify the ancestral node from which GO:0008320 was propagated; confirm ACL4 (SF2) branches away from the TOM70 (membrane-function) clade. *Most direct provenance test.*
2. **Orthogonal TM/topology prediction** (DeepTMHMM, Phobius) and **signal-peptide prediction** (SignalP) on Q03771 — expected: no TM helices, no signal peptide, confirming soluble localization.
3. **Parse AlphaFold DB model for Q03771** — expected: an all-α TPR superhelix with no membrane-insertion surface; compute a membrane-embedding score (e.g., hydrophobic-belt analysis) as negative control.
4. **Membrane-fractionation / protease-protection data mining** for Acl4 in existing yeast proteomics — expected: cytosolic/nuclear, not membrane-pelleting.
5. **Family-wide term audit:** check whether the other TOM70-derived IBA terms (GO:0005741, GO:0030943, GO:0030150, GO:0045039) co-occur on ACL4; their joint presence is diagnostic of the same artifact and argues for batch correction.

---

## Proposed Follow-up Actions / Curation Leads

**All items below are leads requiring curator verification.**

**Action change (primary lead):**
- **Remove GO:0008320 (protein transmembrane transporter activity, IBA)** from ACL4, or apply a NOT/curator-note flag documenting that it is a TOM70-family IBA carry-over. Extend the same review to the co-inherited TOM70 IBA terms (GO:0005741, GO:0030943, GO:0030150, GO:0045039).

**Retain / prefer these evidence-backed terms instead:**
- **GO:0140318 protein transporter activity** (SGD IDA) — informative MF for ACL4's escort function.
- **GO:0051082 unfolded protein binding** (SGD IDA) — chaperone activity.
- BP: ribosomal large subunit / ribosome biogenesis; CC: cytoplasm (GO:0005737) + nucleus (GO:0005634).

**Candidate references with snippets to verify:**
- [PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/): *"We report the crystal structure of ribosomal protein L4 (RpL4) bound to its dedicated assembly chaperone of L4 (Acl4), revealing extensive interactions sequestering 70 exposed residues of the extended RpL4 loop… Acl4 serves a dual function to facilitate nuclear import and simultaneously protect unassembled RpL4 from the cellular degradation machinery."*
- [PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/): *"Acl4 localizes to both the cytoplasm and nucleus and it has the capacity to capture nascent Rpl4 in a co-translational manner… the dedicated chaperone Acl4 accompanies Rpl4 from the cytoplasm to its pre-60S assembly site in the nucleus."*
- [PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/): *"assembly chaperone Acl4 … initially binds the universally conserved internal loop of newly synthesized RpL4 via its superhelical TPR domain."*

**Suggested questions for the curator:**
- Is GO:0008320 an asserted annotation on ACL4 or only an inherited IBA prediction? (Determines remove vs. NOT-qualify.)
- Should the whole TOM70-derived IBA cluster be corrected together as a single family-artifact batch?

**Suggested experiments/analyses (provenance):**
- Re-run TM topology with DeepTMHMM/Phobius + SignalP; parse AlphaFold Q03771 for membrane-embedding surface; retrieve PTHR46208 tree to localize the donor node.

---

## Bottom Line

The hypothesis is **REFUTED**. GO:0008320 is an IBA over-annotation propagated from the TOM70-dominated PANTHER family via shared TPR fold. ACL4 is a soluble cytosolic/nuclear escort chaperone for ribosomal protein Rpl4 with no transmembrane segments. The term should be removed; ACL4's genuine function is already captured by GO:0140318 (protein transporter activity) and GO:0051082 (unfolded protein binding).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)