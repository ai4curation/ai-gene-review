---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T02:23:25.718886'
end_time: '2026-09-21T02:49:16.293244'
duration_seconds: 1550.57
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: ACL4
  gene_symbol: ACL4
  uniprot_accession: Q03771
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: mitochondrial-targeting-and-translocation-contribution
  hypothesis_text: 'Saccharomyces cerevisiae Acl4 localizes to mitochondrial outer
    membrane, contributes_to protein transmembrane transporter activity, participates
    in matrix protein import or inner-membrane protein insertion, or binds mitochondrial
    targeting sequences. Adjudicate each independently from its established Rpl4 chaperone
    function. Preserve the contributes_to qualifier: the claim need not mean Acl4
    forms an integral membrane channel. Inspect relevant family/ancestral placement
    and targeting-sequence recognition data; a soluble architecture and established
    alternative substrate do not themselves exclude a translocation cofactor role.
    The existing transporter report assumed an integral channel and did not settle
    the qualified contribution or each separate process/location.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/ACL4/ACL4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Saccharomyces cerevisiae Acl4 localizes to mitochondrial\
    \ outer membrane, contributes_to protein\n  transmembrane transporter activity,\
    \ participates in matrix protein import or inner-membrane protein\n  insertion,\
    \ or binds mitochondrial targeting sequences. Adjudicate each independently from\
    \ its established\n  Rpl4 chaperone function. Preserve the contributes_to qualifier:\
    \ the claim need not mean Acl4 forms an\n  integral membrane channel. Inspect\
    \ relevant family/ancestral placement and targeting-sequence recognition\n  data;\
    \ a soluble architecture and established alternative substrate do not themselves\
    \ exclude a translocation\n  cofactor role. The existing transporter report assumed\
    \ an integral channel and did not settle the qualified\n  contribution or each\
    \ separate process/location.'\nfocus_type: function_assignment\ncontext: []\n\
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
citation_count: 6
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** ACL4
- **Gene symbol:** ACL4
- **UniProt accession:** Q03771

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** mitochondrial-targeting-and-translocation-contribution
- **Source file:** genes/yeast/ACL4/ACL4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae Acl4 localizes to mitochondrial outer membrane, contributes_to protein transmembrane transporter activity, participates in matrix protein import or inner-membrane protein insertion, or binds mitochondrial targeting sequences. Adjudicate each independently from its established Rpl4 chaperone function. Preserve the contributes_to qualifier: the claim need not mean Acl4 forms an integral membrane channel. Inspect relevant family/ancestral placement and targeting-sequence recognition data; a soluble architecture and established alternative substrate do not themselves exclude a translocation cofactor role. The existing transporter report assumed an integral channel and did not settle the qualified contribution or each separate process/location.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Saccharomyces cerevisiae Acl4 localizes to mitochondrial outer membrane, contributes_to protein
  transmembrane transporter activity, participates in matrix protein import or inner-membrane protein
  insertion, or binds mitochondrial targeting sequences. Adjudicate each independently from its established
  Rpl4 chaperone function. Preserve the contributes_to qualifier: the claim need not mean Acl4 forms an
  integral membrane channel. Inspect relevant family/ancestral placement and targeting-sequence recognition
  data; a soluble architecture and established alternative substrate do not themselves exclude a translocation
  cofactor role. The existing transporter report assumed an integral channel and did not settle the qualified
  contribution or each separate process/location.'
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

# AIGR Gene Hypothesis Deep Research — Final Report

## ACL4 (Q03771, *Saccharomyces cerevisiae*): Mitochondrial Targeting and Translocation Contribution

**Focus type:** function_assignment
**Hypothesis slug:** mitochondrial-targeting-and-translocation-contribution
**Source file:** `genes/yeast/ACL4/ACL4-ai-review.yaml`

---

## Summary

**Verdict: REFUTED (as a core or contributory function).** The seed hypothesis proposes that yeast Acl4 localizes to the mitochondrial outer membrane and *contributes_to* protein transmembrane transporter activity, matrix protein import, inner-membrane protein insertion, or mitochondrial targeting-sequence binding — to be adjudicated independently from its established Rpl4 chaperone role, with the `contributes_to` qualifier preserved so that Acl4 need not form an integral channel. After tracing the provenance of every mitochondrial GO term on Q03771, resolving the phylogenetic seeds behind them, comparing membrane topology against the true import receptors, and mapping the full functional interaction network, the mitochondrial hypothesis collapses.

**All five mitochondrial/transmembrane-transporter GO terms on Acl4 are phylogenetic (IBA, ECO:0000318) annotations propagated from a single PANTHER node (PTN002340064) whose experimental seeds are the TPR-domain mitochondrial import receptors TOM70, TOM71, and human TOMM70.** This is a textbook family/paralog over-annotation driven by a shared cytosolic TPR superhelical fold. Unlike those receptors — each anchored in the mitochondrial outer membrane by an N-terminal transmembrane helix — Acl4 has **zero transmembrane segments** and is curated as **cytoplasmic + nuclear**. Every direct-evidence annotation on Acl4 describes a soluble TPR assembly chaperone dedicated to ribosomal protein Rpl4/uL4.

The `contributes_to` qualifier does not rescue the hypothesis. That qualifier is designed to capture a genuine, evidenced cofactor/subunit contribution to a molecular activity; it is not a mechanism for retaining IBA terms that have no experimental support in the target species and that trace entirely to non-orthologous, membrane-anchored family members. The interaction network is decisive: Acl4 partners exclusively with ribosome-assembly chaperones (Rpl4, Kap104, Syo1, Tsr2, Yar1, Bcp1, Rrb1, Sqt1) and **never** with any TOM/TIM/SAM/PAM import-machinery component. **Recommended curation action (lead requiring curator verification): do not propagate the mitochondrial CC/MF/BP terms into the ACL4 review; treat them as IBA over-annotation and mark them NOT/remove.** The most important caveat is that this conclusion rests on public GO provenance, UniProt topology, PANTHER/InterPro family placement, and STRING interactions rather than a dedicated wet-lab exclusion of a mitochondrial role — but the direct experimental literature that does exist points uniformly and exclusively to the cytoplasmic/nuclear Rpl4 chaperone function.

---

## Key Findings

### Finding F001 — Every mitochondrial GO term on Acl4 is IBA (phylogenetic), with zero experimental support

QuickGO provenance for Q03771 shows the five hypothesis-relevant terms are **all** carried by the phylogenetic inference evidence code IBA (ECO:0000318, `GO_REF:0000033`):

| GO ID | Term | Aspect | Evidence | Source |
|-------|------|--------|----------|--------|
| GO:0005741 | mitochondrial outer membrane | CC | IBA (ECO:0000318) | PANTHER PTN002340064 |
| GO:0030150 | protein import into mitochondrial matrix | BP | IBA | PANTHER PTN002340064 |
| GO:0045039 | protein insertion into mitochondrial inner membrane | BP | IBA | PANTHER PTN002340064 |
| GO:0008320 | transmembrane protein transporter activity | MF | IBA | PANTHER PTN002340064 |
| GO:0030943 | mitochondrion targeting sequence binding | MF | IBA | PANTHER PTN002340064 |

Each traces to PANTHER node **PTN002340064**, and the `with/from` field contains experimental annotations of *other* family members (e.g., human `UniProtKB:O94826`), not experimental data on Acl4 itself. The PANTHER family GO-slim reads like a mitochondrial import receptor: *signal sequence binding*, *protein transmembrane transporter activity*, *protein import into mitochondrial matrix*, *protein insertion into mitochondrial inner membrane*, *mitochondrial outer membrane*, with protein class *primary active transporter* (PC00068).

By contrast, **every direct-evidence (IDA/IMP/EXP/HDA) annotation on Acl4 supports only the chaperone/ribosome-biogenesis function**: protein-folding chaperone (GO:0044183, IDA, [PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/)); protein carrier activity (GO:0140597, IDA, [PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/)); ribosomal large subunit biogenesis (GO:0042273, IMP, both papers); cytoplasm (IDA/EXP/HDA, incl. [PMID: 14562095](https://pubmed.ncbi.nlm.nih.gov/14562095/)); and nucleus (IDA/HDA). The separation is clean: the mitochondrial terms are 100% inferred by phylogeny, the real function is 100% experimental.

### Finding F002 — Experimentally, Acl4 is a soluble cytoplasmic/nuclear TPR assembly chaperone dedicated to Rpl4/uL4

Three primary structural/biochemical studies establish the true function:

1. **[PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/) (Pillet et al., 2015):** Acl4 binds the conserved internal loop of newly synthesized Rpl4 and escorts it, with karyopherin Kap104, to the nuclear pre-60S assembly site. Acl4 localizes to **both cytoplasm and nucleus** and captures nascent Rpl4 co-translationally. Loss of Acl4 causes a severe slow-growth phenotype and a 60S subunit deficiency (IDA protein carrier activity GO:0140597; nucleus & cytoplasm IDA).
2. **[PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/) (Stelter et al., 2015):** Acl4 binds Rpl4 via its **superhelical TPR domain**, restricting premature loop insertion until Rpl18 is available on the nascent pre-ribosome (IDA protein-folding chaperone; IMP ribosomal large subunit biogenesis).
3. **[PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/) (Huber & Hoelz, 2017):** The crystal structure of the Rpl4–Acl4 complex shows Acl4 sequestering ~70 exposed residues of the extended Rpl4 loop. The eukaryote-specific Rpl4 extension carries overlapping Acl4 and Kap104 binding sites; Acl4 simultaneously protects unassembled Rpl4 from the cellular degradation machinery and facilitates its nuclear import.

UniProt curation for Q03771 records localization **Cytoplasm + Nucleus** and function **chaperone for L4**. The domain architecture is a soluble helical-repeat protein: Gene3D 1.25.40.10 (TPR), InterPro IPR011990 (TPR-like helical), and a C-terminal ACL4_C domain (Pfam PF29063). There is **no transmembrane segment** — Acl4 cannot be an integral membrane channel or an outer-membrane-anchored receptor.

### Finding F003 — The paralog confusion is pinned down: Acl4's IBA mito terms are inherited from TOM70/TOM71/TOMM70 receptors, which (unlike Acl4) are membrane-anchored

Resolving the `with/from` experimental seeds behind Acl4's IBA mitochondrial annotations gives:

| Seed | Identity | Role | Localization |
|------|----------|------|--------------|
| SGD S000005065 | **TOM70** (yeast) | Outer-membrane import receptor | Mitochondrial outer membrane |
| SGD S000001159 | **TOM71** (yeast) | Tom70 paralog receptor | Mitochondrial outer membrane |
| UniProtKB O94826 | **TOMM70** (human) | Import receptor subunit | Mitochondrial outer membrane |

All three are TPR-domain mitochondrial import receptors sharing PANTHER family PTN002340064 with Acl4. The defining topological comparison:

| Protein | UniProt | Length | Transmembrane | Localization |
|---------|---------|--------|---------------|--------------|
| **Acl4** | Q03771 | 387 aa | **0 TM segments** | Cytoplasm + Nucleus |
| Tom70 | P07213 | 617 aa | 1 TM (res ~11–30, helical) | Mito outer membrane |
| Tom71 | P38825 | 639 aa | 1 TM (res ~15–32) | Mito outer membrane |

Acl4 shares the cytosolic **TPR superhelix** with these receptors — that is why PANTHER groups them — but lacks the N-terminal membrane anchor that makes Tom70/Tom71/TOMM70 outer-membrane receptors. The shared fold is a solvent-exposed peptide-binding scaffold used convergently: a presequence/preprotein for the receptors, the Rpl4 loop for Acl4. This is exactly the ancestral-function ambiguity that produces IBA over-annotation. (Separately, a distinct HGI "de novo/co-translational folding" annotation GO:0051083 on Acl4 seeds to EGD1/EGD2 = NAC subunits — again cytosolic, not mitochondrial.)

### Finding F004 — Acl4's functional interaction network is entirely ribosome-assembly chaperones, with zero mitochondrial-import partners

A STRING v12 network for ACL4 (*S. cerevisiae*, add_nodes=15) returns functional partners that are, without exception, ribosome-biogenesis factors:

| Partner | STRING score | Role |
|---------|--------------|------|
| RRB1 | 0.979 | Rpl3 assembly chaperone |
| RPL4A/RPL4B | (substrate) | Acl4's client ribosomal protein |
| KAP104 | (transport) | Karyopherin for Rpl4 nuclear import |
| SYO1 | 0.945 | Symportin/assembly chaperone |
| TSR2 | 0.935 | Rps26 chaperone |
| YAR1 | 0.932 | Rps3 chaperone |
| BCP1 | 0.915 | Rpl23 chaperone |
| RPS3 | 0.889 | Ribosomal protein |
| TSR4 | 0.874 | Rpl3 chaperone |
| SQT1 | 0.826 | Rpl10 assembly chaperone |
| RPL5 | 0.816 | Ribosomal protein |

An explicit query against the entire mitochondrial import machinery — {TOM20, TOM22, TOM40, TOM70, TOM71, TIM17, TIM22, TIM23, TIM44, SAM50, MAS1, MAS2, PAM16, PAM18, MGE1, SSC1} — returned **NONE** at any confidence threshold. The only non-ribosome hits are generic high-abundance proteins (PGK1, TPI1, RNA14). If Acl4 contributed to mitochondrial translocation, at least one TOM/TIM/SAM/PAM partner would be expected; there are none.

---

## Mechanistic Model / Interpretation

The evidence resolves into a single coherent story: **a shared TPR fold created a phylogenetic annotation bridge between a cytosolic ribosome-assembly chaperone (Acl4) and a family of membrane-anchored mitochondrial import receptors (Tom70/Tom71/TOMM70), and GO's IBA pipeline propagated the receptors' mitochondrial terms onto Acl4 despite the absence of the one feature — a membrane anchor — that defines the receptor function.**

```
                       PANTHER family PTN002340064
                     (shared cytosolic TPR superhelix)
                                 │
        ┌────────────────────────┴────────────────────────┐
        │                                                  │
   IMPORT RECEPTORS (experimental)                  ACL4 (Q03771)
   Tom70 / Tom71 / human TOMM70                     387 aa, 0 TM
        │  N-terminal TM anchor                          │  soluble
        │  → mito outer membrane                         │  → cytoplasm + nucleus
        │  → presequence / preprotein binding            │  → binds Rpl4 internal loop
        │  → import into matrix / IM insertion           │  → escorts Rpl4 to pre-60S
        │                                                 │     with Kap104
        └──────── IBA propagation (ECO:0000318) ─────────►│  GO:0005741, GO:0030150,
              (with/from = receptors, NOT Acl4)              GO:0045039, GO:0008320,
                                                             GO:0030943  ← ARTIFACTS
```

The `contributes_to` framing is a reasonable general caution — a soluble cofactor can genuinely contribute to a membrane transport activity without being the channel. But that logic requires *some* independent evidence tying the protein to the transport machinery or process. Here there is none: no outer-membrane localization (Acl4 is cytoplasmic/nuclear), no physical or genetic link to TOM/TIM/SAM/PAM, and no assay of presequence binding or import activity. The alternative substrate (Rpl4) is not merely "established"; it is the *only* substrate with structural, biochemical, and genetic support, and it fully explains Acl4's TPR-mediated peptide-binding activity — indeed the substrate-binding surface is structurally saturated by the 70-residue Rpl4 loop. The most parsimonious model is that Acl4 does one thing — chaperone and deliver Rpl4 — and that the mitochondrial terms are database carry-over from non-orthologous family members.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence & limitations |
|----------|---------------|------------------|--------------|-------------|---------|--------------------------|
| QuickGO provenance for Q03771 (GO_REF:0000033) | Database/provenance | **Refutes** mito core function | Are Acl4's mito GO terms experimental? | All 5 mito/transporter terms are IBA from PANTHER PTN002340064; with/from = other family members | GO annotation records | High; provenance-level, not a wet assay |
| PANTHER PTN002340064 geneinfo | Structural/evolutionary | **Explains artifact** | Why does Acl4 carry mito terms? | Family GO-slim = signal-sequence binding, transmembrane transporter, matrix import, IM insertion, OM; class = primary active transporter | PANTHER classification | High |
| [PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/) Pillet 2015 | Direct assay + localization + mutant | **Competing** (true function) | What does Acl4 actually do? | Acl4 escorts Rpl4 with Kap104 to nuclear pre-60S; localizes cytoplasm + nucleus; Δacl4 → slow growth, 60S deficit | *S. cerevisiae* | High |
| [PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/) Stelter 2015 | Direct assay + structural | **Competing** (true function) | Mechanism of Rpl4 binding | Acl4 binds Rpl4 internal loop via superhelical TPR domain; regulates loop-insertion timing | *S. cerevisiae* | High |
| [PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/) Huber & Hoelz 2017 | Structural (crystal) | **Competing** (true function) | Structural basis of Acl4 function | Acl4 sequesters ~70 residues of Rpl4 loop; overlapping Acl4/Kap104 sites; protects from degradation, aids nuclear import | *S. cerevisiae*, in vitro | High; soluble complex, no membrane component |
| UniProt Q03771 vs P07213/P38825 topology | Structural/evolutionary | **Refutes** OM localization | Does Acl4 have a membrane anchor? | Acl4 = 387 aa, 0 TM, cytoplasm+nucleus; Tom70/71 have N-terminal TM, OM localization | Sequence/topology | High |
| PANTHER seed resolution (TOM70/TOM71/TOMM70) | Structural/evolutionary | **Refutes** (identifies paralog error) | What seeds the IBA mito terms? | Seeds are TPR mito import receptors, not orthologs of Acl4's true function | PANTHER/SGD/UniProt | High |
| STRING v12 ACL4 network | Interaction | **Refutes** import role | Does Acl4 interact with import machinery? | 0 of TOM/TIM/SAM/PAM partners; all partners are ribosome-assembly chaperones | *S. cerevisiae* | High; functional+physical STRING evidence |
| [PMID: 35357307](https://pubmed.ncbi.nlm.nih.gov/35357307/) Pillet 2022 | Direct assay + mutant | **Competing** (true function) | Broader chaperone role | Acl4 co-translationally recognizes Rpl4, reduces mRNA degradation; parallel to Rrb1/Rpl3 | *S. cerevisiae* | High |
| [PMID: 39426497](https://pubmed.ncbi.nlm.nih.gov/39426497/) NAC/Caf130 2024 | Genetic interaction | **Competing** (true function) | Genetic context of Δacl4 | Nacβ2/Caf130 modulate Rpl4 mRNA fate; genetic interaction with acl4 in ribosome context | *S. cerevisiae* | Medium-high; ribosome-centric, no mito link |

### How the key papers bear on the finding

- **[PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/)** and **[PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/)** are the foundational functional characterizations: they define Acl4 as the dedicated Rpl4 chaperone, localize it to cytoplasm + nucleus, and attribute its "carrier" activity to nucleo-cytoplasmic escort of Rpl4 — not transmembrane transport. They directly displace the mitochondrial interpretation.
- **[PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/)** provides the structural clincher: the TPR interface is occupied by the Rpl4 loop, arguing against a free presequence-binding function and demonstrating a dedicated, substrate-specific interaction unlike promiscuous import receptors.
- **[PMID: 35357307](https://pubmed.ncbi.nlm.nih.gov/35357307/)** and **[PMID: 39426497](https://pubmed.ncbi.nlm.nih.gov/39426497/)** embed ACL4 in the r-protein production / proteostasis network (Rrb1, NAC, Caf130/CCR4-Not), reinforcing that its genetic neighborhood is translation/ribosome biogenesis, not mitochondrial import.

---

## GO Curation Implications

The likely curation action, **as a lead requiring curator verification**, is to **not propagate any of the five mitochondrial/transmembrane-transporter terms into the ACL4 review and to mark them as IBA over-annotation (NOT / remove)**:

| GO ID | Term | Aspect | Current basis | Recommended action |
|-------|------|--------|---------------|--------------------|
| GO:0005741 | mitochondrial outer membrane | CC | IBA only | **Remove / do not accept** — contradicted by curated cytoplasm+nucleus localization and 0 TM segments |
| GO:0008320 | transmembrane protein transporter activity | MF | IBA only | **Remove / do not accept** — no transport assay; activity is TPR peptide-binding, not transport |
| GO:0030943 | mitochondrion targeting sequence binding | MF | IBA only | **Remove / do not accept** — binding target is the Rpl4 internal loop, not a mito presequence |
| GO:0030150 | protein import into mitochondrial matrix | BP | IBA only | **Remove / do not accept** — no import assay, no import-machinery interaction |
| GO:0045039 | protein insertion into inner membrane | BP | IBA only | **Remove / do not accept** — no evidence; Acl4 is not in the IM-insertion pathway |
| GO:0044183 | protein-folding chaperone | MF | IDA (PMID:25936803) | **Retain — core** |
| GO:0140597 | protein carrier activity | MF | IDA (PMID:26447800) | **Retain** with note: refers to nucleo-cytoplasmic escort of Rpl4, **not** transmembrane transport |
| GO:0042273 | ribosomal large subunit biogenesis | BP | IMP (PMID:25936803; 26447800) | **Retain — core** |
| GO:0005737 / GO:0005634 | cytoplasm / nucleus | CC | IDA/EXP/HDA | **Retain — core** |

On the seed's "transporter" concern: the only *experimental* transporter-flavored term is **GO:0140597 protein carrier activity (IDA)**, the chaperone-escort of Rpl4 to the nucleus. The seed's "protein transmembrane transporter activity" is the separate **IBA** term GO:0008320 and should be adjudicated as unsupported. The `contributes_to` qualifier cannot be used to launder an IBA term with no experimental support in yeast and whose phylogenetic seeds are non-orthologous membrane receptors. We avoid recommending "protein binding" as an endpoint because more informative supported terms already exist (GO:0140597, GO:0044183).

---

## Mechanistic Scope

The immediate, directly evidenced molecular function of Acl4 is **peptide capture and chaperoning via a superhelical TPR domain**: it binds the conserved internal loop and eukaryote-specific extension of nascent Rpl4, sequesters ~70 exposed residues, protects them from aggregation and degradation, and — with Kap104 — delivers Rpl4 to the nuclear pre-60S assembly site, releasing it once Rpl18 is available. This is a soluble, cytoplasm-to-nucleus activity.

Everything mitochondrial in the hypothesis lies **outside** this direct scope, and is not even a downstream phenotype of Acl4: matrix import, IM insertion, and transmembrane transporter activity are simply not connected to Acl4 by any evidence in yeast. They are inherited descriptors of a different protein class (Tom70-type receptors). The slow-growth and 60S-deficiency phenotypes of Δacl4 are downstream consequences of losing the Rpl4 chaperone — ribosomal, not mitochondrial. No loss-of-function phenotype links Acl4 to mitochondrial import.

---

## Conflicts and Alternatives

- **Paralog / family confusion (central issue):** The IBA terms derive from TOM70/TOM71/TOMM70, TPR-domain mitochondrial import receptors that share PANTHER PTN002340064 with Acl4 but are membrane-anchored. Shared TPR fold ≠ shared cellular function.
- **Membrane-anchor contrast (decisive):** Acl4 (387 aa) has **zero TM segments** and is cytoplasmic/nuclear; Tom70 (617 aa) and Tom71 (639 aa) each have an N-terminal TM anchor and reside in the mitochondrial outer membrane. Tom70's TPR clamp binds Hsp70/Hsp90-delivered precursors at the OM; Acl4's superhelical TPR wraps the Rpl4 loop in the cytosol/nucleus — same fold, different job.
- **Database carry-over:** The mitochondrial terms are annotation artifacts propagated by GO_REF:0000033 phylogenetic inference, not species-specific findings.
- **Semantic collision on "transport":** GO:0140597 (protein carrier, IDA, real) vs GO:0008320 (transmembrane transporter, IBA, unsupported) are easily conflated; the seed's "transporter report" concern maps onto this ambiguity.
- **Cross-species carry-over:** `with/from` xrefs point to *S. pombe* (O94826), rat, and *C. elegans* family members — none validate a yeast Acl4 mitochondrial role.
- **No competing experimental claim:** Literature searches for "Acl4 mitochondrial", "Acl4 outer membrane", and "Tom70 targeting" returned no papers linking Acl4 to mitochondria — consistent with the mito terms being annotation-only.

No evidence was found that *conflicts* with the refutation — i.e., no primary study placing Acl4 at the mitochondrion or in the import pathway.

---

## Limitations and Knowledge Gaps

1. **Provenance-based, not assay-based refutation.** The conclusion rests on GO provenance, UniProt topology, PANTHER placement, and STRING interactions rather than a dedicated experiment specifically excluding a mitochondrial role. This is standard and appropriate for adjudicating IBA over-annotation, but the mitochondrial claim is refuted by absence of positive evidence plus a clear artifact mechanism, not by a negative import assay.
2. **No dedicated negative mito-localization assay cited here.** Checked: UniProt curated CC (cytoplasm+nucleus; IDA/HDA/EXP), GFP-based localization ([PMID: 14562095](https://pubmed.ncbi.nlm.nih.gov/14562095/)). A cross-check against MitoCarta / high-confidence yeast mito-proteome inventories would harden the CC call (Acl4 is not an established mito protein).
3. **Negative interaction data are bounded by database coverage.** STRING returning no TOM/TIM/SAM/PAM partner is strong but not absolute; a very transient or condition-specific interaction could be under-sampled.
4. **Targeting-sequence binding not directly excluded in vitro.** No study has directly assayed whether Acl4 can bind a canonical mitochondrial presequence. The structural occupation of its TPR site by the Rpl4 loop argues against it, but a direct in-vitro presequence-binding assay has not been done.
5. **PANTHER tree specifics / stale carry-over.** The exact leaf set of PTN002340064 and whether SGD/GO-Central has already flagged these IBA terms were not exhaustively confirmed.

---

## Discriminating Tests

1. **Localization decider:** endogenous Acl4-GFP co-imaged with a mito marker, plus mitochondrial subfractionation + protease protection. Prediction under the true model: cytosolic/nuclear, absent from mito fractions.
2. **Functional decider:** measure mitochondrial protein-import kinetics of a matrix/IM reporter in Δacl4 vs WT. Prediction: no import defect; only ribosome-biogenesis/Rpl4 phenotypes.
3. **Interaction decider:** affinity purification / proximity labeling (BioID) of Acl4 — expect Rpl4, Kap104, ribosome-biogenesis factors; not TOM/TIM.
4. **In-vitro presequence-binding assay:** titrate a labeled canonical mitochondrial presequence against purified Acl4. Prediction: no specific binding, or binding competed by the Rpl4 loop peptide.
5. **Bioinformatic decider:** re-curate the PANTHER family so the ACL4 r-protein-chaperone clade is separated from the Tom70-like translocase clade, removing the IBA source.

---

## Proposed Follow-up Actions / Curation Leads

*All items below are leads requiring curator verification.*

1. **Action change — reject mitochondrial terms.** In `ACL4-ai-review.yaml`, set the review action for GO:0005741, GO:0008320, GO:0030943, GO:0030150, and GO:0045039 to **remove/NOT**, with rationale: "IBA over-annotation from PANTHER PTN002340064; experimental seeds are TOM70/TOM71/TOMM70 mitochondrial import receptors; Acl4 has 0 TM segments and is curated cytoplasm+nucleus."
2. **Retain experimental terms:** GO:0044183 (protein-folding chaperone), GO:0140597 (protein carrier activity), GO:0042273 (ribosomal large subunit biogenesis), GO:0005737 (cytoplasm), GO:0005634 (nucleus).
3. **Candidate reference snippets to verify:**
   - [PMID: 26447800](https://pubmed.ncbi.nlm.nih.gov/26447800/): *"Acl4 localizes to both the cytoplasm and nucleus and it has the capacity to capture nascent Rpl4 in a co-translational manner"* — confirms non-mitochondrial localization.
   - [PMID: 25936803](https://pubmed.ncbi.nlm.nih.gov/25936803/): *"assembly chaperone Acl4 that initially binds the universally conserved internal loop of newly synthesized RpL4 via its superhelical TPR domain"* — confirms TPR peptide-binding is directed at Rpl4, not a mito presequence.
   - [PMID: 28148929](https://pubmed.ncbi.nlm.nih.gov/28148929/): *"sequestering 70 exposed residues of the extended RpL4 loop"* and *"Acl4 serves a dual function to facilitate nuclear import and simultaneously protect unassembled RpL4"* — confirms the occupied binding site and nuclear (not mitochondrial) import role.
4. **Suggested curator questions:** (1) Should the review explicitly annotate these five terms as IBA-only over-annotation with a PANTHER family note? (2) Should GO:0140597 carry a clarifying note that it is nuclear escort, not transmembrane transport? (3) Is a NOT qualifier (e.g., NOT mitochondrial outer membrane) justified, or is silent non-acceptance preferable?
5. **Suggested experiments:** the discriminating tests above, prioritizing (a) endogenous-tag localization + mito subfractionation and (b) Acl4–Tom70 proximity labeling as the fastest, most decisive.

---

## Bottom Line

Adjudicated independently, **all four mitochondrial sub-claims and the transmembrane-transporter sub-claim fail**: they originate solely from PANTHER IBA propagation (fold-homology to Tom70-class import receptors) with zero experimental support, while every direct assay defines Acl4 as a soluble TPR chaperone that binds and escorts Rpl4/uL4 during cytosolic ribosome biogenesis. The `contributes_to` qualifier does not save the mitochondrial terms. Recommended lead: do not propagate the mitochondrial/transporter terms into the ACL4 review; retain the Rpl4-chaperone / ribosome-biogenesis / cytoplasm+nucleus annotations.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)