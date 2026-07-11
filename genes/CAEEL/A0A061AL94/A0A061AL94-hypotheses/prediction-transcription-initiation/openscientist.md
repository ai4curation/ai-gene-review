---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-09T05:21:34.700715'
end_time: '2026-07-09T05:31:15.354919'
duration_seconds: 580.65
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: CAEEL
  gene: A0A061AL94
  gene_symbol: mcm-4
  uniprot_accession: A0A061AL94
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: computational_prediction
  hypothesis_slug: prediction-transcription-initiation
  hypothesis_text: ProtNLM2 predicts transcription initiation at RNA polymerase II
    promoter (GO:0006367) for the Caenorhabditis elegans protein A0A061AL94 (MCM-4).
    Independently assess whether A0A061AL94 is a minichromosome-maintenance (MCM2-7
    family) replicative DNA helicase / replication-licensing factor -- whose function
    is DNA replication initiation, not RNA polymerase II transcription initiation
    -- and therefore whether the transcription-initiation prediction is supported
    or is a misassignment (for example a frequency-bias conflation of DNA-replication
    initiation with transcription initiation). Determine whether the prediction is
    supported or refuted.
  term_context: '- Term: transcription initiation at RNA polymerase II promoter (GO:0006367)'
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: ProtNLM2 predicts transcription initiation at\
    \ RNA polymerase II promoter (GO:0006367) for\n  the Caenorhabditis elegans protein\
    \ A0A061AL94 (MCM-4). Independently assess whether A0A061AL94 is a\n  minichromosome-maintenance\
    \ (MCM2-7 family) replicative DNA helicase / replication-licensing factor --\n\
    \  whose function is DNA replication initiation, not RNA polymerase II transcription\
    \ initiation -- and\n  therefore whether the transcription-initiation prediction\
    \ is supported or is a misassignment (for example\n  a frequency-bias conflation\
    \ of DNA-replication initiation with transcription initiation). Determine\n  whether\
    \ the prediction is supported or refuted.\nfocus_type: computational_prediction\n\
    term_id: GO:0006367\nterm_label: transcription initiation at RNA polymerase II\
    \ promoter\ncontext: []\nreference_id: []"
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

- **Organism code:** CAEEL
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** A0A061AL94
- **Gene symbol:** mcm-4
- **UniProt accession:** A0A061AL94

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-transcription-initiation
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

ProtNLM2 predicts transcription initiation at RNA polymerase II promoter (GO:0006367) for the Caenorhabditis elegans protein A0A061AL94 (MCM-4). Independently assess whether A0A061AL94 is a minichromosome-maintenance (MCM2-7 family) replicative DNA helicase / replication-licensing factor -- whose function is DNA replication initiation, not RNA polymerase II transcription initiation -- and therefore whether the transcription-initiation prediction is supported or is a misassignment (for example a frequency-bias conflation of DNA-replication initiation with transcription initiation). Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: transcription initiation at RNA polymerase II promoter (GO:0006367)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: ProtNLM2 predicts transcription initiation at RNA polymerase II promoter (GO:0006367) for
  the Caenorhabditis elegans protein A0A061AL94 (MCM-4). Independently assess whether A0A061AL94 is a
  minichromosome-maintenance (MCM2-7 family) replicative DNA helicase / replication-licensing factor --
  whose function is DNA replication initiation, not RNA polymerase II transcription initiation -- and
  therefore whether the transcription-initiation prediction is supported or is a misassignment (for example
  a frequency-bias conflation of DNA-replication initiation with transcription initiation). Determine
  whether the prediction is supported or refuted.
focus_type: computational_prediction
term_id: GO:0006367
term_label: transcription initiation at RNA polymerase II promoter
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

# AIGR Deep Research Report — *mcm-4* (A0A061AL94, *C. elegans*)

**Hypothesis under review (computational_prediction):** ProtNLM2 predicts *transcription initiation at RNA polymerase II promoter* (GO:0006367) for A0A061AL94 (MCM-4). Is A0A061AL94 instead a minichromosome-maintenance (MCM2-7) replicative DNA helicase / replication-licensing factor, making the prediction a misassignment?

---

## Executive Judgment

**Verdict: REFUTED (prediction is a misassignment / over-annotation).**

A0A061AL94 is unambiguously a fragment of the MCM2-7 replicative DNA helicase subunit **MCM4**, not an RNA polymerase II transcription-initiation factor. The evidence is decisive and computationally verifiable:

1. A0A061AL94 is a **74-aa sequence** (WormBase locus **Y39G10AR.14b**, gene *mcm-4*), submission-named by UniProt "*DNA replication licensing factor mcm-4*".
2. Its **only Pfam domain is PF21128 = "MCM4, winged helix domain" (WHD_MCM4)** — an MCM4-specific signature.
3. Its sequence is an **exact substring (residues 750–823, the C-terminal 74 aa) of the reviewed Swiss-Prot entry MCM4_CAEEL (Q95XQ8, 823 aa)**. A0A061AL94 is therefore the isolated C-terminal winged-helix domain of full-length *C. elegans* MCM4.
4. The reviewed parent entry (Q95XQ8) carries only DNA-replication GO terms (DNA helicase activity, ATP binding/hydrolysis, ssDNA binding, Zn binding, MCM complex, mitotic DNA replication initiation, premeiotic DNA replication, DNA strand elongation). **No transcription-related GO term appears.**

The most likely source of the ProtNLM2 error: the **winged-helix (WHD) fold** is a generic DNA-binding module shared by many bona-fide transcription factors, and a language model conflates **"DNA replication initiation" with "transcription initiation"** (frequency bias on the word "initiation"). GO:0006367 should **not** be applied to this gene product.

**Caveat:** A0A061AL94 is a 74-aa fragment, so it lacks the catalytic AAA+/Walker motifs (which lie in the parent's PF00493 domain upstream); the family assignment nonetheless rests on the MCM4-specific WHD signature and exact identity to the reviewed full-length MCM4.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt A0A061AL94 (database record) | Database / computational | Refutes prediction | Identity of A0A061AL94 | Gene *mcm-4*; submission name "DNA replication licensing factor mcm-4"; sole Pfam PF21128 = MCM4 winged-helix domain | *C. elegans*, WormBase Y39G10AR.14b | High; database-level, but corroborated below |
| InterPro/Pfam PF21128 (database) | Structural/evolutionary | Refutes | Domain identity of the 74-aa fragment | PF21128 = "MCM4, winged helix domain" — an MCM4-specific WHD | Family signature | High |
| UniProt Q95XQ8 MCM4_CAEEL (reviewed) + own sequence alignment | Structural/evolutionary (computed) | Refutes | Is A0A061AL94 part of MCM4? | 74-aa fragment is an **exact match to residues 750–823** (C-terminus) of reviewed 823-aa MCM4_CAEEL; parent has PF00493 (MCM AAA+), PF17855, PF14551, PF17207, PF21128 | *C. elegans* | High; exact string identity computed in-run |
| UniProt Q95XQ8 curated GO set | Review/database | Refutes | Function of MCM4 | GO: DNA helicase activity (GO:0003678), ATP binding/hydrolysis, ssDNA binding, Zn binding, MCM complex, **mitotic DNA replication initiation (GO:1902975)**, premeiotic DNA replication, DNA strand elongation; **no transcription term** | *C. elegans* | High |
| Yang et al. 2026, PMID 41448435 | Review/mechanistic (human) | Qualifies (family biology) | MCM2-7 role | ORC/CDC6/CDT1 load MCM2-7 double hexamers to license replication origins — replication initiation, not transcription | Human, in vitro reconstitution | High for family; heterologous organism |
| Tomkins et al. 2025, PMID 41365879 | Mechanistic (human) | Qualifies | MCM2-7 role | MCM2-7 helicase loaded onto origins in G1; geminin/CDT1 licensing control | Human | High for family |
| Yuan et al. 2017, PMID 28191893 | Structural (cryo-EM, 3.9 Å) | Refutes | Function of MCM winged-helix domains | In the OCCM loading intermediate, flexible Mcm2-7 **WHDs engage ORC-Cdc6**; Mcm6 WHD binds Orc4 WHD — WHDs are replication-licensing structural elements | *S. cerevisiae* | High; the exact domain class of A0A061AL94 |
| Zhai et al. 2017, PMID 28191894 | Structural (cryo-EM) | Refutes | Role of MCM C-terminal WHD | Mcm5 C-terminal WHD occludes the central channel of the Cdt1-Mcm2-7 helicase precursor (double-hexamer formation) | *S. cerevisiae* | High; helicase context, not transcription |
| Miller & Winston 2023, PMID 36924499 | Genetic/genomic | Competing→resolved | Any MCM–transcription link | Related hit explicitly **separates** replication (MCM origin loading) from RNAPII transcription; no MCM transcription-initiation activity | *S. cerevisiae* | Rules out a moonlighting confound |

---

## GO Curation Implications

- **GO:0006367 (transcription initiation at RNA Pol II promoter, BP): REJECT / do not add.** No experimental or reliable computational support; it conflicts with the well-established replicative-helicase identity. This is a paralog-independent misassignment driven by domain-fold ambiguity and word-frequency bias.
- **Supported terms for *mcm-4* (from reviewed parent Q95XQ8), as leads requiring curator verification:**
  - MF: **DNA helicase activity (GO:0003678)**, ATP hydrolysis activity (GO:0016887), ATP binding (GO:0005524), single-stranded DNA binding (GO:0003697).
  - BP: **mitotic DNA replication initiation (GO:1902975)**, DNA strand elongation involved in DNA replication (GO:0006271), premeiotic DNA replication (GO:0006279).
  - CC: **MCM complex (GO:0042555)**, nucleus (GO:0005634), chromosome (GO:0005694).
- Because A0A061AL94 is only the **C-terminal WHD fragment**, MF catalytic terms describe the full protein/complex; for this isoform record, the WHD's role is regulatory/DNA-binding within the CMG helicase. "Protein binding" is not needed — more informative replication terms apply.

---

## Mechanistic Scope

The immediate molecular function of MCM4 is as a subunit of the **MCM2-7 hexameric ATPase**, the catalytic core of the eukaryotic **CMG (CDC45–MCM–GINS) replicative DNA helicase**. Its processes are **origin licensing and replication-fork unwinding during DNA replication initiation and elongation** — a *DNA*-templated process at replication origins, mechanistically distinct from **RNA polymerase II transcription initiation at promoters**. The 74-aa C-terminal **winged-helix domain** contributes DNA binding/regulatory contacts within the helicase; it is not an RNA Pol II general transcription factor and is not part of the pre-initiation complex machinery (TFIIA/B/D/E/F/H, Mediator, Pol II).

Downstream *mcm-4* loss-of-function phenotypes in the parent record (gonad development, premeiotic DNA replication, nervous-system development, locomotion) are **secondary consequences of impaired replication**, not evidence of a transcription-initiation activity.

---

## Conflicts and Alternatives

- **No credible conflicting evidence** supports a transcription-initiation role. The prediction stands alone against domain, orthology, exact-sequence, and curated-GO evidence.
- **Alternative explanation for the prediction (favored):** WHD fold ambiguity (winged-helix domains occur in many transcription factors) + language-model frequency-bias conflation of "replication initiation" ↔ "transcription initiation." This is a classic ProtNLM naming artifact, not paralog confusion.
- **Moonlighting confound checked and rejected (Iteration 2):** A targeted search for an MCM/RNA-Pol-II transcription-initiation moonlighting activity returned no supporting primary evidence. The most relevant hit (PMID 36924499) explicitly separates MCM's replication role from RNAPII transcription. Cryo-EM structures (PMID 28191893, 28191894) show the MCM WHD — the exact domain of A0A061AL94 — functions in origin licensing (engaging ORC-Cdc6), not at Pol II promoters.
- **AlphaFold check (could-not-run):** AlphaFold DB has no deposited model for A0A061AL94 or the reviewed parent Q95XQ8 (both HTTP 404), so a per-residue pLDDT/fold confirmation could not be executed; the WHD fold is instead established from the Pfam PF21128 signature and the cryo-EM literature above.
- **Fragment caveat:** the 74-aa isoform lacks Walker A/B and the MCM box (in the upstream AAA+ region), so catalytic MF terms should be curated on the full-length protein rather than asserted from this fragment alone.

---

## Knowledge Gaps

1. **Isoform-specific function of Y39G10AR.14b (the 74-aa product).** Checked: it maps exactly to the MCM4 C-terminus. Gap: whether this short isoform is independently expressed/functional. Matters because GO on isoform records should reflect the isoform. Resolution: WormBase expression/isoform annotation, RNA-seq isoform evidence.
2. **No PMID directly assaying *C. elegans* mcm-4 transcription activity** (correctly — none is expected). Resolution: none needed; absence is consistent with refutation.

---

## Discriminating Tests

- **Domain/sequence (done):** Pfam = MCM4 WHD; exact identity to reviewed MCM4 C-terminus → replication, not transcription. ✔
- **Orthology:** OrthoDB group 10251574at2759 clusters with eukaryotic MCM4 orthologs (replicative helicase), not with RNA Pol II GTFs.
- **Complex membership / interactome:** MCM4 co-purifies with MCM2/3/5/6/7 (MCM complex), CDC45, GINS — not with TFIID/Mediator/Pol II. A physical-interaction check would further discriminate.
- **Structural:** AlphaFold model of the 74-aa fragment should adopt a compact winged-helix fold consistent with MCM4 C-terminal WHD.

---

## Curation Leads (require curator verification)

- **Action:** Do **not** annotate *mcm-4*/A0A061AL94 with GO:0006367; flag the ProtNLM2 prediction as a false positive (fold-ambiguity + "initiation" frequency bias).
- **Replacement terms (leads):** MF GO:0003678 (DNA helicase activity); BP GO:1902975 (mitotic DNA replication initiation); CC GO:0042555 (MCM complex) — transfer with appropriate evidence codes / IBA from the reviewed parent Q95XQ8.
- **Candidate reference to verify (snippet):** UniProt reviewed entry **Q95XQ8 (MCM4_CAEEL)** curated GO includes "mitotic DNA replication initiation" and "MCM complex," with no transcription term — supporting rejection of GO:0006367.
- **Suggested question for curator:** Should isoform record A0A061AL94 (74-aa WHD fragment) inherit full-length MCM4 MF/BP terms, or carry only CC/domain-appropriate annotation?
- **Suggested experiment:** Confirm MCM-complex co-fractionation / interactome membership of the mcm-4 gene product to formally exclude any Pol II association.

---

## Paralog-Specificity Confirmation (Iteration 3)

To exclude MCM-paralog confusion, the 74-aa fragment was tested for exact-substring membership across the reviewed *C. elegans* MCM2-7 subunits. It is contained **only in Q95XQ8 (MCM4, 823 aa)** and is **absent** from the reviewed mcm-5 (Q21902, 759 aa) and mcm-6 (P34647, 810 aa) sequences. This confirms A0A061AL94 is specifically an MCM4 fragment, not a mis-mapped paralog. (UniProt gene-name search is fuzzy and returned some cross-hits by accession, but the substring test is unambiguous.)

## Provenance

Computed in-run: UniProt REST fetch of A0A061AL94 (74 aa, gene *mcm-4*, Pfam PF21128 = MCM4 WHD) and Q95XQ8 (MCM4_CAEEL, 823 aa); exact-substring alignment placing the fragment at residues 750–823 (C-terminal WHD); enumeration of Q95XQ8 curated GO terms (all DNA-replication, none transcription); InterPro/Pfam lookup identifying PF21128 as "MCM4, winged helix domain."


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)