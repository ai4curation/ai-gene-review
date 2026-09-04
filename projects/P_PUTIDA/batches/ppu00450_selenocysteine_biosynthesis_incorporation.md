---
title: "PSEPK ppu00450 selenocysteine biosynthesis and incorporation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00450: selenocysteine biosynthesis and incorporation

- Module seed: `selenocysteine_biosynthesis_incorporation`
- Candidate genes from membership table: 12
- Primary bucket genes: 9
- Existing review files: 8
- Curated review files: 8
- Selected module genes: 4
- Selected gene reviews curated: 4
- Selected OpenScientist reports: 1 of 4 complete

## Curated Boundary

- Required KT2440 machinery: `selD`, `serS`, `selA`, and `selB`.
- SelD supplies selenophosphate, SerS charges tRNA(Sec), SelA converts the
  charged tRNA to Sec-tRNA(Sec), and SelB delivers it during UGA recoding.
- The species-neutral module also records the distinct eukaryotic
  PSTK-SEPSECS and SECISBP2-EEFSEC implementation as one coupled alternative.
- A single taxonomic `EXACTLY_ONE` choice prevents invalid hybrid routes while
  leaving SelD/SEPHS2 and SerS/SARS shared before the branch.
- tRNA(Sec), the SECIS RNA element, and the in-frame UGA context are required
  non-protein substrates or conditions, not missing protein annotons.
- Selenium uptake and selenide production, tRNA transcription and maturation,
  ribosome biogenesis, free selenocysteine catabolism, and downstream
  selenoprotein functions are outside the boundary.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research for wave113.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2322](https://github.com/ai4curation/ai-gene-review/pull/2322).
- [x] Shepherd the earlier PR #2322 through merge.
- [ ] Open and shepherd the wave113 repair PR.

2026-07-26: OpenScientist timed out after 7200s for the module + pathway +
PSEPK report; no report file was produced.

2026-07-26: The gene-level `serS` run timed out after 7200s without producing
a report. The subsequent `selA` run persisted a complete report and artifacts
despite the wrapper returning a timeout status.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `selA` | PP_0493 | Q88QJ8 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | L-seryl-tRNA(Sec) selenium transferase (EC 2.9.1.1) (Selenocysteine synthase) (Sec synthase) (Selenocysteinyl-tRNA(Sec)  |
| [x] | `selB` | PP_0494 | Q88QJ7 | module:translation_rna_processing | PRESENT | CURATED | MISSING | Selenocysteyl-tRNA-specific translation elongation factor |
| [ ] | `metB` | PP_0659 | Q88Q39 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine gamma-synthase |
| [x] | `selD` | PP_0823 | P59392 | kegg:ppu00450 | PRESENT | CURATED | MISSING | Selenide, water dikinase (EC 2.7.9.3) (Selenium donor protein) (Selenophosphate synthase) |
| [ ] | `metG` | PP_1097 | Q88NV7 | kegg:ppu00450 | MISSING | MISSING | MISSING | Methionine--tRNA ligase (EC 6.1.1.10) (Methionyl-tRNA synthetase) (MetRS) |
| [ ] | `cysD` | PP_1303 | Q88NA9 | kegg:ppu00261 | MISSING | MISSING | MISSING | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) |
| [ ] | `cysNC` | PP_1304 | Q88NA8 | kegg:ppu00261 | MISSING | MISSING | MISSING | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) |
| [ ] | `mdeA` | PP_1308 | Q88NA4 | kegg:ppu00450 | MISSING | MISSING | MISSING | L-methionine gamma-lyase (EC 4.4.1.11) |
| [ ] | `metH` | PP_2375 | Q88KB5 | kegg:ppu04980 | PRESENT | CURATED | PRESENT | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) |
| [ ] | `metE` | PP_2698 | Q88JF1 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | 5-methyltetrahydropteroyltriglutamate-homocysteine methyltransferase |
| [x] | `serS` | PP_4000 | Q88FT2 | kegg:ppu00970 | PRESENT | CURATED | MISSING | Serine--tRNA ligase (Seryl-tRNA synthetase) |
| [ ] | `PP_4348` | PP_4348 | Q88EV4 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine beta-lyase |
| [ ] | `PP_4594` | PP_4594 | Q88E72 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine gamma-synthase |
| [ ] | `PP_4637` | PP_4637 | Q88E31 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | 5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase family protein |

## Notes

The checked rows are the four bacterial Sec-machinery proteins. Sulfur and
methionine metabolism entries remain visible only as excluded candidates from
the broad KEGG selenocompound map.

## 2026-09-01 Wave113 Repair

### Reusable structure and scope

The module retains `scope: CONCRETE`. In the module schema, CONCRETE covers a
specific, leaf-grounded biological process as well as a taxon-scoped instance;
it does not mean that the document must be restricted to one species. This
module has exact reaction leaves and concrete reviewed exemplars, so ABSTRACT
would incorrectly describe it as an intentionally ungrounded conformance motif.

The previous model had independent `EXACTLY_ONE` choices for Sec-tRNA synthesis
and insertion. Module-logic enumeration therefore permitted four combinations,
including bacterial SelA with eukaryotic SECISBP2/EEFSEC and eukaryotic
PSTK/SEPSECS with bacterial SelB. Wave113 replaces those independent choices
with one coupled taxonomic `EXACTLY_ONE` branch. Route enumeration now yields
exactly two routes:

1. shared SelD/SerS, then bacterial SelA and SelB;
2. shared SelD/SerS, then eukaryotic PSTK, SEPSECS, SECISBP2, and EEFSEC.

Archaeal PSTK/SEPSECS chemistry is acknowledged but archaeal recoding remains a
knowledge gap rather than an incomplete third branch.

### Family and evolutionary grounding

Exact PANTHER labels and membership were checked against
`interpro/panther/panther.obo` and `panther-members.tsv`. Reviewed E. coli
exemplars P16456 (SelD), P0A8L1 (SerS), P0A821 (SelA), and P14081 (SelB) add
cross-species bacterial grounding; the existing human exemplars ground the
eukaryotic and shared leaves. SelB remains grounded by
`InterPro:IPR004535`, whose exact label is "Translation elongation factor,
selenocysteine-specific", because the local PANTHER assignments do not place
PSEPK Q88QJ7 in the PAINT bacterial SelB node.

Only locally verified PAINT nodes with matching positive IBD rows were added:
PTN000029003 for selenide, water dikinase activity, PTN000207214 for bacterial
serine-tRNA ligase activity, PTN001284456 for bacterial SelA activity, and
PTN002665097 for SECIS binding by SECISBP2. Candidate nodes lacking exact
function or representative-seed support were omitted.

The completed [module/pathway/taxon OpenScientist report](../deep-research/PSEPK__selenocysteine_biosynthesis_incorporation__ppu00450-deep-research-openscientist.md)
finds the KT2440 bacterial route covered by `selD`, `serS`, `selA`, and `selB`
and confirms that the KEGG ppu00450 bucket is over-broad. Its suggestion to add
`selC` as a module gene is interpreted as an RNA-requirement observation:
tRNA(Sec) is essential but is not a protein annoton. Its `fdoG` selenoprotein
target is useful evidence that the route is biologically used, but downstream
selenoprotein function remains outside this machinery module.

### Independent annotation review

The required independent annotation-reviewer pass covered every annotation,
core function, supporting quotation, and local family claim for all four PSEPK
reviews.

| Gene | Wave113 disposition |
|---|---|
| `selD` | No change needed; all five annotations are coherent and the misleading SF0 display-name caveat is handled conservatively |
| `serS` | No change needed; all three MODIFY decisions are true descendant narrowings and both tRNA(Ser) and tRNA(Sec) roles are captured |
| `selA` | No change needed; GO:0001514 to GO:0001717 is a justified narrowing and the NEW PLP-binding proposal is supported |
| `selB` | No change needed; both MODIFY decisions and the cautious unreviewed-entry framing are supported |

The reviewer identified one module blocker: both SelB leaves used a paraphrased
InterPro label. They now carry the exact InterPro name. It also confirmed that
all module PANTHER labels and representative-member containments are exact and
that molecular functions occur only on leaf annotons.

### Wave113 research and validation

- The generic OpenScientist module run completed normally in 1,599 seconds
  with the full 7,200-second provider allowance; its report and HTML/PDF
  artifacts were refreshed.
- The PSEPK module/pathway/taxon run completed normally in 1,056 seconds with
  the same allowance and produced the previously missing report and artifacts.
- Both module validators pass. The semantic validator reports only advisory
  warnings for unavailable NCBITaxon label lookup and the unconfigured
  `InterPro` prefix; the exact InterPro label was independently verified.
- `just validate PSEPK <gene>` passes for `selD`, `serS`, `selA`, and `selB`.
- All 34 module-logic tests pass. Direct route enumeration asserts two routes
  and identifies only SelD and SerS as shared core atoms.
- The module, this batch page, and all four gene reviews render successfully.
- The branch was fetched and explicitly rebased onto the latest `origin/main`
  before the final validation pass. `git diff --check` passes, and generated GO
  cache plus unrelated PANTHER-member noise are excluded.
