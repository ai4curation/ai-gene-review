---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T20:05:04.280148'
end_time: '2026-09-20T20:28:22.876935'
duration_seconds: 1398.6
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: CDH23
  gene_symbol: CDH23
  uniprot_accession: Q9H251
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: catenin-neuronal-and-calcium-process-scope
  hypothesis_text: 'Human CDH23 has beta-catenin binding or catenin-complex membership,
    participates in neuron projection development, or contributes to calcium transport/regulation.
    Assess these independently using PTN008601603 and PTN004649584 placement and primary
    full texts. Distinguish absence of classical cytoplasmic binding motifs from negative
    binding assays; compare PMID:12485990 with beta-catenin colocalization in PMID:30747484
    and PMID:22413011. Inspect the experimental GOA reference PMID:17234811 for the
    calcium processes: a tip-link mechanical contribution can participate in ion transport
    without being an ion pump. Test evidence for alternative isoforms/tissues retaining
    ancestral functions and distinguish conditional negative data from global loss.
    Homophilic adhesion and migration have separate positive primary support; the
    question is not premised on hair-cell exclusivity.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/CDH23/CDH23-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human CDH23 has beta-catenin binding or catenin-complex\
    \ membership, participates in neuron\n  projection development, or contributes\
    \ to calcium transport/regulation. Assess these independently using\n  PTN008601603\
    \ and PTN004649584 placement and primary full texts. Distinguish absence of classical\
    \ cytoplasmic\n  binding motifs from negative binding assays; compare PMID:12485990\
    \ with beta-catenin colocalization\n  in PMID:30747484 and PMID:22413011. Inspect\
    \ the experimental GOA reference PMID:17234811 for the calcium\n  processes: a\
    \ tip-link mechanical contribution can participate in ion transport without being\
    \ an ion\n  pump. Test evidence for alternative isoforms/tissues retaining ancestral\
    \ functions and distinguish conditional\n  negative data from global loss. Homophilic\
    \ adhesion and migration have separate positive primary support;\n  the question\
    \ is not premised on hair-cell exclusivity.'\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
- **Gene directory:** CDH23
- **Gene symbol:** CDH23
- **UniProt accession:** Q9H251

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** catenin-neuronal-and-calcium-process-scope
- **Source file:** genes/human/CDH23/CDH23-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human CDH23 has beta-catenin binding or catenin-complex membership, participates in neuron projection development, or contributes to calcium transport/regulation. Assess these independently using PTN008601603 and PTN004649584 placement and primary full texts. Distinguish absence of classical cytoplasmic binding motifs from negative binding assays; compare PMID:12485990 with beta-catenin colocalization in PMID:30747484 and PMID:22413011. Inspect the experimental GOA reference PMID:17234811 for the calcium processes: a tip-link mechanical contribution can participate in ion transport without being an ion pump. Test evidence for alternative isoforms/tissues retaining ancestral functions and distinguish conditional negative data from global loss. Homophilic adhesion and migration have separate positive primary support; the question is not premised on hair-cell exclusivity.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human CDH23 has beta-catenin binding or catenin-complex membership, participates in neuron
  projection development, or contributes to calcium transport/regulation. Assess these independently using
  PTN008601603 and PTN004649584 placement and primary full texts. Distinguish absence of classical cytoplasmic
  binding motifs from negative binding assays; compare PMID:12485990 with beta-catenin colocalization
  in PMID:30747484 and PMID:22413011. Inspect the experimental GOA reference PMID:17234811 for the calcium
  processes: a tip-link mechanical contribution can participate in ion transport without being an ion
  pump. Test evidence for alternative isoforms/tissues retaining ancestral functions and distinguish conditional
  negative data from global loss. Homophilic adhesion and migration have separate positive primary support;
  the question is not premised on hair-cell exclusivity.'
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

# CDH23 (Q9H251) — Catenin Binding, Neuronal Projection, and Calcium Process Scope

**Focus type:** function_assignment
**Hypothesis slug:** catenin-neuronal-and-calcium-process-scope
**Gene:** CDH23 / Cadherin-related 23 (human, Homo sapiens, NCBITaxon:9606)
**UniProt:** Q9H251

---

## Summary

This report evaluates a three-part function-assignment hypothesis for human
CDH23: that the gene product (i) binds beta-catenin or belongs to a catenin
complex, (ii) participates in neuron projection development, or (iii) contributes
to calcium transport/regulation. The seed asked that each claim be assessed
independently using the phylogenetic placement of nodes PTN008601603 and
PTN004649584 plus primary full texts, and that colocalization be distinguished
from binding and mechanical ion participation from ion-pump activity. The
investigation combined UniProt/QuickGO annotation provenance, PANTHER/Pfam domain
architecture, and targeted full-text mining of the primary literature.

**Overall verdict: weakly supported / over-annotated.** The catenin claim is
effectively refuted as a direct function: beta-catenin binding (GO:0008013) and
catenin complex (GO:0016342) are both **IBA (phylogenetic) inferences** on
Q9H251, propagated through ancestral node **PTN008601603**, whose experimental
seeds are *exclusively classical catenin-binding cadherins* (CDH1/E-cadherin,
CDH2/N-cadherin, CDH5/VE-cadherin, CDH24, CDH26) — never CDH23. CDH23 is an
**atypical cadherin** lacking the classical cytoplasmic catenin-binding domain
(Pfam PF01049); its tail instead anchors to the actin cytoskeleton through
**harmonin PDZ interactions**, described in primary work as "a novel anchorage
mode of the cadherins to the actin cytoskeleton" (PMID:12485990). The seed's
proposed rescue via beta-catenin colocalization fails: PMID:30747484 contains
zero mentions of catenin, and in PMID:22413011 beta-catenin is only an
adherens-junction *marker*, not a demonstrated CDH23 partner.

The neuronal claim is weakly supported at best (IBA-only via node PTN004649584;
neural expression present but no loss-of-function projection phenotype in
zebrafish, PMID:22977299). The calcium claim is partially supported but
mis-scoped: extracellular EC-domain **calcium ion binding** (GO:0005509) is
defensible and mechanistically central, but **calcium ion transport**
(GO:0006816) and **regulation of cytosolic calcium** (GO:0051480) over-interpret a
*digenic PMCA2-pump modifier* study (PMID:17234811) in which CDH23 appears only
as a genetic modifier. Importantly, none of this challenges CDH23's genuine core
functions — calcium-dependent homophilic adhesion and tip-link
mechanotransduction for hearing and vision — which have independent positive
primary support and are not the subject of this hypothesis.

---

## Key Findings

### F001 — CDH23 anchors to F-actin via harmonin PDZ, not via catenins (argues against beta-catenin binding)

UniProt Q9H251 annotates beta-catenin binding (GO:0008013) and catenin complex
(GO:0016342), but **both are IBA:GO_Central** phylogenetic inferences with **no
experimental (IDA/IPI) support** on CDH23 itself. The primary literature
documents a fundamentally *different*, catenin-independent cytoplasmic anchoring
mechanism. The CDH23 cytoplasmic domain binds **harmonin** through PDZ- and
N-domain interactions (PMID:12407180: "Two PDZ domains in harmonin interact with
two complementary binding surfaces in the CDH23 cytoplasmic domain";
PMID:19297620), and harmonin-b anchors CDH23 to the stereocilia actin core in a
manner explicitly framed as **"a novel anchorage mode of the cadherins to the
actin cytoskeleton"** (PMID:12485990). A later structural study confirms the
interaction "involves the harmonin Nter-PDZ1 supramodule, but not the C-terminal
PDZ-binding motif of cadherin-23" (PMID:20639393). CDH23 is classified in PANTHER
**PTHR24026 "FAT atypical cadherin-related"**, not the classical cadherin clade
that carries the ancestral catenin-binding domain. Together these show CDH23 uses
a harmonin-based, non-catenin actin linkage — undercutting any claim of direct
beta-catenin binding or catenin-complex membership.

### F002 — CDH23 "calcium ion transport" derives from a digenic PMCA2 modifier study, not from pump/transporter activity

On Q9H251, calcium ion transport (GO:0006816) and regulation of cytosolic
calcium ion concentration (GO:0051480) are annotated **IMP:DFLAT**; calcium ion
binding (GO:0005509) is **IEA:InterPro**. The experimental GOA reference for the
calcium processes, **PMID:17234811** (Ficarella 2007), is fundamentally a study
of the **PMCA2 (ATP2B2) plasma-membrane calcium pump**. CDH23 appears in that
work only as a **genetic modifier** — a CDH23 T1999S substitution that
"accentuated hearing loss in a previously described human family with a PMCA2
mutation." The paper itself identifies the true Ca²⁺ machinery: "Ca²⁺ enters the
stereocilia of hair cells through mechanoelectrical transduction channels opened
by the deflection of the hair bundle and is exported back to endolymph by an
unusual splicing isoform (w/a) of plasma-membrane calcium-pump isoform 2
(PMCA2)." Neither the entry (MET channel) nor the export (PMCA2) route is CDH23.
CDH23 forms the **upper tip-link** that mechanically gates the MET channel. Thus
a *transport* or *regulation-of-cytosolic-calcium* annotation over-reads CDH23's
mechanical, adhesive role. Extracellular **calcium ion binding** by the EC
repeats, by contrast, is a genuine and central property of the protein — the seed
correctly notes that "a tip-link mechanical contribution can participate in ion
transport without being an ion pump," but that participation is captured by
mechanotransduction and calcium binding, not by a transport annotation.

### F003 — "Neuron projection development" is an IBA inference; neural expression exists but loss-of-function shows no projection defect

Neuron projection development (GO:0031175) on Q9H251 is **IBA:GO_Central only**,
with no experimental support on CDH23. Critically, CDH23's characterized
"projections" are **stereocilia** — actin-based apical microvillar protrusions of
epithelial hair cells — **not neuron projections**; the hair-bundle role is
already captured by more accurate terms (sensory perception of sound GO:0007605
IMP:MGI; stereocilium GO:0032420 ISS). In zebrafish, *cdh23* is expressed in CNS
nuclei and "a small subset of GABAergic amacrine cells," yet *cdh23*-mutant
larvae show "no detectable morphological retinal defects or degeneration" and a
normal optokinetic response (PMID:22977299). This is a textbook case of
**expression without a demonstrated loss-of-function phenotype**: neural
expression alone does not justify a neuron-projection-development function.

### F004 — Catenin IBA is seeded only by classical cadherins at node PTN008601603 — paralog over-propagation

QuickGO annotation records for Q9H251 show GO:0008013 (beta-catenin binding) and
GO:0016342 (catenin complex) are both IBA (GO_REF:0000033, GO_Central) whose
with/from experimental seeds are **exclusively classical type-I/II cadherins**:
CDH1/E-cadherin (P12830, MGI:88354), CDH2/N-cadherin (P19022), CDH5/VE-cadherin
(P33151), CDH24 (Q86UP0), CDH26 (Q8IXH8), plus zebrafish *cdh* genes —
propagated through ancestral node **PTN008601603**, exactly the node named in the
seed hypothesis. **None of the seed genes is CDH23**, and no CDH23-specific
experimental catenin annotation exists. Classical cadherins bind beta-catenin
through a conserved cytoplasmic catenin-binding domain (**Pfam PF01049**) that is
**absent** from CDH23 (Q9H251 lists only PF00028 cadherin repeats plus the
CDH23-specific domain; its tail binds harmonin PDZ instead). The neuron
projection development IBA (GO:0031175) propagates from a *separate* node
**PTN004649584**, seeded by fly/mouse/zebrafish cadherins (Drosophila *fat*
FBgn0262018, MGI:1890219, ZDB-GENE-040513-7), again none of them CDH23. This is
the mechanistic signature of **paralog over-annotation**: an ancestral function
correctly inferred for the classical-cadherin subfamily is carried over onto an
atypical paralog that has diverged away from the seeding function. This finding
directly addresses the seed's request to assess PTN008601603 and PTN004649584
placement.

### F005 — The seed's "beta-catenin colocalization" evidence does not demonstrate binding

Full-text mining (Europe PMC, open access) directly tests the seed's proposed
supporting evidence. **PMID:30747484** (Sannigrahi 2019, PMC6487693) contains
**zero occurrences of "catenin"** in abstract or full text — the seed's
attribution of beta-catenin colocalization to this paper is unsupported.
**PMID:22413011** (Apostolopoulou & Ligon 2012, PMC3296689) mentions β-catenin
12 times, but **exclusively as an adherens-junction marker**: the authors "used
an antibody to β-catenin to identify sites of possible cell-cell adhesion,"
scored contacts for β-catenin recruitment (found at 82.1% of heterotypic
contacts), and *then* scored those β-catenin⁺ sites for cadherin-23 labeling.
This establishes that CDH23 **spatially colocalizes** with β-catenin-marked
adhesion sites; it does **not** provide a co-IP, pulldown, or two-hybrid
demonstration of a CDH23–β-catenin molecular interaction. The paper's actually
demonstrated CDH23 function is **heterotypic cell-cell adhesion** between breast
cancer epithelial cells and fibroblasts — a genuine adhesion role, not a catenin
binding role. This resolves the seed's request to "compare PMID:12485990 with
beta-catenin colocalization in PMID:30747484 and PMID:22413011": one paper does
not mention catenin, and the other uses it only as a marker.

---

## Mechanistic Model / Interpretation

The three sub-claims collapse onto a single coherent picture: **CDH23 is an
atypical, tip-link cadherin whose cytoplasmic and calcium biology diverges from
the classical cadherin–catenin paradigm that seeds its questionable
annotations.**

```
   CLASSICAL CADHERINS (E-/N-/VE-cadherin)          CDH23 (atypical, tip-link)
   ─────────────────────────────────────           ──────────────────────────
   EC repeats  (Ca2+-dependent adhesion)            27 EC repeats (Ca2+ binding,
        │                                                homophilic + heterophilic
        │  transmembrane                                 handshake w/ PCDH15)
        ▼                                                     │  transmembrane
   Cytoplasmic tail WITH catenin-binding                     ▼
   domain (Pfam PF01049)                             Cytoplasmic tail, NO PF01049
        │                                                     │
        ▼                                                     ▼
   β-catenin ── α-catenin ── ACTIN                    HARMONIN (PDZ + N-domain)
   (catenin complex, GO:0016342)                             │
                                                             ▼
                                                       ACTIN core of stereocilium
                                                    "novel anchorage mode" (12485990)

   IBA node PTN008601603  ──(β-catenin binding, catenin complex)──►  carried onto CDH23
        seeds: CDH1, CDH2, CDH5, CDH24, CDH26  (NO CDH23)             = PARALOG OVER-PROP.
```

**Catenin axis.** The catenin-binding/complex annotations are pure phylogenetic
carry-over. The seeding node contains only classical cadherins that possess the
PF01049 catenin-binding domain; CDH23 lacks that domain and uses a
harmonin-based, structurally characterized alternative. The seed hypothesis
asked to "distinguish absence of classical cytoplasmic binding motifs from
negative binding assays." The honest answer is that both the motif is absent
*and* the positive cytoplasmic partner is a different protein (harmonin) — so
there is no residual positive evidence for beta-catenin binding to rescue.

**Calcium axis.** CDH23 is genuinely a **calcium-binding** protein: its EC
repeats require Ca²⁺ for rigidity and adhesive function, and Ca²⁺ occupancy at
inter-repeat linkers governs tip-link mechanics. That is a *molecular-function*
(binding) and *mechanotransduction* role — not *ion transport*. The "calcium ion
transport / regulation of cytosolic calcium" terms conflate the mechanical
gating of a downstream channel (and a digenic interaction with a real pump,
PMCA2) with CDH23 itself being a transporter. The correct causal chain is:

```
sound → hair-bundle deflection → CDH23–PCDH15 tip link tension →
        MET channel opens → Ca2+ (and K+) influx → PMCA2 exports Ca2+
                                   ▲                      ▲
                             (not CDH23)             (not CDH23)
```

CDH23's node in this chain is the **mechanical linker/gate**, which is why
"sensory perception of sound" (GO:0007605) is the well-supported BP term.

**Neuronal axis.** CDH23's "projections" are epithelial stereocilia. Neural
expression is real but phenotypically silent in the available loss-of-function
model. The neuron-projection-development term is a second, independent instance
of IBA carry-over (from node PTN004649584) and should be treated as
non-core/unsupported for the human gene.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:12485990](https://pubmed.ncbi.nlm.nih.gov/12485990/) | Localization / interaction | Refutes catenin | CDH23 cytoplasmic anchoring mechanism | "novel anchorage mode of the cadherins to the actin cytoskeleton" via harmonin, not catenin | Mouse/human hair cell bundle | High; establishes non-catenin actin linkage |
| [PMID:12407180](https://pubmed.ncbi.nlm.nih.gov/12407180/) | Interaction (direct) | Refutes catenin | CDH23 cytoplasmic partner identity | "Two PDZ domains in harmonin interact with two complementary binding surfaces in the CDH23 cytoplasmic domain" | Biochemical | High; identifies harmonin, not β-catenin |
| [PMID:20639393](https://pubmed.ncbi.nlm.nih.gov/20639393/) | Structural | Refutes catenin | Nature of CDH23 tail interaction | Uses harmonin Nter-PDZ1 supramodule; ternary Usher complex | Structural/biochemical | High |
| QuickGO / UniProt Q9H251 (GO_REF:0000033, node PTN008601603) | Computational / database | Refutes (provenance) | Are catenin terms experimental? | GO:0008013 & GO:0016342 are IBA; seeds = CDH1/2/5/24/26, no CDH23 | GO_Central pipeline | High; direct provenance of over-annotation |
| [PMID:17234811](https://pubmed.ncbi.nlm.nih.gov/17234811/) | Mutant phenotype / genetics | Qualifies calcium | Basis of Ca²⁺-transport annotation | CDH23 is a digenic *modifier* of a PMCA2 pump; Ca²⁺ moves via MET channel + PMCA2 | Human family + functional assay | High; shows CDH23 ≠ transporter |
| [PMID:21786191](https://pubmed.ncbi.nlm.nih.gov/21786191/) | Review-level synthesis | Qualifies calcium | Ca²⁺ role of CDH23 vs PMCA2 | CDH23 is a "Ca²⁺ binding protein" forming tip links; PMCA2 does the export | Inner ear physiology review | Moderate (review); consistent with binding-not-transport |
| [PMID:22977299](https://pubmed.ncbi.nlm.nih.gov/22977299/) | Mutant phenotype / expression | Refutes neuronal | Neuron-projection-development function | Neural expression present, but mutant shows "no detectable morphological retinal defects or degeneration" | Zebrafish brain/retina | Moderate-High; expression ≠ phenotype |
| [PMID:22413011](https://pubmed.ncbi.nlm.nih.gov/22413011/) | Localization / adhesion | Refutes catenin-binding; supports adhesion | Is β-catenin a CDH23 binding partner? | β-catenin used only as junction marker; CDH23 mediates heterotypic adhesion | Breast cancer epithelial + fibroblast | High; no molecular interaction shown |
| [PMID:30747484](https://pubmed.ncbi.nlm.nih.gov/30747484/) | Full-text mining | Refutes (seed premise) | Does paper show β-catenin colocalization? | Zero "catenin" occurrences; paper is about aggregation/migration suppression | HEK293T + cancer cells | High; seed attribution unsupported |
| [PMID:27349180](https://pubmed.ncbi.nlm.nih.gov/27349180/) | Interaction (direct) | Qualifies | CDH23-C cytoplasmic partners | CDH23-C binds CAMSAP3/Marshalin near the harmonin-binding region | Organ of Corti / in vitro | Moderate; further non-catenin cytoplasmic biology |
| [PMID:23467356](https://pubmed.ncbi.nlm.nih.gov/23467356/) | Mutant phenotype / structural | Supports core function | Tip-link handshake integrity | CDH23 EC1–EC2 "handshake" with PCDH15; disruption abolishes mechanotransduction | Mouse inner ear | High; supports true core role |

---

## GO Curation Implications

These are **leads requiring curator verification**, organized by the three
sub-claims.

| GO term | ID | Aspect | Current evidence | Recommended action |
|---|---|---|---|---|
| beta-catenin binding | GO:0008013 | MF | IBA only; seeds are classical cadherins; PF01049 absent in CDH23 | **Remove / do NOT accept** (paralog IBA carry-over) |
| catenin complex | GO:0016342 | CC | IBA only; same node PTN008601603 | **Remove / do NOT accept**; CDH23 CC is stereocilium tip-link, not catenin complex |
| neuron projection development | GO:0031175 | BP | IBA only (node PTN004649584); no LoF phenotype | **Remove / treat as non-core**; prefer stereocilium/sensory-perception terms |
| calcium ion transport | GO:0006816 | BP | IMP:DFLAT from digenic PMCA2 modifier study | **Remove or generalize**; CDH23 gates MET channel, is not a transporter |
| regulation of cytosolic calcium ion concentration | GO:0051480 | BP | IMP:DFLAT, same reference | **Remove / demote to non-core** |
| calcium ion binding | GO:0005509 | MF | IEA:InterPro; central to EC-repeat function | **Retain** — defensible and informative |
| sensory perception of sound | GO:0007605 | BP | IMP:MGI (experimental) | **Retain** — well supported core BP |
| stereocilium | GO:0032420 | CC | ISS | **Retain** — accurate location |
| cell-cell adhesion (homophilic/calcium-dependent) | — | BP/MF | Positive primary support (PMID:22413011, PMID:30747484, PMID:23467356) | **Retain** — this is core |

The recommended replacement for the catenin/neuronal/transport annotations is
**not** "protein binding" (uninformative). The informative, supported alternatives
already exist: **calcium ion binding** (MF), **stereocilium** / tip-link (CC),
**sensory perception of sound** (BP), and **calcium-dependent cell-cell
adhesion** (BP). The cytoplasmic interaction that a curator *could* positively
annotate — if seeking a real partner — is **harmonin/USH1C binding** (supported
by PMID:12407180, PMID:19297620, PMID:20639393), not beta-catenin.

---

## Mechanistic Scope

The immediate molecular functions being tested are: (a) a protein–protein
*binding* activity toward beta-catenin, (b) a *developmental process* (neuron
projection development), and (c) an *ion-transport/regulation* activity.

- **Direct gene-product activity that is supported:** extracellular
  calcium-dependent homophilic and heterophilic adhesion (EC-repeat mediated),
  calcium ion binding, and mechanical tip-link formation with PCDH15 that gates
  the MET channel (PMID:23467356). Cytoplasmic tail binding to harmonin/USH1C and
  CAMSAP3 (PMID:12407180, PMID:19297620, PMID:20639393, PMID:27349180).
- **Downstream phenotypes / consequences (not direct MF of CDH23):** Ca²⁺ influx
  and cytosolic Ca²⁺ changes are consequences of channel gating, not CDH23
  transport. Hearing/vision loss is a disease manifestation of adhesion/tip-link
  failure. The digenic hearing-loss modification with PMCA2 (PMID:17234811) is a
  genetic-interaction effect, not evidence of CDH23 pump activity.
- **Effects inferred only from loss of function or expression:** the neuronal
  claim rests on expression plus phylogeny; the single available LoF model shows
  no neuronal defect (PMID:22977299).

---

## Conflicts and Alternatives

1. **Paralog confusion (primary alternative explanation).** The catenin and
   neuronal terms are best explained not as CDH23 biology but as **IBA
   over-propagation from classical cadherins** through nodes PTN008601603 and
   PTN004649584. This is corroborated by domain architecture: CDH23 lacks
   PF01049. This is the dominant, well-supported alternative to the seed
   hypothesis.

2. **Colocalization ≠ interaction.** The seed treats spatial colocalization with
   β-catenin-marked junctions (PMID:22413011) as evidence of catenin membership.
   The full text shows β-catenin is only a *marker*; no binding assay exists, and
   the other cited paper (PMID:30747484) does not mention catenin at all.

3. **Digenic modifier ≠ transporter.** The calcium-transport annotation stems
   from a study whose subject is the PMCA2 pump; CDH23's contribution is genetic
   modification of a pump phenotype (PMID:17234811). An alternative, defensible
   framing is EC-repeat **calcium binding**, which the transport term wrongly
   promotes to transport activity.

4. **Isoform/tissue caveat (partially addresses the seed's request).** The seed
   asks whether alternative isoforms/tissues retain ancestral functions. CDH23
   has multiple isoforms (e.g., CDH23-C binds CAMSAP3/Marshalin, PMID:27349180;
   excretory isoforms modulate adhesion, PMID:30747484) and broad tissue
   expression (kidney, muscle, testis, heart). However, none of these isoform- or
   tissue-specific data document beta-catenin binding, neuron projection
   development, or calcium transport; they document *more* non-catenin cytoplasmic
   partnerships and adhesion biology. So the isoform argument, while legitimate to
   raise, does not rescue the seed claims with current evidence.

5. **Stereocilia vs neuron projections.** A genuine terminological conflict:
   CDH23's protrusions are epithelial stereocilia, not neurites. The
   neuron-projection term likely reflects this category error compounded by IBA.

---

## Limitations and Knowledge Gaps

- **No exhaustive interaction screen consulted.** We relied on curated UniProt/
  QuickGO annotations, targeted full-text mining, and the provided literature. A
  systematic published *negative* binding assay (e.g., CDH23 tail vs β-catenin
  co-IP) is not in the record; the argument rests on *absence of the motif +
  presence of an alternative partner*, which is strong but not equivalent to a
  published negative assay. **Resolution:** a direct co-IP / ITC of the CDH23
  cytoplasmic domain against β-catenin.

- **Isoform coverage is incomplete.** CDH23 has many splice isoforms; we
  documented harmonin- and CAMSAP3-binding cytoplasmic behaviors but did not
  survey every isoform's tail for a cryptic catenin-binding capacity.
  **Resolution:** isoform-resolved domain analysis and pulldowns.

- **Neuronal function relies on a single zebrafish LoF model.** PMID:22977299
  reports no retinal phenotype, but a mammalian CNS-specific CDH23 knockout with
  detailed neurite/synapse morphometry has not been examined here. Absence of a
  reported phenotype is not proof of no function. **Resolution:** conditional
  neuronal *Cdh23* knockout with axon/dendrite morphometry.

- **Calcium binding stoichiometry not quantified here.** We accept GO:0005509 on
  InterPro/structural grounds but did not compute EC-linker Ca²⁺ occupancy from
  structure. **Resolution:** structural/biophysical Ca²⁺-binding measurement (not
  needed to reject *transport*, which is already refuted mechanistically).

- **QuickGO records were read at a point in time.** GO_Central annotations can be
  updated; a curator should re-verify current IBA seeds for GO:0008013,
  GO:0016342, and GO:0031175 on Q9H251.

---

## Discriminating Tests

1. **Direct CDH23 tail vs β-catenin binding assay** (co-IP, GST-pulldown, or ITC
   using the CDH23 cytoplasmic domain). A clean negative would convert
   "no-motif + alternative-partner" into a published negative binding result and
   fully close the catenin question.

2. **Domain-swap / motif search across CDH23 isoforms** for any PF01049-like
   catenin-binding module. Positive would reopen the isoform-rescue argument;
   negative confirms domain loss.

3. **Conditional neuronal *Cdh23* knockout** (mouse) with quantitative
   neurite/axon-guidance morphometry and synapse counts, to test neuron
   projection development directly rather than by expression inference.

4. **Ca²⁺-flux electrophysiology** in hair cells separating CDH23's mechanical
   gating role from any putative transport: CDH23 mutation should alter MET-channel
   *gating* (tension) without conferring intrinsic ion-transport activity.

5. **Re-audit of GO_Central IBA seeds** for the three terms on Q9H251, confirming
   nodes PTN008601603 / PTN004649584 and the absence of a CDH23 experimental seed.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

**Candidate action changes (leads requiring curator verification):**

- **Do not accept** beta-catenin binding (GO:0008013) and catenin complex
  (GO:0016342) for CDH23. Provenance = IBA over-propagation from classical
  cadherins (node PTN008601603); domain PF01049 is absent; the real cytoplasmic
  partner is harmonin.
- **Do not accept / demote** neuron projection development (GO:0031175) to
  non-core. Provenance = IBA (node PTN004649584); LoF model shows no neuronal
  phenotype (PMID:22977299).
- **Remove or generalize** calcium ion transport (GO:0006816) and regulation of
  cytosolic calcium (GO:0051480). These over-read a digenic PMCA2-pump modifier
  study (PMID:17234811).
- **Retain** calcium ion binding (GO:0005509), stereocilium (GO:0032420),
  sensory perception of sound (GO:0007605), and calcium-dependent cell-cell
  adhesion as the informative, supported terms.
- **Consider adding** a positively supported cytoplasmic MF: **harmonin/USH1C
  binding** (PMID:12407180, PMID:19297620, PMID:20639393) in place of the
  unsupported catenin term.

**Candidate references with exact snippets to verify:**

- PMID:12485990 — "thereby identifying a novel anchorage mode of the cadherins to
  the actin cytoskeleton."
- PMID:12407180 — "Two PDZ domains in harmonin interact with two complementary
  binding surfaces in the CDH23 cytoplasmic domain."
- PMID:17234811 — "which accentuated hearing loss in a previously described human
  family with a PMCA2 mutation"; "Ca²⁺ enters the stereocilia ... through
  mechanoelectrical transduction channels ... and is exported back to endolymph
  by an unusual splicing isoform (w/a) of ... PMCA2."
- PMID:22977299 — "revealed no detectable morphological retinal defects or
  degeneration"; "cdh23 is expressed by a small subset of GABAergic amacrine
  cells."
- PMID:22413011 — "cadherin-23 mediates heterotypic cell-cell adhesion between
  breast cancer epithelial cells and fibroblasts" (β-catenin used as junction
  marker only).

**Suggested curator questions:**

- Is there any CDH23-specific experimental (IDA/IPI) annotation for GO:0008013 or
  GO:0016342? (Expected: no.)
- Do current GO_Central seeds at PTN008601603 include CDH23? (Expected: no.)
- Should the review explicitly flag stereocilia vs neuron projections to prevent
  recurring category error?

---

## Bottom Line

For human CDH23 (Q9H251), the seed hypothesis's three claims are **weakly
supported to refuted** as direct gene-product functions. The catenin binding /
complex terms are paralog IBA carry-over from classical cadherins and are
contradicted by CDH23's domain architecture (no PF01049) and its harmonin-based
actin anchorage; the neuron-projection term is IBA-only with a null LoF
phenotype; and the calcium-transport/regulation terms over-interpret a digenic
PMCA2 modifier study. Only **calcium ion binding** survives as a defensible
molecular-function annotation, alongside CDH23's genuine, independently supported
core roles in calcium-dependent homophilic adhesion and tip-link
mechanotransduction for hearing and vision.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)