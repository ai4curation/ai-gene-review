---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T21:26:04.106176'
end_time: '2026-09-20T21:43:48.253553'
duration_seconds: 1064.15
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: A3GALT2
  gene_symbol: A3GALT2
  uniprot_accession: U3KPV4
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: human-enzyme-constructs-and-glycan-substrate-specificity
  hypothesis_text: Human A3GALT2 retains glycosyltransferase/hexosyltransferase activity,
    contributes to glycosphingolipid biosynthesis and has LacNAc-specific activity.
    Evaluate each separately and interpret the existing NOT for GO:0001962 rather
    than erasing it. Reconcile PMID:18630988 human-domain chimera negatives with PMID:23378701
    reconstructed-human-ORF weak positives in CHO cells. Inspect exact construct sequences,
    substrates, assay sensitivity and ancestral catalytic specificity; absence of
    an endogenous human assay is not proof of inactivity, and a positive different
    substrate does not establish LacNAc activity.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/A3GALT2/A3GALT2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human A3GALT2 retains glycosyltransferase/hexosyltransferase\
    \ activity, contributes to glycosphingolipid\n  biosynthesis and has LacNAc-specific\
    \ activity. Evaluate each separately and interpret the existing NOT\n  for GO:0001962\
    \ rather than erasing it. Reconcile PMID:18630988 human-domain chimera negatives\
    \ with PMID:23378701\n  reconstructed-human-ORF weak positives in CHO cells. Inspect\
    \ exact construct sequences, substrates,\n  assay sensitivity and ancestral catalytic\
    \ specificity; absence of an endogenous human assay is not proof\n  of inactivity,\
    \ and a positive different substrate does not establish LacNAc activity.\nfocus_type:\
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
citation_count: 4
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: A3GALT2_GO_decision_table.csv
  path: openscientist_artifacts/A3GALT2_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist A3GALT2 GO decision table
- filename: A3GALT2_evidence_matrix.csv
  path: openscientist_artifacts/A3GALT2_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist A3GALT2 evidence matrix
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
- **Gene directory:** A3GALT2
- **Gene symbol:** A3GALT2
- **UniProt accession:** U3KPV4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** human-enzyme-constructs-and-glycan-substrate-specificity
- **Source file:** genes/human/A3GALT2/A3GALT2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human A3GALT2 retains glycosyltransferase/hexosyltransferase activity, contributes to glycosphingolipid biosynthesis and has LacNAc-specific activity. Evaluate each separately and interpret the existing NOT for GO:0001962 rather than erasing it. Reconcile PMID:18630988 human-domain chimera negatives with PMID:23378701 reconstructed-human-ORF weak positives in CHO cells. Inspect exact construct sequences, substrates, assay sensitivity and ancestral catalytic specificity; absence of an endogenous human assay is not proof of inactivity, and a positive different substrate does not establish LacNAc activity.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human A3GALT2 retains glycosyltransferase/hexosyltransferase activity, contributes to glycosphingolipid
  biosynthesis and has LacNAc-specific activity. Evaluate each separately and interpret the existing NOT
  for GO:0001962 rather than erasing it. Reconcile PMID:18630988 human-domain chimera negatives with PMID:23378701
  reconstructed-human-ORF weak positives in CHO cells. Inspect exact construct sequences, substrates,
  assay sensitivity and ancestral catalytic specificity; absence of an endogenous human assay is not proof
  of inactivity, and a positive different substrate does not establish LacNAc activity.
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

# AIGR Gene Hypothesis Deep Research — Human A3GALT2 (UniProt U3KPV4)

**Focus:** function_assignment · **Hypothesis slug:** human-enzyme-constructs-and-glycan-substrate-specificity
**Gene:** A3GALT2 (isoglobotriaosylceramide synthase / iGb3 synthase, iGb3S) · **Organism:** *Homo sapiens* (NCBITaxon:9606)

---

## Executive Judgment

**Verdict: Partially supported — but the enzymatic sub-claims are over-annotated.**

The seed hypothesis bundles three separable claims: (1) human A3GALT2 retains glycosyltransferase/hexosyltransferase activity, (2) it contributes to glycosphingolipid biosynthesis, and (3) it has LacNAc-specific (N-acetyllactosaminide 3-α-galactosyltransferase, GO:0047276) activity. When each is evaluated **separately**, as the seed itself demands, the evidence does not support human catalytic activity. Every positive activity annotation on U3KPV4 rests on inference from active rodent orthologs (ECO:0000250 "by similarity", ISS, IEA, IBA), while the **only direct human experimental evidence is negative**: a chimera bearing the human A3GALT2 catalytic domain cannot synthesize iGb3, and the human-type Asn253 residue eliminates activity when transplanted into the otherwise-active rat enzyme ([PMID: 18630988](https://pubmed.ncbi.nlm.nih.gov/18630988/)). This IDA-based **NOT|enables GO:0001962** (α-1,3-galactosyltransferase activity) is therefore well justified and should be **retained**, not erased.

The seed correctly instructs the curator to "interpret the existing NOT rather than erase it," and to treat "absence of an endogenous human assay" as distinct from "proof of inactivity." That epistemic caution is appropriate in principle — but here we have more than absence-of-assay: we have a **direct positive experiment showing loss of activity** (the Y253N substitution ablates the rat enzyme) plus corroborating comparative genomics showing that all human GT6-family genes except ABO are nonfunctional ([PMID: 17298992](https://pubmed.ncbi.nlm.nih.gov/17298992/)). The "reconstructed-human-ORF weak positive in CHO cells" that the seed attributes to [PMID: 23378701](https://pubmed.ncbi.nlm.nih.gov/23378701/) **could not be confirmed**: that paper's abstract concerns pig organs and reports the *absence* of iGb3/isoglobo-series glycosphingolipids by sensitive mass spectrometry; it provides no human endogenous positive assay. The seed's framing of a "human-domain chimera negative vs. reconstructed-human-ORF weak positive" conflict thus appears to rest on a mis-attributed or unverifiable positive.

**Most important caveats:** (a) Human A3GALT2 *is* transcribed (GTEx v8, max 1.01 TPM in testis) and encodes an intact, foldable GT6 protein retaining DXD/metal-binding residues — so it is not a classical pseudogene; "over-annotated activity" is the correct framing, not "gene does not exist." (b) The LacNAc claim (GO:0047276) is a *different substrate* from the iGb3-synthase reaction assayed in [PMID: 18630988](https://pubmed.ncbi.nlm.nih.gov/18630988/); no human assay directly tested LacNAc, so its removal/NOT-qualification is an inference-consistency lead rather than a directly assayed negative.

---

## Key Findings

### Finding 1 — Human A3GALT2 carries an inactivating Asn253 substitution; NOT GO:0001962 is directly supported

The reviewed UniProt entry U3KPV4 (340 aa) carries a CAUTION comment citing [PMID: 18630988](https://pubmed.ncbi.nlm.nih.gov/18630988/). In that study, a chimeric molecule bearing the **human A3GALT2 catalytic domain was unable to synthesize iGb3**, and introducing the human-type residue (Tyr→Asn) at position 253 into the otherwise-active rat enzyme **completely eliminated α-1,3-galactosyltransferase activity**. The verified abstract quotes are direct:

> *"These hybrid molecules were unable to synthesize iGb3, due to at least one amino acid substitution."*
> *"our data suggest that iGb3S is not expressed in humans, and even if it were expressed, this enzyme would be inactive."*

To confirm the residue identity independently, a Needleman–Wunsch global alignment was run between human U3KPV4 and the functional rat ortholog Q3V1N9 (69.4% identity over 340 aligned columns). The alignment confirms that **human position 253 = Asn (N)** where the active rat enzyme has **Tyr (Y)** — exactly the inactivating substitution described experimentally. QuickGO records the corresponding human annotation as **NOT|enables GO:0001962** (α-1,3-galactosyltransferase activity), evidence code **IDA**, sourced from PMID:18630988 and assigned by UniProt. This is the single strongest, most direct piece of evidence in the whole dossier, and it is negative for catalytic activity. The NOT annotation is a faithful, experimentally grounded curation decision.

### Finding 2 — All positive activity annotations (including LacNAc GO:0047276) are inference-only and conflict with the direct-assay NOT

A systematic audit of the evidence codes behind U3KPV4's positive activity statements shows a uniform pattern of **inference from rodent orthologs, never human experiment**:

| Annotation | GO / RHEA | Evidence code | Source |
|---|---|---|---|
| iGb3 synthase FUNCTION statement | — | ECO:0000305 (curator inference) | PMID:23378701 |
| Catalytic activity (iGb3 reaction) | — | ECO:0000250 (by similarity) | rodent ortholog |
| Catalytic activity — **LacNAc reaction** | RHEA:13013 (LacNAc + UDP-Gal → Gal-α-1,3-LacNAc) | ECO:0000250 (by similarity) | rodent ortholog |
| enables **GO:0047276** (N-acetyllactosaminide 3-α-galactosyltransferase) | — | ISS (GO_REF:0000024) + IEA (GO_REF:0000120) | electronic |
| enables GO:0016757 (glycosyltransferase) | — | IBA | phylogenetic |
| enables GO:0016758 (hexosyltransferase) | — | IEA | electronic |
| involved_in GO:0006688 (glycosphingolipid biosynthetic process) | — | IBA | phylogenetic |
| **NOT|enables GO:0001962** (α-1,3-GalT activity) | — | **IDA** | **PMID:18630988** |

The asymmetry is decisive: the *only* experimental (IDA) annotation is the negative one, while every positive annotation is "by similarity"/ISS/IEA/IBA propagated from active rodent iGb3 synthases. Critically, the FUNCTION statement cites [PMID: 23378701](https://pubmed.ncbi.nlm.nih.gov/23378701/), whose verified abstract actually reports the **absence** of the product:

> *"We did not detect iGb3 or other isoglobo-series glycosphingoli[pids]"*

That paper examined **pig organs used for xenotransplantation** and provides no human endogenous positive assay. Therefore the seed's "LacNAc-specific activity" claim (GO:0047276) is unsupported by any human data and is in direct logical tension with the NOT GO:0001962 — the LacNAc reaction is itself an α-1,3-galactosyltransferase reaction on a specific acceptor, and the enzyme demonstrated to have lost α-1,3-Gal transfer cannot be assumed to retain it selectively on LacNAc.

### Finding 3 — Comparative genomics: human GT6-family genes are nonfunctional except ABO

The CAZy GT6 (ABO) glycosyltransferase family — comprising the A/B histo-blood-group enzymes (ABO), the Forssman synthase (GBGT1), the αGal-epitope synthase (GGTA1), and the iGb3 synthase (A3GALT2/iGb3S) — was analyzed across fishes-to-mammals by Turcot-Dubois et al. ([PMID: 17298992](https://pubmed.ncbi.nlm.nih.gov/17298992/)). The verified conclusions:

> *"In human, except ABO functional alleles, all other GT6 genes are either absent or nonfunctional."*
> *"Functional glycosyltransferase 6 (GT6) family members catalyze the transfer of galactose or N-acetylgalactosamine in alpha1,3 linkage to various substrates and synthesize structures related to the A and B histo-blood group antigens, the Forssman antigen, alphaGal epitope, and iGb3 glycolipid."*

Human GGTA1 is a well-known pseudogene, and human GBGT1 is largely inactive; A3GALT2 falls in the same nonfunctional set. This evolutionary context both (a) reinforces the loss-of-function call and (b) flags the paralog-confusion risk behind the LacNAc annotation: GGTA1 makes the αGal epitope on LacNAc acceptors, so an ISS/IEA propagation onto A3GALT2 for GO:0047276 may reflect family-level acceptor inference rather than a demonstrated human A3GALT2 activity. The presence of retained DXD/metal-binding residues (positions 199, 201) alongside the inactivating acceptor/catalytic substitution (Asn253) is fully consistent with a **folded GT6 protein that has lost its specific α-1,3-Gal transferase activity** rather than a degraded pseudogene product.

### Finding 4 — GTEx shows low but real transcription; it does not rescue the activity hypothesis

Because the 2008 study reported that spliced iGb3S mRNA was "not detected" in human tissues, modern RNA-seq was checked to update that claim. GTEx v8 median expression for A3GALT2 (ENSG00000184389.9) across 54 tissues shows **very low but non-zero transcription**: maximum median = **1.01 TPM (testis)**, next highest Brain_Cerebellum 0.43 and Whole_Blood 0.40; the across-tissue median is 0.12 TPM, and only 1 of 54 tissues exceeds 1 TPM. This partially updates the 2008 "not detected" statement — the locus *is* transcribed at trace levels — but does not rescue the enzymatic hypothesis, because (a) expression is uniformly very low and (b) the encoded protein still carries the experimentally validated inactivating Asn253 residue. Transcription of an mRNA encoding a catalytically dead protein is not evidence of enzymatic function.

---

## Mechanistic Model / Interpretation

The molecular question is narrow and well posed: does the human A3GALT2 protein directly catalyze transfer of galactose in α-1,3 linkage (to Gal-β-1-4-GlcNAc/LacNAc, or to lactosylceramide en route to iGb3)? The evidence converges on **"no."**

```
   ACTIVE ORTHOLOG (rat Q3V1N9)                 HUMAN A3GALT2 (U3KPV4)
   ---------------------------                  -----------------------
   GT6 fold + DXD/metal site  ..........same.... GT6 fold + DXD/metal site (res 199,201 retained)
   Acceptor/catalytic residue Tyr253            Acceptor/catalytic residue Asn253  <-- INACTIVATING
        |                                              |
        v                                              v
   LacCer + UDP-Gal --> iGb3   (works)          LacCer + UDP-Gal --> iGb3   (FAILS, PMID:18630988)
   LacNAc + UDP-Gal --> Gal-a1,3-LacNAc         LacNAc reaction: never assayed in human;
                                                inferred "by similarity" only (RHEA:13013)

   Direct human evidence:  NOT|enables GO:0001962  (IDA, PMID:18630988)   <== only experiment
   All positive terms:     ECO:0000250 / ISS / IEA / IBA                  <== inference from rodents
```

The interpretive key is the distinction the seed itself insists on: **a positive on a different substrate does not establish LacNAc activity, and absence of an endogenous assay is not proof of inactivity.** Applying that rigor symmetrically:

- The **negative** here is *not* mere absence of an endogenous assay — it is a *positive experiment demonstrating loss*: transplanting the human Asn253 into the active rat enzyme abolishes activity (a gain-of-loss experiment), and the human catalytic domain chimera fails to make iGb3.
- The **LacNAc positive** is exactly the kind of "different-substrate / by-similarity" claim the seed warns against — it is propagated from rodent orthologs and from family paralogs (GGTA1), never measured on human A3GALT2.

Hence the coherent model is: human A3GALT2 is a **transcribed, foldable, but catalytically dead** relic of an ancestral GT6 iGb3 synthase, inactivated by the Tyr→Asn substitution at the acceptor/catalytic position 253, consistent with the family-wide loss of GT6 function in humans (except ABO). The "iGb3 synthase" and "LacNAc 3-α-galactosyltransferase" molecular-function annotations describe the **ancestral/ortholog activity**, not the extant human protein.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 18630988](https://pubmed.ncbi.nlm.nih.gov/18630988/) | Direct assay (chimera + point mutant) | **Refutes** activity | Does human A3GALT2 catalytic domain make iGb3 / retain α-1,3-GalT? | Human-domain chimera cannot synthesize iGb3; human-type Y253N ablates rat enzyme activity | Human catalytic domain; rat enzyme scaffold; in vitro | High. Chimera context (not full endogenous human enzyme in native cells); reinforced by point-mutant gain-of-loss |
| U3KPV4 / QuickGO (from PMID:18630988) | Database (IDA-backed NOT) | **Supports** NOT | Is the NOT GO:0001962 experimentally grounded? | NOT|enables GO:0001962, evidence IDA | Human, UniProt-assigned | High. Faithful curation of the direct assay |
| Sequence alignment (U3KPV4 vs rat Q3V1N9) | Structural/evolutionary (computational) | **Supports** loss | Does human carry the inactivating residue? | 69.4% identity; human pos 253 = Asn vs rat Tyr | In silico Needleman–Wunsch | High for residue identity; functional effect inferred from PMID:18630988 |
| [PMID: 17298992](https://pubmed.ncbi.nlm.nih.gov/17298992/) | Structural/evolutionary (comparative genomics) | **Supports** loss / **qualifies** LacNAc | Are human GT6 genes functional? | All human GT6 genes nonfunctional except ABO; family transfers Gal/GalNAc in α1,3 | Fishes→mammals; human genome | High for family context; indirect for A3GALT2 specifics; flags GGTA1 paralog-confusion for LacNAc |
| [PMID: 23378701](https://pubmed.ncbi.nlm.nih.gov/23378701/) | Direct assay (MS) | **Competing / qualifies** | Does the seed's "reconstructed-human-ORF weak positive" exist? | Reports *absence* of iGb3/isoglobo-series GSLs by sensitive MS; **no human endogenous positive assay** | Pig organs (xenotransplant) | Undermines seed's claimed positive; abstract is pig-focused; cited by UniProt for FUNCTION nonetheless |
| [PMID: 17372206](https://pubmed.ncbi.nlm.nih.gov/17372206/) | Mutant phenotype (KO mouse) | Qualifies (BP relevance) | Is iGb3 a required physiological ligand? | iGb3S-KO mice develop normally; iGb3 unlikely to be endogenous NKT-selecting ligand | Mouse | Contextual; concerns downstream biology, not human catalytic activity |
| GTEx v8 | Database (expression) | Qualifies | Is A3GALT2 transcribed in human? | Max median 1.01 TPM (testis); median 0.12 TPM; 1/54 tissues >1 TPM | Human, 54 tissues | High for transcription; irrelevant to catalytic competence |

---

## GO Curation Implications

**Lead requiring curator verification.** The evidence favors the following actions:

1. **Retain NOT|enables GO:0001962** (α-1,3-galactosyltransferase activity). This is the correctly grounded, IDA-backed decision from [PMID: 18630988](https://pubmed.ncbi.nlm.nih.gov/18630988/), corroborated by the Asn253 residue and family-wide GT6 loss. Do **not** erase it. *(MF term; retain as NOT.)*

2. **Re-scope the positive MF activity terms as ortholog-inference, not extant human function.** GO:0047276 (N-acetyllactosaminide 3-α-galactosyltransferase, the LacNAc term), the iGb3-synthase catalytic activity, GO:0016757 (glycosyltransferase, IBA), and GO:0016758 (hexosyltransferase, IEA) are all inference-only. Because the LacNAc reaction is itself an α-1,3-Gal transfer, GO:0047276 is in logical tension with the NOT and is a strong candidate for **removal or a NOT qualifier**, pending curator confirmation that no human LacNAc assay exists. *(MF; generalize/remove or NOT-qualify.)*

3. **Treat BP GO:0006688 (glycosphingolipid biosynthetic process, IBA) as non-core / inference-only** for the human gene. The human protein does not demonstrably contribute product to this pathway. *(BP; downgrade to non-core or remove.)*

4. **Do not recommend "protein binding" as a fallback** — the informative statement is that the human ortholog *lost* a specific catalytic MF, which is better captured by the retained NOT plus a CAUTION note than by a vague binding term.

**GO decision table**

| GO term | Current | Evidence | Recommended lead |
|---|---|---|---|
| GO:0001962 α-1,3-galactosyltransferase | **NOT**|enables (IDA) | Direct human negative (PMID:18630988) | **Retain NOT** |
| GO:0047276 LacNAc 3-α-GalT | enables (ISS/IEA) | Inference only; conflicts with NOT | **Remove or NOT-qualify** |
| iGb3 synthase catalytic activity | enables (ECO:0000250) | By similarity | Re-scope as ortholog inference |
| GO:0016757 glycosyltransferase | enables (IBA) | Phylogenetic | Generalize/annotate as inferred; low priority |
| GO:0016758 hexosyltransferase | enables (IEA) | Electronic | Non-core |
| GO:0006688 glycosphingolipid biosynthesis | involved_in (IBA) | Phylogenetic | Downgrade to non-core / inference |

---

## Mechanistic Scope

The immediate molecular function under test is **UDP-galactose:acceptor α-1,3-galactosyltransferase activity** — specifically iGb3 synthesis (Gal-α-1,3 onto lactosylceramide) and, per the seed, the LacNAc-acceptor variant (RHEA:13013). This is a single enzymatic step. The direct evidence (PMID:18630988) speaks to exactly this step and finds it lost in the human sequence.

Downstream/contextual layers that must **not** be conflated with the molecular activity:
- **iGb3 as a glycosphingolipid** and its proposed role as an endogenous NKT-cell-selecting lipid — [PMID: 17372206](https://pubmed.ncbi.nlm.nih.gov/17372206/) shows iGb3S-KO mice develop normally with normal iNKT cells, arguing iGb3 is not the required ligand. This is a BP/physiology question, not evidence for human catalytic activity.
- **Xenotransplantation glycobiology** ([PMID: 23378701](https://pubmed.ncbi.nlm.nih.gov/23378701/)) concerns product abundance in pig organs, again downstream of the human molecular-function question.
- **Transcription** (GTEx) is upstream of protein function and does not imply catalysis.

Keeping these separate is essential: the human gene may be transcribed and its ortholog physiologically studied, yet the *human protein's direct catalytic MF* is the blinded decision, and it is negative.

---

## Conflicts and Alternatives

- **Ortholog-inference over-annotation (primary alternative, favored).** The positive terms are propagated from active rodent iGb3 synthases; they describe ancestral function, not human function. This is the parsimonious reading of the ECO:0000250/ISS/IEA/IBA pattern.
- **Paralog confusion for LacNAc (GO:0047276).** Within GT6, GGTA1 synthesizes the αGal epitope on LacNAc. Family-level acceptor inference could have seeded the LacNAc annotation onto A3GALT2 without direct measurement — precisely the "different substrate does not establish LacNAc activity" caution in the seed.
- **Database carry-over.** The FUNCTION statement cites PMID:23378701 (a pig-organ negative), suggesting the positive framing is a citation/carry-over artifact rather than a demonstrated human positive.
- **The seed's asserted "reconstructed-human-ORF weak positive in CHO cells."** This could not be verified against the cited abstract (which is a pig-organ negative). If such a CHO reconstitution positive exists, it would be a genuine competing datum and must be located in the full text; on current evidence it appears mis-attributed. A weak in-CHO signal, if real, would still be an in-vitro overexpression result requiring reconciliation with the human-domain chimera negative and the Asn253 point-mutant result.
- **Chimera caveat (pro-hypothesis nuance).** PMID:18630988 tested a human *catalytic domain* in a chimeric/rat scaffold, not the intact native human enzyme in human cells. This is the strongest pro-hypothesis point — but the accompanying single-residue Y253N gain-of-loss experiment substantially closes that gap.

---

## Limitations and Knowledge Gaps

1. **No intact-native-human-enzyme assay.** The direct negative uses a chimera plus a point mutant, not full-length human A3GALT2 expressed and assayed in human cells against a panel of acceptors. *Why it matters:* the seed's epistemics ("absence of endogenous assay ≠ inactivity") apply. *Resolver:* express full-length U3KPV4 in a null background and assay UDP-Gal transfer to LacCer and LacNAc.
2. **LacNAc acceptor never directly tested in human.** GO:0047276 rests entirely on inference. *Resolver:* in-vitro glycosyltransferase assay with LacNAc + UDP-Gal (RHEA:13013) using purified human protein; LC-MS product detection.
3. **The seed's CHO "weak positive" is unverified.** *Why it matters:* it is the linchpin of the claimed conflict. *Resolver:* obtain PMID:23378701 full text (and any companion) to confirm/deny a human-ORF reconstitution result; search for the primary source of any CHO positive.
4. **Functional effect of Asn253 confirmed only via the rat scaffold.** *Resolver:* reverse experiment — Asn253→Tyr "resurrection" of human A3GALT2 to test whether a single back-mutation restores activity, which would cleanly prove the residue is the sole inactivating lesion.
5. **Trace testis transcription of unknown consequence.** *Resolver:* ribosome-profiling/proteomics evidence for translated, stable human A3GALT2 protein.

---

## Discriminating Tests

1. **Full-length human A3GALT2 in-vitro assay** against LacCer *and* LacNAc with UDP-Gal; LC-MS/MS product quantification. Distinguishes "catalytically dead" from "active on some acceptor" and directly tests GO:0047276.
2. **Asn253→Tyr resurrection mutant** of human A3GALT2: if activity is restored, it nails the single-residue inactivation model and confirms the ancestral specificity.
3. **Reciprocal residue swaps across GT6 paralogs** (A3GALT2 ↔ GGTA1 acceptor loops) to test the paralog-confusion hypothesis for LacNAc specificity.
4. **Targeted proteomics / ribo-seq** in testis to establish whether the trace transcript yields stable protein.
5. **Literature/full-text retrieval** of PMID:23378701 and citing papers to locate or refute the seed's "reconstructed-human-ORF weak positive in CHO cells."

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

**Leads requiring curator verification:**

- **Action lead A (retain):** Keep **NOT|enables GO:0001962** (IDA, PMID:18630988). *Snippet to verify:* "these hybrid molecules were unable to synthesize iGb3, due to at least one amino acid substitution" and "even if it were expressed, this enzyme would be inactive."
- **Action lead B (remove / NOT-qualify):** Flag **GO:0047276** (LacNAc 3-α-GalT) as inference-only and in tension with the NOT; recommend removal or NOT-qualification pending a human LacNAc assay. *Rationale:* ISS/IEA only; the LacNAc reaction is an α-1,3-Gal transfer, which the human enzyme has lost.
- **Action lead C (downgrade):** Treat **GO:0006688** (glycosphingolipid biosynthetic process, IBA) and **GO:0016757/GO:0016758** as non-core / ortholog-inference for the human gene.
- **Reference-integrity lead D:** Note that the FUNCTION statement cites **PMID:23378701**, whose abstract reports *absence* of isoglobo-series products in pig organs and provides **no human positive assay**. *Snippet to verify:* "We did not detect iGb3 or other isoglobo-series glycosphingoli[pids]." Curator should confirm whether this citation actually supports a human FUNCTION.
- **Reconciliation lead E:** Attempt to locate the seed's "reconstructed-human-ORF weak positive in CHO cells." If unlocatable, record that the claimed PMID:18630988-vs-PMID:23378701 conflict does not resolve into a genuine human positive.
- **Suggested question for curators:** Should A3GALT2's human MF annotations be reframed uniformly as "ancestral/ortholog activity, lost in *H. sapiens*," with a single CAUTION note, rather than carrying multiple positive activity terms alongside the NOT?
- **Suggested experiments:** full-length human assay (LacCer + LacNAc), Asn253→Tyr resurrection, testis proteomics — as detailed in Discriminating Tests.

---

## Evidence Base (Literature)

- **[PMID: 18630988](https://pubmed.ncbi.nlm.nih.gov/18630988/)** — *Humans lack iGb3 due to the absence of functional iGb3-synthase: implications for NKT cell development and transplantation.* The pivotal direct-assay negative: human catalytic-domain chimera cannot make iGb3; human-type Y253N ablates the active rat enzyme. Grounds the NOT GO:0001962.
- **[PMID: 23378701](https://pubmed.ncbi.nlm.nih.gov/23378701/)** — *Lack of iGb3 and Isoglobo-Series Glycosphingolipids in Pig Organs Used for Xenotransplantation: Implications for Natural Killer T-Cell Biology.* Reports absence of isoglobo-series products by sensitive MS in pig organs; cited by UniProt for FUNCTION but provides no human positive assay — undercuts the seed's claimed positive.
- **[PMID: 17298992](https://pubmed.ncbi.nlm.nih.gov/17298992/)** — *Long-term evolution of the CAZY glycosyltransferase 6 (ABO) gene family from fishes to mammals — a birth-and-death evolution model.* Establishes that all human GT6 genes except ABO are nonfunctional and defines the paralog set (GGTA1/αGal-on-LacNAc, GBGT1/Forssman, A3GALT2/iGb3), relevant to paralog-confusion in the LacNAc annotation.
- **[PMID: 17372206](https://pubmed.ncbi.nlm.nih.gov/17372206/)** — *Normal development and function of invariant natural killer T cells in mice with isoglobotrihexosylceramide (iGb3) deficiency.* iGb3S-KO mice are phenotypically normal; iGb3 unlikely to be the endogenous NKT-selecting ligand — contextualizes the BP/physiology layer, separate from human catalytic MF.

---

*Prepared for AI Gene Review curation. All activity conclusions distinguish direct human experimental evidence (negative, IDA) from ortholog/paralog inference (positive, ECO:0000250/ISS/IEA/IBA). Computational residue identity (Asn253) was verified by pairwise alignment; the sequence conflict, expression, and evidence-code audits are reported conservatively as leads for curator verification.*


## Artifacts

- [OpenScientist A3GALT2 GO decision table](openscientist_artifacts/A3GALT2_GO_decision_table.csv)
- [OpenScientist A3GALT2 evidence matrix](openscientist_artifacts/A3GALT2_evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)