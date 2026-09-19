---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T01:00:34.919488'
end_time: '2026-09-01T01:16:10.116666'
duration_seconds: 935.2
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: pol5
  gene_symbol: pol5
  uniprot_accession: O60094
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe 972h-
  focus_type: free_text
  hypothesis_slug: direct-pol-i-regulation
  hypothesis_text: S. pombe Pol5 directly regulates RNA polymerase I transcription
    through sequence-specific binding of the rDNA promoter, rather than acting primarily
    as a ribosome-biogenesis and pre-rRNA-processing factor whose perturbation secondarily
    changes rRNA output.
  term_context: '- Current GOA retains direct rDNA promoter-binding annotations, carries
    a NOT nucleolar large rRNA transcription annotation by ISO, and has retired the
    former IDA rRNA transcription row.'
  reference_context: '- PMID:16816948

    - PMID:31745560'
  source_file: genes/SCHPO/pol5/pol5-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: S. pombe Pol5 directly regulates RNA polymerase\
    \ I transcription through sequence-specific\n  binding of the rDNA promoter, rather\
    \ than acting primarily as a ribosome-biogenesis and pre-rRNA-processing\n  factor\
    \ whose perturbation secondarily changes rRNA output.\nfocus_type: free_text\n\
    context:\n- Current GOA retains direct rDNA promoter-binding annotations, carries\
    \ a NOT nucleolar large rRNA transcription\n  annotation by ISO, and has retired\
    \ the former IDA rRNA transcription row.\nreference_id:\n- PMID:16816948\n- PMID:31745560"
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
citation_count: 7
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
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
- filename: provenance_pol5_evidence_matrix.csv
  path: openscientist_artifacts/provenance_pol5_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pol5 evidence matrix
- filename: provenance_pol5_go_decision_table.csv
  path: openscientist_artifacts/provenance_pol5_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pol5 go decision table
- filename: provenance_pol5_orthology_family_check.md
  path: openscientist_artifacts/provenance_pol5_orthology_family_check.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pol5 orthology family check
- filename: provenance_pol5_polymerase_motif_analysis.md
  path: openscientist_artifacts/provenance_pol5_polymerase_motif_analysis.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pol5 polymerase motif analysis
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe 972h- (NCBITaxon:284812)
- **Gene directory:** pol5
- **Gene symbol:** pol5
- **UniProt accession:** O60094

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** direct-pol-i-regulation
- **Source file:** genes/SCHPO/pol5/pol5-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

S. pombe Pol5 directly regulates RNA polymerase I transcription through sequence-specific binding of the rDNA promoter, rather than acting primarily as a ribosome-biogenesis and pre-rRNA-processing factor whose perturbation secondarily changes rRNA output.

## Term and Decision Context

- Current GOA retains direct rDNA promoter-binding annotations, carries a NOT nucleolar large rRNA transcription annotation by ISO, and has retired the former IDA rRNA transcription row.

## Reference Context

- PMID:16816948
- PMID:31745560

## Source Context YAML

```yaml
hypothesis: S. pombe Pol5 directly regulates RNA polymerase I transcription through sequence-specific
  binding of the rDNA promoter, rather than acting primarily as a ribosome-biogenesis and pre-rRNA-processing
  factor whose perturbation secondarily changes rRNA output.
focus_type: free_text
context:
- Current GOA retains direct rDNA promoter-binding annotations, carries a NOT nucleolar large rRNA transcription
  annotation by ISO, and has retired the former IDA rRNA transcription row.
reference_id:
- PMID:16816948
- PMID:31745560
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

# Pol5 (SCHPO, UniProt O60094) — Hypothesis Review: "Direct Pol I Regulation via Sequence-Specific rDNA-Promoter Binding"

**Gene:** pol5 / SPBC14C8.14c (*Schizosaccharomyces pombe* 972h-, NCBITaxon:284812), UniProt **O60094**
**Hypothesis slug:** direct-pol-i-regulation · **Focus type:** free_text · **Source:** `genes/SCHPO/pol5/pol5-ai-review.yaml`
**Seed hypothesis:** *S. pombe Pol5 directly regulates RNA polymerase I transcription through sequence-specific binding of the rDNA promoter, rather than acting primarily as a ribosome-biogenesis and pre-rRNA-processing factor whose perturbation secondarily changes rRNA output.*

---

## Summary

The seed hypothesis is **refuted as a primary-function claim**, and the "direct RNA-polymerase-I-regulation" reading of Pol5 is best treated as a **legacy over-annotation**. The convergent, mechanistically resolved evidence — most of it from independent studies of the orthologues — places Pol5's primary, direct molecular role in **pre-rRNA processing and ribosome (chiefly 60S) biogenesis** within the nucleolus. The reduction in mature rRNA seen when Pol5 is depleted is most parsimoniously a **downstream consequence of stalled pre-rRNA processing and precursor turnover**, not a loss of Pol I transcription initiation.

The direct-Pol-I model rests on a single primary paper, [PMID:16816948](https://pubmed.ncbi.nlm.nih.gov/16816948/), which reports only two observations: *in vitro* binding to "rDNA promoter fragments" (with no sequence-specificity control) and reduced steady-state rRNA on knockdown (with no nascent-transcription or run-on assay). Both are equally consistent with a processing/assembly factor. Against this, two mechanistically detailed *S. cerevisiae* studies ([PMID:31413149](https://pubmed.ncbi.nlm.nih.gov/31413149/); [PMID:31745560](https://pubmed.ncbi.nlm.nih.gov/31745560/)) establish Pol5 as an essential 60S biogenesis factor that binds **pre-rRNA (RNA)** — the 5′ external transcribed spacer and domain III of 25S rRNA — not promoter DNA. The historical "polymerase" framing (family-B DNA polymerase) has been formally refuted by UniProt (CAUTION, citing PMID:12695662), and a computed motif scan confirms Pol5 lacks the catalytic palm and finger motifs of a genuine family-B polymerase. Finally, the human orthologue MYBBP1A is a nucleolar ribosome-biogenesis factor that acts as an rRNA-transcription **repressor/epigenetic silencer** ([PMID:22686419](https://pubmed.ncbi.nlm.nih.gov/22686419/)) — the opposite polarity of a conserved sequence-specific Pol I *activator*.

The most important caveat is that the *S. pombe* protein itself has not been studied with modern pre-rRNA processing assays; the reclassification rests on strong orthologue data plus UniProt "By similarity." A *S. pombe*-specific transcription-vs-processing experiment would close this gap. Nonetheless, the current GO context — a NOT annotation for nucleolar large rRNA transcription, retirement of the former IDA rRNA-transcription row, and retention of the MYBBP1A-family rRNA-processing annotations — is fully consistent with the refutation.

---

## Key Findings

### Finding 1 — Pol5's primary function is pre-rRNA processing / ribosome biogenesis, not direct Pol I transcription

Two independent mechanistic *S. cerevisiae* studies establish Pol5 as an essential 60S/pre-rRNA processing factor. Ramos-Sáenz et al. 2019 ([PMID:31413149](https://pubmed.ncbi.nlm.nih.gov/31413149/)) "identified the essential nucleolar Pol5 protein as a novel trans-acting factor required for the synthesis of 60S ribosomal subunits." Depletion produces the canonical large-subunit maturation signature: "Both processing of 27SB pre-rRNA to mature 25S rRNA and release of pre-60S ribosomal particles from the nucle(ol)us to the cytoplasm are impaired in the Pol5-depleted strain," accompanied by 60S deficiency and half-mer polysomes, with Pol5 physically associating with pre-60S particles. Braun et al. 2020 ([PMID:31745560](https://pubmed.ncbi.nlm.nih.gov/31745560/)) — one of the two seed-provided references — maps Pol5's physical binding sites and finds them on **RNA, not promoter DNA**: "we identify binding sites for Pol5 in the 5′ external transcribed spacer and within domain III of the 25S rRNA sequence," with roles in 5′ ETS release and formation of the peptide exit tunnel. UniProt O60094 is named "rRNA processing protein pol5," assigns family MYBBP1A, and carries GO:0006364 (rRNA processing) plus ribosome-biogenesis keywords. Critically, the direct-Pol-I claim rests solely on PMID:16816948's in-vitro rDNA-fragment binding and reduced steady-state rRNA on knockdown — with no nascent-transcription or run-on assay to localize the defect to transcription.

### Finding 2 — The DNA-polymerase and sequence-specific rDNA-promoter classifications are legacy/in-vitro-only and unsupported

UniProt O60094 carries an explicit CAUTION note: the protein "Was originally thought to belong to the DNA polymerase type-B family based on conserved motifs (PubMed:12093911). Has later been shown to be unrelated to B class DNA polymerases (PubMed:12695662)." The sole primary support for direct rDNA-promoter regulation is PMID:16816948, which reports that "Pol5p is shown to bind to rDNA promoter fragments" and that "reducing levels of Pol5p inhibits rRNA production" — but demonstrates neither sequence specificity nor nascent transcription. Current GOA carries two IDA annotations traceable to this single paper: GO:0000182 (rDNA binding) and GO:0001163 (RNA polymerase I transcription regulatory region sequence-specific DNA binding). The human orthologue MYBBP1A functions as a nucleolar ribosome-biogenesis factor and, where an rDNA-transcription role is documented, as a **repressor/epigenetic silencer** — Tan & Zhang 2012 ([PMID:22686419](https://pubmed.ncbi.nlm.nih.gov/22686419/)) "identify the nucleolar protein Myb-binding protein 1a (Mybbp1a) as a novel negative regulator of rRNA expression" — contradicting a conserved sequence-specific Pol I *activator* function.

### Finding 3 — Sequence/domain analysis: Pol5 lacks a functional family-B polymerase active site

A computed motif scan of UniProt sequences shows that both *S. pombe* Pol5 (O60094) and *S. cerevisiae* Pol5 (P39985) **lack** the family-B catalytic RegionI palm motif (D-x-x-SLYPS / SLYPS) and RegionIII (K…NS.YG) that the bona fide control polymerase Pol1/CDC17 (P13382) contains (SLYPS@866, YGDTDS@993, KxxxNSxYG@943). Pol5 retains only a degenerate GDTDS ("YAGDTDS"), the vestige that underlies its legacy annotations (InterPro IPR007015 "DNA polymerase V/Myb-binding protein 1A," Pfam PF04931 "DNA polymerase phi," PROSITE PS00116). Without the palm and finger catalytic residues, Pol5 cannot assemble a functional polymerase active site. InterPro instead assigns O60094 an Armadillo/ARM-repeat fold (IPR016024/SSF48371) and PANTHER MYB-binding protein 1A family (PTHR13213) — a nucleic-acid/protein-interaction scaffold, not a polymerase fold and not a canonical sequence-specific DNA-binding domain.

### Finding 4 — Ortholog chain (Sp Pol5 / Sc Pol5 / human MYBBP1A) shares one defining family, justifying processing-annotation transfer

InterPro co-membership shows that *S. pombe* Pol5 (O60094), *S. cerevisiae* Pol5 (P39985), and human MYBBP1A (Q9BQG0) all carry IPR007015, Pfam PF04931, and PANTHER PTHR13213 (MYB-binding protein 1A family). This shared HMM family membership, together with explicit statements in the primary literature (Ramos-Sáenz 2019: "Pol5 is homologous to the human tumor suppressor Myb-binding protein 1A (MYBBP1A)"), establishes the orthology chain and justifies transfer of the processing/biogenesis annotations, especially fungal-to-fungal (Sc→Sp). The sequences are highly diverged (lengths 959/1022/1328; exact 5-mer Jaccard 0.001–0.004, an orientation proxy only), and human MYBBP1A fails to complement yeast pol5Δ (PMID:31413149) — so cross-species transfer of any *regulatory* claim should be made cautiously, while the shared core biogenesis role is well supported.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:16816948](https://pubmed.ncbi.nlm.nih.gov/16816948/) | Direct assay (in vitro binding) + knockdown phenotype | **Supports (weakly)** the seed | Pol5 binds rDNA promoter & is needed for rRNA transcription | Binds rDNA promoter fragments in vitro; knockdown reduces rRNA "production"; nuclear; essential | *S. pombe* | Low. No sequence-specificity test; steady-state readout, not transcription; single paper |
| [PMID:31413149](https://pubmed.ncbi.nlm.nih.gov/31413149/) | Mutant phenotype + particle association | **Refutes** primary Pol I role | Transcription factor or biogenesis factor? | Essential nucleolar 60S biogenesis factor; depletion blocks 27SB→25S; 60S deficit + half-mers | *S. cerevisiae* | High; detailed; orthologue not *S. pombe* |
| [PMID:31745560](https://pubmed.ncbi.nlm.nih.gov/31745560/) | Direct assay (RNA-binding-site mapping) + processing phenotype | **Refutes** promoter-DNA model | What does Pol5 physically bind? | Binds **RNA**: 5′ ETS and 25S domain III; 5′ ETS release; exit-tunnel formation | *S. cerevisiae* | High; RNA not promoter DNA; orthologue |
| [PMID:22686419](https://pubmed.ncbi.nlm.nih.gov/22686419/) | Mechanistic (ChIP/epigenetics) | **Competing / Refutes** conserved-activator model | Does the ortholog activate Pol I via promoter binding? | MYBBP1A is a **negative** regulator / co-repressor of rRNA expression | Human/mouse | Medium-High; opposite polarity to seed |
| [PMID:26044764](https://pubmed.ncbi.nlm.nih.gov/26044764/) | Mechanistic (nucleolar stress) | Qualifies | Ortholog's core cellular role | MYBBP1A released from nucleolus on rRNA-tx block → p53 acetylation → apoptosis | Human | Medium; reinforces nucleolar biogenesis-linked role, not Pol I initiation |
| UniProt O60094 (record) | Database/curation | **Refutes** polymerase framing | Is Pol5 a DNA polymerase? | Named "rRNA processing protein pol5", MYBBP1A family; CAUTION "unrelated to B class DNA polymerases (PubMed:12695662)" | *S. pombe* | High as orientation; database-level |
| This work (motif scan; UniProt) | Structural/evolutionary (sequence) | **Refutes** polymerase framing | Does Pol5 retain a family-B active site? | O60094 & P39985 lack RegionI (SLYPS) and RegionIII (KxxxNSxYG) present in Pol1/CDC17; retain only degenerate GDTDS | In silico | Medium-High; motif-level, not enzymology |
| This work (InterPro) | Structural/evolutionary (orthology) | Qualifies (validates transfer) | Is Sc→Sp processing evidence transferable? | O60094, P39985, Q9BQG0 share IPR007015 / PF04931 / PTHR13213; ARM-repeat fold | In silico + literature | Medium-High; family-level orthology |
| UniProt/PomBase GO set | Database | Context | Current annotation state | IDA GO:0000182 & GO:0001163 both from PMID:16816948; ISO GO:0006364; nucleolus | *S. pombe* | Two IDA DNA-binding rows are single-paper, in-vitro-only |

---

## Mechanistic Model / Interpretation

```
   SEED HYPOTHESIS (refuted)                 SUPPORTED MODEL
   ─────────────────────────                ────────────────
   Pol5 → binds rDNA PROMOTER (DNA)         Pol5 → binds PRE-rRNA (RNA:
        → sequence-specific                       5' ETS + 25S domain III)
        → activates Pol I initiation              → assists 27SB→25S processing
        → increases rRNA transcription            → 60S maturation, exit-tunnel
                                                     formation, 5' ETS release
              │                                          │
              ▼                                          ▼
        (would predict a                          Loss of function →
         nascent-transcription defect)            processing block →
                                                  60S deficiency, half-mers →
                                                  REDUCED steady-state rRNA
                                                  (a DOWNSTREAM consequence)
```

The pivotal point is that **reduced mature rRNA on Pol5 loss is a shared prediction of both models**, so it cannot discriminate them. What discriminates them is (a) *what Pol5 physically binds* — pre-rRNA (RNA), not promoter DNA (PMID:31745560), and (b) *whether nascent transcription is directly reduced* — a measurement never made in PMID:16816948. The directly supported immediate activity is therefore an **RNA-associated ribosome-assembly function in the nucleolus** (binding 5′ ETS / 25S domain III, chaperoning domain-III folding, recruiting exit-tunnel ribosomal proteins, promoting 5′ ETS release and pre-40S factor recycling). The transcriptional readout is a pathway-level, loss-of-function consequence, not a direct gene-product activity. The legacy "polymerase" name and family-B motifs are vestigial: Pol5 lacks the catalytic residues to polymerize and folds as an ARM-repeat MYBBP1A scaffold.

---

## Evidence Base

- ***Pol5 is required for recycling of small subunit biogenesis factors and for formation of the peptide exit tunnel of the large ribosomal subunit*** — Braun et al. 2020, [PMID:31745560](https://pubmed.ncbi.nlm.nih.gov/31745560/). Seed reference. Decisive discriminating study: maps Pol5 binding to **pre-rRNA (5′ ETS, 25S domain III)**, not promoter DNA, and documents the reclassification from B-type polymerase to ribosome-assembly factor. **Refutes** the seed's promoter-DNA premise.
- ***Pol5 is an essential ribosome biogenesis factor required for 60S ribosomal subunit maturation in S. cerevisiae*** — Ramos-Sáenz et al. 2019, [PMID:31413149](https://pubmed.ncbi.nlm.nih.gov/31413149/). Assigns Pol5's essential role to 60S biogenesis; depletion blocks 27SB→25S processing and pre-60S export; establishes MYBBP1A orthology and non-complementation. **Refutes** the transcription-centric model.
- **PMID:16816948** (the origin of the direct-Pol-I annotations), [PMID:16816948](https://pubmed.ncbi.nlm.nih.gov/16816948/). Seed reference. Reports in-vitro rDNA-fragment binding and reduced rRNA on knockdown — the sole basis for GO:0000182 and GO:0001163, but lacking sequence-specificity and nascent-transcription controls. **Weakly supports** the seed; the ambiguity here underlies the whole hypothesis.
- ***Epigenetic silencing of ribosomal RNA genes by Mybbp1a*** — Tan & Zhang 2012, [PMID:22686419](https://pubmed.ncbi.nlm.nih.gov/22686419/). Human orthologue is a **negative** regulator of rRNA expression. **Competes with / refutes** a conserved sequence-specific Pol I activator model.
- ***Gradual reduction in rRNA transcription triggers p53 acetylation and apoptosis via MYBBP1A*** — Kumazawa et al. 2015, [PMID:26044764](https://pubmed.ncbi.nlm.nih.gov/26044764/). Places MYBBP1A in a nucleolar ribosome-biogenesis/stress-sensing role. **Qualifies** — reinforces nucleolar biogenesis context, not promoter activation.
- **UniProt O60094 / InterPro (database-level).** Name "rRNA processing protein pol5"; MYBBP1A family; CAUTION that it is unrelated to B-class DNA polymerases (PMID:12695662 superseding PMID:12093911); ARM-repeat fold (IPR016024) and PANTHER PTHR13213. **Refutes** the polymerase framing.

---

## Limitations and Knowledge Gaps

1. **No *S. pombe* nascent-transcription assay.** Checked: PMID:16816948 measured steady-state rRNA only. This is the crux of transcription-vs-processing. Resolve with metabolic labeling / Pol I run-on / 4sU-seq in a *pol5* shut-off *S. pombe* strain.
2. **No test of sequence specificity or DNA-vs-RNA preference for *S. pombe* Pol5.** Checked: PMID:16816948 fragment binding was not competed/specificity-controlled; PMID:31745560 shows RNA binding only in *S. cerevisiae*. Matters directly for GO:0001163. Resolve with EMSA competition, SELEX, or ChIP-seq vs CRAC/CLIP in *S. pombe*.
3. **Whether *S. pombe* Pol5 depletion causes the same 27SB/25S processing defect and half-mer polysomes.** Checked: only shown in *S. cerevisiae*. Resolve with northern/primer-extension pre-rRNA analysis and polysome profiling in *S. pombe*.
4. **Motif scan is orientation-level only.** In-silico motif absence supports but does not prove the lack of catalysis; a published structure would settle the ARM-scaffold assignment definitively.
5. **Cross-species transfer caveat.** Human MYBBP1A fails to complement yeast pol5Δ (PMID:31413149), so human data inform polarity/direction but not per-residue *S. pombe* function.

---

## Discriminating Tests

1. **Metabolic labeling / Pol I transcription run-on in *S. pombe* pol5 shut-off** — directly separates transcription (unchanged = processing model) from initiation loss (seed model). *Most decisive.*
2. **In vivo crosslinking (CRAC/CLIP) vs ChIP-seq in *S. pombe*** — DNA-promoter occupancy vs pre-rRNA binding. Predicted: pre-rRNA binding dominates (processing model).
3. **Pre-rRNA processing analysis (northern/primer extension) + polysome profiling** in *S. pombe* — expect a 27S-equivalent processing block, 60S deficit, and half-mers, as in *S. cerevisiae*.
4. **EMSA specificity controls** on the PMID:16816948 rDNA fragment — competition with nonspecific DNA/RNA to test whether "promoter binding" is sequence-specific.
5. **Domain-swap / point-mutant complementation** in *S. pombe* (e.g., RNA-binding surface) to map the essential activity to processing rather than transcription.

---

## Proposed Follow-up Actions — GO Curation Leads (require curator verification)

| GO term | Aspect | Current status | Recommended action | Rationale |
|---|---|---|---|---|
| **GO:0001163** RNA Pol I regulatory-region *sequence-specific* DNA binding | MF | IDA (PMID:16816948) | **Remove or strongly downgrade** | Sequence specificity never demonstrated; orthologue binds pre-rRNA, not promoter DNA; most over-reaching term |
| **GO:0000182** rDNA binding | MF | IDA (PMID:16816948) | **Downgrade / flag non-core**; consider generalizing to nucleic-acid binding | Single-paper in-vitro fragment binding; no specificity control |
| **GO:0006364** rRNA processing | BP | Retained | **Retain (core)** | Directly supported by PMID:31413149, 31745560; UniProt name/family |
| **GO:0042254** ribosome biogenesis / 60S maturation | BP | Retained (keyword) | **Retain (core)**; consider a more specific LSU-rRNA / 60S maturation term "By similarity" | 27SB→25S block, half-mers, pre-60S association |
| **GO:0005730** nucleolus | CC | Retained | **Retain** | Nucleolar localization conserved across orthologues |
| NOT nucleolar large rRNA transcription (ISO) | BP | NOT annotation | **Retain the NOT** | Consistent with refutation of direct transcription role |
| pre-rRNA / RNA binding | MF | (not currently primary) | **Consider adding as a lead** | PMID:31745560 maps direct binding to 5′ ETS and 25S domain III |

**Candidate references / snippets to verify:**
- PMID:31745560 — *"we identify binding sites for Pol5 in the 5' external transcribed spacer and within domain III of the 25S rRNA sequence"* (RNA, not promoter DNA).
- PMID:31413149 — *"we identified the essential nucleolar Pol5 protein as a novel trans-acting factor required for the synthesis of 60S ribosomal subunits"* (primary role = biogenesis).
- PMID:22686419 — *"identify the nucleolar protein Myb-binding protein 1a (Mybbp1a) as a novel negative regulator of rRNA expression"* (ortholog is a repressor).
- UniProt O60094 CAUTION — Pol5 "shown to be unrelated to B class DNA polymerases (PubMed:12695662)".

**Suggested curator question:** Does any primary *S. pombe* dataset measure Pol I transcription (not steady-state rRNA) for pol5? If not, the "direct Pol I regulation" annotations should not be treated as core.

**Suggested experiment for authors:** *S. pombe* pol5 shut-off + 4sU/run-on + CRAC to definitively assign transcription vs processing and DNA vs RNA binding.

---

## Provenance

- UniProt O60094 record programmatically retrieved (family = MYBBP1A; name "rRNA processing protein pol5"; GO set including IDA GO:0000182, GO:0001163 and ISO GO:0006364; CAUTION regarding DNA-pol-B misclassification).
- Motif scan (UniProt REST + regex) across O60094, P39985 (Sc Pol5), and P13382 (Pol1/CDC17 control): Pol5 orthologues lack RegionI (SLYPS) and RegionIII (KxxxNSxYG) catalytic motifs and retain only a degenerate GDTDS; control polymerase contains SLYPS@866, YGDTDS@993, KxxxNSxYG@943.
- InterPro co-membership check: O60094, P39985, Q9BQG0 all carry IPR007015 / PF04931 / PTHR13213; O60094 additionally ARM-repeat (IPR016024/SSF48371).
- Abstracts for PMID:16816948, 31745560, 31413149 retrieved via NCBI efetch; MYBBP1A orthologue papers (22686419, 26044764) via PubMed.
- Analysis is literature/annotation/sequence based; no primary *S. pombe* wet-lab data were generated. Orthologue inferences are labeled as such and reported conservatively.

---

## Conclusion

The direct-Pol-I-regulation hypothesis for *S. pombe* Pol5 is **refuted / over-annotated**. Pol5's primary, directly supported function is **pre-rRNA processing and 60S ribosome biogenesis in the nucleolus**, with direct binding to **pre-rRNA (RNA), not the rDNA promoter DNA**. The reduced rRNA output on Pol5 loss is a downstream consequence of a processing block, and the two single-paper, in-vitro IDA DNA-binding GO terms (GO:0000182, GO:0001163) should be removed or downgraded, while the rRNA-processing, ribosome-biogenesis, nucleolus, and NOT-large-rRNA-transcription annotations are retained.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist pol5 evidence matrix](openscientist_artifacts/provenance_pol5_evidence_matrix.csv)
- [OpenScientist pol5 go decision table](openscientist_artifacts/provenance_pol5_go_decision_table.csv)
- [OpenScientist pol5 orthology family check](openscientist_artifacts/provenance_pol5_orthology_family_check.md)
- [OpenScientist pol5 polymerase motif analysis](openscientist_artifacts/provenance_pol5_polymerase_motif_analysis.md)