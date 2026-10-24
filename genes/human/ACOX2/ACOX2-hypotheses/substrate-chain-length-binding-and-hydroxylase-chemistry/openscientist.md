---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T03:24:11.083724'
end_time: '2026-09-21T03:51:34.153288'
duration_seconds: 1643.07
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ACOX2
  gene_symbol: ACOX2
  uniprot_accession: Q99424
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: substrate-chain-length-binding-and-hydroxylase-chemistry
  hypothesis_text: Human ACOX2 (Q99424) has free-fatty-acid binding, very-long-chain
    fatty-acid metabolism, and the exact GO0033791 cholestanoyl-CoA 24-hydroxylase
    reaction in addition to established branched-chain acyl-CoA oxidation. Evaluate
    these independently with complete primary substrate/ligand studies and live GO
    reaction definitions. Low C10/C16 oxidase efficiency is measurable capacity, not
    absence; compare PMID29287774 C24/C26 assays separately from C27 cyclic bile intermediates
    and PMID2079609. GO0000038 requires an aliphatic tail longer than 22 carbons.
    GO0033791 currently specifies a 25R substrate plus water/acceptor yielding the
    24R,25R hydroxylated product, whereas UniProt RHEA46728 specifies 25S substrate
    plus O2 yielding a 24E enoyl-CoA and H2O2. Does the original human PMID27884763
    or rat source actually establish the named hydroxylation, or was oxidase/side-chain
    shortening mapped to different chemistry? Read full texts and distinguish annotation
    error from absence of every secondary activity. Exact current PTHR10909 target
    leaf PTN002474948 descends from PTN000097533 (fatty-acid binding), PTN000097706
    (long-chain oxidation/VLCFA process), and PTN008508564 (hydroxylase). Human ACOX2
    itself legitimately seeds the last IBD. Do not challenge using donor count, preferred
    substrate, or missing target assays alone.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/ACOX2/ACOX2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human ACOX2 (Q99424) has free-fatty-acid binding,\
    \ very-long-chain fatty-acid metabolism, and\n  the exact GO0033791 cholestanoyl-CoA\
    \ 24-hydroxylase reaction in addition to established branched-chain\n  acyl-CoA\
    \ oxidation. Evaluate these independently with complete primary substrate/ligand\
    \ studies and\n  live GO reaction definitions. Low C10/C16 oxidase efficiency\
    \ is measurable capacity, not absence; compare\n  PMID29287774 C24/C26 assays\
    \ separately from C27 cyclic bile intermediates and PMID2079609. GO0000038\n \
    \ requires an aliphatic tail longer than 22 carbons. GO0033791 currently specifies\
    \ a 25R substrate plus\n  water/acceptor yielding the 24R,25R hydroxylated product,\
    \ whereas UniProt RHEA46728 specifies 25S substrate\n  plus O2 yielding a 24E\
    \ enoyl-CoA and H2O2. Does the original human PMID27884763 or rat source actually\n\
    \  establish the named hydroxylation, or was oxidase/side-chain shortening mapped\
    \ to different chemistry?\n  Read full texts and distinguish annotation error\
    \ from absence of every secondary activity. Exact current\n  PTHR10909 target\
    \ leaf PTN002474948 descends from PTN000097533 (fatty-acid binding), PTN000097706\
    \ (long-chain\n  oxidation/VLCFA process), and PTN008508564 (hydroxylase). Human\
    \ ACOX2 itself legitimately seeds the\n  last IBD. Do not challenge using donor\
    \ count, preferred substrate, or missing target assays alone.\nfocus_type: function_assignment\n\
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
citation_count: 6
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
artifacts:
- filename: acox2_go_decision_table.csv
  path: openscientist_artifacts/acox2_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist acox2 go decision table
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
- **Gene directory:** ACOX2
- **Gene symbol:** ACOX2
- **UniProt accession:** Q99424

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** substrate-chain-length-binding-and-hydroxylase-chemistry
- **Source file:** genes/human/ACOX2/ACOX2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ACOX2 (Q99424) has free-fatty-acid binding, very-long-chain fatty-acid metabolism, and the exact GO0033791 cholestanoyl-CoA 24-hydroxylase reaction in addition to established branched-chain acyl-CoA oxidation. Evaluate these independently with complete primary substrate/ligand studies and live GO reaction definitions. Low C10/C16 oxidase efficiency is measurable capacity, not absence; compare PMID29287774 C24/C26 assays separately from C27 cyclic bile intermediates and PMID2079609. GO0000038 requires an aliphatic tail longer than 22 carbons. GO0033791 currently specifies a 25R substrate plus water/acceptor yielding the 24R,25R hydroxylated product, whereas UniProt RHEA46728 specifies 25S substrate plus O2 yielding a 24E enoyl-CoA and H2O2. Does the original human PMID27884763 or rat source actually establish the named hydroxylation, or was oxidase/side-chain shortening mapped to different chemistry? Read full texts and distinguish annotation error from absence of every secondary activity. Exact current PTHR10909 target leaf PTN002474948 descends from PTN000097533 (fatty-acid binding), PTN000097706 (long-chain oxidation/VLCFA process), and PTN008508564 (hydroxylase). Human ACOX2 itself legitimately seeds the last IBD. Do not challenge using donor count, preferred substrate, or missing target assays alone.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human ACOX2 (Q99424) has free-fatty-acid binding, very-long-chain fatty-acid metabolism, and
  the exact GO0033791 cholestanoyl-CoA 24-hydroxylase reaction in addition to established branched-chain
  acyl-CoA oxidation. Evaluate these independently with complete primary substrate/ligand studies and
  live GO reaction definitions. Low C10/C16 oxidase efficiency is measurable capacity, not absence; compare
  PMID29287774 C24/C26 assays separately from C27 cyclic bile intermediates and PMID2079609. GO0000038
  requires an aliphatic tail longer than 22 carbons. GO0033791 currently specifies a 25R substrate plus
  water/acceptor yielding the 24R,25R hydroxylated product, whereas UniProt RHEA46728 specifies 25S substrate
  plus O2 yielding a 24E enoyl-CoA and H2O2. Does the original human PMID27884763 or rat source actually
  establish the named hydroxylation, or was oxidase/side-chain shortening mapped to different chemistry?
  Read full texts and distinguish annotation error from absence of every secondary activity. Exact current
  PTHR10909 target leaf PTN002474948 descends from PTN000097533 (fatty-acid binding), PTN000097706 (long-chain
  oxidation/VLCFA process), and PTN008508564 (hydroxylase). Human ACOX2 itself legitimately seeds the
  last IBD. Do not challenge using donor count, preferred substrate, or missing target assays alone.
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

# ACOX2 (Q99424) — Substrate Chain-Length Binding and Hydroxylase Chemistry: A Function-Assignment Review

**Focus type:** function_assignment
**Hypothesis slug:** substrate-chain-length-binding-and-hydroxylase-chemistry
**Target:** Human ACOX2, UniProt Q99424, NCBITaxon:9606 (*Homo sapiens*)
**Source:** `genes/human/ACOX2/ACOX2-ai-review.yaml` (free-text)

---

## Summary

**Verdict: Partially supported — one core claim supported, one refuted as a term-definition defect, and two judged over-annotated.** The seed hypothesis bundles four distinct claims about human ACOX2, and — as the seed explicitly requested — they must be evaluated independently. They resolve very differently. ACOX2's function as a **FAD-dependent peroxisomal acyl-CoA oxidase** acting on 2-methyl-branched-chain acyl-CoAs and C27 bile-acid-CoA intermediates is well supported by direct human enzymology and human deficiency/complementation studies, and this is its non-redundant core role. In contrast, the "exact GO:0033791 cholestanoyl-CoA 24-hydroxylase reaction" is **not** the chemistry ACOX2 performs: the enzyme dehydrogenates (desaturates) the bile-acid side chain to a 24-ene enoyl-CoA + H₂O₂ (RHEA:46728), and the 24-hydroxyl is installed downstream by a different protein, the D-bifunctional protein (DBP/HSD17B4).

The single most important message for a curator is that the GO:0033791 problem is a **term-definition/annotation-mapping defect, not an absence of activity**. The IDA to GO:0033791 (from PMID:27884763) captured the correct enzyme, the correct substrate class, and the correct biological step (bile-acid side-chain shortening). What is wrong is that the *live logical definition* of GO:0033791 — and its EC (1.17.99.3) and RHEA (15733) cross-references — describe a hydroxylation (25R substrate + H₂O + acceptor → 24R,25R-tetrahydroxy product), which differs from ACOX2's actual reaction on three independent axes: stereochemistry (25S vs 25R), oxidant (O₂ vs H₂O/acceptor), and product (24-ene enoyl-CoA + H₂O₂ vs a 24-hydroxy product). This is exactly the distinction the seed asked us to make: annotation error versus absence of a secondary activity. Here it is an annotation defect layered on top of a genuine, correctly identified enzyme.

The remaining two claims — free-fatty-acid binding (GO:0005504) and very-long-chain fatty-acid metabolic process (GO:0000038) — are **IBA-only phylogenetic inferences** with no ACOX2-specific direct evidence. Mechanistically ACOX2 binds acyl-CoA thioesters rather than free fatty acids, and straight-chain/VLCFA oxidation is the assigned role of the paralog ACOX1; ACOX2's own straight-chain capacity reaches only ~C16 at low efficiency, while its genuinely long substrates are branched C27 sterols, not aliphatic VLCFAs (>22-carbon tail). Both are candidate non-core annotations. None of these judgments relies on donor count, preferred substrate, or missing target assays, in accordance with the seed's constraints.

---

## Key Findings

### Finding 1 — ACOX2 catalyzes oxidase (dehydrogenation) chemistry, not literal 24-hydroxylation; GO:0033791's definition conflicts with the enzyme's real reaction

The curated UniProt Q99424 catalytic-activity block lists exclusively oxidase/desaturation reactions of the canonical acyl-CoA oxidase form — *a 2,3-saturated acyl-CoA + O₂ = a (2E)-enoyl-CoA + H₂O₂* (e.g., RHEA:38959) — with **FAD** as the cofactor. The bile-acid reaction at the heart of the hypothesis is RHEA:46728:

> (25S)-3α,7α,12α-trihydroxy-5β-cholestan-26-oyl-CoA + O₂ = (24E)-3α,7α,12α-trihydroxy-5β-cholest-24-en-26-oyl-CoA + H₂O₂

This is a dehydrogenation introducing a **24,25 double bond** (a 24-**ene**), consuming O₂ and producing H₂O₂ — the diagnostic signature of a flavin acyl-CoA oxidase. By contrast, the GO term **GO:0033791 "cholestanoyl-CoA 24-hydroxylase activity"** is defined as a hydroxylation:

> (25R)-3α,7α,12α-trihydroxy-5β-cholestan-26-oyl-CoA + H₂O + acceptor = (24R,25R)-3α,7α,12α,24-**tetrahydroxy**-5β-cholestan-26-oyl-CoA + reduced acceptor

cross-referenced to **EC 1.17.99.3 / RHEA:15733**. The two reactions differ on three independent chemical axes, summarized below:

| Feature | ACOX2 real reaction (RHEA:46728) | GO:0033791 definition (RHEA:15733) |
|---|---|---|
| Substrate stereochemistry | 25**S** | 25**R** |
| Oxidant / co-substrate | **O₂** | **H₂O + acceptor** |
| Product | (24**E**)-enoyl-CoA + **H₂O₂** | (24R,25R)-24-**hydroxy** tetrahydroxy-CoA + reduced acceptor |
| Chemistry | α,β-dehydrogenation (desaturation) | hydroxylation |
| Cofactor | FAD (oxidase) | acceptor-dependent hydroxylase |

The IDA supporting GO:0033791 traces to [PMID:27884763](https://pubmed.ncbi.nlm.nih.gov/27884763/), which frames ACOX2 as *"an acyl-CoA oxidase … involved in the shortening of C27 cholesterol derivatives to generate C24 bile acids"* and shows that *"THCA biotransformation into cholic acid was enhanced in cells overexpressing ACOX2."* The experiment therefore demonstrated **oxidase / side-chain-shortening** chemistry, not a discrete hydroxylation. Notably, GO:0033791's own synonyms include "THCA-CoA oxidase activity," revealing that the term was *intended* to capture this enzyme entity — which is why the annotation should be read as a legacy **term-definition defect** (rooted in an old EC 1.17.99.3 "hydroxylase" nomenclature) rather than a wrong gene-to-function link.

### Finding 2 — ACOX2's demonstrated core substrates are 2-methyl-branched-chain acyl-CoAs and C27 bile-acid-CoA intermediates; "fatty acid binding" and "VLCFA metabolic process" are IBA-only and over-general

The substrate scope of the human enzyme is anchored in direct biochemistry. Vanhove and colleagues ([PMID:8387517](https://pubmed.ncbi.nlm.nih.gov/8387517/)) purified from human liver and kidney *"a novel branched chain acyl-CoA oxidase, which oxidizes the CoA esters of 2-methyl-branched fatty acids as well as those of the bile acid intermediates"* di- and trihydroxycoprostanic acids — establishing a **single** human enzyme with a dual substrate class (branched-chain FA-CoA + bile-acid-CoA) and no separate dedicated human THCA-CoA oxidase.

The modern substrate-specificity and deficiency study ([PMID:29287774](https://pubmed.ncbi.nlm.nih.gov/29287774/)) partitions the family cleanly: *"ACOX2 is the only human acyl-CoA oxidase involved in bile acid biosynthesis,"* whereas *"ACOX1 is responsible for the oxidation of straight-chain fatty acids with different chain lengths."* ACOX2-deficient fibroblasts retained normal pristanic-acid oxidation, indicating redundancy with ACOX3 for branched-chain fatty acids; bile-acid intermediate oxidation is the non-redundant ACOX2 role.

The UniProt FUNCTION annotation records that ACOX2 can oxidize straight-chain decanoyl-CoA (C10; RHEA:40179) and hexadecanoyl-CoA (C16; RHEA:40167) but only with **low efficiency**, alongside pristanoyl-CoA and other methyl-branched-chain fatty acyl-CoAs. The seed rightly cautions that low C10/C16 efficiency is *measurable capacity, not absence* — and this report honors that: the point is not that ACOX2 lacks straight-chain activity, but that its straight-chain reach extends only to ~C16 at low efficiency, which cannot satisfy the two IBA terms:

- **GO:0005504 fatty acid binding** is annotated IBA only (GO_REF:0000033). Mechanistically ACOX2 binds acyl-**CoA thioesters**, not free fatty acids; "fatty acid binding" is a family-level generalization.
- **GO:0000038 very-long-chain fatty acid metabolic process** is annotated IBA only. Its definition requires an aliphatic tail **>22 carbons**. ACOX2's straight-chain capacity extends only to ~C16 (low efficiency), and its genuinely long substrates are **branched C27 sterol/bile-acid** intermediates, not aliphatic VLCFAs. Straight-chain VLCFA oxidation is ACOX1's assigned role ([PMID:29287774](https://pubmed.ncbi.nlm.nih.gov/29287774/)).

Both are therefore candidate **non-core** annotations — reasonable family inferences, but not representative of ACOX2's direct, demonstrated activity.

### Finding 3 — The 24-hydroxyl is installed by D-bifunctional protein (DBP/HSD17B4) at β-oxidation steps 2–3, not by ACOX2; no GO MF term maps to ACOX2's real reaction RHEA:46728

Ferdinandusse and colleagues ([PMID:15769750](https://pubmed.ncbi.nlm.nih.gov/15769750/)) state that *"peroxisomal beta-oxidation is an essential step in bile acid synthesis, since it is required for shortening of C27-bile acid intermediates to produce mature C24-bile acids"* and that *"D-Bifunctional protein (DBP) is responsible for the second and third step of this beta-oxidation process."* In the classic β-oxidation cycle, ACOX2 performs only step 1 (oxidase), and the hydroxyl is introduced at step 2 (hydratase, DBP). The hydroxyl group that GO:0033791's definition attributes to a single "24-hydroxylase" is therefore the product of DBP hydration of the ACOX2-generated enoyl-CoA — a downstream event catalyzed by a different protein. This is corroborated by the rat-liver enzymology of Novikov and colleagues ([PMID:7929456](https://pubmed.ncbi.nlm.nih.gov/7929456/)), which shows the first reaction is an acyl-CoA oxidase and that the 3-hydroxyacyl-CoA dehydrogenase/hydratase steps are separate enzymes (including the multifunctional protein).

A QuickGO ontology search returned **no GO molecular-function term cross-referenced to RHEA:46728** (ACOX2's actual bile-acid oxidase reaction) or to RHEA:15733. The most accurate available MF parent is **GO:0003997 acyl-CoA oxidase activity**, whose definition — *"a 2,3-saturated acyl-CoA + O₂ = a (2E)-enoyl-CoA + H₂O₂"* — exactly matches ACOX2's chemistry and is already present as an IEA annotation. On the BP side, GO:0033540 (fatty acid beta-oxidation using acyl-CoA oxidase) likewise specifies the oxidase first step producing H₂O₂, matching ACOX2's role.

---

## Mechanistic Model / Interpretation

All four hypothesis components map onto a single, well-understood peroxisomal β-oxidation cycle. ACOX2 performs **only the first step**; the "hydroxylase" chemistry belongs to a different enzyme two steps later.

```
        C27 bile-acid-CoA intermediate  (e.g. (25S)-THC-26-oyl-CoA)
                       │
                       │   ACOX2  (FAD oxidase, RHEA:46728)   ← the demonstrated reaction
                       │   acyl-CoA + O2 → (24E)-enoyl-CoA + H2O2
                       ▼
             (24E)-3α,7α,12α-trihydroxy-cholest-24-en-26-oyl-CoA
                       │
                       │   DBP / HSD17B4  (hydratase, step 2)  ← installs the 24-OH
                       │   enoyl-CoA + H2O → 3-hydroxyacyl-CoA
                       ▼
             24-hydroxy(3-hydroxyacyl)-CoA
                       │
                       │   DBP / HSD17B4  (dehydrogenase, step 3)
                       ▼
             3-keto-acyl-CoA
                       │
                       │   SCPx thiolase (step 4): cleave C3 unit (propionyl-CoA)
                       ▼
        C24 bile acid (e.g. cholyl-CoA → cholic acid)
```

Reading the seed's specific chemical claims against this model:

- The seed correctly observes that **GO:0033791 currently specifies a 25R substrate + H₂O/acceptor → 24R,25R product**, whereas **UniProt RHEA:46728 specifies a 25S substrate + O₂ → 24E-enoyl-CoA + H₂O₂**. This report confirms the discrepancy is real and material: they are different reactions, not two descriptions of one.
- The seed's central question — *"Does the original human PMID27884763 or rat source actually establish the named hydroxylation, or was oxidase/side-chain shortening mapped to different chemistry?"* — resolves clearly: **PMID:27884763 established oxidase/side-chain shortening**, which was then mapped to a term (GO:0033791) whose logical definition names hydroxylation. This is an **annotation-mapping error at the term level**, not evidence that ACOX2 lacks the activity it was studied for.

The seed's phylogenetic scaffolding is consistent with this interpretation. PTHR10909 leaf PTN002474948 descending from a hydroxylase node (PTN008508564) and from fatty-acid-binding / long-chain-oxidation nodes (PTN000097533, PTN000097706) reflects **family-level** inheritance of MF/BP terms. Human ACOX2 legitimately seeds the hydroxylase IBD, but the IBA-propagated terms (fatty acid binding, VLCFA process) are precisely the ones that are over-general for the specific human enzyme, whose experimentally demonstrated activity is narrower (branched-chain + bile-acid-CoA oxidase).

---

## Evidence Base

| Citation | Evidence type | Relationship | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID:27884763](https://pubmed.ncbi.nlm.nih.gov/27884763/) | Direct assay + human mutant phenotype | **Refutes** literal 24-hydroxylase; **supports** oxidase | 24-hydroxylation vs oxidase side-chain shortening | "Acyl-CoA oxidase (ACOX2) is involved in the shortening of C27 cholesterol derivatives to generate C24 bile acids"; overexpression enhances THCA→cholic acid | Human; ACOX2-deficiency patient + overexpression cells | High for oxidase role; this is the source of the GO:0033791 IDA — supports term-definition-defect reading |
| UniProt Q99424 (RHEA:46728, RHEA:38959, RHEA:40167, RHEA:40179) | Database (reaction/cofactor curation) | **Qualifies/refutes** hydroxylase; **supports** oxidase | Exact catalyzed reaction | All reactions are FAD-dependent oxidase form (acyl-CoA + O₂ → 2E-enoyl-CoA + H₂O₂); bile-acid reaction yields (24E)-enoyl-CoA from 25S substrate | Human, curated | High; database-level but reaction is chemically explicit |
| GO:0033791 definition / EC 1.17.99.3 / RHEA:15733 | Database (ontology definition) | **Competing** definition | Is GO:0033791 chemistry the same as ACOX2's? | Term defined as hydroxylation (25R + H₂O/acceptor → 24-hydroxy product); differs in stereochem, oxidant, product | Ontology | High; direct inspection of live term; synonym "THCA-CoA oxidase" shows intent |
| [PMID:8387517](https://pubmed.ncbi.nlm.nih.gov/8387517/) | Direct assay (enzyme purification) | **Supports** core function | ACOX2 substrate scope | Single human "branched chain acyl-CoA oxidase" oxidizes 2-methyl-branched FA-CoA and bile-acid intermediate CoAs | Human liver/kidney | High; foundational human biochemistry |
| [PMID:29287774](https://pubmed.ncbi.nlm.nih.gov/29287774/) | Direct assay + mutant phenotype | **Supports** core; **qualifies** VLCFA/FA-binding | Is ACOX2 the bile-acid oxidase? the VLCFA oxidase? | "ACOX2 is the only human acyl-CoA oxidase involved in bile acid biosynthesis"; "ACOX1 is responsible for the oxidation of straight-chain fatty acids with different chain lengths" | Human; patient fibroblasts, redundancy with ACOX3 | High; directly assigns straight-chain/VLCFA to ACOX1 |
| [PMID:15769750](https://pubmed.ncbi.nlm.nih.gov/15769750/) | Mutant phenotype (KO) + pathway | **Refutes** ACOX2-as-24-hydroxylase | Who installs the 24-OH? | DBP catalyzes steps 2–3 of peroxisomal β-oxidation shortening C27→C24 | Mouse L-/D-BP knockouts | High; localizes hydroxyl-installing steps to DBP |
| [PMID:7929456](https://pubmed.ncbi.nlm.nih.gov/7929456/) | Direct assay (purification) | **Supports** step separation | Are oxidase and hydroxyacyl steps separate? | First step is acyl-CoA oxidase; 3-hydroxyacyl-CoA dehydrogenase/hydratase are distinct enzymes | Rat liver peroxisomes | High for enzymology; rat |
| QuickGO/GO MF search for RHEA:46728 | Computational (ontology lookup) | **Qualifies** curation | Is there a GO MF for ACOX2's exact reaction? | No GO MF maps to RHEA:46728 or RHEA:15733; nearest accurate parent is GO:0003997 | Ontology | Medium-high; negative search result |
| GO:0005504 (IBA, GO_REF:0000033), GO:0000038 (IBA) | Database (evidence-code inspection) | **Qualifies** (over-general) | Are FA-binding and VLCFA-process directly supported? | Both IBA-only, family inference; not backed by direct ACOX2 assays | Ontology/QuickGO | Medium-high; evidence-code based |

**Literature notes:**

- *ACOX2 deficiency: An inborn error of bile acid synthesis identified in an adolescent with persistent hypertransaminasemia.* [PMID:27884763](https://pubmed.ncbi.nlm.nih.gov/27884763/) — source of the GO:0033791 IDA; frames ACOX2 as an oxidase performing C27→C24 side-chain shortening.
- *A novel case of ACOX2 deficiency leads to recognition of a third human peroxisomal acyl-CoA oxidase.* [PMID:29287774](https://pubmed.ncbi.nlm.nih.gov/29287774/) — substrate-specificity and redundancy study; ACOX2 = only human bile-acid acyl-CoA oxidase; ACOX1 = straight-chain/VLCFA.
- *The CoA esters of 2-methyl-branched chain fatty acids and of the bile acid intermediates … are oxidized by one single peroxisomal branched chain acyl-CoA oxidase in human liver and kidney.* [PMID:8387517](https://pubmed.ncbi.nlm.nih.gov/8387517/) — foundational human enzyme purification.
- *Developmental changes of bile acid composition … in L- and D-bifunctional protein single and double knockout mice.* [PMID:15769750](https://pubmed.ncbi.nlm.nih.gov/15769750/) — localizes hydroxyl-installing steps to DBP.
- *Peroxisomal beta-oxidation. Purification of four novel 3-hydroxyacyl-CoA dehydrogenases from rat liver peroxisomes.* [PMID:7929456](https://pubmed.ncbi.nlm.nih.gov/7929456/) — confirms the first step is an oxidase and the 3-hydroxyacyl steps are separate enzymes.

---

## GO Curation Implications

The following are **leads requiring curator verification**, organized by GO aspect.

**Molecular Function**

- **GO:0033791 "cholestanoyl-CoA 24-hydroxylase activity" (IDA, PMID:27884763):** Do **not** treat this as a clean gene-to-function match. The IDA is supported for the *enzyme and biological step* (bile-acid side-chain shortening), but the term's **live logical definition and EC/RHEA cross-references (EC 1.17.99.3, RHEA:15733) describe hydroxylase chemistry that ACOX2 does not perform**. Lead: flag GO:0033791 as a term-definition/mapping issue (candidate for ontology repair or reannotation), and prefer **GO:0003997 acyl-CoA oxidase activity** — whose definition matches RHEA:46728 — as the accurate MF. Consider requesting a new/repaired MF term anchored to RHEA:46728.
- **GO:0016402 pristanoyl-CoA oxidase activity / GO:0003997 acyl-CoA oxidase activity:** Retain as accurate core/branched-chain MF terms.
- **GO:0120523 / GO:0120524 medium/long-chain acyl-CoA oxidase activity (IEA:RHEA):** Retain as *measurable low-efficiency capacity* (C10, C16), annotated as such.
- **GO:0005504 "fatty acid binding" (IBA only):** Candidate **non-core / demote**. ACOX2 binds acyl-CoA thioesters, not free fatty acids. Do not leave "fatty acid binding" as the informative MF; an acyl-CoA-oriented term (or none) is preferable, and far preferable to generic "protein binding."

**Biological Process**

- **GO:0006699 bile acid biosynthetic process (IDA):** Retain — directly demonstrated.
- **GO:0033540 fatty acid beta-oxidation using acyl-CoA oxidase:** Retain — accurate and consistent with the oxidase first step.
- **GO:0000038 "very-long-chain fatty acid metabolic process" (IBA only):** Candidate **non-core / demote or remove for ACOX2**. The definition requires a >22-C aliphatic tail; ACOX2's straight-chain reach is ~C16 (low efficiency), and its long substrates are branched C27 sterols. Straight-chain VLCFA metabolism is ACOX1's role.

**Cellular Component**

- Peroxisomal matrix localization is well established for this enzyme class and is not in dispute; it is not the focus of this hypothesis.

---

## Mechanistic Scope

The **immediate molecular function** under test is a single-turnover FAD-dependent acyl-CoA oxidase reaction: abstraction of the 2,3 (α,β) hydrogen pair from a bile-acid-CoA or branched-chain acyl-CoA, transferring electrons to O₂ to form H₂O₂ and creating an enoyl-CoA double bond. For the C27 bile-acid substrate this places the double bond at the 24,25 position (24-ene), the committed first step of side-chain shortening.

Everything else in the hypothesis is either (a) a **downstream pathway consequence** — the 24-hydroxyl (DBP hydration), the eventual C24 bile-acid product, and cholic-acid output — or (b) a **family-level generalization** — free-fatty-acid binding and VLCFA metabolism. The disease manifestation (ACOX2 deficiency: persistent hypertransaminasemia, C27 accumulation, C24 bile-acid deficiency) is a **loss-of-function phenotype**, informative for confirming the pathway role but not itself evidence of hydroxylase chemistry. Curators should not let the loss-of-function bile-acid phenotype license a "24-hydroxylase" MF; the phenotype is equally explained by loss of the oxidase step.

---

## Conflicts and Alternatives

1. **Term-definition vs. gene annotation (primary conflict).** GO:0033791's definition (hydroxylation, 25R, H₂O/acceptor, 24-hydroxy product; EC 1.17.99.3, RHEA:15733) conflicts with UniProt RHEA:46728 (dehydrogenation, 25S, O₂, 24-ene product). The synonym "THCA-CoA oxidase activity" shows the term *intends* the right enzyme, so this is a legacy definitional artifact (old EC 1.17.99.3 "hydroxylase" nomenclature) rather than paralog confusion or conflicting experimental data.
2. **Stereochemistry mismatch (25R vs 25S).** UniProt specifies the 25S diastereomer as the physiological ACOX2 substrate and notes ACOX2 desaturates only the (2S)/(25S)-methyl isomers; GO:0033791 specifies 25R and a 24R,25R product. This is a genuine chemical inconsistency worth flagging.
3. **Paralog attribution.** ACOX1 (straight-chain, including VLCFA) and ACOX3 (branched-chain, redundant with ACOX2) can absorb functions that IBA propagation blurs onto ACOX2. The VLCFA-process and fatty-acid-binding terms are best read as ACOX1-like / family attributes over-applied to ACOX2. Redundant pristanoyl-CoA oxidation by ACOX3 explains normal pristanic-acid oxidation in ACOX2-deficient fibroblasts.
4. **Species differences.** Rat has three distinct oxidases (palmitoyl-, pristanoyl-, THC-CoA oxidases; PMID:7929456), whereas human uses a single branched-chain acyl-CoA oxidase (ACOX2) for both branched-chain and bile-acid substrates (PMID:8387517). Rat-derived reaction naming should not be transplanted onto the human enzyme without care.
5. **Low-efficiency straight-chain capacity is real but non-core.** Consistent with the seed's caution, C10/C16 oxidase activity exists and should not be used to *deny* ACOX2 any straight-chain capacity — but it is too weak and too short-chain to justify a VLCFA term.

---

## Limitations and Knowledge Gaps

1. **Does ACOX2 ever act on a genuine straight-chain VLCFA (>C22)?** Checked UniProt/RHEA/literature: only ≤C16 low-efficiency documented. This matters because GO:0000038 is currently attached. Resolve with a kinetic panel of straight-chain C18–C26 acyl-CoAs on recombinant ACOX2.
2. **Any direct free-fatty-acid (non-CoA) binding?** No primary ligand/binding study was found; GO:0005504 is IBA only. Resolve with ITC/SPR or structural ligand studies distinguishing free-FA from acyl-CoA binding.
3. **Exact stereochemistry/product of the human ACOX2 bile-acid reaction (25S → 24E).** Accepted here from curated RHEA/UniProt records rather than re-derived from raw kinetics. Which diastereomer(s) ACOX2 turns over, and whether GO:0033791's 25R is merely an older convention, should be confirmed from full-text methods of PMID:27884763/PMID:29287774 and the Van Veldhoven/Vanhove substrate-synthesis series.
4. **GO/QuickGO reaction-to-term mapping was checked by ontology search, not exhaustively.** The "no GO MF maps to RHEA:46728" conclusion is a negative search result and should be confirmed against the current ontology release and RHEA2GO mapping.
5. **PMID:2079609 (cited in the seed)** was not independently retrieved in the reviewed set; its specific contribution to separating C24/C26 from C27 cyclic bile-intermediate assays should be verified in full text by the curator.
6. **No structural corroboration** of FAD-oxidase geometry was performed; not expected to change the verdict but would strengthen it.

---

## Discriminating Tests

1. **Reaction-product identification (most decisive).** LC-MS/MS of the ACOX2 product from THCA-CoA (ideally with ¹⁸O₂ labeling): a **24-ene enoyl-CoA + H₂O₂** (oxidase, no ¹⁸O in a 24-OH) versus a **24-hydroxy-THCA-CoA** (hydroxylase) directly discriminates GO:0033791's definition from RHEA:46728. The oxidase product is expected.
2. **O₂/H₂O₂ dependence.** Oxidase chemistry consumes O₂ and produces H₂O₂ ~1:1 (measure via peroxidase coupling); a hydroxylase per the GO definition would use H₂O + an external acceptor.
3. **Stereochemical substrate panel (25R vs 25S).** Kinetics on both diastereomers clarify whether the 25R in GO:0033791 is spurious or a real minor substrate.
4. **DBP (HSD17B4) knockdown/knockout + intermediate profiling.** Accumulation of the 24-ene enoyl-CoA upstream of the 24-hydroxy species confirms DBP installs the hydroxyl (complements PMID:15769750).
5. **Straight-chain VLCFA kinetics (C18–C26 acyl-CoA) across ACOX1/2/3.** Tests the GO:0000038 attribution to ACOX2 vs ACOX1.
6. **Comparative binding assay (free FA vs acyl-CoA).** Tests whether GO:0005504 "fatty acid binding" is even the correct binding term.

---

## Curation Leads

*All items below are leads requiring curator verification.*

**Candidate action changes**

- Treat the **GO:0033791** annotation as a **term-definition/mapping defect**, not a wrong gene assignment. Retain the biological intent (ACOX2 = bile-acid oxidase / side-chain shortening) but map the MF to **GO:0003997 acyl-CoA oxidase activity** (matches RHEA:46728), and file an ontology note that GO:0033791's definition/EC(1.17.99.3)/RHEA(15733) describes hydroxylase chemistry inconsistent with the enzyme's FAD-oxidase reaction.
- Mark **GO:0005504 fatty acid binding** and **GO:0000038 very-long-chain fatty acid metabolic process** as **IBA-only, non-core / candidate demotion** for ACOX2.

**Candidate reference snippets to verify**

- PMID:27884763 — *"Acyl-CoA oxidase (ACOX2) is involved in the shortening of C27 cholesterol derivatives to generate C24 bile acids."*
- PMID:27884763 — *"THCA biotransformation into cholic acid was enhanced in cells overexpressing ACOX2."*
- PMID:8387517 — *"a novel branched chain acyl-CoA oxidase, which oxidizes the CoA esters of 2-methyl-branched fatty acids as well as those of the bile acid intermediates."*
- PMID:29287774 — *"ACOX2 is the only human acyl-CoA oxidase involved in bile acid biosynthesis."*
- PMID:29287774 — *"ACOX1 is responsible for the oxidation of straight-chain fatty acids with different chain lengths."*
- PMID:15769750 — *"D-Bifunctional protein (DBP) is responsible for the second and third step of this beta-oxidation process."*

**Candidate GO terms**

- **Retain / promote as core MF:** GO:0003997 acyl-CoA oxidase activity; GO:0016402 pristanoyl-CoA oxidase activity.
- **Retain as core BP:** GO:0006699 bile acid biosynthetic process; GO:0033540 fatty acid beta-oxidation using acyl-CoA oxidase.
- **Flag / repair:** GO:0033791 (definition mismatch).
- **Demote / non-core:** GO:0005504; GO:0000038.

**Suggested curator questions**

- Should the GO ontology group repair GO:0033791's definition (or replace its RHEA/EC cross-reference) so it matches the flavin-oxidase reaction ACOX2 actually catalyzes?
- Is there any GO MF term (present or requestable) directly anchored to RHEA:46728? If not, should one be created?
- Is there any human ACOX2 straight-chain >C22 assay that would justify GO:0000038? If not, add the non-core qualification.

**Suggested experiments** — see *Discriminating Tests* (¹⁸O₂ product ID, H₂O₂ stoichiometry, 25R/25S kinetics, DBP-knockout intermediate profiling, VLCFA kinetic panel, free-FA vs acyl-CoA binding).

---

## Provenance Artifact

A computed GO decision table (`acox2_go_decision_table.csv`) accompanies this report, listing the relevant GO terms with their current evidence codes and recommended curator leads, generated from the live UniProt/RHEA/QuickGO records and primary-literature evidence gathered across the three investigation iterations.

---

## Bottom Line for the Curator

ACOX2's **branched-chain and bile-acid acyl-CoA oxidase** function is well supported and should anchor the review (GO:0003997 + bile-acid biosynthesis BP). The seed's "exact GO:0033791 cholestanoyl-CoA 24-hydroxylase reaction" is **not** performed by ACOX2 as the term is defined — the IDA captured the right enzyme and the right biological step but is bound to a term whose definition/EC/RHEA describes hydroxylase chemistry that belongs, in the pathway, to DBP hydration downstream. Treat this as a term-definition defect to flag, not proof of a hidden hydroxylase activity. The **free-fatty-acid-binding** (GO:0005504) and **VLCFA-metabolic-process** (GO:0000038) claims are IBA-only, over-general, and are candidate non-core annotations. None of these judgments rests on donor count, preferred substrate, or missing target assays, per the seed's constraints.


## Artifacts

- [OpenScientist acox2 go decision table](openscientist_artifacts/acox2_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)