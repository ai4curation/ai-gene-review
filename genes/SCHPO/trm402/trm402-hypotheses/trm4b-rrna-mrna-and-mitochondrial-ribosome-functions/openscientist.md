---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T22:15:57.940797'
end_time: '2026-09-20T22:48:25.213994'
duration_seconds: 1947.27
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: trm402
  gene_symbol: trm4b
  uniprot_accession: O13935
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: function_assignment
  hypothesis_slug: trm4b-rrna-mrna-and-mitochondrial-ribosome-functions
  hypothesis_text: Schizosaccharomyces pombe Trm4b (O13935; gene directory trm402)
    methylates rRNA or mRNA at cytosine C5, participates in rRNA processing or mitochondrial
    large ribosomal subunit assembly. Evaluate each independently from established
    tRNA C49/C50 methylation. PMID:30646830 identifies tRNA-site specificity and leaves
    other RNA substrates open; a negative tRNA C34 result is not a negative rRNA/mRNA
    assay. Examine PTN000516076 placement and experimentally supported descendants,
    including verifying identity of MGI:1919431 rather than assuming it is NSUN4,
    plus the separate ISS provenance for mRNA activity. Distinguish positive evidence
    for a different substrate from demonstrated loss of these functions.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/trm402/trm402-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe Trm4b (O13935; gene\
    \ directory trm402) methylates rRNA or mRNA at\n  cytosine C5, participates in\
    \ rRNA processing or mitochondrial large ribosomal subunit assembly. Evaluate\n\
    \  each independently from established tRNA C49/C50 methylation. PMID:30646830\
    \ identifies tRNA-site specificity\n  and leaves other RNA substrates open; a\
    \ negative tRNA C34 result is not a negative rRNA/mRNA assay.\n  Examine PTN000516076\
    \ placement and experimentally supported descendants, including verifying identity\n\
    \  of MGI:1919431 rather than assuming it is NSUN4, plus the separate ISS provenance\
    \ for mRNA activity.\n  Distinguish positive evidence for a different substrate\
    \ from demonstrated loss of these functions.\nfocus_type: function_assignment\n\
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** trm402
- **Gene symbol:** trm4b
- **UniProt accession:** O13935

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** trm4b-rrna-mrna-and-mitochondrial-ribosome-functions
- **Source file:** genes/SCHPO/trm402/trm402-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Schizosaccharomyces pombe Trm4b (O13935; gene directory trm402) methylates rRNA or mRNA at cytosine C5, participates in rRNA processing or mitochondrial large ribosomal subunit assembly. Evaluate each independently from established tRNA C49/C50 methylation. PMID:30646830 identifies tRNA-site specificity and leaves other RNA substrates open; a negative tRNA C34 result is not a negative rRNA/mRNA assay. Examine PTN000516076 placement and experimentally supported descendants, including verifying identity of MGI:1919431 rather than assuming it is NSUN4, plus the separate ISS provenance for mRNA activity. Distinguish positive evidence for a different substrate from demonstrated loss of these functions.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe Trm4b (O13935; gene directory trm402) methylates rRNA or mRNA at
  cytosine C5, participates in rRNA processing or mitochondrial large ribosomal subunit assembly. Evaluate
  each independently from established tRNA C49/C50 methylation. PMID:30646830 identifies tRNA-site specificity
  and leaves other RNA substrates open; a negative tRNA C34 result is not a negative rRNA/mRNA assay.
  Examine PTN000516076 placement and experimentally supported descendants, including verifying identity
  of MGI:1919431 rather than assuming it is NSUN4, plus the separate ISS provenance for mRNA activity.
  Distinguish positive evidence for a different substrate from demonstrated loss of these functions.
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

# AIGR Gene Hypothesis Deep Research — *S. pombe* Trm4b (O13935): rRNA/mRNA and Mitochondrial Ribosome Functions

**Target:** *Schizosaccharomyces pombe* Trm4b / trm4b (gene directory `trm402`, SPAC23C4.17), UniProt **O13935**
**Focus type:** function_assignment
**Hypothesis slug:** `trm4b-rrna-mrna-and-mitochondrial-ribosome-functions`
**Iterations completed:** 3

---

## Summary

The seed hypothesis proposes that *S. pombe* Trm4b methylates rRNA or mRNA at cytosine C5, and/or participates in rRNA processing or mitochondrial large-ribosomal-subunit (LSU) assembly — each to be judged independently of its established tRNA C49/C50 methylation, and each requiring positive evidence for a *new substrate* rather than merely the absence of a negative (tRNA-C34) result. Evaluating each sub-claim against primary literature and public bioinformatics resources, the answer is: **Trm4b is strongly supported only as a nuclear tRNA C5 (m5C) methyltransferase; the mRNA-methylation claim is weakly supported by computational ortholog inference (ISS) alone; and the rRNA-methylation, rRNA-processing, and mitochondrial-LSU-assembly claims are refuted as paralog carry-over from NSUN4.**

Three independent, *positive* lines of evidence — not just the absence of a positive assay — argue against the mitochondrial and rRNA claims. First, Trm4b is a **685-aa nuclear protein with no mitochondrial transit peptide**, essentially identical in size and architecture to its true 1:1 ortholog, *S. cerevisiae* Trm4/NCL1 (684 aa, nuclear/nucleolar), whose curated GO set is **tRNA-only**. Second, the enzyme that actually performs mitochondrial 12S rRNA C911 methylation and coordinates mitoribosome monosome (SSU+LSU) assembly is **NSUN4**, a short (~381–384 aa) protein bearing a mitochondrial transit peptide (residues 1–25). Third, although Trm4b, NSUN2, and NSUN4 all share PANTHER family **PTHR22808**, the seed's open question — whether the IBA "with" identifier MGI:1919431 is NSUN4 — is confirmed: **MGI:1919431 = *Nsun4***. The mitochondrial/rRNA signal thus enters Trm4b's record through shared-superfamily phylogenetic inference, not any *S. pombe* measurement.

The only non-tRNA function with a defensible rationale is **mRNA (cytidine-5-)-methyltransferase (GO:0062152)**, which sits on Trm4b as an **ISS projection from human NSUN2 (Q08J23)**. Because vertebrate NSUN2 does carry experimentally supported mRNA m5C activity, the projection is lineage-plausible — but it *skips* the yeast ortholog (ScTrm4/NCL1) that lacks mRNA activity entirely, making it a phylogenetically non-conservative, low-confidence inference. Recommended curation: retain the tRNA MF as core; keep GO:0062152 only as low-confidence ISS/non-core; add no rRNA or mitochondrial terms.

---

## Key Findings

### F001 — Trm4b's demonstrated function is restricted to tRNA C49/C50 m5C

The curated UniProt entry **TRM4B_SCHPO (O13935)** lists only tRNA substrates under FUNCTION and CATALYTIC ACTIVITY: 5-methylcytosine formation at **C49 and C50** ([PMID: 30646830](https://pubmed.ncbi.nlm.nih.gov/30646830/), ECO:0000269, experimental) and at C60/61/62 in tRNA-Asp ([PMID: 23074192](https://pubmed.ncbi.nlm.nih.gov/23074192/)). The primary tRNA-methylome paper states plainly that **"Trm4b methylates C49 and C50, which both lie in the TΨC-stem,"** and — critically for this hypothesis — **only the tRNA methylome was assayed**; there was no rRNA, mRNA, or mitochondrial substrate panel. PomBase records the experimental molecular function as **GO:0016428 tRNA (cytidine-N5)-methyltransferase** (IDA/IMP, PMID:30646830), and the deletion is viable.

This finding anchors the entire evaluation. The single high-quality experimental study behind Trm4b defines its *demonstrated* substrate as tRNA and its *demonstrated* sites as C49/C50. Consistent with the seed's framing, it neither tested nor excluded rRNA/mRNA — but it provides **zero positive support** for the rRNA/mRNA/mitochondrial extensions.

### F002 — The mitochondrial-ribosome / rRNA functions trace to NSUN4 (MGI:1919431) via paralog co-membership in PANTHER PTHR22808

PomBase's IBA (phylogenetic inference; GO_REF:0000033) provenance for trm4b's cytoplasm annotation (GO:0005737) uses a `with=` list of **MGI:1919431, MGI:107252, UniProtKB:Q08J23, PANTHER:PTN000516077**. Resolving these identifiers programmatically via mygene.info: **MGI:1919431 = *Nsun4*** and **MGI:107252 = *Nsun2***. The seed explicitly asked to verify — rather than assume — that MGI:1919431 is NSUN4; **this is now confirmed: MGI:1919431 is *Nsun4*.**

InterPro/PANTHER placement shows that Trm4b (O13935), **NSUN2** (human Q08J23 / mouse Q1HFZ0), **and NSUN4** (human Q96CB9 / mouse Q9CZ57) all map to **PTHR22808**, whereas **NSUN5** (Q96P11/Q8K4F6) and **NOP2/NSUN1** (P46087) map to a *separate* family, **PTHR22807**. Because NSUN4 co-resides in PTHR22808, tree-based propagation (IBA) can pull NSUN4-derived signals onto Trm4b even though NSUN4's function is compartmentally and mechanistically distinct. That NSUN4 function is well defined: **[PMID: 24516400](https://pubmed.ncbi.nlm.nih.gov/24516400/)** shows **"NSUN4 methylates cytosine 911 in 12S rRNA"** and that **"the NSUN4/MTERF4 complex is required to assemble the SSU and LSU to form a monosome."** The mito-rRNA and mitoribosome-assembly ideas in the seed are therefore **NSUN4-specific**, entering the record through shared-family inference, not a pombe measurement.

Reassuringly, an audit of Trm4b's actual IBA terms found that **mito/rRNA terms were not, in fact, propagated onto Trm4b** — only generic *cytoplasm* and *tRNA binding* were. NSUN5-type cytoplasmic rRNA m5C sits in a different family (PTHR22807) and cannot legitimately project onto Trm4b.

### F003 — Trm4b's mRNA (cytidine-5-)-methyltransferase annotation (GO:0062152) is an ISS ortholog projection from human NSUN2, not a *S. pombe* measurement

PomBase annotation **87463** assigns **GO:0062152 mRNA (cytidine-5-)-methyltransferase** with reference **GO_REF:0000024 (ISS)** and `with=` **UniProtKB:Q08J23** (**NSUN2_HUMAN**), assigned_by PomBase. Human NSUN2 (Q08J23) carries GO:0062152 by **IDA:UniProtKB** — i.e., the experimental anchor lives on the human protein and is *projected* onto Trm4b by sequence similarity (ISS). The review **[PMID: 42587746](https://pubmed.ncbi.nlm.nih.gov/42587746/)** notes that, of eight human m5C RNA methyltransferases, **"only two, NSUN2 and NSUN6, were found to be capable of modifying the main portion of cellular mRNAs,"** which rationalizes why an mRNA projection would come from NSUN2 while also emphasizing that bulk mRNA m5C is comparatively rare and restricted. Trm4b's subcellular location is **Nucleus** (HDA:PomBase, [PMID: 16823372](https://pubmed.ncbi.nlm.nih.gov/16823372/)) plus cytoplasm (IBA), with **no mitochondrial localization** — consistent with a nuclear tRNA/mRNA enzyme, not a mitochondrial one.

### F004 — Architecture and localization cleanly separate Trm4b from mitochondrial NSUN4

A direct UniProt feature comparison makes the paralog-confusion mechanism explicit:

| Protein | UniProt | Organism | Length (aa) | Mito transit peptide | Localization | PANTHER family | Known substrate/function |
|---|---|---|---|---|---|---|---|
| **Trm4b (this gene)** | O13935 | *S. pombe* | **685** | **None** | **Nucleus** (+cytoplasm IBA) | PTHR22808 | tRNA C49/C50 m5C (demonstrated) |
| Trm4/NCL1 (true ortholog) | P38205 | *S. cerevisiae* | 684 | None | Nucleus/nucleolus | PTHR22808 | tRNA m5C |
| NSUN2 (human) | Q08J23 | *H. sapiens* | 767 | None | Nucleus/nucleolus, cytoplasm | PTHR22808 | tRNA + mRNA m5C (IDA) |
| **NSUN4 (human)** | Q96CB9 | *H. sapiens* | **384** | **YES (1–25)** | **Mitochondrion** | PTHR22808 | mito 12S rRNA m5C + mitoribosome assembly |
| **NSUN4 (mouse)** | Q9CZ57 | *M. musculus* | **381** | **YES (1–25)** | **Mitochondrion** | PTHR22808 | mito 12S rRNA m5C + mitoribosome assembly |
| NSUN5 (human) | Q96P11 | *H. sapiens* | 429 | None | Nucleolus | **PTHR22807 (different family)** | cytoplasmic large-subunit rRNA m5C |

Trm4b (685 aa) is essentially the same length as ScTrm4/NCL1 (684 aa), the true 1:1 ortholog, and both are nuclear with **no transit peptide**. NSUN4, by contrast, is **roughly half the length** and carries a **mitochondrial transit peptide (residues 1–25)**, localizing to the mitochondrion. Because Trm4b lacks mitochondrial targeting entirely, the mito-LSU-assembly claim cannot be a direct Trm4b function. This is *positive* architectural evidence against the mitochondrial claim, exactly the kind of evidence the seed asks for — not merely the absence of a positive tRNA-C34 result.

### F005 — The true ortholog ScTrm4/NCL1 carries no rRNA/mRNA/mito functions, weakening the mRNA-ISS projection

A programmatic scan of the full GO set for **P38205 (*S. cerevisiae* Trm4/NCL1)** — the 1:1 experimentally characterized ortholog of Trm4b — returns **only tRNA-centric terms**: MF **GO:0016428** tRNA (cytidine-N5)-MTase (IDA:SGD) and **GO:0000049** tRNA binding (IDA:SGD); BP **GO:0030488** tRNA methylation, **GO:0002127** tRNA wobble cytosine methylation, **GO:0006400** tRNA modification, **GO:0070301** response to hydrogen peroxide; CC nucleus/nucleolus/nucleoplasm/cytoplasm. An explicit search for rRNA / mRNA / mitochondrion / ribosome terms returned **NONE**. The mRNA (cytidine-5-)-methyltransferase activity appears **only on vertebrate NSUN2 (Q08J23, IDA)** — not on the yeast ortholog. This is the strongest single argument that the mRNA-ISS annotation on Trm4b is a phylogenetically non-conservative, lineage-boundary projection: the closest experimentally characterized fungal relative shows tRNA specificity and no mRNA activity, implying mRNA m5C is a metazoan NSUN2-lineage innovation.

---

## Mechanistic Model / Interpretation

The evidence resolves into a clean model in which **one PANTHER superfamily (PTHR22808) contains functionally divergent m5C RNA methyltransferases**, and annotation-propagation machinery has partially blurred those boundaries onto Trm4b.

```
                      PANTHER PTHR22808  (m5C RNA methyltransferases)
        ┌───────────────────────────────┬────────────────────────────────┐
        │                               │                                │
   Trm4/NSUN2 clade                 NSUN4 clade                     (vertebrate
   (nuclear, tRNA/mRNA)            (mito, 12S rRNA)                  expansion)
        │                               │
  ┌─────┴─────┐                    ┌────┴─────┐
  │           │                    │          │
ScTrm4      Trm4b (O13935)      Human/Mouse NSUN4
(P38205)    685 aa, NUCLEAR     ~381–384 aa, MITO transit pep
684 aa      no transit pep      → 12S rRNA C911 m5C
tRNA-ONLY   tRNA C49/C50 m5C    → MTERF4 complex → mitoribosome
            (PMID:30646830)       SSU+LSU monosome assembly
                │                   (PMID:24516400)
                │
   Human NSUN2 (Q08J23): tRNA + mRNA m5C (IDA)
                │  ISS projection (GO_REF:0000024, with=Q08J23)
                ▼
   Trm4b GO:0062152 mRNA (cytidine-5-)-MTase  ← weak, non-core

   Separate family PTHR22807: NSUN5 (large-subunit rRNA), NOP2/NSUN1 (rRNA)
   → NOT the source of the trm4b annotations
```

**Direct, demonstrated Trm4b activity:** SAM-dependent 5-methylcytosine deposition on **tRNA at C49/C50** (and C60–62 in tRNA-Asp), acting as a **nuclear tRNA (cytidine-N5)-methyltransferase** (class I Rossmann-fold MTase, NOL1/NOP2/SUN domain). This is the primary molecular function.

**Inferred, non-core:** **mRNA C5 methylation (GO:0062152)** — plausible at the lineage level because human NSUN2 has this activity, but supported only by ISS from a *human* paralog and *absent* from the true fungal ortholog. Best treated as low-confidence inference.

**Not supported (paralog carry-over):** **rRNA methylation, rRNA processing, and mitochondrial LSU assembly.** These are NSUN4 (mito 12S rRNA) and, in a *different* family, NSUN5/NOP2 functions. They reach Trm4b only through shared-superfamily phylogenetic inference (IBA `with=MGI:1919431`=Nsun4) and are contradicted by Trm4b's nuclear, non-mito architecture.

The key discriminator is **subcellular targeting plus ortholog identity**. A mitochondrial LSU-assembly role requires a mitochondrial protein; Trm4b has no transit peptide and is nuclear. A cytoplasmic rRNA-processing role requires a nucleolar rRNA MTase (NSUN5/NOP2, family PTHR22807 — not Trm4b's family). Trm4b fits neither.

---

## Evidence Base

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 30646830](https://pubmed.ncbi.nlm.nih.gov/30646830/) | Direct assay (RNA-BS-seq + in vitro) | Supports tRNA; qualifies rRNA/mRNA | Trm4b substrate/site specificity | Trm4b methylates tRNA **C49/C50** (TΨC-stem); Trm4a does C48/C34; **only the tRNA methylome was assayed** | *S. pombe*, in vivo + in vitro | High for tRNA; **silent** on rRNA/mRNA/mito |
| [PMID: 23074192](https://pubmed.ncbi.nlm.nih.gov/23074192/) | Direct assay | Supports tRNA | Additional Trm4b tRNA sites | m5C at C60/61/62 in tRNA-Asp | *S. pombe* | High; tRNA only |
| [PMID: 16823372](https://pubmed.ncbi.nlm.nih.gov/16823372/) | Localization (HDA) | Refutes mito | Subcellular location | Trm4b localizes to **nucleus** (GFP ORFeome) | *S. pombe* | Med–High; no mitochondrial signal |
| UniProt O13935 (TRM4B_SCHPO) | Database (curated) | Refutes mito / qualifies | Curated function + architecture | 685 aa, no transit peptide, nucleus; only tRNA C5 MTase activities; mRNA term present **only as ISS** | Swiss-Prot | High as synthesis of primary data |
| UniProt Q96CB9 / Q9CZ57 (NSUN4) | Database (curated) | Refutes mito (contrast) | Architecture of NSUN4 | ~381–384 aa, **mito transit peptide 1–25**, mitochondrion | Human/mouse | High; contrasting architecture |
| UniProt P38205 (ScTrm4/NCL1) | Database (curated) | Refutes mRNA/rRNA extension | GO set of true ortholog | tRNA-only; **no** rRNA/mRNA/mito/ribosome terms | *S. cerevisiae* | High; programmatic scan |
| PomBase ann 87463 (GO_REF:0000024) | Computational (ISS) | Qualifies mRNA | GO:0062152 mRNA (C5) MTase | ISS `with=` **Q08J23 = human NSUN2** (which has GO:0062152 by IDA) | GO_Central / PomBase | Ortholog-inferred; **not demonstrated in *S. pombe*** |
| PomBase IBA (GO_REF:0000033) | Computational (IBA) | Competing / paralog | IBA with-list contents | with = **Nsun4 (MGI:1919431)** + Nsun2 (MGI:107252) + NSUN2 (Q08J23) + PANTHER node | GO_Central IBA | Only *cytoplasm* & *tRNA binding* propagated; mito/rRNA terms **NOT** propagated |
| mygene.info (ID mapping) | Computational | Competing | Identity of MGI:1919431 | **MGI:1919431 = Nsun4**; MGI:107252 = Nsun2 | Mouse / MGI | High — resolves seed's open question |
| InterPro / PANTHER | Structural / evolutionary | Competing / qualifies | Paralog family membership | Trm4b, NSUN2, **NSUN4** → **PTHR22808**; NSUN5 & NOP2/NSUN1 → **PTHR22807** | Cross-species | High; NSUN5 rRNA m5C cannot project onto Trm4b |
| [PMID: 24516400](https://pubmed.ncbi.nlm.nih.gov/24516400/) | Mutant phenotype + direct assay | Competing (paralog) | NSUN4 function | NSUN4 methylates **12S rRNA C911**; with **MTERF4** coordinates mitoribosome monosome assembly | Mouse mitochondria | High; establishes mito functions as **NSUN4-specific** |
| [PMID: 42587746](https://pubmed.ncbi.nlm.nih.gov/42587746/) | Review | Qualifies mRNA | Which MTases modify mRNA | Of 8 human m5C MTases, "only two, **NSUN2 and NSUN6**" modify bulk mRNA; mRNA m5C is comparatively rare | Human | Review-level orientation |

---

## GO Curation Implications

**Leads requiring curator verification:**

1. **GO:0016428 tRNA (cytidine-N5)-methyltransferase activity (MF) — RETAIN (core).** Experimentally supported (IDA/IMP, PMID:30646830). Ensure the annotation captures C49/C50 site specificity.
2. **tRNA methylation BP terms — RETAIN**, but re-examine **GO:0002127 (tRNA wobble base C34 cytosine methylation)** on Trm4b: PMID:30646830 assigns C34 methylation to the paralog **Trm4a**, so this BP term may belong to Trm4a, not Trm4b.
3. **GO:0062152 mRNA (cytidine-5-)-methyltransferase activity (MF) — RETAIN WITH CAVEAT / mark non-core.** Keep the **ISS** evidence code and `with=` (Q08J23); do **not** upgrade to an experimental code. Add a curator note that *S. pombe* splits Trm4 into Trm4a/Trm4b and that the true fungal ortholog ScTrm4/NCL1 lacks mRNA activity, making this a phylogenetically non-conservative projection.
4. **rRNA methylation / rRNA processing (e.g., GO:0031167, GO:0006364) — DO NOT ADD.** No positive evidence; canonical rRNA m5C (NSUN5/NOP2) is in a different PANTHER family (PTHR22807).
5. **Mitochondrial LSU assembly / mito rRNA methylation / mitochondrial translation (e.g., GO:0000466, GO:0032543) — DO NOT ADD.** These are NSUN4-specific; Trm4b is nuclear/cytoplasmic with no transit peptide. Any such term appearing via IBA is paralog-conflation and should be removed or NOT-qualified.
6. **CC:** *nucleus* (HDA, PMID:16823372) and *cytoplasm* (IBA) are appropriate; **no mitochondrion** term is supported.

"Protein binding" is not needed as a fallback — the informative, well-supported MF is the tRNA C5-methyltransferase activity.

---

## Mechanistic Scope

- **Direct molecular activity:** SAM-dependent cytosine-C5 methyltransferase acting on **tRNA** at C49/C50 (and C60–62 in tRNA-Asp); nuclear.
- **Inferred (ortholog) activity:** mRNA C5 methylation, by analogy to human NSUN2 — a molecular activity (not a downstream phenotype), but unverified in *S. pombe* and absent from the yeast ortholog.
- **Not the gene product's function (downstream/paralog):** mitochondrial 12S rRNA methylation and mitoribosome (SSU/LSU) assembly are **NSUN4** activities; large-subunit cytoplasmic rRNA m5C is an **NSUN5** activity. Neither belongs to Trm4b. No *S. pombe* loss-of-function phenotype implicates Trm4b in rRNA maturation or mitoribosome assembly (the deletion is viable), so the rRNA/mito claims lack even loss-of-function support.

---

## Conflicts and Alternatives

- **Paralog confusion (primary alternative):** NSUN4 (MGI:1919431) co-resides with Trm4b in PTHR22808, so propagation of NSUN4's mito-rRNA/LSU-assembly terms would be a family-level (IBA) artifact, not a real Trm4b function. Confirmed: **MGI:1919431 is *Nsun4*.**
- **Family boundary protects against rRNA over-annotation:** the canonical rRNA-m5C enzymes NSUN5 and NOP2/NSUN1 are in **PTHR22807**, distinct from Trm4b's **PTHR22808** — rRNA-processing terms cannot legitimately reach Trm4b by orthology.
- **Sub-functionalization:** *S. pombe* uniquely splits Trm4/NSUN2 into Trm4a and Trm4b (PMID:30646830). A human-NSUN2-based ISS (mRNA activity) may map to Trm4a, Trm4b, both, or neither — a real organism-specific caveat for the mRNA term.
- **Node discrepancy:** the seed cites PANTHER node **PTN000516076**; the actual PomBase with-refs use **PTN000516077**. Both are ancestral nodes within PTHR22808; not decision-changing, but worth verifying against the current PANTHER tree.
- **In-vitro / cross-species extrapolation:** even NSUN2's mRNA activity is a mammalian in-vivo finding; extrapolating substrate breadth across ~1 billion years of divergence to fission yeast is speculative.

No evidence was found that *supports* the seed's rRNA/mito extensions over the paralog-confusion alternative.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No direct rRNA/mRNA methylation assay for Trm4b in *S. pombe* | UniProt, PomBase, PMID:30646830/23074192 — none test non-tRNA substrates | "Refuted" = annotations unjustified + paralog-explained, not biochemically impossible | RNA-bisulfite-seq / m5C-MeRIP on *trm4bΔ* vs WT (tRNA-depleted) total RNA |
| Trm4a vs Trm4b division of any mRNA activity | Not addressed by any study | Determines which paralog (if any) the mRNA ISS represents | Compare *trm4aΔ* and *trm4bΔ* mRNA m5C profiles |
| PANTHER node curation (PTN000516076 vs 077) and which descendants anchor which terms | With-lists inspected; full tree annotations not audited | Predicts future IBA over-propagation | Inspect PTHR22808 GO annotation tree |
| Formal mitochondrial-targeting prediction | UniProt reports nucleus only; TargetP/MitoFates not run this iteration | Fully excludes a mito role computationally | Run TargetP/MitoFates on O13935 |
| Structural confirmation of substrate pocket | Length/domain architecture compared; no structure solved here | Could show tRNA-elbow vs mRNA/rRNA preference | AlphaFold model + comparison to NSUN2/NSUN4 target-recognition domains |

---

## Discriminating Tests

1. **RNA bisulfite sequencing** of *trm4bΔ* vs WT *S. pombe* on rRNA and (tRNA-depleted) mRNA — directly tests rRNA/mRNA m5C dependence on Trm4b. *Most decisive single experiment.*
2. **Mitochondrial fractionation + GFP imaging** to confirm Trm4b is excluded from mitochondria (predicted: excluded), formally closing the mito-LSU claim.
3. **In vitro methylation** of rRNA/mRNA substrates by recombinant Trm4b (predicted: little/no activity vs strong tRNA activity).
4. **Ortholog complementation:** test whether human NSUN2 (mRNA-competent) but not NSUN4 rescues *trm4bΔ*, and whether Trm4b rescues *ScTrm4Δ*.
5. **Polysome/mitoribosome profiling** in *trm4bΔ* (predicted: no mitoribosome-assembly defect).
6. **Comparative PANTHER-tree audit** of PTHR22808 to confirm mito/rRNA terms are anchored below the Trm4b/NSUN2 ancestor (predicted: yes — hence no legitimate IBA propagation).

---

## Proposed Follow-up Actions / Curation Leads

**Leads requiring curator verification:**

- **Reference to verify (core tRNA function):** [PMID: 30646830](https://pubmed.ncbi.nlm.nih.gov/30646830/) — snippet: *"Trm4b methylates C49 and C50, which both lie in the TΨC-stem."* Supports the retained tRNA MF and shows only tRNA was assayed.
- **Reference to verify (mRNA ISS basis):** UniProtKB:Q08J23 (human NSUN2), which carries GO:0062152 by IDA — supports keeping GO:0062152 as **ISS**, not experimental.
- **Reference to verify (paralog distinction):** [PMID: 24516400](https://pubmed.ncbi.nlm.nih.gov/24516400/) — snippets: *"NSUN4 methylates cytosine 911 in 12S rRNA"* and *"the NSUN4/MTERF4 complex is required to assemble the SSU and LSU to form a monosome."* Grounds the mito-LSU-assembly function in NSUN4, not Trm4b.
- **Reference to verify (mRNA competence is lineage-restricted):** [PMID: 42587746](https://pubmed.ncbi.nlm.nih.gov/42587746/) — snippet: *"only two, NSUN2 and NSUN6, were found to be capable of modifying the main portion of cellular mRNAs."*

**Candidate action changes:**
- Retain tRNA MF/BP; retain mRNA-ISS only with a low-confidence/non-core caveat; **do not add** any rRNA-processing, mito-rRNA-methylation, or mitochondrial-LSU-assembly term.
- If such terms already appear via IBA, treat as **paralog carry-over** and remove or NOT-qualify.
- Re-examine GO:0002127 (wobble C34) on Trm4b, since PMID:30646830 assigns C34 methylation to **Trm4a**.

**Suggested curator question:** "Is the mRNA-MTase ISS meant to represent Trm4b specifically, given *S. pombe*'s Trm4a/Trm4b split, or is it a genus-level NSUN2 projection that skips the yeast ortholog lacking the activity?"

**Suggested experiment:** *trm4bΔ* RNA-BS-seq on rRNA + mRNA (definitive test of the entire hypothesis).

---

## Bottom Line

Trm4b (O13935) is well supported **only** as a **nuclear tRNA C5 (m5C) methyltransferase** acting at tRNA C49/C50. The hypothesis's rRNA-methylation, rRNA-processing, and mitochondrial-LSU-assembly extensions have **no positive experimental support in any organism** and are best explained as **paralog carry-over from NSUN4** (confirmed MGI:1919431 = *Nsun4*) via shared PANTHER family PTHR22808 — contradicted by Trm4b's 685-aa nuclear, transit-peptide-free architecture that matches the tRNA-only ortholog ScTrm4/NCL1. The only non-tRNA annotation with a defensible rationale — **mRNA (cytidine-5-)-methyltransferase (GO:0062152)** — is a **weak ISS projection from human NSUN2** that even the yeast ortholog lacks, and should be retained only as low-confidence, non-core inference; **no rRNA or mitochondrial terms should be added.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)