---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T17:59:36.041218'
end_time: '2026-09-20T18:12:49.195988'
duration_seconds: 793.16
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: BAIAP2L2
  gene_symbol: BAIAP2L2
  uniprot_accession: Q6UXY1
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0005654
  hypothesis_text: Human BAIAP2L2/Pinkbar localizes to the nucleoplasm (GO:0005654).
    Assess target-specific and phylogenetic evidence, distinguish it from BAIAP2 and
    BAIAP2L1, and consider transient/context-dependent localization. Documented membrane
    functions do not by themselves establish exclusive localization. The existing
    epithelial-function investigation does not settle this claim.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/BAIAP2L2/BAIAP2L2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human BAIAP2L2/Pinkbar localizes to the nucleoplasm\
    \ (GO:0005654). Assess target-specific and\n  phylogenetic evidence, distinguish\
    \ it from BAIAP2 and BAIAP2L1, and consider transient/context-dependent\n  localization.\
    \ Documented membrane functions do not by themselves establish exclusive localization.\
    \ The\n  existing epithelial-function investigation does not settle this claim.\n\
    focus_type: function_assignment\ncontext: []\nreference_id: []"
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
- **Gene directory:** BAIAP2L2
- **Gene symbol:** BAIAP2L2
- **UniProt accession:** Q6UXY1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0005654
- **Source file:** genes/human/BAIAP2L2/BAIAP2L2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human BAIAP2L2/Pinkbar localizes to the nucleoplasm (GO:0005654). Assess target-specific and phylogenetic evidence, distinguish it from BAIAP2 and BAIAP2L1, and consider transient/context-dependent localization. Documented membrane functions do not by themselves establish exclusive localization. The existing epithelial-function investigation does not settle this claim.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human BAIAP2L2/Pinkbar localizes to the nucleoplasm (GO:0005654). Assess target-specific and
  phylogenetic evidence, distinguish it from BAIAP2 and BAIAP2L1, and consider transient/context-dependent
  localization. Documented membrane functions do not by themselves establish exclusive localization. The
  existing epithelial-function investigation does not settle this claim.
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

# BAIAP2L2/Pinkbar Nucleoplasm (GO:0005654) Hypothesis — Deep Research Report

**Gene:** BAIAP2L2 (Pinkbar) · **Organism:** *Homo sapiens* (NCBITaxon:9606) · **UniProt:** Q6UXY1 · **Ensembl:** ENSG00000128298
**Focus type:** function_assignment · **Hypothesis slug:** function-hypothesis-go-0005654
**Source file:** `genes/human/BAIAP2L2/BAIAP2L2-ai-review.yaml` (free-text selector)

---

## Summary

The seed hypothesis proposes that human **BAIAP2L2/Pinkbar localizes to the
nucleoplasm (GO:0005654)** and asks whether transient, context-dependent, or
paralog-specific evidence might support a nuclear pool that documented membrane
functions do not exclude. After three iterations examining primary literature, GO/GOA
term-specific records, UniProt, the Human Protein Atlas, paralog annotations, and the
protein sequence itself, the verdict is clear: **the nucleoplasm claim is refuted /
over-annotated.** There is no experimental, database, or sequence-based source for a
nuclear localization at any level of confidence.

Every direct localization study places BAIAP2L2 at **membrane and actin-based
protrusion compartments.** The founding characterization localized Pinkbar to
Rab13-positive vesicles and the plasma membrane at intercellular junctions of intestinal
epithelial cells ([PMID: 21743456](https://pubmed.ncbi.nlm.nih.gov/21743456/)). A wholly
independent body of inner-ear work places it at the tips of shorter-row transducing
stereocilia in cochlear hair cells, where it is a "row-2 complex" component required for
mechanotransduction ([PMID: 33151556](https://pubmed.ncbi.nlm.nih.gov/33151556/),
[PMID: 34346063](https://pubmed.ncbi.nlm.nih.gov/34346063/),
[PMID: 35044843](https://pubmed.ncbi.nlm.nih.gov/35044843/),
[PMID: 39093051](https://pubmed.ncbi.nlm.nih.gov/39093051/)). This is exactly what its
I-BAR (IMD) + SH3 membrane-curvature architecture predicts, and it is the functional
opposite of a soluble nucleoplasmic protein.

Critically, the hypothesis's proposed escape routes all fail when tested directly.
Term-specific QuickGO queries return **zero** annotations for GO:0005654 (nucleoplasm),
GO:0005634 (nucleus), and GO:0005730 (nucleolus); **neither paralog** (BAIAP2, BAIAP2L1)
carries any nuclear annotation; the Human Protein Atlas antibody yields **no** subcellular
call at any reliability level; and the 529-aa sequence has **no** classical NLS or basic
patch capable of driving nuclear import. The recommended curation lead is therefore to
**not assign GO:0005654** and to flag any existing nucleoplasm annotation for **removal**,
pending curator verification of its (undocumented) source.

---

## Key Findings

### F001 — Nucleoplasm localization is unsupported by all primary literature and current database records

Direct localization experiments across two entirely different tissue systems converge on
membrane compartments and never report a nucleus. In the founding paper, Pinkbar is
**"specifically expressed in intestinal epithelial cells, where it localizes to
Rab13-positive vesicles and to the plasma membrane at intercellular junctions"**
([PMID: 21743456](https://pubmed.ncbi.nlm.nih.gov/21743456/)). These three
compartments — plasma membrane, cell junction, cytoplasmic vesicle membrane — are exactly
what UniProt curates for Q6UXY1, each with experimental evidence code ECO:0000269 tracing
to this paper.

An independent inner-ear literature reaches the identical conclusion in a different cell
type: **"the I-BAR protein BAIAP2L2 … localizes to the tips of the shorter transducing
stereocilia in both inner and outer hair cells"**
([PMID: 33151556](https://pubmed.ncbi.nlm.nih.gov/33151556/)). Stereocilia tips are
apical, actin-based membrane protrusions — again membrane/cytoskeletal, not nuclear.

At the annotation level, QuickGO returns **8 cellular_component annotations** for
BAIAP2L2: plasma membrane (IBA/IEA), cytosol (TAS), vesicle membrane (IDA, PMID:21743456),
cytoplasmic vesicle membrane (IEA), cell–cell contact zone (IDA, PMID:21743456), anchoring
junction (IEA), and clathrin complex (IDA, dictyBase, PMID:21401524). **None** is
GO:0005654 or any nuclear term. The two paralogs behave the same way — **BAIAP2 (Q9UQB8)
has 42 CC annotations and BAIAP2L1 (Q9UHR4) has 11 CC annotations, and neither carries a
single nuclear annotation.** Targeted PubMed searches for "BAIAP2L2 nuclear/nucleus" and
"I-BAR nuclear localization" returned no relevant papers. The negative result is
convergent across two experimental systems and three databases.

### F002 — No GO term-specific, HPA immunofluorescence, or proteomic source supports a nuclear annotation

To exclude a hidden or low-visibility source, each candidate nuclear term was queried
directly. QuickGO term-specific queries for Q6UXY1 return **numberOfHits = 0** for
**GO:0005654 (nucleoplasm)**, **GO:0005634 (nucleus)**, and **GO:0005730 (nucleolus)**.
Across all 17 GO annotations spanning all three aspects, **no term contains the string
"nucle"** — including no NOT-qualified nuclear annotations.

The Human Protein Atlas has a BAIAP2L2 antibody (**HPA003043**), but its Cell Atlas
Subcellular-location, main-location, and additional-location fields are **all null** —
BAIAP2L2 has no HPA immunofluorescence localization call at any reliability level. HPA
therefore provides neither a nuclear call nor any competing call. In sum, none of the
three standard curation sources (GO/GOA, UniProt, HPA) offers direct or predicted
nucleoplasm evidence, and the seed claim has **no identifiable source document** to trace.

### F003 — The sequence carries no nuclear-localization-signal signature

A nuclear pool would require a mechanism of import. Sequence analysis of the 529-aa
Q6UXY1 protein found none. The **global basic-residue (K+R) fraction is 0.123**, and the
two annotated intrinsically disordered regions (residues 221–327 and 403–510) — the most
plausible NLS locations — have K+R fractions of only **0.121 and 0.111**, i.e., they are
*not* basic-enriched relative to the whole protein. This is the reverse of the basic-patch
enrichment characteristic of NLS-bearing nuclear proteins. The **longest contiguous K/R
run is 3 residues**, below the 4–6 residue basic core of a classical monopartite NLS, and
**no strict bipartite NLS motif** (KR-x(9–12)-[KR]{3}) is present anywhere in the
sequence. There is thus no sequence-based route for nuclear import, removing the last
plausible rationale for a computational/predicted nuclear annotation.

---

## Mechanistic Model / Interpretation

BAIAP2L2's architecture and every functional study converge on one coherent model: it is
a **membrane-deforming I-BAR/IMD-domain protein** that senses and shapes plasma-membrane
curvature at actin-based protrusions, working within multiprotein complexes at the
cytoplasm–membrane interface. It has neither a role at, nor a documented route into, the
nucleoplasm.

```
   BAIAP2L2 / Pinkbar (Q6UXY1, 529 aa)
   ┌───────────────┬──────────────────────────┬────────────┬───────────────────────┐
   │  I-BAR (IMD)  │  disordered 221–327       │ SH3-region │  disordered 403–510    │
   │ membrane      │  (K+R 0.121, no NLS)      │ partner    │  (K+R 0.111, no NLS)   │
   │ curvature     │                           │ binding    │                        │
   └───────┬───────┴──────────────────────────┴─────┬──────┴────────────────────────┘
           │                                          │
           ▼                                          ▼
   Binds/senses negative                     EPS8L2, TWF2, CAPZB2, CIB2,
   membrane curvature; makes                 EPS8, MYO15A, Rho-GTPase Rif
   planar membrane sheets                            │
           │                                          │
           ▼                                          ▼
   ┌──────────────────────────────┐   ┌──────────────────────────────┐
   │ Intestinal epithelium:        │   │ Cochlear hair cells:          │
   │ Rab13+ vesicles + plasma      │   │ tips of shorter (row-2)       │
   │ membrane at cell junctions    │   │ transducing stereocilia       │
   │ (PMID:21743456)               │   │ (PMID:33151556, 34346063)     │
   └──────────────────────────────┘   └──────────────────────────────┘

   NUCLEUS / NUCLEOPLASM (GO:0005654):
       ✗ 0 GO annotations   ✗ no HPA IF call   ✗ no NLS   ✗ no literature report
```

The two documented contexts — intestinal junctions and stereocilia tips — are different
tissues that share the **same molecular logic**: membrane-curvature sensing/generation
coupled to actin regulators. In hair cells, BAIAP2L2 is a bona fide "row-2 complex"
component whose stereocilia-tip retention is Ca²⁺- and mechanotransduction-channel
dependent, and it binds EPS8L2, TWF2, CAPZB2 and CIB2
([PMID: 34346063](https://pubmed.ncbi.nlm.nih.gov/34346063/),
[PMID: 35044843](https://pubmed.ncbi.nlm.nih.gov/35044843/)). None of these partners is
nuclear. The interesting subtlety the seed hypothesis raises — that localization *is*
context-dependent — is genuinely true (PMID:35044843 shows conditional, Ca²⁺-dependent
targeting), but the conditional target is a **membrane protrusion tip, not the nucleus.**
The immediate molecular function under test is a **CC (localization) assignment**, and
every attempt to reconcile it with a nucleoplasm pool fails.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports / Refutes | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 21743456](https://pubmed.ncbi.nlm.nih.gov/21743456/) | Direct localization (IDA), structural | **Refutes** nucleoplasm | Where does Pinkbar localize? | Plasma membrane at intercellular junctions + Rab13⁺ vesicles; flat I-BAR makes planar membrane sheets | Human intestinal epithelial cells; in vitro structure | High; founding paper; no nuclear signal |
| [PMID: 33151556](https://pubmed.ncbi.nlm.nih.gov/33151556/) | Direct localization, mutant phenotype | **Refutes** nucleoplasm | Subcellular site of function | Tips of shorter transducing stereocilia; loss → stereocilia degeneration, deafness | Mouse cochlear hair cells | High; independent, in vivo |
| [PMID: 34346063](https://pubmed.ncbi.nlm.nih.gov/34346063/) | Localization + interaction + KO phenotype | **Refutes** nucleoplasm | Complex/compartment | Row-2 stereocilia-tip complex; binds EPS8L2, TWF2, CAPZB2, CIB2; KO → hearing loss | Mouse cochlea | High; multiple orthogonal assays |
| [PMID: 35044843](https://pubmed.ncbi.nlm.nih.gov/35044843/) | Localization, mechanism | **Qualifies** (transient/context) | Ca²⁺/channel dependence | Tip retention is transduction-Ca²⁺-dependent — localization IS context-dependent, but to stereocilia tips, not nucleus | Mouse cochlea + cultured cells | High; conditional membrane targeting |
| [PMID: 39093051](https://pubmed.ncbi.nlm.nih.gov/39093051/) | Localization / paralog comparison | **Refutes**; paralog discrimination | BAIAP2L2 vs BAIAP2L1 sites | BAIAP2L1 → tallest-row tips (Ca²⁺-independent); BAIAP2L2 → row-2 tips (Ca²⁺-dependent) — both membrane protrusions | Mouse hair cells | High; directly distinguishes paralogs |
| [PMID: 27278019](https://pubmed.ncbi.nlm.nih.gov/27278019/) | Interaction | **Qualifies** (cytoskeletal/membrane) | Signalling partners | Pinkbar interacts with Rho-GTPase Rif; I-BAR proteins modulate cell-surface morphology | N1E-115 neuroblastoma | Medium; reinforces membrane role |
| UniProt Q6UXY1 (SUBCELL) | Database (curated from PMID:21743456) | **Refutes** | Curated locations | Cell membrane; Cell junction; Cytoplasmic vesicle membrane. **No nucleoplasm.** | Human | High (curated) |
| QuickGO CC (8 terms) | Database | **Refutes** | Existing GO CC set | plasma membrane, cytosol, vesicle/cytoplasmic vesicle membrane, cell-cell contact zone, anchoring junction, clathrin complex. **No GO:0005654.** | Human | High |
| Human Protein Atlas (HPA003043) | Database (localization) | Neutral/absent | Independent IF localization | Antibody exists but **no subcellular call at any reliability** (all fields null) | Human cell lines | Medium; absence of call, not a negative call |
| QuickGO term-specific (this run) | Database | **Refutes** | Any nuclear annotation? | numberOfHits = **0** for GO:0005654/0005634/0005730; 0/17 total annotations contain "nucle" | Human, all evidence codes/qualifiers | High; definitive negative |
| Paralog QuickGO (BAIAP2, BAIAP2L1) | Database / evolutionary | **Refutes** (paralog check) | Are paralogs nuclear? | 42 and 11 CC annotations; zero nuclear | Q9UQB8, Q9UHR4 | High; family-wide absence |
| Sequence/NLS scan (this run) | Computational | **Refutes** (weakly) | Sequence import signal? | No mono/bipartite NLS; disordered regions not basic-enriched (K+R 0.11–0.12); longest K/R run = 3 | Q6UXY1, 529 aa | Medium-high; NLS prediction heuristic |

---

## GO Decision Table (computed provenance, this run)

| GO_ID | Term | Aspect | Evidence source | Key basis | Curation action | Verdict |
|---|---|---|---|---|---|---|
| GO:0005654 | nucleoplasm | CC | Seed hypothesis (no DB/lit source) | 0 GO annotations; no HPA call; no lit; no NLS; disordered regions not basic-enriched (11–12% K+R) | **DO NOT ADD / REMOVE if present** | **Refuted / over-annotation candidate** |
| GO:0005886 | plasma membrane | CC | IBA GO_Central; IEA; lit PMID:21743456 | Direct IDA to membrane at junctions | RETAIN | Supported |
| GO:0044291 | cell-cell contact zone | CC | IDA PMID:21743456 | Localizes at intercellular junctions | RETAIN | Supported |
| GO:0030659 | cytoplasmic vesicle membrane | CC | IEA UniProt; IDA vesicle membrane | Rab13⁺ vesicles | RETAIN | Supported |
| GO:0032420 | stereocilium | CC | Multiple IDA/KO (PMID:33151556, 34346063) | Stereocilia-tip row-2 complex | CONSIDER ADD (hair cell) | Supported (mouse) |
| GO:0071439 | clathrin complex | CC | IDA dictyBase PMID:21401524 | *Dictyostelium* projection | REVIEW (cross-organism carry-over) | Weak/uncertain for human |

---

## GO Curation Implications

- **Lead (requires curator verification):** Do **not** assign GO:0005654 (nucleoplasm, CC)
  to BAIAP2L2/Q6UXY1. If a nucleoplasm annotation exists in the working review, flag it for
  **removal** or downgrade to "not supported / source unverified."
- **Aspect:** The hypothesis concerns a **CC** term. The evidence supports no nuclear CC
  term (GO:0005654, GO:0005634, GO:0005730). It should **not** be generalized to
  GO:0005634 (nucleus) — generalizing an unsourced specific term to its parent merely
  propagates the same unsupported claim.
- **Retain / support instead:** The well-sourced CC terms are membrane/junction/vesicle
  (GO:0005886, GO:0044291, GO:0030659; PMID:21743456) and, for hair-cell context,
  stereocilium/stereocilium tip (GO:0032420; PMID:33151556, 34346063) — all more
  informative than any generic location.
- **Review-worthy carry-over:** GO:0071439 (clathrin complex, IDA from dictyBase) deserves
  scrutiny as a cross-organism projection that may not reflect human Pinkbar.
- Nucleoplasm is neither "too broad" nor "too narrow" — it is **unsupported**, so the
  qualifier question does not apply.

---

## Mechanistic Scope

The immediate molecular function is a **subcellular localization (CC) assignment**, not a
catalytic or process claim. The direct gene-product activity supported by evidence is
**membrane-curvature sensing/generation via the I-BAR (IMD) domain**, coupled to actin
regulators through the SH3 and disordered regions. This stabilizes membrane–cytoskeleton
interfaces: planar epithelial junction membranes and the membrane at shorter-row
stereocilia tips (the row-2 complex maintaining mechanotransduction).

The downstream *phenotypes* — stereocilia maintenance, mechanotransduction current, and
hearing (from knockout mice) — are consequences of that membrane/actin activity in
cytoplasmic/plasma-membrane compartments. A nucleoplasm role would imply a distinct,
undocumented function (chromatin/transcription or nuclear transport) with no supporting
assay, interaction, or phenotype. The nucleoplasm claim is therefore **not** a downstream
phenotype that could be reconciled with the membrane model — it is a separate localization
assertion with no molecular route (no NLS, no importin partner, no reported nuclear pool)
and cannot be rescued as a "context-specific" facet of the documented function.

---

## Conflicts and Alternatives

The hypothesis anticipates several ways a nuclear call could still be correct; each was
tested:

1. **Paralog confusion (BAIAP2 vs BAIAP2L1 vs BAIAP2L2).** The most likely *source* of an
   erroneous annotation, but it does not rescue the claim: **all three** family members
   lack nuclear annotations (42, 11, 8 CC annotations respectively; zero nuclear). The
   hair-cell literature explicitly distinguishes the paralogs by localization
   ([PMID: 39093051](https://pubmed.ncbi.nlm.nih.gov/39093051/)), and all are
   membrane/actin-associated.
2. **Transient/context-dependent nuclear pool.** Localization *is* context-dependent
   (PMID:35044843), but the conditional target is a stereocilium tip, not the nucleus.
   No IF call, proteomic nuclear-fraction hit, or stimulus-induced translocation is
   reported, and no NLS enables import.
3. **Isoform-specific localization.** No BAIAP2L2 isoform has been reported nuclear; the
   disordered regions where an isoform-specific NLS might sit are not basic-enriched.
4. **Database carry-over / unsourced prediction.** The most parsimonious explanation: a
   spurious or predictor-derived nucleoplasm term (deep-learning localization tools often
   default disordered, mildly basic proteins to "nucleoplasm"), a historical/withdrawn HPA
   IF call, or antibody cross-reactivity — none of which is curatable evidence. This is
   precisely the artifact class this review is designed to catch.

No evidence was found that *conflicts* with the refutation; the conflict runs the other
way — the hypothesis conflicts with the entire evidence base.

---

## Limitations and Knowledge Gaps

1. **Negative evidence is not proof of absence.** The strongest statements are "zero
   annotations," "null HPA fields," and "no NLS." These make a nuclear pool unlikely and
   unsourced but cannot formally exclude a minor/transient nucleoplasmic fraction no study
   has looked for. *Checked:* GO term-specific queries, UniProt, HPA, NLS scan. *Why it
   matters:* the claim should be recorded as "unsupported/no source," not "experimentally
   disproven." *Resolution:* targeted fractionation or validated-antibody IF.
2. **Provenance of the seed nucleoplasm term is unidentified.** No document asserting
   nucleoplasm could be traced. A curator should inspect the review YAML's cited
   source/prediction log; its absence from all curation sources itself argues against
   curation.
3. **HPA has no call at all** rather than an explicit non-nuclear call — the antibody
   (HPA003043) may simply lack a validated Cell Atlas entry.
4. **NLS prediction is heuristic.** Absence of a classical NLS does not exclude
   non-classical or piggyback import, though no partner-mediated route is documented.
5. **No wet-lab data were generated;** this is a literature/database/sequence assessment
   across three iterations. Computed tables are embedded here rather than saved as separate
   files because the sandbox working directory was read-only.

---

## Discriminating Tests / Proposed Follow-up Actions

- **Trace the annotation source (highest priority, lowest cost).** Search the working
  review and its evidence chain for the origin of GO:0005654 (evidence code, reference,
  assigned-by). If it is IEA/prediction or paralog carry-over with no experimental
  backing, the case is closed.
- **Validated-antibody IF / endogenous-tag live imaging** with nuclear (DAPI/lamin) and
  membrane (junction/stereocilia) markers in intestinal epithelial and cochlear hair
  cells — the single most decisive test.
- **Subcellular fractionation** (nuclear vs membrane/cytosolic) with immunoblot to detect
  any nuclear pool.
- **APEX2/BioID proximity labeling** — a nuclear interactome would be required to support
  any nucleoplasm role; membrane/actin partners are expected instead.
- **Cross-check cell-map proteomic localization datasets** for nuclear-neighbor
  enrichment; none is expected.
- **Deletion of disordered basic patches** to test any predicted nuclear import — expected
  null.

---

## Curation Leads (require curator verification)

- **Action:** Reject/remove GO:0005654 (nucleoplasm) for BAIAP2L2; document as
  unsupported/likely computational over-annotation.
- **Replacement/retained CC terms:** GO:0005886 (plasma membrane), GO:0044291 (cell-cell
  contact zone), GO:0030659 (cytoplasmic vesicle membrane), and — for hair-cell context —
  GO:0032420 (stereocilium)/stereocilium tip.
- **Candidate references to verify (exact snippets):**
  - [PMID: 21743456](https://pubmed.ncbi.nlm.nih.gov/21743456/) — *"Pinkbar, is
    specifically expressed in intestinal epithelial cells, where it localizes to
    Rab13-positive vesicles and to the plasma membrane at intercellular junctions."*
  - [PMID: 33151556](https://pubmed.ncbi.nlm.nih.gov/33151556/) — *"the I-BAR protein
    BAIAP2L2, which localizes to the tips of the shorter transducing stereocilia in both
    inner and outer hair cells."*
- **Suggested question for submitter:** What is the primary source of the nucleoplasm
  assignment (predictor name/version, HPA release, or reference)?
- **Suggested experiment:** Validated-antibody IF + subcellular fractionation in intestinal
  epithelial and cochlear hair cells.

---

## Final Answer

The hypothesis that human BAIAP2L2/Pinkbar localizes to the nucleoplasm (GO:0005654) is
**refuted / over-annotated**. All direct localization data place it at the plasma
membrane, intercellular junctions, Rab13⁺ vesicles (PMID:21743456), and cochlear
stereocilia tips (PMID:33151556, 34346063); term-specific QuickGO returns zero nuclear
annotations for BAIAP2L2 and both paralogs; the Human Protein Atlas yields no subcellular
call; and the sequence has no NLS or basic-patch signature — so there is no experimental,
database, or sequence basis for a nucleoplasm annotation, which should not be assigned
and, if present, should be flagged for removal pending source verification.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)