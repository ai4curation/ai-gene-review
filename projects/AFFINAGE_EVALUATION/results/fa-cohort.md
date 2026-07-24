# FA cohort — Affinage as a deep-research *input* to AIGR (22 Fanconi-anemia genes)

Earlier cohorts ([pilot](summary.md), [batch2–4](hard-cases.md), [narrative-vs-go](narrative-vs-go.md))
evaluated Affinage's **GO grounding** against finished AIGR reviews. This cohort asks the
*forward* question the project page flagged as "weaker than it first appears": **used as a
deep-research source, does Affinage's narrative actually improve a curated review?**

The 22 Fanconi-anemia complementation-group genes (A–W) were freshly reviewed de-novo, then
each Affinage record was read against its review and its cited primary papers folded in
conservatively (see per-gene files in [`fa-cohort/`](fa-cohort/)). Unlike the earlier
cohorts this measures **net curation value**, not just exact-GO-id overlap.

## Headline

- **59 primary papers** surfaced by Affinage's narrative were incorporated into the reviews
  (as `references` + verbatim `supported_by`), anchoring annotations that had rested on the
  UniProt/deep-research file or high-throughput interactome hits.
- **13 NEW GO annotations** across **10 genes** were added for genuinely well-evidenced
  functions the GOA-grounded review had missed or held only in prose.
- **0 existing AIGR curation decisions reversed.** Affinage's evidence never overturned an
  action; it strengthened or extended.
- **Affinage's own `mechanism_profile` GO layer was imported 0 times** — the coarse/wrong-branch
  pattern from the earlier cohorts reproduced on every gene (details below).

So the two layers behave exactly as the [narrative-vs-go](narrative-vs-go.md) analysis
predicted: **the narrative is a strong, citation-dense research input; the GO layer is not
directly usable.** The novelty here is quantifying the *narrative's* upside — it is real.

## Per-gene outcome

Run dates 2026-06-09→11. "New" = new GO annotations added; "Papers" = Affinage-surfaced
primary papers folded into the review.

| Gene | FA | Affinage self-eval | Papers | New | What Affinage genuinely added (or the key disagreement) |
|------|----|--------------------|:-----:|:---:|---------------------------------------------------------|
| [FANCA](fa-cohort/FANCA.md) | A | win (29) | 2 | **2** | Intrinsic ssDNA binding + RAD52-like single-strand-annealing (SSA) activity — a real biochemistry gap, now non-core (GO:0003697, GO:0045002) |
| [FANCB](fa-cohort/FANCB.md) | B | — (8) | 2 | 0 | Anchored HR/SCE annotations; MF mistagged "catalytic activity acting on protein" (FANCB is non-catalytic) |
| [FANCC](fa-cohort/FANCC.md) | C | win (34) | 3 | 0 | Its own cited separation-of-function mutants *reinforce* AIGR's non-core call on the redox/PKR roles |
| [FANCD2](fa-cohort/FANCD2.md) | D2 | win (60) | 6 | **3** | Fork protection/restart (→core), R-loop suppression, mitochondrial pool (GO:0031297, GO:0062176, GO:0005739) |
| [FANCE](fa-cohort/FANCE.md) | E | win (10) | 4 | 0 | 4 primary adaptor/bridge-to-FANCD2 papers; MF over-reach "catalytic activity acting on protein" |
| [FANCF](fa-cohort/FANCF.md) | F | win (9) | 2 | 0 | The FANCF flexible-adaptor primary paper (PMID:15262960); blurs regulation-of / plant-meiosis into function |
| [FANCG](fa-cohort/FANCG.md) | G | win (30) | 2 | **1** | HR DSB-repair (Ser7 D1-D2-G-X3 complex) as a discrete annotation (GO:0000724) |
| [FANCI](fa-cohort/FANCI.md) | I | win (43) | 3 | 0 | Primary DNA-binding / FANCD2-monoub-stimulation papers; wrong-branches FANCI as a protein-acting enzyme |
| [FANCL](fa-cohort/FANCL.md) | L | win (22) | 1 | **1** | ELF-domain ubiquitin binding (GO:0043130); AIGR's RING-E3 term beats Affinage's generic ligase parent |
| [FANCM](fa-cohort/FANCM.md) | M | win (41) | 3 | **1** | Translocase-dependent ATR/Chk1 checkpoint signaling (GO:0000077) |
| [BRIP1](fa-cohort/BRIP1.md) | J | win (38) | 1 | 0 | No BACH1-bZIP collision this time; coarse layer mislabels the catalytic helicase "molecular adaptor" |
| [PALB2](fa-cohort/PALB2.md) | N | win (35) | 2 | **1** | ChAM nucleosome binding (GO:0031491) + the primary KEAP1 paper; layer says histone-vs-nucleosome / catalytic-on-DNA |
| [RAD51C](fa-cohort/RAD51C.md) | O | win (42) | 5 | **1** | ICL repair / FANCO founding paper (GO:0036297); does **not** claim RAD51C is itself an endonuclease — AIGR's over-annotation of GO:0008821 stands |
| [SLX4](fa-cohort/SLX4.md) | P | win (57) | 3 | **1** | SLX4-complex SUMO E3 ligase (GO:0061665, non-core); narrative correctly frames SLX4 as nuclease-dead scaffold |
| [ERCC4](fa-cohort/ERCC4.md) | Q | **tie / CAUTION** (40) | 1 | 0 | The FANCQ disease-defining paper (PMID:23623386); CAUTION warranted vs the GO layer, not the (sound) prose |
| [RAD51](fa-cohort/RAD51.md) | R | win (45) | 3 | 0 | Foundational Gupta/Radding 1997 recombinase paper; RNA/TERRA left as documented candidate |
| [UBE2T](fa-cohort/UBE2T.md) | T | win (35) | 1 | 0 | Anchored polyubiquitination; declines the large single-study cancer-substrate / RNF8 / NER set |
| [XRCC2](fa-cohort/XRCC2.md) | U | win (29) | 5 | **1** | ICL repair / FANCU (GO:0036297); narrative *reinforces* "not an ATP-dependent damage sensor" |
| [RFWD3](fa-cohort/RFWD3.md) | W | win (17) | 2 | 0 | Two RFWD3-focused fork-remodeling papers; p53/MDM2 correctly non-core |
| [BRCA1](fa-cohort/BRCA1.md) | S | **tie / CAUTION** (22) | 3 | 0 | Anchored HR/E3/H2AK127 terms; CAUTION warranted vs GO layer (spurious RNA-catalytic term), not the prose; ~70 protein-binding REMOVEs untouched |
| [BRCA2](fa-cohort/BRCA2.md) | D1 | win (27) | 3 | 0 | 3 canonical primary papers (Yang 2002 structure, fork protection, single-molecule RAD51 loading) replacing indirect support |
| [MAD2L2](fa-cohort/MAD2L2.md) | V | win (47) | 2 | **1** | Shieldin-independent fork-resection protection (GO:0110027) + the previously-uncited FANCV disease paper |

## Cross-cutting findings

**1. The GO layer's failure mode on this cohort is systematic: adaptors/scaffolds get typed as
enzymes.** The FA pathway is rich in non-catalytic structural subunits, and Affinage's
`mechanism_profile` mislabels them almost every time — `catalytic activity, acting on a
protein` for the non-catalytic adaptors FANCB / FANCE / FANCI, `catalytic activity, acting on
DNA` for FANCA / PALB2 / SLX4, `structural molecule activity` for FANCA / FANCG, generic
`ligase activity` for the specific RING-E3s FANCL / RFWD3 / BRCA1, and — inverting the error —
`molecular adaptor activity` for the *catalytic* helicase BRIP1/FANCJ. None were importable;
AIGR's curated MF terms are correct in every case. This is the earlier cohorts' "collapses to a
general parent" finding, sharpened: on structural subunits it doesn't just generalize, it lands
on the **wrong catalytic branch**.

**2. The narrative, by contrast, is a high-value research input.** 59 primary papers and 13 new
annotations came out of it, including one genuine biochemistry gap (FANCA's intrinsic SSA
activity) and several functions the review had only in prose (FANCD2 fork protection, FANCM ATR
checkpoint, RAD51C/XRCC2 ICL-repair, MAD2L2 fork-resection control). Critically, several times
Affinage's *own cited evidence reinforced* an AIGR non-core/over-annotation call it superficially
seemed to challenge (FANCC redox mutants; RAD51C not-an-endonuclease; XRCC2 not-a-damage-sensor;
SLX4 nuclease-dead). This is the opposite of the redundancy the project page worried about — on a
genuinely hard, adaptor-heavy pathway the narrative pulled real, checkable literature the
GOA-seeded review had not surfaced.

**3. The two `tie`/CAUTION records (ERCC4, BRCA1) were correctly flagged, but for the GO layer,
not the prose.** In both, the narrative was factually sound and PMID-dense with no fabrication or
mis-attribution; the `tie` tracked the coarse/wrong-branch GO grounding (a spurious RNA-catalytic
term on BRCA1; RNA-binding + parent-level catalytic terms on ERCC4) plus a breadth-over-focus
narrative. So the self-eval gate is a useful "scrutinize the GO layer" signal, not a
narrative-reliability verdict.

**4. Net curation effect.** Every FA review is now better sourced (mixed-maturity deep-research /
interactome support replaced by primary literature) and 10 are functionally more complete, with
no decision weakened. Used the way this project endorses — narrative-as-input, GO-layer-ignored —
Affinage delivered measurable value on the cohort where it should have been most redundant with
AIGR's own deep-research step.

## Caveats

- Conservative incorporation bar: single-study / non-human / regulation-of and consequence-of
  claims were deliberately **not** annotated (documented per gene). A more aggressive pass would
  add more but at lower confidence.
- "New annotation" counts are additive to already-thorough de-novo reviews, so they *understate*
  Affinage's narrative coverage — most of what it says was already annotated.
- Exact-GO-id non-import is a design choice here (the layer is coarse), not a claim that every
  Affinage GO term is wrong — many are true *ancestors* of the curated term.
