---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-17T14:55:18.343714'
end_time: '2026-09-17T15:06:05.449452'
duration_seconds: 647.11
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: GCNT1
  gene_symbol: GCNT1
  uniprot_accession: Q02742
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0016607
  hypothesis_text: GCNT1 has nuclear speck (GO:0016607).
  term_context: '- Term: nuclear speck (GO:0016607)

    - Evidence type: IDA

    - Original reference: GO_REF:0000052'
  reference_context: '- GO_REF:0000052

    - PMID:23027862

    - PMID:1329093'
  source_file: genes/human/GCNT1/GCNT1-ai-review.yaml
  source_selector: existing_annotations[16].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0016607\n  label: nuclear speck\nevidence_type:\
    \ IDA\noriginal_reference_id: GO_REF:0000052"
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
- **Gene directory:** GCNT1
- **Gene symbol:** GCNT1
- **UniProt accession:** Q02742

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016607
- **Source file:** genes/human/GCNT1/GCNT1-ai-review.yaml
- **Source selector:** existing_annotations[16].function_hypothesis

## Seed Hypothesis

GCNT1 has nuclear speck (GO:0016607).

## Term and Decision Context

- Term: nuclear speck (GO:0016607)
- Evidence type: IDA
- Original reference: GO_REF:0000052

## Reference Context

- GO_REF:0000052
- PMID:23027862
- PMID:1329093

## Source Context YAML

```yaml
term:
  id: GO:0016607
  label: nuclear speck
evidence_type: IDA
original_reference_id: GO_REF:0000052
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

# GCNT1 Nuclear Speck (GO:0016607) — Function-Assignment Hypothesis Review

**Gene:** GCNT1 (Q02742), *Homo sapiens* — Beta-1,3-galactosyl-O-glycosyl-glycoprotein beta-1,6-N-acetylglucosaminyltransferase (core-2 GlcNAc-transferase, C2GnT-L)
**Focus type:** function_assignment | **Hypothesis slug:** function-hypothesis-go-0016607
**Seed hypothesis:** "GCNT1 has nuclear speck (GO:0016607)."
**Annotation under review:** GO:0016607 nuclear speck, evidence **IDA**, original reference **GO_REF:0000052** (Human Protein Atlas immunofluorescence; UniProt cross-reference evidence code **IDA:HPA**).

---

## Summary

**Verdict: Weakly supported / over-annotated — do not treat as a core localization.** The proposed cellular-component assignment of GCNT1 to the **nuclear speck (GO:0016607)** rests on a **single Human Protein Atlas (HPA) immunofluorescence antibody pattern**, imported automatically under evidence code IDA with reference GO_REF:0000052. It is contradicted by the strong, independent, and mechanistically coherent evidence establishing GCNT1 as a **single-pass type II Golgi membrane glycosyltransferase** whose catalytic domain faces the Golgi lumen. Such a protein has no known trafficking route into the nuclear interior and no plausible role in membraneless nuclear-speckle condensates, which are liquid–liquid phase-separated assemblies of splicing factors. No primary literature reports a nuclear pool or nuclear function of GCNT1, and the enzyme's established biochemistry — core-2 O-glycan branching using lumenal UDP-GlcNAc — is a Golgi-luminal process.

A comparative check of HPA subcellular records across twelve Golgi type II glycosyltransferases (GCNT1–4, B3GNT6, C1GALT1, ST3GAL1, ST6GALNAC1, GALNT1, MGAT1, B4GALT1, FUT8) reinforces this reading. GCNT1 is the **only** enzyme in the panel (1/12) reported with "Nuclear speckles," it is reported as the **sole main location**, and — uniquely — it carries **no Golgi call at all** in HPA immunofluorescence. Its peers with informative HPA IF data recover the Golgi as expected, and three that also show a "Nucleoplasm" background call still retain the Golgi, reflecting a recognized HPA nuclear-artifact tendency for this membrane-enzyme class. The complete substitution of GCNT1's biochemically established Golgi compartment by an outlier speckle call is the signature of an antibody artifact, not a genuine dual localization.

**Curation lead (requires curator verification):** Treat GO:0016607 as **non-core** for GCNT1 — a candidate for **removal** or a **NOT qualifier** pending orthogonal validation (second independent antibody, knockout-validated stain, endogenous tagging, or fractionation). Retain the Golgi CC terms (GO:0000139 Golgi membrane, GO:0005802 trans-Golgi network, GO:0031985 Golgi cisterna) and the core-2 branching MF/BP terms as the gene product's true location and function. The nuclear-speck term should not influence the gene review as a bona fide localization.

---

## Key Findings

### Finding 1 — The nuclear-speck term is a single unvalidated HPA immunofluorescence call, at odds with GCNT1's Golgi membrane topology

GCNT1 (UniProt Q02742) is a **428-residue single-pass type II membrane protein** with a short cytoplasmic tail (residues 1–9), a transmembrane anchor (residues 10–32), and a large lumenal catalytic domain (residues 33–428). Its curated UniProt subcellular location is **Golgi apparatus membrane**, and its GO cellular-component annotations are dominated by Golgi compartments: Golgi cisterna (GO:0031985, IDA), Golgi membrane (GO:0000139, EXP), and trans-Golgi network (GO:0005802, IDA). Against this backdrop, the nuclear-speck term (GO:0016607) is supported by exactly one line of evidence — **IDA:HPA**, reference **GO_REF:0000052** — i.e., an automated import of a Human Protein Atlas immunofluorescence result. In the HPA record (ENSG00000187210), "Nuclear speckles" is listed as the sole main subcellular location with an IF reliability of "Supported," while the immunohistochemistry reliability for the same gene is only "Uncertain."

The membrane topology is decisive. A type II Golgi glycosyltransferase is inserted into the Golgi membrane with its catalytic domain in the lumen; it is synthesized on the rough ER and trafficked through the secretory pathway, with no signal, mechanism, or precedent for entering the nucleus, let alone partitioning into membraneless nuclear-speckle condensates. The original molecular cloning of GCNT1 explicitly reported type II membrane topology:

> *"The cDNA sequence predicts a protein with type II membrane topology, as has been found for all other mammalian glycosyltransferases cloned to date."*
> — [PMID: 1329093](https://pubmed.ncbi.nlm.nih.gov/1329093/)

No primary study reports a nuclear pool or nuclear activity for GCNT1. The enzyme's biochemical function — building the core-2 branch of mucin-type O-glycans by transferring GlcNAc from UDP-GlcNAc onto Galβ1-3GalNAc-R ([PMID: 1329093](https://pubmed.ncbi.nlm.nih.gov/1329093/); [PMID: 23027862](https://pubmed.ncbi.nlm.nih.gov/23027862/)) — is intrinsically a Golgi-luminal reaction dependent on the nucleotide-sugar donor and the Golgi glycosylation machinery. There is no substrate, donor, or acceptor for this chemistry in nuclear speckles.

### Finding 2 — GCNT1 is the lone Golgi glycosyltransferase HPA calls "nuclear speckles," and it uniquely misses the Golgi entirely

To test whether the nuclear-speckle call is a systematic property of Golgi glycosyltransferases or an isolated outlier, HPA subcellular records were compared across twelve Golgi type II glycosyltransferases: GCNT1, GCNT2, GCNT3, GCNT4, B3GNT6, C1GALT1, ST3GAL1, ST6GALNAC1, GALNT1, MGAT1, B4GALT1, and FUT8.

Two features single GCNT1 out:

1. **GCNT1 is the only gene (1/12) reported with "Nuclear speckles,"** and it is reported as the **sole main location**.
2. **GCNT1 uniquely carries no Golgi call in HPA immunofluorescence.** Enzymes in the panel with informative HPA IF data (GCNT3, ST6GALNAC1, B4GALT1, FUT8, GCNT4) show "Golgi apparatus" as expected. Three of them (GCNT4, ST6GALNAC1, FUT8) additionally show a "Nucleoplasm" background call — a known HPA nuclear-artifact pattern for membrane proteins — but all of them still recover the Golgi.

| Gene | HPA main location | HPA all locations |
|---|---|---|
| **GCNT1** (target) | **Nuclear speckles** | **Nuclear speckles** (no Golgi) |
| GCNT3 | Golgi apparatus | Golgi apparatus, Vesicles |
| GCNT4 | Golgi apparatus | Nucleoplasm, Golgi apparatus |
| ST6GALNAC1 | Golgi apparatus | Nucleoplasm, Golgi apparatus |
| B4GALT1 | Golgi apparatus | Golgi apparatus |
| FUT8 | Golgi apparatus | Nucleoplasm, Golgi apparatus, Cytosol |
| GCNT2, B3GNT6, C1GALT1, ST3GAL1, GALNT1, MGAT1 | (no HPA IF loc data) | — |

GCNT1 is therefore doubly anomalous: it gains an implausible nuclear-speckle call **and** loses the compartment where its biochemistry is known to occur. A genuinely dual-localized protein would be expected to retain a Golgi signal alongside any secondary compartment. GCNT1's speckle call **replaces** rather than **supplements** the expected Golgi signal — the classic signature of an antibody that binds an off-target, speckle-enriched epitope while failing to detect the true Golgi target. The nucleoplasm background calls in three other Golgi GTs confirm that HPA has a recognized nuclear-artifact tendency for this membrane-enzyme class, reinforcing the artifact interpretation.

---

## Mechanistic Model / Interpretation

The competing interpretations can be laid out compactly:

```
  SEED HYPOTHESIS                        ESTABLISHED BIOLOGY
  ---------------                        -------------------
  GCNT1 -> nuclear speck                 GCNT1 = type II Golgi membrane enzyme
  (GO:0016607)                            cytoplasmic tail (1-9)
        |                                 TM anchor (10-32)
        | single HPA IF antibody          lumenal catalytic domain (33-428)
        | evidence IDA (GO_REF:0000052)         |
        v                                        v
  membraneless splicing-factor           core-2 O-glycan branching
  condensate in the nucleus              UDP-GlcNAc -> Galb1-3GalNAc-R
        |                                 in the GOLGI LUMEN
        |  no donor, no acceptor,               |
        |  no trafficking route,                v
        |  no primary literature         PMID:1329093, PMID:23027862,
        v                                PMID:9915862, PMID:8308016
   NOT MECHANISTICALLY VIABLE
```

Nuclear speckles (GO:0016607) are interchromatin granule clusters enriched in pre-mRNA splicing factors (e.g., SRRM2/SC35, SR proteins). They are liquid–liquid phase-separated bodies, not membrane compartments, and their resident proteins characteristically have intrinsically disordered regions and RNA-binding capacity — for example, galectin-3 partitions into speckles via an intrinsically disordered domain and ribonucleoprotein association ([PMID: 37003559](https://pubmed.ncbi.nlm.nih.gov/37003559/)). GCNT1 has none of these properties: it is a folded, membrane-anchored, lumenal glycosyltransferase with no reported disordered speckle-targeting region and no RNA-binding role.

The most parsimonious explanation is that the HPA antibody produces a punctate nuclear pattern that the automated HPA pipeline classified as "nuclear speckles," while failing to detect the true Golgi pool. This yields a single-antibody, single-modality IDA annotation that propagated into GO via GO_REF:0000052. It is exactly the class of annotation that hypothesis-level review is designed to catch: technically an IDA, but biologically an uncorroborated localization that conflicts with the gene product's core molecular identity.

---

## Evidence Base

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| HPA ENSG00000187210 (GO_REF:0000052) | Localization (IF) | Supports (sole basis) | GCNT1 in nuclear speckles | Main location "Nuclear speckles"; Reliability(IF)=**Supported**; Reliability(IH)=**Uncertain** | Cultured human cell lines, single antibody IF | Low–moderate: "Supported" = internal consistency, not orthogonal validation; antibody independence not shown |
| UniProt Q02742 (curated) | Structural/topology, curated CC | Refutes/qualifies | Where does GCNT1 reside | Golgi apparatus membrane; type II single-pass TM; lumenal catalytic domain (33–428); GO CC Golgi cisterna/membrane/TGN | Human, Swiss-Prot review | High: multiple independent Golgi lines |
| [PMID: 1329093](https://pubmed.ncbi.nlm.nih.gov/1329093/) | Direct assay + sequence | Refutes | Molecular nature of GCNT1 | Type II membrane topology; forms core-2 O-glycan branch | Expression cloning, CHO/COS | High: original characterization |
| [PMID: 23027862](https://pubmed.ncbi.nlm.nih.gov/23027862/) | Enzymatic characterization | Qualifies (function only) | Catalytic activity | Basis of UniProt FUNCTION (core-2 branching); no nuclear claim | In vitro / cellular glyco-assay | Function, not localization |
| [PMID: 9915862](https://pubmed.ncbi.nlm.nih.gov/9915862/) | Direct assay | Qualifies (context) | C2GnT family function | C2GnT enzymes build core 2/4/I branches on O-glycans | Human cloning, expression | High: Golgi family function |
| [PMID: 8308016](https://pubmed.ncbi.nlm.nih.gov/8308016/) | Direct assay; transfection | Qualifies (context) | C2GnT O-glycan output | C2GnT directs core-2 branched O-glycans and poly-LacNAc on cell-surface mucins | CHO transfection | High: Golgi/secretory function |
| [PMID: 37003559](https://pubmed.ncbi.nlm.nih.gov/37003559/) | Review | Qualifies (competing concept) | What resides in speckles | Speckles are LLPS bodies of SR/splicing factors; residents have IDRs & RNA association | Review | Defines properties GCNT1 lacks |

**Literature narrative.** The foundational cloning paper ([PMID: 1329093](https://pubmed.ncbi.nlm.nih.gov/1329093/)) establishes GCNT1's type II membrane topology and core-2 branching activity, directly refuting a soluble nuclear localization. The C2GnT family characterizations ([PMID: 9915862](https://pubmed.ncbi.nlm.nih.gov/9915862/); [PMID: 8308016](https://pubmed.ncbi.nlm.nih.gov/8308016/)) situate GCNT1 within a family of Golgi O-glycan branching enzymes, none of which is a nuclear/speckle protein. The speckle-biology review ([PMID: 37003559](https://pubmed.ncbi.nlm.nih.gov/37003559/)) defines the physical properties of genuine speckle residents — properties GCNT1 does not have — underscoring the implausibility of the seed hypothesis.

---

## GO Curation Implications

**Lead requiring curator verification.**

- **Cellular component (CC):** Retain the Golgi set as core — **GO:0031985 (Golgi cisterna)**, **GO:0000139 (Golgi membrane)**, **GO:0005802 (trans-Golgi network)** — supported by curated UniProt location and consistent with type II topology. **Do not treat GO:0016607 (nuclear speck) as core.** Recommended action: downgrade to non-core; candidate for **removal** or a **NOT qualifier**, on the grounds that a single unvalidated HPA IF pattern conflicts with strong, independent Golgi/topology evidence.
- **Molecular function (MF):** Unaffected and well-supported — core-2 β1,6-N-acetylglucosaminyltransferase activity (UDP-GlcNAc-dependent branch formation).
- **Biological process (BP):** Unaffected — mucin-type O-glycosylation / core-2 branch biosynthesis.
- Do **not** fall back to "protein binding"; the informative, supported CC terms (Golgi membrane / trans-Golgi network) already exist and should be retained.

### Final Curation Decision Table (lead — verify)

| GO term | Aspect | Current evidence | Recommendation |
|---|---|---|---|
| GO:0016607 nuclear speck | CC | IDA:HPA, single antibody, GCNT1-only outlier, no Golgi in HPA, no primary lit | **Non-core → remove or NOT-qualify** pending orthogonal validation |
| GO:0000139 Golgi membrane | CC | EXP:UniProtKB | Retain as core |
| GO:0005802 trans-Golgi network | CC | IDA:UniProtKB | Retain as core |
| GO:0031985 Golgi cisterna | CC | IDA:UniProtKB | Retain |
| core-2 branching activity / O-glycan process | MF/BP | PMID:1329093, PMID:23027862 | Retain (primary function) |

---

## Mechanistic Scope

The immediate molecular property under test is **subcellular localization**, not catalytic activity. The seed hypothesis asserts that GCNT1 physically resides in nuclear speckles. This must be separated from:

- **Direct gene-product activity:** GCNT1's actual direct activity is Golgi-luminal core-2 O-glycan branch synthesis (core-2 β1,6-GlcNAc branching of mucin-type O-glycans using lumenal UDP-GlcNAc). This is well established and not in dispute, and is spatially incompatible with nuclear speckles.
- **Downstream phenotypes:** O-glycan branching affects mucin structure, selectin-ligand formation, and cell-surface glycan display — all downstream of the Golgi reaction and unrelated to a nuclear location.
- **Inference from a single stain:** The nuclear-speckle claim is inferred entirely from one antibody's staining pattern, with no functional readout in the nucleus and no described mechanism. If real, it would be a secondary observation, not the gene product's primary function or location.

---

## Conflicts and Alternatives

- **Antibody artifact (most likely):** Punctate nuclear staining is a frequent HPA false-positive class; HPA's own IHC reliability for GCNT1 is "Uncertain." The complete absence of a Golgi call for GCNT1 — unique in the 12-gene panel — is exactly what an off-target antibody would produce.
- **HPA nuclear-background pattern:** Several membrane glycosyltransferases in the panel (GCNT4, ST6GALNAC1, FUT8) show a "Nucleoplasm" background call while still recovering the Golgi; GCNT1's speckle call may be an extreme instance of the same phenomenon, aggravated by loss of the Golgi signal.
- **Paralog confusion (unlikely to rescue):** GCNT1/2/3/4 and the broader C2GnT family are all Golgi type II enzymes; none is a known nuclear/speckle protein ([PMID: 9915862](https://pubmed.ncbi.nlm.nih.gov/9915862/)).
- **Isoform (no support):** No described soluble/nuclear isoform of GCNT1 lacking the signal-anchor exists.
- **Reliability discordance:** IF "Supported" vs. IHC "Uncertain" indicates the localization is not robustly reproduced across methods.

---

## Limitations and Knowledge Gaps

1. **Orthogonal validation of the HPA pattern.** Checked: HPA reliability tiers (IF "Supported," IHC "Uncertain"). Not resolved because no paired-antibody or knockdown IF is reported. Why it matters: single-antibody localizations are the weakest IDA class. Resolve with a second independent antibody plus siRNA/CRISPR knockout IF, or endogenous tagging.
2. **Any endogenous nuclear pool.** Checked: primary literature (none reported). Why it matters: an orthogonal detection of nuclear GCNT1 would change the verdict. Resolve with subcellular fractionation plus mass spec / western blot.
3. **Raw HPA image not re-examined.** The assessment relies on HPA's classified output and reliability flags rather than a fresh manual read of the primary micrographs. Resolve with expert re-annotation of the HPA IF images.
4. **GO_REF:0000052 text not directly retrieved.** The official GO_REF markdown could not be fetched programmatically (HTTP 403/404 from current.geneontology.org and go-site raw/API). However, the UniProt cross-reference for GO:0016607 is explicitly attributed as **IDA:HPA**, which unambiguously identifies the source as HPA immunofluorescence — consistent with GO_REF:0000052's known scope. No fabrication: the GO_REF text itself was not accessed.

---

## Discriminating Tests

The following would most efficiently distinguish the seed hypothesis from the antibody-artifact alternative:

1. **Knockout/knockdown-validated immunofluorescence** with ≥2 independent antibodies — does the speckle signal disappear on GCNT1 loss?
2. **Endogenous fluorescent tagging** (CRISPR knock-in) to visualize native localization without antibody bias (expected: Golgi, not speckles).
3. **Subcellular fractionation** (nuclear vs. membrane) with orthogonal detection (western/MS) to quantify any nuclear GCNT1 pool.
4. **Co-localization** with a bona fide speckle marker (SRRM2/SC35) versus a Golgi marker (GM130/TGN46) — a real speckle protein co-localizes with SRRM2; GCNT1 should co-localize with the Golgi marker.
5. **Sequence/feature check** for intrinsically disordered or RNA-binding speckle-targeting determinants ([PMID: 37003559](https://pubmed.ncbi.nlm.nih.gov/37003559/)); their absence argues against genuine speckle residence.

---

## Curation Leads (require curator verification)

- **Candidate action change:** Demote or remove **GO:0016607 (nuclear speck, IDA, GO_REF:0000052)** from GCNT1, or apply a **NOT** qualifier, pending orthogonal validation. Do not let it stand as a core localization.
- **Retain as core:** Golgi CC terms (GO:0031985, GO:0000139, GO:0005802) and core-2 β1,6-GlcNAc-transferase MF/BP terms.
- **Reference to verify (topology/identity):** [PMID: 1329093](https://pubmed.ncbi.nlm.nih.gov/1329093/) — snippet: *"The cDNA sequence predicts a protein with type II membrane topology, as has been found for all other mammalian glycosyltransferases cloned to date."*
- **References for family function:** [PMID: 9915862](https://pubmed.ncbi.nlm.nih.gov/9915862/) and [PMID: 8308016](https://pubmed.ncbi.nlm.nih.gov/8308016/) — establish the Golgi core-2/O-glycan branching role of the C2GnT family.
- **Suggested curator question:** Is the HPA nuclear-speckle call supported by any orthogonal (second-antibody or knockdown) data, or is it a single-antibody pattern? If single-antibody, treat as insufficient against the strong Golgi prior.
- **Suggested experiments:** Second-antibody + KO IF; endogenous tagging; Golgi/nuclear fractionation with MS; SRRM2 vs. GM130 co-localization.

---

## Proposed Follow-up Experiments / Actions

1. **Curation:** Flag GO:0016607 for GCNT1 as non-core; recommend removal or NOT qualifier subject to curator confirmation of HPA antibody count and modality.
2. **Validation experiment (highest value):** Second-antibody IF in GCNT1-knockout cells to test antibody specificity of the speckle signal.
3. **Orthogonal detection:** Endogenous tagging or subcellular fractionation + quantitative MS to determine whether any nuclear GCNT1 pool exists.
4. **Co-localization:** SRRM2/SC35 vs. Golgi-marker two-color imaging to place GCNT1 definitively in the Golgi or in speckles.
5. **Documentation:** Record the comparative HPA outlier analysis (GCNT1 as 1/12 speckle-called, uniquely Golgi-negative) as provenance supporting the non-core recommendation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)