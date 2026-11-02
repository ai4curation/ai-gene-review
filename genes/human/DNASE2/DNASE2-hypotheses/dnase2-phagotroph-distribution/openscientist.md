---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-26T20:07:25.501226'
end_time: '2026-10-26T21:19:19.982347'
duration_seconds: 4314.48
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: DNASE2
  gene_symbol: DNASE2
  uniprot_accession: O00115
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: dnase2-phagotroph-distribution
  hypothesis_text: 'DNase II family enzymes (PANTHER PTHR10858), which digest the
    DNA of engulfed cells in animal phagolysosomes, are present in phagotrophic protists
    (for example Dictyostelium discoideum, Acanthamoeba, choanoflagellates), consistent
    with digestion of phagocytosed DNA being an ancestral eukaryotic function. Test
    with one analysis: the phylogenetic distribution of DNase II homologs across eukaryotic
    reference proteomes, noting lineages that lack it.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/DNASE2/DNASE2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'DNase II family enzymes (PANTHER PTHR10858),\
    \ which digest the DNA of engulfed cells in animal\n  phagolysosomes, are present\
    \ in phagotrophic protists (for example Dictyostelium discoideum, Acanthamoeba,\n\
    \  choanoflagellates), consistent with digestion of phagocytosed DNA being an\
    \ ancestral eukaryotic function.\n  Test with one analysis: the phylogenetic distribution\
    \ of DNase II homologs across eukaryotic reference\n  proteomes, noting lineages\
    \ that lack it.'\nfocus_type: free_text\ncontext: []\nreference_id: []"
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
- **Gene directory:** DNASE2
- **Gene symbol:** DNASE2
- **UniProt accession:** O00115

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** dnase2-phagotroph-distribution
- **Source file:** genes/human/DNASE2/DNASE2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

DNase II family enzymes (PANTHER PTHR10858), which digest the DNA of engulfed cells in animal phagolysosomes, are present in phagotrophic protists (for example Dictyostelium discoideum, Acanthamoeba, choanoflagellates), consistent with digestion of phagocytosed DNA being an ancestral eukaryotic function. Test with one analysis: the phylogenetic distribution of DNase II homologs across eukaryotic reference proteomes, noting lineages that lack it.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'DNase II family enzymes (PANTHER PTHR10858), which digest the DNA of engulfed cells in animal
  phagolysosomes, are present in phagotrophic protists (for example Dictyostelium discoideum, Acanthamoeba,
  choanoflagellates), consistent with digestion of phagocytosed DNA being an ancestral eukaryotic function.
  Test with one analysis: the phylogenetic distribution of DNase II homologs across eukaryotic reference
  proteomes, noting lineages that lack it.'
focus_type: free_text
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

# DNASE2 Phagotroph Distribution Hypothesis — Deep Research Report

**Target gene:** DNASE2 (human), UniProt **O00115**
**Family:** InterPro **IPR004947** = PANTHER **PTHR10858** = Pfam **PF03265**
**Hypothesis slug:** `dnase2-phagotroph-distribution`
**Focus type:** free_text (evolutionary / phylogenetic distribution)
**Source review:** `genes/human/DNASE2/DNASE2-ai-review.yaml`

---

## Summary

The seed hypothesis proposes that DNase II family enzymes — which digest the DNA
of engulfed cells in animal phagolysosomes — are present in phagotrophic protists
(*Dictyostelium discoideum*, *Acanthamoeba*, choanoflagellates), and that this
distribution is "consistent with digestion of phagocytosed DNA being an ancestral
eukaryotic function." The requested test was the phylogenetic distribution of
DNase II homologs across eukaryotic reference proteomes.

I evaluated this by tabulating InterPro/UniProt protein counts for family
**IPR004947** (equivalently PANTHER **PTHR10858** / Pfam **PF03265**) across major
eukaryotic lineages, with protein-level identity audits of surprising hits and a
proteome-coverage control for the key negative example. The verdict is **partially
supported**. Two of the three named phagotroph examples are genuine:
*Dictyostelium discoideum* encodes a real ~14-member family expansion and
*Acanthamoeba castellanii* encodes 3 bona fide members. The family is indeed
ancient and broadly eukaryotic (5,031 eukaryotic proteins across 1,423 reference
proteomes), reaching Amoebozoa, land plants, ciliates and stramenopiles. However,
the **third named example — choanoflagellates — is refuted**: both well-sequenced
species (*Monosiga brevicollis*, *Salpingoeca rosetta*) lack the family entirely,
and this is not a proteome-coverage artifact.

More importantly, the **evolutionary interpretation is only weakly supported**.
Presence of the family does not track phagotrophy: non-phagotrophic land plants
retain a robust complement (72 proteins) while several phagotrophic lineages
(kinetoplastids, *Giardia*/Fornicata, and the choanoflagellates themselves) have
lost it. The pattern is best explained as an **ancient eukaryotic family subject
to many independent lineage-specific losses**, not as a clean marker of an
ancestral phagocytic-DNA-digestion function. For curation, the evolutionary
free-text should be **narrowed and the choanoflagellate claim corrected**; this
observation is orientation/context only and **should not by itself drive any GO
term change** on the human DNASE2 record.

---

## Key Findings

### Finding 1 — The DNase II family is patchily distributed across eukaryotes: present in Amoebozoan phagotrophs but absent from choanoflagellates

Using the EBI InterPro and UniProt REST APIs, I tabulated protein counts for
family **IPR004947** (= PTHR10858 = PF03265) across major eukaryotic taxa. The
family totals **5,031 proteins in Eukaryota**, distributed across **1,423
reference proteomes** — confirming a deep, broad eukaryotic presence.

| Lineage | DNase II proteins (IPR004947) | Phagotroph? | Status |
|---|---|---|---|
| Metazoa | 4,603 | Mixed | Present (dominant) |
| Amoebozoa (total) | 157 | Yes | **Present** |
| — *Dictyostelium discoideum* | 14 | Yes | Present (family expansion) |
| — *Acanthamoeba castellanii* | 3 | Yes | Present |
| Viridiplantae (land plants/algae) | 72 | **No** | Present |
| Stramenopiles | 62 | Mixed | Present |
| Ciliophora | 55 | Yes | Present |
| *Capsaspora* | 1 | Yes | Present |
| Choanoflagellata | **0** | **Yes** | **Absent** |
| Fungi | 1 (spurious) | No | Effectively absent |
| Apicomplexa | 0 | No/parasitic | Absent |
| Kinetoplastida | 0 | **Yes** | Absent |
| Rhodophyta | 0 | No | Absent |
| Fornicata / *Giardia* | 0 | **Yes** | Absent |

The choanoflagellate absence was explicitly tested against a **proteome-coverage
control**: *Monosiga brevicollis* (9,331 UniProt proteins) and *Salpingoeca
rosetta* (12,235 UniProt proteins) both have well-populated proteomes, so a count
of zero DNase II proteins reflects a **genuine evolutionary loss**, not missing
sequence data.

This finding simultaneously **supports** the hypothesis for the two named amoebae
and **refutes** it for choanoflagellates. It also undercuts the deeper inference:
phagotrophy does not predict presence, because several phagotrophic lineages lack
the family while non-phagotrophic land plants retain it.

The *function* the hypothesis attributes to the family is itself well established.
The DNase II review states that *"Its lysosomal localization and ubiquitous tissue
distribution suggested that this enzyme played a role in the degradation of
exogenous DNA encountered by phagocytosis"*
([PMID: 14644493](https://pubmed.ncbi.nlm.nih.gov/14644493/)). In an invertebrate
gut, a DNase II homolog digests engulfed/dietary bacterial DNA — DNase II
homologs *"both fail to replace nuc-1 in degrading bacterial DNA in intestine"*
([PMID: 19809494](https://pubmed.ncbi.nlm.nih.gov/19809494/)). These confirm the
engulfed-DNA digestion role beyond mammals but do **not** establish that this
function is ancestral or phagotrophy-linked across the eukaryotic tree.

### Finding 2 — Protein-level identity checks confirm genuine DNase II in amoebae and plants, and show the sole fungal "hit" is spurious — strengthening the loss pattern

Because InterPro signature matches can occasionally be incidental, each surprising
hit was inspected at the protein-annotation level:

- **Dictyostelium discoideum** hits are annotated *"Deoxyribonuclease II"* and
  *"Deoxyribonuclease II family protein"* (e.g., C7G058, Q54FV5) — confirming a
  genuine ~14-member family expansion rather than low-quality matches.
- **Viridiplantae** hits include real, functionally named members:
  *"Cell-death-related nuclease 7"*, *"Plancitoxin-1"*, and
  *"Deoxyribonuclease-2-alpha"* — bona fide DNase II enzymes in a
  non-phagotrophic lineage.
- The single **Fungi** hit (A0A2H9TI56) is annotated *"Repressor of RNA polymerase
  III transcription"* — an incidental/spurious signature match, **not** a true
  DNase II. Fungi are therefore effectively devoid of the family.

This audit removes the one apparent counter-example to fungal loss, confirms that
plant retention is real, and verifies that the Dictyostelium expansion is
authentic. Together these sharpen the conclusion that the presence/absence pattern
is driven by **repeated independent losses** of an ancient family rather than by
phagotrophic lifestyle.

### Finding 3 — The catalytic domain is not strictly eukaryote-specific

An outgroup query of IPR004947 returned **Bacteria 66, Archaea 0, Viruses 6**
against Eukaryota 5,031. The family is overwhelmingly eukaryotic but not strictly
eukaryote-restricted; sparse bacterial members suggest a deeper domain origin or
horizontal transfer. This is a minor qualifier to the seed's phrase "ancestral
**eukaryotic** function": the catalytic domain may predate or extend beyond
eukaryotes even though the lysosomal/phagolysosomal DNA-digestion *role* is a
eukaryotic elaboration. It does not change the core verdict.

---

## Mechanistic Model / Interpretation

The molecular function under test is narrow and well-defined: DNase II–family
enzymes are **acid (lysosomal/phagolysosomal) endonucleases** that cleave DNA at
low pH without divalent-cation dependence, degrading DNA delivered into the
lysosome — from apoptotic/engulfed cells, phagocytosed microbes, or dietary
sources. The hypothesis takes this well-supported function and makes an
**evolutionary extrapolation**: that the enzyme's distribution should mark
phagotrophy as an ancestral eukaryotic activity.

The data support a more parsimonious model:

```
                 Ancient DNase II family (domain predates/spans eukaryotes;
                             sparse bacterial members)
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
   RETAINED                     RETAINED                       LOST (independently,
   in many phagotrophs          in NON-phagotrophs             many lineages)
   (Dictyostelium 14,           (land plants 72,               Choanoflagellata 0
    Acanthamoeba 3,              stramenopiles 62)             Fungi ~0 (spurious)
    ciliates 55)                                               Kinetoplastida 0
                                                               Apicomplexa 0
                                                               Giardia/Fornicata 0
                                                               Rhodophyta 0

   ⇒ Distribution = "ancient family + many lineage-specific losses"
   ⇒ NOT "clean marker of phagotrophic DNA digestion"
```

Key logical points:

1. **Presence in phagotrophs is consistent with — but not diagnostic of — an
   ancestral phagocytic role.** Dictyostelium and Acanthamoeba fit, but the
   inference is confounded by the exceptions below.
2. **Retention in non-phagotrophic plants** shows the family is maintained for
   functions unrelated to phagocytosis (e.g., programmed-cell-death nucleases).
3. **Loss in multiple phagotrophs** (choanoflagellates, kinetoplastids, *Giardia*)
   shows phagotrophy can proceed without this specific family — other acid
   nucleases can substitute.
4. **Sparse bacterial members** indicate the catalytic domain's deep origin,
   offering an alternative to a strictly eukaryotic-phagotrophic framing.

The correct framing for curation is therefore **evolutionary context, not
mechanistic evidence for the human gene's GO annotations.** Human DNASE2 function
(lysosomal DNA catabolism, clearance of DNA from engulfed apoptotic cells and
erythroid nuclei) is established by direct mammalian and invertebrate experiments;
the cross-eukaryote distribution neither adds to nor subtracts from those
annotations.

---

## Evidence Base

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| InterPro/UniProt REST (IPR004947 = PTHR10858 = PF03265), computed this study | Structural/evolutionary, computational | **Qualifies** (supports in part, refutes in part) | Phylogenetic distribution across eukaryotes | 5,031 euk. proteins, 1,423 proteomes; present in Amoebozoa (Dicty 14, Acanthamoeba 3), plants 72, ciliates 55, stramenopiles 62; **absent in Choanoflagellata (0), Fungi (~0), Kinetoplastida, Apicomplexa, Giardia, Rhodophyta** | Pan-eukaryotic DB survey, UniProtKB 2026-10 | High for counts; family-signature counts are not a formal phylogeny; paralog inflation possible |
| InterPro/UniProt coverage check, this study | Computational | **Refutes** (choanoflagellate example) | Is choanoflagellate absence real? | M. brevicollis 9,331 & S. rosetta 12,235 proteins present → absence genuine | UniProtKB | High that it is not a coverage gap; a highly divergent homolog cannot be fully excluded without HMM search |
| InterPro/UniProt protein annotations (identity audit), this study | Computational / database | **Supports** (data-quality) | Are hits genuine DNase II? | Dicty & plant hits are real DNase II; sole fungal hit is spurious ("Repressor of RNA Pol III") | Protein-level review | High; annotation-based, not experimentally verified per protein |
| [PMID: 14644493](https://pubmed.ncbi.nlm.nih.gov/14644493/) | Review/database | **Supports** (function premise) | DNase II digests phagocytosed/exogenous DNA in lysosome | *"lysosomal localization… role in the degradation of exogenous DNA encountered by phagocytosis"* | Mammalian DNase II | Review-level; establishes function, not evolutionary claim |
| [PMID: 19809494](https://pubmed.ncbi.nlm.nih.gov/19809494/) | Mutant phenotype / direct | **Supports** (function in invertebrate) | DNase II homologs digest engulfed bacterial DNA | Homologs *"fail to replace nuc-1 in degrading bacterial DNA in intestine"* | *C. elegans* gut | Moderate-high; invertebrate, nuc-1-specific |
| [PMID: 12718884](https://pubmed.ncbi.nlm.nih.gov/12718884/) | Mutant phenotype (RNAi) | **Qualifies** | DNase II in apoptotic DNA degradation | NUC-1 (DNase II) among nucleases degrading chromosomal DNA in apoptosis | *C. elegans* | Function support; not phylogenetic |
| [PMID: 26182365](https://pubmed.ncbi.nlm.nih.gov/26182365/) | Localization / mutant | **Qualifies** | Autonomous vs non-autonomous DNase II action | NUC-1 is major DNase II degrading apoptotic DNA; ~3–7× non-autonomous:autonomous | *C. elegans* embryos | Function support; mechanistic |
| [PMID: 26251453](https://pubmed.ncbi.nlm.nih.gov/26251453/) | Mutant phenotype | **Qualifies** | DNase II paralogs (nuc-1, crn-6, crn-7) in germ-cell apoptosis | Three DNase II paralogs with distinct roles | *C. elegans* gonad | Illustrates metazoan paralog expansion |
| [PMID: 41805323](https://pubmed.ncbi.nlm.nih.gov/41805323/) | Direct assay | **Qualifies/Supports** | DNA clearance inside phagosomes | Defective clearance of phagocytosed DNA drives inflammation; dissects phagosomal DNA processing | Mouse macrophages | High; mammalian, confirms phagosomal context |
| [PMID: 42901880](https://pubmed.ncbi.nlm.nih.gov/42901880/) | Human genetics (case) | **Qualifies** | DNASE2 loss causes autoinflammation | AIPCS from biallelic DNASE2 mutation; interferonopathy | Human patient | Downstream disease role, not evolutionary |

---

## GO Curation Implications

**Likely curation action (lead — requires curator verification):** *Narrow and
correct the evolutionary free-text; make no GO term change driven by this
hypothesis.*

- **No MF change.** Deoxyribonuclease II activity (GO:0004531; acid,
  cation-independent endonuclease) is established by direct biochemistry and is
  unaffected by the distribution survey. **Retain.**
- **No BP change.** DNA catabolism in the context of engulfed/apoptotic DNA
  (e.g., GO:0006308 "DNA catabolic process"; apoptotic-cell-clearance–associated
  DNA degradation) is supported by direct metazoan genetics (PMIDs 19809494,
  26182365, 41805323), not by the distribution survey. Do **not** add a
  phagocytosis-pathway BP term to the human gene on evolutionary grounds alone.
  **Retain existing.**
- **No CC change.** Lysosome localization (GO:0005764) is independently
  established. **Retain.**
- **Edit the evolutionary free-text.** As written it (a) names choanoflagellates
  as a positive example when they lack the family, and (b) implies phagotrophy
  predicts presence when the distribution does not support that. Treat as
  **non-core orientation** that should not alter the gene's GO annotation set.
- **Over-annotation caution.** Lineage-specific expansions (Dictyostelium ×14)
  mean family-level presence must not be transferred as 1:1 orthology of human
  DNASE2 or of a specific sub-function.

This is a **free-text / evolutionary-context** item, not a function-assignment
item for the human gene.

---

## Mechanistic Scope

- **Direct gene-product activity (in scope, well-supported):** an acid-optimum,
  divalent-cation-independent endonuclease that cleaves dsDNA within the
  lysosome/phagolysosome. This is the immediate, cell-autonomous molecular
  function, documented biochemically in mammals and genetically in *C. elegans*.
- **Downstream phenotypes (out of scope for this evolutionary hypothesis):**
  failure of DNA clearance → undegraded cytosolic DNA → cGAS–STING/interferon
  activation → autoinflammation (human AIPCS,
  [PMID: 42901880](https://pubmed.ncbi.nlm.nih.gov/42901880/)); innate-immune gene
  upregulation in *C. elegans*
  ([PMID: 26251453](https://pubmed.ncbi.nlm.nih.gov/26251453/)). These are
  loss-of-function consequences, not evidence for the ancestral-function claim.
- **Evolutionary distribution** is an orthology/inference layer, not a direct
  functional assay; it constrains ancestry but cannot assign the ancestral
  *function*.

---

## Conflicts and Alternatives

1. **Choanoflagellate counter-evidence (direct conflict).** The seed names
   choanoflagellates as a positive example, but *Monosiga brevicollis* and
   *Salpingoeca rosetta* have zero members in well-covered proteomes — refuting a
   named example.
2. **Phagotrophy does not predict presence (interpretive conflict).** Phagotrophic
   kinetoplastids and *Giardia* lack the family; non-phagotrophic land plants
   retain it. The "ancestral phagotroph" framing is confounded.
3. **Paralog expansion / annotation inflation.** Counts reflect family-signature
   hits, including paralogs; raw counts are not a phylogeny and can overstate
   independent acquisitions. The identity audit mitigated but did not eliminate
   this.
4. **Spurious signature matches (database carry-over).** The lone fungal hit was a
   mis-annotated "Repressor of RNA Pol III," showing raw InterPro counts can
   contain false positives; single-hit "presence" needs identity checks.
5. **Deep (pre-eukaryotic) origin.** Sparse bacterial members indicate the domain
   predates eukaryotic phagotrophy, an alternative to the "ancestral eukaryotic
   phagocytic function" story.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| True absence vs divergence in choanoflagellates | UniProt coverage good (9,331 / 12,235 proteins); family count 0 | Decisive counterexample; InterPro recall could miss a divergent homolog | `hmmsearch` with the PF03265 HMM against raw *M. brevicollis* / *S. rosetta* gene models/transcriptomes |
| Family-signature counts ≠ phylogeny | Tallied IPR004947 hits per taxon | Counts inflate via paralogs/fragments; cannot time gains vs losses | ML gene tree + species-tree reconciliation (Dollo/ML) to map gain/loss events |
| Reference-proteome bias in "absent" lineages | Verified choanoflagellate coverage | Absences could be artifacts in poorly sequenced lineages | BUSCO completeness for every "absent" lineage before calling loss |
| Function–lifestyle correlation untested | Qualitative presence/absence table | The core claim is about phagotrophy linkage; no formal test run | Pagel's correlated-evolution test / phylogenetic logistic regression of presence vs phagotrophy |
| Functional confirmation in protists | Annotation-level only | Signature presence ≠ verified acid-DNase function | Acid-DNase assays or active-site conservation checks on representative protist homologs |

---

## Proposed Follow-up Experiments / Actions

### Discriminating analyses
- **Profile-HMM (PF03265) search** of raw choanoflagellate, fungal, and additional
  protist genomes to firm up presence/absence beyond InterPro annotation recall.
- **Reconciled gene tree** of PTHR10858 with Dollo/ML parsimony to count
  independent losses and test the LECA-origin hypothesis.
- **Phylogenetic comparative test** (Pagel / phylogenetic logistic regression) of
  family presence vs phagotrophic trait — the decisive test of the seed's core
  inference.
- **BUSCO completeness controls** for all "absent" lineages.
- **Functional assay:** knock out/down DNase II in *Dictyostelium* and test for
  persistence of undigested DNA in phagosomes — a direct test of the
  ancestral-function claim.

### Curation leads (verify before applying)
- **Action:** Soften/correct the free-text evolutionary statement; remove or
  reverse the claim that choanoflagellates carry DNase II. Suggested replacement:
  *"DNase II (IPR004947 / PTHR10858 / PF03265) is an ancient, broadly distributed
  eukaryotic family subject to many independent losses. It is present in
  phagotrophic amoebae such as Dictyostelium discoideum (a ~14-member expansion)
  and Acanthamoeba castellanii, and in ciliates, stramenopiles, and land plants,
  but is absent from choanoflagellates, kinetoplastids, Giardia, Apicomplexa, and
  (apart from a spurious hit) fungi; sparse bacterial members also exist. Family
  presence does not track phagotrophy, so the distribution reflects an ancient
  family with repeated lineage-specific losses rather than a diagnostic marker of
  ancestral phagocytic DNA digestion."*
- **Candidate references:** [PMID: 14644493](https://pubmed.ncbi.nlm.nih.gov/14644493/)
  (phagocytic exogenous-DNA role, review);
  [PMID: 19809494](https://pubmed.ncbi.nlm.nih.gov/19809494/) &
  [PMID: 26182365](https://pubmed.ncbi.nlm.nih.gov/26182365/) (engulfed/apoptotic
  DNA digestion, *C. elegans*);
  [PMID: 41805323](https://pubmed.ncbi.nlm.nih.gov/41805323/) (phagosomal DNA
  clearance, macrophages). Add as BP/MF support; keep evolutionary distribution as
  a computed note citing InterPro IPR004947 / PANTHER PTHR10858.
- **Candidate GO:** retain MF deoxyribonuclease II activity (GO:0004531), CC
  lysosome (GO:0005764), BP DNA catabolism in apoptotic/engulfment context; do
  **not** elevate the evolutionary narrative to a GO annotation.
- **Suggested question for curator:** Should the review assert a protist-conserved
  ancestral phagotrophic function, given that the distribution is patchy and the
  flagship choanoflagellate example is negative?

---

## Hypothesis Scorecard

| Component of seed hypothesis | Verdict | Basis |
|---|---|---|
| DNase II present in *Dictyostelium discoideum* | **Supported** | 14 genuine members ("Deoxyribonuclease II") |
| DNase II present in *Acanthamoeba* | **Supported** | 3 genuine members |
| DNase II present in choanoflagellates | **Refuted** | 0 members in well-covered Monosiga & Salpingoeca proteomes |
| Family is ancient / broadly eukaryotic | **Supported** | 5,031 euk. proteins across 1,423 proteomes |
| Distribution ⇒ ancestral phagocytic-DNA-digestion function | **Weakly supported / not demonstrated** | Phagotrophy does not predict presence; plants retain, several phagotrophs lack it |
| Should change a human DNASE2 GO annotation | **No** | Evolutionary context only; human annotations rest on direct evidence |

---

*Report generated from a 3-iteration autonomous investigation. Distribution counts
were obtained from the EBI InterPro and UniProt REST APIs for family IPR004947 /
PTHR10858 / PF03265 (UniProtKB 2026-10); all presence/absence calls for named
lineages were cross-checked at the protein-annotation level, and the
choanoflagellate absence was controlled against proteome coverage. Results are
reported conservatively: database signature counts are not a formal phylogeny, no
gene tree or ancestral-state reconstruction was run, and the phagotrophy-linkage
inference remains statistically untested. Provenance artifacts:
`/tmp/outputs/dnase2_taxonomic_distribution.csv`,
`/tmp/outputs/dnase2_distribution.png`.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)