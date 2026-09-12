---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T16:51:51.694225'
end_time: '2026-07-06T17:01:03.725524'
duration_seconds: 552.03
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: ubl-5
  gene_symbol: ubl-5
  uniprot_accession: P91302
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0031386
  hypothesis_text: ubl-5 has protein tag activity (GO:0031386).
  term_context: '- Term: protein tag activity (GO:0031386)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - file:worm/ubl-5/ubl-5-deep-research-falcon.md'
  source_file: genes/worm/ubl-5/ubl-5-ai-review.yaml
  source_selector: existing_annotations[4].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0031386\n  label: protein tag activity\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033"
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

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** ubl-5
- **Gene symbol:** ubl-5
- **UniProt accession:** P91302

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0031386
- **Source file:** genes/worm/ubl-5/ubl-5-ai-review.yaml
- **Source selector:** existing_annotations[4].function_hypothesis

## Seed Hypothesis

ubl-5 has protein tag activity (GO:0031386).

## Term and Decision Context

- Term: protein tag activity (GO:0031386)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- file:worm/ubl-5/ubl-5-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0031386
  label: protein tag activity
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

# Deep Research Report: Does *C. elegans* ubl-5 (P91302) have protein tag activity (GO:0031386)?

**Focus:** function-assignment — does the gene product directly have GO:0031386 "protein tag activity"?
**Source annotation:** `existing_annotations[4].function_hypothesis`, evidence IBA, GO_REF:0000033.

---

## Executive Judgment

**Verdict: REFUTED (over-annotated).**

The seed hypothesis — that ubl-5 has **protein tag activity (GO:0031386)** — is **not supported** and should be treated as an over-annotation. Three independent, mutually reinforcing lines of evidence converge:

1. **Definitional mismatch.** GO:0031386 is defined as an activity of a protein "that is **covalently attached (AKA tagged or conjugated) to another protein**" (QuickGO), and its curator comment restricts the term to *conjugated* tags. Covalent conjugation is a hard requirement of the term.
2. **Structural signature (computed here).** UBL-5 (P91302, 73 aa) ends in **…FNFEL-Y-Y-Q**, terminating in Gln73 with **no C-terminal di-glycine (GG)**. The di-glycine is mechanistically obligatory for isopeptide-bond conjugation and is present in every canonical covalent tag (ubiquitin, SUMO, NEDD8, ISG15). Its absence in UBL-5 (and in the identical-length human ortholog UBL5) is a diagnostic marker that this subfamily is **not conjugation-competent**.
3. **Direct experimental evidence.** Primary literature across yeast, human, and *C. elegans* states that Hub1/UBL-5 **does not form covalent conjugates** and instead **binds partners non-covalently** through the HIND motif of spliceosomal proteins (Snu66/SART-1, Prp38/PRP-38).

The IBA annotation is a phylogenetic carry-over from the broad ubiquitin superfamily that fails to account for the well-characterized, conjugation-independent divergence of the Hub1/UBL5 clade. The genuinely supported function is **non-covalent binding to HIND-motif spliceosomal factors**, contributing to **mRNA splicing (GO:0000398)** — already annotated (IBA) — not protein tag activity.

**Most important caveat:** UniProt's human UBL5 entry still carries the legacy keyword "Ubl conjugation pathway," and older yeast reports (early 2000s) initially suggested Hub1 conjugation; these were superseded. This legacy is the likely origin of the over-annotation and should not be weighted against the direct non-covalent evidence.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| This report (UniProt P91302 FASTA) | Structural/evolutionary (computed) | **Refutes** | Does UBL-5 have a conjugation-competent C-terminus? | 73 aa, C-terminus …ELYYQ; **no C-terminal GG**; contrasts ubiquitin/SUMO/NEDD8/ISG15 which all end in GG | Sequence-level, worm + human ortholog | High; sequence-based inference of mechanism |
| Ammon et al. 2014, PMID **24872507** | Direct assay / cell biology | **Refutes** | Is Hub1/UBL5 a covalent tag? | "Hub1 does not form covalent conjugates with substrates but binds proteins non-covalently"; modulator of alternative splicing | Human + yeast | High; explicit statement of binding mode |
| Mishra et al. 2011, PMID **21614000** | Structural + biochemical | **Refutes / re-assigns** | Binding mode & function | Hub1 "binds non-covalently to a conserved element termed HIND" (Snu66/Prp38); "non-covalent modification of the spliceosome by an unconventional ubiquitin-like modifier" | *S. cerevisiae*, structural | High; foundational mechanistic paper |
| Kolathur et al. 2023, PMID **36480405** | Mutant phenotype + interaction | **Refutes (organism-specific) / re-assigns** | Worm UBL-5 binding mode & role | "Hub1/UBL-5 associates with proteins **non-covalently**"; binds HIND factors Snu66/SART-1 and PRP-38; *ubl-5* mutants die at L3 with splicing defects | ***C. elegans*** | High; the directly relevant organism |
| Oka et al. 2014, PMID **25092792** | Depletion / functional assay | Qualifies (re-assigns) | Metazoan UBL5 function | UBL5 "primarily associates with spliceosomal proteins"; depletion → intron retention, loss of sister-chromatid cohesion via Sororin | Human cells | High; function is splicing, not tagging |
| Karaduman et al. 2017, PMID **28712727** | Biochemical | Qualifies (re-assigns) | Molecular mechanism | Hub1 binds DEAD-box helicase Prp5 and stimulates its ATPase → error-prone splicing | *S. cerevisiae* | High; non-covalent partner regulation |
| Haynes et al. 2007, PMID **17925224** (UniProt FUNCTION) | Mutant phenotype | Competing (downstream BP) | Worm-specific role | ubl-5 required for mitochondrial UPR (mtUPR); interacts with dve-1 under stress | *C. elegans* | Downstream biological process, not an MF |
| QuickGO GO:0031386 (definition) | Database / ontology | Sets the bar | What the term requires | "covalently attached (…conjugated) to another protein"; comment: "annotate conjugated tags" | Ontology | Definitional; decisive for the call |

---

## GO Curation Implications

**Lead (requires curator verification): REMOVE / do-not-annotate GO:0031386 (protein tag activity) for ubl-5.**

- **MF:** GO:0031386 is **not supported**; the covalent-conjugation requirement of the term is contradicted by direct evidence and by the missing C-terminal di-glycine. Recommend removing the IBA annotation (or entering it as a NOT annotation for the family propagation). If a molecular-function term is desired, the defensible activity is **non-covalent protein binding to spliceosomal HIND-motif partners** — a more informative candidate than bare "protein binding" would be a splicing-factor/spliceosome binding term (e.g., a "spliceosomal complex binding"–type MF) supported by PMID 36480405/21614000, though direct MF terms for UBL5 remain sparse.
- **BP (retain):** GO:0000398 "mRNA splicing, via spliceosome" (IBA) is well supported and now has *C. elegans*-specific backing (PMID 36480405). GO:0034514 "mitochondrial unfolded protein response" (IMP) is a valid worm-specific downstream process but is not a molecular tag activity.
- **CC (retain):** cytoplasm/cytosol/nucleus and transcription-regulator-complex localizations are experimentally supported (IDA/IPI, WormBase).

Net: the protein-tag MF should be **removed/generalized away**; the splicing BP and localization CC annotations carry the real function.

---

## Mechanistic Scope

- **Immediate molecular function tested:** whether UBL-5 acts as a covalent post-translational tag (like ubiquitin/SUMO) that is conjugated to substrate lysines to mark them for a cellular fate.
- **What the evidence actually shows:** UBL-5 is a ubiquitin-*fold* protein that engages partners **non-covalently** via the HIND motif (Snu66/SART-1, PRP-38) and modulates spliceosome performance and alternative/weak-intron splicing. It is a **binding modulator**, not a conjugatable marker.
- **Downstream / not the direct MF:** mtUPR regulation (with dve-1/atfs-1), lipid-metabolism modulation upstream of nhr-80, L3 lethality, sister-chromatid cohesion (via Sororin), and stress-response phenotypes are **downstream consequences** of impaired non-covalent splicing/complex function — not evidence of tag activity.

---

## Conflicts and Alternatives

- **Database carry-over / legacy artifact:** Human UBL5 (Q9BZL1) retains the UniProt keyword "Ubl conjugation pathway," and early-2000s yeast work initially proposed Hub1 conjugation. These are the most likely source of the IBA propagation and are contradicted by later definitive studies (PMID 24872507, 21614000).
- **Family/paralog over-annotation:** GO:0031386 is a superfamily-level attribute inherited by IBA across ubiquitin-like proteins; the Hub1/UBL5 clade (InterPro IPR039732 Hub1/Ubl5) is the recognized exception. The seed hypothesis reflects clade-blind propagation.
- **No conflicting primary evidence found** that UBL-5 is ever covalently conjugated to a substrate.

---

## Knowledge Gaps

1. **Formal MF term for a non-covalent Ubl modulator.** Checked GO/QuickGO: GO:0031386 requires covalency, so it cannot apply. A precise MF term capturing "non-covalent spliceosome-modulating binding" is not clearly established in GO. *Resolves by:* curator selection of an appropriate binding MF or a new/related term; supported by PMID 36480405, 21614000.
2. **Direct in vivo conjugation assay in worm.** No mass-spec/isopeptide evidence exists showing UBL-5–substrate conjugates in *C. elegans*. *Matters because* it would be the only way to overturn the non-covalent consensus. *Resolves by:* anti-UBL-5 IP + LC-MS/MS for GG-remnant/branched peptides (expected negative).
3. **C-terminal maturation.** UBL-5 ends in Gln, not a processed Gly; there is no evidence of a protease exposing a conjugatable Gly. *Resolves by:* checking for any C-terminal hydrolase activity (none reported).

---

## Discriminating Tests

- **Isopeptide/GG-remnant proteomics:** IP UBL-5 from worm lysate (± mitochondrial/splicing stress) and search for branched di-glycine remnant peptides — a canonical tag would yield conjugates; UBL-5 should not.
- **C-terminal mutagenesis:** appending or deleting residues at the C-terminus should not affect conjugation (there is none) but should affect fold/partner binding — distinguishing tag vs. binding-module models.
- **Comparative motif/structure analysis:** confirm HIND-binding surface conservation in UBL-5 and absence of a conjugation-competent Gly across the Hub1/UBL5 ortholog set (worm/human/yeast/plant) vs. ubiquitin/SUMO/NEDD8 — already partially done here.
- **AlphaFold geometry:** verify the C-terminal tail is a helix/loop terminating in YYQ (not an extended exposed Gly-Gly), consistent with non-conjugation.

---

## Curation Leads (require curator verification)

- **Action change:** Remove GO:0031386 (protein tag activity, IBA) from ubl-5, or record it as NOT-supported at the family-propagation step. Do **not** replace with bare "protein binding"; prefer a splicing/spliceosome-binding MF if one is warranted.
- **Retain:** GO:0000398 (mRNA splicing, via spliceosome, IBA) — now corroborated in *C. elegans*; GO:0034514 (mtUPR, IMP) as BP; CC terms.
- **Candidate references + exact snippets to verify:**
  - PMID **24872507** — "*Different from canonical ubiquitin-like proteins, Hub1 does not form covalent conjugates with substrates but binds proteins non-covalently.*"
  - PMID **21614000** — "*Hub1 binds non-covalently to a conserved element termed HIND, which is present in the spliceosomal protein Snu66 in yeast and mammals, and Prp38 in plants.*"
  - PMID **36480405** (worm-specific) — "*The ubiquitin-like protein Hub1/UBL-5 associates with proteins non-covalently.*"
  - PMID **25092792** — UBL5 "*primarily associates with spliceosomal proteins*"; depletion → intron retention.
- **Suggested curator question:** Is there any primary *C. elegans* evidence of a covalent UBL-5 conjugate? (None found; expected none.)
- **Suggested experiment:** GG-remnant proteomics on UBL-5 pulldowns to formally close the conjugation question.

---

## Provenance (computed)

- UniProt P91302 FASTA retrieved; length 73; C-terminus `…IHEGFNFELYYQ`; no C-terminal Gly-Gly.
- C-terminal comparison panel (mature/precursor last residues): UBL5_worm `FNFELYYQ` (no GG), UBL5_human `MNLELYYQ` (no GG) vs. ubiquitin `…LRGG`, SUMO1 `…QTGG`, NEDD8 `…LRGG`, ISG15 `…LRGG` (all GG).
- GO:0031386 definition (QuickGO): requires covalent attachment/conjugation; comment restricts to conjugated tags.
- Domain assignment: InterPro IPR039732 (Hub1/Ubl5), IPR000626 (Ubiquitin-like domain); PANTHER PTHR13042 (UBIQUITIN-LIKE PROTEIN 5) — the recognized non-conjugated Ubl clade.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)