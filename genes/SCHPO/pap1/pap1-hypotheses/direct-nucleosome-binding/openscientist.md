---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:36:08.866963'
end_time: '2026-08-31T22:47:43.685608'
duration_seconds: 694.82
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: pap1
  gene_symbol: pap1
  uniprot_accession: Q01663
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: free_text
  hypothesis_slug: direct-nucleosome-binding
  hypothesis_text: Schizosaccharomyces pombe Pap1 directly binds nucleosomes as a
    biologically meaningful molecular function, rather than nucleosome association
    being an incidental signal in the 2025 transcription-factor interaction atlas.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/pap1/pap1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe Pap1 directly binds\
    \ nucleosomes as a biologically meaningful molecular\n  function, rather than\
    \ nucleosome association being an incidental signal in the 2025 transcription-factor\n\
    \  interaction atlas.\nfocus_type: free_text\ncontext: []\nreference_id: []"
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** pap1
- **Gene symbol:** pap1
- **UniProt accession:** Q01663

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** direct-nucleosome-binding
- **Source file:** genes/SCHPO/pap1/pap1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Schizosaccharomyces pombe Pap1 directly binds nucleosomes as a biologically meaningful molecular function, rather than nucleosome association being an incidental signal in the 2025 transcription-factor interaction atlas.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe Pap1 directly binds nucleosomes as a biologically meaningful molecular
  function, rather than nucleosome association being an incidental signal in the 2025 transcription-factor
  interaction atlas.
focus_type: free_text
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

# Pap1 (SCHPO, UniProt Q01663) — Direct Nucleosome-Binding Hypothesis Review

**Hypothesis under evaluation:** *Schizosaccharomyces pombe* Pap1 directly binds nucleosomes
as a biologically meaningful molecular function, rather than nucleosome association being an
incidental signal in the 2025 transcription-factor interaction atlas.

**Focus type:** free_text · **Slug:** direct-nucleosome-binding · **Iteration:** 1 of 3

---

## Executive Judgment

**Verdict: Partially supported / weakly supported (do not upgrade to a confident direct-MF claim).**

The hypothesis contains two separable claims that resolve differently:

1. **"The nucleosome signal is not merely incidental atlas background."** → **Supported.**
   In the source study (Skribbe et al., *Molecular Cell* 2025, PMID **40015273**), core histones
   were pervasive contaminants co-purifying in *all* low-stringency IPs, including the untagged
   control. Critically, under **high-stringency** conditions the histone association was retained
   for only three transcription factors — **Pap1, Atf1, and Pcr1** — out of the 89-TF library.
   Because the authors explicitly controlled for the generic histone background and Pap1 still
   scored, the signal is *specific*, not indiscriminate atlas noise.

2. **"Pap1 *directly* binds nucleosomes as a biologically meaningful molecular function
   (pioneering activity)."** → **Weakly supported / unresolved.** This is an *inference*, not a
   demonstrated activity. The evidence is co-immunoprecipitation/IP-MS, which cannot distinguish
   direct core-histone contact from a stable indirect/bridged association (e.g., Pap1 bound to its
   target DNA within a nucleosomal/chromatin context, carrying histones along). No reconstituted-
   nucleosome binding assay (EMSA, fluorescence anisotropy, NCAP-SELEX, Pioneer-seq) or functional
   nucleosome-displacement/pioneering assay has been performed for Pap1. The atlas authors
   themselves use suggestive language: the co-purification *"indicates interactions with the
   nucleosome and suggests pioneering activity."*

**Most important caveat:** Pap1's dominant, experimentally established molecular function is
sequence-specific promoter DNA binding as a bZIP (AP-1/Jun-Fos-like) oxidative-stress activator.
The nucleosome association must be interpreted against this backdrop; "direct nucleosome binding"
is currently a plausible-but-unproven secondary property carried largely by orthology analogy to
human Jun/Fos.

---

## Evidence Matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|--------|--------------|-------------|---------|--------------------------|
| 1 | Skribbe et al. 2025, **PMID 40015273** (Mol Cell) | Interaction (IP-MS) | **Qualifies / partially supports** | Pap1 physically associates with nucleosomes | Under high-stringency IP-MS, histone co-purification is uniquely retained for Pap1, Atf1, Pcr1 (vs. pervasive low-stringency background incl. untagged control) | *S. pombe*, endogenously tagged TFs, IP-MS | Signal is specific, but co-IP ≠ direct binding; cannot resolve direct vs. bridged; no in vitro nucleosome assay |
| 2 | Skribbe et al. 2025, **PMID 40015273** | Review/interpretation within primary paper | **Qualifies** | Pioneering activity | Authors state co-purification *"suggests pioneering activity"*; note Pap1 *"has not been linked to nucleosome remodeling"* | *S. pombe* | Explicitly inferential; no functional pioneering assay in pombe |
| 3 | UniProt/PomBase **Q01663** (GO:0031491, EXP) | Database | **Supports (annotation exists)** | Nucleosome binding is annotated | GO:0031491 "nucleosome binding" now present with EXP evidence, traceable to the atlas co-purification | Curated record | EXP label overstates a co-purification; provenance is a single interaction study |
| 4 | UniProt **Q01663** feature table | Structural/domain | **Competing (primary MF)** | Pap1's core molecular function | bZIP domain (76–139), basic DNA-contact motif (81–102), leucine zipper (104–111); redox CRDs; NES/NLS | Sequence/domain | Establishes canonical sequence-specific DNA-binding TF as the primary MF |
| 5 | PomBase GO MF (IDA): GO:0001228, GO:0000978, GO:0008301 | Direct assay / curated | **Competing (primary MF)** | Sequence-specific promoter DNA binding | Pap1 has IDA-level activator activity, Pol II cis-regulatory sequence-specific DNA binding, and DNA bending | *S. pombe* | Well-supported dominant function |
| 6 | Fellas et al. 2026, **PMID 41326690** | Mutant phenotype / localization | **Competing (primary MF)** | Pap1 acts via promoter occupancy | "Pap1 nuclear localisation and recruitment to promoters of oxidoreductase and membrane transporter genes is increased," driving efflux | *S. pombe* epimutants | Reinforces sequence-specific promoter binding as mechanism |
| 7 | Lai et al. 2021, **PMID 34740252** | Mutant phenotype / occupancy | **Competing / context** | Pap1 promoter occupancy is chromatin-context dependent | Histone variant replacement (H2A.Z) *increases* Pap1 occupancy at drug-resistance promoters | *S. pombe* + AtOXS3 | Suggests Pap1 access is *facilitated by* chromatin remodeling — arguing against strong intrinsic pioneering |
| 8 | Human ortholog literature (Jun/Fos) cited by PMID 40015273 | Structural/evolutionary | **Supports (by analogy)** | bZIP factors can bind nucleosomes | Jun/Fos bind nucleosomes in vitro and associate with nucleosome-rich regions in vivo | Human/in vitro | Orthology analogy only; not direct evidence for pombe Pap1 |
| 9 | Convergent bZIP pattern in atlas (Atf1, Pcr1 also retain histones; Zip1 does not) | Structural/evolutionary | **Supports (plausibility)** | Nucleosome binding may be a bZIP-family trait | Three of four mitotic bZIPs co-purify histones; authors propose family-wide property | *S. pombe* | Correlative; consistent with either direct binding OR shared chromatin-association behavior |

---

## GO Curation Implications (leads requiring curator verification)

- **Term in question:** `GO:0031491 nucleosome binding` (MF), currently on Q01663/PomBase with
  evidence code **EXP**.
- **Assessment:** The evidence type (high-stringency co-IP/IP-MS) supports a **physical
  interaction with histones/nucleosomes**, but an **EXP** code on a *direct* MF term is arguably
  **too strong** for what is a co-purification that cannot resolve direct vs. bridged binding.
- **Recommended lead actions (curator to verify):**
  1. **Retain but re-scope the evidence, not remove the term.** The specific high-stringency signal
     justifies keeping a nucleosome/histone-interaction annotation rather than deleting it.
  2. **Prefer an interaction-flavored provenance.** Consider annotating with evidence code **IPI**
     (physical interaction) with the histone/nucleosome as the "with" object, or downgrading the
     directness implied by EXP, so the annotation reflects "co-purifies with nucleosome" rather
     than a validated direct binding activity.
  3. **Consider `GO:0042393 histone binding`** as an equally or more *literal* description of what
     was observed (co-purification of **core histone subunits**), pending a discriminating assay.
     `GO:0031491 nucleosome binding` is the atlas's chosen framing and is defensible, but curators
     should note it is model-dependent.
  4. **Mark as non-core / tentative.** Pap1's core MF annotations remain `GO:0001228`,
     `GO:0000978`, `GO:0008301`. Nucleosome binding should be treated as a **secondary, provisional**
     function, ideally with a curator note that it rests on a single interaction study and orthology.
  5. **Do not** promote to functional pioneer-factor process/MF terms — no pioneering/remodeling
     activity has been demonstrated for Pap1.

*(Per instructions, "protein binding" is deliberately avoided as the recommendation; "histone
binding" / "nucleosome binding" with interaction-level evidence is the more informative option.)*

### GO decision table (lead — curator to verify)

| GO term | Aspect | Current status | Evidence basis | Recommended lead action |
|---------|--------|----------------|----------------|-------------------------|
| GO:0031491 nucleosome binding | MF | Present, **EXP** (Q01663/PomBase) | Single high-stringency IP-MS co-purification (PMID 40015273); no direct/in vitro assay | **Retain but re-scope**: change evidence from EXP→**IPI** (with = histones/nucleosome); mark **non-core / provisional**; add note that directness & pioneering are inferred |
| GO:0042393 histone binding | MF | Not annotated | More literal description of "co-purifies with core histone subunits" | **Candidate alternative** to GO:0031491 if curator prefers matching term to the actual observable |
| GO:0001228 DNA-binding transcription activator activity, Pol II-specific | MF | Present, IDA | Multiple primary studies | **Retain — core function** (unchanged) |
| GO:0000978 RNA Pol II cis-regulatory region sequence-specific DNA binding | MF | Present, IDA | Multiple primary studies | **Retain — core function** (unchanged) |
| GO:0008301 DNA binding, bending | MF | Present, IDA | Primary | **Retain** (unchanged) |
| (pioneer/remodeling MF or BP terms) | MF/BP | Not annotated | None (no functional pioneering assay for Pap1) | **Do NOT add** — unsupported |

---

## Mechanistic Scope

- **Immediate molecular activity tested:** whether Pap1 makes a *direct physical contact with the
  nucleosome core particle* (histone octamer ± nucleosomal DNA) as an intrinsic binding activity.
- **What the data actually show:** Pap1 **co-purifies** with core histones under stringent IP
  conditions — a physical-association readout at the level of the assembled complex, not a
  reconstituted binary binding measurement.
- **Separated downstream/secondary layers (NOT the direct activity):**
  - Transcriptional activation of oxidative-stress/drug-resistance regulons (BP consequence).
  - Nuclear accumulation via redox-controlled Crm1/NES switching (regulatory input, not nucleosome MF).
  - Increased efflux and drug resistance phenotypes (organismal/phenotypic downstream effects).
  - Chromatin-context effects on Pap1 occupancy (e.g., H2A.Z replacement *enabling* Pap1 access,
    PMID 34740252) — this frames Pap1 as a *beneficiary* of remodeling rather than a demonstrated
    pioneer that opens chromatin itself.

---

## Conflicts and Alternatives

1. **Direct vs. bridged interaction (primary alternative).** IP-MS cannot distinguish Pap1↔histone
   direct contact from Pap1 bound to nucleosomal target DNA that co-precipitates histones. Pap1's
   very strong, well-documented sequence-specific DNA binding makes the "carried along on chromatin"
   explanation a serious competitor. High stringency reduces but does not eliminate this ambiguity.
2. **Orthology overreach.** The strongest positive framing (Jun/Fos bind nucleosomes in vitro) is
   an analogy across a >500 Myr divergence; pombe Pap1 has diverged CRDs and its own regulatory
   logic. Orthology motivates the hypothesis but is not evidence of the pombe activity.
3. **Chromatin facilitates Pap1, not vice versa.** PMID 34740252 shows histone-variant replacement
   *increases* Pap1 promoter occupancy — consistent with Pap1 needing accessible chromatin rather
   than acting as a strong intrinsic nucleosome invader/pioneer.
4. **Shared-artifact possibility across bZIPs.** Atf1/Pcr1 (an obligate heterodimer) and Pap1 all
   scoring could reflect a common bona fide bZIP property *or* a shared behavior (e.g., particularly
   stable chromatin residence) that co-retains histones under stringency without direct core contact.
5. **Database carry-over risk.** Once GO:0031491 (EXP) is on the record, it can propagate to
   orthologs/paralogs by inference; curators should ensure downstream IBA/ISS annotations do not
   over-generalize an unvalidated pioneering activity.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|-----|------------------|-----------------------------|-----------------------|
| Direct vs. indirect binding | Confirmed evidence is IP-MS co-purification (PMID 40015273); no in vitro assay found | Determines whether GO:0031491 EXP (direct MF) is warranted vs. an interaction annotation | Reconstituted-nucleosome EMSA / fluorescence anisotropy with recombinant Pap1 (or its bZIP domain) |
| Functional pioneering | No pombe nucleosome-displacement/accessibility data for Pap1 | "Biologically meaningful function" implies a functional consequence, not just contact | ATAC/MNase accessibility change at Pap1 sites upon induction; ISO/Pioneer-seq assay |
| DNA-dependence of the co-IP | Not tested in source | If benzonase/DNase abolishes the histone co-IP, the interaction is DNA-bridged, not direct | Nuclease-treated IP-MS; salt-titration of the Pap1–histone co-complex |
| Which histones / stoichiometry | Atlas reports "core histone subunits" generically | Distinguishes octamer/nucleosome binding from single-histone chaperone-like binding | Quantitative crosslinking-MS; defined-nucleosome pulldowns |
| bZIP-family generality | Zip1 negative; Atf21/Atf31 untested (meiotic) | Determines whether this is a conserved MF worth family-wide annotation | Meiotic-cell IP-MS of Atf21/Atf31; comparative in vitro binding |

---

## Discriminating Tests (recommended, ranked)

1. **Reconstituted-nucleosome binding assay** (EMSA or fluorescence anisotropy) with recombinant
   full-length Pap1 and its isolated bZIP domain on Widom-601 nucleosomes ± cognate AP-1 motif.
   *Directly tests "direct binding"; discriminates sequence-directed vs. core-histone binding.*
2. **Nuclease-controlled re-IP-MS**: repeat the Pap1 pulldown ± benzonase and ± high salt.
   *If histone co-purification is DNA-dependent → association is chromatin-bridged, not a direct
   nucleosome MF.*
3. **Pioneer-seq / NCAP-SELEX** with Pap1 to quantify nucleosomal vs. free-DNA binding preference
   and end vs. dyad positioning.
4. **In vivo accessibility change**: ATAC-seq/MNase-seq before and after Pap1 activation (H2O2) at
   Pap1 target loci, in *pap1Δ* vs. wild type. *Tests functional pioneering.*
5. **Comparative bZIP panel** (Atf1, Pcr1, Zip1, meiotic Atf21/Atf31) in the same in vitro assay to
   test whether nucleosome binding is a genuine family trait.

---

## Curation Leads (require curator verification)

- **Candidate reference to attach/verify:** Skribbe M, Soneson C, Stadler MB, Schwaiger M, et al.
  *A comprehensive Schizosaccharomyces pombe atlas of physical transcription factor interactions
  with proteins and chromatin.* Mol Cell. 2025;85(7):1426–1444.e8. **PMID 40015273.**
  - Snippet to verify in full text: histone co-purification "uniquely preserved for Pap1 and the
    heterodimeric TFs Atf1 and Pcr1 … under high stringency conditions," and this "indicates
    interactions with the nucleosome and **suggests** pioneering activity." (Verify verbatim; the
    published abstract does not itself mention Pap1/nucleosome — the claim is in the Results/Discussion.)
- **Candidate GO action:** Retain `GO:0031491 nucleosome binding` **but** re-scope evidence from
  EXP to an interaction-level code (IPI, "with" = histones/nucleosome), OR replace with
  `GO:0042393 histone binding`; annotate as **non-core / provisional** with a curator note.
- **Candidate qualifier:** Add note that directness and pioneering are **inferred**, based on a
  single co-purification study plus Jun/Fos orthology.
- **Suggested curator questions:**
  1. Does the atlas supplement report DNase/benzonase-resistance of the Pap1–histone co-IP?
  2. Is there any reconstituted-nucleosome or accessibility assay for Pap1 (none found here)?
  3. Should nucleosome binding for Atf1/Pcr1 be curated consistently with Pap1?
- **Suggested experiments:** the five discriminating tests above (priority: #1 and #2).

---

## Computed Provenance: bZIP basic-region conservation (Iteration 2)

Sequences fetched from UniProt (Q01663, P52890, Q09926, Q9Y7P6, P01100, P05412); ungapped
positional comparison of the basic-region→leucine-zipper window (28 aa) against Pap1.

| Protein | bZIP basic-region window (basic region → leucine zipper) | % identity vs Pap1 | AP-1 redox Cys in basic region |
|---------|----------------------------------------------------------|--------------------|-------------------------------|
| Pap1 (Q01663) | `RKAQNRAAQRAFRKRKEDHLKALETQVVTLKE` | 100% (ref) | **No** |
| Atf1 (P52890) | `FLERNRQAALKCRQRKKQWLSNLQAKVEFYGN` | 32.1% | Yes |
| Pcr1 (Q09926) | `ILERNRIAASKFRQKKKEWIKELEQTANAAFE` | 32.1% | No |
| FOS (P01100) | `RRERNKMAAAKCRNRRRELTDTLQAETDQLED` | 21.4% | Yes |
| JUN (P05412) | `KRMRNRIAASKCRKRKLERIARLEEKVKTLKA` | 35.7% | Yes |
| Zip1 (Q9Y7P6) | (basic region not auto-detected by heuristic) | — | — |

**Interpretation (conservative):**
- Pap1 has a *bona fide* bZIP basic region carrying the invariant `N-R-A-A-Q-R` signature, so the
  Jun/Fos orthology is real **at the diverged-fold level** — but sequence identity to human
  JUN/FOS is low (21–36%), so the "pioneer like Jun/Fos" argument is weak analogy, not homology-grade evidence.
- Pap1 **lacks** the AP-1 basic-region redox cysteine present in FOS/JUN/Atf1; Pap1 instead senses
  redox via separate n-CRD/c-CRD domains — a documented mechanistic divergence from the AP-1 paradigm.
- In Jun/Fos the **same** basic-region helix reads free DNA *and* nucleosomal DNA. Thus, if Pap1
  engages nucleosomes, the fold predicts **nucleosomal-DNA reading via its DNA-binding basic region**,
  i.e., an extension of sequence-specific DNA binding onto chromatin — *not* a separate histone-core
  protein-protein MF. This nuance should shape the GO term choice (nucleosomal-DNA/chromatin binding
  vs. a distinct nucleosome/histone-binding MF) and argues further against an unqualified,
  high-confidence "direct nucleosome binding" MF call.

*Note:* Attempts to retrieve the atlas full text (bioRxiv / Cell) for the decisive methods detail —
whether the Pap1–histone co-IP is nuclease/DNase-resistant — were blocked (HTTP 429/403). That
single fact (DNA-dependence of the co-purification) remains the key unresolved discriminator and
should be checked by a curator in the paper's supplement.

---

## Limitations of this review

- Programmatic access: PubMed and UniProt REST were queried successfully; the bioRxiv/Cell full
  text was rate-limited (HTTP 429), so the exact Results-section wording was obtained via web
  search summaries and should be verified verbatim by a curator before quoting in the annotation.
- The published abstract of PMID 40015273 does not mention Pap1 or nucleosomes; the finding lives
  in the body, limiting snippet-level validation.
- No local `*-bioinformatics` analyses were available (intentionally withheld); conclusions rest on
  primary literature, the public atlas, and UniProt/PomBase records.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)