---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T09:56:09.655695'
end_time: '2026-09-12T10:16:24.508490'
duration_seconds: 1214.85
template_file: /Users/cjm/orca/workspaces/ai-gene-review/arath-test/tmp/openscientist-arath-20260912/4-EIN3-template.md
template_variables:
  organism: ARATH
  gene: EIN3
  gene_symbol: EIN3
  uniprot_accession: O24606
  taxon_id: NCBITaxon:3702
  taxon_label: Arabidopsis thaliana
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0042393
  hypothesis_text: EIN3 has histone binding (GO:0042393).
  term_context: '- Term: histone binding (GO:0042393)

    - Evidence type: IDA

    - Original reference: PMID:28874528'
  reference_context: '- PMID:28874528'
  source_file: genes/ARATH/EIN3/EIN3-ai-review.yaml
  source_selector: existing_annotations[7].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0042393\n  label: histone binding\nevidence_type:\
    \ IDA\noriginal_reference_id: PMID:28874528"
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

- **Organism code:** ARATH
- **Taxon:** Arabidopsis thaliana (NCBITaxon:3702)
- **Gene directory:** EIN3
- **Gene symbol:** EIN3
- **UniProt accession:** O24606

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0042393
- **Source file:** genes/ARATH/EIN3/EIN3-ai-review.yaml
- **Source selector:** existing_annotations[7].function_hypothesis

## Seed Hypothesis

EIN3 has histone binding (GO:0042393).

## Term and Decision Context

- Term: histone binding (GO:0042393)
- Evidence type: IDA
- Original reference: PMID:28874528

## Reference Context

- PMID:28874528

## Source Context YAML

```yaml
term:
  id: GO:0042393
  label: histone binding
evidence_type: IDA
original_reference_id: PMID:28874528
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

## Specific adjudication question

Adjudicate direct EIN3 histone binding from PMID28874528. Trace the exact protein assayed and distinguish purified-protein histone binding from chromatin occupancy, co-complex association, and interaction through EIN2-C or ENAP1. Do not treat absence of an experiment in the abstract as refutation. Identify whether histone-binding MF is supported for EIN3 itself, what more specific function is defensible, or what assay is missing. Use primary evidence and independently reproducible analyses. Do not consult ai-gene-review repository reviews, generated reports or local bioinformatics results; these are held out. Verify the exact Arabidopsis protein and distinguish paralogs, mutants, tissue and assay context. Give evidence for and against the assignment, the narrowest defensible function, and what observation would change the verdict. Missing evidence is not refutation. Do not infer catalytic or regulatory function from interaction, docking or shared fold alone.


## Output

# AIGR Gene Hypothesis Deep Research — EIN3 histone binding (GO:0042393)

**Gene:** EIN3 (ETHYLENE INSENSITIVE 3) · *Arabidopsis thaliana* (ARATH, NCBITaxon:3702) · locus AT3G20770 (628 aa)
**UniProt:** O24606
**Focus:** function_assignment — `existing_annotations[7].function_hypothesis`
**Seed hypothesis:** EIN3 has histone binding (GO:0042393), IDA, from [PMID: 28874528](https://pubmed.ncbi.nlm.nih.gov/28874528/)

---

## Summary

**Verdict: Over-annotated / refuted as a direct molecular function for EIN3.** The IDA "histone binding" (GO:0042393) annotation assigned to EIN3 from [PMID: 28874528](https://pubmed.ncbi.nlm.nih.gov/28874528/) is not supported by the primary evidence. The full text of that paper (PNAS 2017; PMC5617289) was retrieved and mined — not just the abstract — and contains **no direct EIN3–histone binding assay of any kind**: the strings "pull-down," "recombinant," "in vitro," "MBP-EIN3," and "GST-EIN3" are all absent. Every result reported for EIN3 is **ChIP-seq/ChIP-qPCR DNA/chromatin occupancy** at target loci. The protein experimentally shown to "associate with histone" is the **EIN2 C-terminus (EIN2-C)**, "partially through … ENAP1."

The most defensible reading is that EIN3 acts within an ethylene-signaling module (EIN2-C → ENAP1 → histone H3K14/H3K23 acetylation) as a **sequence-specific DNA-binding transcription factor** that occupies target promoters, while the histone-directed activity is contributed by EIN2-C and the SANT-domain adaptor ENAP1. EIN3's only demonstrated protein partner in this module is ENAP1 — shown by GST pulldown and co-IP in the companion open-access paper [PMID: 27694846](https://pubmed.ncbi.nlm.nih.gov/27694846/) — and that interaction is already independently annotated as GO:0005515 protein binding (IPI). A reproducible InterPro domain scan confirms EIN3 carries **no histone-reader module** (no bromodomain, chromodomain, PHD, Tudor, PWWP, or WD40); it has only its own EIN3-family DNA-binding domain (Pfam PF04873) and N-terminal domain (PF27048).

Critically, a reproducible QuickGO query shows UniProt derived **two** IDA molecular-function terms from the *same* reference: GO:0003682 "chromatin binding" and GO:0042393 "histone binding." The chromatin-binding term correctly captures the ChIP-seq occupancy; the histone-binding term is a **redundant, less-accurate parallel** that asserts a direct protein–histone contact the paper never demonstrates for EIN3. The recommended curation lead is therefore to **remove GO:0042393 or replace it with the already-present GO:0003682**, retaining EIN3's core TF/DNA-binding annotations. Because absence of an experiment is not refutation, the door remains open: a direct, ENAP1- and DNA-independent EIN3–histone/nucleosome binding assay would restore the annotation. No such assay currently exists in the literature reviewed.

---

## Key Findings

### F001 — In PMID:28874528, histone binding is attributed to EIN2-C, not EIN3 itself

The original reference for the annotation, [PMID: 28874528](https://pubmed.ncbi.nlm.nih.gov/28874528/) (*EIN2 mediates direct regulation of histone acetylation in the ethylene response*, PNAS 2017), attributes histone association explicitly to the EIN2 C-terminus. The record states that "the **EIN2 C terminus (EIN2-C) is sufficient to rescue the levels of H3K14/23Ac**" and that "**EIN2-C associates with histone partially through an interaction with EIN2 nuclear-associated protein1 (ENAP1)**." EIN3, by contrast, is described only in terms of genomic occupancy: "**more EIN3 proteins bind to the loci where ENAP1 is enriched** for a quick response." The subject of the sentence that supports GO:0042393 ("associates with histone") is EIN2-C — not EIN3. Annotating EIN3 with histone binding from this statement is a subject/entity-transfer error: the molecular function belongs to a different protein co-referenced in the same paper.

### F002 — EIN3's histone link is indirect: it binds the SANT-protein ENAP1 and occupies DNA, not histones

The companion open-access study [PMID: 27694846](https://pubmed.ncbi.nlm.nih.gov/27694846/) (*EIN2-dependent regulation of acetylation of histone H3K14 and non-canonical histone H3K23 in ethylene signalling*, Nat Commun 2016) establishes the mechanistic wiring. "**Both EIN2 and EIN3 interact with a SANT domain protein named EIN2 nuclear associated protein 1 (ENAP1)**," shown by in vitro GST pull-down (GST-ENAP1 + MBP-EIN3 expressed in *E. coli*) and in vivo co-IP. The histone marks (H3K14Ac, non-canonical H3K23Ac) are ChIP-qPCR/ChIP-seq enrichments at EIN3 target promoters, are EIN2-dependent, and the paper concludes that "**ENAP1 may potentially mediate ethylene-induced histone acetylation via its interactions with EIN2 C terminus**." Notably, up-regulation of histone acetylation in response to ethylene is reported to be largely **not EIN3/EIL1 dependent**. Thus EIN3's demonstrated partner is a SANT-domain adaptor, and the route to histones runs through ENAP1/EIN2-C — an indirect, co-complex association, not a direct EIN3–histone contact. No assay of purified EIN3 binding histones or nucleosomes is reported in either paper.

### F003 — EIN3 (O24606) has no histone-reader domain (reproducible InterPro scan)

A reproducible InterPro API scan of O24606 (`https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/O24606`) returns 9 entries, **all EIN3-family / DNA-binding modules**: Pfam PF04873 (EIN3 DNA-binding domain), Pfam PF27048 (EIN3 N-terminal domain), InterPro IPR006957 / IPR023278 / IPR047091 / IPR060335 (EIN3-like DNA-binding), CATH-Gene3D G3DSA:1.10.3180.10 and SUPERFAMILY SSF116768 (DNA-binding domain of EIN3-like), and PANTHER PTHR33305. **None** of the canonical histone-reader/histone-binding folds is present — no bromodomain, chromodomain, PHD finger, Tudor, PWWP, or WD40. Domain architecture alone does not formally exclude a non-canonical binding surface, but it removes the most common structural basis for a bona fide histone-binding molecular function and is consistent with EIN3 acting as a sequence-specific DNA-binding TF rather than a histone reader.

### F004 — Full text of PMID:28874528 contains no direct EIN3–histone binding assay

Full-text mining of the PMC HTML (PMC5617289) confirms the abstract-level reading. The strings **'pull-down', 'recombinant', 'in vitro', 'MBP-EIN3', and 'GST-EIN3' are all absent** from the article. Every EIN3 result is ChIP-seq/ChIP-qPCR locus occupancy — e.g., the section heading "**ENAP1 Binds to Active Gene Regions and EIN3 Prefers to Bind ENAP-Targeted Regions**," and statements that "EIN3 prefers to bind to ENAP1 target regions, which are more accessible" and "more EIN3 proteins bind to the loci where ENAP1 is enriched." The histone binder in the paper remains EIN2-C. Decisively, the authors themselves flag EIN3's molecular role as unresolved: "**Further examining the binding activity of EIN2 and ENAP1 in the *ein3-1* mutant will provide more insight into the molecular function of EIN3 in histone acetylation in the ethylene response.**" An IDA (direct-assay) histone-binding claim is inconsistent with the authors' own statement that EIN3's molecular contribution is an open question.

### F005 — QuickGO provenance: the same paper already yields the correct term (GO:0003682); GO:0042393 is redundant

A reproducible QuickGO API query (`geneProductId=O24606`, aspect MF) returns 31 molecular-function annotations. The **same reference PMID:28874528** is used by UniProt to assign **two** IDA MF terms: GO:0003682 "chromatin binding" (IDA, assignedBy UniProt) **and** GO:0042393 "histone binding" (IDA, ECO:0000314, qualifier 'enables', dated 2021-09-06, withFrom=None). The EIN3–ENAP1 interaction is independently annotated as GO:0005515 "protein binding" (IPI, PMID:27694846, withFrom UniProtKB Q8VZI9 = ENAP1 / AT3G11100). EIN3's core functions are separately and robustly supported: GO:0003677 DNA binding (IDA, PMID:26352699), GO:0003700 DNA-binding transcription factor activity (multiple IDA/ISS/TAS, incl. PMID:9851977, 18466304, 23795294), and GO:0000976 cis-regulatory region binding. Because chromatin binding already captures the ChIP-seq occupancy from PMID:28874528, the parallel histone-binding term from the same paper adds a stronger, more specific claim (direct histone contact) the paper does not support — the definition of an over-reach. Removing GO:0042393 loses no real information, since the ENAP1 partnership is already recorded as protein binding.

---

## Mechanistic Model / Interpretation

The papers and the domain/annotation scans converge on a single coherent model in which the histone-directed activity and the DNA-directed activity are carried by **different proteins in the same signaling module**:

```
        ethylene signal
              │
              ▼
   ┌──────────────────────┐
   │      EIN2-C          │  ← C-terminus ASSOCIATES WITH HISTONE
   │  (cleaved fragment)  │     (partly via ENAP1) → drives H3K14Ac / H3K23Ac
   └──────────┬───────────┘
              │ interacts
              ▼
   ┌──────────────────────┐
   │  ENAP1 (SANT domain) │  ← adaptor; "may mediate histone acetylation"
   └──────────┬───────────┘
              │ interacts (GST pulldown + co-IP; GO:0005515 protein binding)
              ▼
   ┌──────────────────────┐
   │        EIN3          │  ← sequence-specific TF
   │  (PF04873 DNA-binding│     BINDS DNA / occupies chromatin at target loci
   │   domain; no reader) │     (ChIP-seq) → GO:0003677, GO:0003700, GO:0003682
   └──────────────────────┘
              │
              ▼
     transcription of ethylene-response genes
```

**Direct EIN3 activities (well supported):** sequence-specific DNA binding (GO:0003677), DNA-binding transcription-factor activity (GO:0003700), cis-regulatory region binding (GO:0000976), chromatin/locus occupancy (GO:0003682), and protein–protein interaction with ENAP1 (GO:0005515).

**Not a direct EIN3 activity (the seed hypothesis):** binding to histones (GO:0042393). The observed correlation between EIN3 occupancy and histone-acetylation marks is a *pathway/chromatin-context consequence*, not evidence that EIN3 itself contacts a histone. The histone contact is demonstrated for EIN2-C, and the acetylation response is largely EIN3/EIL1-independent.

| Molecular claim | Protein that carries it | Direct assay in the cited papers? | Correct GO reflection |
|---|---|---|---|
| Associates with histone | EIN2-C (via ENAP1) | Yes — attributed to EIN2-C | GO:0042393 belongs to EIN2, not EIN3 |
| Binds SANT adaptor ENAP1 | EIN3 | Yes — GST pulldown + co-IP (PMID:27694846) | GO:0005515 protein binding (already present) |
| Occupies target DNA / chromatin | EIN3 | Yes — ChIP-seq/ChIP-qPCR (PMID:28874528) | GO:0003682 chromatin binding (already present) |
| Sequence-specific DNA binding / TF | EIN3 | Yes — independent refs | GO:0003677 / GO:0003700 (already present) |
| Direct histone/nucleosome binding | EIN3 | **No** | GO:0042393 not supported for EIN3 |

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 28874528](https://pubmed.ncbi.nlm.nih.gov/28874528/) (PNAS 2017) | Direct assay + ChIP-seq (full text mined) | Refutes-direct (for EIN3) | Does EIN3 directly bind histone? | "EIN2-C … sufficient to rescue H3K14/23Ac"; "**EIN2-C associates with histone partially through … ENAP1**"; EIN3 only "bind[s] to the loci where ENAP1 is enriched"; no in vitro EIN3–histone assay present | Arabidopsis etiolated seedlings; ChIP-seq/ChIP-qPCR | High. Full text inspected (PMC5617289). Original reference for the annotation. |
| [PMID: 27694846](https://pubmed.ncbi.nlm.nih.gov/27694846/) (Nat Commun 2016, OA) | Interaction (GST pulldown, co-IP) + ChIP | Qualifies | What does EIN3 bind; is the histone link direct? | EIN3 interacts with **SANT-protein ENAP1**; histone-acetylation route runs through ENAP1/EIN2-C; ethylene-induced acetylation "**not EIN3/EIL1 dependent**" | Arabidopsis; recombinant MBP-EIN3 + GST-ENAP1; in planta co-IP | High. Open access. Indirect, co-complex path — not direct histone contact. |
| InterPro O24606 (reproducible API scan) | Structural/evolutionary (computational) | Refutes / qualifies | Does EIN3 have a histone-reader fold? | 9 entries, all EIN3-family DNA-binding (PF04873, PF27048, IPR006957 etc.); **no** bromo/chromo/PHD/Tudor/PWWP/WD40 | Sequence-level | High reproducibility; absence of domain is suggestive, not definitive. |
| QuickGO O24606 (reproducible API query) | Review/database provenance | Competing / qualifies | Is GO:0042393 redundant with a better term? | Same PMID yields both GO:0003682 (chromatin binding, IDA) and GO:0042393 (histone binding, IDA); ENAP1 tie is GO:0005515 IPI | Annotation database | High. Demonstrates parallel over-reach from one paper. |
| [PMID: 26352699](https://pubmed.ncbi.nlm.nih.gov/26352699/) | Direct DNA-binding assay | Competing (correct MF) | EIN3 core molecular function | EIN3 binds DNA (sequence-specific TF at ethylene-response element) | Arabidopsis | High. Supports GO:0003677. |
| UniProt O24606 | Curated database record | Context | How is the histone link recorded? | Histone link stored only as SUBUNIT "association with histone"; FUNCTION = "Transcription factor … Binds DNA"; annotates TF activity, DNA binding, chromatin binding | 628 aa; nucleus; homodimer | Moderate; database-level orientation. |

**How each key paper bears on the verdict:**
- **PMID:28874528** is the annotation's own source. On full-text inspection it does the opposite of supporting the hypothesis for EIN3: it assigns histone association to EIN2-C and shows EIN3 only as a DNA-occupying TF.
- **PMID:27694846** explains *why* EIN3 appears linked to histones — it binds the SANT adaptor ENAP1 — and simultaneously undercuts a direct role by showing the acetylation response is largely EIN3-independent.
- **InterPro** and **QuickGO** provide reproducible, independent lines confirming (a) no reader domain and (b) that a more accurate term from the same paper already exists.

---

## GO Curation Implications (leads — require curator verification)

**Lead: remove GO:0042393 "histone binding" (IDA, PMID:28874528) from EIN3/O24606, or replace it with the already-present GO:0003682 "chromatin binding" (IDA) from the same reference.**

**GO decision table:**

| GO ID | Label | Aspect | Current annotation | Recommendation (lead) | Rationale |
|---|---|---|---|---|---|
| **GO:0042393** | histone binding | MF | IDA / PMID:28874528 | **REMOVE or REPLACE** | No purified EIN3–histone assay in source paper; evidence is ChIP occupancy; no histone-reader domain; same paper already yields accurate GO:0003682 |
| GO:0003682 | chromatin binding | MF | IDA / PMID:28874528 | **RETAIN** (accurate term) | ChIP-seq shows EIN3 occupies target loci — correct reading of the occupancy evidence |
| GO:0005515 | protein binding (ENAP1) | MF | IPI / PMID:27694846 (ENAP1 Q8VZI9) | **RETAIN** | GST pulldown + co-IP; demonstrated EIN3 partner is SANT-protein ENAP1 |
| GO:0003677 | DNA binding | MF | IDA / PMID:26352699 | **RETAIN** | Direct sequence-specific DNA binding; core MF |
| GO:0003700 | DNA-binding TF activity | MF | IDA/ISS/TAS (multiple) | **RETAIN** (core function) | EIN3 is the master ethylene-response transcription factor |

- If EIN3's participation in a histone/chromatin complex is to be represented, prefer the **BP** term GO:0040029 *epigenetic regulation of gene expression* (already present) over the MF *histone binding*.
- **Do not** fall back to bare "protein binding" as the headline representation; the informative, defensible MF for the occupancy evidence is **chromatin binding (GO:0003682)**, with the specific partner captured by the existing ENAP1 IPI.

---

## Mechanistic Scope

- **Immediate EIN3 molecular activity being tested:** does purified EIN3 physically bind histone proteins/nucleosomes? **No direct assay supports this.**
- **What EIN3 actually does (direct):** sequence-specific DNA-binding transcription factor; homodimer binding the primary ethylene response element; interacts with the SANT-domain protein ENAP1.
- **Downstream / indirect (must not be conflated with EIN3 MF):** ethylene-induced H3K14Ac/H3K23Ac enrichment at EIN3 target promoters is executed by the EIN2-C/ENAP1 module (and recruited acetyltransferase activity), is EIN2-dependent, and is largely EIN3-independent. EIN3 occupancy at these loci is DNA binding; EIN3 acts downstream to activate transcription.

---

## Conflicts and Alternatives

- **Partner/entity confusion (most important):** the histone-binding activity belongs to **EIN2 (EIN2-C)**, a different protein; annotation transfer to the co-referenced EIN3 in the same paper is the likely source of the mis-assignment.
- **ChIP-occupancy ≠ histone binding:** ChIP enrichment of a TF measures DNA/locus occupancy, not a protein–histone molecular interaction; conflating them inflates MF specificity.
- **Co-complex artifact:** EIN3 being in a complex with EIN2-C/ENAP1/histones (co-IP/reChIP) does not establish a direct EIN3–histone contact.
- **EIN3-independence of the mark:** histone-acetylation elevation is "not EIN3/EIL1 dependent," arguing against EIN3 being the histone effector.
- **Redundant database carry-over:** QuickGO shows UniProt derived both GO:0003682 and GO:0042393 from a single "association with histone" statement; the histone-binding term is the less accurate of the pair.
- **Paralog consideration:** EIN3 has the close paralog EIL1 (and family members EIL2–EIL4). The evidence and annotations here are for EIN3 (O24606, AT3G20770) specifically; the shared EIN3-family fold carries no histone-reader domain in any member, so paralog confusion does not rescue the claim.

---

## Limitations and Knowledge Gaps

1. **Source full text — resolved.** The main-text article (PMC5617289) was retrieved and mined; it contains no in vitro EIN3–histone binding experiment. Residual minor gap: individual supplementary dataset files were not each downloaded, but the Results/Methods narrative describes only ChIP-seq for EIN3.
2. **No in vitro EIN3–histone/nucleosome assay anywhere in the searched literature.** Multiple PubMed queries for direct EIN3 histone/nucleosome binding returned none. This matters because IDA requires a direct assay. Absence, per the adjudication rules, is not proof EIN3 cannot bind histone — it means the IDA claim lacks support.
3. **Histone-reader domain — resolved (none).** The reproducible InterPro/Pfam scan shows only EIN3 DNA-binding (PF04873) and N-terminal (PF27048) domains. This argues structurally against a direct histone-binding MF but cannot exclude a non-canonical binding surface.
4. **ENAP1 mechanism partly open:** the exact biochemical basis by which the EIN2-C/ENAP1 module contacts histone (and whether EIN3 ever contributes directly) is not fully resolved even by the authors, who explicitly call for further work in the *ein3-1* mutant.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

**Leads requiring curator verification:**

- **Action:** Flag `existing_annotations[7]` (GO:0042393 histone binding, IDA, PMID:28874528) as **not supported for EIN3 as a direct MF**; recommend **removal or replacement with GO:0003682 chromatin binding**, which is already annotated from the same reference.
- **Candidate replacement / retained terms:** keep GO:0003700 / GO:0003677 / GO:0003682 / GO:0000976 (TF activity / DNA binding / chromatin binding / cis-regulatory region binding); represent the histone connection at the **BP** level (GO:0040029 epigenetic regulation of gene expression) and the ENAP1 tie as GO:0005515 protein binding (IPI, PMID:27694846, with ENAP1 = Q8VZI9).
- **Snippets to verify (exact quotes):**
  - PMID:28874528: *"EIN2-C associates with histone partially through an interaction with EIN2 nuclear-associated protein1 (ENAP1)"*; *"more EIN3 proteins bind to the loci where ENAP1 is enriched"*; *"ENAP1 Binds to Active Gene Regions and EIN3 Prefers to Bind ENAP-Targeted Regions"*; *"Further examining the binding activity of EIN2 and ENAP1 in the ein3-1 mutant will provide more insight into the molecular function of EIN3 in histone acetylation in the ethylene response."*
  - PMID:27694846: *"Both EIN2 and EIN3 interact with a SANT domain protein named EIN2 nuclear associated protein 1 (ENAP1)"*; *"ENAP1 may potentially mediate ethylene-induced histone acetylation via its interactions with EIN2 C terminus."*
- **Suggested curator questions:** Does the PNAS paper contain a purified EIN3–histone binding figure (supplement)? Was the GO:0042393 IDA transferred from EIN2's activity? Is chromatin binding (GO:0003682) the intended, more accurate term?

**Discriminating experiments that would change the verdict:**

1. **In vitro binding of recombinant EIN3 to histones/nucleosomes** (histone-peptide array or pulldown, nucleosome EMSA, ITC/SPR), performed **±ENAP1 and DNA-free** — the decisive test for a direct MF. A positive, partner- and DNA-independent signal would justify reinstating GO:0042393.
2. **ENAP1-dependence test:** repeat any apparent EIN3–histone co-purification in an *enap1* background or with ENAP1-binding-deficient EIN3, to show the histone link is ENAP1-routed.
3. **Domain mapping / structure:** AlphaFold-Multimer EIN3–histone octamer modeling with interface-confidence (PAE/ipTM) scoring, reported conservatively; docking or shared fold alone is not evidence of function.
4. **reChIP directionality:** determine whether EIN3 occupancy at loci precedes or follows H3K14/23Ac deposition, separating cause (histone binder) from consequence (mark-dependent recruitment).

**What would change the verdict:** a reproducible direct binding assay of purified EIN3 to histones/nucleosomes that is independent of ENAP1 and of DNA.

---

## Conclusion

The molecular-function annotation **EIN3 histone binding (GO:0042393, IDA, PMID:28874528) is over-annotated and should not stand for EIN3.** The cited paper demonstrates histone association for EIN2-C (partly via ENAP1) and shows EIN3 only as a DNA-binding TF occupying target loci by ChIP-seq. EIN3 has no histone-reader domain, its demonstrated partner is the SANT-protein ENAP1 (already captured as protein binding), and the same paper already yields the correct, more accurate term — chromatin binding (GO:0003682). The narrowest defensible molecular functions for EIN3 remain DNA binding / DNA-binding transcription factor activity plus chromatin binding. Only a direct, partner- and DNA-independent EIN3–histone binding experiment would justify reinstating the histone-binding MF.

---

*Prepared across Iterations 1–3. Analyses used NCBI efetch (abstracts/record), full-text mining of PMC5617289 (PNAS 2017), Europe-PMC full text of the 2016 companion (PMID:27694846), a reproducible InterPro/Pfam domain scan of O24606, and QuickGO/GOA annotation provenance for O24606. No results were fabricated; where a resource returned only partial content (e.g., individual PNAS supplementary files were not each downloaded) this is stated plainly.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)