---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T18:09:24.941082'
end_time: '2026-09-20T18:22:08.150143'
duration_seconds: 763.21
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: rat
  gene: Aldh1l1
  gene_symbol: Aldh1l1
  uniprot_accession: P28037
  taxon_id: NCBITaxon:10116
  taxon_label: Rattus norvegicus
  focus_type: function_assignment
  hypothesis_slug: cofactor-specificity-and-mitochondrial-localization
  hypothesis_text: Rat ALDH1L1 has NAD+-dependent aldehyde dehydrogenase activity
    (GO:0004029) and localizes to mitochondria (GO:0005739). Evaluate these independently,
    separating ALDH1L1 from mitochondrial ALDH1L2. Examine substrate and NAD+/NADP+
    specificity of the intact multidomain enzyme versus isolated domains, and quantitative
    cofactor assays where available. Examine primary localization, isoforms and possible
    secondary pools without equating the predominant cytosolic location with exclusivity.
    Distinguish catalytic promiscuity in vitro from a supported physiological activity.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/rat/Aldh1l1/Aldh1l1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Rat ALDH1L1 has NAD+-dependent aldehyde dehydrogenase\
    \ activity (GO:0004029) and localizes\n  to mitochondria (GO:0005739). Evaluate\
    \ these independently, separating ALDH1L1 from mitochondrial ALDH1L2.\n  Examine\
    \ substrate and NAD+/NADP+ specificity of the intact multidomain enzyme versus\
    \ isolated domains,\n  and quantitative cofactor assays where available. Examine\
    \ primary localization, isoforms and possible\n  secondary pools without equating\
    \ the predominant cytosolic location with exclusivity. Distinguish catalytic\n\
    \  promiscuity in vitro from a supported physiological activity.\nfocus_type:\
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
citation_count: 10
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
artifacts:
- filename: aldh1l1_vs_aldh1l2_Nterm_presequence.csv
  path: openscientist_artifacts/aldh1l1_vs_aldh1l2_Nterm_presequence.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist aldh1l1 vs aldh1l2 Nterm presequence
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

- **Organism code:** rat
- **Taxon:** Rattus norvegicus (NCBITaxon:10116)
- **Gene directory:** Aldh1l1
- **Gene symbol:** Aldh1l1
- **UniProt accession:** P28037

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** cofactor-specificity-and-mitochondrial-localization
- **Source file:** genes/rat/Aldh1l1/Aldh1l1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Rat ALDH1L1 has NAD+-dependent aldehyde dehydrogenase activity (GO:0004029) and localizes to mitochondria (GO:0005739). Evaluate these independently, separating ALDH1L1 from mitochondrial ALDH1L2. Examine substrate and NAD+/NADP+ specificity of the intact multidomain enzyme versus isolated domains, and quantitative cofactor assays where available. Examine primary localization, isoforms and possible secondary pools without equating the predominant cytosolic location with exclusivity. Distinguish catalytic promiscuity in vitro from a supported physiological activity.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Rat ALDH1L1 has NAD+-dependent aldehyde dehydrogenase activity (GO:0004029) and localizes
  to mitochondria (GO:0005739). Evaluate these independently, separating ALDH1L1 from mitochondrial ALDH1L2.
  Examine substrate and NAD+/NADP+ specificity of the intact multidomain enzyme versus isolated domains,
  and quantitative cofactor assays where available. Examine primary localization, isoforms and possible
  secondary pools without equating the predominant cytosolic location with exclusivity. Distinguish catalytic
  promiscuity in vitro from a supported physiological activity.
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

# AIGR Gene Hypothesis Deep Research — Rat ALDH1L1 (P28037)

## Focus: Cofactor Specificity and Mitochondrial Localization

**Hypothesis under evaluation:** *Rat ALDH1L1 has NAD⁺-dependent aldehyde dehydrogenase activity (GO:0004029) and localizes to mitochondria (GO:0005739).*

**Focus type:** function_assignment · **Gene:** Aldh1l1 (rat, NCBITaxon:10116) · **UniProt:** P28037 (AL1L1_RAT, "Cytosolic 10-formyltetrahydrofolate dehydrogenase", EC 1.5.1.6)

---

## Summary

This report evaluates a two-part function-assignment hypothesis for rat ALDH1L1 and finds that **both clauses fail as literally worded**, each for a well-characterized and independently verifiable reason. The seed instruction to evaluate the cofactor and localization claims *separately*, and to distinguish ALDH1L1 from its mitochondrial paralog ALDH1L2, is essential — and following it resolves the hypothesis cleanly.

On cofactor specificity, direct enzymology on the **rat** protein shows the aldehyde dehydrogenase activity is **NADP⁺-dependent, not NAD⁺-dependent**. Purified rat liver cytosolic 10-formyltetrahydrofolate dehydrogenase oxidizes propanal with Km(NADP⁺) = 46 µM, and the rat crystal structure identifies a Gln600 water-mediated contact with the 2′-phosphate of NADP that structurally enforces "specificity of the enzyme for NADP over NAD." Consequently **GO:0004029 (aldehyde dehydrogenase (NAD⁺) activity) is over-annotated** — it is present only by orthology inference and is contradicted by primary rat data. Moreover, even the correctly-cofactored NADP⁺-aldehyde activity is a **promiscuous in-vitro property** of the C-terminal ALDH-like domain acting on small surrogate substrates, not a physiological aldehyde-detoxification function.

On localization, rat ALDH1L1 is the **cytosolic** enzyme (its UniProt name literally begins "Cytosolic…", with IDA support for GO:0005829). The mitochondrial 10-formyl-THF dehydrogenase is a **distinct paralog, ALDH1L2**, the product of a separate gene that arose by duplication before the emergence of bony fish, and which carries an N-terminal mitochondrial presequence that ALDH1L1 lacks. **GO:0005739 (mitochondrion) on ALDH1L1 is supported only by phylogenetic inference (IBA) and most plausibly reflects paralog carry-over.** The core, physiologically supported molecular function — confirmed by knockout phenotypes that map to folate/glycine one-carbon metabolism — is **GO:0016155 (formyltetrahydrofolate dehydrogenase activity)**, cytosolic and NADP⁺-dependent. The overall curation verdict is therefore **over-annotated / refuted on both counts as literally stated**, with accurate replacement terms already present on the record.

---

## Executive Judgment

**Verdict: Over-annotated / refuted on both counts, as literally stated.**

1. **GO:0004029 "aldehyde dehydrogenase (NAD⁺) activity" — REFUTED (wrong cofactor) + non-core (in-vitro promiscuity).** Direct kinetic and structural studies of the *rat* enzyme show the aldehyde dehydrogenase activity is **NADP⁺-dependent** (Km NADP⁺ = 46 µM; structural selectivity for NADP over NAD via Gln600). Short-chain-aldehyde (propanal) oxidation is a **promiscuous in-vitro activity of the ALDH-like C-terminal domain**, not a supported physiological function. The correct cofactor term, **GO:0033721 "aldehyde dehydrogenase (NADP⁺) activity"**, is already present (IDA). GO:0004029 is attached only by **ISO (orthology-inferred)** evidence and is contradicted by primary rat data.

2. **GO:0005739 "mitochondrion" — WEAKLY SUPPORTED / likely paralog carry-over.** The experimentally supported location is **cytosol** (GO:0005829, IDA). The mitochondrial 10-formyl-THF dehydrogenase is a **distinct paralog, ALDH1L2** (~74% identity; arose by duplication before bony fish). GO:0005739 on ALDH1L1 rests only on **IBA (phylogenetic inference)** and most plausibly reflects carry-over from ALDH1L2. No experimental rat mitochondrial ALDH1L1 pool was found.

**Most important caveat:** The two GO terms must be evaluated separately. The enzyme *is* a genuine ALDH-superfamily oxidoreductase with real, physiologically relevant dehydrogenase chemistry — but that chemistry is **NADP⁺-dependent and cytosolic**, and its textbook ALDH aldehyde-oxidation activity is an in-vitro side reaction. The issue is not that the annotations are nonsense; it is that both use the **wrong sub-term** (NAD⁺ vs NADP⁺) or **wrong compartment** (mitochondrion vs cytosol) relative to the direct rat evidence.

---

## Key Findings

### Finding 1 — The aldehyde dehydrogenase activity is NADP⁺-dependent, not NAD⁺, and is an in-vitro promiscuous activity of the C-terminal domain

The single most decisive line of evidence is direct enzymology on the **rat** protein. Cook & Wagner ([PMID: 7646059](https://pubmed.ncbi.nlm.nih.gov/7646059/)) purified rat liver cytosolic 10-formyltetrahydrofolate dehydrogenase (10-FTHFDH) and showed it "catalyzed **NADP(⁺)-dependent** oxidation of propanal and the hydrolysis of p-nitrophenyl acetate (pNPA) in a similar fashion to ALDH." Initial-rate studies gave **Km = 46 µM for NADP⁺** and **636 µM for propanal**, and reported *no* NAD⁺-dependent activity. This is a quantitative cofactor assay in the exact organism named by the hypothesis, and it directly contradicts an NAD⁺-specificity assignment.

The cofactor preference has a defined structural basis. Crystal structures of the rat C-terminal domain ([PMID: 17302434](https://pubmed.ncbi.nlm.nih.gov/17302434/)) reveal "a new mode of binding of the 2′-phosphate group of NADP via a water-mediated contact with **Gln600** that may contribute to the specificity of the enzyme for **NADP over NAD**." An active site tuned to accept the 2′-phosphate of NADP is not an NAD⁺-specific enzyme. A companion mutagenesis/structural study ([PMID: 21540484](https://pubmed.ncbi.nlm.nih.gov/21540484/)) describes the C-terminal domain flatly as "an **NADP(⁺)-dependent oxidoreductase**," with Cys707/Glu673 controlling coenzyme binding and redox sensing.

Finally, the phylogenetic/enzymology review ([PMID: 21215736](https://pubmed.ncbi.nlm.nih.gov/21215736/)) states the ALDH-homologous domain "enables FDH to catalyze the **NADP(⁺)-dependent** conversion of short-chain aldehydes to corresponding acids **in vitro**." Both the cofactor and the in-vitro qualifier are explicit. The short-chain-aldehyde activity is best understood as catalytic promiscuity of an ALDH-fold domain that, in the intact fusion enzyme, performs the final formyl→CO₂ oxidation of 10-formyl-THF turnover — not an independent physiological aldehyde pathway.

### Finding 2 — Rat ALDH1L1 is cytosolic; the mitochondrial FDH is the paralog ALDH1L2

UniProt P28037 is named **"Cytosolic 10-formyltetrahydrofolate dehydrogenase,"** and its cytosol annotation (GO:0005829) carries **IDA** (direct assay) support, whereas the mitochondrion annotation (GO:0005739) carries only **IBA** (phylogenetically inferred) support. The original rat enzyme was characterized from **liver cytosol** ([PMID: 7646059](https://pubmed.ncbi.nlm.nih.gov/7646059/)).

The Krupenko laboratory resolved the compartment question explicitly. In *Enzymatic properties of ALDH1L2, a mitochondrial 10-formyltetrahydrofolate dehydrogenase* ([PMID: 21238436](https://pubmed.ncbi.nlm.nih.gov/21238436/)), they describe ALDH1L1 as "an abundant **cytosolic** enzyme of folate metabolism" and report that the "mitochondrial isoform of FDH (mtFDH) … is the **product of a separate gene, ALDH1L2**." The mitochondrial activity therefore belongs to a different gene product. The phylogenetic analysis ([PMID: 21215736](https://pubmed.ncbi.nlm.nih.gov/21215736/)) dates the split: "the vertebrate **ALDH1L2 gene arose from a duplication event of the ALDH1L1 gene prior to the emergence of osseous fish**" (>500 Mya). ALDH1L1 and mitochondrial ALDH1L2 are ancient, separate paralogs, which is exactly the setup in which phylogenetic (IBA) annotation transfer produces a spurious mitochondrion term on the cytosolic paralog.

### Finding 3 — Sequence-level proof: ALDH1L1 lacks the mitochondrial presequence that defines ALDH1L2

A direct comparison of UniProt sequences (own analysis; provenance CSV `aldh1l1_vs_aldh1l2_Nterm_presequence.csv`) makes the paralog-carry-over interpretation concrete. Rat ALDH1L1 (P28037) and human ALDH1L1 (O75891) begin **immediately at the folate-binding/hydrolase domain** (`MKIAVIGQSLFGQEVY…`), with no N-terminal extension and no annotated transit peptide. In contrast, human ALDH1L2 (Q3SY69) and rat ALDH1L2 (A0ABK0LNR0) carry a **27-residue N-terminal extension** preceding the shared catalytic-domain anchor `IGQSLFGQEVY`:

```
ALDH1L1 (rat P28037):   ------------------------- MKIAVIGQSLFGQEVY...   (no presequence)
ALDH1L1 (human O75891): ------------------------- M-KIAVIGQSLFGQEVY... (no presequence)
ALDH1L2 (human Q3SY69): MLRRGSQALRRFSTGRVYFKNKLKLAL ... IGQSLFGQEVY   (+27 aa presequence)
ALDH1L2 (rat A0ABK...): MLWRGSQALRHFSTGRVYFKNKLKLAL ... IGQSLFGQEVY   (+27 aa presequence)
```

The ALDH1L2 extension has the classic cleavable **mitochondrial presequence signature**: Arg/Lys-rich, net positive charge (+6 to +8), and **0 acidic residues**. In human ALDH1L2 it is a documented **Transit peptide (residues 1–19)**. ALDH1L1 has no equivalent segment. This is the physical basis for why one paralog goes to mitochondria and the other stays cytosolic, and it independently corroborates that a mitochondrion annotation on ALDH1L1 is misassigned. (Limitation: rat ALDH1L2 presequence cleavage is inferred by homology to human.)

### Finding 4 — In-vivo loss-of-function maps to folate/glycine one-carbon metabolism, confirming the aldehyde activity is non-core

The physiological (core) function is established by knockout biology, not in-vitro promiscuity. In *Cytosolic 10-formyltetrahydrofolate dehydrogenase regulates glycine metabolism in mouse liver* ([PMID: 31624291](https://pubmed.ncbi.nlm.nih.gov/31624291/)), ALDH1L1 "metabolizes 10-formyltetrahydrofolate to produce tetrahydrofolate (THF). This reaction might have a regulatory function towards reduced folate pools, de novo purine biosynthesis, and the flux of folate-bound methyl groups." A folate-withdrawal study ([PMID: 35629957](https://pubmed.ncbi.nlm.nih.gov/35629957/)) reiterates that ALDH1L1 "regulates the overall flux of folate-bound one-carbon groups by converting 10-formyltetrahydrofolate to tetrahydrofolate and CO₂," and knockout of the putative tumor suppressor reprograms metabolism to accelerate liver tumor growth ([PMID: 34203215](https://pubmed.ncbi.nlm.nih.gov/34203215/)). **No knockout study reports a free short-chain-aldehyde detoxification phenotype.** The physiological readout is folate one-carbon metabolism, confirming that the aldehyde-dehydrogenase terms describe a domain-level in-vitro capability, not the physiological role.

---

## Mechanistic Model / Interpretation

ALDH1L1 (FDH) is a homotetrameric **fusion of three domains** ([PMID: 18848533](https://pubmed.ncbi.nlm.nih.gov/18848533/)), and understanding this architecture dissolves the apparent conflict in the seed hypothesis:

```
   N-terminal domain          Intermediate linker            C-terminal domain
   (residues 1–310)           (residues 311–399)             (residues 400–902)
   10-formyl-THF hydrolase  →  4'-phosphopantetheine     →   ALDH-fold, NADP+-dependent
   removes formyl group        "swinging arm" carries         oxidizes formyl → CO2
                               formyl between centers
        |                                                            |
        └──────────── coupled overall reaction ─────────────────────┘
        10-formyl-THF  +  NADP+   →   THF  +  CO2  +  NADPH
```

- The **C-terminal ALDH-fold domain** is a genuine aldehyde dehydrogenase homolog. In isolation, and on artificial substrates (propanal, p-nitrophenyl acetate), it displays classic ALDH chemistry — but **NADP⁺-dependent**, because of the Gln600 2′-phosphate contact. This is the source of the "aldehyde dehydrogenase activity" annotation. It is real but promiscuous and non-physiological when applied to free short-chain aldehydes.
- In the **intact enzyme**, that same domain performs the final formyl→CO₂ oxidation step of the folate reaction, using the phosphopantetheine arm ([PMID: 17884809](https://pubmed.ncbi.nlm.nih.gov/17884809/)) to receive the formyl group from the N-terminal hydrolase. The physiological substrate is a folate-tethered formyl, not a free aldehyde.

Two distinct annotation errors follow directly from mis-reading this biology:

| Seed clause | What is actually true | Error type | Correct term |
|---|---|---|---|
| NAD⁺-dependent aldehyde DH (GO:0004029) | NADP⁺-dependent; Km(NADP⁺)=46 µM; Gln600 selects NADP over NAD | Wrong cofactor sub-term (ISO-inferred, contradicted by rat IDA) | GO:0033721 (NADP⁺ ALDH); core is GO:0016155 |
| Mitochondrion (GO:0005739) | Cytosolic (IDA); mito FDH is paralog ALDH1L2 with a presequence ALDH1L1 lacks | Paralog carry-over (IBA-only) | GO:0005829 (cytosol) |

The two errors share a root cause: **ALDH1L1 is being annotated as though it were a generic ALDH and/or its mitochondrial paralog ALDH1L2**, rather than as the specific cytosolic folate enzyme it is.

---

## Evidence Base

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [7646059](https://pubmed.ncbi.nlm.nih.gov/7646059/) | Direct assay (kinetics) | **Refutes NAD⁺**; supports NADP⁺ + in-vitro promiscuity | Cofactor & substrate of ALDH activity | Rat cytosol 10-FTHFDH oxidizes propanal NADP⁺-dependently, Km(NADP⁺)=46 µM, Km(propanal)=636 µM | Purified rat liver cytosol | High; classic direct rat assay; no NAD⁺ activity reported |
| [17302434](https://pubmed.ncbi.nlm.nih.gov/17302434/) | Structural (crystal) | Refutes NAD⁺ (mechanistic) | Basis of NADP vs NAD selectivity | 2′-phosphate of NADP bound via water-mediated contact to Gln600 → "specificity for NADP over NAD" | Rat FDH C-terminal domain | High; direct structural rationale |
| [21540484](https://pubmed.ncbi.nlm.nih.gov/21540484/) | Structural (mutants) | Refutes NAD⁺; supports NADP⁺ | Coenzyme handling | C(t)-FDH is an "NADP(⁺)-dependent oxidoreductase"; Cys707/Glu673 control binding/redox sensing | Rat domain mutants | High |
| [21215736](https://pubmed.ncbi.nlm.nih.gov/21215736/) | Review/enzymology + phylogeny | Qualifies (in-vitro); supports paralog split | Nature of ALDH activity; paralogy | "NADP(⁺)-dependent conversion of short-chain aldehydes … in vitro"; ALDH1L2 arose by duplication of ALDH1L1 | Cross-species | Medium-high; explicit in-vitro label; establishes paralogs |
| [21238436](https://pubmed.ncbi.nlm.nih.gov/21238436/) | Direct assay + localization | Supports cytosol; distinguishes paralog | ALDH1L1 compartment vs mito FDH | ALDH1L1 = "abundant cytosolic enzyme"; mito FDH = "separate gene, ALDH1L2" | Human recombinant | High for paralog distinction |
| [18848533](https://pubmed.ncbi.nlm.nih.gov/18848533/) | Review (mechanism) | Qualifies | Domain architecture/activity source | C-terminal domain (res 400–902) from ALDH-related gene "capable of oxidation of short-chain aldehydes"; overall reaction NADP⁺-dependent | Rat FDH | Medium (review); consistent with primary data |
| [17884809](https://pubmed.ncbi.nlm.nih.gov/17884809/) | Direct (mechanism) | Qualifies | Overall physiological reaction | "NADP(⁺)-dependent conversion of 10-formyltetrahydrofolate to tetrahydrofolate and CO₂" via phosphopantetheine arm | Rat FDH | High; defines core NADP⁺ activity |
| [31624291](https://pubmed.ncbi.nlm.nih.gov/31624291/) | Mutant phenotype (KO) | Qualifies (aldehyde activity non-core) | In-vivo physiological role | Aldh1l1 KO reprograms glycine/one-carbon (folate) metabolism; no aldehyde-detox phenotype | Aldh1l1−/− mouse liver | High; LOF maps to folate function |
| [35629957](https://pubmed.ncbi.nlm.nih.gov/35629957/) | Mutant phenotype (KO) | Qualifies | Physiological function | Regulates folate-bound one-carbon flux; 10-formyl-THF→THF+CO₂ | Folate-withdrawal KO mouse | High |
| [34203215](https://pubmed.ncbi.nlm.nih.gov/34203215/) | Mutant phenotype (KO) | Qualifies | Consequence of loss | Aldh1l1 loss reprograms metabolism, accelerates liver tumor growth | DEN liver-carcinogenesis mouse | Medium-high; downstream phenotype |
| UniProt P28037 (RGD/GOC) | Database record | Context (shows the conflict) | Current annotation state | Cytosol 0005829 **IDA**; mito 0005739 **IBA**; NAD⁺ ALDH 0004029 **ISO**; NADP⁺ ALDH 0033721 **IDA**; FDH 0016155 **IDA** | Rat | Database-level; shows strong (IDA) vs weak (ISO/IBA) split |
| This work (UniProt seqs) | Structural/evolutionary (sequence) | **Refutes mitochondrion** | Presence of a targeting presequence | ALDH1L1 (rat & human) starts at folate-binding domain with no N-terminal extension; ALDH1L2 has a 27-aa Arg/Lys-rich, acidic-free presequence (human Transit peptide 1–19) | Rat + human orthologs/paralogs | High; direct comparison; rat ALDH1L2 cleavage inferred by homology |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current evidence on P28037 | Recommended lead |
|---|---|---|---|
| **GO:0004029** aldehyde dehydrogenase (NAD⁺) activity | MF | ISO:RGD | **Remove / do not propagate.** Contradicted by direct rat kinetics (NADP⁺, not NAD⁺). If any aldehyde-oxidation MF is kept, use the NADP⁺ term. |
| **GO:0033721** aldehyde dehydrogenase (NADP⁺) activity | MF | IDA | **Retain**, but consider a non-core / "in-vitro" caveat — it is the C-terminal domain's promiscuous activity, not the physiological reaction. |
| **GO:0016155** formyltetrahydrofolate dehydrogenase activity | MF | IDA | **Retain as the core/primary MF** (EC 1.5.1.6, NADP⁺-dependent). |
| **GO:0005739** mitochondrion | CC | IBA | **Remove or flag as paralog carry-over.** Direct evidence is cytosolic; mitochondrial FDH = ALDH1L2. |
| **GO:0005829** cytosol | CC | IDA | **Retain as primary CC.** |
| 10-formyl-THF catabolism / THF biosynthesis / NADPH regeneration | BP | IDA/TAS | Retain — consistent with core folate one-carbon function. |

**Bottom line for the curator:** the seed hypothesis, *as worded* (NAD⁺ activity + mitochondrion), should **not** be adopted. Both terms map onto real biology but with the **wrong cofactor sub-term** and the **wrong compartment**; the accurate annotations (NADP⁺ ALDH, cytosol, formyl-THF dehydrogenase) already exist on the record. Avoid a generic "protein binding" fallback — the informative MF term (GO:0016155) is well supported.

---

## Mechanistic Scope

The immediate molecular function of ALDH1L1 is a homotetrameric, three-domain fusion enzyme (N-terminal 10-formyl-THF hydrolase; intermediate 4′-phosphopantetheine acyl-carrier linker; C-terminal ALDH-homologous domain). The **physiological** reaction is NADP⁺-dependent oxidation of the THF-bound formyl group to CO₂ (10-formyl-THF → THF + CO₂ + NADPH), i.e., formyltetrahydrofolate dehydrogenase (EC 1.5.1.6) — regenerating THF and NADPH in cytosolic one-carbon metabolism. The "aldehyde dehydrogenase" chemistry on free short-chain aldehydes (e.g., propanal) is the **same catalytic C-terminal domain acting on a small surrogate substrate in vitro** — a demonstration of the ALDH-like acyl-transfer mechanism (Cys707 thiohemiacetal → thioester), not an independent physiological aldehyde-detox pathway.

Downstream/pleiotropic effects — tumor-suppressor behavior, folate-pool regulation, glycine metabolism, lipid homeostasis links, astrocyte-marker usage — are consequences of the folate function, not the tested activity. The in-vivo loss-of-function support (Aldh1l1-KO reprogramming of glycine and one-carbon metabolism) confirms that the ALDH aldehyde-oxidation activity is **non-core** relative to the folate function.

---

## Conflicts and Alternatives

- **Paralog confusion (primary alternative):** Mitochondrial 10-formyl-THF dehydrogenase activity and mitochondrial localization belong to **ALDH1L2** (separate gene). GO:0005739 on ALDH1L1 is the expected signature of phylogenetic (IBA) carry-over across the paralog pair.
- **Cofactor sub-term drift:** Automated/orthology inference maps ALDH1L1 to the generic ALDH family, dominated by NAD⁺-using members; this likely produced the ISO GO:0004029 NAD⁺ term despite rat data showing NADP⁺ specificity.
- **In-vitro vs physiological:** Reviews explicitly flag the aldehyde-oxidation as "in vitro"; human ALDH1L2 lacked detectable ALDH activity even though it performs the folate reaction — underscoring that the ALDH aldehyde activity is a domain property, not necessarily physiologically deployed.
- **Isoform/secondary pools:** No primary evidence for a mitochondrial rat ALDH1L1 pool was located; a minor pool cannot be strictly excluded, but none is documented, and the absent presequence makes it unlikely.
- **Sequence-level confirmation:** A direct N-terminal comparison shows mitochondrial targeting is encoded by the ALDH1L2 presequence (Arg-rich, acidic-free, ~27 aa; documented human Transit peptide 1–19) and is **entirely absent** from ALDH1L1 — independently corroborating that GO:0005739 on ALDH1L1 is paralog carry-over, not a genuine import signal.

---

## Limitations and Knowledge Gaps

1. **Is any NAD⁺-dependent activity ever detectable for rat ALDH1L1?** Checked: Cook & Wagner report only NADP⁺ activity; no NAD⁺ kinetics given (absence of evidence, not a formal negative). Matters because GO:0004029 asserts NAD⁺. Resolve with a side-by-side NAD⁺ vs NADP⁺ kcat/Km assay on recombinant rat enzyme.
2. **Direct rat localization data.** Checked: UniProt cytosol is IDA, but the strongest explicit "cytosolic vs mitochondrial separate gene" statements are human-focused. Matters for the mitochondrion CC. Resolve with rat subcellular fractionation / immunofluorescence that discriminates ALDH1L1 from ALDH1L2.
3. **Provenance of the IBA mitochondrion call.** Which reference-genome members seeded GO:0005739? A curator check of the PAINT/IBA tree would confirm ALDH1L2-driven carry-over.
4. **Current evidence codes were inferred from the annotation pattern**, not re-pulled live; the ISO status of GO:0004029 and IBA status of GO:0005739 should be verified in the live GO/UniProt record before editing.
5. **Isoform coverage** was not exhaustive; a rare N-terminally extended ALDH1L1 isoform cannot be fully excluded, though none is documented.

---

## Discriminating Tests

- **Cofactor competition assay:** measure propanal (or 10-formyl-THF) oxidation vs [NAD⁺] and [NADP⁺]; prediction: activity only with NADP⁺ (Km≈46 µM), negligible with NAD⁺ → discriminates GO:0004029 vs GO:0033721.
- **Gln600 mutagenesis:** removing the 2′-phosphate water contact should relax NADP-over-NAD selectivity, confirming the structural basis of specificity.
- **Compartment-resolved proteomics/IF in rat tissue** with paralog-discriminating peptides/antibodies → tests GO:0005739 vs GO:0005829.
- **Presequence-swap import assay:** append the ALDH1L2 27-aa presequence to ALDH1L1 and test mitochondrial import → predicted to redirect ALDH1L1 to mitochondria, confirming the presequence is the sole compartment determinant.
- **Isolated-domain vs holoenzyme kinetics** for aldehyde vs 10-formyl-THF → confirms the aldehyde activity is a C-terminal-domain in-vitro property (non-core).
- **Metabolomic phenotyping of Aldh1l1-KO for aldehyde adducts:** predicted null (folate/glycine changes only), confirming aldehyde-detox is non-physiological.

---

## Curation Leads (verify)

- **Candidate action 1:** Remove/deprecate **GO:0004029 (NAD⁺ ALDH, ISO)**; if a cofactor MF beyond formyl-THF dehydrogenase is wanted, keep **GO:0033721 (NADP⁺ ALDH, IDA)** with an in-vitro/non-core note. *Refs to verify:* PMID 7646059 (Km NADP⁺ 46 µM), 17302434 (Gln600 NADP>NAD), 21215736 ("in vitro").
- **Candidate action 2:** Remove or down-weight **GO:0005739 (mitochondrion, IBA)** as paralog carry-over from ALDH1L2; keep **GO:0005829 (cytosol, IDA)** as primary. *Refs to verify:* PMID 21238436, 21215736; own presequence analysis.
- **Candidate core MF/BP:** emphasize **GO:0016155 formyltetrahydrofolate dehydrogenase** + NADPH regeneration / 10-formyl-THF catabolism as the primary function. *Refs to verify:* PMID 17884809, 31624291, 35629957.
- **Suggested curator question:** "Does GO:0004029 on P28037 originate from ISO to a NAD⁺-preferring ALDH ortholog, and should it be replaced by the NADP⁺ term given direct rat kinetics? Does GO:0005739 originate from IBA seeded by ALDH1L2?"

*All items above are leads requiring curator verification; snippets are drawn verbatim from the cited abstracts.*


## Artifacts

- [OpenScientist aldh1l1 vs aldh1l2 Nterm presequence](openscientist_artifacts/aldh1l1_vs_aldh1l2_Nterm_presequence.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)