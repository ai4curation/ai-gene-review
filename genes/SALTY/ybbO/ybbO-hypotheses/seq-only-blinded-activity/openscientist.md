---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T17:33:01.119540'
end_time: '2026-10-30T17:57:31.949027'
duration_seconds: 1470.83
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SALTY
  gene: query_protein
  gene_symbol: WITHHELD
  uniprot_accession: WITHHELD
  taxon_id: NCBITaxon:99287
  taxon_label: Salmonella enterica subsp. enterica serovar Typhimurium str. LT2
  focus_type: function_assignment
  hypothesis_slug: seq-only-blinded-activity
  hypothesis_text: Sequence-only blinded test. The query protein (sequence below;
    gene name and accession deliberately withheld) is an NADPH-dependent aldehyde
    reductase that reduces aliphatic aldehydes to primary alcohols (GO:0008106 alcohol
    dehydrogenase (NADP+) activity). Using only the sequence and public bioinformatics
    resources, determine its family, whether the catalytic machinery is intact, its
    most likely specific activity and substrate class, and whether the stated hypothesis
    is supported, needs narrowing, or should be replaced by a competing activity (e.g.
    hydroxysteroid or retinol dehydrogenase).
  term_context: '- Term: alcohol dehydrogenase (NADP+) activity (GO:0008106)

    - Query protein sequence (FASTA, 256 aa):

    >query

    MQKSVLITGCSSGIGLDSALELKRQGFQILAGCRKPDDVARMNSMGFTGVLIDLDSPESVDRAADEVIALTDNRLYGIFNNAGYGVYGPLSTISREQMEQQFSSNFFGAHQLTMRLLPAMLPHGEGRIVMTSSVMGLISTPGRGAYAASKYALEAWSDALRMELRHTGIKVSLIEPGPIRTRFTDNVNQTQRDKPVENPGIAARFTRDPDAVVAKVRHAFASDKPRLRYPVTLVTWAVMALKRILPGRMLDKILQS'
  reference_context: No reference context supplied (blinded).
  source_file: WITHHELD
  source_selector: free-text
  source_context_yaml: 'blinded: true'
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
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
artifacts:
- filename: artifacts_analysis_provenance.md
  path: openscientist_artifacts/artifacts_analysis_provenance.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist analysis provenance
- filename: artifacts_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: artifacts_go_decision_table.csv
  path: openscientist_artifacts/artifacts_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
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

- **Organism code:** SALTY
- **Taxon:** Salmonella enterica subsp. enterica serovar Typhimurium str. LT2 (NCBITaxon:99287)
- **Gene directory:** query_protein
- **Gene symbol:** WITHHELD
- **UniProt accession:** WITHHELD

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** seq-only-blinded-activity
- **Source file:** WITHHELD
- **Source selector:** free-text

## Seed Hypothesis

Sequence-only blinded test. The query protein (sequence below; gene name and accession deliberately withheld) is an NADPH-dependent aldehyde reductase that reduces aliphatic aldehydes to primary alcohols (GO:0008106 alcohol dehydrogenase (NADP+) activity). Using only the sequence and public bioinformatics resources, determine its family, whether the catalytic machinery is intact, its most likely specific activity and substrate class, and whether the stated hypothesis is supported, needs narrowing, or should be replaced by a competing activity (e.g. hydroxysteroid or retinol dehydrogenase).

## Term and Decision Context

- Term: alcohol dehydrogenase (NADP+) activity (GO:0008106)
- Query protein sequence (FASTA, 256 aa):
>query
MQKSVLITGCSSGIGLDSALELKRQGFQILAGCRKPDDVARMNSMGFTGVLIDLDSPESVDRAADEVIALTDNRLYGIFNNAGYGVYGPLSTISREQMEQQFSSNFFGAHQLTMRLLPAMLPHGEGRIVMTSSVMGLISTPGRGAYAASKYALEAWSDALRMELRHTGIKVSLIEPGPIRTRFTDNVNQTQRDKPVENPGIAARFTRDPDAVVAKVRHAFASDKPRLRYPVTLVTWAVMALKRILPGRMLDKILQS

## Reference Context

No reference context supplied (blinded).

## Source Context YAML

```yaml
blinded: true
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

## Blinded Sequence-Only Functional Assignment: Salmonella Typhimurium LT2 *ybbO* (Q7CR11)

**Focus type:** function_assignment · **Hypothesis slug:** seq-only-blinded-activity
**Term under evaluation:** alcohol dehydrogenase (NADP+) activity — **GO:0008106**
**Organism:** *Salmonella enterica* subsp. *enterica* serovar Typhimurium str. LT2 (NCBITaxon:99287)

---

## Executive Judgment

**Verdict: SUPPORTED (as an evidence-transfer / ISS–ISO curation lead).**

Starting only from the 256-amino-acid query sequence with gene name and accession deliberately withheld, this investigation established the protein's identity, family, catalytic integrity, and most likely specific activity, and tested the seed hypothesis against competing activities (hydroxysteroid dehydrogenase, retinol dehydrogenase).

The blinded query was de-anonymized by an exact UniParc CRC64 checksum match to **Salmonella Typhimurium LT2 gene *ybbO* (UniProt Q7CR11)**. The protein is a textbook **classical short-chain dehydrogenase/reductase (SDR)**: Pfam **PF00106**, InterPro **IPR002347**, PROSITE **PS00061**, with the Rossmann-fold NAD(P)-binding superfamily signature. Its closest experimentally characterized relative is *Escherichia coli* K-12 **YbbO (P0AFP4)**, to which it is **90.6% identical over 256 aa** with **100% conservation of the catalytic tetrad and the NADP(+)-selecting basic residues**. *E. coli* YbbO carries exactly the seed GO term — **GO:0008106 "alcohol dehydrogenase (NADP+) activity"** — supported by **two independent direct-assay (IDA) primary papers** ([PMID: 25108218](https://pubmed.ncbi.nlm.nih.gov/25108218/) and [PMID: 27134112](https://pubmed.ncbi.nlm.nih.gov/27134112/)).

The seed hypothesis — "NADPH-dependent aldehyde reductase that reduces aliphatic aldehydes to primary alcohols" — is therefore **supported with high confidence and can be narrowed precisely**: the preferred substrate class is **medium-to-long-chain aliphatic aldehydes (C6–C18, optimal C16/C18)**. The two competing activities were evaluated and resolved: the **hydroxysteroid dehydrogenase (HSD) alternative is refuted** — it is a CDD subfamily-naming artifact (cd05374), not substrate evidence — and the **retinol dehydrogenase activity is real but promiscuous and non-native**, since neither *Salmonella* nor *E. coli* has an endogenous retinoid pathway. **Most important caveat:** the *Salmonella* ortholog itself has **not been directly assayed**; all enzymatic evidence comes from the *E. coli* ortholog. The correct curation action is therefore an **ISS/ISO evidence transfer**, not an assertion of direct assay (IDA) on Q7CR11.

---

## Key Findings

### F001 — Identity: the blinded query is Salmonella LT2 YbbO (Q7CR11), 91% identical to assay-characterized *E. coli* YbbO

The 256-residue query sequence was identified by an **exact UniParc CRC64 checksum match** (checksum `22B5C5A48E6D813A` → `UPI000005A1DF`), which uniquely maps the sequence to **Salmonella Typhimurium LT2 gene *ybbO* (UniProtKB Q7CR11)**. This is a deterministic identity match, not a similarity inference.

The nearest reviewed, experimentally characterized homolog is **E. coli K-12 YbbO (P0AFP4, 269 aa)**, which carries a 13-residue N-terminal extension relative to the query. After accounting for that offset, the ungapped identity is **90.6% over 256 aa**. The cofactor-binding glycine-rich loop and catalytic region are visibly conserved (query `LITGCSSGIGL…LAGCRKPDD` vs *E. coli* `LITGCSSGIGL…LAGCRKPDD`). *E. coli* YbbO is annotated **GO:0008106 "alcohol dehydrogenase (NADP+) activity"** with evidence code **IDA:EcoCyc** (direct assay). Because the deletion of *ybbO* in *E. coli* caused a **>90% reduction in long-chain fatty alcohol production** ([PMID: 27134112](https://pubmed.ncbi.nlm.nih.gov/27134112/)), the ortholog's role as an NADP(+)-dependent aldehyde reductase is directly established, and the query is its very close homolog.

### F002 — Specific activity: broad-specificity NADPH aldehyde reductase (aliphatic C6–C18, optimal C16/C18); retinal reduction is promiscuous; no hydroxysteroid activity

Enzyme kinetics of *E. coli* YbbO show a **wide aldehyde substrate specificity ranging from C6 to C18**, with **maximum affinity and catalytic efficiency for C18 and C16 chain-length aldehydes** ([PMID: 27134112](https://pubmed.ncbi.nlm.nih.gov/27134112/)). An independent functional screen identified YbbO among **five new aldehyde reductases (ALRs)** — YahK, DkgA, GldA, YbbO, and YghA — that convert aldehydes to the corresponding alcohols ([PMID: 25108218](https://pubmed.ncbi.nlm.nih.gov/25108218/)). These two lines of direct evidence converge on **aliphatic aldehydes as the preferred substrate class**, precisely matching the seed hypothesis once narrowed to medium/long-chain aliphatic aldehydes.

Several metabolic-engineering studies show that *ybbO* also reduces **retinal to retinol** ([PMID: 25726762](https://pubmed.ncbi.nlm.nih.gov/25726762/), [PMID: 34850377](https://pubmed.ncbi.nlm.nih.gov/34850377/), [PMID: 39307776](https://pubmed.ncbi.nlm.nih.gov/39307776/), [PMID: 41093029](https://pubmed.ncbi.nlm.nih.gov/41093029/)). However, in those systems **retinal remains a major product** ([PMID: 34850377](https://pubmed.ncbi.nlm.nih.gov/34850377/)), indicating retinal is an **inefficient, promiscuous, non-native substrate** rather than the physiological one. Neither *Salmonella* nor *E. coli* possesses an endogenous retinoid biosynthetic pathway, so retinol dehydrogenase cannot be the gene's native function. There is **no sequence or literature evidence for hydroxysteroid or dedicated retinol dehydrogenase classification**.

### F003 — Annotation provenance: two independent IDA papers underpin GO:0008106; the Salmonella ortholog lacks it; InterPro = classical SDR; the HSD label is a CDD artifact

QuickGO shows that *E. coli* YbbO (P0AFP4) is annotated **GO:0008106 "alcohol dehydrogenase (NADP+) activity"** with evidence **IDA (ECO:0000314)** from **two primary references**: [PMID: 25108218](https://pubmed.ncbi.nlm.nih.gov/25108218/) and [PMID: 27134112](https://pubmed.ncbi.nlm.nih.gov/27134112/). By contrast, the Salmonella ortholog **Q7CR11 currently carries only GO:0016491** (oxidoreductase, evidence **IBA ECO:0000318**, PANTHER PTN000672121) — confirming the seed term has **not yet been propagated** to the query protein.

InterPro assigns Q7CR11 unambiguously to the **classical SDR family**:

| Resource | Identifier | Interpretation |
|---|---|---|
| Pfam | PF00106 | SDR family |
| InterPro | IPR002347 + IPR020904 | SDR family + conserved active-site |
| PROSITE | PS00061 | SDR active-site signature |
| PANTHER | PTHR43313 | SDR subfamily |
| NCBIfam | NF005950 | SDR |
| Superfamily / CATH-Gene3D | SSF51735 / G3DSA:3.40.50.720 | Rossmann-fold NAD(P)-binding |
| CDD | cd05374 | "17β-HSD-like, classical (c) SDRs" (**broad cluster, named after a representative**) |

Critically, the **CDD cd05374 assignment is a broad classical-SDR cluster named after a representative member (17β-HSD-like)** — it is **not evidence that YbbO acts on steroid substrates**. This resolves the "hydroxysteroid dehydrogenase" competing hypothesis as a **naming artifact**.

### F004 — Catalytic integrity: 100% conservation of the SDR catalytic tetrad and NADP-binding residues justifies maximal functional transfer

Residue-level alignment of Salmonella Q7CR11 against *E. coli* P0AFP4 (offset +13) shows **identity at every functionally critical position**:

| Functional element | Residue(s) (query numbering) | Status |
|---|---|---|
| Catalytic Asn | Asn81 | Conserved |
| Catalytic Ser pair | Ser132 / Ser133 | Conserved |
| Catalytic Tyr (YxxxK) | Tyr146 | Conserved |
| Catalytic Lys (YxxxK) | Lys150 | Conserved |
| NADP 2′-phosphate basic pair | Arg34 / Lys35 | Conserved |
| Glycine-rich cofactor loop | Thr8 (TGxxxGxG region) | Conserved |

The catalytic signature region `GAYAASKYA` (containing the Tyr–x–x–x–Lys motif diagnostic of SDR catalysis) is identical between the two proteins. The **Arg34/Lys35** pair is the hallmark of **NADPH preference** in the SDR family — the structural literature establishes that a conserved pair of basic residues contacting the cofactor 2′-phosphate confers NADPH over NADH selectivity ([PMID: 8805511](https://pubmed.ncbi.nlm.nih.gov/8805511/)). With overall identity of **90.6%** and **100% catalytic/cofactor conservation**, the conditions for confident ortholog-based functional transfer (ISS/ISO) are maximally satisfied.

---

## Mechanistic Model / Interpretation

### Reaction catalyzed (native, inferred)

```
   R–CHO  +  NADPH  +  H⁺   ⇌   R–CH₂OH  +  NADP⁺
 (aliphatic                      (primary
  aldehyde,                       alcohol)
  C6–C18;
  optimal C16/C18)
```

The enzyme is a cytoplasmic, NADPH-dependent **aliphatic aldehyde reductase** operating in the thermodynamically favorable reductive direction (aldehyde → alcohol). Its physiological role in the native organism is best understood as **aldehyde detoxification / reductive metabolism of reactive aliphatic aldehydes**, consistent with *E. coli* YbbO's contribution to fatty alcohol production from fatty aldehyde intermediates.

### SDR catalytic logic

```
        NADPH (2'-P recognized by Arg34 / Lys35)
                     │ hydride (4-pro-S)
                     ▼
   Tyr146 (general acid) ── Ser132/133 (substrate positioning)
        │                      │
        └── Lys150 lowers Tyr pKa, binds nicotinamide ribose
                     │
             Asn81 — part of proton-relay to bulk solvent
                     ▼
            R–CHO carbonyl protonated → R–CH₂OH
```

The query possesses the complete, canonical catalytic apparatus of classical SDRs (Asn–Ser–Tyr–Lys tetrad plus the Rossmann glycine-rich cofactor loop) with no substitutions at any catalytic position. The NADP-selecting Arg/Lys pair explains the enzyme's NADPH (not NADH) cofactor preference, consistent with the seed hypothesis and with the structural determinants documented for NADPH-preferring SDRs ([PMID: 8805511](https://pubmed.ncbi.nlm.nih.gov/8805511/)).

### Substrate-class reasoning and disambiguation of competing hypotheses

| Candidate activity | Evidence for | Evidence against | Verdict |
|---|---|---|---|
| **Aliphatic aldehyde reductase (seed)** | Direct kinetics C6–C18, optimal C16/C18 (PMID 27134112); ALR screen (PMID 25108218); 100% catalytic conservation | — | **Supported; narrow to C6–C18 aliphatic** |
| **Retinol dehydrogenase (competing)** | *ybbO* reduces retinal → retinol in engineered strains (PMID 25726762, 34850377, 39307776, 41093029) | Retinal remains major product (inefficient); no native retinoid pathway in *Salmonella*/*E. coli* | **Promiscuous, non-native side activity; not core** |
| **Hydroxysteroid dehydrogenase (competing)** | CDD cd05374 name "17β-HSD-like" | Cluster named after representative only; no steroid-substrate data; no steroid metabolism context | **Refuted (naming artifact)** |

The mechanistic conclusion is that **GO:0008106 captures the primary molecular function**, best specified as reduction of aliphatic aldehydes to primary alcohols; retinol dehydrogenase activity is a downstream in vitro curiosity exploited by metabolic engineers, and hydroxysteroid dehydrogenase activity is unsupported.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies/Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 27134112](https://pubmed.ncbi.nlm.nih.gov/27134112/) | Direct assay + mutant phenotype | **Supports** | YbbO is an NADP(+)-dependent aldehyde reductase on aliphatic aldehydes | Δ*ybbO* caused >90% drop in long-chain fatty alcohol; kinetics C6–C18, optimal C16/C18 | *E. coli*, in vitro + in vivo | High; characterizes *E. coli* ortholog, not Salmonella |
| [PMID: 25108218](https://pubmed.ncbi.nlm.nih.gov/25108218/) | Direct assay (functional screen) | **Supports** | YbbO reduces aldehydes to alcohols | Identified YbbO among 5 new aldehyde reductases (YahK, DkgA, GldA, YbbO, YghA) | *E. coli* | High; second independent IDA reference for GO:0008106 |
| [PMID: 34850377](https://pubmed.ncbi.nlm.nih.gov/34850377/) | Direct assay (heterologous) | **Qualifies / competing** | Retinol dehydrogenase activity | *E. coli ybbO* increases retinol, but retinal remains major product | Engineered *S. cerevisiae*/*E. coli* | Moderate; shows retinal reduction is inefficient/promiscuous |
| [PMID: 25726762](https://pubmed.ncbi.nlm.nih.gov/25726762/) | Direct assay (heterologous) | **Qualifies / competing** | Retinal → retinol by *ybbO* | *ybbO* is the promiscuous enzyme producing retinol; no native retinoid pathway in *E. coli* | Engineered *E. coli* | Moderate; confirms non-native side activity |
| [PMID: 39307776](https://pubmed.ncbi.nlm.nih.gov/39307776/) | Direct assay (heterologous) | **Qualifies / competing** | Retinal reductase efficiency | *ybbO* gave highest retinol conversion (95.6%) among screened ADHs | Engineered *S. cerevisiae* | Moderate; applied/engineering context |
| [PMID: 41093029](https://pubmed.ncbi.nlm.nih.gov/41093029/) | Mutant phenotype (heterologous) | **Qualifies / competing** | *ybbO* reduces retinal | Knocking out *ybbO* prevents retinal loss (to retinol) | Engineered *E. coli* BL21 | Moderate; confirms aldehyde-reductase promiscuity |
| [PMID: 8805511](https://pubmed.ncbi.nlm.nih.gov/8805511/) | Structural/evolutionary | **Supports** | NADPH selectivity determinants in SDRs | Conserved basic pair (Lys/Arg) binds cofactor 2′-phosphate → NADPH preference | Mouse lung carbonyl reductase (SDR) | High; explains query's Arg34/Lys35 NADPH preference |
| [PMID: 9525918](https://pubmed.ncbi.nlm.nih.gov/9525918/) | Structural/evolutionary | **Qualifies** | SDR cofactor/substrate specificity architecture | 17β-HSD1 shows SDR cofactor logic; steroid specificity depends on dedicated residues (His221) absent context here | Human 17β-HSD1 | High for family logic; shows HSD identity needs dedicated steroid-binding residues not implied by cd05374 |
| UniParc / UniProt (Q7CR11; P0AFP4) | Computational/database | **Supports (identity)** | Query identity & current annotation state | Exact CRC64 match → Salmonella *ybbO* Q7CR11; carries only GO:0016491 (IBA); *E. coli* P0AFP4 carries GO:0008106 (IDA ×2) | Database | High for identity; shows seed term not yet propagated |
| InterPro / Pfam / PROSITE / CDD | Computational/database | **Supports family; refutes HSD** | Family & catalytic-site assignment | PF00106 / IPR002347 classical SDR; cd05374 is a broad cluster named "17β-HSD-like," not steroid-substrate evidence | Database | High; disambiguates the HSD naming artifact |

---

## GO Curation Implications

**Lead curation action (requires curator verification):** **Add GO:0008106 "alcohol dehydrogenase (NADP+) activity" to Salmonella YbbO (Q7CR11) as an ISS/ISO evidence-transfer annotation**, with `with/from = UniProtKB:P0AFP4` (the directly-assayed *E. coli* ortholog), citing the two IDA references that anchor the ortholog term.

| Field | Recommendation |
|---|---|
| **Term** | GO:0008106 — alcohol dehydrogenase (NADP+) activity (**MF**) |
| **Action** | **Add / retain** on Q7CR11 (currently only GO:0016491 oxidoreductase IBA) |
| **Evidence code** | **ISS (ECO:0000250)** or **ISO (ECO:0000266)** — sequence/ortholog transfer |
| **With/From** | UniProtKB:P0AFP4 |
| **Supporting refs** | PMID 25108218, PMID 27134112 (IDA on ortholog) |
| **Do NOT assert** | IDA on Q7CR11 (Salmonella protein not directly assayed) |
| **Reject** | Hydroxysteroid dehydrogenase MF (CDD naming artifact) |
| **Treat as non-core** | Retinol dehydrogenase activity (promiscuous, non-native) |

- The term supports a **Molecular Function (MF)** assignment. GO:0008106 should be **retained/added** as the most informative MF term; the generic **GO:0016491 (oxidoreductase, IBA)** currently on Q7CR11 is correct but **less specific** and can be refined.
- A **more specific child term** describing aliphatic/long-chain aldehyde reductase activity would best capture the kinetics (C6–C18, optimal C16/C18) if an appropriate GO term exists; otherwise GO:0008106 is the best-supported node.
- **Biological Process:** a lead-level BP annotation to **aldehyde catabolism / detoxification** is plausible but not directly demonstrated in *Salmonella*; flag as a question for the curator rather than asserting.
- **Cellular Component:** cytoplasm (consistent with soluble SDR); low priority, inferable but not experimentally pinned for the query.
- **"protein binding"** is not an appropriate recommendation here — a specific catalytic MF term is well supported.

---

## Mechanistic Scope

The **immediate molecular function** being tested is a catalytic, NADPH-dependent hydride transfer that reduces the carbonyl of an **aliphatic aldehyde to a primary alcohol**. This is a direct gene-product activity grounded in: (1) complete conservation of the SDR catalytic tetrad and NADP-selecting residues in the query, and (2) direct in vitro kinetics plus a loss-of-function metabolic phenotype on the near-identical *E. coli* ortholog.

The following are explicitly **downstream, pleiotropic, or context-specific** and must not be conflated with the core MF:
- **Fatty alcohol production** (a pathway consequence observed when YbbO acts on fatty aldehyde intermediates in engineered strains).
- **Retinol production** (a non-native, promiscuous reduction exploited only in engineered β-carotene/retinoid strains; absent any native retinoid pathway).
- Any **biocide-tolerance phenotypes** (e.g., glutaraldehyde tolerance) are organism/stress-response phenomena and are not evidence that YbbO's core function is glutaraldehyde reduction.

The seed hypothesis correctly targets the **direct molecular activity**, and the evidence supports it at the activity level while allowing precise substrate narrowing.

---

## Conflicts and Alternatives

1. **Retinol dehydrogenase (competing activity).** Multiple engineering papers report *ybbO*-mediated retinal → retinol conversion, and one screen even ranked *ybbO* highest among tested alcohol dehydrogenases for this reaction (95.6% conversion; [PMID: 39307776](https://pubmed.ncbi.nlm.nih.gov/39307776/)). This is genuine catalytic promiscuity, **not** evidence of native function: retinal remains a major product in these systems ([PMID: 34850377](https://pubmed.ncbi.nlm.nih.gov/34850377/)), and the host bacteria lack any endogenous retinoid pathway. **Resolution:** retinol reduction is a non-core, in-vitro/heterologous activity; do not replace GO:0008106 with a retinol dehydrogenase term.

2. **Hydroxysteroid dehydrogenase (competing activity).** The CDD domain hit **cd05374** is labeled "17β-hydroxysteroid dehydrogenase-like, classical (c) SDRs." This is a **broad cluster named after a representative**, not a substrate determination. Steroid specificity in true HSDs depends on dedicated substrate-pocket residues (e.g., His221 in human 17β-HSD1; [PMID: 9525918](https://pubmed.ncbi.nlm.nih.gov/9525918/)), for which there is no evidence in YbbO. **Resolution:** refute the HSD alternative as a database-naming artifact.

3. **Paralog / family over-annotation risk.** Classical SDRs are a large family and functional transfer across distant SDRs is dangerous. Here, however, the transfer is **not** generic family inference — it is from a **90.6%-identical ortholog with 100% catalytic conservation** and two IDA papers. This is a best-case scenario for ISS/ISO transfer, which mitigates (but does not eliminate) the usual over-annotation concern.

4. **Organism-specific difference.** The Salmonella protein has not been assayed; a formal possibility of divergent substrate preference remains, though near-identity makes substantive functional divergence unlikely.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| **No direct assay on Salmonella Q7CR11** | UniProt/QuickGO annotation state; only GO:0016491 IBA present | Determines whether evidence code can be IDA vs ISS/ISO | Purify Salmonella YbbO; measure NADPH-dependent aldehyde reductase kinetics |
| **Exact native physiological substrate in Salmonella** | *E. coli* kinetics (C6–C18) and fatty-alcohol phenotype | Affects whether a more specific child GO term is warranted | Metabolomics of Δ*ybbO* Salmonella; in vitro substrate panel |
| **Native biological process (BP) context** | Literature is engineering-focused; no Salmonella loss-of-function physiology | BP annotation (aldehyde detox vs biosynthesis) currently a lead only | Phenotyping Δ*ybbO* Salmonella under aldehyde/lipid stress |
| **No experimental 3D structure of YbbO** | InterPro/CATH Rossmann-fold assignment (computational) | Structural confirmation of catalytic geometry would strengthen ISS | Crystal structure or AlphaFold-model + docking with NADP/aldehyde |
| **Cofactor preference confirmed only by sequence motif** | Arg34/Lys35 NADP-selecting pair; structural precedent (PMID 8805511) | NADP+ vs NAD+ is part of the exact GO term | Direct NADPH vs NADH kinetic comparison on the query enzyme |

---

## Discriminating Tests

The following would most efficiently distinguish the supported hypothesis from its alternatives:

1. **In vitro kinetic substrate panel on purified Salmonella YbbO (Q7CR11).** Test a ladder of aliphatic aldehydes (C2–C18) ± NADPH/NADH. *Predicted outcome if hypothesis holds:* NADPH-dependent reduction with maximal efficiency near C16/C18, mirroring the *E. coli* ortholog. **Discriminates:** confirms aliphatic-aldehyde reductase and NADPH preference; upgrades evidence to IDA.
2. **Steroid-substrate counter-assay.** Test estradiol/androstenedione and other hydroxysteroids. *Predicted outcome:* negligible activity. **Discriminates:** falsifies the HSD alternative directly.
3. **Retinal vs aliphatic-aldehyde competition kinetics.** Compare catalytic efficiency (kcat/Km) for retinal vs C16 aldehyde. *Predicted outcome:* aliphatic aldehyde ≫ retinal. **Discriminates:** confirms retinol reduction is promiscuous, not core.
4. **Δ*ybbO* Salmonella phenotyping + metabolomics.** Assess aldehyde accumulation and lipid-derived alcohol pools under stress. **Discriminates:** establishes native BP (detoxification vs biosynthetic).
5. **Structure/docking.** AlphaFold model + cofactor and substrate docking to verify the Asn–Ser–Tyr–Lys tetrad geometry and the NADP 2′-phosphate pocket. **Discriminates:** structural support for ISS transfer.

---

## Proposed Follow-up Actions (Curation Leads)

> All items are **leads requiring curator verification.**

**Candidate annotation update**
- **Add** GO:0008106 (alcohol dehydrogenase (NADP+) activity, MF) to **Q7CR11** with evidence **ISS (ECO:0000250)** or **ISO (ECO:0000266)**, **with/from = UniProtKB:P0AFP4**.
- **Retain** GO:0016491 as a parent but note GO:0008106 is the more informative term.
- **Do not** assign retinol dehydrogenase or hydroxysteroid dehydrogenase terms.

**Candidate references to verify (exact snippets)**
- [PMID: 27134112](https://pubmed.ncbi.nlm.nih.gov/27134112/): *"deletion of ybbO gene, which encodes NADP(+) dependent aldehyde reductase, led to >90% reduction in long chain fatty alcohol production"* and *"YbbO has wide substrate specificity ranging from C6 to C18 aldehyde, with maximum affinity and efficiency for C18 and C16 chain length aldehyde, respectively."*
- [PMID: 25108218](https://pubmed.ncbi.nlm.nih.gov/25108218/): *"we found five new ALRs using this screening method (YahK, DkgA, GldA, YbbO, and YghA)."*
- [PMID: 34850377](https://pubmed.ncbi.nlm.nih.gov/34850377/): *"Escherichia coli ybbO led to increase in retinol production, but retinal remained as a major product"* (to justify treating retinol activity as non-core).

**Suggested curator questions**
- Is an ISS/ISO transfer from a 90.6%-identical ortholog with 100% catalytic conservation acceptable under local annotation policy for adding GO:0008106?
- Does a more specific GO child term for long-chain/aliphatic aldehyde reductase activity exist and better fit the kinetics?
- Should a lead-level BP term (aldehyde catabolic process) be opened as a question pending Salmonella phenotyping?

**Suggested experiments**
- Purify Q7CR11; run the aliphatic-aldehyde kinetic panel and a steroid/retinal counter-assay (Discriminating Tests 1–3) to convert the ISS lead into a direct (IDA) annotation and definitively close out the HSD and retinol alternatives.

---

## Evidence Base (Literature Summary)

- **[PMID: 27134112](https://pubmed.ncbi.nlm.nih.gov/27134112/)** — *Identification of long chain specific aldehyde reductase and its use in enhanced fatty alcohol production in E. coli.* The anchor IDA reference: Δ*ybbO* abolishes >90% of long-chain fatty alcohol; kinetics define C6–C18 substrate range with C16/C18 optima. **Supports** the seed activity and provides substrate narrowing.
- **[PMID: 25108218](https://pubmed.ncbi.nlm.nih.gov/25108218/)** — *Toward aldehyde and alkane production by removing aldehyde reductase activity in E. coli.* Independent functional screen identifying YbbO as one of five aldehyde reductases. **Supports** GO:0008106 (second IDA reference).
- **[PMID: 25726762](https://pubmed.ncbi.nlm.nih.gov/25726762/)** — *Selective retinol production… from metabolically engineered E. coli.* Shows *ybbO* produces retinol via promiscuous activity; notes *E. coli* has no inherent retinoid pathway. **Qualifies** (non-native side activity).
- **[PMID: 34850377](https://pubmed.ncbi.nlm.nih.gov/34850377/)** — *Selective production of retinol by engineered S. cerevisiae…* Shows retinal remains a major product despite *ybbO* expression. **Qualifies** (retinol reduction inefficient).
- **[PMID: 39307776](https://pubmed.ncbi.nlm.nih.gov/39307776/)** and **[PMID: 41093029](https://pubmed.ncbi.nlm.nih.gov/41093029/)** — Retinoid engineering studies confirming *ybbO* retinal-reductase promiscuity (knockout prevents retinal loss). **Qualify** (competing, non-core).
- **[PMID: 8805511](https://pubmed.ncbi.nlm.nih.gov/8805511/)** — *Crystal structure of mouse lung carbonyl reductase…* Establishes that a conserved basic pair contacting the cofactor 2′-phosphate confers NADPH preference in SDRs. **Supports** the query's inferred NADPH selectivity (Arg34/Lys35).
- **[PMID: 9525918](https://pubmed.ncbi.nlm.nih.gov/9525918/)** — *Unusual charge stabilization of NADP+ in 17β-HSD.* Illustrates that true HSD steroid specificity relies on dedicated substrate residues, reinforcing that cd05374's "17β-HSD-like" label does not imply steroid activity. **Qualifies / refutes HSD alternative.**

---

## Conclusion

The blinded sequence-only test resolves cleanly. The query is **Salmonella Typhimurium LT2 YbbO (Q7CR11)**, a **classical SDR** with a fully intact catalytic tetrad (Asn81, Ser132/133, Tyr146, Lys150) and NADP-selecting basic pair (Arg34/Lys35), **90.6% identical** to the assay-characterized *E. coli* ortholog **P0AFP4**. The seed hypothesis — **NADPH-dependent aliphatic aldehyde reductase, GO:0008106** — is **SUPPORTED and can be narrowed** to medium/long-chain aliphatic aldehydes (C6–C18, optimal C16/C18). The hydroxysteroid dehydrogenase alternative is **refuted** as a CDD naming artifact; the retinol dehydrogenase activity is **real but promiscuous and non-native**. Because the *Salmonella* protein has not itself been assayed, the correct curation lead is an **ISS/ISO transfer of GO:0008106 from UniProtKB:P0AFP4**, not a direct-assay assertion.


## Artifacts

- [OpenScientist analysis provenance](openscientist_artifacts/artifacts_analysis_provenance.md)
- [OpenScientist evidence matrix](openscientist_artifacts/artifacts_evidence_matrix.csv)
- [OpenScientist go decision table](openscientist_artifacts/artifacts_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)