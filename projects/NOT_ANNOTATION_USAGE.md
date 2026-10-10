---
title: "NOT Annotation Usage Audit"
maturity: IN_PROGRESS
last_reviewed: "2026-10-04"
tags: [EVALUATION, PIPELINE]
species: [human, rat, ARATH, SCHPO]
genes: [FGFR4, AGR2, GCH1, HSPA6, CRY2, Ghr, CLV3, GID1A, chk1]
---
# NOT Annotation Usage Audit

**Bottom line:** GOA contains 10,622 NOT annotations on 7,408 gene products. The
qualifier is used in very different ways. Its strongest use is to negate a molecular
function, typically a catalytic activity that a pseudoenzyme or a diverged family
member has lost (3,405 rows), backed by an assay or by a PAINT loss-of-function call
(IKR). Its weakest use is to negate a process from an expression or perturbation readout,
above all "NOT response to <chemical/stimulus>". There are 490 such rows, and the most
common evidence for them is IEP, an expression pattern, which by itself cannot show that
a gene product lacks a function. In total 169 NOTs rest on IEP alone, and another 627 are
TAIR computational (`RCA`) localization calls. UniProt CAUTION notes track the useful
end: 27% of reviewed proteins with an MF NOT carry a CAUTION, 19.5% with loss-of-activity
wording, against 7% and 1.9% for proteins whose NOTs are only to processes or
locations. Our own gene reviews have so far ACCEPTed 266 of 342 NOTs they met
(77.8%), so the
review guidance needs a rule for judging NOTs, not just positive annotations.

We started this because the FGFR4 review met `NOT involved_in response to bile acid`
(GO:1903412, IMP, PMID:19085950). The paper's only negative result is that bile acid did
not change FGFR4 protein level, which is an expression observation, not evidence that
FGFR4 lacks a function. FGFR4 acts in the FGF19 signal that bile acid induces, which is
already captured as negative regulation of bile acid biosynthesis.

## Question

How is the NOT qualifier used across GO, which uses are sound, and how do NOTs relate
to UniProt CAUTION notes? The working hypothesis is that NOT is meaningful mainly for
molecular functions (a gene product demonstrably lacks an activity its family or domain
predicts), and much weaker for "response to" and other process terms, where the
negative readout is usually an expression or phenotype null.

## Methods

All code and data are in [NOT_ANNOTATION_USAGE/](NOT_ANNOTATION_USAGE/).

1. `fetch_not_annotations.py` downloads every NOT-qualified annotation from QuickGO
   (one download per `NOT|<relation>`), filling GO labels from the local GO build.
   Output: `not_annotations.tsv` (10,622 rows, fetched 2026-10-01).
2. `fetch_caution_notes.py` fetches the UniProt CAUTION text for each of the 7,369
   distinct UniProt accessions. Output: `not_accessions_caution.tsv`.
3. `analyze_not_usage.py` assigns each negated term to a coarse category by GO
   is_a/part_of ancestry (first match wins: signaling, defense/immune response, other
   response to stimulus, regulation, development, metabolism, localization for BP;
   catalytic, transporter, transducer, transcription regulator, binding for MF). It
   flags CAUTION notes with loss-of-activity wording, and joins the actions our gene
   reviews gave negated rows. It writes `not_annotations_classified.tsv`,
   `review_negated_actions.tsv` and [RESULTS.md](NOT_ANNOTATION_USAGE/RESULTS.md).

Re-run all three scripts in order with `uv run python <script>`; RESULTS.md is
regenerated each time.

## Findings so far

Full tables are in [RESULTS.md](NOT_ANNOTATION_USAGE/RESULTS.md).

- **MF NOTs dominate and are mostly sound in kind.**
  - 4,664 rows (44%) negate a molecular function, 3,405 of them catalytic activities.
  - These rest on IBA (1,336), IDA (752) and IKR (608). IKR is PAINT's explicit
    "key residues lost" call, mostly peptidase and kinase activities.
  - Only 2 NOTs negate bare `protein binding`.
- **NOTs to processes are where the qualifier drifts.**
  - The process NOTs are spread across regulation (796), metabolism (1,010),
    development (423) and "response to" terms.
  - Defense and immune responses (234 rows) are mostly IDA from antimicrobial assays.
    These are close to activity negatives ("this peptide does not kill Gram-negative
    bacteria") and are defensible.
  - The other 490 "response to" rows (chemicals, abiotic stimuli, hormones) are led
    by IEP (138 rows). They typically record that expression did not change.
- **IEP NOTs are the clearest misuse.**
  - 169 rows, 82% of them to "response to" terms.
  - Submitted mainly by AgBase (65), UniProt (44), TAIR (33) and FlyBase (17).
- **Computational NOTs exist.** 627 `RCA` NOTs, all TAIR localization calls (for
  example "NOT located_in cytosol", "NOT located_in Golgi apparatus").
- **CAUTION notes align with MF NOTs, not process NOTs.**

  | Reviewed proteins | Any CAUTION | Loss-of-activity CAUTION |
  |---|---|---|
  | with an MF NOT (1,838) | 27.0% | 19.5% |
  | with only BP/CC NOTs (2,388) | 7.0% | 1.9% |

  The reverse direction (CAUTION notes describing lost activity on proteins with no MF
  NOT) is covered by Query B of the [UniProt CAUTION Note project](UNIPROT_CAUTION_NOTE.md).
- **Our reviews have been deferential.**
  - 342 negated rows in 222 reviews: 266 ACCEPT, 28 UNDECIDED, 24 KEEP_AS_NON_CORE,
    21 REMOVE and 3 MARK_AS_OVER_ANNOTATED.
  - The worklist in RESULTS.md lists the 9 reviewed NOTs to non-defense "response to"
    terms or with IEP evidence. FGFR4 and AGR2 are already REMOVE.
  - Not every item on that list is bad. CRY2 NOT photoreactive repair records that a
    photolyase homolog lacks repair activity, which is a process-shaped statement of an
    MF negative and is sound.

## Proposed guidance (draft, for discussion)

1. A NOT is strongest when it negates a **molecular function** a reader would otherwise
   predict from family, domain or orthology, with assay or key-residue evidence.
2. A NOT to a **process** should be judged by asking whether the gene product was shown
   unable to do the process's work. "Expression did not change" never meets this bar,
   so IEP-only process NOTs should be REMOVE in reviews.
3. "NOT response to X" is acceptable only when the gene product was tested for a direct
   role, for example a receptor shown not to bind and transduce X. It is not acceptable
   for an expression or abundance null.
4. Where a CAUTION note records lost activity and no MF NOT exists, propose an MF NOT
   (see [Top-Nots](TOP_NOTS.md)).

## Related projects

- [Top-Nots](TOP_NOTS.md): mines REMOVE decisions in our reviews for NOTs worth
  proposing (the forward direction).
- [UniProt CAUTION Note](UNIPROT_CAUTION_NOTE.md): CAUTION notes as a worklist for
  over-annotation, including CAUTIONs with no matching NOT.
- [Over-annotation patterns](OVER_ANNOTATION_PATTERNS.md).

---
# STATUS

Updated 2026-10-04.

- [x] Download all GOA NOT annotations (QuickGO, 10,622 rows)
- [x] Fetch UniProt CAUTION notes for NOT-annotated proteins (7,369 accessions)
- [x] Classify NOTs by aspect, relation, evidence, assigning group and term category
- [x] Join with the actions our reviews took on negated rows
- [x] Fix the FGFR4 `NOT response to bile acid` review reasoning (human/FGFR4)
- [ ] Review the reviewed-NOT worklist with the draft guidance
      ([#3982](https://github.com/ai4curation/ai-gene-review/issues/3982)):
  - [ ] human/GCH1 GO:0032496 response to lipopolysaccharide (IEP, KEEP_AS_NON_CORE)
  - [ ] human/HSPA6 GO:0070370 cellular heat acclimation (IMP, ACCEPT)
  - [ ] ARATH/CLV3 GO:0002221 pattern recognition receptor signaling pathway (IEP, ACCEPT)
  - [ ] ARATH/GID1A GO:0009739 response to gibberellin (IGI, KEEP_AS_NON_CORE)
  - [ ] rat/Ghr GO:0046898 response to cycloheximide (ISO, KEEP_AS_NON_CORE)
  - [ ] SCHPO/chk1 GO:0006281 DNA repair (EXP, ACCEPT)
  - [x] human/FGFR4 GO:1903412 response to bile acid (IMP, REMOVE)
  - [x] human/AGR2 GO:0034976 response to endoplasmic reticulum stress (IMP, REMOVE)
  - [x] human/CRY2 GO:0000719 photoreactive repair (IDA, ACCEPT; sound MF-shaped negative)
- [ ] Sample and read IEP NOTs by group (AgBase, UniProt, TAIR, FlyBase) to estimate the
      misuse rate
- [ ] Inspect the 627 TAIR `RCA` localization NOTs (how were they generated?)
- [ ] Agree the guidance above and add it to the annotation-reviewer skill and CLAUDE.md
- [ ] Cross-check: proteins with a loss-of-activity CAUTION but no MF NOT

# NOTES

## 2026-10-04

Revalidated the nine reviews represented in the reviewed-NOT worklist against the
current YAML. FGFR4, AGR2 and human CRY2 remain completed; the remaining six
rows still need a guidance-driven re-read alongside the broader sampling and
CAUTION-note cross-checks, now tracked in
[#3982](https://github.com/ai4curation/ai-gene-review/issues/3982).

## 2026-10-01

Project started from the FGFR4 review (FGFR signaling module work). First full
download and classification run; see Findings. The "response to stimulus" bucket was
initially too broad because GO places signaling pathways under cellular response to
stimulus, and defense responses from antimicrobial assays behave like activity
negatives; both are now separate categories.
