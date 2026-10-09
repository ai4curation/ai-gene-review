---
title: "Non-Physiological Reactions in EC, Rhea and GO"
maturity: SCOPING
tags: [PIPELINE, OBSOLETION]
genes: [IRC24, NRE1, yueD, atzA, tfdA, pcpB, linA, opd, dhlA]
species: [yeast, BACCE, BACSU, PSESD, CUPPJ, SPHCR, SPHIU, BREDI, XANAU]
---

# Non-Physiological Reactions in EC, Rhea and GO

**Bottom line:** EC and Rhea record reactions that have been demonstrated;
they do not judge whether a substrate matters biologically. GO does make that
judgment, one issue at a time, and has obsoleted roughly fifteen molecular
function terms for non-physiological substrates with no systematic criteria.
A substrate being synthetic is not the test: `atzA`, `tfdA`, `pcpB`, `linA`,
`opd` and `dhlA` all act on man-made chemicals and all carry real, selected,
pathway-committed functions, whereas benzil reductase activity was a
chromogenic assay readout that EC turned into a reaction and GO turned into a
term. This project aims to separate the two classes systematically, and to
clean up what previous obsoletions left behind.

## Motivation: the chain from assay to annotation

The failure mode is a pipeline, and every step is individually defensible:

> a test-tube activity → an EC number → a Rhea reaction → a GO term →
> IEA annotations that read as the gene's function

The entry point is the choice of assay substrate. Chromogenic and fluorogenic
compounds exist because they make a reaction measurable, not because cells
encounter them. Once such a substrate produces a publishable activity, the
rest follows mechanically.

GO's obsoletion of `GO:0102306 benzil reductase [(S)-benzoin-forming]
activity` (go-ontology#30498, "not a physiologically relevant substrate") shows
both that GO recognizes the problem and that the remedy is incomplete: the
obsoletion request asked for the Rhea xref to be moved to the parent, so
`RHEA:25968` became a `skos:narrowMatch` of the EC 1.1.1.- grouping class
`GO:0016616`, which now generates uninformative IEA annotations on five UniProt
entries. See [the benzil reductase worked example](#worked-example-benzil-reductase).

## Taxonomy

Five categories, which a naive "is the substrate synthetic?" filter would
conflate:

| # | Category | Test | Action |
|---|---|---|---|
| 1 | **Assay substitute** | Compound exists to make a reaction measurable (chromogenic, fluorogenic, surrogate) | Obsoletion candidate |
| 2 | **Side activity on a real metabolite** | Weak activity on a second natural compound; the "underground metabolism" question | Kinetics decide |
| 3 | **Generalist named after one test substrate** | Detox enzymes (carbonyl reductases, P450s, transferases) whose real role spans many compounds | Map to the broad term |
| 4 | **Evolved xenobiotic degradation** | Substrate is man-made, but the enzyme is selected, pathway-committed and often kinetically optimized | Keep; these are real functions |
| 5 | **Biocatalysis adoption** | EC entry created from a screening or protein-engineering paper | Depends on whether 1 or 4 applies |

Benzil reductase straddles 1 and 5. The six degradation enzymes reviewed below
are category 4, and establish that the category is real and populated.

## Candidate detection signals

Computable per Rhea-mapped GO term, before any manual curation:

- **Pathway membership** — is the reaction in MetaCyc, KEGG or Reactome, or is
  it an orphan? (Category 4 enzymes sit in UniPathway/MetaCyc pathways;
  benzil reduction does not.)
- **Substrate origin** — is the compound in a metabolome database (HMDB, YMDB,
  ECMDB), or flagged in ChEBI as a xenobiotic or assay reagent?
- **Kinetics** — BRENDA/SABIO-RK catalytic efficiency against the typical value
  for the EC class. Benzil turnover is ~9–64 min⁻¹, roughly three orders of
  magnitude below a well-matched enzyme. But note that **low kcat does not by
  itself indicate category 1**: `pcpB` has kcat 0.024 s⁻¹ on its genuine
  physiological substrate, and that slowness appears to be *selected* rather
  than unoptimized (see below). Kinetics is the weakest of these signals and
  should never be used alone.
- **Evidence provenance** — a single founding paper in a biocatalysis or
  applied-microbiology journal, versus genetics in a host organism.
- **GO footprint** — annotated only via Rhea/EC-derived IEAs, with no
  experimental annotation anywhere.

No single signal is decisive. Pathway membership plus host genetics is the
strongest discriminator between categories 1 and 4; kinetics alone is the
weakest.

## Existing GO decisions (the labelled set)

Obsolete MF terms whose obsoletion comment cites a non-physiological reaction
or substrate — 15 in the current `go-edit.obo`:

| Term | Reason | Issue |
|---|---|---|
| `GO:0102306` benzil reductase | substrate not physiological | #30498 |
| `GO:0018543` 4-amino-2-nitroso-6-nitrotoluene reductase | "no known physiological substrate" (TNT breakdown product) | #23357 |
| `GO:0102480` 5-fluorocytosine deaminase | prodrug | #28070 |
| `GO:0103030` ethylglyoxal reductase | "not known to be physiological significant" | #25302 |
| `GO:0047949` glutarate-semialdehyde dehydrogenase (NAD+) | no evidence reaction is physiological | #25447 |
| `GO:0052812` PI(3,4)P2 5-kinase | not believed physiologically relevant | #25355 |
| `GO:0003840` gamma-glutamyltransferase | does not correspond to a physiological reaction | #13571 |
| `GO:0061746` ssDNA-dependent GTPase | no evidence under physiological conditions | #19078 |
| `GO:0140868` 4,4'-diapophytoene desaturase | may not be physiologically relevant | #23557 |
| `GO:0035827` rubidium ion transmembrane transporter | "represents an assay" | — |
| `GO:1904012` platinum binding / `GO:1904013` xenon atom binding | no physiological relevance | — |

Plus two substrate-specific-transporter obsoletions (`GO:0043216`,
`GO:0103113`) which are a granularity rather than a physiology decision.

This set is small enough to serve as a hand-labelled reference for calibrating
the signals above, and heterogeneous enough to show that no single criterion
was in use.

## Damage left behind by previous obsoletions

Two distinct residues, both found while reviewing this gene set:

**1. Rhea xrefs pushed onto EC-level grouping classes.** Only three live GO
terms carry a `skos:narrowMatch` Rhea xref alongside an EC `x.x.x.-` xref, for
nine reactions in total:

| Term | Reactions |
|---|---|
| `GO:0016616` oxidoreductase, CH-OH donor, NAD(P) acceptor | RHEA:25968 |
| `GO:0008241` peptidyl-dipeptidase | RHEA:12845, RHEA:63560 |
| `GO:0016712` oxidoreductase, paired donors, reduced flavin | RHEA:17149, RHEA:51984, RHEA:68160, RHEA:75847, RHEA:75863, RHEA:76419 |

Small enough to inspect by hand, and cheap to guard with a QC check. The other
eight have not yet been assessed, and some may genuinely need new specific
terms rather than re-pointing. Contrast `GO:0018786 haloalkane dehalogenase
activity` (annotated on `dhlA`), which holds `RHEA:19081` as an exactMatch and
the specific `RHEA:25185` (1,2-dichloroethane) as a narrowMatch — the correct
arrangement, and the template for fixing `RHEA:25968`.

**2. Bulk obsoletion that caught a real enzyme.** go-ontology#28108 obsoleted
160 leaf catalytic terms selected for having a partial EC xref, zero
annotations, no Rhea xref and no MetaCyc/KEGG xref, with the comment "there is
no evidence that this specific activity exists". For `GO:0018830
gamma-hexachlorocyclohexane dehydrochlorinase activity` that comment is
incorrect: LinA has Tn5-mutant genetics, in vitro complementation, and GC-MS /
NMR / CD mechanistic characterization, and UniProt now maps its reaction to
`RHEA:45480`. **The criteria selected for curation coverage, not for
evidence**, and LinA consequently has no molecular function annotation at all
in GOA today. The surviving sibling `GO:0018833 DDT-dehydrochlorinase activity`
escaped only because it had an EC number and a Rhea mapping. An audit of the
other 159 terms against current UniProt catalytic activity records is a
concrete next step.

## Reviewed genes

### Worked example: benzil reductase

Four reviews, covering every UniProt entry carrying `RHEA:25968` except gerbil
SPR (a sepiapterin reductase incidentally tested on benzil):

| Gene | Evidence | Key calls |
|---|---|---|
| yeast/IRC24 | benzil reduction in vitro, NADPH-preferring; DNA-damage induced; increased Rad52 foci on deletion | `GO:0016616` → `GO:0004090`; `GO:0050664` (O₂ acceptor) IDA + its IBA → `GO:0004090` |
| yeast/NRE1 | tandem paralog, 52% identical, same activity; crystal structures 3KZV/6UHX | same |
| BACCE/yueD | found by expression screen; broad aromatic carbonyl range; cytoplasmic by GFP | `GO:0016616` → `GO:0004090`; BH4 biosynthesis REMOVE; SPR activity over-annotated |
| BACSU/yueD | never assayed; 41% identical to the B. cereus enzyme | `GO:0016616` → `GO:0004090`; BH4 IBA REMOVE; SPR IBA UNDECIDED |

`GO:0004090 carbonyl reductase (NADPH) activity` (EC 1.1.1.184, whose synonyms
include "xenobiotic ketone reductase") is the right target: (S)-benzoin is a
secondary alcohol, and the sister EC 1.1.1.320 reaction `RHEA:31891` is already
mapped there. No new benzil-specific term is warranted — that would reverse
#30498.

Supporting observations for category 1: turnover is 9–64 min⁻¹; all five papers
indexed under "benzil reductase" in PubMed come from biotechnology groups; the
founding paper closes by noting the enzymes "will be utilized to produce
important chiral compounds"; and B. cereus YueD's tightest-binding substrate is
not benzil (Km 768 µM) but 1,4-naphthoquinone (27.6 µM), which hints at quinone
or reactive-carbonyl detoxification as the real role.

### Counter-example set: evolved xenobiotic degradation

Six classic degradation enzymes, chosen to test whether "synthetic substrate"
tracks "not a real function". It does not.

| Gene | Substrate (introduced) | Status in host | Notable annotation finding |
|---|---|---|---|
| `atzA` (Pseudomonas sp. ADP) | atrazine (1950s) | grows on it as N source; step 1/3 | `GO:0016810` C-N hydrolase REMOVE — fold-level InterPro transfer; AtzA cleaves C-halide. The 98%-identical paralog TriA *does* belong in `GO:0016810` |
| `tfdA` (C. pinatubonensis JMP134) | 2,4-D (1940s) | pJP4-encoded pathway; Tn5 mutants complemented | only MF annotation is a Rhea IEA, despite 1987 genetics |
| `pcpB` (S. chlorophenolicum) | pentachlorophenol (1930s) | rate-limiting step of a patchwork pathway | kcat 0.024 s⁻¹ with heavy uncoupling to H₂O₂ — yet the slowness may be a *selected* optimum, not a defect |
| `linA` (S. indicum UT26) | lindane (1940s) | grows on it as sole C source | **no MF annotation exists**; specific term bulk-obsoleted in error (see above) |
| `opd` (B. diminuta) | paraoxon and nerve agents (20th c.) | — | paraoxon turnover near the **diffusion limit**; progenitor identified as a quorum-sensing lactonase (PLL family) |
| `dhlA` (X. autotrophicus GJ10) | 1,2-dichloroethane (commodity) | grows on it as sole C source; step 1/4 | `GO:0004301` epoxide hydrolase REMOVE — α/β-hydrolase fold shared with epoxide hydrolases |

Three patterns worth extracting:

1. **The decisive signal is host genetics plus pathway membership**, not the
   substrate's provenance. Five of the six support growth of their host on the
   compound.
2. **Catalytic efficiency spans four orders of magnitude within category 4**
   (`opd` near-diffusion-limited, `pcpB` at 0.024 s⁻¹), so kinetics cannot
   separate categories 1 and 4 on its own. `pcpB` is the clearest refutation
   of a kcat threshold, and an OpenScientist run strengthened it: the slow
   turnover is plausibly **maintained by selection**, because the product TCBQ
   is a potent alkylating agent and slow release lets the reductase PcpD
   capture it before it escapes the active site (PMID:23676275, from the same
   group as the "poorly functioning enzyme" paper). A low kcat can therefore be
   evidence *of* selection rather than of its absence. Both readings fit the
   same measured number, so the gene review records the question rather than
   asserting either.
3. **A second, independent failure mode surfaced repeatedly**: fold-level
   InterPro/PANTHER transfer predicting a superfamily's prevalent chemistry
   rather than the member's own reaction (`atzA` → C-N hydrolase, `dhlA` →
   epoxide hydrolase). This is the `ASSAY_TO_FUNCTION` proximity problem in a
   sequence-inference guise, and is tracked in
   [`OVER_ANNOTATION_PATTERNS.md`](OVER_ANNOTATION_PATTERNS.md) category 3.

A fourth observation cuts across the set: **`tfdA`, `pcpB` and `dhlA` have no
experimental GO annotation at all** despite decades of genetics, crystallography
and mechanistic enzymology. Their only MF annotations are Rhea- or EC-derived
IEAs. That is a curation gap, not an annotation error, but it means the
xenobiotic-degradation corner of GO looks electronically annotated when it is
actually among the best-characterized enzymology in the database.

## Proposed GO changes

1. **Move `xref: RHEA:25968 {source="skos:narrowMatch"}` from `GO:0016616` to
   `GO:0004090`**, matching the existing treatment of `RHEA:31891`. Needs an
   issue number for `term_tracker_item`.
2. **Add a QC check** flagging any Rhea xref on a term whose EC xref ends in
   `.-`. Nine reactions affected today, so it is cheap to add and keep green.
   Candidate as a SPARQL violation query or a Soufflé rule.
3. **Restore `GO:0018830`** (gamma-hexachlorocyclohexane dehydrochlorinase
   activity) under `GO:0016848 carbon-halide lyase activity`, mapped to
   `RHEA:45480`. Proposed in `genes/SPHIU/linA/linA-ai-review.yaml`.
4. **Audit the remaining 159 terms from #28108** against current UniProt
   catalytic activity records and Rhea mappings.
5. **Review the other eight grouping-term Rhea xrefs** (`GO:0008241`,
   `GO:0016712`) to decide between re-pointing and new specific terms.

Items 1–3 are per-term edits; 4–5 are audits that should precede further
obsoletions.

## Next steps

1. **Pilot the first two signals** (pathway membership, substrate in a
   metabolome) across all GO terms with a Rhea exactMatch, to size the
   candidate pool before any manual curation. Blocked on checking network
   reachability for MetaCyc/KEGG/BRENDA from the working environment; UniProt
   and PubMed are reachable, `rest.rhea-db.org` currently is not.
2. **Calibrate against the 15 labelled obsoletions** above.
3. **Extend the counter-example set** with a few category 2 and 3 cases, which
   are currently unrepresented. `GO:0047949` glutarate-semialdehyde
   dehydrogenase and `GO:0052812` PI(3,4)P2 5-kinase are candidates.
4. **Open the GO issues** for proposed changes 1–3.

## Relationship to existing projects

- [`ASSAY_TO_FUNCTION.md`](ASSAY_TO_FUNCTION.md) — the direct conceptual
  parent. That project asks whether an experiment's *readout* is proximal to
  the gene product's own activity; this one asks whether its *substrate* is
  one the gene product ever encounters. Both are properties of the assay that
  GO evidence codes do not record, and both produce annotations that are
  literally true and functionally misleading. The pipelines are complementary:
  `ASSAY_TO_FUNCTION` mines cached publications for readout classes behind
  PMID-backed annotations, while this project scores reactions and substrates
  behind Rhea/EC-derived IEAs — the electronic annotations that
  `ASSAY_TO_FUNCTION`'s publication-mining approach cannot reach by
  construction.
- [`OVER_ANNOTATION_PATTERNS.md`](OVER_ANNOTATION_PATTERNS.md) — category 2
  ("overly broad enzymatic terms") is exactly what a grouping-class Rhea xref
  generates, and category 3 ("domain-based predictions without validation") is
  the `atzA`/`dhlA` fold-transfer pattern.
- [`ENZYME_SPECIFICITY.md`](ENZYME_SPECIFICITY.md) — overlapping concern with
  substrate-level precision in catalytic annotation.
