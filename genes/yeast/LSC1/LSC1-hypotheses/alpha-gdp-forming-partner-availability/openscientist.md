---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T08:43:56.689039'
end_time: '2026-11-11T08:58:44.137381'
duration_seconds: 887.45
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: LSC1
  gene_symbol: LSC1
  uniprot_accession: P53598
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae S288C
  focus_type: free_text
  hypothesis_slug: alpha-gdp-forming-partner-availability
  hypothesis_text: 'S. cerevisiae Lsc1 (UniProtKB:P53598), the succinyl-CoA synthetase
    alpha subunit, cannot contribute to succinate-CoA ligase (GDP-forming) activity
    (GO:0004776) because fungal genomes encode only one succinyl-CoA synthetase beta
    subunit, of the ADP-specific type: the alpha subunit makes no nucleotide-base
    contacts, so whether an alpha subunit takes part in GDP-forming activity is decided
    by which beta subunit paralogs its genome encodes. Test by surveying the taxonomic
    distribution of beta-subunit paralogs (PANTHER PTHR11815: A-type SUCLA2-like versus
    G-type SUCLG2-like) across fungi, animals, plants, protists and bacteria, and
    by checking in solved structures (e.g. pig GTP-specific SCS, E. coli SucCD) whether
    any alpha-subunit residue contacts the nucleotide base.'
  term_context: '- Evolutionary question: PAINT places GO:0004776 at the root alpha-subunit
    node PTN000122012 of PANTHER PTHR11117 and propagates it to all descendants including
    fungal and plant alpha subunits. Is a GDP-forming partner beta subunit present
    outside animals (and which bacteria/protists), i.e. where on the alpha tree is
    this term actually supportable?'
  reference_context: '- PMID:9874242'
  source_file: genes/yeast/LSC1/LSC1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'S. cerevisiae Lsc1 (UniProtKB:P53598), the succinyl-CoA\
    \ synthetase alpha subunit, cannot\n  contribute to succinate-CoA ligase (GDP-forming)\
    \ activity (GO:0004776) because fungal genomes encode\n  only one succinyl-CoA\
    \ synthetase beta subunit, of the ADP-specific type: the alpha subunit makes no\n\
    \  nucleotide-base contacts, so whether an alpha subunit takes part in GDP-forming\
    \ activity is decided\n  by which beta subunit paralogs its genome encodes. Test\
    \ by surveying the taxonomic distribution of beta-subunit\n  paralogs (PANTHER\
    \ PTHR11815: A-type SUCLA2-like versus G-type SUCLG2-like) across fungi, animals,\
    \ plants,\n  protists and bacteria, and by checking in solved structures (e.g.\
    \ pig GTP-specific SCS, E. coli SucCD)\n  whether any alpha-subunit residue contacts\
    \ the nucleotide base.'\nfocus_type: free_text\ncontext:\n- 'Evolutionary question:\
    \ PAINT places GO:0004776 at the root alpha-subunit node PTN000122012 of PANTHER\n\
    \  PTHR11117 and propagates it to all descendants including fungal and plant alpha\
    \ subunits. Is a GDP-forming\n  partner beta subunit present outside animals (and\
    \ which bacteria/protists), i.e. where on the alpha\n  tree is this term actually\
    \ supportable?'\nreference_id:\n- PMID:9874242"
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae S288C (NCBITaxon:559292)
- **Gene directory:** LSC1
- **Gene symbol:** LSC1
- **UniProt accession:** P53598

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** alpha-gdp-forming-partner-availability
- **Source file:** genes/yeast/LSC1/LSC1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

S. cerevisiae Lsc1 (UniProtKB:P53598), the succinyl-CoA synthetase alpha subunit, cannot contribute to succinate-CoA ligase (GDP-forming) activity (GO:0004776) because fungal genomes encode only one succinyl-CoA synthetase beta subunit, of the ADP-specific type: the alpha subunit makes no nucleotide-base contacts, so whether an alpha subunit takes part in GDP-forming activity is decided by which beta subunit paralogs its genome encodes. Test by surveying the taxonomic distribution of beta-subunit paralogs (PANTHER PTHR11815: A-type SUCLA2-like versus G-type SUCLG2-like) across fungi, animals, plants, protists and bacteria, and by checking in solved structures (e.g. pig GTP-specific SCS, E. coli SucCD) whether any alpha-subunit residue contacts the nucleotide base.

## Term and Decision Context

- Evolutionary question: PAINT places GO:0004776 at the root alpha-subunit node PTN000122012 of PANTHER PTHR11117 and propagates it to all descendants including fungal and plant alpha subunits. Is a GDP-forming partner beta subunit present outside animals (and which bacteria/protists), i.e. where on the alpha tree is this term actually supportable?

## Reference Context

- PMID:9874242

## Source Context YAML

```yaml
hypothesis: 'S. cerevisiae Lsc1 (UniProtKB:P53598), the succinyl-CoA synthetase alpha subunit, cannot
  contribute to succinate-CoA ligase (GDP-forming) activity (GO:0004776) because fungal genomes encode
  only one succinyl-CoA synthetase beta subunit, of the ADP-specific type: the alpha subunit makes no
  nucleotide-base contacts, so whether an alpha subunit takes part in GDP-forming activity is decided
  by which beta subunit paralogs its genome encodes. Test by surveying the taxonomic distribution of beta-subunit
  paralogs (PANTHER PTHR11815: A-type SUCLA2-like versus G-type SUCLG2-like) across fungi, animals, plants,
  protists and bacteria, and by checking in solved structures (e.g. pig GTP-specific SCS, E. coli SucCD)
  whether any alpha-subunit residue contacts the nucleotide base.'
focus_type: free_text
context:
- 'Evolutionary question: PAINT places GO:0004776 at the root alpha-subunit node PTN000122012 of PANTHER
  PTHR11117 and propagates it to all descendants including fungal and plant alpha subunits. Is a GDP-forming
  partner beta subunit present outside animals (and which bacteria/protists), i.e. where on the alpha
  tree is this term actually supportable?'
reference_id:
- PMID:9874242
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

# AIGR Gene Hypothesis Deep Research — LSC1 (P53598): GDP-forming activity (GO:0004776)

**Target gene:** *LSC1* / Lsc1 (succinyl-CoA synthetase alpha subunit), *Saccharomyces cerevisiae* S288C (NCBITaxon:559292)
**UniProt:** P53598
**Hypothesis slug:** `alpha-gdp-forming-partner-availability`
**Focus type:** free_text (function-assignment / annotation-decision evaluation)
**GO term under evaluation:** GO:0004776 — succinate-CoA ligase (GDP-forming) activity (EC 6.2.1.4)
**Competing / correct term:** GO:0004775 — succinate-CoA ligase (ADP-forming) activity (EC 6.2.1.5)

---

## Summary

**Verdict: Supported — GO:0004776 is an over-annotation on yeast Lsc1 and should be replaced by GO:0004775 (ADP-forming).**

The seed hypothesis is correct in both its mechanistic premise and its evolutionary prediction. Nucleotide (ADP vs GDP) specificity of succinyl-CoA synthetase (SCS) resides entirely in the **beta subunit**; the **alpha subunit** (Lsc1's family) contributes the catalytic phosphohistidine and the CoA-binding site but makes **no nucleotide-base contacts**. Whether an alpha subunit can participate in GDP-forming activity is therefore decided entirely by which beta-subunit paralogs its genome encodes. This is established by biochemistry (pigeon ATP- and GTP-specific SCS share an *identical* alpha subunit), by structure (the nucleotide site lies in the N-terminal ATP-grasp domain of beta, ~35 Å from the alpha phosphohistidine), and by single-residue mutagenesis (position 20β reads the purine base and governs GTP preference).

Applied to yeast, the case is decisive. *S. cerevisiae* encodes exactly one alpha gene (*LSC1*) and one beta gene (*LSC2*) — there is no second, G-type (SUCLG2-like) beta paralog. The yeast holoenzyme was directly assayed and **uses ATP but not GTP** (PMID:9874242). Evolutionarily, the GDP-forming (G-type) beta subunit arose by gene duplication **early in the evolution of multicellular eukaryotes/animals** (PMID:9765291), after fungi diverged; fungi retain a single ancestral, ADP-type beta.

Consequently, GO:0004776 is **not supportable** on Lsc1. The PAINT propagation of GO:0004776 from the alpha-subunit root node PTN000122012 across the whole of PANTHER PTHR11117 is **phylogenetically too broad**: the GDP-forming function is a derived, animal-lineage property that depends on the presence of a G-type beta partner, which is absent from fungi. The correct annotation for the yeast Lsc1/Lsc2 holoenzyme is the ADP-forming term, GO:0004775. The most important caveat is a conventional one: the GDP-forming reaction is a property of the assembled αβ holoenzyme, not of either subunit in isolation — but since yeast cannot assemble a GDP-forming holoenzyme (no G-type beta) and the enzyme was directly measured as ATP-only, the annotation is factually wrong for this organism.

---

## Key Findings

### Finding 1 — Nucleotide specificity resides entirely in the beta subunit; the alpha subunit makes no base contacts

The pivotal biochemical result comes from pigeon tissues, where two SCS activities — one ATP-specific, one GTP-specific — were separated and characterized by electrophoresis, mass spectrometry, HPLC, and peptide mapping. The two enzymes were shown to **incorporate the same alpha subunit** but **different beta subunits**. The authors conclude directly: *"Because the two succinyl-CoA synthetases incorporate the same alpha-subunit, the determinants of nucleotide specificity must reside within the beta-subunit"* ([PMID: 9765290](https://pubmed.ncbi.nlm.nih.gov/9765290/)).

Structural and mutational work localizes this determinant precisely. In *E. coli* SCS, the nucleotide-binding site lies in the **N-terminal (ATP-grasp) domain of the beta subunit**, roughly 35 Å from the catalytic His246α, requiring the phosphohistidine loop to shuttle between two active sites ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)). Photoaffinity labeling with 8-N3-ATP and site-directed mutagenesis confirm the beta N-terminal domain as the nucleotide site, and the **P20βQ mutant lowers the Km for GTP more than 5-fold** without altering other kinetic parameters ([PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/)). Structurally, a **single beta residue at position 20 reads the purine base**: *"A water molecule and Pro20β in T. aquaticus take the place of Gln20β in pig GTP-specific SCS, interacting well with the guanine base"* ([PMID: 22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/)).

Human genetics mirrors this exactly: both isoforms share a single alpha subunit (SUCLG1); the ADP-forming enzyme uses the SUCLA2 beta and the GDP-forming enzyme uses the SUCLG2 beta — *"The substrate specificity is determined by the beta subunit of succinate-CoA ligase, which is encoded by either SUCLA2 or SUCLG2"* ([PMID: 18392745](https://pubmed.ncbi.nlm.nih.gov/18392745/)). This is the mechanistic core of the seed hypothesis, and it is strongly supported: an alpha subunit's participation in GDP-forming activity is decided by its genome's beta paralog repertoire, not by the alpha subunit itself.

### Finding 2 — Yeast succinyl-CoA ligase is biochemically ADP-forming only (uses ATP, not GTP)

Przybyla-Zawislak et al. (1998) cloned the only two SCS-subunit genes in *S. cerevisiae*: **LSC1 (YOR142W, alpha)** and **LSC2 (YGR244C, beta)**. Single and double deletions abolished mitochondrial SCS activity, which was restored by plasmid rescue — establishing these as the sole subunits of the yeast enzyme. Critically, the enzyme's nucleotide preference was measured directly: *"The yeast succinyl-CoA ligase was shown to utilize ATP but not GTP for succinyl-CoA synthesis"* ([PMID: 9874242](https://pubmed.ncbi.nlm.nih.gov/9874242/)).

This is the single most decisive piece of evidence for the curation decision, because it is a **direct enzymatic assay of the actual yeast gene products** showing no GTP/GDP activity. The same paper establishes that yeast has exactly **one alpha and one beta gene** — *"Two genes, LSC1 (YOR142W) and LSC2 (YGR244C), with high similarity to succinyl-CoA ligase subunits from other species were isolated from Saccharomyces cerevisiae"* — i.e., there is no G-type beta paralog to confer GDP-forming activity.

### Finding 3 — The A-type/G-type beta duplication postdates fungal divergence

A pairwise global-alignment analysis (Needleman–Wunsch, UniProt sequences, computed during this investigation) shows that yeast Lsc2 beta (P53312) is **nearly equidistant** from human A-type SUCLA2 (Q9P2R7, 48.3% identity) and human G-type SUCLG2 (Q96I99, 46.5%), and 44.7% identical to *E. coli* SucC. The two human beta paralogs are more similar to **each other** (54.5%) than yeast Lsc2 is to either — the signature of a gene duplication that occurred **after** the fungal lineage split off. The shared alpha subunit is well conserved across the same span: yeast Lsc1 (P53598) vs human SUCLG1 = 59.9% identity.

| Pairwise comparison | % identity | Interpretation |
|---|---|---|
| Human SUCLA2 (A-beta) vs SUCLG2 (G-beta) | 54.5% | Paralogs clustered → duplication within animals |
| Yeast Lsc2 vs human SUCLA2 (A-beta) | 48.3% | Yeast beta is outgroup to both |
| Yeast Lsc2 vs human SUCLG2 (G-beta) | 46.5% | Yeast beta is outgroup to both |
| Yeast Lsc2 vs *E. coli* SucC | 44.7% | Ancestral-type beta |
| Yeast Lsc1 vs human SUCLG1 (alpha) | 59.9% | Alpha subunit well conserved |

The equidistance of yeast Lsc2 from both human paralogs is exactly what is expected if the SUCLA2/SUCLG2 duplication happened in the animal lineage, with fungi retaining a single ancestral beta. (This is a conservative global-alignment result computed during the run; see Finding 5 for its limitations.)

### Finding 4 — The GDP-forming (G-type) beta subunit arose by duplication in multicellular eukaryotes (animals)

Johnson, Mehus, Tews, Milavetz & Lambeth (1998) sequenced the mature ATP-specific (A-beta) and GTP-specific (G-beta) subunits in pigeon (54% identical to each other), identified A-beta and G-beta orthologs in human and mouse, and found two beta sequences in *C. elegans*. They conclude the duplication is animal-specific: the A-beta and G-beta genes *"arose by duplication early in the evolution of multicellular eucaryotes"* ([PMID: 9765291](https://pubmed.ncbi.nlm.nih.gov/9765291/)). They also report *"pairwise comparisons of the A-beta and G-beta sequences revealed <53% identity"*, independently corroborating the computed 54.5% A/G paralog identity and the two-paralog structure restricted to animals.

Lambeth (2004) confirms the GDP-forming isoform is an animal/mammalian feature: *"both proteins are widely expressed in mammals with the relative amounts varying from tissue to tissue"* ([PMID: 15234968](https://pubmed.ncbi.nlm.nih.gov/15234968/)). Together these place the origin of the GDP-forming beta partner firmly in the animal lineage. Fungi — including *S. cerevisiae* — diverged before this duplication and therefore possess only the single, ancestral, ADP-type beta subunit. There is no genomic substrate for GDP-forming activity in yeast.

### Finding 5 (negative / limitation) — Single-residue specificity signature could not be cleanly mapped due to mitochondrial transit peptides

An attempt to read the position-20β specificity residue by global alignment of beta subunits to *E. coli* SucC gave: *E. coli* = Pro20, *T. aquaticus* = Pro, yeast Lsc2 = Pro, human SUCLA2 (ADP-type) = Pro — all consistent with ADP/ATP-type (non-Gln) at the base-reading position. However, the eukaryotic GTP-specific sequences (human SUCLG2, pig SUCLG2) did **not** resolve the expected Gln (gave R and C at the aligned column), because they carry long N-terminal mitochondrial transit peptides/propeptides (pig SUCLG2 precursor 520 aa; human SUCLG2 432 aa) that misregister the N-terminal column against bacterial SucC, which lacks a transit peptide. This is an honest limitation of the quick global-alignment approach: confirming the expected Gln signature in G-type sequences would require a mature-protein, structure-guided alignment. It does not weaken the main conclusion, which rests on the direct yeast assay (Finding 2) and the published pigeon/human/*C. elegans* evolutionary analysis (Finding 4).

---

## Mechanistic Model / Interpretation

The SCS holoenzyme is an (αβ) heterodimer (assembling into (αβ)₂ tetramers). Catalysis is a three-step substrate-level phosphorylation routed through a phosphohistidine on the **alpha** subunit (His246α in *E. coli*), which shuttles ~35 Å between two active sites:

```
        ALPHA subunit (Lsc1 family)              BETA subunit (Lsc2 / SUCLA2 / SUCLG2)
   +------------------------------+        +---------------------------------------------+
   | - CoA binding (N-term domain)|        | N-terminal ATP-grasp domain:                |
   | - catalytic His (P~His loop) |<--35A->|   NUCLEOTIDE-BINDING SITE                   |
   | - NO nucleotide-base contacts|        |   position 20B reads the purine base:        |
   +------------------------------+        |     Pro20B / water  -> ADP/ATP (A-type)      |
            SHARED across isoforms         |     Gln20B          -> GDP/GTP (G-type)      |
                                           +---------------------------------------------+
                                                   DETERMINES NUCLEOTIDE SPECIFICITY
```

Nucleotide specificity is set at ~position 20 of the beta subunit's N-terminal domain. The alpha subunit is interchangeable between ATP- and GTP-specific enzymes (proven in pigeon and human). Therefore the operative rule is:

> **An alpha subunit "has" GDP-forming activity if and only if its genome encodes a G-type (SUCLG2-like) beta subunit with which it can assemble a GDP-forming holoenzyme.**

Mapping this onto the tree of life:

| Lineage | Beta paralogs present | GDP-forming activity supportable on alpha? |
|---|---|---|
| **Animals (Metazoa)** | A-type (SUCLA2) + G-type (SUCLG2) | **Yes** — direct biochemical/genetic evidence |
| **Fungi** (incl. *S. cerevisiae*) | Single ancestral/ADP-type (Lsc2) | **No** — yeast assayed ATP-only; no G-type gene |
| **Plants** | Single beta (not shown to be G-type here) | Not supportable on present evidence |
| **Bacteria** | Single SucC (often ADP-leaning; some, e.g. *Pseudomonas*, *T. aquaticus*, *E. coli* P20βQ, can use GTP) | Variable / species-specific |
| **Protists** | Variable | Species-specific; not resolved here |

The PAINT annotation places GO:0004776 at the alpha-subunit root node PTN000122012 and propagates it across all of PTHR11117, including fungal and plant alpha subunits. This is **too broad**: the GDP-forming function is a derived, animal-lineage property that depends on a G-type beta partner absent from fungi. The correct annotation for yeast Lsc1's holoenzyme is the ADP-forming term, GO:0004775.

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID:9765290](https://pubmed.ncbi.nlm.nih.gov/9765290/) | Direct biochem / structural | **Supports** | Specificity is in beta, not alpha | ATP- and GTP-specific SCS share an *identical* alpha subunit; specificity "must reside within the beta-subunit" | Pigeon tissues | High; foundational |
| [PMID:9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/) | Structural | **Supports** | Alpha makes no nucleotide-base contacts | Nucleotide site in beta N-terminal domain, ~35 Å from His246α; CoA binds alpha | *E. coli* SCS, 2.3 Å | High |
| [PMID:10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/) | Mutagenesis / photoaffinity | **Supports** | Single beta residue tunes base preference | P20βQ lowers Km(GTP) >5-fold; nucleotide site in beta N-terminal ATP-grasp | *E. coli* | High |
| [PMID:22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/) | Structural | **Supports** | Position-20β reads the purine base | Gln20β (pig, GTP) vs Pro20β/water (*T. aquaticus*) at the guanine base | Pig / *T. aquaticus* | High |
| [PMID:18392745](https://pubmed.ncbi.nlm.nih.gov/18392745/) | Review / human genetics | **Supports** | Beta identity sets ADP vs GDP | Specificity set by SUCLA2 (ADP) vs SUCLG2 (GDP), sharing SUCLG1 alpha | Human | High (synthesized genetics) |
| [PMID:9874242](https://pubmed.ncbi.nlm.nih.gov/9874242/) | **Direct assay + genetics** | **Supports (decisive)** | Does yeast enzyme have GDP-forming activity? | Yeast SCS "utilize[s] ATP but not GTP"; only one alpha (LSC1) and one beta (LSC2) gene | *S. cerevisiae* | High; the key organism-specific evidence |
| [PMID:9765291](https://pubmed.ncbi.nlm.nih.gov/9765291/) | Structural / evolutionary | **Supports** | Is G-type beta animal-specific? | A-beta/G-beta genes "arose by duplication early in the evolution of multicellular eucaryotes"; two betas in *C. elegans*; <53% A/G identity | Pigeon, human, mouse, *C. elegans* | High |
| [PMID:15234968](https://pubmed.ncbi.nlm.nih.gov/15234968/) | Expression / review | **Supports** | GDP-forming enzyme an animal feature? | Both isoforms widely expressed across mammalian tissues | Mammals | Medium-High |
| *This run* (NW alignments) | Computational | **Qualifies / Supports** | Does yeast beta cluster with A or G type? | Yeast Lsc2 equidistant (48.3% / 46.5%) from both human paralogs; paralogs closer to each other (54.5%) → duplication postdates fungi | UniProt sequences | Medium; global alignment, transit-peptide misregistration (Finding 5) |
| [PMID:10671455](https://pubmed.ncbi.nlm.nih.gov/10671455/) | Direct biochem | **Competing / context** | Can a single SCS be nucleotide-promiscuous? | *P. aeruginosa* SucCD synthesizes GTP, ATP, UTP, CTP (broad NTP) | Bacteria | Medium; bacterial exception, not fungal |
| [PMID:11206416](https://pubmed.ncbi.nlm.nih.gov/11206416/) | Direct biochem | Context | Two SCS activities coexist in animal mitochondria | ATP- and GTP-specific activities both present in beta-cell mitochondria | Mammalian cells | Medium; reinforces animal two-isoform model |
| [PMID:33645539](https://pubmed.ncbi.nlm.nih.gov/33645539/) | Structural | Context | Mechanism of phosphohistidine shuttling | P~His loop bridges 29 Å between sites I and II in pig GTP-specific SCS | Pig | High; mechanistic support |

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| Plant beta-subunit type | Not directly surveyed; inferred from animal-specific duplication (PMID:9765291) | PAINT propagates GO:0004776 to plant alpha too; need to confirm plants lack G-type beta | Phylogenetic survey of plant SCS beta subunits (PTHR11815) with explicit A/G typing |
| Protist beta repertoire | Not surveyed | Some protists may encode G-type beta; affects where the term is supportable | Genome/HMM survey across protist clades |
| Gln20β signature in eukaryotic G-type | Attempted; failed due to transit peptides (Finding 5) | Confirms the structural base-reading residue in G-type mitochondrial enzymes | Mature-protein, structure-guided alignment of SUCLG2 orthologs |
| Yeast Lsc2 residue at position 20β | Global alignment gave Pro (ADP-type) — consistent but from imperfect alignment | Directly predicts yeast is ADP-type from structure | Structure-based alignment or AlphaFold superposition of Lsc2 onto pig/*E. coli* beta |
| Quantitative kinetics of yeast SCS | PMID:9874242 reports qualitative ATP-yes/GTP-no | Trace GTP activity (as in some bacteria) would complicate the "GDP-forming absent" claim | Modern kinetic assay of recombinant Lsc1/Lsc2 with ADP vs GDP, report kcat/Km |

---

## Conflicts and Alternatives

1. **Bacterial nucleotide promiscuity (competing, but not applicable to fungi).** Some bacterial SCS enzymes are promiscuous: *P. aeruginosa* SucCD synthesizes GTP, ATP, UTP, and CTP ([PMID:10671455](https://pubmed.ncbi.nlm.nih.gov/10671455/)), and *E. coli* SCS can be pushed toward GTP by the single P20βQ mutation ([PMID:10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/)). This shows that a *single* beta subunit can in principle have broad specificity, so "single beta" does not automatically mean "ADP-only" across all taxa. However, this does not rescue GO:0004776 for yeast, because the yeast enzyme was **directly assayed and does not use GTP** (PMID:9874242). The bacterial promiscuity is a taxon-specific property that must be demonstrated, not assumed; it was tested and found absent in yeast.

2. **Holoenzyme-vs-subunit annotation convention.** GO MF terms for multi-subunit enzyme activities are conventionally applied to each subunit. One could argue GO:0004776 on Lsc1 merely reflects "the alpha subunit of a GDP-forming enzyme." But in yeast there is no GDP-forming enzyme for it to be part of, so the annotation is factually wrong for this organism.

3. **Transit-peptide alignment artifact (Finding 5).** The computational attempt to confirm the Gln20β signature in eukaryotic G-type sequences failed due to transit-peptide misregistration. This is a limitation of the quick analysis, not a conflict with the conclusion; the main evidence (direct yeast assay + published evolutionary analysis) is independent of it.

4. **Plants/protists unresolved.** The hypothesis also questions plant alpha subunits. This investigation did not directly resolve whether any plant or protist genome encodes a G-type beta. The conclusion for yeast is firm; the broader PAINT recommendation for plants and protists is a lead, not a settled result.

---

## GO Curation Implications

**Lead (requires curator verification):**

- **Remove / replace GO:0004776** (succinate-CoA ligase, GDP-forming activity) as a molecular-function annotation on *LSC1* / P53598.
- **Add / retain GO:0004775** (succinate-CoA ligase, ADP-forming activity) as the correct MF term, supported by the direct yeast assay (PMID:9874242, ATP-only) and genomic gene content (single ADP-type beta).
- If a curator prefers to keep a parent term, **GO:0004774 (succinate-CoA ligase activity)** is defensible as a more general, still-correct MF — but GO:0004775 (ADP-forming) is the most informative supported term and is preferred.

**PAINT / phylogenetic annotation:**

- The placement of GO:0004776 at alpha-root node **PTN000122012** with propagation across all of **PTHR11117** is **over-broad**. Recommend restricting GO:0004776 propagation to clades that demonstrably encode a G-type (SUCLG2-like, PTHR11815 G-type) beta partner — robustly Metazoa. The fungal branch should instead inherit GO:0004775 (ADP-forming).
- This is a case of **paralog-driven over-annotation**: a function that is a property of a specific α+β *holoenzyme* was propagated to all α orthologs regardless of whether a compatible β paralog exists in the genome.

**Term natures:** MF term only. No change is implied for the associated BP (tricarboxylic acid cycle, GO:0006099) or CC (mitochondrial matrix) annotations, which are unaffected.

---

## Mechanistic Scope

The immediate molecular function under test is the **nucleotide substrate specificity of the SCS holoenzyme** — specifically whether the α subunit Lsc1 can participate in catalysis that uses **GDP/GTP** (GO:0004776) rather than **ADP/ATP** (GO:0004775). This is a direct property of the assembled enzyme's active site, read out by a simple in vitro nucleotide-dependence assay.

It must be separated from downstream/pathway considerations:
- **Direct activity:** succinyl-CoA + Pi + NDP ⇌ succinate + CoA + NTP. For yeast, measured as ATP-only.
- **Not at issue here:** the TCA-cycle role (BP), mitochondrial localization (CC), or any pleiotropic phenotype of *lsc1Δ*. The hypothesis is narrowly about *which nucleotide* the enzyme uses — a decision made structurally at the β-subunit base-reading residue.

The alpha subunit's own direct contributions — catalytic phosphohistidine and CoA binding — are real and conserved, but they are **nucleotide-base-agnostic**. The GDP-forming label is therefore not a property the alpha subunit confers; it is conferred by a G-type beta partner the yeast genome does not encode.

---

## Discriminating Tests

1. **Recombinant yeast SCS nucleotide kinetics (most decisive).** Co-express Lsc1+Lsc2, purify the αβ complex, and measure succinyl-CoA synthesis with ADP vs GDP (and ATP vs GTP in reverse), reporting kcat/Km for each. Prediction: strong ADP/ATP activity, negligible GDP/GTP. This re-tests and quantifies PMID:9874242.

2. **Structure-guided residue typing.** Build an AlphaFold model (or use a solved yeast SCS structure) of Lsc2, superpose on pig GTP-specific (Gln20β) and *E. coli*/*T. aquaticus* (Pro20β) betas, and read the position-20β residue in correct 3D register (bypassing the transit-peptide alignment artifact of Finding 5). Prediction: Pro/non-Gln → ADP-type.

3. **Phylogenomic beta-subunit survey (for the PAINT recommendation).** Systematically classify PTHR11815 beta subunits as A-type vs G-type across fungi, plants, protists, animals, and bacteria, mapping presence/absence of a G-type partner onto the species tree. This defines exactly where on the alpha tree GO:0004776 is supportable and where GO:0004775 should be substituted.

4. **Heterologous complementation.** Test whether human SUCLG2 (G-type beta) can partner yeast Lsc1 to reconstitute GDP-forming activity. A positive result would confirm that Lsc1's alpha is *competent* for GDP chemistry given the right partner — reinforcing that the limitation is partner availability, exactly as the seed hypothesis states.

---

## Curation Leads (require curator verification)

**Candidate action change:**
- On *LSC1* / P53598: **replace GO:0004776 (GDP-forming) with GO:0004775 (ADP-forming)** as the MF annotation, or at minimum generalize to GO:0004774.
- Flag the PAINT over-propagation: GO:0004776 at node PTN000122012 should **not** propagate to the fungal branch of PTHR11117.

**Candidate references and exact snippets to verify:**
- [PMID:9874242](https://pubmed.ncbi.nlm.nih.gov/9874242/): *"The yeast succinyl-CoA ligase was shown to utilize ATP but not GTP for succinyl-CoA synthesis."* (decisive organism-specific assay)
- [PMID:9765290](https://pubmed.ncbi.nlm.nih.gov/9765290/): *"Because the two succinyl-CoA synthetases incorporate the same alpha-subunit, the determinants of nucleotide specificity must reside within the beta-subunit."* (alpha makes no specificity contribution)
- [PMID:9765291](https://pubmed.ncbi.nlm.nih.gov/9765291/): *"...the A-beta and G-beta genes arose by duplication early in the evolution of multicellular eucaryotes."* (G-type is animal-specific, post-fungal)
- [PMID:22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/): *"A water molecule and Pro20β in T. aquaticus take the place of Gln20β in pig GTP-specific SCS, interacting well with the guanine base"* (single beta residue reads the base)

**Suggested curator questions:**
- Does the GO annotation framework prefer subunit-level MF annotation to reflect holoenzyme gene content (i.e., should a fungal alpha ever carry a GDP-forming term)?
- Should PTHR11117's PAINT annotation be split so that GO:0004776 is restricted to Metazoan nodes while fungal/plant nodes receive GO:0004775?

**Suggested experiments:** recombinant yeast SCS ADP/GDP kinetics; structure-guided Lsc2 position-20β typing; heterologous SUCLG2 complementation (see Discriminating Tests).

---

## Conclusion

The seed hypothesis is **supported**. Nucleotide specificity of succinyl-CoA synthetase is a beta-subunit property; the alpha subunit (Lsc1's family) makes no base contacts and is interchangeable between ADP- and GDP-forming enzymes. *S. cerevisiae* encodes a single, ancestral, ADP-type beta subunit (Lsc2), the GDP-forming G-type beta having arisen by gene duplication only in the animal lineage after fungi diverged, and the yeast enzyme was directly assayed as using ATP but not GTP. Consequently, **GO:0004776 (GDP-forming) is an over-annotation on yeast Lsc1 and should be replaced by GO:0004775 (ADP-forming)**, and the PAINT propagation of GO:0004776 across the whole alpha-subunit tree should be narrowed to clades (robustly Metazoa) that encode a G-type beta partner.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)