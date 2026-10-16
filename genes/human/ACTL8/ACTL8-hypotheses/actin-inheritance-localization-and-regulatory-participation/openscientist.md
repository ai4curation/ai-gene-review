---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:10:11.216739'
end_time: '2026-09-21T04:29:55.962770'
duration_seconds: 1184.75
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ACTL8
  gene_symbol: ACTL8
  uniprot_accession: Q9H568
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: actin-inheritance-localization-and-regulatory-participation
  hypothesis_text: 'Human ACTL8 (Q9H568) inherits actin-family functions: synapse
    GO:0045202, axon GO:0030424, structural constituent of postsynaptic actin cytoskeleton
    GO:0098973, actin filament GO:0005884, axonogenesis GO:0007409, membrane GO:0016020,
    protein kinase binding GO:0019901, NuA4 histone acetyltransferase complex GO:0035267,
    and cell motility GO:0048870. Evaluate each claim independently against literature,
    sequence/structure and the PANTHER PTHR11937 ancestral assertions PTN002631484,
    PTN002631586 and PTN007551913. Distinguish actual tree topology and ancestral-state
    evidence from pairwise similarity and from lists of human annotation recipients;
    neither donor number nor lack of a target experiment alone proves failure. Does
    any demonstrated divergence exclude noncanonical structural association, peripheral
    membrane binding or complex membership? Separately assess whether ACTL8 itself
    contributes to positive regulation of cell migration GO:0030335 and cell population
    proliferation GO:0008284, or whether tumour-cell perturbations are compatible
    with indirect pleiotropy. Check the 2026 Momordin Ic study PMID:41621692 as well
    as earlier knockdown studies and flag retracted PMID:32125225. Do not assume testis
    enrichment establishes absence in neurons or that regulatory participation follows
    from necessity alone.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/ACTL8/ACTL8-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human ACTL8 (Q9H568) inherits actin-family functions:\
    \ synapse GO:0045202, axon GO:0030424,\n  structural constituent of postsynaptic\
    \ actin cytoskeleton GO:0098973, actin filament GO:0005884, axonogenesis\n  GO:0007409,\
    \ membrane GO:0016020, protein kinase binding GO:0019901, NuA4 histone acetyltransferase\
    \ complex\n  GO:0035267, and cell motility GO:0048870. Evaluate each claim independently\
    \ against literature, sequence/structure\n  and the PANTHER PTHR11937 ancestral\
    \ assertions PTN002631484, PTN002631586 and PTN007551913. Distinguish\n  actual\
    \ tree topology and ancestral-state evidence from pairwise similarity and from\
    \ lists of human annotation\n  recipients; neither donor number nor lack of a\
    \ target experiment alone proves failure. Does any demonstrated\n  divergence\
    \ exclude noncanonical structural association, peripheral membrane binding or\
    \ complex membership?\n  Separately assess whether ACTL8 itself contributes to\
    \ positive regulation of cell migration GO:0030335\n  and cell population proliferation\
    \ GO:0008284, or whether tumour-cell perturbations are compatible with\n  indirect\
    \ pleiotropy. Check the 2026 Momordin Ic study PMID:41621692 as well as earlier\
    \ knockdown studies\n  and flag retracted PMID:32125225. Do not assume testis\
    \ enrichment establishes absence in neurons or\n  that regulatory participation\
    \ follows from necessity alone.'\nfocus_type: function_assignment\ncontext: []\n\
    reference_id: []"
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
citation_count: 8
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
- **Gene directory:** ACTL8
- **Gene symbol:** ACTL8
- **UniProt accession:** Q9H568

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** actin-inheritance-localization-and-regulatory-participation
- **Source file:** genes/human/ACTL8/ACTL8-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ACTL8 (Q9H568) inherits actin-family functions: synapse GO:0045202, axon GO:0030424, structural constituent of postsynaptic actin cytoskeleton GO:0098973, actin filament GO:0005884, axonogenesis GO:0007409, membrane GO:0016020, protein kinase binding GO:0019901, NuA4 histone acetyltransferase complex GO:0035267, and cell motility GO:0048870. Evaluate each claim independently against literature, sequence/structure and the PANTHER PTHR11937 ancestral assertions PTN002631484, PTN002631586 and PTN007551913. Distinguish actual tree topology and ancestral-state evidence from pairwise similarity and from lists of human annotation recipients; neither donor number nor lack of a target experiment alone proves failure. Does any demonstrated divergence exclude noncanonical structural association, peripheral membrane binding or complex membership? Separately assess whether ACTL8 itself contributes to positive regulation of cell migration GO:0030335 and cell population proliferation GO:0008284, or whether tumour-cell perturbations are compatible with indirect pleiotropy. Check the 2026 Momordin Ic study PMID:41621692 as well as earlier knockdown studies and flag retracted PMID:32125225. Do not assume testis enrichment establishes absence in neurons or that regulatory participation follows from necessity alone.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human ACTL8 (Q9H568) inherits actin-family functions: synapse GO:0045202, axon GO:0030424,
  structural constituent of postsynaptic actin cytoskeleton GO:0098973, actin filament GO:0005884, axonogenesis
  GO:0007409, membrane GO:0016020, protein kinase binding GO:0019901, NuA4 histone acetyltransferase complex
  GO:0035267, and cell motility GO:0048870. Evaluate each claim independently against literature, sequence/structure
  and the PANTHER PTHR11937 ancestral assertions PTN002631484, PTN002631586 and PTN007551913. Distinguish
  actual tree topology and ancestral-state evidence from pairwise similarity and from lists of human annotation
  recipients; neither donor number nor lack of a target experiment alone proves failure. Does any demonstrated
  divergence exclude noncanonical structural association, peripheral membrane binding or complex membership?
  Separately assess whether ACTL8 itself contributes to positive regulation of cell migration GO:0030335
  and cell population proliferation GO:0008284, or whether tumour-cell perturbations are compatible with
  indirect pleiotropy. Check the 2026 Momordin Ic study PMID:41621692 as well as earlier knockdown studies
  and flag retracted PMID:32125225. Do not assume testis enrichment establishes absence in neurons or
  that regulatory participation follows from necessity alone.'
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

# ACTL8 (Q9H568) — Actin-Inheritance, Localization, and Regulatory Participation

**Gene:** ACTL8 / Actin-like protein 8 · **Organism:** Homo sapiens (NCBITaxon:9606) · **UniProt:** Q9H568 · **PANTHER:** PTHR11937:SF208
**Focus type:** function_assignment
**Hypothesis slug:** actin-inheritance-localization-and-regulatory-participation
**Source:** genes/human/ACTL8/ACTL8-ai-review.yaml (free-text)

---

## Summary

**Executive judgment: OVER-ANNOTATED — refuted as a set of direct function assignments for the nine inherited actin-family GO terms; partially supported but indirect for the two migration/proliferation regulatory terms.**

The seed hypothesis proposes that human ACTL8 "inherits" nine actin-family Gene Ontology terms — synapse (GO:0045202), axon (GO:0030424), structural constituent of postsynaptic actin cytoskeleton (GO:0098973), actin filament (GO:0005884), axonogenesis (GO:0007409), membrane (GO:0016020), protein kinase binding (GO:0019901), the NuA4 histone acetyltransferase complex (GO:0035267), and cell motility (GO:0048870). The evidence gathered across this investigation indicates that **none of these nine terms is supported as a direct, ACTL8-specific molecular function, cellular location, or biological process.** Every one is present on the UniProt record only as an **IBA (Inferred from Biological Ancestor)** annotation propagated from GO_Central, and every one traces back to a single family-level PANTHER GO-slim (PTHR11937) that **self-contradictorily co-lists mutually exclusive roles** — the nuclear NuA4 chromatin-remodeling function of the ACTL6A paralog *and* the neuronal/synaptic/axonal functions of ACTL6B — attached indiscriminately to every family recipient including ACTL8. This is the signature of paralog over-annotation, not lineage-specific ancestral-state inheritance.

Independent sequence, structural-motif, and localization checks reinforce this verdict. ACTL8 is a divergent actin-related protein: it shares only ~33–41% identity with canonical actins and with the functionally characterized ARP paralogs, it **lacks the conserved actin C-terminal signature (PROSITE PS00432)** retained by β-actin and by the NuA4-associated ACTL6A/ACTL6B, and the Human Protein Atlas localizes it to the **cytosol only**, restricted to germ cells (testis/spermatogonia and oocytes) and **not detected in brain**. A cytosolic, germ-cell-restricted protein absent from neural tissue cannot support brain-specific CC terms (synapse, axon, postsynaptic actin cytoskeleton) or the nuclear NuA4 complex term as direct assignments.

The only experimentally grounded activities of ACTL8 are **positive regulation of cell migration (GO:0030335)** and **positive regulation of cell population proliferation (GO:0008284)**, seen consistently across cancer knockdown studies. However, these are **downstream, indirect, tumor-cell-context phenotypes routed through PI3K/AKT/mTOR–MYC signaling and glutamine metabolism** — no study demonstrates direct ACTL8 binding to a kinase, direct actin polymerization, or filament localization. They reflect pleiotropic regulatory participation, not a demonstrated core molecular mechanism. One frequently cited knockdown paper ([PMID:32125225](https://pubmed.ncbi.nlm.nih.gov/32125225/), endometrial cancer) is **retracted** and must be excluded. **Most important caveat:** absence of a direct experiment is not proof of absence, and the retained actin-like ATPase fold means a *noncanonical* structural or peripheral role cannot be formally excluded — but the burden of evidence for the high-information neuronal/NuA4/filament terms is unmet at their current specificity.

---

## Key Findings

### F001 — All nine seed actin-family GO terms are IBA (phylogenetically inferred), never experimental

A direct inspection of the UniProt Q9H568 record (retrieved 2026) shows that **every** seed term carries the evidence code **IBA:GO_Central**: GO:0045202 (synapse), GO:0030424 (axon), GO:0098973 (structural constituent of postsynaptic actin cytoskeleton), GO:0005884 (actin filament), GO:0016020 (membrane), GO:0019901 (protein kinase binding), GO:0035267 (NuA4 histone acetyltransferase complex), GO:0015629 (actin cytoskeleton), and GO:0005737 (cytoplasm). The two biological-process seed terms — cell motility (GO:0048870) and axonogenesis (GO:0007409) — are likewise IBA. The **only experimental annotation** on the record is GO:0030855 (epithelial cell differentiation), coded IEP. Even the subcellular-location statement "Cytoplasm, cytoskeleton" is ECO:0000250 (**by similarity**, i.e., inferred, not observed).

The curation implication is decisive: IBA is a computationally propagated evidence class — a hypothesis of function, not a demonstration. When every member of a set of contested terms shares the same non-experimental provenance and none is independently confirmed for the target protein, the set should be treated as low-confidence inference rather than as established gene-product function.

### F002 — ACTL8 is a divergent actin-family member, distant from the paralogs that actually carry NuA4/neuronal functions

Global Needleman–Wunsch alignments (percent identity over the longer sequence) place ACTL8 far from both canonical actin and the functionally annotated ARPs:

| Comparison | % identity |
|---|---|
| ACTL8 vs β-actin (ACTB) | 41.1% |
| ACTL8 vs γ-actin (ACTG1) | 41.3% |
| ACTL8 vs ACTL6A (BAF53a) | 33.8% |
| ACTL8 vs ACTL6B (BAF53b) | 33.3% |
| ACTL8 vs ACTL7A | 34.3% |
| ACTL8 vs ACTL9 | 39.9% |
| *ACTB vs ACTG1 (sanity check)* | *98.9%* |

ACTL8 (366 aa) retains the generic actin-like ATPase fold (Pfam PF00022, InterPro IPR004000, SUPFAM SSF53067 actin-like ATPase, Gene3D 3.90.640.10), which is why it clusters into PTHR11937 at all. But ~33% identity to ACTL6A/ACTL6B — the proteins that genuinely execute NuA4 chromatin remodeling and neuronal chromatin functions — is well within the twilight zone where fold conservation coexists with functional divergence. Fold membership justifies the family assignment; it does not justify transferring the specialized functions of distant paralogs. In sequence space ACTL8 clusters instead with the testis actin-related proteins (ACTL7A/ACTL9).

### F003 — The only experimental phenotypes are indirect tumor-cell proliferation/migration via PI3K/AKT/mTOR–MYC

Across independent cancer models, ACTL8 knockdown consistently reduces proliferation, migration, and invasion: lung adenocarcinoma ([PMID:31962007](https://pubmed.ncbi.nlm.nih.gov/31962007/), [PMID:35116946](https://pubmed.ncbi.nlm.nih.gov/35116946/)), head and neck squamous cell carcinoma ([PMID:30535476](https://pubmed.ncbi.nlm.nih.gov/30535476/)), oral squamous cell carcinoma ([PMID:35051678](https://pubmed.ncbi.nlm.nih.gov/35051678/)), triple-negative breast cancer ([PMID:33883901](https://pubmed.ncbi.nlm.nih.gov/33883901/)), gastric cancer ([PMID:39322809](https://pubmed.ncbi.nlm.nih.gov/39322809/)), and breast cancer via the 2026 Momordin Ic study ([PMID:41621692](https://pubmed.ncbi.nlm.nih.gov/41621692/)).

The **mechanism is uniformly signal-transductional, not cytoskeletal**: the effect is consistently routed through PI3K/AKT/mTOR signaling and downstream MYC — with SLC1A5/GLS1 glutamine-metabolism coupling in the Momordin Ic study, and CDK1/cyclin E1/cyclin B2/c-Myc cell-cycle proteins in the OSCC study. The TNBC study is the strongest on mechanism: a PI3K/AKT/mTOR activator (740Y-P) reverses and an inhibitor (Wortmannin) enhances the knockdown phenotype, showing the phenotype flows *through* the pathway. Critically, **no study demonstrates direct ACTL8 binding to a kinase, direct actin polymerization, or filament localization.** The migration/proliferation phenotypes are best modeled as indirect pleiotropy of an overexpressed cancer/testis antigen amplifying oncogenic signaling, not as evidence of a direct actin-based motility machine. The endometrial-cancer paper [PMID:32125225](https://pubmed.ncbi.nlm.nih.gov/32125225/) is **retracted** and is excluded.

### F004 — ACTL8 lacks the canonical actin C-terminal signature (PROSITE PS00432) retained by ACTB and the NuA4/neuronal ARPs

A regex scan of the PROSITE actin-family C-terminal signature ACTINS_2 (PS00432; pattern W-[IV]-[STAK]-[RK]-x-[DE]-Y-[DNE]-[DE]) gives a **match in β-actin (ACTB; "WISKQEYDE" — validating the pattern), in ACTL6A, and in ACTL6B**, but **no match in ACTL8**. ACTL8's C-terminus reads `...EWMSREEYGEHMRM`: the residue at signature position 2 is Met (not [IV]) and the residue after the tyrosine is Gly (not [DNE]). The canonical phosphate-loop motif D-N-G-S-G is present only in ACTB; all actin-related proteins tested (ACTL8, ACTL6A/B, and the testis ARP ACTL7A) diverge there. The absence of the conserved C-terminal signature — a motif retained precisely by the paralogs that do the NuA4 and neuronal jobs — is a concrete, position-level molecular argument that ACTL8 has diverged away from the canonical actin filament / actin-binding surface. (Signature loss is not proof of no structural role, but it removes support for canonical actin behavior.)

### F005 — The seed GO terms trace to a self-contradictory PANTHER family GO-slim, not to an ACTL8-lineage ancestral state

The PANTHER v19 geneinfo record places ACTL8 (Q9H568) in family **PTHR11937**, subfamily **PTHR11937:SF208**, protein class "actin and actin related protein" (PC00039). The family/subfamily GO-slim attached to ACTL8 contains **the entire seed term set simultaneously**: MF terms chromatin DNA binding (GO:0031490), protein kinase binding (GO:0019901), structural constituent of cytoskeleton / postsynaptic actin, and nucleosome binding; BP terms axonogenesis (GO:0007409), cell motility (GO:0048870), and chromatin remodeling (GO:0006338); and CC terms synapse (GO:0045202), axon (GO:0030424), NuA4 complex (GO:0035267), membrane (GO:0016020), actin filament (GO:0005884), and cytoplasm.

This co-listing is internally incoherent as a description of any single protein: the **nuclear NuA4 chromatin-remodeling role and the neuronal synaptic/axonal roles are mutually exclusive locations and processes** that belong to different specialized paralogs (nuclear ACTL6A vs. neuronal ACTL6B), not to one ancestral state that ACTL8 could have inherited whole. The seed's own caution — to distinguish tree topology and ancestral-state evidence from "lists of human annotation recipients" — is exactly the failure mode here: ACTL8 is a *recipient* of a pooled family GO-slim, not a demonstrated inheritor of a specific ancestral function.

### F006 — HPA: ACTL8 is germ-cell-restricted, cytosolic, and undetected in brain

The Human Protein Atlas (ENSG00000117148) reports RNA tissue specificity as **"Tissue enriched" in testis** (nTPM 6.8; cell-type enrichment "Testis – Spermatogonia"; tissue-expression Cluster 6 "Spermatogenesis"), with single-cell enrichment in **oocytes**. The subcellular main location is **"Cytosol" (only)**. RNA brain regional distribution is **"Not detected"**, pig brain is "Not detected", and single-nuclei brain shows only trace signal (fibroblast 1.1, mammillary body 1.2 nCPM ≈ noise). Protein tissue distribution is "Not detected" by antibody in normal tissues, consistent with a low-abundance cancer/testis antigen.

A protein that is cytosolic, confined to germ cells, and absent from brain **cannot directly occupy** synapse (GO:0045202), axon (GO:0030424), or postsynaptic actin cytoskeleton (GO:0098973) locations, and a strictly cytosolic localization argues against the nuclear NuA4 complex (GO:0035267) and against stable actin-filament (GO:0005884) incorporation. The seed's caveat that testis enrichment does not by itself prove absence in neurons is fair in principle — but here we have *direct* "not detected in brain" measurements, not merely an argument from testis enrichment.

---

## Mechanistic Model / Interpretation

The picture that emerges is one of **fold membership without functional inheritance**, plus **indirect signaling pleiotropy** in cancer.

```
                          PTHR11937  (actin + actin-related family)
                                │  pooled family GO-slim (self-contradictory)
        ┌───────────────┬───────┴────────┬────────────────┬───────────────┐
     ACTB/ACTG1      ACTL6A            ACTL6B           ACTL7A           ACTL8 (Q9H568)
   canonical actin  NuA4 / BAF        neuronal BAF     testis ARP       divergent testis ARP
   PS00432  ✔       PS00432  ✔        PS00432  ✔       PS00432 diverged  PS00432  ABSENT
   filament,        nuclear chromatin synapse/axon,    sperm/acrosome    cytosol only,
   motility         remodeling        chromatin                          germ-cell restricted,
                                                                          NOT in brain

   Seed hypothesis: transfer ALL of {synapse, axon, postsyn. actin, filament,
   axonogenesis, membrane, protein-kinase binding, NuA4, motility} onto ACTL8.
        └──> UNSUPPORTED: these are IBA carry-over from the pooled family slim;
             ACTL8 diverges in sequence (~33% id to ACTL6A/B), motif (no PS00432),
             and localization (cytosol / germ-cell / no-brain).

   What ACTL8 actually does (experimentally):
        overexpression in tumor cells ──> PI3K/AKT/mTOR ──> MYC ──> SLC1A5/GLS1
                                                                    (glutamine metab.)
                                          └──> proliferation ↑, migration ↑, invasion ↑
        = INDIRECT regulatory pleiotropy (GO:0030335 / GO:0008284),
          not a direct actin/cytoskeletal molecular function.
```

### GO curation table (leads requiring curator verification)

| GO term | Aspect | Current basis | Recommended action |
|---|---|---|---|
| GO:0035267 NuA4 histone acetyltransferase complex | CC | IBA | **Remove.** NuA4 actin subunit is ACTL6A; ACTL8 ~34% id, cytosolic. |
| GO:0098973 structural constituent of postsynaptic actin cytoskeleton | MF | IBA | **Remove.** Belongs to ACTL6B/ACTB in neurons; ACTL8 not in brain. |
| GO:0045202 synapse; GO:0030424 axon; GO:0007409 axonogenesis | CC/BP | IBA | **Remove / strongly down-weight.** No ACTL8 evidence; brain-absent. |
| GO:0005884 actin filament; GO:0015629 actin cytoskeleton | CC | IBA | **Hold as low-confidence IBA only.** Fold retained; no filament assay; PS00432 absent. |
| GO:0016020 membrane; GO:0019901 protein kinase binding | CC/MF | IBA | **Remove / non-core.** No direct binding assay; generic and uninformative. |
| GO:0048870 cell motility | BP | IBA | **Generalize/replace** with GO:0030335; treat as non-core. |
| GO:0030335 positive regulation of cell migration | BP | IMP (cancer KD, indirect) | **Retain as non-core, qualify as indirect** (tumor-cell, via PI3K/AKT/mTOR-MYC). |
| GO:0008284 positive regulation of cell population proliferation | BP | IMP (cancer KD, indirect) | **Retain as non-core, qualify as indirect.** |
| GO:0030855 epithelial cell differentiation | BP | IEP | Curator to verify original IEP source. |

For the two experimentally supported processes, the honest annotation is that ACTL8 *participates in the positive regulation of* migration and proliferation in tumor-cell contexts, mediated by PI3K/AKT/mTOR–MYC, rather than possessing a direct cell-motility molecular function. These should not be elevated to a "structural constituent of cytoskeleton" or "actin filament" interpretation.

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt Q9H568 (database, 2026) | Computational/database | **Refutes** direct assignment | Are the 9 actin terms experimental? | All 9 are IBA:GO_Central; only experimental annot is GO:0030855 (IEP) | Human record | High for provenance; IBA ≠ demonstration |
| PANTHER PTHR11937:SF208 (database) | Structural/evolutionary | **Refutes** ancestral inheritance | Do terms trace to ACTL8 lineage? | Terms are a pooled, self-contradictory family GO-slim | Family-level | High; slim co-lists mutually exclusive roles |
| Sequence alignment (this work) | Structural/evolutionary | **Qualifies** | Is ACTL8 close to NuA4/neuronal paralogs? | ~33% id to ACTL6A/B; 41% to actin | Human paralogs | High; global NW identity |
| PROSITE PS00432 scan (this work) | Structural/evolutionary | **Refutes** canonical actin function | Does ACTL8 retain the actin C-terminal signature? | No match in ACTL8; match in ACTB/ACTL6A/ACTL6B | Motif-level | High; position-level divergence |
| HPA ENSG00000117148 (database) | Localization | **Refutes** neural/nuclear CC terms | Where is ACTL8 expressed/localized? | Cytosol only; testis/oocyte enriched; brain not detected | Human tissues | High for RNA; antibody "not detected" in normal tissue |
| [PMID:31962007](https://pubmed.ncbi.nlm.nih.gov/31962007/) | Mutant phenotype + in vivo | **Supports (indirect)** GO:0030335/0008284 | Does ACTL8 KD reduce proliferation/migration? | shRNA KD ↓ proliferation, migration, invasion; tumor growth ↓ in nude mice | LUAD A549/H1975 | Strongest in vivo; indirect mechanism |
| [PMID:35116946](https://pubmed.ncbi.nlm.nih.gov/35116946/) | Mutant phenotype + profiling | **Supports (indirect)** | KD effect + mechanism | KD ↓ proliferation via FOXM1/STMN1/PLK1/BIRC5, cell-cycle pathways | LUAD A549 | Indirect; transcriptomic |
| [PMID:30535476](https://pubmed.ncbi.nlm.nih.gov/30535476/) | Mutant phenotype | **Supports (indirect)** | KD effect + pathway | KD ↓ proliferation/migration/invasion; PI3K/AKT suppressed; notes cytoplasmic/testis | HNSCC PCI-13 | Indirect; CTA framing |
| [PMID:35051678](https://pubmed.ncbi.nlm.nih.gov/35051678/) | Mutant phenotype | **Supports (indirect)** | KD effect + mechanism | KD arrests cell cycle; ↓ CDK1/cyclin E1/cyclin B2/c-Myc; ↑ apoptosis | OSCC TCA-83/CAL27 | Indirect; downstream cell cycle |
| [PMID:33883901](https://pubmed.ncbi.nlm.nih.gov/33883901/) | Mutant phenotype | **Supports (indirect)** | KD effect + pathway | Silencing ↓ proliferation/migration/invasion via PI3K/AKT/mTOR; rescue with 740Y-P | TNBC MDA-MB-231/BT-549 | Indirect; pathway rescue confirms indirectness |
| [PMID:39322809](https://pubmed.ncbi.nlm.nih.gov/39322809/) | Mutant phenotype | **Supports (indirect)** | KD effect + pathway | KD ↓ proliferation/migration/invasion; OE ↑ p-PI3K/AKT/mTOR | Gastric cancer | Indirect; bioinformatics-led |
| [PMID:41621692](https://pubmed.ncbi.nlm.nih.gov/41621692/) (2026) | Mutant phenotype + drug | **Supports (indirect)** | ACTL8-dependent metabolism | shRNA KD ↓ MYC→SLC1A5/GLS1, glutamine metab, redox; ↓ proliferation/migration | Breast cancer; Momordin Ic | Indirect; couples ACTL8 to metabolism, not cytoskeleton |
| [PMID:32125225](https://pubmed.ncbi.nlm.nih.gov/32125225/) | Mutant phenotype | **Excluded (RETRACTED)** | EC progression | Reported KD ↓ proliferation/migration | Endometrial cancer | **Retracted — do not cite as support** |

**Narrative.** The ACTL8 literature is dominated by cancer/testis-antigen oncology, uniformly using overexpression correlations plus knockdown functional assays. It is internally consistent and cross-tumor reproducible in one respect: ACTL8 depletion reduces tumor-cell proliferation, migration, and invasion, mechanistically pinned to PI3K/AKT/mTOR and MYC. None of these papers reports a direct molecular assay for actin polymerization, kinase binding, filament co-sedimentation, or NuA4 co-purification. The HNSCC paper is notable for stating plainly that ACTL8 is "mainly localized in the cytoplasm and generally expressed in the testis" — consistent with HPA and inconsistent with a nuclear NuA4 or neuronal-synaptic role. Against this experimental backdrop, the seed's nine terms have no primary-literature support and exist only as IBA propagation.

---

## Conflicts and Alternatives

- **Paralog confusion is the dominant risk.** NuA4→ACTL6A, neuronal/postsynaptic→ACTL6B/ACTB, testis/acrosome→ACTL7A/ACTL9. IBA propagation across PTHR11937 pulls all of these onto every leaf including ACTL8. This is confirmed mechanistically: PANTHER attaches the entire self-contradictory seed slim to ACTL8 at family level, and ACTL8 sits in the distinct SF208 subfamily — the seed terms are the *union* of two distinct paralogs' jobs, which no single protein performs.
- **Fold vs. function.** ACTL8 genuinely has the actin-like ATPase fold, which is why domain databases annotate it as actin-like. This justifies family membership but is not evidence of filament assembly or actin-binding activity, and ACTL8 lacks the conserved PS00432 C-terminal signature that even ACTL6A/ACTL6B retain.
- **Indirect vs. direct for migration/proliferation.** The cancer phenotypes are real but pleiotropic — an overexpressed CTA amplifying oncogenic signaling. They do not establish a direct cytoskeletal/motility mechanism.
- **Organism/context.** All functional data come from human tumor cell lines with ectopic/elevated ACTL8; the native testis/germ-cell role is untested.
- **Retraction artifact.** [PMID:32125225](https://pubmed.ncbi.nlm.nih.gov/32125225/) must not count as evidence.
- **Cannot fully exclude.** A noncanonical structural or peripheral-membrane association (fold retained, ~41% actin identity) remains a hypothesis, not evidence.

---

## Mechanistic Scope

- **Immediate molecular function (native):** Unknown. ACTL8 has an actin-like ATPase fold but no demonstrated ATP hydrolysis, filament assembly, or defined binding partner. Native context is testis germ cells / oocytes (CTA).
- **Direct gene-product activity vs. downstream:** All cancer phenotypes are downstream of an oncogenic PI3K/AKT/mTOR–MYC axis. ACTL8 acts as an upstream modulator; no data place it in the migration machinery, at synapses, on filaments, or in NuA4.
- **Loss-of-function inference only:** Migration/proliferation conclusions derive from knockdown (necessity), not from a direct mechanism — regulatory participation does not follow from necessity alone (seed caution respected).

---

## Limitations and Knowledge Gaps

1. **Does ACTL8 polymerize / bind actin?** Checked: no assay in literature; fold present, PS00432 absent. Matters for GO:0005884. Resolve with in-vitro polymerization / co-sedimentation and live-cell F-actin colocalization.
2. **NuA4 / chromatin complex membership?** Checked: no ACTL8 IP-MS; term is IBA; localization is cytosolic. Matters for GO:0035267. Resolve with endogenous ACTL8 affinity-MS.
3. **Direct kinase interaction?** Checked: cancer papers use pathway readouts / STRING predictions, no direct binding. Matters for GO:0019901. Resolve with co-IP / proximity labeling (BioID).
4. **Native germ-cell function?** Checked: only expression data. Resolve with knockout mouse / spermatogenesis phenotyping.
5. **PANTHER tree topology not independently re-derived** here (PTN002631484 / PTN002631586 / PTN007551913). A formal ancestral-state reconstruction would show whether ACTL8 branches basally or within a specialized clade — though the self-contradictory pooled slim already undermines whole-set inheritance.
6. **No AlphaFold interface analysis performed** — a cheap in-silico check of whether the divergent C-terminus disrupts the filament/complex-binding surface.
7. **Retraction confirmation** of [PMID:32125225](https://pubmed.ncbi.nlm.nih.gov/32125225/): confirm the notice in the curation system.

---

## Discriminating Tests

1. **AlphaFold/structure comparison:** superpose the ACTL8 model on F-actin and on the ACTL6A–NuA4 and ACTL6B interfaces; test whether the divergent C-terminus and loss of PS00432 abolish the binding surface. Adjudicates GO:0005884/GO:0035267.
2. **Recombinant ACTL8 pyrene-actin polymerization / co-sedimentation** → tests filament (GO:0005884) competence.
3. **Endogenous ACTL8 affinity-purification MS** in a testis or expressing tumor line → tests NuA4/complex membership (GO:0035267) and kinase binding (GO:0019901) directly.
4. **ACTL8-GFP localization + synaptic/cytoskeletal markers** → tests synapse/axon CC terms.
5. **Neuronal expression check** in single-cell/single-nucleus brain atlases beyond HPA (Allen Brain, GTEx neuron subsets) → firmly closes GO:0045202/GO:0030424/GO:0007409.
6. **Epistasis / rescue test:** is the migration/proliferation knockdown phenotype fully rescued by constitutive PI3K/AKT/MYC activation? If yes, this confirms indirect (regulatory) rather than direct (cytoskeletal) action.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

- **Remove or down-rank to low-confidence IBA:** GO:0035267 (NuA4), GO:0098973 (postsynaptic actin), GO:0045202 (synapse), GO:0030424 (axon), GO:0007409 (axonogenesis), GO:0019901 (protein kinase binding), GO:0016020 (membrane), GO:0048870 (cell motility) — paralog carry-over, no ACTL8 evidence, contradicted by cytosolic/germ-cell/no-brain localization.
- **Retain cautiously as low-confidence IBA only:** GO:0005884 (actin filament), GO:0015629 (actin cytoskeleton) — fold present, no functional assay; do not upgrade.
- **Retain but qualify as indirect / non-core experimental annotations:** GO:0030335 (positive regulation of cell migration) and GO:0008284 (positive regulation of cell population proliferation), supported by [PMID:41621692](https://pubmed.ncbi.nlm.nih.gov/41621692/), [PMID:39322809](https://pubmed.ncbi.nlm.nih.gov/39322809/), [PMID:35051678](https://pubmed.ncbi.nlm.nih.gov/35051678/), [PMID:33883901](https://pubmed.ncbi.nlm.nih.gov/33883901/), [PMID:31962007](https://pubmed.ncbi.nlm.nih.gov/31962007/), [PMID:35116946](https://pubmed.ncbi.nlm.nih.gov/35116946/), [PMID:30535476](https://pubmed.ncbi.nlm.nih.gov/30535476/) — annotate with an "indirect/pleiotropic, tumor-cell context, via PI3K–AKT–mTOR–MYC" note.
- **Exclude:** [PMID:32125225](https://pubmed.ncbi.nlm.nih.gov/32125225/) (retracted).
- **Candidate snippets to verify:**
  - HNSCC ([PMID:30535476](https://pubmed.ncbi.nlm.nih.gov/30535476/)): "*Actin‑like protein 8 (ACTL8) is a member of the cancer‑testis antigens (CTA) family, which is mainly localized in the cytoplasm and generally expressed in the testis.*"
  - TNBC ([PMID:33883901](https://pubmed.ncbi.nlm.nih.gov/33883901/)): "*silencing ACTL8 could inhibit the activation of PI3K/AKT/mTOR signaling pathway ... reversed by ... 740Y-P.*"
  - Momordin Ic ([PMID:41621692](https://pubmed.ncbi.nlm.nih.gov/41621692/)): "*shRNA knockdown of ACTL8 reduced MYC expression and its downstream targets SLC1A5 and GLS1, suppressing cell proliferation, migration and invasion.*"
- **Suggested question to curators:** Should divergent cancer/testis-antigen actin paralogs (like ACTL8) be excluded from PTHR11937 IBA propagation of the neuronal/NuA4 terms, given the self-contradictory family GO-slim?

---

## Bottom Line

The nine "inherited" actin-family GO terms for ACTL8 are **over-annotations** — IBA carry-over from a self-contradictory PANTHER family GO-slim, unsupported by ACTL8's divergent sequence (~33% identity to the NuA4/neuronal ARP paralogs), its loss of the conserved actin C-terminal signature PS00432, and its cytosolic, germ-cell-restricted, brain-absent localization. They should be removed or held as low-confidence rather than assigned as direct function. The only experimentally supported activities — positive regulation of cell migration (GO:0030335) and proliferation (GO:0008284) — are indirect, tumor-context, PI3K/AKT/mTOR–MYC-mediated pleiotropy, not a direct molecular function; and the endometrial-cancer study PMID:32125225 is retracted and must be excluded.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)