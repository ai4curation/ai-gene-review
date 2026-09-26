---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T20:29:06.795533'
end_time: '2026-09-20T20:57:59.040430'
duration_seconds: 1732.25
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: BCL2
  gene_symbol: BCL2
  uniprot_accession: P10415
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: conditional-proapoptotic-and-channel-capacities
  hypothesis_text: Human BCL2 can positively regulate apoptotic processes after caspase
    cleavage or conformational conversion, and can form functional channels or pores
    contributing to transmembrane transport. Evaluate these claims independently against
    full primary studies including PMID:9395403, PMID:14980220 and PMID:9219694, target
    construct/processing state, assay pH and membrane context. Distinguish predominant
    native antiapoptotic function from demonstrated conditional intrinsic capacities.
    Establish which gene product performs the proapoptotic step and whether transport
    evidence reflects intrinsic BCL2 pore formation or regulation of another channel.
    Read actual PAINT node placement, descendant evidence and loss/divergence; do
    not use family-role exclusivity or absent target assays alone to reject ancestral
    assertions. Consider whether conclusions extend to mouse Bcl2 with species-specific
    primary support.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/BCL2/BCL2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human BCL2 can positively regulate apoptotic processes\
    \ after caspase cleavage or conformational\n  conversion, and can form functional\
    \ channels or pores contributing to transmembrane transport. Evaluate\n  these\
    \ claims independently against full primary studies including PMID:9395403, PMID:14980220\
    \ and PMID:9219694,\n  target construct/processing state, assay pH and membrane\
    \ context. Distinguish predominant native antiapoptotic\n  function from demonstrated\
    \ conditional intrinsic capacities. Establish which gene product performs the\n\
    \  proapoptotic step and whether transport evidence reflects intrinsic BCL2 pore\
    \ formation or regulation\n  of another channel. Read actual PAINT node placement,\
    \ descendant evidence and loss/divergence; do not\n  use family-role exclusivity\
    \ or absent target assays alone to reject ancestral assertions. Consider whether\n\
    \  conclusions extend to mouse Bcl2 with species-specific primary support.\nfocus_type:\
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
citation_count: 11
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
- **Gene directory:** BCL2
- **Gene symbol:** BCL2
- **UniProt accession:** P10415

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** conditional-proapoptotic-and-channel-capacities
- **Source file:** genes/human/BCL2/BCL2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human BCL2 can positively regulate apoptotic processes after caspase cleavage or conformational conversion, and can form functional channels or pores contributing to transmembrane transport. Evaluate these claims independently against full primary studies including PMID:9395403, PMID:14980220 and PMID:9219694, target construct/processing state, assay pH and membrane context. Distinguish predominant native antiapoptotic function from demonstrated conditional intrinsic capacities. Establish which gene product performs the proapoptotic step and whether transport evidence reflects intrinsic BCL2 pore formation or regulation of another channel. Read actual PAINT node placement, descendant evidence and loss/divergence; do not use family-role exclusivity or absent target assays alone to reject ancestral assertions. Consider whether conclusions extend to mouse Bcl2 with species-specific primary support.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human BCL2 can positively regulate apoptotic processes after caspase cleavage or conformational
  conversion, and can form functional channels or pores contributing to transmembrane transport. Evaluate
  these claims independently against full primary studies including PMID:9395403, PMID:14980220 and PMID:9219694,
  target construct/processing state, assay pH and membrane context. Distinguish predominant native antiapoptotic
  function from demonstrated conditional intrinsic capacities. Establish which gene product performs the
  proapoptotic step and whether transport evidence reflects intrinsic BCL2 pore formation or regulation
  of another channel. Read actual PAINT node placement, descendant evidence and loss/divergence; do not
  use family-role exclusivity or absent target assays alone to reject ancestral assertions. Consider whether
  conclusions extend to mouse Bcl2 with species-specific primary support.
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

# AIGR Gene Hypothesis Deep Research — Human BCL2 (P10415)

## Conditional Pro-apoptotic and Channel Capacities

**Focus type:** function_assignment
**Hypothesis slug:** conditional-proapoptotic-and-channel-capacities
**Source file:** genes/human/BCL2/BCL2-ai-review.yaml

---

## Summary

**Executive verdict: PARTIALLY SUPPORTED.** The seed hypothesis makes two distinct
claims about human BCL2 — (1) that it can *positively* regulate apoptosis after
caspase cleavage or conformational conversion, and (2) that it can form functional
channels/pores contributing to transmembrane transport. Both claims are backed by
direct primary experimental data, but in each case the activity is **conditional,
in-vitro or context-restricted, and mechanistically distinct from BCL2's predominant
native antiapoptotic function.** The correct curation posture is therefore *retain
with qualifiers*, not *reject*, and not *promote to core function*.

The proapoptotic capacity is real but proteoform- and context-dependent. BCL2 becomes
a death effector in two mechanistically separate ways. First, caspase-3 cleaves BCL2 at
Asp34, and the resulting **C-terminal cleavage fragment** — not the intact native
protein — behaves like a Bax-like killer that triggers cell death via its BH3 and
transmembrane domains ([PMID:9395403](https://pubmed.ncbi.nlm.nih.gov/9395403/)).
Second, the **intact full-length protein** can be converted from protector to killer by
binding the orphan nuclear receptor Nur77/TR3, which induces a conformational change
exposing the BH3 domain ([PMID:14980220](https://pubmed.ncbi.nlm.nih.gov/14980220/)).
The gene product that performs the proapoptotic step is thus either a processed fragment
or a conformationally altered complex, not the resting antiapoptotic conformer.

The channel/transport capacity is likewise genuine but restricted. Purified recombinant
BCL2 forms discrete, cation-selective ion-conducting channels in planar lipid bilayers,
and this requires the core hydrophobic h5–h6 helices
([PMID:9144199](https://pubmed.ncbi.nlm.nih.gov/9144199/)). However, its
membrane-permeabilizing pore activity is only observed at **acidic pH on acidic lipids**
([PMID:9219694](https://pubmed.ncbi.nlm.nih.gov/9219694/)), and at physiological pH its
dominant transport-related role is the opposite — **inhibiting** other channels, blocking
Bax channel activity ([PMID:9219694](https://pubmed.ncbi.nlm.nih.gov/9219694/)) and
reducing IP3 receptor open probability
([PMID:15263017](https://pubmed.ncbi.nlm.nih.gov/15263017/)). Both the channel-activity
(MF) and positive-regulation-of-apoptosis (BP) GO terms **already exist** on BCL2, and
the channel-activity IBA is supported by direct experimental (IDA) annotations across the
Bcl-2 family (BCL2, BAX, BAK1), so the ancestral GO_Central inference should not be
rejected on family-role-exclusivity grounds.

---

## Key Findings

### Finding 1 — Caspase cleavage at Asp34 yields a Bax-like proapoptotic fragment

Cheng et al. 1997 ([PMID:9395403](https://pubmed.ncbi.nlm.nih.gov/9395403/), *Conversion
of Bcl-2 to a Bax-like death effector by caspases*, Science) demonstrated that the
flexible loop of BCL2 is cleaved at Asp34 by caspase-3. This cleavage was observed *in
vitro* with recombinant caspase-3, in caspase-3-overexpressing cells, and during
physiological apoptosis (Fas ligation and IL-3 withdrawal). The critical mechanistic
point is that proapoptotic activity is a property of the **cleavage product**, not the
intact native protein:

> "The carboxyl-terminal Bcl-2 cleavage product triggered cell death and accelerated
> Sindbis virus-induced apoptosis, which was dependent on the BH3 homology and
> transmembrane domains of Bcl-2." — [PMID:9395403](https://pubmed.ncbi.nlm.nih.gov/9395403/)

Importantly, cleavage-resistant Asp34 mutants showed **increased** protection against
apoptosis, confirming that removing the cleavage site removes a proapoptotic liability.
This establishes a clean answer to one of the seed's discriminating questions: **the gene
product that performs the proapoptotic step is the C-terminal caspase fragment**, which
acts through the conserved BH3 and transmembrane domains, functionally converting BCL2
into a Bax-like effector. This is a feed-forward amplification mechanism, not the
resting function.

### Finding 2 — Nur77/TR3 converts intact BCL2 into a killer via BH3 exposure

Lin et al. 2004 ([PMID:14980220](https://pubmed.ncbi.nlm.nih.gov/14980220/), *Conversion
of Bcl-2 from protector to killer by interaction with nuclear orphan receptor
Nur77/TR3*, Cell) showed a second, cleavage-independent route to proapoptotic activity.
The orphan nuclear receptor Nur77/TR3 binds the N-terminal loop of BCL2, and:

> "Nur77 binding induces a Bcl-2 conformational change that exposes its BH3 domain,
> resulting in conversion of Bcl-2 from a protector to a killer." — [PMID:14980220](https://pubmed.ncbi.nlm.nih.gov/14980220/)

Here the **same full-length gene product** (no proteolysis) acquires proapoptotic
activity through an induced conformational change that unmasks its BH3 domain and targets
Nur77 to mitochondria. This is significant for curation because it shows the proapoptotic
capacity is intrinsic to the folded protein under the right partner/conformational
context — it does not strictly require caspase processing. Together, Findings 1 and 2
establish two independent, experimentally validated conditional proapoptotic mechanisms.

### Finding 3 — BCL2 forms intrinsic channels, but permeabilization is pH/lipid-restricted; physiological role is channel *regulation*

Schendel et al. 1997 ([PMID:9144199](https://pubmed.ncbi.nlm.nih.gov/9144199/), *Channel
formation by antiapoptotic protein Bcl-2*, PNAS) provided direct biophysical evidence
that purified recombinant BCL2 has intrinsic channel-forming activity:

> "In planar lipid bilayers, where detection of single channels is possible, Bcl-2
> formed discrete ion-conducting, cation-selective channels, whereas the Bcl-2
> (Deltah5, 6) mutant did not." — [PMID:9144199](https://pubmed.ncbi.nlm.nih.gov/9144199/)

Single-channel conductance was 18 ± 2 pS in 0.5 M KCl at pH 7.4, with larger 41 and 90 pS
substates, and the activity required the core hydrophobic h5–h6 helices (the Δh5,6 mutant
was inactive). This structurally maps the channel to the same pore-forming module shared
across the Bcl-2 fold and the bacterial pore-forming toxins (diphtheria toxin, colicins).

However, the *membrane-permeabilizing* (pore/efflux) activity is strongly restricted.
Antonsson et al. 1997 ([PMID:9219694](https://pubmed.ncbi.nlm.nih.gov/9219694/),
*Inhibition of Bax channel-forming activity by Bcl-2*) found that:

> "Bcl-2, in contrast, triggered carboxyfluorescein release at acidic pH only." —
> [PMID:9219694](https://pubmed.ncbi.nlm.nih.gov/9219694/)

and, critically, that at physiological pH BCL2 **blocks** Bax channel activity rather than
forming its own permeabilizing pore. This directly answers the seed's discriminating
question about whether transport evidence reflects intrinsic pore formation or regulation
of another channel: **both are documented, but the physiologically dominant activity is
channel regulation/inhibition, not intrinsic permeabilization.** This is reinforced by
Chen et al. 2004 ([PMID:15263017](https://pubmed.ncbi.nlm.nih.gov/15263017/)), which
showed BCL2 reduces the open probability of IP3 receptor Ca²⁺ channels reconstituted in
bilayers, again an inhibitory/regulatory role.

Paralog evidence supports an ancestral channel-forming capacity of the fold: Minn et al.
1997 ([PMID:9002522](https://pubmed.ncbi.nlm.nih.gov/9002522/)) showed Bcl-xL forms
ion-conducting channels in synthetic membranes:

> "Like the bacterial toxins, Bcl-xL can insert into either synthetic lipid vesicles or
> planar lipid bilayers and form an ion-conducting channel." —
> [PMID:9002522](https://pubmed.ncbi.nlm.nih.gov/9002522/)

### Finding 4 — Caspase Asp34 motif and h5–h6 channel core are conserved human↔mouse

Comparison of UniProt sequences P10415 (human, 239 aa) and P10417 (mouse, 236 aa) shows
that the structural determinants of both conditional activities are conserved. The
caspase-3 cleavage motif DAGD (D31-A32-G33-D34) is fully conserved (residue 34 = Asp in
both species), and the core hydrophobic h5–h6 channel-forming region (~res 140–200) is
essentially identical:

| Feature | Human (P10415) | Mouse (P10417) | Conserved? |
|---|---|---|---|
| Length | 239 aa | 236 aa | — |
| Caspase site (res 25–45) | QRGYEW**DAGD**VGAAPPGAAPA | QRGYEW**DAGD**ADAAPLGAAPT | Asp34 conserved |
| h5–h6 core (~140–200) | DGVNWGRIVAFFEFGGVMCVESVNREMSPLVDNIALWMTEYLNRHLHTWIQDNGGWDAFVE | NWGRIVAFFEFGGVMCVESVNREMSPLVDNIALWMTEYLNRHLHTWIQDNGGWDAFVELYG | Essentially identical |

This means the *capacity* to be cleaved into a Bax-like fragment and to form a channel is
sequence-encoded in mouse Bcl2, but this is inference from conservation only —
**species-specific primary functional support in mouse was not established** in this
investigation.

### Finding 5 — Both GO terms already exist on BCL2, but direct proapoptotic papers are uncited

QuickGO for UniProtKB:P10415 (248 annotations) shows the relevant terms are already
present:

| GO term | Aspect | Evidence on BCL2 | Notes |
|---|---|---|---|
| GO:0015267 channel activity | MF | **IBA** (GO_REF:0000033) + **IDA** (PMID:9219694) | Ancestral + direct |
| GO:0016248 channel inhibitor activity | MF | IDA (PMID:9219694) | Regulatory role |
| GO:0055085 transmembrane transport | BP | IEA (GO_REF:0000108) | Electronic only |
| GO:0043065 positive regulation of apoptotic process | BP | **IBA** + **NAS** (PMID:14634621) | No IDA; neither PMID:9395403 nor 14980220 cited |
| GO:0043066 negative regulation of apoptotic process | BP | ~14 annotations incl. IDA/IMP | Predominant native role |
| GO:0046902 reg. mitochondrial membrane permeability | BP | ISS (PMID:9843949) | — |
| GO:0051924 regulation of calcium ion transport | BP | IDA (PMID:8022822) | — |

The predominant native antiapoptotic role (GO:0043066) is much more heavily and directly
supported (~14 annotations, many IDA/IMP) than the proapoptotic role, confirming that
positive regulation of apoptosis is a **minority, conditional** annotation. Notably, the
two strongest primary proapoptotic papers (PMID:9395403, PMID:14980220) are **not** cited
on the positive-regulation term — they are candidate IDA additions.

### Finding 6 — The ancestral channel IBA is descendant-supported across the family

QuickGO across the Bcl-2 family for GO:0015267 channel activity:

| Gene | UniProt | Channel activity evidence |
|---|---|---|
| BCL2 | P10415 | IBA + IDA (PMID:9219694) |
| BAX | Q07812 | IBA + IDA (PMID:9219694) |
| BAK1 | Q16611 | IBA + IDA (PMID:22006182) |
| BCL2L1 (Bcl-xL) | Q07817 | IBA (+ bilayer data PMID:9002522) |

Multiple family members carry **direct experimental (IDA)** channel-activity annotations.
The GO_Central ancestral (IBA) inference on BCL2 therefore rests on real descendant
experimental evidence, not paralog guesswork. This directly addresses the seed's
instruction not to reject ancestral assertions on family-role-exclusivity or absent-assay
grounds alone: the ancestral node placement is legitimate.

---

## Mechanistic Model / Interpretation

BCL2 is fundamentally an **antiapoptotic guardian** whose resting conformation sequesters
proapoptotic BH3-containing effectors and inhibits other channels. The seed hypothesis's
two "conditional capacities" are best understood as *state-switches* away from this
default:

```
                         ┌─────────────────────────────────────────────┐
                         │        NATIVE / RESTING BCL2 (core)          │
                         │  • Antiapoptotic (GO:0043066, IDA-rich)      │
                         │  • Blocks Bax channel @ physiological pH     │
                         │  • Inhibits IP3R Ca2+ channel (GO:0016248)   │
                         └───────────────┬─────────────────────────────┘
                                         │
              ┌──────────────────────────┼──────────────────────────┐
              │ CASPASE-3 @ Asp34         │ Nur77/TR3 binding         │ Acidic pH +
              │ (proteolysis)             │ (conformational)          │ acidic lipid
              ▼                           ▼                           ▼
   ┌────────────────────┐    ┌──────────────────────────┐   ┌────────────────────┐
   │ C-TERMINAL FRAGMENT│    │ BH3-EXPOSED FULL-LENGTH  │   │ INTRINSIC PORE     │
   │ Bax-like killer    │    │ protector→killer         │   │ (CF release)       │
   │ needs BH3 + TM     │    │ mito-targets Nur77       │   │ in-vitro only      │
   │ PMID:9395403       │    │ PMID:14980220            │   │ PMID:9219694/9144199│
   │ → GO:0043065 (+apop)│   │ → GO:0043065 (+apop)     │   │ → GO:0015267       │
   └────────────────────┘    └──────────────────────────┘   └────────────────────┘
```

**Which gene product performs the proapoptotic step?** Two answers, both correct in their
context: (i) the **C-terminal caspase-3 fragment** (a distinct proteoform), and (ii) the
**Nur77-complexed, BH3-exposed full-length conformer**. Neither is the resting
antiapoptotic species. This is the key qualifier for any positive-regulation-of-apoptosis
annotation.

**Is transport evidence intrinsic pore formation or channel regulation?** Both are
experimentally documented, but they operate under different conditions. Intrinsic
cation-selective channel formation is demonstrable for purified BCL2 in bilayers
(pH 7.4), and pore/permeabilization activity appears only at acidic pH on acidic lipids.
Under physiological conditions the dominant, biologically relevant transport role is
**negative regulation** of other channels (Bax, IP3R). The MF term GO:0015267 (channel
activity) is thus valid as an intrinsic capacity, but the physiological narrative is
better captured by the co-existing GO:0016248 (channel inhibitor activity).

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID:9395403](https://pubmed.ncbi.nlm.nih.gov/9395403/) | Direct assay + mutant phenotype | Supports (qualifies) | Proapoptotic after caspase cleavage | Caspase-3 cleaves BCL2 at Asp34; C-terminal fragment triggers death via BH3+TM; cleavage-resistant mutant is more protective | Human, in vitro + cell lines (Fas, IL-3 withdrawal, Sindbis) | High; activity is of the *fragment*, not intact protein |
| [PMID:14980220](https://pubmed.ncbi.nlm.nih.gov/14980220/) | Direct assay + interaction | Supports (qualifies) | Proapoptotic via conformational conversion | Nur77/TR3 binds N-loop, exposes BH3, converts protector→killer | Human cancer cells, mitochondria | High; requires Nur77 partner/context |
| [PMID:9144199](https://pubmed.ncbi.nlm.nih.gov/9144199/) | Direct assay (biophysical) | Supports (qualifies) | Intrinsic channel formation | Purified BCL2 forms cation-selective channels (18 pS); Δh5,6 mutant inactive | In vitro planar bilayer, pH 7.4 | High for capacity; physiological relevance uncertain |
| [PMID:9219694](https://pubmed.ncbi.nlm.nih.gov/9219694/) | Direct assay | Qualifies / competing | Pore vs channel regulation | BCL2 permeabilizes only at acidic pH; at physiological pH it BLOCKS Bax channel | In vitro vesicles/bilayers | High; establishes regulatory dominance |
| [PMID:9002522](https://pubmed.ncbi.nlm.nih.gov/9002522/) | Structural/evolutionary (paralog) | Supports | Ancestral channel capacity of fold | Bcl-xL forms ion-conducting channel like bacterial toxins | In vitro | High; paralog, not BCL2 directly |
| [PMID:15263017](https://pubmed.ncbi.nlm.nih.gov/15263017/) | Direct assay + interaction | Competing (regulatory) | Transport = channel regulation | BCL2 reduces IP3R open probability; forms complex with IP3R | WEHI7.2 T cells, bilayers | High; supports inhibitory role |
| UniProt P10415/P10417 | Computational (sequence) | Supports (inference) | Mouse conservation | Asp34 motif + h5–h6 core conserved human↔mouse | Sequence | Moderate; conservation ≠ function |
| QuickGO P10415 | Review/database | Orientation | GO term existence | Both MF channel + BP positive-apoptosis terms already annotated | Database | High for annotation status |
| QuickGO family (BAX/BAK1/BCL2L1) | Review/database | Supports | Descendant support for IBA | Family members carry direct IDA channel annotations | Database | High; validates ancestral node |

---

## GO Curation Implications

**Lead action (requires curator verification): RETAIN both terms with conditional/
non-core qualifiers; do NOT remove on family-role-exclusivity grounds.**

1. **GO:0015267 channel activity (MF)** — *Retain.* It carries both an IBA (ancestral,
   descendant-supported by BAX/BAK1 IDA) and a direct IDA (PMID:9219694). The intrinsic
   channel-forming capacity is directly demonstrated for purified BCL2 (PMID:9144199).
   Curators may consider adding a note that permeabilization is pH/lipid-restricted and
   that the physiologically dominant transport role is inhibitory.

2. **GO:0016248 channel inhibitor activity (MF)** — *Retain and emphasize.* This
   IDA-supported term (PMID:9219694, plus IP3R inhibition PMID:15263017) better captures
   the physiological transport-related function than intrinsic pore formation.

3. **GO:0043065 positive regulation of apoptotic process (BP)** — *Retain, but currently
   under-supported at the primary level.* It has an IBA and an NAS (PMID:14634621) but no
   IDA. **Candidate IDA additions:** PMID:9395403 (caspase fragment) and PMID:14980220
   (Nur77 conversion), each with a proteoform/context qualifier. Because the proapoptotic
   activity belongs to a distinct proteoform (caspase fragment) or an induced conformer,
   the annotation should carry qualifiers noting it is not the resting-state activity.

4. **GO:0055085 transmembrane transport (BP)** — currently IEA only; the direct evidence
   points more to *channel activity* (MF) and *regulation of transport* than to BCL2
   itself being a bulk transporter. Treat as non-core / low priority.

5. **Do not** reject the ancestral (IBA) assertions using the argument that BCL2 is
   "an antiapoptotic protein so it cannot be proapoptotic or a channel." The seed's
   caution is correct: the PAINT node is descendant-supported, and both capacities have
   direct BCL2 primary evidence.

The predominant native role — **GO:0043066 negative regulation of apoptotic process** —
remains the core function and is far more strongly (IDA/IMP) supported; nothing here
challenges that.

---

## Mechanistic Scope

The immediate molecular functions being tested are: (i) BH3-mediated proapoptotic
effector activity exposed by cleavage or conformational change, and (ii) intrinsic ion
channel/pore formation in lipid membranes. Both are *direct gene-product activities*, but
each is gated by a specific molecular state (proteolytic fragment, partner-induced
conformer, or acidic membrane environment). These must be separated from downstream
phenotypes such as mitochondrial outer membrane permeabilization, cytochrome c release,
and cell death, which are pathway consequences rather than the immediate BCL2 activity.
The proapoptotic annotation is a *state-specific molecular capacity*, not a constitutive
function or a mere loss-of-function phenotype.

---

## Conflicts and Alternatives

- **Proteoform confusion.** The proapoptotic activity (PMID:9395403) belongs to the
  C-terminal caspase fragment, not intact BCL2. A naive annotation of "BCL2 promotes
  apoptosis" without a proteoform qualifier would misrepresent the resting protein.
- **pH/lipid artifact risk.** BCL2's intrinsic pore/permeabilization activity
  (PMID:9219694) is seen only at acidic pH on acidic lipids — a non-physiological
  condition. The channel-activity MF term is defensible as an intrinsic capacity, but the
  *transport* interpretation should not be over-read as a physiological permeabilizing
  role. At physiological pH BCL2 is a channel *inhibitor*.
- **Paralog attribution.** Some channel evidence (PMID:9002522) is for Bcl-xL, and Bax
  channel activity (PMID:9219694, PMID:20885444) is the object BCL2 *inhibits*. Curators
  should ensure channel annotations reflect BCL2's own IDA (PMID:9219694/9144199), not
  paralog carry-over.
- **Species extension.** Mouse Bcl2 conservation of the Asp34 motif and h5–h6 core is
  sequence-level only; species-specific functional primary support was not established
  here.

---

## Limitations and Knowledge Gaps

1. **Physiological relevance of intrinsic pore.** *Checked:* PMID:9144199, 9219694.
   *Gap:* whether BCL2's intrinsic channel/pore ever forms under physiological pH in
   vivo, versus being an in-vitro property. *Resolve:* single-molecule/electrophysiology
   in native mitochondrial membranes at physiological pH; conditional pore-dead h5–h6
   mutants.

2. **In vivo contribution of the caspase fragment.** *Checked:* PMID:9395403 (cells +
   in vitro). *Gap:* quantitative contribution of the Asp34 fragment to apoptosis
   amplification in normal physiology. *Resolve:* Asp34→Ala knock-in mouse phenotyping.

3. **Generality of Nur77 conversion.** *Checked:* PMID:14980220. *Gap:* whether BH3
   exposure by Nur77 occurs broadly or only in specific cell types/stimuli. *Resolve:*
   conformation-specific (BH3-exposed) antibodies across tissues.

4. **Mouse functional support.** *Checked:* sequence conservation only. *Gap:* no mouse
   primary functional assays reviewed. *Resolve:* mouse Bcl2 caspase-cleavage and
   Nur77-conversion assays.

5. **PAINT node placement details.** *Checked:* QuickGO IBA/IDA distribution across
   family. *Gap:* the exact ancestral node and loss/divergence pattern were inferred from
   annotation presence, not from direct inspection of the PANTHER tree. *Resolve:*
   consult the PANTHER family tree / PAINT annotations directly.

---

## Discriminating Tests

1. **Proteoform-resolved apoptosis assay.** Compare intact BCL2, Asp34→Ala
   (cleavage-resistant), and the isolated C-terminal fragment for pro- vs antiapoptotic
   output — cleanly separates fragment activity from resting activity.
2. **pH-controlled bilayer electrophysiology** of purified BCL2 vs Δh5,6 mutant at pH
   7.4 vs 5.0 — distinguishes intrinsic channel from acidic-only permeabilization.
3. **Bax/IP3R co-reconstitution** at physiological pH — tests whether BCL2's net transport
   effect is inhibitory (channel regulation) rather than pore-forming.
4. **Nur77 knockdown + BH3-exposure antibody** — tests conformational-conversion route in
   cells.
5. **PANTHER tree inspection** to confirm ancestral node placement and descendant IDA
   distribution formally.

---

## Curation Leads (require curator verification)

- **Candidate IDA additions to GO:0043065 (positive regulation of apoptotic process):**
  - [PMID:9395403](https://pubmed.ncbi.nlm.nih.gov/9395403/) — snippet to verify: *"The
    carboxyl-terminal Bcl-2 cleavage product triggered cell death and accelerated Sindbis
    virus-induced apoptosis, which was dependent on the BH3 homology and transmembrane
    domains of Bcl-2."* Add with **proteoform qualifier** (caspase C-terminal fragment).
  - [PMID:14980220](https://pubmed.ncbi.nlm.nih.gov/14980220/) — snippet to verify:
    *"Nur77 binding induces a Bcl-2 conformational change that exposes its BH3 domain,
    resulting in conversion of Bcl-2 from a protector to a killer."* Add with
    **conformational/context qualifier** (Nur77/TR3-dependent).
- **Retain GO:0015267 channel activity (MF)** — IBA is descendant-supported (BAX/BAK1
  IDA); direct IDA PMID:9219694. Optionally annotate pH/lipid restriction.
- **Emphasize GO:0016248 channel inhibitor activity (MF)** as the physiologically dominant
  transport-related function (PMID:9219694; support from PMID:15263017 for IP3R).
- **Do NOT remove** the ancestral channel/proapoptotic assertions on family-role-
  exclusivity grounds.
- **Suggested curator questions:** Should proapoptotic BP terms carry proteoform qualifiers
  in this schema? Should transmembrane transport (GO:0055085, IEA) be deprecated in favor
  of the more specific channel-activity/inhibitor terms?
- **Suggested experiments:** Asp34→Ala knock-in; physiological-pH bilayer recordings; PANTHER
  tree inspection for node placement.

---

## Conclusion

The hypothesis is **partially supported**. Both the conditional proapoptotic capacity and
the channel/pore capacity of human BCL2 are backed by direct primary experimental data,
but each is a **conditional, non-core capacity** distinct from BCL2's predominant native
antiapoptotic function. The proapoptotic step is performed by either the caspase-3
C-terminal fragment (PMID:9395403) or the Nur77-converted, BH3-exposed conformer
(PMID:14980220) — not the resting protein. Intrinsic channel formation is real
(PMID:9144199) but permeabilization is acidic-pH/lipid-restricted; at physiological pH the
dominant transport role is channel inhibition (PMID:9219694, PMID:15263017). The
corresponding GO terms already exist, are descendant-supported for the ancestral IBA, and
should be **retained with conditional/non-core qualifiers** rather than removed. The two
direct proapoptotic papers are strong candidate IDA additions, and mouse extension is
supported only at the sequence level.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)