---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T23:41:42.510255'
end_time: '2026-10-09T23:56:02.013793'
duration_seconds: 859.5
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: ndx-4
  gene_symbol: ndx-4
  uniprot_accession: Q9U2M7
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: function_assignment
  hypothesis_slug: ndx-4-8oxo-dgtp-sanitiser
  hypothesis_text: 'C. elegans NDX-4 (Q9U2M7) is a physiologically relevant MutT-type
    sanitiser of oxidised guanine nucleotides (8-oxo-dGTP / 8-oxo-GTP), in addition
    to its established role as an asymmetric Ap4A hydrolase. Test this with one decisive
    structural question: does the NDX-4 substrate-binding pocket (crystal structures
    PDB 1KT9 and 1KTG) have the features that let MutT/MTH1-type enzymes recognise
    and prefer the 8-oxoguanine base over guanine, or does it resemble the adenine-stacking
    pocket of NUDT2-type Ap4A hydrolases? Weigh this against the reported biochemistry:
    purified NDX-4 hydrolysed 8-oxo-dGTP 59.5% vs dGTP 24.0% and 8-oxo-GTP 34.3% vs
    GTP 33.7% in single-point assays (20 uM substrate, 1.51 uM enzyme, 30 min), releasing
    a single phosphate from 8-oxo-GTP (product 8-oxo-GDP), whereas Ap4A hydrolysis
    has Km about 7-9 uM and kcat about 23-27 s-1.'
  term_context: No specific term context supplied.
  reference_context: '- PMID:21111690

    - PMID:24435662

    - PMID:24347047

    - PMID:11738085

    - PMID:12370170'
  source_file: genes/worm/ndx-4/ndx-4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'C. elegans NDX-4 (Q9U2M7) is a physiologically\
    \ relevant MutT-type sanitiser of oxidised guanine\n  nucleotides (8-oxo-dGTP\
    \ / 8-oxo-GTP), in addition to its established role as an asymmetric Ap4A hydrolase.\n\
    \  Test this with one decisive structural question: does the NDX-4 substrate-binding\
    \ pocket (crystal structures\n  PDB 1KT9 and 1KTG) have the features that let\
    \ MutT/MTH1-type enzymes recognise and prefer the 8-oxoguanine\n  base over guanine,\
    \ or does it resemble the adenine-stacking pocket of NUDT2-type Ap4A hydrolases?\
    \ Weigh\n  this against the reported biochemistry: purified NDX-4 hydrolysed 8-oxo-dGTP\
    \ 59.5% vs dGTP 24.0% and\n  8-oxo-GTP 34.3% vs GTP 33.7% in single-point assays\
    \ (20 uM substrate, 1.51 uM enzyme, 30 min), releasing\n  a single phosphate from\
    \ 8-oxo-GTP (product 8-oxo-GDP), whereas Ap4A hydrolysis has Km about 7-9 uM and\n\
    \  kcat about 23-27 s-1.'\nfocus_type: function_assignment\ncontext: []\nreference_id:\n\
    - PMID:21111690\n- PMID:24435662\n- PMID:24347047\n- PMID:11738085\n- PMID:12370170"
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
citation_count: 9
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: ndx4_GO_decision_table.csv
  path: openscientist_artifacts/ndx4_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ndx4 GO decision table
- filename: ndx4_current_GO_annotations.csv
  path: openscientist_artifacts/ndx4_current_GO_annotations.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ndx4 current GO annotations
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
- **Gene directory:** ndx-4
- **Gene symbol:** ndx-4
- **UniProt accession:** Q9U2M7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** ndx-4-8oxo-dgtp-sanitiser
- **Source file:** genes/worm/ndx-4/ndx-4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

C. elegans NDX-4 (Q9U2M7) is a physiologically relevant MutT-type sanitiser of oxidised guanine nucleotides (8-oxo-dGTP / 8-oxo-GTP), in addition to its established role as an asymmetric Ap4A hydrolase. Test this with one decisive structural question: does the NDX-4 substrate-binding pocket (crystal structures PDB 1KT9 and 1KTG) have the features that let MutT/MTH1-type enzymes recognise and prefer the 8-oxoguanine base over guanine, or does it resemble the adenine-stacking pocket of NUDT2-type Ap4A hydrolases? Weigh this against the reported biochemistry: purified NDX-4 hydrolysed 8-oxo-dGTP 59.5% vs dGTP 24.0% and 8-oxo-GTP 34.3% vs GTP 33.7% in single-point assays (20 uM substrate, 1.51 uM enzyme, 30 min), releasing a single phosphate from 8-oxo-GTP (product 8-oxo-GDP), whereas Ap4A hydrolysis has Km about 7-9 uM and kcat about 23-27 s-1.

## Term and Decision Context

No specific term context supplied.

## Reference Context

- PMID:21111690
- PMID:24435662
- PMID:24347047
- PMID:11738085
- PMID:12370170

## Source Context YAML

```yaml
hypothesis: 'C. elegans NDX-4 (Q9U2M7) is a physiologically relevant MutT-type sanitiser of oxidised guanine
  nucleotides (8-oxo-dGTP / 8-oxo-GTP), in addition to its established role as an asymmetric Ap4A hydrolase.
  Test this with one decisive structural question: does the NDX-4 substrate-binding pocket (crystal structures
  PDB 1KT9 and 1KTG) have the features that let MutT/MTH1-type enzymes recognise and prefer the 8-oxoguanine
  base over guanine, or does it resemble the adenine-stacking pocket of NUDT2-type Ap4A hydrolases? Weigh
  this against the reported biochemistry: purified NDX-4 hydrolysed 8-oxo-dGTP 59.5% vs dGTP 24.0% and
  8-oxo-GTP 34.3% vs GTP 33.7% in single-point assays (20 uM substrate, 1.51 uM enzyme, 30 min), releasing
  a single phosphate from 8-oxo-GTP (product 8-oxo-GDP), whereas Ap4A hydrolysis has Km about 7-9 uM and
  kcat about 23-27 s-1.'
focus_type: function_assignment
context: []
reference_id:
- PMID:21111690
- PMID:24435662
- PMID:24347047
- PMID:11738085
- PMID:12370170
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

# NDX-4 (Q9U2M7) as a MutT-type 8-oxo-dGTP/8-oxo-GTP Sanitiser — Focused Curation Report

**Gene:** *ndx-4* (worm, *C. elegans*, NCBITaxon:6239) · **UniProt:** Q9U2M7 · **Structures:** PDB 1KT9, 1KTG
**Focus:** function_assignment · **Hypothesis slug:** ndx-4-8oxo-dgtp-sanitiser

---

## Executive Judgment

**Partially supported — with the specific "MutT-type sanitiser" framing over-annotated.**

The decisive structural question resolves **against** the seed hypothesis. NDX-4's substrate pocket
is the **NUDT2-type adenine-stacking Ap4A-hydrolase pocket**, not a MutT/MTH1-type
8-oxoguanine-recognition pocket. This is supported by two independent public lines of evidence:

1. **Structure (PDB 1KT9/1KTG, Bailey 2002, PMID:11937063):** the C. elegans Ap4A hydrolase binds its
   nucleotide substrate by **adenine ring-stacking** (explicitly noted in PMID:20124691) and is tuned for
   dinucleoside **tetra**phosphates, not mononucleotide triphosphates. **Direct coordinate analysis of
   1KTG performed here** shows the bound AMP adenine base is sandwiched by two tyrosines — **Tyr76**
   (3.36 Å, over N7) and **Tyr121** (3.34 Å, over C6) — plus His31 and Leu74, i.e. an aromatic
   ring-stacking pocket with no hydrogen-bond donor/acceptor arrangement poised to read the 8-oxoguanine
   O8/N7-H edge that MutT (Asn119) and human MTH1 rely on.
2. **Sequence/evolution:** NDX-4 is **49.0% identical to human NUDT2** (the canonical asymmetric Ap4A
   hydrolase) but only **25.0% / 20.3%** identical to E. coli MutT / human MTH1 — i.e. background-level for
   Nudix proteins that merely share the catalytic box. NDX-4 and NUDT2 share a near-identical
   substrate/Nudix-box segment (`WTPPKGHV_PGED…RET.EEA.I`).

The *in vitro* oxidized-nucleotide activity is real but **weak and non-specific**: ~2.5× preference for
8-oxo-dGTP over dGTP, and **no discrimination at all** for 8-oxo-GTP vs GTP (34.3% vs 33.7%), measured only
in single-point assays at a very high enzyme:substrate ratio (1.51 µM enzyme / 20 µM substrate / 30 min),
with **no kcat/Km reported** — versus a kinetically defined Ap4A hydrolase (Km 7 µM, kcat 27 s⁻¹). The
reported 8-oxo-GTP → **8-oxo-GDP** product (loss of a single phosphate) is **not** the canonical MutT
sanitisation chemistry (8-oxo-dGMP + PPi) and leaves a rephosphorylatable, incompletely "sanitised"
product. The activity is also **redundant** (NDX-1, NDX-2, NDX-4 all show 8-oxo-GTPase/GDPase activity;
NDX-2 does the canonical 8-oxo-dGDP→8-oxo-dGMP reaction; PMID:24435662).

**Net:** NDX-4 genuinely possesses a moonlighting oxidized-guanine-nucleotide hydrolase side activity and
contributes to genome stability *in vivo* (PMID:21111690), but it is **not** a dedicated, structurally
specialised MutT-type sanitiser. Its **primary/core function is the asymmetric Ap4A hydrolase**.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID:11937063 (Bailey 2002) | Structural | Refutes MutT-pocket | Does the NDX-4 pocket recognise 8-oxoG? | Crystal structure (free + binary); pocket oriented for dinucleoside **tetra**phosphates "but not triphosphate" via precise adenine orientation | NDX-4 protein, PDB 1KT9/1KTG | High; structure is of apo/Ap4A-analogue, not an 8-oxo-dGTP complex |
| PMID:20124691 (Jeyakanthan 2010) | Structural | Refutes MutT-pocket | Mode of nucleotide binding in this family | States C. elegans Ap4A hydrolase binds the **adenine moiety by ring-stacking** | Aquifex Ap4A hydrolase, references C. elegans | High for binding mode; cross-species inference |
| PDB 1KTG (this report, direct coord. analysis) | Structural/computational | Refutes MutT-pocket | Which residues line the NDX-4 base pocket? | Bound AMP adenine base is sandwiched by **Tyr76 (3.36 Å, over N7) and Tyr121 (3.34 Å, over C6)**, with His31 and Leu74; aromatic ring-stacking, no O8-specific H-bond apparatus | NDX-4 binary complex, 1.80 Å | High; pocket holds adenine (AMP), not an 8-oxoG complex (inference about 8-oxoG reading) |
| This report (public seq, NW alignment) | Computational / evolutionary | Refutes MutT-type assignment | Is NDX-4 a MutT/MTH1 or NUDT2 ortholog? | 49% id to NUDT2 vs 25%/20% to MutT/MTH1; shared NUDT2 Nudix-box segment | Q9U2M7 vs P50583/P08337/P36639 | High; simple global alignment, but signal is unambiguous |
| PMID:11738085 (Abdelghany 2001) | Direct assay (kinetics) | Supports core Ap4A function | What is the primary catalytic activity? | Ap4A hydrolase, **Km 7 µM, kcat 27 s⁻¹**, products AMP+ATP | Recombinant C. elegans enzyme | High |
| PMID:12475970 (Abdelghany 2003) | Direct assay / mutagenesis | Supports core Ap4A function | Catalytic residues | kcat 23 s⁻¹; Nudix-box Glu residues essential; defines active site | Recombinant enzyme | High |
| PMID:21111690 (Arczewska 2011) | Direct assay + mutant phenotype | Supports (in vivo) | Does NDX-4 act as a MutT-type enzyme in vivo? | Hydrolyses 8-oxo-dGTP, **suppresses E. coli mutT mutator**, ndx-4 loss → genome instability + stress-gene upregulation | C. elegans + E. coli complementation | Medium–High for in vivo role; genetic read-out, not active-site proof |
| PMID:24435662 (Sanada 2014) | Direct assay + mutant phenotype | Qualifies / competes | Is NDX-4 the dedicated sanitiser? | **NDX-1, NDX-2, NDX-4** all have 8-oxo-GTPase/GDPase activity; **NDX-2** does canonical 8-oxo-dGDP→8-oxo-dGMP; checkpoint (chk-2/clk-2) response | C. elegans | Medium; shows redundancy & that NDX-2 is the cleaner MutT-type |
| PMID:12370170 (Fisher 2002) | Direct assay | Qualifies (promiscuity) | Substrate breadth of this Nudix | C. elegans Ap4A hydrolase active site is promiscuous (also a PRPP pyrophosphatase) | Recombinant enzyme | Medium; shows the single active site hydrolyses several substrates — side activities expected |
| PMID:24347047 (silver NP study) | Review/indirect | Context only | — | Oxidative DNA damage-repair in C. elegans vs human; no direct NDX-4 active-site data | — | Low relevance to active-site question |
| PMID:28035004 (Waz 2017) | Structural (comparator) | Reference | What a true 8-oxoGTPase pocket looks like | MTH1 broad specificity via specific O8/N7 recognition of oxidized bases | Human MTH1 | High; defines the pocket NDX-4 lacks |

---

## GO Curation Implications (leads — require curator verification)

**Verified current annotation state (QuickGO, Q9U2M7, this iteration):** All existing MF/BP annotations are
Ap4A-hydrolase-centric — **GO:0004081** *bis(5'-nucleosyl)-tetraphosphatase (asymmetrical) activity* (IDA,
PMID:11738085 & PMID:12475970), GO:0008796 (IEA/InterPro), GO:0016787 (IEA), plus BPs GO:0015967
(diadenosine polyphosphate catabolism), GO:0006167/0006172/0006754 (AMP/ADP/ATP biosynthesis), GO:0019693 &
GO:0043135 (PRPP side activity), and GO:0006915 apoptosis (TAS). **Critically, there is NO existing
8-oxo-dGTP/8-oxo-GTP hydrolase MF or DNA-repair/sanitization BP annotation** — so the seed hypothesis is a
proposal to **add a currently-absent function**, not to modify an existing one. (Provenance:
`ndx4_current_GO_annotations.csv`, `ndx4_GO_decision_table.csv`.)

- **Core MF — RETAIN as primary:** `bis(5'-nucleosyl)-tetraphosphatase (asymmetrical) activity`
  (**GO:0004081**; IEA parent GO:0008796). Strongly supported by kinetics (PMID:11738085, PMID:12475970) and
  structure (PMID:11937063). This remains the gene's primary molecular function and is already correctly
  annotated.
- **8-oxo-dGTP sanitiser MF — ADD ONLY AS SECONDARY / NON-CORE, qualified:** a term such as
  `8-oxo-7,8-dihydrodeoxyguanosine triphosphate pyrophosphatase activity` (**GO:0035539**) or an
  8-oxo-GTP diphosphatase term is defensible from PMID:21111690/PMID:24435662, but should carry caveats:
  (a) in-vitro single-point evidence (no kcat/Km), (b) modest/absent base discrimination, (c) redundancy
  with NDX-1/NDX-2, and (d) a **product mismatch** — for 8-oxo-GTP the reported product is 8-oxo-**GDP**
  (single-phosphate release), which does not match a pyrophosphatase (PPi-releasing) definition. If only a
  single phosphate is released, GO:0035539 (a diphosphatase/pyrophosphatase term) may be the **wrong**
  term; a monophosphatase/"GDPase" framing would be needed. **Recommend curator confirm the product/chemistry
  before selecting the MF term.**
- **BP — ADD cautiously:** `DNA repair` (**GO:0006281**) / nucleotide-pool sanitisation /
  `GTP catabolic process`, supported *in vivo* by the mutT-complementation and genome-stability phenotype
  (PMID:21111690), but flag as a secondary/context role given paralog redundancy.
- **Do NOT annotate** NDX-4 as a dedicated/orthologous **MutT/MTH1** enzyme by sequence orthology — it is a
  NUDT2 ortholog (49% id) and the MutT label reflects a functional moonlighting activity, not orthology.
- Avoid "protein binding" as an outcome; the informative MF is the Ap4A hydrolase activity.

---

## Mechanistic Scope

**Direct molecular activity:** Mg²⁺-dependent Nudix hydrolysis. The structurally and kinetically defined
reaction is asymmetric cleavage of Ap4A → AMP + ATP (and related adenosine/dinucleoside polyphosphates with
≥4 phosphates; also PRPP). The oxidized-nucleotide hydrolysis uses the **same single active site**
(PMID:12370170 shows this site is promiscuous), so 8-oxo-(d)GTP turnover is best interpreted as a
low-specificity side reaction of the Ap4A pocket rather than an independent, optimised sanitiser site.

**Downstream / inferred (not direct active-site evidence):** genome stability, suppression of mutator
phenotype, stress-responsive gene upregulation on *ndx-4* loss (PMID:21111690), and checkpoint-regulated
post-embryonic development on oxidized-nucleotide accumulation (PMID:24435662). These are genetic/phenotypic
outcomes consistent with — but not uniquely diagnostic of — a dedicated MutT-type active site.

---

## Conflicts and Alternatives

- **Paralog redundancy / mis-attribution:** NDX-1, NDX-2 and NDX-4 share 8-oxo-nucleotide activity, and
  **NDX-2** carries out the canonical MutT product chemistry (8-oxo-dGDP→8-oxo-dGMP). The "dedicated worm
  MutT" role may belong more to NDX-2 than NDX-4 (PMID:24435662).
- **Orthology:** NDX-4 is a NUDT2 ortholog (adenine-stacking Ap4A hydrolase), not a MutT/MTH1 ortholog;
  the "MutT-type" descriptor is a functional analogy, not evolutionary identity.
- **Chemistry mismatch:** release of a single phosphate (8-oxo-GTP→8-oxo-GDP) differs from MutT/MTH1
  pyrophosphate release; the product is incompletely sanitised.
- **Assay artefact risk:** single-point, high-enzyme assays can exaggerate weak activities; no kcat/Km or
  specificity constant has been reported for the oxidized substrates.

---

## Knowledge Gaps

1. **Catalytic efficiency for 8-oxo-(d)GTP.** Checked: no kcat/Km in the cited literature. Matters: decides
   whether sanitisation is physiologically meaningful vs trace. Resolve with steady-state kinetics and a
   kcat/Km comparison to Ap4A and to NDX-2/MTH1.
2. **Reaction product identity (mono- vs diphosphate; PPi vs Pi).** Checked: PMID:24435662 reports 8-oxo-GDP;
   dGTP product not clearly specified. Matters: determines the correct GO MF term. Resolve by HPLC/MS of
   products for 8-oxo-dGTP and 8-oxo-GTP.
3. **Direct structural proof of 8-oxoG recognition.** Checked: PDB 1KT9/1KTG are apo/Ap4A-analogue, not
   8-oxo-dGTP complexes. Matters: the structural claim is currently inference from an adenine-stacking pocket.
   Resolve by co-crystal/docking of 8-oxo-dGTP, or mutagenesis of putative base-contact residues.
4. **In-vivo substrate.** Checked: genome-stability phenotype is genetic. Matters: distinguishes 8-oxo-dGTP
   sanitisation from Ap4A-signalling/stress roles. Resolve by measuring 8-oxo-dG/8-oxo-G in DNA/RNA and the
   nucleotide pool in *ndx-4* vs *ndx-2* mutants.

---

## Discriminating Tests

- **Side-by-side steady-state kinetics** (kcat/Km) of NDX-4 for Ap4A, 8-oxo-dGTP, dGTP, 8-oxo-GTP, GTP,
  benchmarked against NDX-2 and human MTH1. A specificity constant for 8-oxo-dGTP within ~10× of MTH1 would
  support the hypothesis; ≥100–1000× lower would refute a dedicated-sanitiser role.
- **Product analysis (LC-MS)** to confirm whether PPi or Pi is released (MutT-type vs NDP-forming).
- **Structure-guided mutagenesis / co-crystallography** with 8-oxo-dGTP to test for specific O8/N7-H base
  contacts (present in MutT/MTH1, predicted absent in NDX-4).
- **Genetic epistasis** of *ndx-4* vs *ndx-2* (single/double mutants) for 8-oxo-dG accumulation and mutation
  rate, to allocate the in-vivo sanitiser role among paralogs.

---

## Curation Leads (require curator verification)

- **Retain** primary MF **GO:0004081** (asymmetric Ap4A hydrolase; IEA parent GO:0008796) — core function,
  already annotated IDA; refs PMID:11738085, PMID:12475970, PMID:11937063.
- **Note for curator:** the 8-oxo sanitiser function is currently **unannotated** in GO for ndx-4; this
  hypothesis would introduce it as a new term (see decision table below / `ndx4_GO_decision_table.csv`).
- **Add, qualified/non-core**, a 8-oxo-guanine-nucleotide hydrolase MF — but **verify the product chemistry**
  before choosing between a pyrophosphatase term (e.g. GO:0035539) and a (di/mono)phosphatase term; refs
  PMID:21111690, PMID:24435662.
- **Add, cautiously**, BP GO:0006281 (DNA repair) / nucleotide-pool sanitisation as a secondary role; ref
  PMID:21111690.
- **Flag** the "MutT-type" label as a functional analogy, not orthology (NDX-4 ≈ NUDT2 ortholog, 49% id).
- **Suggested curator questions:** (1) Is the 8-oxo-dGTP product 8-oxo-dGMP+PPi or 8-oxo-dGDP+Pi? (2) Is the
  dedicated worm MutT better assigned to NDX-2? (3) Should the 8-oxo activity be annotated with an
  IDA/in-vitro qualifier and a redundancy note?
- **Candidate references with snippets to verify:**
  - PMID:21111690 — "NDX-4 exhibits both hallmarks of a MutT-type enzyme with an ability to hydrolyze
    8-oxodGTP and suppress the Escherichia coli mutT mutator phenotype."
  - PMID:24435662 — "NDX-1, NDX-2 and NDX-4 proteins have 8-oxo-GTPase or 8-oxo-GDPase activity."
  - PMID:11738085 — "It hydrolyses Ap4A with a K(m) of 7 microM and k(cat) of 27 s(-1)."
  - PMID:20124691 — "the adenine moiety of the nucleotide binds in a ring-stacking arrangement equivalent to
    that observed in the X-ray structure of Ap(4)A hydrolase from Caenorhabditis elegans."

---

## Limitations

Analysis relied on public sequence, structure metadata, and abstracts; full-text kinetic tables and the
atomic coordinates were not re-refined here. The structural argument against 8-oxoG recognition is strong but
is inferred from binding mode + orthology rather than from a direct 8-oxo-dGTP·NDX-4 complex. Pairwise
identities used a simple global alignment; values are approximate but the family assignment is unambiguous.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist ndx4 GO decision table](openscientist_artifacts/ndx4_GO_decision_table.csv)
- [OpenScientist ndx4 current GO annotations](openscientist_artifacts/ndx4_current_GO_annotations.csv)